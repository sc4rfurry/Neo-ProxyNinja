#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import mkdir
from socket import inet_aton, error as err, socket
import urllib3
from urllib3.contrib.socks import SOCKSProxyManager
# import os
# import logging



urllib3.disable_warnings()
isError = False
message = "None"



# function to validate the ip address
def validate_ip(ip):
    try:
        inet_aton(ip)
        return True
    except err:
        return False


# validate ports
def validate_port(port):
    if port.isdigit():
        if 0 <= int(port) <= 65535:
            return True
        else:
            return False
    else:
        return False



# Create logs directory if it doesn't exist
# if not os.path.exists('logs'):
#     mkdir('logs')

# # Configure logging
# log_file = 'logs/proxies_checker.log'
# logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


class ProxiesChecker:
    def __init__(self):
        pass


    def https(proxy, port, timeout):
        # implement it using urllib3 and ProxyManager
        try:
            proxy = urllib3.ProxyManager(f"http://{proxy}:{port}")
            response = proxy.request("GET", "http://ifconfig.io", timeout=int(timeout))
            print(response.status)
            if response.status == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False


    def socks4(proxy, port, timeout):
        # implement it using urllib3[socks] and SOCKSProxyManager
        # Not Working for some odd reason ...!
        try:
            proxy = SOCKSProxyManager(f"socks4a://{proxy}:{port}/")
            response = proxy.request("GET", "http://ifconfig.io", timeout=int(timeout))
            print(response)
            if response.status == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False