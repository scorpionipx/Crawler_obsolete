from crawler.utils.connection.host import Host

forced_ip = '192.168.0.101'
host = Host(forced_ip=forced_ip, port=1369)
host.run_echo_mode()


