from time import sleep
from crawler.core import Crawler

crawler_ip = '192.168.0.101'
crawler_port = 1369

crawler = Crawler(ip=crawler_ip, port=crawler_ip)
crawler.drive(300)

sleep(2)

crawler.drive(0)





