from database import database

# Dependency to get the MongoDB collection
def get_KF_collection():
    KF_collection = database["KeyFrame_Embeddings"]
    return KF_collection