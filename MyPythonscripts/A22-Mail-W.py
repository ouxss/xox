# Import smtplib for the actual sending function
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("EPHSRP@gmail.com", "kAXF:.<g6yw]dN>+")
 
msg = "test"
server.sendmail("EPHSRP@gmail.com", "EPHSGRP@gmail.com", msg)
server.quit()
