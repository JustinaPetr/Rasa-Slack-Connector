from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from builtins import str
from flask import Blueprint, request, jsonify
from bot import Bot

from rasa_core.channels.channel import UserMessage, OutputChannel
from rasa_core.channels.rest import HttpInputComponent

logger = logging.getLogger(__name__)




class SlackBot(Bot, OutputChannel):
    """A bot that uses fb-messenger to communicate."""

    def __init__(self, access_token):
        super(SlackBot, self).__init__(access_token)
        print()

    def send_text_with_buttons(self, recipient_id, text, buttons, **kwargs):
        pass

    def _add_postback_info(self, buttons):
        pass

    def send_custom_message(self, recipient_id, elements):
        pass


class SlackInput(HttpInputComponent):
    def __init__(self, slack_dev_token, slack_verification_token, slack_client, debug_mode):
        self.slack_dev_token = slack_dev_token
        self.debug_mode = debug_mode
        self.slack_client = slack_client
        self.slack_verification_token = slack_verification_token

		
    def blueprint(self, on_new_message):
        from flask import Flask, request, Response
        slack_webhook = Blueprint('slack_webhook', __name__)
		
        @slack_webhook.route("/", methods=['GET'])
        def health():
            return jsonify({"status": "ok"})
		
        @slack_webhook.route('/slack/events', methods=['POST'])
        def event():
		    # Echo the URL verification challenge code
            if request.json.get('type') == "url_verification":
                return request.json.get('challenge'), 200
            print(request.json)
				
            if request.json.get('token') == self.slack_client and request.json.get('type') == "event_callback": #verify token
                payload = request.json
                data = payload
                messaging_events = data.get('event')
                channel = messaging_events.get('channel')
                user = messaging_events.get('user')
                text = messaging_events.get('text')	
                bot = messaging_events.get('bot_id')				
                if bot == None: #check if it's a new message from the user. Bot users will not have userids
                    on_new_message(UserMessage(text, SlackBot(self.slack_dev_token)))
			
            return Response(), 200 	
				
        return slack_webhook