from django.db import models
from pydantic import BaseModel

class DocumentMigration(BaseModel):
    successful: bool = None
    reason:str = None

class Attachment(BaseModel):
    clinical_type: str = None
    mine_type: str = None
    size_bytes: int = None

class Payload(BaseModel):
    payload: Attachment = None

class Message(BaseModel):
    document_migration: DocumentMigration = None
    payload: Payload = None



