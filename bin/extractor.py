# -*- coding: utf-8 -*-

import logging

import spacy
import re

from spacy.matcher import Matcher 
#from docx.api import Document
from bin import loader
import docx2txt





nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)  

def name_extraction(resume_text):
    logging.info('Extracting name')
    nlp_text = nlp(resume_text)
    
    # First name and Last name are always Proper Nouns
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    
    matcher.add('NAME', None, pattern)
    
    matches = matcher(nlp_text)

    for match_id, start, end in matches:
        span = nlp_text[start:end]
        span.text
    return nlp_text[0:2]



def extract_mob_number(text):
    mob1=loader.Mob_Regex
    phone = re.findall(re.compile(mob1), text)   
    if phone:
        number = ''.join(phone[0])
        if len(number) > 10:
            return '+' + number
        else:
            return number
    


def extract_mail(email):
    email2=loader.Email_Regex3
    email_extract = re.findall(re.compile(email2), email)
    #print(email_extract)
    if email_extract: 
        try:
            #return email[0].split()[0].strip(';')
            return email_extract[0]
        except IndexError:
            return None
   

def iter_headings(paragraphs):
    for i in range(0,len(paragraphs)):
        if paragraphs[i].style.name.startswith('Heading'):
            yield paragraphs[i],i

def extract_linkedinurl(text):
    url=loader.linurl_Regex
    url_extract=re.findall(re.compile(url),text)
    if url_extract:
        return url_extract[0]
    
    

def extract_skills(doch,aft=[],skills=[]):
    for heading,i in iter_headings(doch.paragraphs):
        if 'Skills' in heading.text :
            for j in range(i+1,len(doch.paragraphs)):
                #print(doch.paragraphs[j].text)
                aft.append(doch.paragraphs[j].text)
                txt=doch.paragraphs[j].text
                if doch.paragraphs[j].style.name.startswith('Heading'):
                    break
                if not txt:
                    continue
                else:
                    if ':' in txt :
                        word=txt.split(':')
                        skills.append(word[1])
                    else:
                        skills.append(txt)    
            return skills

def txt_extraction(file):
    temp = docx2txt.process(file)
    text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
    full_t= ' '.join(text)
    return full_t
