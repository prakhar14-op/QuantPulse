import { Link } from 'react-router-dom';
import { BarChart3, TrendingUp, Brain, Shield, Zap, Target } from 'lucide-react';
import { Card } from '@/app/components/ui/card';

export function HomePage() {
  const features = [
    {
      icon: Brain,
      title: 'AI-Driven Predictions',
      description: 'Advanced machine learning algorithms analyze market patterns and technical indicators.'
    },
    {
      icon: TrendingUp,
      title: 'Real-Time Analytics',
      description: 'Get instant insights on NSE stocks with live price updates and sentiment analysis.'
    },
    {
      icon: Shield,
      title: 'Secure & Reliable',
      description: 'Bank-grade security with 99.9% uptime for uninterrupted market monitoring.'
    },
    {
      icon: Zap,
      title: 'Lightning Fast',
      description: 'Sub-second response times for critical trading decisions and market movements.'
    },
    {
      icon: Target,
      title: 'Precision Accuracy',
      description: 'High-confidence predictions backed by comprehensive market data analysis.'
    },
    {
      icon: BarChart3,
      title: 'Advanced Charts',
      description: 'Interactive visualizations with technical indicators and pattern recognition.'
    }
  ];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative py-20 px-6 overflow-hidden">
        {/* Background gradient effect */}
        <div className="absolute inset-0 bg-gradient-to-b from-blue-600/10 via-transparent to-transparent"></div>
        
        <div className="max-w-6xl mx-auto text-center relative">
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-600/10 border border-blue-600/20 mb-6">
            <span className="size-2 rounded-full bg-blue-600 animate-pulse"></span>
            <span className="text-sm text-blue-400">AI-Powered Stock Market Intelligence</span>
          </div>
          
          <h1 className="text-5xl md:text-7xl mb-6 bg-gradient-to-r from-zinc-100 to-zinc-400 bg-clip-text text-transparent">
            QuantPulse India
          </h1>
          
          <p className="text-xl md:text-2xl text-zinc-400 mb-4">
            Next-Generation Stock Market Predictions
          </p>
          
          <p className="text-lg text-zinc-500 mb-12 max-w-3xl mx-auto">
            Harness the power of artificial intelligence to predict market movements on NSE stocks. 
            Get real-time sentiment analysis, AI-driven predictions, and actionable insights.
          </p>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <Link
              to="/signup"
              className="px-8 py-4 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-lg transition-colors flex items-center gap-2"
            >
              <Zap className="size-5" />
              Get Started Free
            </Link>
            <Link
              to="/dashboard"
              className="px-8 py-4 bg-zinc-800 hover:bg-zinc-700 text-zinc-100 rounded-lg text-lg transition-colors flex items-center gap-2"
            >
              <TrendingUp className="size-5" />
              View Dashboard
            </Link>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-3 gap-8 mt-20 max-w-2xl mx-auto">
            <div>
              <div className="text-3xl text-blue-500 mb-2">85%</div>
              <div className="text-sm text-zinc-500">Prediction Accuracy</div>
            </div>
            <div>
              <div className="text-3xl text-emerald-500 mb-2">1000+</div>
              <div className="text-sm text-zinc-500">NSE Stocks Tracked</div>
            </div>
            <div>
              <div className="text-3xl text-amber-500 mb-2">24/7</div>
              <div className="text-sm text-zinc-500">Market Monitoring</div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 px-6 bg-zinc-900/30">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl mb-4 text-zinc-100">
              Powered by Advanced Technology
            </h2>
            <p className="text-lg text-zinc-400 max-w-2xl mx-auto">
              Our platform combines cutting-edge AI with comprehensive market data to deliver 
              actionable insights for Indian stock markets.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {features.map((feature, index) => {
              const Icon = feature.icon;
              return (
                <Card key={index} className="p-6 bg-zinc-900 border-zinc-800 hover:border-zinc-700 transition-colors">
                  <div className="p-3 rounded-lg bg-blue-600/10 w-fit mb-4">
                    <Icon className="size-6 text-blue-500" />
                  </div>
                  <h3 className="text-xl mb-2 text-zinc-100">{feature.title}</h3>
                  <p className="text-zinc-400">{feature.description}</p>
                </Card>
              );
            })}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-6">
        <div className="max-w-4xl mx-auto text-center">
          <Card className="p-12 bg-gradient-to-br from-blue-600 to-blue-800 border-0">
            <h2 className="text-3xl md:text-4xl mb-4 text-white">
              Ready to Transform Your Trading?
            </h2>
            <p className="text-lg text-blue-100 mb-8 max-w-2xl mx-auto">
              Join thousands of traders using QuantPulse India to make smarter, 
              data-driven decisions in the Indian stock market.
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <Link
                to="/signup"
                className="px-8 py-4 bg-white hover:bg-zinc-100 text-blue-600 rounded-lg text-lg transition-colors"
              >
                Start Free Trial
              </Link>
              <Link
                to="/contact"
                className="px-8 py-4 bg-blue-700 hover:bg-blue-800 text-white rounded-lg text-lg transition-colors"
              >
                Contact Sales
              </Link>
            </div>
          </Card>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-8 px-6 border-t border-zinc-800">
        <div className="max-w-6xl mx-auto text-center text-zinc-500 text-sm">
          <p>&copy; 2026 QuantPulse India. All rights reserved.</p>
          <p className="mt-2">
            Market data is simulated for demonstration purposes. Not financial advice.
          </p>
        </div>
      </footer>
    </div>
  );
}
