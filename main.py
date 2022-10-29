#!/usr/bin/python3

"""subprocess library allows us to execute and manage subprocesses directly from Python"""
import subprocess
import time

# # Installing required software for our hosting platform
# subprocess.call(["sudo", "apt", "update"])
# subprocess.call(["sudo", "apt", "upgrade"])
#
# # Install Node/NPM
# subprocess.call("sudo " + "curl " + "-sL " + "https://deb.nodesource.com/setup_14.x " + "| " + "sudo " + "-E " + "bash " + "-", shell=True)
# subprocess.call(["sudo", "apt", "install", "nodejs"])
# subprocess.call(["sudo", "node", "--version"])
# subprocess.call(["sudo", "npm", "--version"])

# Clone your project from Github
# subprocess.call(["sudo", "mkdir", "apps"])
subprocess.call("sudo " + "cat " + "/etc/nginx/sites-available/default ", shell=True)
subprocess.call("sudo " + "cp " + "/etc/nginx/sites-available/default " + "nginx_sites_available_config.txt", shell=True)

### IMPORTANT ###
# Create config.env and add all environment variables to config.env

