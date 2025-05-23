from azure.storage.blob import BlobServiceClient
import uuid
from flask import current_app

def upload_to_blob(file, container_name):
    connect_str = current_app.config['AZURE_STORAGE_CONNECTION_STRING']
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container_name)

    if not container_client.exists():
        container_client.create_container()

    blob_name = f"{uuid.uuid4()}_{file.filename}"
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file, overwrite=True)
    return blob_client.url