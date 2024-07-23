# INFO
As mentioned in the other README file, this folder includes the weights of the model along with the standard output of the YOLO fine-tuning. Check the images folder to see the images I'm testing this model on (note that the model has ALREADY been made I'm just testing it to see how it's working). Here are the different classes of images:
- car
- threewheel
- bus
- truck
- motorbike
- van

The most important file here is the "vehicle_detection.pt" which contains the weights of the model importantly in binary format. PT stands for PyTorch (these are pytorch files because YOLO when installed through GitHub runs on PyTorch). For those interested, if you try and obtain YOLO in different formats such as through DarkNet, you will typically have differing file formats, most commonly being ".weights" format. 

# More information about DARKNET 
I don't really know much about DarkNET except why it exists and that it's a HUGE pain to install so be very careful. That being said, DARKNET runs on C and you need some type of wrapper to make it usable in Python (like Cython, for instance). It has native support for CUDA (because it uses C), and thus, tends to be faster for people who are using NVIDIA GPUs (like me). But, because this is a relatively small project and not that important, I didn't want to go through the hassle of installing this "version" of YOLO. Pick which way you want to obtain and use YOLO based on this information going forward!
