#!/usr/bin/python
#
# scraper.py
#
import sys
import subprocess
import os
import time
import signal

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

# Define a signals handler to capture at least Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# If not given, use 14 seconds sleep
timeout = 14
if len(sys.argv) > 1:
    timeout = sys.argv[1]

option = ""
if len(sys.argv) > 2:
    option = "--" + sys.argv[2]

while True:
    os.system('clear')

    os.system('blockScrape ' + option)
    print("")

    os.system('miniBlocks --freshen')
    print("")

    os.system('getBlock --latest')
    print("")

#    os.system("echo 'index size: \c' ; cut -f3 /Volumes/Samsung_T7/scraper/addr_index/unsorted_by_block/counts.txt | awk '{s+=$1}END{print s/1024/1024 \" MB\"}'")
#    print("")

    print("Hit Ctrl+C to quit...");

    time.sleep(float(timeout))