import urllib.request, json, re

page_count = 1
address = 'http://dotace.plzensky-kraj.cz/verejnost/zadosti?_name=Zadosti&_search=false&nd=1560581767414&rows=25&page=1&sidx=&sord=asc'
with urllib.request.urlopen(address) as url:
    data = json.loads(url.read().decode('utf-8'))
    page_count = int(data['total'])

all_data = {}

for i in range(1, page_count):
    address = 'http://dotace.plzensky-kraj.cz/verejnost/zadosti?_name=Zadosti&_search=false&nd=1560581767414&rows=25&page={0}&sidx=&sord=asc'.format(i)
    with urllib.request.urlopen(address) as url:
        data = json.loads(url.read().decode('utf-8'))
        for row in data['rows']:
            converted_data = {}
            cell_data = row['cell']
            converted_data['program_name'] = cell_data['nazevtitulu']
            converted_data['program_year'] = cell_data['roktitulu']
            converted_data['subject_identification_number'] = cell_data['subjektic']
            converted_data['subject_name'] = cell_data['subjektnazev']
            converted_data['title_name'] = cell_data['nazevakce']
            converted_data['approved_amount'] = cell_data['schvalenacastka']
            converted_data['contract_signed_on'] = cell_data['datumpodpisusmlouvy']
            converted_data['request_status'] = cell_data['stavzadosti']
            cell_string = cell_data['buttons']

            zadost_pattern = r'/zadost/\d*/'
            result = re.search(zadost_pattern, cell_string)
            zadost_string = result.group(0)
            zadost_id_parsed = zadost_string.replace('/','').replace('zadost','')
            converted_data['request_id'] = int(zadost_id_parsed)
            all_data[int(zadost_id_parsed)] = converted_data

with open('data.json', 'w', encoding='utf-8') as fp:
    json.dump(all_data, fp, ensure_ascii=False, indent=4, sort_keys=True)