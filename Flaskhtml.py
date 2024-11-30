from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/send_email', methods=['POST'])
def send_email_on_submit():
    # Get form data
    recipient = request.form['recipient']
    subject = request.form['subject']
    body = request.form['body']
    
    # Send the email
    send_email(recipient, subject, body)
    
    return redirect(url_for('success'))

def send_email(recipient, subject, body):
    sender_email = "jaiminpatel.cn@gmail.com"  # Your email
    sender_password = "Anaya@0212"  # Your email password (for Gmail)
    
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

@app.route('/success')
def success():
    return "Email sent successfully!"

if __name__ == '__main__':
    app.run(debug=True)
