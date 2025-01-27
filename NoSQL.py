import pandas as pd
from pymongo import MongoClient

# Correct file path
file_path = r"E:\SLTC\ICE\3rd Year\6th Sem\Big data\Project\dataset.csv"

# Read the dataset
data = pd.read_csv(file_path)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['big_data_project']
collection = db['energy_data']

# Insert data into MongoDB
collection.insert_many(data.to_dict('records'))

print(f"Inserted {collection.count_documents({})} records into MongoDB!")