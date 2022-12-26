import requests, random, time
from bs4 import BeautifulSoup


ua = open('ua.txt', 'r')
split_ua = ua.read().split("\n")
ua = random.choice(split_ua)

cookies = {
    'flash': '',
    '_ga_RWP85XL4SC': 'GS1.1.1671922198.3.1.1671922439.53.0.0',
    '_ga': 'GA1.2.1410604696.1671911504',
    'amp_bc6a9b': 'c2c47680-dc47-4dcc-9e9d-275c4f847412R...1gl35895n.1gl35flio.0.1.1',
    '_gid': 'GA1.2.1667066500.1671911505',
    '__gads': 'ID=0cc3cc96e79987e0-2205a6fb03d90028:T=1671911518:RT=1671911518:S=ALNI_MYKj0JE8t6P2NssqnTsZC4qbFVwSA',
    '__gpi': 'UID=00000b96bd2d238a:T=1671911518:RT=1671911518:S=ALNI_Ma65_7hyOusvmENDJpPXwPT8MKxhA',
    '_gat_UA-2336519-21': '1',
}

headers = {
    'Accept': 'text/html',
    'User-Agent': ua
}

def main(ip_address, port, country_code, anonymity):
    get_ip_route = requests.get('https://ipinfo.io/{}'.format(ip_address), headers=headers, cookies=cookies)
    response_get_ip_route = BeautifulSoup(get_ip_route.content, 'html.parser')
    # get route from ip address
    div_ip_range = response_get_ip_route.find_all('div', class_="ml-2")
    # get ip address lain di proxy yang aktif, example: site.com/ISP/{IP_ADDRESS}
    if len(div_ip_range) >= 0:
        link_ip_route = BeautifulSoup(str(div_ip_range[-1]), 'html.parser').a.get('href')
        get_other_ip = requests.get('https://ipinfo.io{}'.format(link_ip_route), headers=headers, cookies=cookies)
        list_other_ip = BeautifulSoup(get_other_ip.content, 'html.parser').find_all('a', class_='text-nowrap charcoal-link')
        # loop
        for loop_ip in list_other_ip:
            print('{}|{}|{}|{}|{}'.format(loop_ip.string, port, country_code, anonymity, 'Unknown'))
            save_result = open('results.txt', 'a')
            save_result.write("{}|{}|{}|{}|{}\n".format(loop_ip.string, port, country_code, anonymity, 'Unknown'))
            save_result.close()
            time.sleep(100/1000)


if __name__ == "__main__":
    main()