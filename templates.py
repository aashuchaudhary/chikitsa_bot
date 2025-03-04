# for creating str of file

import os
from pathlib import Path
import logging #inbuilt package :for log infoin terminal


# creating logging stream:logging configuration

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s :')   # in format ascitime refers current time, log msg is what going to display.

# list of folder to create file and folders :MODULAR APPROACH 
list_of_files = [
    "src/__init__.py",   #constructor file 
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trails.ipynb",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)  # splitting file ans folder from list of files and store in two variables


    if filedir !="":                 #check for  file is empty or not 
        os.makedirs(filedir, exist_ok=True)     #create folder
        logging.info(f"Creating directory; {filedir} for the file: {filename}")   
# create file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):   #check file path size
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")