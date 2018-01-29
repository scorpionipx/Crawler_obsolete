from crawler.controller import CrawlerController


crawler_ip = '192.168.0.101'
crawler_port = 1369

control = CrawlerController(crawler_ip, crawler_port)
control.connect_to_crawler()

while True:
    user_input = input()
    control.connection.send_package(user_input)
    if user_input == 'exit':
        break



