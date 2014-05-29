# -*- coding: utf-8 -*-

proxy_domains = white_domains = None
proxy = 'SOCKS5 localhost:1234;SOCKS localhost:1234;'

with open('domain/proxylist.txt') as f:
    proxy_domains = f.read().splitlines()

with open('domain/whitelist.txt') as f:
    white_domains = f.read().splitlines()

with open('proxy.tpl') as f:
    tpl = f.read()
    print tpl %(proxy, str(proxy_domains), str(white_domains))
