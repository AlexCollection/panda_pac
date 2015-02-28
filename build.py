# -*- coding: utf-8 -*-

import json

proxy = 'SOCKS5 localhost:1234;SOCKS localhost:1234;'


def read_domains():
    with open('res/domains.txt') as f:
        domains = f.read().splitlines()
    with open('res/custom.txt') as f:
        custom_domains = f.read().splitlines()
    return custom_domains + domains


def generate_pac(domains):
    with open('res/proxy.pac') as f:
        proxy_content = f.read()

    proxy_content = proxy_content.replace('__PROXY__', proxy)

    domains_dict = {}
    for domain in domains:
        domains_dict[domain] = 1
    proxy_content = proxy_content.replace(
        '__WHITELIST__',
        json.dumps(domains_dict, indent=2, sort_keys=True)
    )

    return proxy_content


if __name__ == '__main__':
    domains = read_domains()
    print generate_pac(domains)
