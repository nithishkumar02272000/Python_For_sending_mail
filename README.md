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
git clone https://github.com/nithishkumar02272000/Python_For_sending_mail

3. Open the mars4.py file and update the following variables with your Gmail address and password:
sender_email = 'your_email@gmail.com'  # Replace with your Gmail address
sender_password = 'your_password'  # Replace with your Gmail password

4. Run the script using the following command:
mars4.py
Enter the title, message, and recipient's email address when prompted.

The script will send the email using the Gmail SMTP server and display a success message if the email was sent successfully.

Note: Make sure to Go to the Google Account Security page.
   1.Under the "Signing in to Google" section, click on "App passwords". You may need to verify your identity by signing in again.
   2.In the "Select app" dropdown, choose "Mail" or "Other (Custom name)".
   3.In the "Select device" dropdown, choose "Other (Custom name)".
   4.Enter a custom name for the app or device (e.g., "Python Email").
   5.Click on the "Generate" button.
   6.Google will generate an application-specific password for you. Copy the generated password.
   
Now, replace the sender_password variable in your code with the application-specific password you generated. Save and run the code again. It should authenticate successfully and send the email without the error.
