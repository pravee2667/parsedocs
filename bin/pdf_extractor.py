# -*- coding: utf-8 -*-

import PyPDF2
from bin import loader

def pdf_txt(file):
    txt=list()
    fileobj=open(file, 'rb') 
    pdfReader = PyPDF2.PdfFileReader(fileobj) 
    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page) 
        txt.append(pageObj.extractText()) 
    return txt
            
        
def pdf_extract_skills(pdftext,skills=set()):
    conf=loader.load_conf()
    skills_list=conf['skills']
    print(skills_list)
    #pdf_text="".join(pdftext)
    #print(pdf_text)
    if type(pdftext) is list:
        pdf_text="".join(pdftext)
        for word in pdf_text.split():
            if word.lower() in skills_list:
                print(word)
                skills.add(word)
        return skills
    else:
        for word in pdftext.split():
            if word.lower() in skills_list:
                print(word)
                skills.add(word)
        return skills
            
    