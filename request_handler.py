import os
import requests

filename = os.getcwd() + '/myfile.txt'

a = requests.get('http://localhost:65000/{"read": ("/home/mayukh/Desktop/HDPMSD_SERV/server.py", 0)}')
print(a.text)