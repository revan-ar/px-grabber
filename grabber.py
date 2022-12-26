import requests, re, time
from bs4 import BeautifulSoup
import ip_range

# Free Proxy Grabber
# Author: https://github.com/revan-ar

def banner():
    banner = """
\033[1;34;40m
8888888b. Y88b   d88P        .d8888b.                   888      888                       
888   Y88b Y88b d88P        d88P  Y88b                  888      888                       
888    888  Y88o88P         888    888                  888      888                       
888   d88P   Y888P          888        888d888  8888b.  88888b.  88888b.   .d88b.  888d888 
8888888P"    d888b          888  88888 888P"       "88b 888 "88b 888 "88b d8P  Y8b 888P"   
888         d88888b  888888 888    888 888     .d888888 888  888 888  888 88888888 888     
888        d88P Y88b        Y88b  d88P 888     888  888 888 d88P 888 d88P Y8b.     888     
888       d88P   Y88b        "Y8888P88 888     "Y888888 88888P"  88888P"   "Y8888  888

=================================Free Proxy Grabber v1.0====================================
[+] Author          : https://github.com/revan-ar
[+] Prefix Results  : IP Address|Port|Country|Anonymity|Last Checked
[+] Example         : 127.0.0.1|1337|ID|Elite Proxy|3 secs ago
============================================================================================
    \033[0;37;40m"""
    print(banner)

def main():
    get_proxy_fpl = requests.get('https://free-proxy-list.net/')
    res_proxy_fpl = BeautifulSoup(get_proxy_fpl.content, 'html.parser')
    list_proxy_fpl = res_proxy_fpl.find_all('tr')
    list_proxy_fpl.pop(0)

    for px_fpl in list_proxy_fpl:
        proxy_fpl = re.findall('<td>(.*?)</td>', str(px_fpl))
        detail_proxy_fpl = re.findall('<td class="hm">(.*?)</td>', str(px_fpl))
        if len(proxy_fpl) > 2 and len(detail_proxy_fpl) > 2:
            print('{}|{}|{}|{}|{}'.format(proxy_fpl[0], proxy_fpl[1], detail_proxy_fpl[0], proxy_fpl[3], detail_proxy_fpl[2]))
            save_result = open('results.txt', 'a')
            save_result.write("{}|{}|{}|{}|{}\n".format(proxy_fpl[0], proxy_fpl[1], detail_proxy_fpl[0], proxy_fpl[3], detail_proxy_fpl[2]))
            save_result.close()
            time.sleep(100/1000)

    for px_fpl in list_proxy_fpl:
        proxy_fpl = re.findall('<td>(.*?)</td>', str(px_fpl))
        detail_proxy_fpl = re.findall('<td class="hm">(.*?)</td>', str(px_fpl))
        if len(proxy_fpl) > 2 and len(detail_proxy_fpl) > 2:
            ip_range.main(proxy_fpl[0], proxy_fpl[1], detail_proxy_fpl[0], proxy_fpl[3])
            time.sleep(1)


if __name__ == "__main__":
    banner()
    time.sleep(2)
    main()