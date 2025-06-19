#load env
import os

#read task from the file
from dotenv import load_dotenv
load_dotenv()


def read_tasks(filepath):
    with open(filepath,"r") as f:
        return f.read()
#make a call to open Ai