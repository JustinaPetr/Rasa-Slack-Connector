from rasa_core.channels import HttpInputChannel
from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

#load your agent

nlu_interpreter = RasaNLUInterpreter('./models/nlu')
agent = Agent.load("examples/babi/models/policy/current", interpreter=nlu_interpreter)


input_channel = SlackInput(
    'xoxp...', #slack_dev_token
    'xoxb...', #slack_client_token
    '...', #verification_token for interactive messages, events
	True)
	
	
agent.handle_channel(HttpInputChannel(5004, "/", input_channel))
