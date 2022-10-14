from azure.servicebus import ServiceBusMessage
from connection import ServiceBusConfig


class AzureSender:

    def __init__(self):
        self.config = ServiceBusConfig()
        self.queue_name = self.config.get_queue_name()
        self.sender = self.config.get_client().get_queue_sender(self.queue_name)

    def sender_single_message(self, conteudo):
        try:
            message = ServiceBusMessage(str(conteudo))
            self.sender.send_messages(message)
            return print('Terminou o envio da mensagem')
        except Exception:
            raise Exception
