from paramiko.client import SSHClient,AutoAddPolicy

client = SSHClient()

client.set_missing_host_key_policy(AutoAddPolicy())
client.connect("10.0.2.15",22,"rani","toxicteros")

while(True):  
  stdin,stdout,stderr = client.exec_command('python3 ppmonitoring.py')
  lines = stdout.readlines()
  lines_err = stderr.readlines()
  for i in lines_err:
    print(i)
  for i in lines:
    print(i)

client.close()
