from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Literal
from datetime import datetime



class User_data(BaseModel):

    user_id: int
    user_name: str = Field(..., min_length=1)
    user_email: Optional[str] = None
    user_joined_date: datetime


class RAG_setting(BaseModel):

    bot_name: str = Field(..., min_length=1)
    llm_model: Literal['gpt-4', 'claude-3', 'gemini-pro']
    temperature: float = Field(ge=0.0, le=2.0)

class RAGDocument(BaseModel):
    id: int
    title: str
    content: str

class ProjectWorkspace(BaseModel):

    project_id: str =Field(..., min_length=1)
    project_name: str = Field(..., min_length=1)


    default_user_data: User_data
    default_RAG_setting: RAG_setting
    document: List[RAGDocument] = Field(default_factory=List)
    created_at: datetime    = Field(default_factory=datetime.now)


    model_config = ConfigDict (

        
        extra='forbid',      
        strict=True,       
        frozen=True  
    )