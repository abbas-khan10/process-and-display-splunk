from django.db import models
from pydantic import BaseModel

class DocumentMigration(BaseModel):
    successful: bool = False
    reason:str = ''

class Attachment(BaseModel):
    clinicalType: str = ''
    mimeType: str = ''
    sizeBytes: int = 0

class Payload(BaseModel):
    payload: Attachment = ''

class Message(BaseModel):
    documentMigration: DocumentMigration = None
    payload: Payload = None



