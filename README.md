# Vehicle-Type
This project uses YOLO (Deep-Learning Computer Vision Tool) that has been trained specifically for the purpose of guessing types of vehicles. This particular model was trained on YOLO which you can find here: https://github.com/ultralytics/ultralytics. I used the Kaggle Dataset found at this link (https://www.kaggle.com/datasets/nadinpethiyagoda/vehicle-dataset-for-yolo) (intended for really just learning since it's labelled and annotated well - I didn't really check or change anything with the dataset manually).

After using YOLO to fine-tune the YOLOV5 model, I put it in this project along with certain information regarding the accuracy and further information regarding the model. I ran this model locally on my RTX 4060 TI using Windows (not WSL or Linux) with an image size of 640x640, a batch size of 60, and 50 different epochs. 

# Classes in the Project
So there are multiple classes of images in the project - strictly in order:
1. bus
2. car
3. motorbike
4. threewheel
5. truck
6. van

My model takes in an input (any photo), and will classify it as one of the above with a percentage-likeliness. Do note, however, that since I'm using YOLO, if you put an image that doesn't really have one of the above classes, then it will likely output "nothing" or a prediction with extremely low confidence. If you want to try that, you can check mye xample in the "NO_MODEL" folder. 

# Commands to RUN
- "main.py" - this program will run the model on the images in the respective folders for each of the classes and output an accuracy percentage of the model based on whether it matches the respective folder it's located in. I have 3-4 images in each folder right now, and the current accuracy rate is around 79%, but that's because of some additional circumstances I'll mention in the "Discussion" section. You can run this by inputting the below command within the directory "Vehicle-Type":
```python main.py```
- "detect.py" - this program will output the result of the model (using YOLO) on an image provided after the command. Input it in the same directory as above in the following way:
```python detect.py INSERT_PATH_HERE```

# Discussion
So, this model is actually extremely good at classifying, especially compared to other non-YOLO based image-classifiers I've made in the past. Although the accuracy rate of the image isn't really high (at around 80%), this is because the preset inputs I have are intended to confuse the model. First, for those who don't have the ability to run the model for themselves, this is the output (that I programmed to output -- YOLO doesn't output in this format):
```
Image Name: bus1.jpg, Class ID: 4, Class name: motorbike, Confidence: 0.88
Image Name: bus2.jpeg, Class ID: 3, Class name: truck, Confidence: 0.89
Image Name: bus3.jpeg, Class ID: 2, Class name: bus, Confidence: 0.93
Image Name: car1.jpeg, Class ID: 0, Class name: car, Confidence: 0.93
Image Name: car2.jpeg, Class ID: 0, Class name: car, Confidence: 0.98
Image Name: car3.jpg, Class ID: 0, Class name: car, Confidence: 0.98
Image Name: car4.jpeg, Class ID: 4, Class name: motorbike, Confidence: 0.67
Image Name: motorbike1.jpg, Class ID: 4, Class name: motorbike, Confidence: 0.92
Image Name: motorbike2.jpeg, Class ID: 4, Class name: motorbike, Confidence: 0.95
Image Name: motorbike3.jpeg, Class ID: 4, Class name: motorbike, Confidence: 0.83
Image Name: auto1.jpg, Class ID: 1, Class name: threewheel, Confidence: 0.94
Image Name: auto2.jpg, Class ID: 1, Class name: threewheel, Confidence: 0.87
Image Name: auto3.jpeg, Class ID: 0, Class name: car, Confidence: 0.98
Image Name: truck1.jpg, Class ID: 3, Class name: truck, Confidence: 0.75
Image Name: truck2.jpg, Class ID: 3, Class name: truck, Confidence: 0.97
Image Name: truck3.jpg, Class ID: 3, Class name: truck, Confidence: 0.68
Image Name: van1.jpeg, Class ID: 5, Class name: van, Confidence: 0.98
Image Name: van2.jpeg, Class ID: 5, Class name: van, Confidence: 0.97
Image Name: van3.jpeg, Class ID: 5, Class name: van, Confidence: 0.98

TOTAL ACCURACY IS: 0.79
```
Now, let's walk through the main places where this model went "wrong" -- most of them were pretty much a result of intended behaviors, lack of depth in the dataset, or just honest mistakes that really humans could make as well.
- Bus1 - this is classified as a motorbike because my model is instructed to pick the prediction with the highest confidence. If you see in that image, there is a bike in the very front of the image which the model predicted as a motorbike. This information would be more prevalent if you ran the "detect.py" functionality on that image and saw that it was detecting the motorbike with a higher confidence (not sure exactly why) then the truck behind it, and went with picking that as the "vehicle" for the image.
- Bus2 - this is a school-bus. In our dataset, we had NO school-buses and all buses were classified as typical passenger buses. I will play around with this more later down the line, but my guess is that the fact that the particular school-bus in that photo has an "extension" in the front (like a proper fender and front instead of being in-line with the rest of the front of the school-bus), that probably caused the model to assume it was a truck. Once again, this mistake is a result of a lack of depth in the training set, and deliberate confusion of the model from my end.
- Car4 - note that this is a race-car. There are some very important characteristics of a normal car that this car lacks (such as proper covering of the vehicle, etc). Once again, this type of car wasn't really prevalent in my dataset and these certain characteristics appear more in line with some of the motorbikes I had in the dataset. Note that although the model did predict this image as a motorcycle, it did so with a relatively low confidence rate indicating some of the confusion that I had mentioned earlier.
- Auto3 - note that this is isn't a typical "auto" or "tuk tuk" which is what the model trained to be a three-wheeler, and instead looks significantly more like a "3-wheeled *car*". Once again, this confused the model (despite the fact that the confidence for that prediction is relatively high). 

# Further Conclusions and Improvements
To improve this model, it's obvious that I/we need to get a more comprehensive training dataset and train the model with that in order to make it capable of handling some of the edge-case images I inputted while testing. That being said, this model works extremely well and was extremely easy to make indicating how good of a technology YOLO (You Only Look Once) is!