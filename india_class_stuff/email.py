import smtplib 

def gmail(email, password, message):
    connection=smtplib.SMTP('smtp.gmail.com',587)# where to connect by port
    connection.ehlo() #establishes connection
    connection.starttls() #composes email post login
    connection.login(email, password)
    connection.sendmail("sagrawal21@groton.org", email, message)
    connection.quit()
mess = "Subject: wassup\n\nThis email has been sent through unconventional methods... Enquire for further details"
email = "sagrawal21@groton.org"
password = "SAgroton21"

gmail(email, password, mess) 