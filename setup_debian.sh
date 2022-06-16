#!/bin/bash

sudo apt-get update
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-pyfiglet
sudo apt install python3-termcolor
sudo apt install git


sudo apt install dnsutils 

sudo apt install traceroute

sudo apt install whois

sudo apt install dnsrecon


wget https://golang.org/dl/go1.17.linux-amd64.tar.gz
sudo tar -zxvf go1.17.linux-amd64.tar.gz -C /usr/local/
echo "export PATH=/usr/local/go/bin:${PATH}" | sudo tee /etc/profile.d/go.sh
source /etc/profile.d/go.sh


git clone https://github.com/projectdiscovery/subfinder.git
cd subfinder/v2/cmd/subfinder
go build .
sudo mv subfinder /usr/local/bin
cd ../../../../


sudo apt install nmap


git clone https://github.com/maurosoria/dirsearch.git
cd dirsearch
pip3 install -r requirements.txt
