# Market Insight

An AI-powered stock market analysis platform that provides comprehensive financial data and intelligent insights through a conversational interface.

## Overview

Market Insight leverages advanced AI agents to deliver real-time stock market information, financial analysis, and investment insights. The platform combines the power of LangChain and OpenAI's language models with Yahoo Finance data to create an intelligent assistant for stock market research.

## Technology Stack

**Backend:**
- FastAPI for high-performance API endpoints
- LangChain & LangGraph for AI agent orchestration
- OpenAI GPT models for intelligent responses
- YFinance for financial data retrieval
- Langfuse for observability and tracing

**Frontend:**
- Modern React-based interface
- Real-time streaming responses
- Responsive design for all devices

## Getting Started

### Prerequisites
- Python 3.x
- Node.js (for frontend)
- OpenAI API key

### Installation

1. Clone the repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables in `.env` file
4. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```
5. Run the backend server:
   ```bash
   python main.py
   ```
6. Run the frontend development server:
   ```bash
   cd frontend
   npm run dev
   ```
7. Access the API at `http://localhost:8000` and frontend at `http://localhost:5173`

## Project Structure

```
MarketInsight/
├── components/     # AI agent configuration
├── utils/          # Tools and utilities
├── config/         # Configuration files
├── frontend/       # React frontend application
└── main.py         # FastAPI server entry point
```

## API Capabilities

The platform provides 16 specialized tools for comprehensive stock analysis:
- Stock price tracking
- Historical data analysis
- Financial statements (Balance Sheet, Income Statement, Cash Flow)
- Company information and ratios
- Dividend and split history
- Ownership and holder data
- Insider transactions
- Analyst recommendations
- Company ticker lookup