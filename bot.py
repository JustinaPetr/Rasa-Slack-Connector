import json

import requests
from requests_toolbelt import MultipartEncoder
from slack_api import SlackApi
from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import os
import io


class Bot(SlackApi):

    def __init__(self, *args, **kwargs):
        super(Bot, self).__init__(*args, **kwargs)
		
    def send_text_message(self, recipient_id, message):
        text = message
        recipient = recipient_id
		
        return self.send_raw1(text, recipient)
			
	
    def send_raw(self, text, recipient): ###sending message back through the http call(this approach will be responding as slack tester so you will 
	                                     ###have to specicy your bot's name as well as avatar picture)
        request_endpoint = '{0}'.format(self.graph_url)
        params = {"token":self.access_token,
                  "channel":"",  #specify the slack channel 
                  "text":text,
                  "username":"",
                  "icon_url":""}
            
        requests.post(request_endpoint, data=params)


		
		
    def send_raw1(self, text, recipient): ###sending message back through the api call (this will be directly responding as your bot so it will be useing the name and avatar as you specified when registering your application)
        # Create a SlackClient for your bot to use for Web API requests
        SLACK_BOT_TOKEN = ""
        CLIENT = SlackClient(SLACK_BOT_TOKEN)
		
        CLIENT.api_call("chat.postMessage", channel='', text=text, as_user = True) #specify a slack channel