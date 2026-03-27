import json
from pathlib import Path
import re



def paddy(photo):
    from paddleocr import PaddleOCR
    ocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False, lang='ru')

    # Run OCR inference on a sample image 
    result = ocr.predict(
        input=photo)

    # Visualize the results and save the JSON results
    for res in result:
        res.save_to_img("output")
        res.save_to_json("output")
        

def get_img_text(in_img):
    print('get_img_____', in_img)
    paddy(in_img)
    name = Path(in_img).stem
    with open (f'output/{(name)}_res.json') as jfile:
        jfile = json.load(jfile)
    text_list = jfile['rec_texts']
    new_list = []
    temp_string = ''
    year = r'18\d{2}|19\d{2}'
    author = r'[А-Я]\.[А-Я]\. \w+|[А-Я]\.[А-Я]\.\w+|[А-Я]\.\w{3,20}'
    for each in text_list:
        if re.search(r"^\d{4,6}|^\w\.\d{4,5}", each) and each[:2] != '18' and each[:2] != '19':
            new_list.append(temp_string)
            temp_string = ''
        if each.strip() and text_list[-1] != each:
            temp_string += each
        if text_list[-1] == each:
            temp_string += each
            new_list.append(temp_string)
    
    end_list = []
    temp_dict = {'year':'', 'author':'', 'title':''}

    for each in new_list:
        if re.search(year, each):
            temp_dict['year'] = ' '.join(set(re.findall(year, each)))
        if re.search(author, each):
            temp_dict['author'] = ' '.join(set(re.findall(author, each)))
        if each.strip():
            temp_dict['title'] = each

        if ''.join(list(temp_dict.values())):
            end_list.append(temp_dict.copy())
            temp_dict = {'year':'', 'author':'', 'title':''}

    return end_list


if __name__ == "__main__":
    img_orig = 'img/img_all.jpg'
    get_img_text(img_orig)