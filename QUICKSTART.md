# 🚀 Quick Start Guide
## Get Market Intelligence Running in 15 Minutes

### Step 1: Install Prerequisites (2 minutes)

```bash
# Install uvx (Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify installation
uvx --version
```

### Step 2: Set Up API Keys (5 minutes)

1. **Reddit API** (Essential - Free):
   - Go to https://www.reddit.com/prefs/apps
   - Click "Create App" → Select "script"
   - Note your `client_id` and `client_secret`

2. **Tavily Search** (Essential - Free tier):
   - Go to https://tavily.com
   - Sign up for free account
   - Get your API key

3. **Configure Environment**:
   ```bash
   cp .env.template .env
   # Edit .env with your API keys
   ```

### Step 3: Install MCP Servers (5 minutes)

```bash
# Run the automated installer
./install_mcp_servers.sh

# If some servers fail, try manual installation:
pip install praw textblob requests beautifulsoup4
```

### Step 4: Configure Claude Desktop (2 minutes)

1. Copy your Claude Desktop config location:
   - **macOS**: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
   - **Linux**: `~/.config/claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

2. Update the config:
   ```bash
   # Replace the template values with your actual API keys
   cp claude_desktop_config.json ~/.config/claude/claude_desktop_config.json
   ```

3. **Restart Claude Desktop**

### Step 5: Test Your Setup (1 minute)

```bash
# Generate sample analysis templates
python3 sample_analysis_scripts.py
```

### 🎯 Ready to Analyze!

Copy this prompt into Claude Desktop:

```
# Startup Market Validation Analysis - AI Productivity Tools

## 1. Reddit Sentiment Analysis
Please analyze r/startups and r/entrepreneur for discussions about "AI productivity tools" in the last 30 days:
- Overall sentiment score
- Top 5 most mentioned pain points
- Emerging trends and opportunities
- Market size indicators

## 2. News Trend Correlation
Search Google News for "AI productivity startups" from the last 30 days:
- Identify top 5 trending topics
- Compare with Reddit community sentiment
- Highlight any market timing signals

## 3. Market Validation Summary
Based on all data sources:
- Market validation score (1-10)
- Key opportunities identified
- Recommended next steps
```

### 🔧 Common Issues & Quick Fixes

#### Problem: MCP servers not showing up
**Solution**: 
- Restart Claude Desktop
- Check config file path
- Verify API keys are correct

#### Problem: Reddit API errors
**Solution**:
- Check client_id/secret are correct
- Verify Reddit app is "script" type
- Check rate limits

#### Problem: News search not working
**Solution**:
- Verify Tavily API key
- Check internet connection
- Try different search terms

### 💡 Quick Tips

1. **Start Simple**: Use basic Reddit + News analysis first
2. **Test Incrementally**: Add one MCP server at a time
3. **Monitor Rate Limits**: Don't exceed API quotas
4. **Save Results**: Copy analysis results to files

### 🎪 Next Steps

Once basic setup works:
- Add app store analysis servers
- Create custom analysis workflows
- Set up automated monitoring
- Build client reporting systems

---

**Total Setup Time: ~15 minutes**

*You're now ready to access the same market intelligence as major consulting firms!*