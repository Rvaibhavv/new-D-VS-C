import os
def mlflowset():
    os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Rvaibhavv/new-D-VS-C.mlflow"
    os.environ["MLFLOW_TRACKING_USERNAME"]="Rvaibhavv"
    os.environ["MLFLOW_TRACKING_PASSWORD"]="a37ad20e3c8a402cd86cae1238ec2ef1bed9ba0d"


#     #### dagshub
# [dagshub](https://dagshub.com/)

# export MLFLOW_TRACKING_URI=https://dagshub.com/Rvaibhavv/kidney-Disease-Dl-Classifier.mlflow 

# export MLFLOW_TRACKING_USERNAME=Rvaibhavv 

# export MLFLOW_TRACKING_PASSWORD=a37ad20e3c8a402cd86cae1238ec2ef1bed9ba0d 


# ### following will work for conda enviroment
# conda env config vars set MLFLOW_TRACKING_URI=https://dagshub.com/Rvaibhavv/NEW-D-VS-C.mlflow --name cvdn

# conda env config vars set MLFLOW_TRACKING_USERNAME=Rvaibhavv --name cvdn

# conda env config vars set MLFLOW_TRACKING_PASSWORD=a37ad20e3c8a402cd86cae1238ec2ef1bed9ba0d --name cvdn