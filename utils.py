def generate_messages(messages: list, query: str) -> list:
    formated_messages = [
        {
            'role': 'system',
            'content': 'you are a network and home device troubleshooting expert that is able to call the function in your tools library to reference devices on the network, idenify them by thier given properties and able to use the functions to interacte with the devices for control and troubleshooting purposes. See whats on the network by using the "get_all_network_clients" function. Do not assume or make up any information.'
        }
    ]
    for m in messages:
        formated_messages.append({
            'role': 'user',
            'content': m['query']
        })
        formated_messages.append({
            'role': 'system',
            'content': m['response']
        })
    formated_messages.append(
        {
            'role': 'user',
            'content': query
        }
    )
    return formated_messages
