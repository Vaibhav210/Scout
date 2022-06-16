#!/bin/bash

sudo pacman -Syy
sudo pacman -S python3
sudo pacman -S python-pip
sudo pip3 install pyfiglet
sudo pip3 install termcolor
sudo pacman -S git


sudo pacman -S dnsutils

sudo pacman -S traceroute

sudo pacman -S whois

sudo pip3 install dnsrecon


wget https://golang.org/dl/go1.17.linux-amd64.tar.gz
sudo tar -zxvf go1.17.linux-amd64.tar.gz -C /usr/local/
echo "export PATH=/usr/local/go/bin:${PATH}" | sudo tee /etc/profile.d/go.sh
source /etc/profile.d/go.sh


git clone https://github.com/projectdiscovery/subfinder.git
cd subfinder/v2/cmd/subfinder
go build .
sudo mv subfinder /usr/local/bin
cd ../../../../


sudo pacman -S nmap


git clone https://github.com/maurosoria/dirsearch.git
cd dirsearch
pip3 install -r requirements.txt
