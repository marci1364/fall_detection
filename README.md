# Fall Detection on Heroku
## Users: 
The primary users of this project are elderly people. But it can also be beneficial for anyone who is at risk of falling such as, bikers, construction workers etc.

## Objective: 
One out of four older adults will fall each year in the United State. It causes many disabling fractures. It also reduces the independence of the person.
Current solutions are not very effective and they are not free. The objective of this project is to address these issues.
## Dataset: 
The training data is acquired from Biomedical Informatics & eHealth Laboratory. MobiAct dataset includes:\
 •	Four different types of falls performed by 66 participants \
 •	Eleven different types of ADLs performed by 19 participants and nine types of ADLs performed by 59 participants
 ## Training:
 Training is performed by following a two step process. First, the windows of accelerometer time-series data with magnitude of larger than a predefined threshold are detected. Then, seven features are extracted from these windows of data. And finally, a SVM model is udes for the training. The train.py is run and the model is saved in "fall_model".
## Inference:
The trained model is loaded in inference.py to predict the fall of test data (.txt file).
## Heroku App:
The heroku fall detection app can be found here: https://fall-detection-1364.herokuapp.com/ \
First, it asks for an emergency contact phone number to send a message to them if a fall happens. Then, data from 11 different dataset can be selected and the app processe that. If a fall happens, a red message appears to inform fall occurance.
### Description of 11 options in heroku app:\
1. Walk
2. Jog
3. FW Fall ( Fall Forward from standing, use of hands to dampen fall)
4. Jump
5. BW Fall (Fall backward while trying to sit on a chair)
6. Side Fall (Fall sidewards from standing, bending legs)
7. Stand
8. Car-step in
9. Stair-down
10. FW Knee Fall (Fall forward from standing, first impact on knees)
11. Sit to Stand
