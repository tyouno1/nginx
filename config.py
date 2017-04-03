#!/usre/bin/env python
#encoding: utf-8

port = 9020
server = 'default'
servername = 'cmdb'
access_log = '/var/log/cmdb.log'
home = '/root/github/cmdb'
proxy_port = 9010

rh = open('nginx.tpl')
nginx_conf = rh.read().format(port=port, server=server, 
                        servername=servername, access_log=access_log,
                        home=home, proxy_port=proxy_port)
handler = open('cmdb.conf', 'w')
handler.write(nginx_conf)
handler.close()
rh.close()
