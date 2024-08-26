import os
import paramiko
from getpass import getpass

host = "192.168.147.128"
username = input("enter username: ")
password = getpass("enter password: ")

sai = paramiko.SSHClient()

# Define the path to the known_hosts file
known_hosts_path = '/home/saikiran/.ssh/known_hosts'

# Ensure the known_hosts file exists
if not os.path.exists(known_hosts_path):
    os.makedirs(os.path.dirname(known_hosts_path), exist_ok=True)
    with open(known_hosts_path, 'w'):
        pass

sai.load_host_keys(known_hosts_path)

sai.connect(hostname=host, username=username, password=password)
stdin, stdout, stderr = sai.exec_command("ls")
print(stdout.read().decode())
sai.close()
