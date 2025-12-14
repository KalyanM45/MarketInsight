import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from langchain_core.messages import SystemMessage, HumanMessage
from config.config import RequestObject
from MarketInsight.components.agent import agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://market-insight.vercel.app"],  # Update with your Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat")
async def chat(request: RequestObject):
    config = {'configurable': {'thread_id': request.threadId}}

    def generate():
        for token, _ in agent.stream(
            {
                'messages': [
                    SystemMessage(content="You are a stock market analyst. You have the ability to get the realtime stock market data and balance sheet, income statement, cash flow statement, historical data, and other financial data of the ticker from Yahoo Finance."),
                    HumanMessage(content=request.prompt.content)
                ]
            },
            stream_mode='messages',
            config=config
        ):
            yield token.content
    
    return StreamingResponse(generate(), media_type='text/event-stream',
        headers={
            'cache-control': 'no-cache, no-transform', 
            'connection': 'keep-alive'
        })

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)