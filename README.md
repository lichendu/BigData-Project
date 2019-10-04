# **MNIST Project**


## Table of Context
    *General Information
    *Project Description
    *Technologies
    *Set Up
    * Prediction
    
## General Information
Welcome! This MNIST project received assistance from Dr. Zhang Fan from MIT LIGO Lab.

## Project Description
This project uses the TensorFlow training model and MNIST database to help users to recognize a single digit number (0-9) from a picture which contains a hand-writing number. The users can use the curl- X POST command to upload their test picture (which should be in 28px* 28px) to the localhost URL address. Then, the project will use Flask to handle the picture upload requests and will run the prediction for the digit number it contains. MNIST is a large database contains more than 60,000 training images. Applying TensorFlow to the model, users can receive high accuracy digital number outputs from their uploaded pictures. 


## Technologies
This project is created with the following: 
* Python               3.6  
* redis                3.3.8  
* numpy                1.16.5   
* Pillow               6.1.0  
* Flask                1.1.1  
* tensorflow           1.14.0 

##Set Up
To run this project, you should install the technologies above in the right version. And then pull the documents and ckpt file from GitHub. 


## Model Prediction 
Notice: The picture should contain a single digit number and be in 28px*28px. You can either draw a hand-writing number in a picture or use the testing pictures called "test1.png" and "test2.png".
Then, Use the following curl command to upload picture. subsitute the [filename]with the name of your picture or the name of test picture. 

       curl -F "file=@[filename]" localhost:5000/upload

As the result, you will have a output which is a digit number from 0-9.
For more code running process, Please see Video.mp4.

                      
For more details about the project, Please see Project report.pdf 
