from django.db import models
from pydantic import BaseModel

class DocumentMigration(BaseModel):
    successful: bool = None



