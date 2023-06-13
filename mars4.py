import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(title, message, recipient):
    # Email configuration
    sender_email = 'nithishkumar02272000@gmail.com'  # Replace with your Gmail address
    sender_password = 'uihmoedjvihrziwz'  # Replace with your Gmail password

    # Create the email message
    email_message = MIMEMultipart('alternative')
    email_message['Subject'] = title
    email_message['From'] = sender_email
    email_message['To'] = recipient

    # Create the HTML content of the email
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        body {{
          background-color: #f8f8f8;
          font-family: 'Arial', sans-serif;
          margin: 0;
          padding: 0;
        }}

        .container {{
          max-width: 600px;
          margin: 0 auto;
          padding: 20px;
          background-color: #ffffff;
          border-radius: 10px;
          box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }}

        h1 {{
          color: #333333;
          font-family: 'Arial Black', sans-serif;
          font-size: 30px;
          text-align: center;
          margin-top: 0;
        }}

        p {{
          color: #666666;
          font-size: 18px;
          line-height: 1.5;
          margin-bottom: 20px;
        }}

        .image-container {{
          text-align: center;
          margin-top: 20px;
        }}

        img {{
          max-width: 100%;
          height: auto;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <h1>{title}</h1>
        <p>{message}</p>
        <div class="image-container">
          <img src="https://cdna.artstation.com/p/assets/images/images/019/056/448/large/wen-jie-wang-dm2p-18b-wangwenjie-z-06-01.jpg?1561827588" alt="Advertisement Image">
        </div>
      </div>
    </body>
    </html>
    '''

    # Attach the HTML content to the email
    email_message.attach(MIMEText(html_content, 'html'))

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(email_message)
        print('Email sent successfully!')
    except Exception as e:
        print('An error occurred while sending the email:', str(e))

# Prompt the user for input
title = input('Enter the title: ')
message = input('Enter the message: ')
recipient = input('Enter the recipient email address: ')

# Send the email
send_email(title, message, recipient)
