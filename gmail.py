def mailreceipt(path):
    
    # libraries to be imported 
    import smtplib 
    from email.mime.multipart import MIMEMultipart 
    from email.mime.text import MIMEText 
    from email.mime.base import MIMEBase 
    from email import encoders 

    fromaddr = "BookMyMoviezz@gmail.com"
    toaddr =input('ENTER GMAIL ID TO GET RECEIPT: ')
    if '@gmail.com' not in toaddr:
        toaddr=toaddr+'@gmail.com'
    
    print()
    print('JUST A MOMENT....')

    # instance of MIMEMultipart 
    msg = MIMEMultipart() 

    # storing the senders email address 
    msg['From'] = fromaddr 

    # storing the receivers email address 
    msg['To'] = toaddr 

    # storing the subject 
    msg['Subject'] = "MOVIE TICKET CONFIRMATION"

    # string to store the body of the mail
    body='THANK YOU FOR BOOKING YOUR SHOW WITH US.\n\nYour show has been confirmed and movie ticket(s) enclosed.\nPlease bring your ticket(s) to the show entrance.\nWe hope that you have a pleasurable experience and choose us again for booking shows in future.\n\nThanks and Regards\nVidit\nManager-BookMyMoviezz.\n\nFor any further assisstance, feel free to contact us at BookMyMoviezz@gmail.com'
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 

    # open the file to be sent 
    filename = "receipt.txt"
    attachment = open(path) 

    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 

    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 

    # encode into base64 
    encoders.encode_base64(p) 

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 

    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 

    # start TLS for security 
    s.starttls() 

    # Authentication 
    s.login(fromaddr, "Savini@123") 

    # Converts the Multipart msg into a string 
    text = msg.as_string() 

    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 

    # terminating the session 
    s.quit()

    print()
    print('MAIL SUCCESSFULLY DELIVERED TO', toaddr)
    print()
    print('CHECK YOUR MAIL TO DOWNLOAD TICKET(S).....')
    print('-------------------------------------')
    print()

