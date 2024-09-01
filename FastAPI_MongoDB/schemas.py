from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional

# Define the Image_Document model
class Image_Document(BaseModel):
    Metadata: Optional[Dict[str, Any]] = Field(
        default=None, title="The field is a dict containing metadata such as Image_Path, Objects appearing in Image"
    )
    Embedding: Optional[Dict[str, Any]] = Field(
        default=None, title="The field is a dict containing types of embeddings such as CLIP_Embeddings, ..."
    )

    class Config:
        from_attributes = True

# Define the Update_Image_Document model that extends Image_Document
class Update_Image_Document(Image_Document):
    Fields_to_unset: Optional[List[str]] = Field(
        default=None, title="List of fields to unset in the document"
    )


