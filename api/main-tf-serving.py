from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import requests

#create app which is an instance of fast api
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the endpoint for making predictions using a pre-trained model
endpoint = "http://localhost:8501/v1/pestmodels/predict"
# Define class names for predictions
CLASS_NAMES = ["cashew_leaf miner", "cashew_leafminer", "cassava_green mite","maize_fall armyworm","maize_grasshoper","maize_leaf beetle","rice_hispa","Tomato_Spider_mites"]

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

    # Prepare the image batch for model prediction
    img_batch = np.expand_dims(image, 0)

    # Prepare JSON data for the model prediction request
    json_data = {
        "instances": img_batch.tolist()
    }

    # Make a POST request to the model serving endpoint
    response = requests.post(endpoint, json=json_data)

    # Process the model's response
    prediction = np.array(response.json()["predictions"][0])
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction)

    # Return the prediction result
    return {
        "class": predicted_class,
        "confidence": float(confidence)
    }

# Run the FastAPI application using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)


