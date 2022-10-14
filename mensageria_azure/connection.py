from azure.servicebus import ServiceBusClient


class ServiceBusConfig:

    def __init__(self):
        self.CONNECTION_STR = "Endpoint=sb://namespace-otiliano.servicebus.windows.net/;SharedAccessKeyName" \
                              "=RootManageSharedAccessKey;SharedAccessKey=xIsW2FXx3IFpiQeThMF/Fh36HfEQBQHNiVZwt0vIs9w= "
        self.queue_name = "fila-otiliano"
        self.client = ServiceBusClient.from_connection_string(self.CONNECTION_STR)

    def get_client(self):
        return self.client

    def get_queue_name(self):
        return self.queue_name
