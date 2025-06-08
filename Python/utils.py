import os # importing a library

print(os.system('df -h'))
print(os.system('uptime')) # uptime and load average
print(os.system('sysctl hw.memsize')) # RAM for Mac