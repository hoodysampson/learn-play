import webbrowser,sys
from ftplib import FTP
from getpass import getpass


if sys.version[0]=='2':input=raw_input

nonpassive=False
filename=input('File?')
dirname=input('Dir? ') or '.'
sitename=input('Site?')
user=input('User?')
if not user:
    userinfo=()
else:
    from getpass import getpass
    userinfo=(user,getpass('Pswd?'))

print('Connecting...')
connection=FTP(sitename)
connection.login(*userinfo)
connection.cwd(dirname)
if nonpassive:
    connection.set_pasv(False)

print('Downloading...')
localfile=open('formaterror.txt','wb')
connection.retrbinary('RETR'+filename,localfile.write,1024)
connection.quit()
localfile.close()

print('Playing...')
webbrowser.open(filename)