# Market Intelligence MCP Setup Guide
## Reddit Sentiment Analysis + Google News Trends + App Store Competitor Data

### 🎯 System Overview
This setup creates a powerful market intelligence system that combines:
- **Reddit sentiment analysis** across multiple subreddits
- **Google News trend monitoring** for market signals
- **Competitor app store intelligence** for product insights

### 📦 Required MCP Servers

#### 1. Reddit Data Collection & Sentiment Analysis

**WSB Analyst MCP Server**
```json
{
  "mcpServers": {
    "wsb-analyst": {
      "command": "uvx",
      "args": ["run", "wsb-analyst"],
      "env": {
        "REDDIT_CLIENT_ID": "your_reddit_client_id",
        "REDDIT_CLIENT_SECRET": "your_reddit_secret"
      }
    }
  }
}
```

**General Reddit MCP Server**
```json
{
  "mcpServers": {
    "reddit-mcp": {
      "command": "uvx", 
      "args": ["run", "reddit-mcp"],
      "env": {
        "REDDIT_CLIENT_ID": "your_reddit_client_id",
        "REDDIT_CLIENT_SECRET": "your_reddit_secret",
        "REDDIT_USER_AGENT": "MarketIntel/1.0"
      }
    }
  }
}
```

#### 2. News Trends & Market Signals

**Google News MCP Server**
```json
{
  "mcpServers": {
    "google-news": {
      "command": "uvx",
      "args": ["run", "google-news-mcp"]
    }
  }
}
```

**Tavily Search MCP (for comprehensive news)**
```json
{
  "mcpServers": {
    "tavily-search": {
      "command": "uvx",
      "args": ["run", "tavily-search"],
      "env": {
        "TAVILY_API_KEY": "your_tavily_api_key"
      }
    }
  }
}
```

#### 3. App Store Competitor Intelligence

**AppInsight MCP Server**
```json
{
  "mcpServers": {
    "app-insight": {
      "command": "uvx",
      "args": ["run", "app-insight-mcp"],
      "env": {
        "APP_STORE_CONNECT_KEY": "your_key",
        "GOOGLE_PLAY_API_KEY": "your_google_play_key"
      }
    }
  }
}
```

### 🛠️ Installation Steps

#### Step 1: Set Up Reddit API Access
1. Go to https://www.reddit.com/prefs/apps
2. Create a new application (script type)
3. Note your `client_id` and `client_secret`

#### Step 2: Set Up Additional API Keys
```bash
# Tavily for enhanced search (free tier available)
# Sign up at https://tavily.com

# Google Play Developer API (if analyzing Android apps)
# Apple App Store Connect API (if analyzing iOS apps)
```

#### Step 3: Configure Claude Desktop
Add the MCP server configurations to your Claude Desktop `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "wsb-analyst": {
      "command": "uvx",
      "args": ["run", "wsb-analyst"],
      "env": {
        "REDDIT_CLIENT_ID": "your_reddit_client_id",
        "REDDIT_CLIENT_SECRET": "your_reddit_secret"
      }
    },
    "reddit-general": {
      "command": "uvx",
      "args": ["run", "reddit-mcp"],
      "env": {
        "REDDIT_CLIENT_ID": "your_reddit_client_id", 
        "REDDIT_CLIENT_SECRET": "your_reddit_secret"
      }
    },
    "tavily-search": {
      "command": "uvx",
      "args": ["run", "tavily-search"],
      "env": {
        "TAVILY_API_KEY": "your_tavily_key"
      }
    },
    "app-insight": {
      "command": "uvx",
      "args": ["run", "app-insight-mcp"],
      "env": {
        "GOOGLE_PLAY_API_KEY": "your_google_play_key"
      }
    }
  }
}
```

### 🎪 Market Intelligence Workflows

#### Workflow 1: Startup Market Validation
```
1. Reddit Sentiment Analysis
   → Analyze discussions in relevant subreddits (r/startups, r/entrepreneur, industry-specific)
   → Extract sentiment trends around problem spaces
   → Identify pain points and opportunities

2. News Trend Correlation  
   → Search Google News for industry trends
   → Cross-reference with Reddit discussions
   → Identify emerging market signals

3. Competitive App Analysis
   → Analyze competitor apps in app stores
   → Review ratings, features, user feedback
   → Identify market gaps and opportunities
```

#### Workflow 2: Investment/Trend Research
```
1. WSB & Finance Subreddit Analysis
   → Monitor stock discussions and sentiment
   → Track meme stock trends and retail investor behavior
   → Analyze options flow discussions

2. Financial News Integration
   → Search for company/sector news
   → Correlate news sentiment with Reddit discussions
   → Identify divergences between institutional and retail sentiment

3. Fintech App Competitive Analysis
   → Monitor fintech app store performance
   → Analyze user reviews for feature requests
   → Track competitive positioning
```

#### Workflow 3: Product Market Fit Analysis
```
1. Product Category Reddit Research
   → Search relevant subreddits for product discussions
   → Analyze user complaints and feature requests
   → Identify underserved market segments

2. Market News & Trend Analysis
   → Monitor industry news for market changes
   → Track regulatory changes affecting the space
   → Identify market timing opportunities

3. Direct Competitor App Intelligence
   → Analyze competitor app store presence
   → Monitor review sentiment and feature evolution
   → Identify competitive advantages/disadvantages
```

### 📊 Sample Analysis Prompts

#### Reddit Sentiment Analysis
```
"Analyze the last 100 posts in r/startups mentioning 'AI tools' and provide:
1. Overall sentiment score
2. Most common pain points mentioned
3. Emerging trends in AI tool adoption
4. Potential market opportunities identified"
```

#### News Trend Correlation
```
"Search Google News for 'business intelligence startups' in the last 30 days and:
1. Identify the top 5 trending topics
2. Correlate with Reddit discussions in r/datascience and r/entrepreneur  
3. Highlight any divergent sentiments between news and community discussions"
```

#### App Store Competitive Intelligence
```
"Analyze the top 10 business intelligence apps in both iOS and Android app stores:
1. Feature comparison matrix
2. User review sentiment analysis
3. Pricing strategy analysis
4. Identify feature gaps and opportunities"
```

### 🚀 Advanced Integration Ideas

#### Data Pipeline Enhancement
- **Set up automated monitoring**: Schedule regular sentiment checks
- **Create alert system**: Notify when sentiment shifts significantly
- **Build trend correlation**: Cross-reference all three data sources

#### Custom Analysis Tools
- **Sentiment scoring**: Combine Reddit + News sentiment for market mood
- **Competitive tracking**: Monitor specific competitors across all channels
- **Market timing**: Identify optimal launch windows based on trend data

#### Reporting & Visualization
- **Weekly market intelligence reports**: Automated summaries
- **Real-time dashboard**: Live sentiment and trend monitoring
- **Client deliverables**: Professional reports for consulting clients

### 🔧 Troubleshooting Tips

#### Common Issues
1. **Reddit API rate limits**: Implement request throttling
2. **News search quotas**: Rotate between different news APIs
3. **App store data access**: Some data may require premium APIs

#### Performance Optimization
- **Batch requests**: Combine multiple queries where possible
- **Cache results**: Store frequently accessed data locally
- **Prioritize sources**: Focus on highest-value data sources first

### 📈 Scaling Your Market Intelligence

#### For Small Clients
- Focus on specific subreddits and local news
- Manual analysis with AI assistance
- Weekly/bi-weekly reporting cadence

#### For Larger Clients  
- Full multi-platform monitoring
- Real-time alerts and monitoring
- Daily insights and trend analysis
- Custom competitive intelligence dashboards

This setup gives you a powerful foundation for market intelligence consulting. The combination of Reddit sentiment, news trends, and app store data provides comprehensive market insights that most startups and small businesses can't access on their own.