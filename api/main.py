from fastapi import FastAPI, UploadFile,File
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image

#create app which is an instance of fast api
app = FastAPI()

# Define a route for a simple ping endpoint
@app.get("/ping")
async def ping():
    return "Hello, I am alive"

# Define a function to read a file as an image
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

# Define a route for making predictions using a file upload
@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    # Read the uploaded file as an image
    image = read_file_as_image(await file.read())
    return
# Run the FastAPI application using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)