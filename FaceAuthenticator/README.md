### IoT-A2
<b>Part C</b><br>

Design: 
 - Using local camera to capture an image
 - Using local facial detecting lib to determine if there is a human face in the image
 - Facial recoknition requires high accuracy for authentication purpose, so using cloud based facial recoknition service for better security
 - Cloud service to be serverless to simplify the development 
 - Put all into FaceAuthenticator module for code reusing

Dependencies:
 - opencv and its dependencies: used to detect face in an image. To install run the shell script named 'install-cv2.sh'
 - boto3: used for interacting with aws recoknition service
 - awscli: used to config the access keys

AWS Rekognition:
 - Full-managed cloud service
 - No images will be saved locally or stored in the cloud: facial signatures consist of facial vectors will be stored instead of the images
 - Very high accuracy
 - Using aws key to interact with personal aws account, the keys are for a user created to interact with aws rekognition only. After installed boto3 and awscli, run ```aws configure``` then type in access_key_id and access_key_id in the "credentials.csv" file
 