#!/usr/bin/python3

"""subprocess library allows us to execute and manage subprocesses directly from Python"""
import subprocess

subprocess.call(["sudo", "apt-get", "install", "python3-certbot-nginx"])
subprocess.call(["sudo", "certbot", "--nginx", "-d", "businessregistry.xyz"])
subprocess.call(["sudo", "certbot", "--nginx", "-d", "www.businessregistry.xyz"])
