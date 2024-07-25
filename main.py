import torch
from PIL import Image
import requests
import os
from io import BytesIO
import mimetypes
import math

# Load the YOLOv5 model (replace 'yolov5s.pt' with your model path)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/vehicle_detection.pt')
model.eval()  # Set to evaluation mode

# Load and prepare the image
class_list = ["car", "threewheel", "bus", "truck", "motorbike", "van"] 

'''{
    "car": 1,
    "threewheel": 2,
    "bus": 3,
    "truck": 4, 
    "motorbike": 5, 
    "van": 6
}'''

total_pred = 0
accurate_pred = 0
output_text = ''
# Define the path to the 'images' folder
image_path = 'images'

# List all folders in the specified folder
folders = [f for f in os.listdir(image_path) if os.path.isdir(os.path.join(image_path, f))]

# Print the folder names
for folder in folders:
    vehicle_path = image_path + '/' + folder 
    vehicle_contents = os.listdir(vehicle_path)
    if folder == "NO_MODEL":
        vehicle_contents = []
    for image in vehicle_contents:
        image_filepath = vehicle_path + '/' + image
        mime_type, _ = mimetypes.guess_type(image)
        if mime_type == "image/jpeg":
            results = model(image_filepath)
            predictions = results.pred[0]
            if len(predictions) == 0:
                output_text += f'Image Name: {image}, Class ID: {class_id}, Class name: NO PREDICTIONS AVAILABLE \n'
            else:
                sorted_predictions = sorted(predictions, key=lambda x: x[4], reverse=True)
                best_prediction = sorted_predictions[0]
                class_id = int(best_prediction[5])
                class_name = results.names[class_id]
                confidence = float(best_prediction[4])
                output_text += f'Image Name: {image}, Class ID: {class_id}, Class name: {class_name}, Confidence: {round(confidence, 2)} \n' 
                if class_name == folder:
                    accurate_pred += 1
                    total_pred += 1
                else:
                    total_pred += 1
            # Print results
            #results.print() #Display results
            #results.show()   # Display results
            results.save()   # Save results to a directory'''

total_accuracy = round((accurate_pred/total_pred), 2)

print("-"*30)
print(output_text)
print(f"TOTAL ACCURACY IS: {total_accuracy}")