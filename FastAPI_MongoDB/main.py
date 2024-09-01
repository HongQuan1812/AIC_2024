# main.py
from fastapi import FastAPI, HTTPException, Depends
from typing import List
import schemas
import curd
from collection import get_KF_collection

app = FastAPI()

# Create a new document
@app.post("/image_documents/create_one", response_model=str)
async def create_new_image_document(path: str, document: schemas.Image_Document, collection=Depends(get_KF_collection)):
    returned_document = await curd.get_image_document_by_path(path, collection)
    if returned_document:
        raise HTTPException(status_code=400, detail="Document is already exist")
    document_id = await curd.create_image_document(document, collection)
    return document_id

# Read all documents 
@app.get("/image_documents/read_all", response_model=List[schemas.Image_Document])
async def read_all_image_document(collection=Depends(get_KF_collection)):
    returned_documents = await curd.get_all_image_document(collection)
    if returned_documents:
        return returned_documents
    raise HTTPException(status_code=404, detail="Documents not found")

# Read documents by Metadata.Path
@app.get("/image_documents/read_one", response_model=schemas.Image_Document)
async def read_image_document_by_path(path: str, collection=Depends(get_KF_collection)):
    returned_documents = await curd.get_image_document_by_path(path, collection)
    if returned_documents:
        return returned_documents
    raise HTTPException(status_code=404, detail="Documents not found")

# Update a document by Metadata.Path
@app.put("/image_documents/update_one", response_model=bool)
async def update_existing_image_document(path: str, update_document: schemas.Update_Image_Document, collection=Depends(get_KF_collection)):
    returned_documents = await curd.get_image_document_by_path(path, collection)
    if returned_documents:
        updated = await curd.update_image_document(path, update_document, collection)
        if updated:
            return True
        else:
            return False
    else:
        raise HTTPException(status_code=404, detail="Document not found")
    
    
# Delete a document by Metadata.Path
@app.delete("/image_documents/delete_one", response_model=bool)
async def delete_existing_document(path: str, collection=Depends(get_KF_collection)):
    returned_documents = await curd.get_image_document_by_path(path, collection)
    if returned_documents:
        deleted = await curd.delete_document(path, collection)
        if deleted:
            return True
    else:
        raise HTTPException(status_code=404, detail="Document not found")
