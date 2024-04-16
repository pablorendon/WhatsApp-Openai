from datetime import datetime
import threading

from flask import Flask, request

from database_api import create_user, update_messages, get_user
from utils import generate_messages
from openai_api import chat_completion
from twilio_api import send_message, get_recent_message_sid
import config

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'OK', 200


def handle_request(data: dict) -> None:
    sender_id = data['From']
    query = data['Body']
    user_name = data['ProfileName']
    sms_sid = data['SmsSid']
    user = get_user(sender_id)
    print(user)
    '''We check using Twilio APIs that the incoming message is from Twilio
    '''
    retrieved_sms_sid = get_recent_message_sid(from_=sender_id)
    #if retrieved_sms_sid != sms_sid:
        #print(config.MESSAGE_FOR_INVALID_NUMBER)
        #send_message(sender_id, config.MESSAGE_FOR_INVALID_NUMBER)
    if not user: #was elif
        print(config.MESSAGE_FOR_INVALID_NUMBER)
        send_message(sender_id, config.MESSAGE_FOR_INVALID_NUMBER)
    else:
        # create chat_history from the previous conversations
        if user:
            messages = generate_messages(user['messages'][-3:], query) #the -3 means get last 3 messages from the user list
        else:
            messages = generate_messages([], query)
        print(query)
        print(sender_id)
        print(messages)
        response = chat_completion(messages)
        print(response)
        send_message(sender_id, response)
        if user:
            update_messages(sender_id, query, response,
                            user['messageCount'])
        else:
            # if not create
            message = {
                'query': query,
                'response': response,
                'createdAt': datetime.now().strftime('%d/%m/%Y, %H:%M')
            }
            user = {
                'userName': user_name,
                'senderId': sender_id,
                'messages': [message],
                'messageCount': 1,
                'mobile': sender_id.split(':')[-1],
                'channel': 'WhatsApp',
                'is_paid': False,
                'created_at': datetime.now().strftime('%d/%m/%Y, %H:%M')
            }
            create_user(user)


@app.route('/twilio/webhook', methods=['POST'])
def handle_twilio_webhook():
    try:
        print('A new twilio request...')
        data = request.form.to_dict()
        print(data)
        # Create a new thread to handle the time consuming request
        threading.Thread(
            target=handle_request,
            args=[data]
        ).start()
        print('Request success.')
    except:
        print('Request failed.')
    finally:
        return 'OK', 200


@app.route('/create/user', methods=['POST'])
def handle_create_user():
    try:
        body = dict(request.get_json())
        print(body)
        user_name = body['userName']
        sender_id = body['senderId']
        user = {
            'userName': user_name,
            'senderId': sender_id,
            'messages': [],
            'messageCount': 1,
            'mobile': sender_id.split(':')[-1],
            'channel': 'WhatsApp',
            'is_paid': False,
            'created_at': datetime.now().strftime('%d/%m/%Y, %H:%M')
        }
        flag = create_user(user)
        print(flag)
        return 'OK', 200
    except:
        return 'BAD REQUEST', 401
