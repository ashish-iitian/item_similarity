#!/usr/bin/env bash

# Set up some standard workspace essentials
echo "Updating apt repositories"
apt-get update >/dev/null 2>&1
echo "Installing build-essential, Java 7 and git"
apt-get install -y build-essential openjdk-7-jdk git  >/dev/null 2>&1

# Add any other needed commands here and they will be executed during the Vagrant
# provisioning step

sudo apt-get install python-scipy