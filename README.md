# EnviarEmail
Small case with SMTP to send emails from a list with minimal interface.

##Deploy
Recommended to create a virtual environment for the application.
Use:
´´´
'pip3 install -r requirements.txt'
´´´
to install dependencies
´´´
'python3 -m smtpd -c DebuggingServer -n localhost:1025'
´´´
for starting debug server for emailing test.
