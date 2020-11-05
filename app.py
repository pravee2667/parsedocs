# -*- coding: utf-8 -*-

import spacy
#import re
#import sys
from spacy.matcher import Matcher 
from docx.api import Document
from bin import extractor as ex
import logging
from bin import linkedin

from flask import Flask,request,session,jsonify

app=Flask(__name__)
app.secret_key="sfsdfdsfdsf"
nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)   
 
@app.route('/home')
def home():
    return "PrepTalk Hiring"

@app.route('/upload',methods=['POST','GET'])
def parse_doc():
    if request.method=='POST':
        filename=request.files['img']
        #print(filename)
        txt=list()
        logging.getLogger().setLevel(logging.INFO)
        logging.info('File Name {}'.format(filename))
        fileextens=filename.filename.split('.')[1]
        print(fileextens)
        if fileextens=='docx':
            logging.info('File name ends with docx')
            doc=Document(filename)
            for para in doc.paragraphs:
                txt.append(para.text)
            full_t= ' '.join(txt)
            name_e=ex.name_extraction(full_t)
            session['name_session']=name_e
            logging.info('Extracted Name {}'.format(name_e))
            
            mob=ex.extract_mob_number(full_t)
            session['mob_session']=mob
            logging.info('Extracted Mobile  {}'.format(mob))
            
            mail=ex.extract_mail(full_t)
            session['mail_session']=mail
            logging.info('Extracted mail {}'.format(mail))
            print(session.get('mail_session'))
            skills=ex.extract_skills(doc)
            logging.info('Extracted Skills {}'.format(skills))
            session['skills_session']=skills
            
            
            if not mail or not name_e  or not mob  or not skills: 
                
                txt_doc=ex.txt_extraction(filename)
            if not mob:
                mob_doc=ex.extract_mob_number(txt_doc)
                print(mob_doc)
            if not mail:
                mail_doc=ex.extract_mail(txt_doc)
                print(mail_doc)
            if not name_e:
                name_doc=ex.name_extraction(txt_doc)
                print(name_doc)
            if not skills:
                
                url=ex.extract_linkedinurl(txt_doc)
                skills=linkedin.skills_linkdn(url)
                print(skills)
        print("skills")    
        return "Skills"
     
    return "File Not Uploaded"

@app.route('/mail')            
def mail_extract():
    mail=session.get('mail_session')
    print(mail)
    return "mail"
    
#def execute(inp,txt=[]):
#    logging.getLogger().setLevel(logging.INFO)
#    filename=inp[1]
#    logging.info('File Name {}'.format(filename))
#    if filename.endswith('.docx'):
#        logging.info('File name ends with docx')
#        doc=Document(filename)
#        for para in doc.paragraphs:
#            txt.append(para.text)
#        full_t= ' '.join(txt)
#        name_e=ex.name_extraction(full_t)
#        logging.info('Extracted Name {}'.format(name_e))
#        
#        mob=ex.extract_mob_number(full_t)
#        logging.info('Extracted Mobile  {}'.format(mob))
#        
#        mail=ex.extract_mail(full_t)
#        logging.info('Extracted mail {}'.format(mail))
#        
#        skills=ex.extract_skills(doc)
#        logging.info('Extracted Skills {}'.format(skills))
#        
#        
#        if not mail or not name_e  or not mob  or not skills:   
#            txt_doc=ex.txt_extraction(filename)
#        if not mob:
#            mob_doc=ex.extract_mob_number(txt_doc)
#            print(mob_doc)
#        if mail=='Not Found':
#            mail_doc=ex.extract_mail(txt_doc)
#            print(mail_doc)
#        if not name_e:
#            name_doc=ex.name_extraction(txt_doc)
#            print(name_doc)
#        if not skills:
#            url=ex.extract_linkedinurl(txt_doc)
#            skills=linkedin.skills_linkdn(url)
#            print(skills)
            
            
            
            
      

        
#def txt_extraction(file):
#    temp = docx2txt.process(file)
#    text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
#    full_t= ' '.join(text)
#    return full_t
#    
#    
#def name_extraction(resume_text):
#    nlp_text = nlp(resume_text)
#    
#    # First name and Last name are always Proper Nouns
#    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
#    
#    matcher.add('NAME', None, pattern)
#    
#    matches = matcher(nlp_text)
#
#    for match_id, start, end in matches:
#        span = nlp_text[start:end]
#        span.text
#    return nlp_text[0:2]
#
#
#
#def extract_mob_number(text):
#    phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), text)
#    
#    if phone:
#        number = ''.join(phone[0])
#        if len(number) > 10:
#            return '+' + number
#        else:
#            return number
#
#
#def extract_mail(email):
#    email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", email)
#    #print(email)
#    if email:
#        try:
#            return email[0].split()[0].strip(';')
#        except IndexError:
#            return None
#
#def iter_headings(paragraphs):
#    for i in range(0,len(paragraphs)):
#        if paragraphs[i].style.name.startswith('Heading'):
#            yield paragraphs[i],i
#
#
#def extract_skills(doch,aft=[],skills=[]):
#    for heading,i in iter_headings(doch.paragraphs):
#        if 'Skills' in heading.text :
#            for j in range(i+1,len(doch.paragraphs)):
#                #print(doch.paragraphs[j].text)
#                aft.append(doch.paragraphs[j].text)
#                txt=doch.paragraphs[j].text
#                if doch.paragraphs[j].style.name.startswith('Heading'):
#                    break
#                if not txt:
#                    continue
#                else:
#                    if ':' in txt :
#                        word=txt.split(':')
#                        skills.append(word[1])
#                    else:
#                        skills.append(txt)    
#            return skills
#    

    
    
if __name__=="__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
    #execute(sys.argv)