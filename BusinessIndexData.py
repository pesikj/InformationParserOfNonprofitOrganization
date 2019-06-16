import requests
import urllib.request, json, re

def load_organizational_data(identification_number):
    address = 'https://or.justice.cz/ias/ui/rejstrik-$firma?ico={0}'.format(identification_number)
    with urllib.request.urlopen(address) as url:
        page = url.read().decode('utf-8')
        detail_page_pattern = r'subjektId=\d*'
        result = re.search(detail_page_pattern, page)
        zadost_string = result.group(0)
        print(zadost_string)
load_organizational_data(22758518)