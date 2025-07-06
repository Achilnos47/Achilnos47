# 🎯 Market Intelligence MCP System
## Comprehensive Reddit Sentiment + Google News + App Store Intelligence

A powerful market intelligence system that combines Reddit sentiment analysis, Google News trends, and app store competitor data through Model Context Protocol (MCP) servers.

### 🚀 What This System Does

This MCP setup provides:
- **Reddit Sentiment Analysis**: Monitor discussions across multiple subreddits
- **Google News Trend Monitoring**: Track market signals and news sentiment
- **App Store Intelligence**: Analyze competitor apps and user reviews
- **Integrated Analysis**: Combine all data sources for comprehensive market insights

Perfect for:
- Market validation for startups
- Investment research and trend analysis
- Product-market fit assessment
- Competitive intelligence
- Crypto market analysis

### 📦 Quick Start

1. **Install MCP Servers**:
   ```bash
   ./install_mcp_servers.sh
   ```

2. **Set Up API Keys**:
   ```bash
   cp .env.template .env
   # Edit .env with your actual API keys
   ```

3. **Configure Claude Desktop**:
   - Copy `claude_desktop_config.json` to your Claude Desktop config location
   - Update with your actual API keys

4. **Start Analysis**:
   ```bash
   python3 sample_analysis_scripts.py
   ```

### 🔧 Required API Keys

#### Essential (Free Tier Available):
- **Reddit API**: Get from [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
- **Tavily Search**: Get from [tavily.com](https://tavily.com) (free tier)

#### Optional (For Enhanced Features):
- **Google Play Developer API**: For Android app analysis
- **Apple App Store Connect**: For iOS app analysis
- **OpenAI API**: For enhanced sentiment analysis

### 🎪 Analysis Workflows

#### 1. Startup Market Validation
```
1. Reddit Sentiment Analysis
   → Analyze r/startups, r/entrepreneur, industry subreddits
   → Extract pain points and opportunities
   → Market size indicators

2. News Trend Correlation
   → Google News industry trends
   → Cross-reference with Reddit discussions
   → Identify market timing signals

3. Competitive App Analysis
   → App store competitor review
   → Feature gaps and opportunities
   → Pricing strategy analysis
```

#### 2. Investment Research
```
1. Reddit Finance Communities
   → r/wallstreetbets, r/investing sentiment
   → Retail investor behavior tracking
   → Options flow discussions

2. Financial News Integration
   → Institutional vs retail sentiment
   → Market catalyst identification
   → Regulatory impact analysis

3. Contrarian Analysis
   → Sentiment divergence opportunities
   → Market timing indicators
   → Risk assessment
```

#### 3. Product Market Fit
```
1. Customer Pain Analysis
   → Reddit product discussions
   → Feature requests and complaints
   → Unmet needs identification

2. Market Timing Assessment
   → Industry trend analysis
   → Regulatory environment
   → Technology adoption patterns

3. Competitive Positioning
   → App store competitor tracking
   → Feature evolution analysis
   → Market gap identification
```

### 📊 Sample Analysis Prompts

#### For Startup Validation:
```
"Analyze r/startups and r/entrepreneur for discussions about 'AI productivity tools' in the last 30 days. Provide sentiment scores, pain points, and market opportunities."
```

#### For Investment Research:
```
"Compare Reddit sentiment in r/wallstreetbets with Google News coverage for Tesla (TSLA) over the last 2 weeks. Identify any sentiment divergences."
```

#### For Product Analysis:
```
"Analyze the top 10 business intelligence apps in both iOS and Android stores. Create a feature comparison matrix and identify market gaps."
```

### 🛠️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Reddit MCP    │    │  Google News    │    │  App Store MCP  │
│   Servers       │    │     MCP         │    │    Servers      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   Claude with   │
                    │   MCP Support   │
                    └─────────────────┘
                                 │
                    ┌─────────────────┐
                    │  Market Intel   │
                    │   Analysis      │
                    └─────────────────┘
```

### 📈 Advanced Features

#### Data Pipeline Enhancement:
- Automated monitoring schedules
- Sentiment shift alerts
- Multi-source correlation analysis
- Historical trend tracking

#### Custom Analysis Tools:
- Combined sentiment scoring
- Competitor tracking dashboards
- Market timing optimization
- Risk assessment frameworks

#### Reporting & Visualization:
- Weekly intelligence reports
- Real-time monitoring dashboards
- Client-ready deliverables
- Trend visualization tools

### 🔧 Troubleshooting

#### Common Issues:
1. **Reddit API Rate Limits**: Implement request throttling
2. **Missing MCP Servers**: Some may need manual installation
3. **API Key Configuration**: Ensure all keys are properly set

#### Performance Tips:
- Batch multiple queries together
- Cache frequently accessed data
- Use appropriate time ranges for analysis
- Monitor API usage quotas

### 📚 Files Overview

- `market-intelligence-setup.md`: Complete setup guide
- `claude_desktop_config.json`: MCP server configuration
- `install_mcp_servers.sh`: Automated installer script
- `.env.template`: API key configuration template
- `sample_analysis_scripts.py`: Analysis workflow examples

### 🎯 Use Cases

#### For Startups:
- Market validation and sizing
- Competitive landscape analysis
- Product-market fit assessment
- Launch timing optimization

#### For Investors:
- Sentiment-based investment signals
- Retail vs institutional divergence
- Market timing indicators
- Risk assessment tools

#### For Product Managers:
- Feature gap identification
- Customer pain point analysis
- Competitive positioning
- Market trend monitoring

#### For Consultants:
- Client market intelligence
- Industry trend analysis
- Competitive research
- Investment thesis development

### 🚀 Getting Started

1. **Prerequisites**: Ensure you have Python 3.8+ and uvx installed
2. **Installation**: Run the setup script
3. **Configuration**: Add your API keys
4. **Testing**: Use sample analysis scripts
5. **Customization**: Adapt workflows to your needs

### 💡 Next Steps

Once set up, you can:
- Create custom analysis workflows
- Set up automated monitoring
- Build client reporting systems
- Integrate with existing tools
- Scale for enterprise use

---

**Ready to revolutionize your market intelligence?** 🎪

This system gives you the same data access as major consulting firms at a fraction of the cost. Perfect for startups, investors, and anyone who needs deep market insights.

*Get started today and turn data into actionable market intelligence!*
