import random
import subprocess
import time

def random_ip():
    return f"192.168.0.{random.randint(2, 254)}"

def change_ip(interface):
    new_ip = random_ip()
    print(f"[+] New IP: {new_ip}")
    
    cmd = f'netsh interface ip set address name="{interface}" static {new_ip} 255.255.255.0 192.168.0.1'
    subprocess.run(cmd, shell=True)

interface = "Wi-Fi"

while True:
    change_ip(interface)
    time.sleep(3)
