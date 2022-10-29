#!/usr/bin/python3

"""subprocess library allows us to execute and manage subprocesses directly from Python"""
import subprocess

# Install dependencies and test app
subprocess.call("sudo " + "npm " + "install ", cwd="/root/apps/businessregistry/", shell=True)

# Setup PM2 process manager to keep your app running
# subprocess.call(["sudo", "npm", "i", "pm2", "-g"])
subprocess.call("sudo " + "npm " + "i " + "pm2 " + "-g", cwd="/root/apps/businessregistry/", shell=True)
# Start the app
# subprocess.call(["sudo", "pm2", "start", "server.js"])
subprocess.call("sudo " + "pm2 " + "start " + "server.js", cwd="/root/apps/businessregistry/", shell=True)
# To make sure app starts when reboot
subprocess.call(["sudo", "pm2", "startup", "ubuntu"])
subprocess.call("sudo " + "pm2 " + "startup " + "ubuntu", cwd="/root/apps/businessregistry/", shell=True)

