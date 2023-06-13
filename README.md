# Python_For_sending_mail
This is a Python script that sends an email with HTML-styled content using the Gmail SMTP server. The script prompts the user to enter the email title, message, and recipient's email address. It then constructs an HTML email with predefined styling and an image and sends it to the specified recipient.

## Features

- Customizable email title and message
- HTML-styled content with predefined CSS
- Predefined image included in the email
- Uses Gmail SMTP server for sending the email

## Usage

1. Install the required dependencies by running the following command:

   ```shell
   pip install smtplib
   
2. Clone the repository:
git clone https://github.com/your-username/your-repository.git

3. Open the mars4.py file and update the following variables with your Gmail address and password:
sender_email = 'your_email@gmail.com'  # Replace with your Gmail address
sender_password = 'your_password'  # Replace with your Gmail password

4. Run the script using the following command:
python html_email_sender.py
Enter the title, message, and recipient's email address when prompted.

The script will send the email using the Gmail SMTP server and display a success message if the email was sent successfully.

Note: Make sure to enable "Less secure app access" in your Gmail account settings or use App Password if you have 2-Step Verification enabled.
