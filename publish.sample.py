import os

FTP_HOST = 'example.com'
FTP_USER = 'milkmonkey'
FTP_PASS = 'secretpword'
FTP_TARGET_DIR = '/'

# build output based on publish profile
os.system('pelican content -s publishconf.py')

command = f'pyftpsync upload ./output ftp://{FTP_USER}:{FTP_PASS}@{FTP_HOST}{FTP_TARGET_DIR}'
os.system(command)
