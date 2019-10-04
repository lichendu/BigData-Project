# **MNIST Project**


## Project Description
Welcome! This MNIST project received assistance from Dr. Zhang Fan from MIT LIGO Lab.  about using the TensorFlow training model and MNIST database to help users to recognize a single digit number (0-9) from a picture which contains a hand-writing number. The users can use the curl- X POST command to upload their test picture (which should be in 28px* 28px) to the localhost URL address. Then, the project will use Flask to handle the picture upload requests and will run the prediction for the digit number it contains. MNIST is a large database contains more than 60,000 training images. Applying TensorFlow to the model, users can receive high accuracy digital number outputs from their uploaded pictures. 

## Model Prediction 
###### Pull the documents and ckpt file from GitHub

Use the following curl command to upload picture. Notice: The picture should contain a single digit number and be in 28px*28px.
    curl -F "file=@[filename]" localhost:5000/upload

###### Try to use the picture called "test1.png" and "test2.png" for testing. For more code running process, Please see Video.mp4.

                      
###### For more details about the project, Please see Project report.pdf 
