from formsg.webhook import decrypt_form
from flask import Flask, request
from datetime import datetime
import logging
import os

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

FORMSG_SECRET_KEY = os.environ['FORMSG_SECRET_KEY']
 
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/formsg_webhook', methods=['POST'])
def formsg_webhook():
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info('FormSG Webhook received at %s', time_now)
    
    clear_text_data = decrypt_form(
        request,        
        secret_key=FORMSG_SECRET_KEY,
        has_attachments=True
    )

    logging.info('FormSG Webhook cleartext data is %s', clear_text_data)

    return 'Ok'

if __name__ == "__main__":
    app.run(host="localhost", debug='True', port=2000)