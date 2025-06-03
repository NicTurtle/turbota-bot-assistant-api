from pydantic import BaseModel

class UserMessage(BaseModel):
    user_id: int
    message: str
    reply: str
