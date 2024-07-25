import torch
from PIL import Image
import requests
import os
import sys
from io import BytesIO
import mimetypes

# Load the YOLOv5 model (replace 'yolov5s.pt' with your model path)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/vehicle_detection.pt')
model.eval()  # Set to evaluation mode

def predict_image(image_filepath):
    results = model(image_filepath)
    
    # Print results
    results.show()   # Display results
    results.save()   # Save results to a directory'''



def main():
    if len(sys.argv) != 2:
        print("Usage: python detect.py <input>")
        sys.exit(1)

    image_filepath = sys.argv[1]
    mime_type, _ = mimetypes.guess_type(image_filepath)
    if mime_type == "image/jpeg":
        predict_image(image_filepath)
    else:
        raise TypeError("The filetype isn't an image!")

if __name__ == "__main__":
    main()