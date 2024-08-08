import paramiko
from getpass import getpass

host = "192.168.147.128"
username = input("Enter username: ")
password = getpass("Enter password: ")

try:
    # Create SSH client
    ssh_client = paramiko.SSHClient()

    # Automatically add the server's host key
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the SSH server
    ssh_client.connect(hostname=host, port=22, username=username, password=password)

    # Execute a command (e.g., check hostname)
    stdin, stdout, stderr = ssh_client.exec_command('hostname')
    print(f'Hostname is: {stdout.read().decode()}')

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Always close the session in the finally block
    ssh_client.close()
