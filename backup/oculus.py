import os 
import time
import json
# import easyocr
# from shiftlab_ocr.doc2text.reader import Reader
# import urllib
# from doctr.io import DocumentFile
# from doctr.models import kie_predictor
# from paddleocr import PaddleOCR
from pathlib import Path
import re





def easy(link):
    # Create an OCR reader object
    reader = easyocr.Reader(['ru'])
    # Read text from an image
    result = reader.readtext(link)
    # Print the extracted text
    for detection in result:
        print(detection[1])

def doct(photo):
    # Model
    model = kie_predictor(det_arch='db_resnet50', reco_arch='crnn_vgg16_bn', pretrained=True)
    # PDF
    doc = DocumentFile.from_images(photo)
    # Analyze
    result = model(doc)
    print(result)



def easy_2():
    reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
    result = reader.readtext('photo_1.jpg')
    reader = Reader()
    result = reader.doc2text("photo_1.png")
    print(result)


def shift(photo):
    urllib.request.urlretrieve(
    'https://raw.githubusercontent.com/konverner/shiftlab_ocr/main/demo_image.png',
    photo)
    reader = Reader()
    result = reader.doc2text(photo)
    print(result)

def paddy(photo):
    ocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False, lang='ru')

    # Run OCR inference on a sample image 
    result = ocr.predict(
        input=photo)

    # Visualize the results and save the JSON results
    for res in result:
        res.print()
        res.save_to_img("output")
        res.save_to_json("output")
        


def paddy_struct(photo):
    from pathlib import Path
    from paddleocr import PPStructureV3

    pipeline = PPStructureV3(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False, lang='ru'
    )

    # For Image
    output = pipeline.predict(
        input=photo,
    )

    # Visualize the results and save the JSON results
    for res in output:
        # res.print() 
        res.save_to_json(save_path="output") 
        res.save_to_markdown(save_path="output")  
        result = res


# photo = 'photo_1.jpg'
img_orig = 'img/img_all.jpg'
img_contrast = 'img/img_contrast.png'
img_upscale = 'img/img_upscale.png'
# img_upscale = 'img/4x-DWTP-DS-dat2-v3.png'
# easy(photo_hard)
# doct(photo)
# easy_2()
# shift(photo)
code_contrast = f'ffmpeg -i "{img_orig}" -vf eq=contrast=2 -y  {img_contrast}'
# os.system(code_contrast)
code_upscale = f'../vhs/realesrgan-ncnn-vulkan-20220424-macos/realesrgan-ncnn-vulkan -i {img_orig} -o {img_upscale} -m ../vhs/realesrgan-ncnn-vulkan-20220424-macos/models -n realesr-animevideov3 -s 2'
# os.system(code_upscale)
# paddy(img_orig)
name = Path(img_orig).stem
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
        print(each)
    else:
        temp_string += each
end_list = []
temp_dict = {}

for each in new_list:
    if re.search(year, each):
        temp_dict['year'] = ' '.join(set(re.findall(year, each)))
        temp_dict['author'] = ' '.join(set(re.findall(author, each)))
        temp_dict['title'] = str([re.sub(fin, ' ', each) for fin in set(re.findall(year, each)) ])
    end_list.append(temp_dict.copy())

print(end_list)

'''3.6650
-Всероссийская промышленная и худо-.
жественная выстоека: Н-Новгороді.
Горное дало и металургія на
18%ee0oc.
сійской промышленной и художественной
выставить 1896 года во Нижнемь-Новгоро-дло. Вып. 1 - 6
Спб, изд. Горн. Департамен.
та, 1897-1898.
6 т.
См.след. карт-'''