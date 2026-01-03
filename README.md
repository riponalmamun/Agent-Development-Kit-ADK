# Agent Development Kit (ADK)

A progressive learning project for building AI agents with Google's Gemini API, from basic conversational agents to tool-enabled intelligent systems.

## 📁 Project Structure

```
AGENT DEVELOPMENT KIT/
├── 1-Basic-Agent/
│   └── greeting_agent/
│       ├── agent.py
│       ├── requirements.txt
│       ├── .env
│       └── venv/
├── 2-tool-agent/
│   └── tool_agent/
│       ├── agent.py
│       ├── requirements.txt
│       ├── .env
│       └── venv/
```

## 🎯 Overview

This repository contains a step-by-step guide to building AI agents:

### 1. Basic Agent (Greeting Agent)
A foundational conversational agent that demonstrates:
- Basic chat interactions
- API integration with Google Gemini
- Simple prompt engineering
- Environment variable management

### 2. Tool Agent
An advanced agent that showcases:
- Function calling capabilities
- Tool integration and execution
- Multi-step reasoning
- External API interactions

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AGENT-DEVELOPMENT-KIT
   ```

2. **Choose an agent to start with**
   ```bash
   cd 1-Basic-Agent/greeting_agent
   # or
   cd 2-tool-agent/tool_agent
   ```

3. **Set up virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**
   
   Create a `.env` file in the agent directory:
   ```env
   GOOGLE_GENAI_USER=your_email@example.com
   GOOGLE_API_KEY=your_api_key_here
   ```

6. **Run the agent**
   ```bash
   python agent.py
   ```

## 🔧 Configuration

Each agent requires the following environment variables:

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_GENAI_USER` | Your Google account email | Yes |
| `GOOGLE_API_KEY` | Your Google Gemini API key | Yes |

## 📚 Learning Path

**Recommended progression:**

1. **Start with Basic Agent** - Learn fundamental concepts of agent interaction
2. **Move to Tool Agent** - Understand advanced capabilities and tool integration
3. **Experiment and extend** - Build your own custom agents with specific tools

## 🛠️ Technologies Used

- Python 3.x
- Google Gemini API
- python-dotenv (for environment management)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new agent examples
- Improve documentation
- Fix bugs
- Suggest new features

## 📝 License

This project is open source and available under the MIT License.

## ⚠️ Security Notes

- **Never commit `.env` files** - They contain sensitive API keys
- **Never share your API keys** publicly
- Use `.gitignore` to exclude sensitive files from version control

## 📞 Support

If you encounter any issues or have questions:
- Open an issue in the repository
- Check Google's Gemini API documentation
- Review the example code in each agent directory

## 🎓 Additional Resources

- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [AI Agent Design Patterns](https://ai.google.dev/gemini-api/docs/function-calling)

---

**Happy Agent Building! 🤖**
