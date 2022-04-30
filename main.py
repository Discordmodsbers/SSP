import os
import sys
import time
import socket
import threading
from terms import *
delay = 0.1

print("please press 1 to proceed (type terms to see the tools terms of use)")
while True:
  u = input("")
  if u =='1':
    break
  elif u =='terms' or 'Terms':
    terms()
os.system('clear')

p = """1. install suggested hacking tools.
2. launch attack on url
3. port scanner
4. ddos
5. run recon
6. change ascii text
7. clear"""
print(p)
while True:
  t = input("")
  if t =='1':
    
