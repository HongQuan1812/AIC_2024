from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

# Load the MongoDB connection string from the environment variable MONGODB_URI
CONNECTION_STRING = os.environ['MONGODB_URI']

# Create a MongoDB client
client = AsyncIOMotorClient(CONNECTION_STRING)

database = client["AIC_2024"]
