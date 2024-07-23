# Vehicle-Type
This project uses YOLO (Deep-Learning Computer Vision Tool) that has been trained specifically for the purpose of guessing types of vehicles. This particular model was trained on YOLO which you can find here: https://github.com/ultralytics/ultralytics. I used the Kaggle Dataset found at this link (https://www.kaggle.com/datasets/nadinpethiyagoda/vehicle-dataset-for-yolo) (intended for really just learning since it's labelled and annotated well - I didn't really check or change anything with the dataset manually).

After using YOLO to fine-tune the YOLOV5 model, I put it in this project along with certain information regarding the accuracy and further information regarding the model. I ran this model locally on my RTX 4060 TI using Windows (not WSL or Linux) with an image size of 640x640, a batch size of 60, and 50 different epochs. 

# Classes in the Project
So there are 
