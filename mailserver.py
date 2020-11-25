'''
as per requirement make changes in message,sender_email,password, receiver_email list (To list),cc_email(cc mail list)
host and port in  server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
mail subject in "subject"

Omkar.Rane

'''
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib,ssl



def testmail(EmployeeID,EmployeeName,EmployeePhone):  # write function parameters

    # sending system mail ID and password
    sender_email = "Put your mail address for sending mails"
    password = 'put here password' #put password here

    # receiver mail  To mail list

    receiver_email=['something@outlook.com','somethinhg@got.ac.in']

    # receiver_email=["abc@mail.COM","bhj@mail.COM","hjk@mail.COM","hj@mail.COM","uio@mail.COM","uio@mail.COM","rty@mail.COM" ]

     # cc_mail list

    cc_email = ['abs@outlook.com','cds@outlook.com']

    #cc_email = ['wer@mail.COM','JAYDEEP@mail.COM','arati@mail.com','SARFARAJ@mail.COM','GOURISANKAR.PATRA@mail.COM','ANURADHA@mail.COM','rajiv@mail.com','ROHIT@mail.COM','KULKARNI@mail.COM','PRANAV.K@mail.COM','KULKARNI@mail.COM']

    # subject of mail

    subject='TEST DONE BY OMKAR RANE'

     # message body here (make changes here)

    message='Dear all,\n'+'The below employee/family/both reported to be   Monitoring System\n''Employee ID -' +' '+ str(EmployeeID)+'\n''Name -'+' '+str(EmployeeName)+'\n''Reg. Mobile number - '+' '+str(EmployeePhone)+'\n''Thanks,\n''Systems'

    #print(body)

    msg = MIMEMultipart()
    msg['From']=sender_email

   
    msg['subject']=subject 
    message = "From: %s\r\n" % sender_email + "To: %s\r\n" % receiver_email + "CC: %s\r\n" % ",".join(cc_email) + "Subject: %s\r\n" % subject + "\r\n" + message
    receiver_email = receiver_email + cc_email

    #msg.attach(MIMEText(message,'plain'))


    try:
        # make changes here also in SMTP hostname and port based on SSL if required
        server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        server.starttls()
        server.ehlo()
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,message)
        print("MAIL SENT")
        server.close()
        return True
        
    except Exception as e:
        print("something is wrong with system"+str(e))
        return False




if __name__ == '__main__':
     testmail(123,"Omkar",420)


