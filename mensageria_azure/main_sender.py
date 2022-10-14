from sender import AzureSender

if __name__ == '__main__':
    AzureSender = AzureSender()
    AzureSender.sender_single_message({'Id': 'Value', 'color': 'red', 'UF': 'BA', 'Band': 'Metallica'})
