from flask import Flask, request, jsonify
import numpy as np
from PIL import Image

app = Flask(__name__)


@app.route('/upload_image', methods=['POST'])
def upload_image():
    # Get the image data from the HTTP request body
    data = request.get_data()

    # Convert the binary data to a numpy array of floats
    image_data = np.frombuffer(data, dtype=np.float32)

    # Reshape the numpy array into a 128x128 array
    image_data = image_data.reshape((256, 256)) * 255.0
    image_data = image_data.astype(np.uint8)

    # Convert the numpy array to a Pillow image
    image = Image.fromarray(image_data)

    # Save the image as a JPEG file
    image.save('image.jpg', 'JPEG')

    # Return a success message to the ESP32
    response = {'message': 'Image data received and saved successfully'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
