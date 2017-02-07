# Distributed Computing - Part 1
In this lab we will be doing data processing with data from AWS S3. A small rest API has been provided to you. Your job is to implement one function that API needs to call to find the average census tract population size for a given city. The goal of this lab is to set up for part two, where we will run this API on a cluster of multiple machines to increase performance.

## The REST API
This API only has two endpoints. The / endpoint just returns a string saying "Welcome to lab!"
The second endpoint is documented as follows

`/average_pop?city`

city: name of a US city. Can be one of
    `baltimore`, `charelston`, `chicago`, `columbus`, `dayton`, `denver`,
    `kc`, `memphis`, `milwaukee`, `ok_city`, `pittsburg`, `st_louis`,
    `syracuse`, or `wichita`

## Virtual Environments
Virtual environments are a popular tool with python developers for self containing dependencies within a directory. You simply make a new eirtual environment, and anything you install or remove with pip will only apply to that directory, not your global pip packages.

To make a new virtual environment: `virtualenv ./project_directory`

To start that environment: _**On Mac/Linux**_ `source ./project_directory/bin/activate` _**On windows**_ `.\project_directory\Source\activate`

To stop that environment: _**On Mac/Linux**_ `source ./project_directory/bin/deactivate` _**On Windows**_ `.\project_directory\Source\activate`

## Setup
Before you start this lab you should make a new virtual environment in this directory and start it. Next, notice that there is a file called `requirements.txt`. This is a format that pip understands and that contains all the python packages needed for this project. You can install them with `pip install -r requirements.txt`

## To-do
Your job for this part of the lab is to edit the `processing.py` file. It contains a function called `get_average_pop` which is called by the REST API. Follow the directions ins the `processing.py` file to implement this function.

# Testing your solution
To test your code, I have written a small program in `test.py` which just calls the `average_pop` endpoint for every city and prints out the results.
