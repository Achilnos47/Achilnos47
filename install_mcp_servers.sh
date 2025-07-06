#!/bin/bash

# Market Intelligence MCP Server Installation Script
# This script installs all required MCP servers for market intelligence analysis

echo "🚀 Market Intelligence MCP Server Installation"
echo "=============================================="

# Check if uvx is installed
if ! command -v uvx &> /dev/null; then
    echo "❌ uvx is not installed. Please install it first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

echo "✅ uvx is installed"

# Function to install MCP server
install_mcp_server() {
    local server_name=$1
    local package_name=$2
    
    echo "📦 Installing $server_name..."
    
    if uvx install "$package_name"; then
        echo "✅ $server_name installed successfully"
    else
        echo "❌ Failed to install $server_name"
        echo "   You may need to install it manually or check if the package exists"
    fi
}

# Install Reddit-related MCP servers
echo ""
echo "🔴 Installing Reddit Analysis Servers"
echo "------------------------------------"
install_mcp_server "WSB Analyst" "wsb-analyst"
install_mcp_server "Reddit MCP" "reddit-mcp"

# Install News and Search MCP servers
echo ""
echo "📰 Installing News & Search Servers"
echo "-----------------------------------"
install_mcp_server "Google News MCP" "google-news-mcp"
install_mcp_server "Tavily Search MCP" "tavily-search"
install_mcp_server "Web Search MCP" "web-search-mcp"

# Install App Store Analysis servers
echo ""
echo "📱 Installing App Store Analysis Servers"
echo "----------------------------------------"
install_mcp_server "App Insight MCP" "app-insight-mcp"

# Install Sentiment Analysis servers
echo ""
echo "🧠 Installing Sentiment Analysis Servers"
echo "----------------------------------------"
install_mcp_server "Sentiment Analysis MCP" "sentiment-analysis-mcp"

# Alternative installations (if the above don't work)
echo ""
echo "🔄 Alternative Installation Methods"
echo "====================================="
echo "If any of the above installations failed, try these alternatives:"
echo ""
echo "For Reddit analysis:"
echo "  pip install praw textblob"
echo "  uvx install --python python3.11 reddit-mcp"
echo ""
echo "For news analysis:"
echo "  pip install requests beautifulsoup4 feedparser"
echo "  uvx install --python python3.11 google-news-mcp"
echo ""
echo "For sentiment analysis:"
echo "  pip install transformers torch textblob vaderSentiment"
echo ""

# Check installations
echo ""
echo "🔍 Checking Installations"
echo "========================="

servers_to_check=(
    "wsb-analyst"
    "reddit-mcp"
    "google-news-mcp"
    "tavily-search"
    "web-search-mcp"
    "app-insight-mcp"
    "sentiment-analysis-mcp"
)

for server in "${servers_to_check[@]}"; do
    if uvx list | grep -q "$server"; then
        echo "✅ $server is installed"
    else
        echo "❌ $server is not installed"
    fi
done

echo ""
echo "📋 Next Steps"
echo "============="
echo "1. Set up your API keys in the .env file (copy from .env.template)"
echo "2. Update the claude_desktop_config.json with your actual API keys"
echo "3. Restart Claude Desktop to load the new MCP servers"
echo "4. Test the setup with the sample analysis scripts"
echo ""
echo "🎯 Your Market Intelligence MCP system is ready!"