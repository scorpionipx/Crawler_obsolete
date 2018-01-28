from crawler.controller import CrawlerController


crawler_ip = '192.168.0.101'
crawler_port = 1369

control = CrawlerController(crawler_ip, crawler_port)
control.connect_to_crawler()

while True:
    user_input = input()
    response = control.connection.send_package_and_get_response(user_input)
    if user_input == 'exit':
        break
    print("Server's response: {}".format(response))


