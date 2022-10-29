#!/usr/bin/python3

"""subprocess library allows us to execute and manage subprocesses directly from Python"""
import subprocess

# Rename original nginx configuration file
subprocess.call(["sudo", "mv", "/etc/nginx/sites-available/default", "/etc/nginx/sites-available/default.ORIG"])
# Create a new nginx configuration file from template
subprocess.call(["sudo", "cp", "nginx_sites_available_config.txt", "/etc/nginx/sites-available/default"])

# Setup ufw firewall
subprocess.call(["sudo", "ufw", "enable"])
subprocess.call(["sudo", "ufw", "allow", "ssh"])
subprocess.call(["sudo", "ufw", "allow", "http"])
subprocess.call(["sudo", "ufw", "allow", "https"])
subprocess.call(["sudo", "ufw", "status"])

# Check NGINX config
subprocess.call(["sudo", "nginx", "-t"])

# Restart NGINX
subprocess.call(["sudo", "service", "nginx", "restart"])