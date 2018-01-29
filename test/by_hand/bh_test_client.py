from crawler.utils.connection.client import Client
import socket

host = 'raspberrypi'
host_ip = '192.168.0.101'
client = Client(host_ip, 1369)
client.connect_to_host()

while True:
    user_input = input()
    response = client.send_package_and_get_response(user_input)
    print("Server's response: {}".format(response))


