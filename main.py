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
    for image in vehicle_contents:
        image_filepath = vehicle_path + '/' + image
        mime_type, _ = mimetypes.guess_type(image)
        if mime_type == "image/jpeg":
            results = model(image_filepath)
            
            main_prediction = False
            for pred in results.pred[0]:
                class_id = int(pred[5])  # Class ID (index)
                class_name = class_list[class_id]  # Class name
                
                if class_name == folder and main_prediction == False:
                    main_prediction = True
                    accurate_pred += 1
                    total_pred += 1
                    output_text += f'Image Name: {image}, Class ID: {class_id}, Class name: {class_name} \n' 
                elif main_prediction == False:
                    main_prediction = True
                    total_pred += 1
                    output_text += f'Image Name: {image}, Class ID: {class_id}, Class name: {class_name} \n' 
            # Print results
            #results.show()   # Display results
            results.save()   # Save results to a directory'''

total_accuracy = round((accurate_pred/total_pred), 2)

print("-"*30)
print(output_text)
print(f"TOTAL ACCURACY IS: {total_accuracy}")