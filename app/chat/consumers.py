import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # aceita a conexão
        self.accept()

    def disconnect(self, code):
        pass

    # Recebe uma message do websocket
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Envia mensagem para WebSocket
        self.send(text_data=json.dumps({'message': message}))

