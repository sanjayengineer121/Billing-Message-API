from flask import Flask, render_template,json,request
from enum import Enum
from flask_sqlalchemy import SQLAlchemy
import os
import flask
import webbrowser
import logging
import requests
import datetime
now = datetime.datetime.now()

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI']='sqlite:///sales.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(application)

class TODO(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    Mobile=db.Column(db.Integer,nullable=False)
    Name=db.Column(db.String(500),nullable=False)
    Msg=db.Column(db.String(2000),nullable=False)
    Price=db.Column(db.Integer,nullable=False)
    Voucher=db.Column(db.String(8),nullable=False)
    date=db.Column(db.String(10),nullable=False)
    
    
    def __repr__(self) -> str:
        return f'{self.sno} - {self.title}'

    

db.create_all()







@application.route("/tallymsg")
def demo_world():
    mobile = request.args.get('mobile')
    message = request.args.get('message')
    attach = request.args.get('attach')
    print(message)
    print(mobile)
    webbrowser.open(attach)
    
    target = "Rs."
    words = message.split()

    for i,w in enumerate(words):
        if w == target:
            prch=(words[i+1])
            print('=======================|PRICE|===============================')
            print("RS",prch)
    target = 'Sir,'
    for i,w in enumerate(words):
        if w == target:
            name=(words[i+1])
            print("==============================|NAME|=============================")
            print(name)

    target = 'No'
    for i,w in enumerate(words):
        if w == target:
            vch=(words[i+1])
            print('===============================|VOUCHER NO.===============================')
            print(vch)

    target = 'Dated' or "on"
    for i,w in enumerate(words):
        if w == target:
            dat=(words[i+2])
            print("======================================|DATE|================================")
            d1=words[i+2]
            d2=words[i+1]
    
            file = open('geek.txt','a')
            file.write("\n\n===============================================================================\n\n")
            file.write("======================================|mobile|=================================\n")
            file.write(mobile)
            file.write("\n====================================|SALES MSG|================================\n")
            file.write(message)
            file.write("\n======================================|PURCHASE|===============================\n")
            file.write(prch)
            file.write("\n===================================|VOUCHER NO|================================\n")
            file.write(vch)
            file.write("\n======================================|DATE|===================================\n")
            file.write(d1)
            file.write("\n======================================|NAME|====================================\n")
            file.write(name)
            file.write("\n\n===============================================================================\n\n")
            file.close()

            file = open('current.txt','w')
            file.write("\n\n===============================================================================\n\n")
            file.write("======================================|mobile|=================================\n")
            file.write(mobile)
            file.write("\n====================================|SALES MSG|================================\n")
            file.write(message)
            file.write("\n======================================|PURCHASE|===============================\n")
            file.write(prch)
            file.write("\n===================================|VOUCHER NO|================================\n")
            file.write(vch)
            file.write("\n======================================|DATE|===================================\n")
            file.write(d1)
            file.write("\n======================================|NAME|====================================\n")
            file.write(name)
            file.write("\n\n===============================================================================\n\n")
            file.close()
            sale=TODO(Mobile=mobile,Name=name,Msg=message,Price=prch,Voucher=vch,date=d1)
            db.session.add(sale)
            db.session.commit()

            Api="http://127.0.0.1:8082/send_att?mobile="+mobile+"&message="+message+"&attach="+attach
            whatsAppHitApi = requests.get(Api)
            mobile1='6388574919'
            Api="http://127.0.0.1:8082/send_att?mobile="+mobile1+"&message="+message+"&attach="+attach
            whatsAppHitApi = requests.get(Api)
            
        

    return "HELLO"

@application.route("/margsms")
def demo_world1():
    mobile = request.args.get('mobile')
    message = request.args.get('message')
    attach = request.args.get('attach')
    print('============================================================\n')
    print(mobile)
    print('============================================================\n')
    print(message)
    str=message.split()
    
    print(str)
   
    
    target = 'Patient'
    for i,w in enumerate(str):
        if w == target:
            cust=(str[i+1])
            print('===============================|NAME.===============================')
            print(cust)

    target = 'Bill'
    for i,w in enumerate(str):
        if w == target:
            vch=(str[i+1])
            print('===============================|VOUCHER NO.===============================')
            print(vch)

    target = "Bill"
    for i,w in enumerate(str):
        if w == target:
            dat=(str[i+2])
            print("======================================|DATE|================================")
            print(dat)
    target='Patient'
    for i,w in enumerate(str):
        if w == target:
            amo=(str[i-1])
            print("==============================|Amount|=============================")
            print(amo)

    print('=======================|Payment Mode|===============================')
    print(str[0])

    file = open('current.txt','w')
    file.write("------------------------Marg Bills--------------------------------------------------------")
    file.write("\n\n===============================================================================\n\n")
    file.write("======================================|mobile|=================================\n")
    file.write(mobile)
    file.write("\n====================================|SALES MSG|================================\n")
    file.write(message)
    file.write("\n======================================|SALES AMOUNT|===============================\n")
    file.write(amo)
    file.write("\n===================================|VOUCHER NO|================================\n")
    file.write(vch)
    file.write("\n======================================|DATE|===================================\n")
    file.write(dat)
    file.write("\n======================================|NAME|====================================\n")
    file.write(cust)
    file.write("\n======================================|Mode Of Payment|====================================\n")
    file.write(str[0])
    file.write("\n\n===============================================================================\n\n")
    file.close()
    file = open('geek.txt','a')
    file.write("------------------------Marg Bills--------------------------------------------------------")
    file.write("\n\n===============================================================================\n\n")
    file.write("======================================|mobile|=================================\n")
    file.write(mobile)
    file.write("\n====================================|SALES MSG|================================\n")
    file.write(message)
    file.write("\n======================================|SALES AMOUNT|===============================\n")
    file.write(amo)
    file.write("\n===================================|VOUCHER NO|================================\n")
    file.write(vch)
    file.write("\n======================================|DATE|===================================\n")
    file.write(dat)
    file.write("\n======================================|NAME|====================================\n")
    file.write(cust)
    file.write("\n======================================|Mode Of Payment|====================================\n")
    file.write(str[0])
    file.write("\n\n===============================================================================\n\n")
    file.close()

    sale=TODO(Mobile=mobile,Name=cust,Msg=message,Price=amo,Voucher=vch,date=dat)
    db.session.add(sale)
    db.session.commit()
    Api="http://127.0.0.1:8082/send_att?mobile="+mobile+"&message="+message+"&attach="+attach
    whatsAppHitApi = requests.get(Api)
    mobile1='6388574919'
    Api="http://127.0.0.1:8082/send_att?mobile="+mobile1+"&message="+message+"&attach="+attach
    whatsAppHitApi = requests.get(Api)
    
    return "HELLO"

@application.route("/busysms")
def demo_world2():
    mobile = request.args.get('mobile')
    message = request.args.get('message')
    print('============================================================\n')
    print(mobile)
    print('============================================================\n')
    print(message)
    str=message.split()
    print(str)

    target = 'Dear'
    for i,w in enumerate(str):
        if w == target:
            cust=(str[i+1])
            print('===============================|NAME.===============================')
            print(cust)

    target = 'attached'
    for i,w in enumerate(str):
        if w == target:
            vch=(str[i+1])
            print('===============================|VOUCHER TYPE.===============================')
            print(vch)

    target='Rs'
    for i,w in enumerate(str):
        if w == target:
            amo=(str[i+1])
            print("==============================|Amount|=============================")
            print(amo)

    file = open('current.txt','w')
    file.write("------------------------Busy Bills--------------------------------------------------------")
    file.write("\n\n===============================================================================\n\n")
    file.write("======================================|mobile|=================================\n")
    file.write(mobile)
    file.write("\n====================================|SALES MSG|================================\n")
    file.write(message)
    file.write("\n======================================|SALES AMOUNT|===============================\n")
    file.write(amo)
    file.write("\n===================================|VOUCHER TYPE|================================\n")
    file.write(vch)
    file.write("\n======================================|DATE|===================================\n")
    file.write(str(now))
    file.write("\n======================================|NAME|====================================\n")
    file.write(cust)
    file.write("\n\n===============================================================================\n\n")
    file.close()
    file = open('geek.txt','a')
    file.write("------------------------Marg Bills--------------------------------------------------------")
    file.write("\n\n===============================================================================\n\n")
    file.write("======================================|mobile|=================================\n")
    file.write(mobile)
    file.write("\n====================================|SALES MSG|================================\n")
    file.write(message)
    file.write("\n======================================|SALES AMOUNT|===============================\n")
    file.write(amo)
    file.write("\n===================================|VOUCHER NO|================================\n")
    file.write(vch)
    file.write("\n======================================|DATE|===================================\n")
    file.write(str(now))
    file.write("\n======================================|NAME|====================================\n")
    file.write(cust)
    file.write("\n\n===============================================================================\n\n")
    file.close()

    sale=TODO(Mobile=mobile,Name=cust,Msg=message,Price=amo,Voucher=vch,date=str(now))
    db.session.add(sale)
    db.session.commit()

@application.route("/", methods = ['GET', 'POST'])
def home():
    
    return flask.send_file("current.txt")

@application.route('/sales', methods = ['GET', 'POST'])
def uploader():
    return flask.send_file("geek.txt")


 

if __name__=="__main__":
    application.run(debug=True,port=8000)
    
