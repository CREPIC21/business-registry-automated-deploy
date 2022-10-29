#!/usr/bin/python3

"""subprocess library allows us to execute and manage subprocesses directly from Python"""
import subprocess
import time

# Installing required software for our hosting platform
subprocess.call(["sudo", "apt", "update"])
subprocess.call(["sudo", "apt", "upgrade"])

# Install Node/NPM
subprocess.call("sudo " + "curl " + "-sL " + "https://deb.nodesource.com/setup_14.x " + "| " + "sudo " + "-E " + "bash " + "-", shell=True)
subprocess.call(["sudo", "apt", "install", "nodejs", "nginx"])
subprocess.call(["sudo", "node", "--version"])
subprocess.call(["sudo", "npm", "--version"])
subprocess.call(["sudo", "nginx", "--version"])

# Clone your project from Github
subprocess.call(["sudo", "mkdir", "/root/apps"])
subprocess.call("sudo " + "git " + "clone " + "https://github.com/CREPIC21/businessregistry.git", cwd="/root/apps/", shell=True)

### IMPORTANT ###
# Create config.env and add all environment variables to config.env