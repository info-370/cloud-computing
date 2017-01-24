# AWS Setup Information

# Documentation
- AWS SDK for Python
    - [boto3](https://boto3.readthedocs.io/en/latest/guide/resources.html) (don't ask me why its called that)
- [AWS cli](https://aws.amazon.com/cli/)
- [EC2](https://aws.amazon.com/ec2/)
- [S3](https://aws.amazon.com/s3/)

## Instructions
- ssh into the demo EC2 instance I have created (remember the .pem file)
- Create a directory with your name in the following format `lastname_firstname`
    - You must do at least this step to receive particiation
- Move the .py file in this directory from your machine to the EC2 instance using scp. You must put the python file in the directory with your name
- ssh into the EC2 again. Open the python file with any command line text editor (nano, vi, emacs)
    - Note that you hould run `python --version` prior to writing your code and comply to that version of python
    - Follow the instructions in the python file (you should only need to write 2 lines max)
- Run your python file to make sure that it works
