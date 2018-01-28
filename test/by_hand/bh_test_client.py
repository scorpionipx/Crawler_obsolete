from crawler.utils.connection.client import Client


client = Client('192.168.0.100', 1369)
client.connect_to_host()

while True:
    user_input = input()
    response = client.send_package_and_get_response(user_input)
    print("Server's response: {}".format(response))


