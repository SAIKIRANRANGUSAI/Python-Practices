import time

import paramiko
from getpass import getpass

host = "192.168.147.128"
username = input("enter username: ")
#password = getpass("enter your password: ")

sai = paramiko.SSHClient()

sai.set_missing_host_key_policy(paramiko.AutoAddPolicy())


sai.connect(hostname=host,username=username)

commands = ["whoami","pwd","ls"]

for i in commands:
    stdin,stdout,stderr = sai.exec_command(i)
    print(stdout.read().decode())
    time.sleep(3)


sai.close()