from datetime import datetime

from database_api import create_user, update_messages, get_user
from utils import generate_messages
from openai_api import chat_completion
#from mistral_api import mistral_chat_completion
from twilio_api import send_message
import config


def handle_request(data: dict) -> None:
    sender_id = data['From']
    query = data['Body']
    user_name = data['ProfileName']
    user = get_user(sender_id)
    if not user:
        return config.MESSAGE_FOR_INVALID_NUMBER
    else:
        # create chat_history from the previous conversations
        if user:
            messages = generate_messages(user['messages'][-3:], query)
        else:
            messages = generate_messages([], query)
        
        response = chat_completion(messages)
        
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
        return response


data = {
    "From": "whatsapp:+13057533151",
    "Body": "",
    "ProfileName": "Pablo Rendon" #User Name
}

while True:
    you = input('YOU: ')
    if you == 'exit':
        break
    data.update({'Body': you})
    #print(f'YOU: {you}')
    bot = handle_request(data)
    print(f'PREFIX: {bot}')
