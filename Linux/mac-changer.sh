#!/bin/bash
macchanger -l > vendor-mac.txt 
ouimac=$(shuf -n 1 vendor-mac.txt | awk '{printf$3}')
uaamac=$(printf '%02x:%02x:%02x' $[RANDOM%256] $[RANDOM%256] $[RANDOM%256]  )
sudo macchanger -m "$ouimac:$uaamac" eth0
