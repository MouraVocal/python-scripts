import socket
import requests

ip_local = socket.gethostbyname(socket.gethostname())
response = requests.get('https://api.ipify.org')
ip_publico = response.text

print(f'IP Local: {ip_local}')
print(f'IP Público: {ip_publico}')
