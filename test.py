from flask import Flask, render_template,json,request,redirect,url_for
from enum import Enum
from flask_sqlalchemy import SQLAlchemy
import os
import flask
import webbrowser
import logging
import requests
import datetime
import glob
from datetime import date
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import decode_header
import platform
import socket
import sys
print(platform.node())


now = datetime.datetime.now()

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI']='sqlite:///sales.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(application)







class TODO(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    Mobile=db.Column(db.Integer,nullable=False)
    Msg=db.Column(db.String(2000),nullable=False)
    date=db.Column(db.String(10),nullable=False)
    
    def to_dict(self):
        return {
            'sno': self.sno,
            'Mobile': self.Mobile,
            'Msg': self.Msg,
            'date': self.date
        }
    def __repr__(self) -> str:
        return f'{self.sno}'

    


    

db.create_all()
file = open('number1.txt','r')  
with open("number1.txt") as mytxt:
    for line in mytxt:
        print (line)



 
with open('config.json', 'r') as openfile:
            port = json.load(openfile)
            port["port"]

with open('marg.json', 'r') as openfile:
            path1 = json.load(openfile)
            path1["path"]

list_of_files = glob.glob(path1["path"]+'emailserver/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)



@application.route("/send_att")
def demo_world():
    mobile = request.args.get('mobile')
    message = request.args.get('message')
    attach = request.args.get('attach')
    print(message)
    print(mobile)
    #webbrowser.open(attach)

    words = message.split()
    print(words)


    file = open('geek.txt','a')
    file.write("\n\n===============================================================================\n\n")
    file.write("======================================|mobile|=================================\n")
    file.write(mobile)
    file.write("\n====================================|SALES MSG|================================\n")
    file.write(message)
    file.write("\n======================================|DATE|===================================\n")
    file.write(str(now))
    file.write("\n\n===============================================================================\n\n")
    file.close()

    file = open('current.txt','w')
    file.write("\n\n===============================================================================\n\n")
    file.write("======================================|mobile|=================================\n")
    file.write(mobile)
    file.write("\n====================================|SALES MSG|================================\n")
    file.write(message)
    file.write("\n======================================|DATE|===================================\n")
    file.write(str(now))
    file.write("\n\n===============================================================================\n\n")
    file.close()
    s=socket.gethostname()
    print(s)
    IP_addres = socket.gethostbyname(s)

    if attach==None:
        Api="http://127.0.0.1:"+str(port["port"])+"/send?mobile="+mobile+"&message="+message
        whatsAppHitApi = requests.get(Api)
        with open("number1.txt") as mytxt:
            for line in mytxt:
                print (line)
                Api="http://127.0.0.1:"+str(port["port"])+"/send?mobile="+line+"&message="+message
                whatsAppHitApi = requests.get(Api)
    else:
        Api="http://127.0.0.1:"+str(port["port"])+"/send_att?mobile="+mobile+"&message="+message+"&attach="+attach
        whatsAppHitApi = requests.get(Api)
        with open("number1.txt") as mytxt:
            for line in mytxt:
                print (line)
                Api="http://127.0.0.1:"+str(port["port"])+"/send_att?mobile="+line+"&message="+message+"&attach="+attach
                whatsAppHitApi = requests.get(Api)
    #Api="http://127.0.0.1:"+str(port["port"])+"/send_att?mobile="+line1+"&message="+message+"&attach="+attach
    #whatsAppHitApi = requests.get(Api)

    sale=TODO(Mobile=mobile,Msg=message,date=date.today())
    db.session.add(sale)
    db.session.commit()        
    COMMASPACE = ', '
    def main():
        sender = 'sanjay.yadav@ensowt.com'
        gmail_password = 'sanjZ1234@'
        recipients = ['sanjayyadav7071@gmail.com']
        
        # Create the enclosing (outer) message
        outer = MIMEMultipart()
        outer['Subject'] = mobile + '\033[1m' + "Please check your bill"
        outer['To'] = COMMASPACE.join(recipients)
        outer['From'] = sender
        outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

        # List of attachments
        attachments = [attach]

        # Add the attachments to the message
        for file in attachments:
            try:
                with open(file, 'rb') as fp:
                    msg = MIMEBase('application', "octet-stream")
                    msg.set_payload(fp.read())
                encoders.encode_base64(msg)
                msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
                outer.attach(msg)
            except:
                print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
                raise

        composed = outer.as_string()

        # Send the email
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as s:
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(sender, gmail_password)
                #s.sendmail(sender, recipients, composed)
                s.close()
            print("Email sent!")
        except:
            print("Unable to send the email. Error:")
            raise

    if __name__ == '__main__':
        main()        
     
    return "HELLO"


@application.route("/margerp")
def demo_world1():
    s=socket.gethostname()
    print(s)
    IP_addres = socket.gethostbyname(s)
    mobile = request.args.get('mobile')
    message = request.args.get('message')
    print(latest_file)
    print('============================================================\n')
    print(mobile)
    print('============================================================\n')
    print(message)

    #webbrowser.open(latest_file)
   

    words = message.split()
    
    
    file = open('geek.txt','a')
    file.write("\n\n===============================================================================\n\n")
    file.write("======================================|mobile|=================================\n")
    file.write(mobile)
    file.write("\n====================================|SALES MSG|================================\n")
    file.write(message)
    file.write("\n======================================|DATE|===================================\n")
    file.write(str(now))
    file.write("\n\n===============================================================================\n\n")
    file.close()

    file = open('current.txt','w')
    file.write("\n\n===============================================================================\n\n")
    file.write("======================================|mobile|=================================\n")
    file.write(mobile)
    file.write("\n====================================|SALES MSG|================================\n")
    file.write(message)
    file.write("\n======================================|DATE|===================================\n")
    file.write(str(now))
    file.write("\n\n===============================================================================\n\n")
    file.close()
    welcome ="Thanks for shoping"      
    Api="http://127.0.0.1"+str(port["port"])+"/send_att?mobile="+mobile+"&message="+message+"&attach="+latest_file
    whatsAppHitApi = requests.get(Api)
    with open("number1.txt") as mytxt:
        for line in mytxt:
            print (line)
            Api="http://127.0.0.1:"+str(port["port"])+"/send_att?mobile="+line+"&message="+message+"&attach="+latest_file
            whatsAppHitApi = requests.get(Api)
    #Api="http://127.0.0.1:"+str(port["port"])+"/send_att?mobile="+line1+"&message="+message+"&attach="+attach
    #whatsAppHitApi = requests.get(Api)

    sale=TODO(Mobile=mobile,Msg=message,date=date.today())
    db.session.add(sale)
    db.session.commit()

    COMMASPACE = ', '
    def main():
        sender = 'sanjay.yadav@ensowt.com'
        gmail_password = 'sanjZ1234@'
        recipients = ['sanjayyadav7071@gmail.com']
        
        # Create the enclosing (outer) message
        outer = MIMEMultipart()
        outer['Subject'] = 'dsgagfn sdgjfhgjkzsg jsdf'
        outer['To'] = COMMASPACE.join(recipients)
        outer['From'] = sender
        outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

        # List of attachments
        attachments = ['E:\MARGERP\emailserver\State Bank Of India-18.pdf']

        # Add the attachments to the message
        for file in attachments:
            try:
                with open(file, 'rb') as fp:
                    msg = MIMEBase('application', "octet-stream")
                    msg.set_payload(fp.read())
                encoders.encode_base64(msg)
                msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
                outer.attach(msg)
            except:
                print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
                raise

        composed = outer.as_string()

        # Send the email
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as s:
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(sender, gmail_password)
                s.sendmail(sender, recipients, composed)
                s.close()
            print("Email sent!")
        except:
            print("Unable to send the email. Error:")
            raise

    if __name__ == '__main__':
        main()        

    return "HELLO"

@application.route("/emailadd", methods = ['GET', 'POST'])
def emailadd():
    emailid=Path = request.form.get("emailid")
    password=Path = request.form.get("pass")
    import json

    desc={
	 "email":emailid,
	 "pass": password,
        }

    with open("example.json", "w",encoding='utf-8') as outfile:

        json.dump(desc, outfile, ensure_ascii=False, indent=4)

    return redirect(url_for("index"))

@application.route("/pramote", methods = ['GET', 'POST'])
def pramote():
    message = request.form.get("message")
    latest_file=request.form.get("file")
    import subprocess
    subprocess.Popen(["notepad","number1.txt"])
    line='6388574919'
    Api="http://127.0.0.1:8086"+"/send_att?mobile="+line+"&message="+message+"&attach="+latest_file
    whatsAppHitApi = requests.get(Api)


    
    
 
                
    
    

    return "done"

  



    

    





@application.route("/current", methods = ['GET', 'POST'])
def home():
    
    return flask.send_file("current.txt")

@application.route('/sales', methods = ['GET', 'POST'])
def uploader():
    return flask.send_file("geek.txt")


@application.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('data.html', title='Data-Table')


@application.route('/email', methods = ['GET', 'POST'])
def email():
    return render_template('index.html')

@application.route('/pramotion', methods = ['GET', 'POST'])
def pramotion():
    return render_template('index1.html')




@application.route('/api/data')
def data():
    query = TODO.query

    # search filter
    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            TODO.sno.like(f'%{search}%'),
            TODO.Mobile.like(f'%{search}%'),
        ))
    total_filtered = query.count()

    # sorting
    order = []
    i = 0
    while True:
        col_index = request.args.get(f'order[{i}][column]')
        if col_index is None:
            break
        col_name = request.args.get(f'columns[{col_index}][data]')
        if col_name not in ['sno', 'Mobile']:
            col_name = 'Mobile'
        descending = request.args.get(f'order[{i}][dir]') == 'desc'
        col = getattr(TODO, col_name)
        if descending:
            col = col.desc()
        order.append(col)
        i += 1
    if order:
        query = query.order_by(*order)

    # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    query = query.offset(start).limit(length)

    # response
    return {
        'data': [todo.to_dict() for todo in query],
        'recordsFiltered': total_filtered,
        'recordsTotal': TODO.query.count(),
        'draw': request.args.get('draw', type=int),
    }


    
if __name__ == '__main__':
    application.debug = True
    url="http://127.0.0.1:"+str(8086)+"/"
    webbrowser.open_new(url)
    application.run(host="0.0.0.0",port=8086) #host="0.0.0.0" will make the page accessable
                            #by going to http://[ip]:5000/ on any computer in 
                            #the network.

    
    
    
