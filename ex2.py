import paramiko
from getpass import getpass

host = "192.168.147.128"
username = input("enter username: ")
password = getpass("enter password: ")

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,username=username,password=password)

stdin,stdop,stderr = ssh_client.exec_command("pwd")
print(f"command output is : {stdop.read().decode()}")

ssh_client.close()