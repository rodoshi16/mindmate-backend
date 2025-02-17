import pickle 
import boto3

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

s3 = boto3.client("s3")
s3.upload_file("model.pkl")

