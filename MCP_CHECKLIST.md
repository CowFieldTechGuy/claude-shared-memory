# MCP Server Installation Checklist 🚀

## ✅ Already Configured
- [x] **n8n** - Workflow automation (API key configured)
- [x] **filesystem** - File system access (directories configured)
- [x] **memory** - Memory persistence
- [x] **time** - Time/date utilities
- [x] **fetch** - HTTP fetch capabilities
- [x] **docker** - Docker container management
- [x] **sequential** - Sequential thinking
- [x] **magic** - Magic UI

## 🔧 Configured but Need Credentials
- [ ] **postgresql** - Need: database URL
- [ ] **sqlite** - Need: database path setup
- [ ] **github** - Need: GitHub token
- [ ] **slack** - Need: Slack bot token
- [ ] **notion** - Need: Notion API key
- [ ] **google-sheets** - Need: Google credentials JSON
- [ ] **web-search** - Need: search engine API key
- [ ] **aws** - Need: AWS credentials
- [ ] **kubernetes** - Need: kubeconfig setup

## 🌟 High Priority to Add
- [ ] **@sinco-lab/mcp-youtube-transcript** - YouTube transcripts (no API key needed!)
- [ ] **@timlukahorstmann/mcp-weather** - Weather forecasts (Need: AccuWeather API)
- [ ] **mcp-obsidian** - Obsidian vault integration (Need: vault path)
- [ ] **mcp-server-discord** - Discord bot integration (Need: bot token)
- [ ] **systemprompt-mcp-reddit** - Reddit search (Need: Reddit API)

## 🎮 Fun & Creative Additions
- [ ] **@cablate/mcp-google-map** - Google Maps (Need: Maps API key)
- [ ] **mcp-server-code-runner** - Execute code in multiple languages
- [ ] **openai-mcp-server** - OpenAI integration (Need: API key)
- [ ] **figma-developer-mcp** - Figma integration (Need: API key)
- [ ] **@anaisbetts/mcp-youtube** - YouTube downloader

## 🚀 Ready to Use (No Setup Required)
- [ ] **playwright** - Browser automation (already in config!)
- [ ] **puppeteer** - Browser automation (already in config!)
- [ ] **context7** - Context management (already in config!)

## 📝 Installation Commands

### Quick install for priority servers:
```bash
# YouTube Transcript (no API needed!)
npm install -g @sinco-lab/mcp-youtube-transcript

# Code Runner (no API needed!)
npm install -g mcp-server-code-runner
```

### Update MCP config:
```bash
# Edit the config file
nano ~/.config/claude-code/mcp_servers.json
```

### Test MCP connection:
```bash
# Use MCP inspector
npx @modelcontextprotocol/inspector ~/.config/claude-code/mcp_servers.json
```

## 🎯 Tomorrow's Goals
1. Install YouTube transcript server (easy win!)
2. Set up Code Runner for multi-language execution
3. Configure Obsidian if you use it
4. Look into Discord integration for fun
5. Consider weather API for utility

---
*Last updated: January 19, 2025*
*Config location: ~/.config/claude-code/mcp_servers.json*