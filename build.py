# -*- coding: utf-8 -*-

import json

proxy = 'SOCKS5 localhost:1234;SOCKS localhost:1234;'


def read_domains():
    with open('res/whitelist.txt') as f:
        whitelist = f.read().splitlines()
    with open('res/whitelist_custom.txt') as f:
        whitelist_custom = f.read().splitlines()
    with open('res/blacklist.txt') as f:
        blacklist = f.read().splitlines()
    with open('res/blacklist_custom.txt') as f:
        blacklist_custom = f.read().splitlines()
    return whitelist + whitelist_custom, blacklist + blacklist_custom


def generate_pac(white_domains, black_domains):
    with open('res/proxy_pac.tpl') as f:
        proxy_content = f.read()

    proxy_content = proxy_content.replace('__PROXY__', proxy)

    domains_dict = {}
    for domain in white_domains:
        domains_dict[domain] = 1
    proxy_content = proxy_content.replace(
        '__WHITELIST__',
        json.dumps(domains_dict, indent=2, sort_keys=True)
    )

    black_domains_dict = {}
    for domain in black_domains:
        black_domains_dict[domain] = 1
    proxy_content = proxy_content.replace(
        '__BLACKLIST__',
        json.dumps(black_domains_dict, indent=2, sort_keys=True)
    )

    return proxy_content


if __name__ == '__main__':
    white_domains, black_domains = read_domains()
    print generate_pac(white_domains, black_domains)
