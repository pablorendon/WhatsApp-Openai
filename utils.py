from tool_functions import get_all_network_clients

device_map = get_all_network_clients()

def generate_messages(messages: list, query: str) -> list:
    formated_messages = [
        {
            'role': 'system',
            'content': 'You are a network and home device troubleshooting expert that is able to use the device map provided here to reference devices on the network, idenify them by thier given properties and able to use the functions in your tools to interacte with the devices for control and troubleshooting purposes. Do not assume or make up any information. Device Map: ' + device_map
        }
    ]
    for m in messages:
        formated_messages.append({
            'role': 'user',
            'content': m['query']
        })
        formated_messages.append({
            'role': 'assistant',
            'content': m['response']
        })
    formated_messages.append(
        {
            'role': 'user',
            'content': query
        }
    )
    return formated_messages


if __name__ == '__main__':
    print(device_map)