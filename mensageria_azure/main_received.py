from received import AzureReceived

if __name__ == '__main__':
    AzureReceived = AzureReceived()
    message = AzureReceived.received_message()
    print(message)
    dlq_message = AzureReceived.received_deadlatter()
    print(dlq_message)
