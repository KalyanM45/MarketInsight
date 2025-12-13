from pydantic import BaseModel

class PromptObject(BaseModel):
    content: str
    id: str
    role: str

class RequestObject(BaseModel):
    prompt: PromptObject
    threadId: str
    responseId: str