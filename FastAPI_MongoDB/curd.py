import schemas
from typing import List

# Create
async def create_image_document(document: schemas.Image_Document, collection):
    document_dict = document.model_dump()
    result = await collection.insert_one(document_dict)
    return str(result.inserted_id)



# READ: Get document by Metadata.Image_Path
async def get_image_document_by_path(path: str, collection):
    document = await collection.find_one({"Metadata.Image_Path": path})
    return document



# READ: Get all document 
async def get_all_image_document(collection) -> List[schemas.Image_Document]:
    documents_cursor = collection.find()
    documents = await documents_cursor.to_list(length=None)  # Convert cursor to list
    return documents



# UPDATE: Update a document by Metadata.Image_Path
async def update_image_document(path: str, update_document: schemas.Update_Image_Document, collection):
    # Convert the Pydantic model to a dictionary and filter out None values
    update_document_dict = update_document.model_dump()
    filtered_dict = {key: value for key, value in update_document_dict.items() if value is not None}
    print(filtered_dict)
    # Remove the Fields_to_unset from the dictionary since it shouldn't be part of the $set operation
    fields_to_unset = filtered_dict.pop('Fields_to_unset', None)

    # Create the $set part of the update query
    update_query = {"$set": filtered_dict}

    # If there are fields to unset, add $unset to the update query
    if fields_to_unset:
        unset_query = {"$unset": {field: "" for field in fields_to_unset}}
        update_query.update(unset_query)

    # Perform the update operation in MongoDB
    result = await collection.update_one({"Metadata.Image_Path": path}, update_query)
    
    # Return whether any documents were modified
    return result.modified_count > 0



# DELETE: Delete a document by Metadata.Image_Path
async def delete_document(path: str, collection):
    result = await collection.delete_one({"Metadata.Image_Path": path})
    return result.deleted_count > 0