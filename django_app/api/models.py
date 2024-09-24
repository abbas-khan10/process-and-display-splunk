from django.db import models
from pydantic import BaseModel

class DocumentMigration(BaseModel):
    successful: bool = None
    reason:str = None

class Attachment(BaseModel):
    clinicalType: str = None
    mimeType: str = None
    sizeBytes: int = None

class Payload(BaseModel):
    payload: Attachment = None

class Message(BaseModel):
    documentMigration: DocumentMigration = None
    payload: Payload = None



