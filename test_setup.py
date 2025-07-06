#!/usr/bin/env python3
"""
Market Intelligence MCP Setup Test & Validation
Tests the complete setup and provides status report
"""

import os
import json
import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a file exists and report status"""
    if Path(filepath).exists():
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - NOT FOUND")
        return False

def check_executable(filepath, description):
    """Check if a file is executable"""
    if Path(filepath).exists() and os.access(filepath, os.X_OK):
        print(f"✅ {description}: {filepath} - EXECUTABLE")
        return True
    else:
        print(f"❌ {description}: {filepath} - NOT EXECUTABLE")
        return False

def check_env_template():
    """Check if .env.template has required keys"""
    try:
        with open('.env.template', 'r') as f:
            content = f.read()
        
        required_keys = [
            'REDDIT_CLIENT_ID',
            'REDDIT_CLIENT_SECRET',
            'TAVILY_API_KEY'
        ]
        
        missing_keys = []
        for key in required_keys:
            if key not in content:
                missing_keys.append(key)
        
        if not missing_keys:
            print("✅ Environment template: All required keys present")
            return True
        else:
            print(f"❌ Environment template: Missing keys: {', '.join(missing_keys)}")
            return False
            
    except FileNotFoundError:
        print("❌ Environment template: .env.template not found")
        return False

def check_claude_config():
    """Check if Claude Desktop config is valid JSON"""
    try:
        with open('claude_desktop_config.json', 'r') as f:
            config = json.load(f)
        
        if 'mcpServers' in config:
            server_count = len(config['mcpServers'])
            print(f"✅ Claude Desktop config: Valid JSON with {server_count} MCP servers")
            return True
        else:
            print("❌ Claude Desktop config: Missing 'mcpServers' section")
            return False
            
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"❌ Claude Desktop config: Error - {e}")
        return False

def check_python_imports():
    """Check if required Python packages are available"""
    required_packages = [
        'datetime',
        'json',
        'typing',
        'os'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if not missing_packages:
        print("✅ Python dependencies: All required packages available")
        return True
    else:
        print(f"❌ Python dependencies: Missing packages: {', '.join(missing_packages)}")
        return False

def generate_next_steps():
    """Generate personalized next steps based on setup status"""
    print("\n🎯 NEXT STEPS")
    print("=" * 50)
    
    print("\n1. SET UP API KEYS:")
    print("   - Copy: cp .env.template .env")
    print("   - Edit .env with your actual API keys")
    print("   - Get Reddit API keys: https://www.reddit.com/prefs/apps")
    print("   - Get Tavily API key: https://tavily.com")
    
    print("\n2. INSTALL MCP SERVERS:")
    print("   - Run: ./install_mcp_servers.sh")
    print("   - If errors occur, try manual installation")
    
    print("\n3. CONFIGURE CLAUDE DESKTOP:")
    print("   - Copy claude_desktop_config.json to Claude's config location")
    print("   - Update API keys in the config")
    print("   - Restart Claude Desktop")
    
    print("\n4. TEST YOUR SETUP:")
    print("   - Run: python3 sample_analysis_scripts.py")
    print("   - Copy generated analysis templates to Claude Desktop")
    print("   - Test with simple Reddit analysis first")
    
    print("\n5. SCALE UP:")
    print("   - Add more MCP servers")
    print("   - Create custom analysis workflows")
    print("   - Set up automated monitoring")

def main():
    """Main test function"""
    print("🚀 MARKET INTELLIGENCE MCP SETUP TEST")
    print("=" * 50)
    
    # Test core files
    print("\n📁 CORE FILES CHECK")
    print("-" * 30)
    
    checks = [
        check_file_exists('README.md', 'Main README'),
        check_file_exists('QUICKSTART.md', 'Quick Start Guide'),
        check_file_exists('market-intelligence-setup.md', 'Detailed Setup Guide'),
        check_file_exists('claude_desktop_config.json', 'Claude Desktop Config'),
        check_file_exists('.env.template', 'Environment Template'),
        check_executable('install_mcp_servers.sh', 'Installation Script'),
        check_file_exists('sample_analysis_scripts.py', 'Sample Analysis Scripts')
    ]
    
    # Test configuration files
    print("\n⚙️ CONFIGURATION CHECK")
    print("-" * 30)
    
    config_checks = [
        check_env_template(),
        check_claude_config(),
        check_python_imports()
    ]
    
    # Summary
    total_checks = len(checks) + len(config_checks)
    passed_checks = sum(checks) + sum(config_checks)
    
    print(f"\n📊 SETUP STATUS SUMMARY")
    print("=" * 50)
    print(f"Total Checks: {total_checks}")
    print(f"Passed: {passed_checks}")
    print(f"Failed: {total_checks - passed_checks}")
    
    if passed_checks == total_checks:
        print("🎉 SETUP COMPLETE! All checks passed.")
        print("You're ready to start market intelligence analysis!")
    else:
        print("⚠️  SETUP INCOMPLETE. Please fix the issues above.")
    
    # Always show next steps
    generate_next_steps()
    
    # Sample analysis prompt
    print("\n🎪 SAMPLE ANALYSIS PROMPT")
    print("=" * 50)
    print("Copy this into Claude Desktop to test your setup:")
    print()
    print("```")
    print("# Quick Market Intelligence Test")
    print("# Please analyze r/startups for discussions about 'AI tools' in the last 7 days:")
    print("# - Overall sentiment score")
    print("# - Top 3 most mentioned topics")
    print("# - Any emerging trends")
    print("```")
    
    return passed_checks == total_checks

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)