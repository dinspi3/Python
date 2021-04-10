
#ping verification

import subprocess

def ping (host):
    command = ['ping' , '-c','1' , host]
    return subprocess.call(command)
host='google.com'

print(ping(host))




