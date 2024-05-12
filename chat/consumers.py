from channels.generic.websocket import WebsocketConsumer
import json

class Chatconsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
    def disconnect(self, close_code):
        pass
    def receive(self, text_data):
        text_data_json = json.load(text_data)
        messages = text_data_json['message']

        self.send(text_data=json.dump({'message':messages}))