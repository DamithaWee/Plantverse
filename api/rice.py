

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

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

MODEL = tf.keras.models.load_model(r"C:\Users\USER\Downloads\disease detection\new models\10\rice.h5")

CLASS_NAMES = ["rice_bacterial_leaf_blight","rice_brown_spot","rice_dead_heart","rice_healthy"]

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    # Read the uploaded file as an image
    image = read_file_as_image(await file.read())

    # Resize the image to match the model's expected input shape
    image = tf.image.resize(image, [224,224])

    img_batch = np.expand_dims(image, 0)

    predictions = MODEL.predict(img_batch)
    confidence = np.max(predictions[0])

    # Set your confidence threshold here
    confidence_threshold = 0.7

    if confidence < confidence_threshold:
        return {
            'class': 'Image not identified',
            'confidence': float(confidence)
        }

    predicted_class_index = np.argmax(predictions[0])

    # Check if the predicted class is within the range of expected classes
    if predicted_class_index < len(CLASS_NAMES):
        predicted_class = CLASS_NAMES[predicted_class_index]
    else:
        predicted_class = 'Unknown'

    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

# Run the FastAPI application using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8001)