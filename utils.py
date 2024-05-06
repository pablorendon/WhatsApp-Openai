from tool_functions import get_all_network_clients, get_all_ubiquiti_devices

#client_device_map = str(get_all_network_clients()) # not needed, being used inside generate_messages now
#ubiquiti_device_map = str(get_all_ubiquiti_devices()) # not needed, being used inside generate_messages now

system_prompt = 'You are a network and home device troubleshooting expert that is able to use the device map provided here to reference devices on the network, idenify them by thier given properties and able to use the functions in your tools to interact with the devices for control and troubleshooting purposes. Do not assume or make up any information and only use the device map information below to answer questions about devices. Do not rely on previous messages for device information. You communicate via WhatsApp messaging so please be as as concise and to the point as possible. '

map_description = """
Here is a description of how to use the all_client_devices Map that you can access via your tools. Only use the following device map to reference device information.
"name": This field holds the descriptive name of the device, identifying the device model or type, and often specifies the physical location within a building or campus. For example, "Apple TV - Living Room" indicates the device is an Apple TV located in the living room.
"mac": Represents the Media Access Control (MAC) address of the device, a unique identifier for network interfaces. The placeholder XX:XX:XX:XX:XX:XX is used here to represent the MAC address of the device.
"ip": The Internet Protocol (IP) address assigned to the device for network communication. A placeholder like XXX.XXX.XXX.XXX is used to represent the local address the device uses.
"_id": The ubiquiti id that is also used to identify devices on the network.
"hostname": Defines the hostname of the device, a label that identifies the device on a network. For example, "Samsung" suggests the device is identified by its brand name.
"switch_mac": Denotes the MAC address of the network switch to which the device is connected. The placeholder XX:XX:XX:XX:XX:XX is used to trace the switch in the network topology This is the Mac address to be used when powercycling a PoE device.
"switch_port": Indicates the port number on the switch that the device is connected to. A value such as XX represents the specific interface on the switch handling traffic for this device This is also used to powercycle a PoE device.
"ap_mac": The MAC address of the Access Point the device connects to, if applicable. "Unknown" indicates no detectable wireless connection or a generic placeholder can be used.
"note": Provides additional information about the device, particularly its power source and how to manage power cycling. This field includes information such as the device's connection its power source, for example, "Power Source: PoE"(in which case you would use the ubiquiti powercycle tool) or "Power Supply[ip_address xxx.xxx.xxx.xxx,  outlet_number x]", indicating how the device can be power cycled using the power supply management like bluebolt.
And here is a description of how to use the 'all ubiquiti unifi devices' Map.
"name": This field holds the descriptive name of the device, identifying the device model or type, and often specifies the physical location within a building or campus. For example, "Apple TV - Living Room" indicates the device is an Apple TV located in the living room.
"model" The ubiquiti model name.
"ip": The Internet Protocol (IP) address assigned to the device for network communication. A placeholder like XXX.XXX.XXX.XXX is used to represent the local address the device uses.
"mac": Represents the Media Access Control (MAC) address of the device, a unique identifier for network interfaces. The placeholder XX:XX:XX:XX:XX:XX is used here to represent the MAC address of the device.
"_id": The ubiquiti id that is also used to identify devices on the network.
"""

def generate_messages(messages: list, query: str) -> list:
    formated_messages = [
        {
            'role': 'system',
            'content': system_prompt + map_description + str(get_all_network_clients()) + str(get_all_ubiquiti_devices()) + "this is the end of the device map.  DO NOT reference any device information from anything past this."
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
    #print(system_prompt + map_description + device_map)
    print("Hello123")