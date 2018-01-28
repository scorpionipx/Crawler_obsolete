import asyncore
from crawler.utils.connection.host import Host


server = Host()
asyncore.loop()


