#!/bin/bash
# This script will be used to do the same thing that we were doing in 
# the /etc/init.d/halt script.

for i in /sys/bus/usb/devices/*/power/control;
	do echo on > $i
done
