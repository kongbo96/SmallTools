import glob,os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import traceback
import re

def is_chinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False
def is_number(num):
    #判断是否纯数字
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = pattern.match(num)
    if result:
        return True
    else:
        return False

for base,dir,files in os.walk('./'):
    for file in files:
        if file[-3:].lower() == 'pdf' and (len(file) <= 20 and not is_chinese(file) or is_number(file[:-3])):
            file_path = base + '/' + file
            try:
                with open(file_path, 'rb') as fp:
                    parser = PDFParser(fp)
                    doc = PDFDocument(parser)
                title = doc.info[0]['Title'].decode('utf-8',errors='ignore')
                title = title.replace(':', '：')
                title = title.replace('\00','')
                title = title + '_' + file
                if len(title) >= 20:
                    title_path = base + '/' + title
                    print('Accomplished:',title_path)
                    os.rename(file_path,title_path)
            except:
                print('Failed:',file_path)
                traceback.print_exc()
            print()