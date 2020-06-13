import smtplib

SENDER_EMAIL = "me@__.net"
SENDER_PASSWORD = input("enter password")

def send_email(receiver, subject, body):
    message = "Subject: {}\n\n{}".format(subject, body)
    with smtplib.SMTP_SSL("smtp.__.net",25) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver, message)

if __name__ == "__main__":
    receiver = "mine@gmail.com"
    subject = "test python message"
    body = "this is just a test"

    send_email(receiver, subject, body)