# -*- coding: utf-8 -*-

import requests
import json
import smtplib

def Send_email(invite_link,user_mail):
    body = 'Subject: Interview invitation from Pactera EDGE .\nDear ContactName, \n\n' + 'Please join the interview from the given link below at your selected time\n'+invite_link + '\n\n\n\n Thanks,\nSunil'
    try:
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    except Exception as e:
        print(e)
        smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465) 
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('banoth.sunil@pacteraedge.com', "Sunil@1913") 
    smtpObj.sendmail('banoth.sunil@pacteraedge.com', user_mail, body)
    print("Invitation has sent to user successfully")
    smtpObj.quit()

def Get_roles(skills):
    url='https://preptalkoutlookcal.azurewebsites.net/Skills/'
    U_Skills=["Python","Java"]
    data={
            "Skills":skills
         }
    print("Data {}".format(data))
    roles=requests.post(url,json=data)
    return roles
    
def Get_slots(role):
    url='https://preptalkoutlookcal.azurewebsites.net/ExtractFreeSlots/'
    print(role)
    free = requests.post(url, json = role)

    return free.text

def Schedule_meet(role,Date,Time):
    url='https://preptalkoutlookcal.azurewebsites.net/ScheduleEvent/'
#    Date=input()
#    Time=input()
    data={
        "Role":role,
        "Date": Date,
        "Time": Time
    }

    meet = requests.post(url, json = data)
    return json.loads(meet.text)["joinUrl"]


#skills = [item for item in input().split()] 

#Get_roles()
#role=input()
#user_mail=input()
#Get_slots()
#link=Schedule_meet()
#Send_email(link)
