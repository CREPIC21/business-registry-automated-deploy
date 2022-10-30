#!/usr/bin/python3

"""subprocess library allows us to execute and manage subprocesses directly from Python"""
import subprocess
"""allows us to get arguments from the user and parse them and use them in our code"""
import optparse
import time

print("Executing script 02")
subprocess.call(["python3", "02_npm_pm2_setup.py"])
print("Going to sleep for 5 seconds before executing script 03")
time.sleep(5)
print("Executing script 03")
subprocess.call(["python3", "03_nginx_and_firewall_setup.py"])
print("Going to sleep for 5 seconds before executing script 04")
time.sleep(5)
print("Executing script 04")
subprocess.call(["python3", "04_ssl_with_letsencrypt_setup.py"])
print("Setup done, go to your browser an visit the site.")



