import requests
from bs4 import BeautifulSoup
import time
import os
import random
import sys 
import json
import re
from openpyxl import load_workbook


def save_file(file):
    with open('ris_file.gif', 'wb') as ris:
        ris.write(file)


def get_proxy():
    url='http://htmlweb.ru/json/proxy/get?api_key=befa1738418a4056c2d4b0eeddb08165'
    if not os.path.isfile('proxy_file.txt'):
        respose = requests.get(url)
        proxy_dict = respose.text
        with open('proxy_file.txt', 'w', encoding='utf-8') as proxy_file:
            proxy_file.write(proxy_dict)
    with open('proxy_file.txt', 'r', encoding='utf-8') as proxy_file:
        proxy_dict = json.loads(proxy_file.read())
    proxy_list = []
    for i in range(20):
        proxy_list.append({proxy_dict[str(i)]['type'].lower().split(',')[-1]:proxy_dict[str(i)]['name']})
    return proxy_list


def save_site(url, site_file, headers, params, cookies):
    source_folder = 'source/'
    site_file = os.path.join(source_folder, site_file)
    site_file = site_file if '.html' in site_file else f'{site_file}.html'
    if 'test' in ''.join(sys.argv):
        if not os.path.isdir(source_folder):
            os.mkdir(source_folder)
        if not os.path.isfile(site_file):
            req = requests.get(url = url, headers=headers, params=params, cookies=cookies, proxies=get_proxy()[random.randint(0, 19)])
            with open(site_file, 'w', encoding='utf-8') as file:
                file.write(req.text)
        with open(site_file, 'r', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
    else:
        time.sleep(random.uniform(0, 1))
        src = requests.get(url = url, headers=headers, params=params, cookies=cookies, proxies=get_proxy()[random.randint(0, 19)])
        soup = BeautifulSoup(src.text, 'lxml')
    return soup

def get_sheet(sheet_name, sheet_row='', status='Найдено'):
    workbook = load_workbook(sheet_name)
    sheet = workbook.active
    sheet_list = []
    for each_row in range(2, sheet.max_row+1):
        title = ''
        year = ''
        author = ''
        if any([cell.value is not None for cell in sheet[each_row]]):
            if sheet.cell(column=1, row=each_row).value != None:
                title = sheet.cell(column=1, row=each_row).value
            if sheet.cell(column=2, row=each_row).value != None:
                year = sheet.cell(column=2, row=each_row).value
            if sheet.cell(column=3, row=each_row).value != None:
                author = sheet.cell(column=3, row=each_row).value
            sheet_list.append({'title':title,
                                'year':year,
                                'author':author})
    if sheet_row:
        sheet.cell(row=1, column=4, value='Status')
        sheet.cell(row=sheet_row, column=4, value=status)
        workbook.save(sheet_name)
    return sheet_list

cookies = {
    'JSESSIONID': '8AF9A2A933CF523E0FF7D5898615262E',
    'rmfe1primo_https': 'rmfe1_https',
    '_ym_uid': '1766582875627199060',
    '_ym_d': '1766582875',
    '_ym_isad': '1',
    'JSESSIONID': '6865ECDF6C30F58E3A76D131108000C4',
    '__utma': '130077136.1544976882.1766751893.1766751893.1766751893.1',
    '__utmc': '130077136',
    '__utmz': '130077136.1766751893.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '_ym_visorc': 'b',
    'PRIMO_RT': 's=1766772959771&r=https%3A%2F%2Fprimo.nlr.ru%2Fprimo_library%2Flibweb%2Faction%2Fsearch.do%3Ffn%3Dsearch%26ct%3Dsearch%26initialSearch%3Dtrue%26mode%3DAdvanced%26tab%3Ddefault_tab%26indx%3D1%26dum%3Dtrue%26srt%3Drank%26vid%3D07NLR_VU1%26frbg%3D%26vl%2528199890271UI0%2529%3Dcreator%26vl%2528199890271UI0%2529%3Dtitle%26vl%2528199890271UI0%2529%3Dcreator%26vl%25281UIStartWith0%2529%3Dcontains%26vl%2528freeText0%2529%3D%25D0%2598%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25BE%25D0%25B2%2B%25D0%2592.%2B%25D0%2598.%26vl%2528boolOperator0%2529%3DAND%26vl%2528199949086UI1%2529%3Daddtitle%26vl%2528199949086UI1%2529%3Dtitle%26vl%2528199949086UI1%2529%3Daddtitle%26vl%25281UIStartWith1%2529%3Dcontains%26vl%2528freeText1%2529%3D%25D0%259F%25D0%25BE%25D0%25B4%25D0%25B3%25D0%25BE%25D1%2582%25D0%25BE%25D0%25B2%25D0%25BA%25D0%25B0%252C%2B%25D1%2580%25D0%25B5%25D0%25B4%25D0%25B0%25D0%25BA%25D1%2582%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25B8%25D0%25B5%2B%25D0%25B8%2B%25D0%25B0%25D0%25BD%25D0%25B0%25D0%25BB%25D0%25B8%25D0%25B7%2B%25D1%258D%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2582%25D1%2580%25D0%25BE%25D0%25BD%25D0%25BD%25D1%258B%25D1%2585%2B%25D1%2581%25D1%2585%25D0%25B5%25D0%25BC%26vl%2528boolOperator1%2529%3DAND%26vl%2528267247494UI2%2529%3Dlsr07%26vl%2528267247494UI2%2529%3Dtitle%26vl%2528267247494UI2%2529%3Dlsr07%26vl%25281UIStartWith2%2529%3Dcontains%26vl%2528freeText2%2529%3D1999%26vl%2528boolOperator2%2529%3DAND%26vl%2528267247768UI3%2529%3Dlsr24%26vl%2528267247768UI3%2529%3Dtitle%26vl%2528267247768UI3%2529%3Dlsr24%26vl%25281UIStartWith3%2529%3Dcontains%26vl%2528freeText3%2529%3D%26vl%2528boolOperator3%2529%3DAND%26vl%2528199950180UI4%2529%3Dbooks%26vl%2528199950185UI5%2529%3Dall_items%26vl%2528422913607UI6%2529%3Dall_items%26Submit%3D%25D0%259F%25D0%25BE%25D0%25B8%25D1%2581%25D0%25BA&p=QWERTY',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru,en;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://primo.nlr.ru/primo_library/libweb/action/search.do?fn=search&ct=search&initialSearch=true&mode=Advanced&tab=default_tab&indx=1&dum=true&srt=rank&vid=07NLR_VU1&frbg=&vl%28199890271UI0%29=creator&vl%28199890271UI0%29=title&vl%28199890271UI0%29=creator&vl%281UIStartWith0%29=contains&vl%28freeText0%29=&vl%28boolOperator0%29=AND&vl%28199949086UI1%29=addtitle&vl%28199949086UI1%29=title&vl%28199949086UI1%29=addtitle&vl%281UIStartWith1%29=contains&vl%28freeText1%29=&vl%28boolOperator1%29=AND&vl%28267247494UI2%29=lsr07&vl%28267247494UI2%29=title&vl%28267247494UI2%29=lsr07&vl%281UIStartWith2%29=contains&vl%28freeText2%29=&vl%28boolOperator2%29=AND&vl%28267247768UI3%29=lsr24&vl%28267247768UI3%29=title&vl%28267247768UI3%29=lsr24&vl%281UIStartWith3%29=contains&vl%28freeText3%29=&vl%28boolOperator3%29=AND&vl%28199950180UI4%29=books&vl%28199950185UI5%29=all_items&vl%28422913607UI6%29=all_items&Submit=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 YaBrowser/25.10.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "YaBrowser";v="25.10", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    # 'Cookie': 'JSESSIONID=8AF9A2A933CF523E0FF7D5898615262E; rmfe1primo_https=rmfe1_https; _ym_uid=1766582875627199060; _ym_d=1766582875; _ym_isad=1; JSESSIONID=6865ECDF6C30F58E3A76D131108000C4; __utma=130077136.1544976882.1766751893.1766751893.1766751893.1; __utmc=130077136; __utmz=130077136.1766751893.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ym_visorc=b; PRIMO_RT=s=1766772959771&r=https%3A%2F%2Fprimo.nlr.ru%2Fprimo_library%2Flibweb%2Faction%2Fsearch.do%3Ffn%3Dsearch%26ct%3Dsearch%26initialSearch%3Dtrue%26mode%3DAdvanced%26tab%3Ddefault_tab%26indx%3D1%26dum%3Dtrue%26srt%3Drank%26vid%3D07NLR_VU1%26frbg%3D%26vl%2528199890271UI0%2529%3Dcreator%26vl%2528199890271UI0%2529%3Dtitle%26vl%2528199890271UI0%2529%3Dcreator%26vl%25281UIStartWith0%2529%3Dcontains%26vl%2528freeText0%2529%3D%25D0%2598%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25BE%25D0%25B2%2B%25D0%2592.%2B%25D0%2598.%26vl%2528boolOperator0%2529%3DAND%26vl%2528199949086UI1%2529%3Daddtitle%26vl%2528199949086UI1%2529%3Dtitle%26vl%2528199949086UI1%2529%3Daddtitle%26vl%25281UIStartWith1%2529%3Dcontains%26vl%2528freeText1%2529%3D%25D0%259F%25D0%25BE%25D0%25B4%25D0%25B3%25D0%25BE%25D1%2582%25D0%25BE%25D0%25B2%25D0%25BA%25D0%25B0%252C%2B%25D1%2580%25D0%25B5%25D0%25B4%25D0%25B0%25D0%25BA%25D1%2582%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25B8%25D0%25B5%2B%25D0%25B8%2B%25D0%25B0%25D0%25BD%25D0%25B0%25D0%25BB%25D0%25B8%25D0%25B7%2B%25D1%258D%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2582%25D1%2580%25D0%25BE%25D0%25BD%25D0%25BD%25D1%258B%25D1%2585%2B%25D1%2581%25D1%2585%25D0%25B5%25D0%25BC%26vl%2528boolOperator1%2529%3DAND%26vl%2528267247494UI2%2529%3Dlsr07%26vl%2528267247494UI2%2529%3Dtitle%26vl%2528267247494UI2%2529%3Dlsr07%26vl%25281UIStartWith2%2529%3Dcontains%26vl%2528freeText2%2529%3D1999%26vl%2528boolOperator2%2529%3DAND%26vl%2528267247768UI3%2529%3Dlsr24%26vl%2528267247768UI3%2529%3Dtitle%26vl%2528267247768UI3%2529%3Dlsr24%26vl%25281UIStartWith3%2529%3Dcontains%26vl%2528freeText3%2529%3D%26vl%2528boolOperator3%2529%3DAND%26vl%2528199950180UI4%2529%3Dbooks%26vl%2528199950185UI5%2529%3Dall_items%26vl%2528422913607UI6%2529%3Dall_items%26Submit%3D%25D0%259F%25D0%25BE%25D0%25B8%25D1%2581%25D0%25BA&p=QWERTY',
}

params = {
    'fn': 'search',
    'ct': 'search',
    'initialSearch': 'true',
    'mode': 'Advanced',
    'tab': 'default_tab',
    'indx': '1',
    'dum': 'true',
    'srt': 'rank',
    'vid': '07NLR_VU1',
    'frbg': '',
    'vl(199890271UI0)': [
        'creator',
        'title',
        'creator',
        ],
    'vl(1UIStartWith0)': 'contains',
    'vl(freeText0)': 'а',
    'vl(boolOperator0)': 'AND',
    'vl(199949086UI1)': [
        'addtitle',
        'title',
        'addtitle',
    ],
    'vl(1UIStartWith1)': 'contains',
    'vl(freeText1)': '',
    'vl(boolOperator1)': 'AND',
    'vl(267247494UI2)': [
        'lsr07',
        'title',
        'lsr07',
    ],
    'vl(1UIStartWith2)': 'contains',
    'vl(freeText2)': '',
    'vl(boolOperator2)': 'AND',
    'vl(267247768UI3)': [
        'lsr24',
        'title',
        'lsr24',
        ],
    'vl(1UIStartWith3)': 'contains',
    'vl(freeText3)': '',
    'vl(boolOperator3)': 'AND',
    'vl(199950180UI4)': 'all_items',
    'vl(199950185UI5)': 'all_items',
    'vl(422913607UI6)': 'all_items',
    'Submit': 'Поиск',
}


xlsx_files = os.listdir()
xlsx_files = [ each for each in xlsx_files if '.xlsx' in each ]
for xlsx in xlsx_files:
    sheet_list = get_sheet(xlsx)
    print(sheet_list)
    for each_row in sheet_list:
        params['vl(freeText0)'] = each_row['author']
        params['vl(freeText1)'] = each_row['title']
        params['vl(freeText2)'] = each_row['year']
        cicle_count = 1 + len(each_row['title'].split())
        url = 'https://primo.nlr.ru/primo_library/libweb/action/search.do'
        search_page = f"search_page_{re.sub('[:,. ]', '_', each_row['author'])}_{len(each_row['title'])}.html"
        for search_iter in range(cicle_count):
            print(params['vl(freeText0)'], params['vl(freeText1)'], params['vl(freeText2)'])
            soup = save_site(url, search_page, headers=headers, params=params, cookies=cookies)
            mark_folder = f"{xlsx.replace('.xlsx', '')}_rusmark_files"
            os.mkdir(mark_folder) if not os.path.isdir(mark_folder) else 1
            result_count = soup.find(id='resultsNumbersTile')
            result_count = result_count.text.strip().split('\n')[0]
            result_count = re.sub('[^0-9]', ' ', result_count).strip().split()
            result_count = int(result_count[-1])
            print('result_count -', result_count)
            if result_count > 0:
                cards = soup.find(class_='EXLResultsTable')
                cards = cards.find_all(class_=re.compile('EXLResultMediaTYPE'))
                card_list = []
                for each_card in cards:
                    link = each_card.find(class_='EXLResultTitle')
                    name = link.find('a').text
                    link = link.find('a').get('href')
                    media_type = each_card.find(class_='EXLThumbnailCaption').text
                    card_list.append({'name':name, 'link':link, 'nedia_type':media_type, 'search_link':''})
                break
            else:
                if len(params['vl(freeText0)'].split()) > 1:
                    params['vl(freeText0)'] = params['vl(freeText0)'].split()[0]
                elif len(params['vl(freeText1)'].split()) > 1:    
                    params['vl(freeText1)'] = ' '.join(params['vl(freeText1)'].split()[:-1])

        for each_dict in card_list[:1]:
            file_name =  re.sub('[:,.()\\ ]', '_', each_dict['name'])
            each_link = f"https://primo.nlr.ru/primo_library/libweb/action/{each_dict['link']}"
            soup = save_site(f'{each_link}.html', file_name, headers=headers, params=params, cookies=cookies)
            rusmarc = soup.find(string=re.compile('RUSMARC ISO2709'))
            rusmarc = rusmarc.parent.get('href')
            rusmarc = requests.get(rusmarc).content
            status = 'Найдено'
            if soup.find(string='Автор:'):
                author = soup.find(string='Автор:').parent.parent
                author = author.find('a').text
                author = re.sub('[:,.() ]', '_', author).replace('\\', '')
                print('file name -----------', file_name, '\n author ----------------', author)
                file_name = f"{author}_{file_name}"
            with open(os.path.join(mark_folder, f'{file_name}.mrc'), 'wb') as mark_file:
                mark_file.write(rusmarc)
            if len(card_list) > 1:
                status = f'{len(card_list)} Найдено'
            get_sheet(xlsx, sheet_row=sheet_list.index(each_row)+2, status=status)
            

# сколько может быть выдача?