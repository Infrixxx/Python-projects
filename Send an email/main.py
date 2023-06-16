import smtplib

# ****************************************************************
# Python email
# ****************************************************************
import smtplib

sender = "sender@gmail.com"       #sender email
receiver = "bcrachoshi@gmail.com"       #receiver email
password = "Password"              #password of sender's email
subject = "Python email test"
body = "I wrote an email! :D"

# To create a header we do the below, we use triple code as it can
# span multiple lines of text
# we can insert a variable at any given place, using curly braces
message = f"""From: Snoop Dogg{sender}  
To: Nicholas Cage{receiver}
Subject: {subject}\n
{body}
"""

#we create a server object
#smptplib.SMTP takes two arguments being the "smtp.gmail.com" and port number
server = smtplib.SMTP("smtp.gmail.com", 587)
#start transport layer security, .starttls()
server.starttls()

try:
    #To login
    server.login(sender, password)
    print("Logged in...")

    #To send an email
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")

# ****************************************************************