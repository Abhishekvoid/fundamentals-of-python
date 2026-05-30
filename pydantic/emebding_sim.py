import asyncio
import uuid
from pydantic import BaseModel, Field, field_validator, model_validator, ValidationError

# pydantic models

class DocumentRequest(BaseModel):
    documentId: str = Field(default_factory=lambda: str(uuid.uuid4()))
    filename: str = Field(..., min_length = 1)
    content: str = Field(min_length = 10)

    
    @field_validator("filename")
    @classmethod
    def validate_filename(cls, value:str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("filename cannot be empty")
        return value
    
    @field_validator("content")
    @classmethod
    def validate_content(cls, value:str) -> str:
        value = value.strip()
        if len(value) < value:
            raise ValueError("content must be atleast 20 character long")
        return value
    
class DocumentResult(BaseModel):
    document_id: str
    filename: str
    status: str
    message: str
    
semaphore = asyncio.Semaphore(3)

async def fake_api_call(filename: str) -> None:
    
    await asyncio.sleep(1)
    print(f"API porceesed: {filename}")
    
async def fake_db_write(filename: str) -> None:
    await asyncio.sleep(0.8)
    print(f"DB write done: {filename}")
    

async def fake_embedding_generation(filename: str) -> None:
    await asyncio.sleep(1.2)
    print(f"Embedding generated: {filename}")
    
async def process_document(doc: DocumentRequest) -> DocumentRequest:
    
    async with semaphore:
        
        print(f" started processing: {doc.filename}")
        
        await asyncio.gather(
              fake_api_call(doc.filename),
            fake_db_write(doc.filename),
            fake_embedding_generation(doc.filename),
        )
        
        print(f"Finished processing: {doc.filename}")

        return DocumentResult(
            document_id=doc.document_id,
            filename=doc.filename,
            status="success",
            message="Document processed successfully",
        )
        
async def main():
    raw_docs = [
        {"filename": f"doc_{i}.txt",
         "content": f"this is sample content for document number {i}."
         }
        for i in range(1, 11)
        
    ]
    
    documents = []
    for raw_doc in raw_docs:
        try:
            doc = DocumentRequest(**raw_doc)
            documents.append(doc)
        except ValidationError as e:
            print("validation error:", e)
    
    
    tasks = [process_document(doc) for doc in documents]
    results = await asyncio.gather(*tasks)
    
    print("\nFinal Results:")
    for result in results:
        print(result.model_dump())


if __name__ == "__main__":
    asyncio.run(main())
            
        