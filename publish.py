import os

# build output based on publish profile
os.system('pelican content -s publishconf.py')
os.system("aws s3 sync output s3://farr-ai --profile kfarr-0596")