import smtplib, ssl

def send_email(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com" 
    sender_email = input("Enter sender email: ")
    password = input("Enter password for sender email: ")

    receiver_email = [input("Enter reciever email(s): ")]#Recommend that user creates an 'app password' 
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            res = server.sendmail(sender_email, receiver_email, message)
            print('email sent!')
        except:
            print("could not login or send the mail.")

send_email("Sending an email with Python!")