"""
Stock Data Router

This module provides endpoints for fetching real-time NSE stock data
using the Yahoo Finance API (via yfinance library).

Yahoo Finance uses a special format for NSE stocks:
- NSE stocks have ".NS" suffix (e.g., RELIANCE → RELIANCE.NS)
- BSE stocks have ".BO" suffix (e.g., RELIANCE → RELIANCE.BO)

This router handles the conversion automatically.
"""

from fastapi import APIRouter, HTTPException, Path
from datetime import datetime
import yfinance as yf

# Create router for stock-related endpoints
router = APIRouter(
    prefix="/stock",       # All routes will be prefixed with /stock
    tags=["Stocks"],       # Group in API docs under "Stocks"
)


def convert_to_nse_symbol(symbol: str) -> str:
    """
    Convert a plain stock symbol to Yahoo Finance NSE format.
    
    Yahoo Finance requires NSE stocks to have ".NS" suffix.
    This function handles the conversion and ensures uppercase.
    
    Args:
        symbol: Plain stock symbol (e.g., "RELIANCE", "TCS")
    
    Returns:
        Yahoo Finance formatted symbol (e.g., "RELIANCE.NS")
    """
    # Remove any existing suffix and whitespace
    clean_symbol = symbol.strip().upper()
    
    # Remove .NS or .BO if already present (to avoid double suffix)
    if clean_symbol.endswith(".NS") or clean_symbol.endswith(".BO"):
        clean_symbol = clean_symbol[:-3]
    
    # Add NSE suffix
    return f"{clean_symbol}.NS"


def format_large_number(value: float) -> str:
    """
    Format large numbers in Indian style (Lakhs, Crores).
    
    Args:
        value: Number to format
    
    Returns:
        Formatted string (e.g., "₹16.8L Cr" for market cap)
    """
    if value is None:
        return "N/A"
    
    if value >= 1e12:  # Lakh Crores
        return f"₹{value / 1e12:.2f}L Cr"
    elif value >= 1e9:  # Thousands Crores
        return f"₹{value / 1e7:.0f} Cr"
    elif value >= 1e7:  # Crores
        return f"₹{value / 1e7:.2f} Cr"
    elif value >= 1e5:  # Lakhs
        return f"₹{value / 1e5:.2f}L"
    else:
        return f"₹{value:,.0f}"


def format_volume(volume: int) -> str:
    """
    Format trading volume in millions/thousands.
    
    Args:
        volume: Trading volume
    
    Returns:
        Formatted string (e.g., "12.5M")
    """
    if volume is None:
        return "N/A"
    
    if volume >= 1e6:
        return f"{volume / 1e6:.2f}M"
    elif volume >= 1e3:
        return f"{volume / 1e3:.1f}K"
    else:
        return str(volume)


@router.get("/{symbol}")
def get_stock_data(
    symbol: str = Path(..., pattern=r"^[A-Z0-9\.]+$", description="NSE stock symbol")
):
    """
    Fetch real-time stock data for an NSE stock.
    
    This endpoint:
    1. Converts the symbol to Yahoo Finance format (adds .NS suffix)
    2. Fetches current price, volume, market cap from Yahoo Finance
    3. Calculates day change percentage
    4. Returns clean JSON response
    
    Args:
        symbol: NSE stock symbol (e.g., "RELIANCE", "TCS", "INFY")
    
    Returns:
        dict: Stock data including price, change, volume, market cap
    
    Raises:
        HTTPException: 404 if symbol is invalid or data unavailable
    """
    try:
        # Convert to Yahoo Finance NSE format
        yf_symbol = convert_to_nse_symbol(symbol)
        
        # Create a Ticker object for the stock
        # This is the main yfinance interface for fetching data
        ticker = yf.Ticker(yf_symbol)
        
        # Fetch the stock info dictionary
        # This contains all available data about the stock
        info = ticker.info
        
        # Check if we got valid data
        # If the symbol is invalid, info will be nearly empty
        if not info or info.get("regularMarketPrice") is None:
            raise HTTPException(
                status_code=404,
                detail={
                    "error": "Stock not found",
                    "message": f"Could not find data for symbol '{symbol}'. Please check if it's a valid NSE stock symbol.",
                    "hint": "Try symbols like RELIANCE, TCS, INFY, HDFCBANK"
                }
            )
        
        # Extract current price
        # regularMarketPrice is the most recent trading price
        current_price = info.get("regularMarketPrice", 0)
        
        # Extract previous close price for calculating change
        previous_close = info.get("regularMarketPreviousClose", 0)
        
        # Calculate price change and percentage
        price_change = current_price - previous_close if previous_close else 0
        change_percent = (price_change / previous_close * 100) if previous_close else 0
        
        # Extract volume (number of shares traded today)
        volume = info.get("regularMarketVolume", 0)
        
        # Extract market capitalization
        market_cap = info.get("marketCap", None)
        
        # Get the stock's full name
        company_name = info.get("longName") or info.get("shortName") or symbol.upper()
        
        # Build the response object
        response = {
            "symbol": symbol.upper(),
            "yahooSymbol": yf_symbol,
            "companyName": company_name,
            "currentPrice": round(current_price, 2),
            "previousClose": round(previous_close, 2),
            "change": round(price_change, 2),
            "changePercent": round(change_percent, 2),
            "volume": volume,
            "volumeFormatted": format_volume(volume),
            "marketCap": market_cap,
            "marketCapFormatted": format_large_number(market_cap) if market_cap else "N/A",
            "currency": info.get("currency", "INR"),
            "exchange": info.get("exchange", "NSE"),
            "timestamp": datetime.now().isoformat(),
            "marketState": info.get("marketState", "UNKNOWN"),  # REGULAR, PRE, POST, CLOSED
        }
        
        return response
        
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
        
    except Exception as e:
        # Handle any unexpected errors gracefully
        # Log the error for debugging (in production, use proper logging)
        print(f"Error fetching stock data for {symbol}: {str(e)}")
        
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Failed to fetch stock data",
                "message": f"An error occurred while fetching data for '{symbol}'. Please try again later.",
                # Removed technicalDetails to prevent info leakage
            }
        )
