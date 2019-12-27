import os

# build output based on publish profile
os.system('pelican content -s publishconf.py')
os.system("AWS_PROFILE=kfarr-0596 aws s3 sync output s3://farr-ai --acl public-read")