import requests

def send_pushover_message(api_token, user_key, message):
    url = 'https://api.pushover.net/1/messages.json'
    data = {
        'token': api_token,
        'user': user_key,
        'message': message,
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message. Status code:", response.status_code)




if __name__=="__main__":
    
    send_pushover_message()
