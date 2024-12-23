

# Checking and setting cwd
import os

## Check the current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

## Set the current working directory if needed
os.chdir(r"C:\Users\me20332\OneDrive - University of Bristol\MscR\Running Model Resources\sgrvinod PyTorch Object Detection")  # Replace with the correct path
## Check the current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")



# Importing data
## The data is stored in a tar file. We will extract the contents of the tar file to the current working directory.

import tarfile

# Define the file_path variable with the actual path to your tar file
file_path = r"C:\Users\me20332\OneDrive - University of Bristol\MscR\Running Model Resources\VOCtest_06-Nov-2007.tar"  # Replace with the correct path

## Open the tar file in read mode ('r')
with tarfile.open(file_path, 'r') as tar:
    # Extract all members of the archive to the current working directory
    tar.extractall()
    print('2007 Test Done')


file_path = r"C:\Users\me20332\OneDrive - University of Bristol\MscR\Running Model Resources\VOCtrainval_06-Nov-2007.tar"  # Replace with the correct path

with tarfile.open(file_path, 'r') as tar:
    tar.extractall()
    print('2007 Train Done')

# Extracting 2012 Train data
file_path = r"C:\Users\me20332\OneDrive - University of Bristol\MscR\Running Model Resources\VOCtrainval_11-May-2012.tar"  # Replace with the correct path

with tarfile.open(file_path, 'r') as tar:
    tar.extractall()
    print('2012 Train Done')

# MOVE DATA TO CWD! 



#Creating datalists for the train and test data
from utils import create_data_lists