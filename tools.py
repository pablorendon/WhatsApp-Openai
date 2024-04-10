tools = [
    {
    "type": "function",
    "function": {
        "name": "get_all_network_clients",
        "description": "Fetches information about all devices connected to the Ubiquiti network in JSON format to be used to find and identify devices on the network, identify what port on what switch they are connected to, how they are getting power, either by POE or a power supply device that is also on the network like the Panamax brands. The pysical locations for the devices can be found in the name and note fields.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
    },
    {
        "type": "function",
        "function": {
                "name": "power_cycle_port_ubiquiti",
                "description": "power cycles a specific port for a given MAC address pertaining to a ubiquiti network switch on the network",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "switch_mac_address": {
                            "type": "string",
                            "description": "The MAC address of the ubiquiti network switch the device is connected to (not the MAC address of a device) that the user is refering to",
                        },
                        "port_number": {
                            "type": "string",
                            "description": "the outlet number on the panamax power supply device that the device the user wished to power cycle is on",
                        }
                    },
                    "required": ["switch_mac_address","port_number"],
                },
        },
    },
    {
        "type": "function",
        "function": {
                "name": "ping_device_on_local_network",
                "description": "pings a device on the network, get ip address by using the get_all_network_clients function if not directly given",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ip_address": {
                            "type": "string",
                            "description": "The ip address of the described device that the user wishes to ping",
                        }
                    },
                    "required": ["ip_address"],
                },
        },
    },
    {
        "type": "function",
        "function": {
                "name": "power_cycle_bluebolt",
                "description": "power cycles specific outlets or bank for a given ip address pertaining to a panamax power supply device on the network",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ip_address": {
                            "type": "string",
                            "description": "The ip address of the power supply device that the user is refering to",
                        },
                        "outlet": {
                            "type": "string",
                            "description": "the outlet number on the panamax power supply device that the device the user wished to power cycle is on",
                        },
                        "delay": {
                            "type": "string",
                            "description": "the amount of time in second for the power cycle to last, default value is 5 seconds",
                        }
                    },
                    "required": ["ip_address","outlet"],
                },
        },
    },
    {
        "type": "function",
        "function": {
                "name": "switch_on_off_bluebolt",
                "description": "Turn specific outlets or banks ON or OFF for a given ip address pertaining to a panamax power supply device on the network",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ip_address": {
                            "type": "string",
                            "description": "The ip address of the power supply device that the user is refering to",
                        },
                        "outlet": {
                            "type": "string",
                            "description": "the outlet number on the panamax power supply device that the device the user wished to power cycle is on",
                        },
                        "state": {
                            "type": "string",
                            "description": "the state that the user wants the outlet or bank to be in. Can only be in all caps as either 'ON' or 'OFF'.",
                        }
                    },
                    "required": ["ip_address","outlet", "state"],
                },
        },
    },
    {
        "type": "function",
        "function": {
                "name": "get_status_bluebolt",
                "description": "gets the status of the outlest or banks in for a given panamax power supply device on the network",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ip_address": {
                            "type": "string",
                            "description": "The ip address of the described panamax device that the user wishes to check the outlet and bank status' for.",
                        }
                    },
                    "required": ["ip_address"],
                },
        },
    },
    {
        "type": "function",
        "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
        },
    },
    {
        "type": "function",
        "function": {
                "name": "get_current_weather_for_ndays",
                "description": "Get the current weather in a given location for n number of days.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                        "n_days": {
                            "type": "number",
                            "description": "number of days to forecaste the weather, e.g. 5"
                        }
                    },
                    "required": ["location", "n_days"],
                },
        },
    }
]