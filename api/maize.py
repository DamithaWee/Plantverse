from fastapi import FastAPI, UploadFile,File,HTTPException
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

#create app which is an instance of fast api
app = FastAPI()

MODEL = tf.keras.models.load_model(r"C:\Users\USER\Downloads\diseasedetection\models\4\maize.h5")

CLASS_NAMES = ["maize_healthy", "maize_leaf blight","maize_leaf spot","maize_streak virus"]


# Define a route for a simple ping endpoint
@app.get("/ping")
async def ping():
    return "Hello, I am alive"

# Define a function to read a file as an image
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

# Define a route for making predictions using a file upload
# Define a route for making predictions using a file upload
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

    # Resize the image to match the model's expected input shape
    image = tf.image.resize(image, [256, 256])

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