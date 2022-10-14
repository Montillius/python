from connection import ServiceBusConfig
from azure.servicebus import ServiceBusSubQueue


class AzureReceived:

    def __init__(self):
        self.config = ServiceBusConfig()
        self.queue_name = self.config.get_queue_name()
        self.received = self.config.get_client().get_queue_receiver(self.queue_name, max_wait_time=5)
        self.dlq_receiver = self.config.get_client().get_queue_receiver(self.queue_name, sub_queue=ServiceBusSubQueue.DEAD_LETTER)

    def received_message(self):
        try:
            receiver = self.received
            for msg in receiver:
                print("Última mensagem recebida: " + str(msg))
                message = receiver.complete_message(msg)
                return message
        except Exception:
            raise Exception

    def received_deadlatter(self):
        try:
            print('receber mensagens atrasadas')
            received_msgs = self.dlq_receiver.receive_messages(max_message_count=10, max_wait_time=5)
            for msg in received_msgs:
                print(str(msg))
                dlq_message = self.dlq_receiver.complete_message(msg)
                return dlq_message
        except Exception:
            raise Exception
