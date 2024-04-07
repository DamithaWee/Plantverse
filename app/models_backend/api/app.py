from fastapi import FastAPI, UploadFile,File,HTTPException
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf


#create app which is an instance of fast api
app = FastAPI()

PEST_MODEL = tf.keras.models.load_model(r"../pestmodels/13/pests.h5")
CASHEW_MODEL = tf.keras.models.load_model(r"../disease_models/Cashew/1/cashew.h5")
CASSAVA_MODEL = tf.keras.models.load_model(r"../disease_models/Cassava/3/cassava.h5")
MAIZE_MODEL = tf.keras.models.load_model(r"../disease_models/Maize/5/maize.h5")
RICE_MODEL = tf.keras.models.load_model(r"../disease_models/Rice/10/rice.h5")
TOMATO_MODEL = tf.keras.models.load_model(r"../disease_models/Tomato/12/tomato.h5")

PEST_CLASS_NAMES = ["cashew_leaf miner","cassava_green mite","maize_fall armyworm","maize_grasshoper","maize_leaf beetle","rice_hispa"]
CASHEW_CLASS_NAMES = ["cashew_anthracnose", "cashew_gumosis", "cashew_healthy", "cashew_red rust"]
CASSAVA_CLASS_NAMES = ["cassava_bacterial blight", "cassava_brown spot", "cassava_healthy", "cassava_mosaic"]
MAIZE_CLASS_NAMES = ["maize_healthy", "maize_leaf blight", "maize_leaf spot", "maize_streak virus"]
RICE_CLASS_NAMES = ["rice_bacterial_leaf_blight", "rice_bacterial_leaf_streak", "rice_bacterial_panicle_blight", "rice_blast", "rice_brown_spot", "rice_dead_heart", "rice_downy_mildew", "rice_healthy", "rice_tungro"]
TOMATO_CLASS_NAMES = ["Tomato_Early_blight", "Tomato_Late_blight", "Tomato_Leaf_Mold","Tomato_Septoria_leaf_spot","Tomato_Late_blight","Tomato__Tomato_YellowLeaf__Curl_Virus","Tomato__Tomato_mosaic_virus","Tomato_healthy","tomato_verticulium wilt"]


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

    # Resize the image to match the model's expected input shape
    image = tf.image.resize(image, [224,224])

    img_batch = np.expand_dims(image, 0)

    predictions = PEST_MODEL.predict(img_batch)
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
    if predicted_class_index < len(PEST_CLASS_NAMES):
        predicted_class = PEST_CLASS_NAMES[predicted_class_index]
    else:
        predicted_class = 'Unknown'

    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

@app.post("/predict-cashew")
async def predictCashew(
    file: UploadFile = File(...)
):
    # Read the uploaded file as an image
    image = read_file_as_image(await file.read())

    # Resize the image to match the model's expected input shape
    image = tf.image.resize(image, [254, 254])

    img_batch = np.expand_dims(image, 0)

    predictions = CASHEW_MODEL.predict(img_batch)
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
    if predicted_class_index < len(CASHEW_CLASS_NAMES):
        predicted_class = CASHEW_CLASS_NAMES[predicted_class_index]
    else:
        predicted_class = 'Unknown'

    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

@app.post("/predict-cassava")
async def predictCassva(
    file: UploadFile = File(...)
):
    # Read the uploaded file as an image
    image = read_file_as_image(await file.read())

    # Resize the image to match the model's expected input shape
    image = tf.image.resize(image, [256, 256])

    img_batch = np.expand_dims(image, 0)

    predictions = CASSAVA_MODEL.predict(img_batch)
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
    if predicted_class_index < len(CASSAVA_CLASS_NAMES):
        predicted_class = CASSAVA_CLASS_NAMES[predicted_class_index]
    else:
        predicted_class = 'Unknown'

    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

@app.post("/predict-maize")
async def predictMaize(
    file: UploadFile = File(...)
):
    # Read the uploaded file as an image
    image = read_file_as_image(await file.read())

    # Resize the image to match the model's expected input shape
    image = tf.image.resize(image, [256, 256])

    img_batch = np.expand_dims(image, 0)

    predictions = MAIZE_MODEL.predict(img_batch)
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
    if predicted_class_index < len(MAIZE_CLASS_NAMES):
        predicted_class = MAIZE_CLASS_NAMES[predicted_class_index]
    else:
        predicted_class = 'Unknown'

    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

@app.post("/predict-rice")
async def predictRice(
    file: UploadFile = File(...)
):
    # Read the uploaded file as an image
    image = read_file_as_image(await file.read())

    # Resize the image to match the model's expected input shape
    image = tf.image.resize(image, [256, 256])

    img_batch = np.expand_dims(image, 0)

    predictions = RICE_MODEL.predict(img_batch)
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
    if predicted_class_index < len(RICE_CLASS_NAMES):
        predicted_class = RICE_CLASS_NAMES[predicted_class_index]
    else:
        predicted_class = 'Unknown'

    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

@app.post("/predict-tomato")
async def predictTomato(
    file: UploadFile = File(...)
):
    # Read the uploaded file as an image
    image = read_file_as_image(await file.read())

    image = image / 255.0  # Normalize pixel values to the range [0, 1]

    # Resize the image to match the model's expected input shape
    image = tf.image.resize(image, [256, 256])

    img_batch = np.expand_dims(image, 0)

    predictions = TOMATO_MODEL.predict(img_batch)
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
    if predicted_class_index < len(TOMATO_CLASS_NAMES):
        predicted_class = TOMATO_CLASS_NAMES[predicted_class_index]
    else:
        predicted_class = 'Unknown'

    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }


# Run the FastAPI application using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)