#!/bin/sh
echo USB info >> /home/user/simran/usb.txt
lsblk | grep sdb >> /home/user/simran/usb.txt
echo Mac address of the system using usb >> /home/user/simran/usb.txt
ifconfig -a wlp6s0 | grep HWaddr >> /home/user/simran/usb.txt 
python3 /home/user/Desktop/usb/face.py 
python3 /home/user/Desktop/usb/mail.py 
rm -f /home/user/simran/usb.txt
rm -f /home/user/Desktop/faces/user/1.jpg 


