tools = [
    {
        "type": "function",
        "function": {
                "name": "power_cycle_port_ubiquiti",
                "description": "power cycles a specific port for a given switch_mac_address pertaining to a ubiquiti network switch on the network",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "switch_mac_address": {
                            "type": "string",
                            "description": "The switch_mac_address of the ubiquiti network switch the device is connected to. Not the mac_address of the actual device that the user is refering to"
                        },
                        "port_number": {
                            "type": "string",
                            "description": "the port_number on the ubiquiti switch that the device the user wished to power cycle is on"
                        }
                    },
                    "required": ["switch_mac_address","port_number"]
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
                            "description": "The ip address of the described device that the user wishes to ping"
                        }
                    },
                    "required": ["ip_address"]
                },
        },
    },
    {
        "type": "function",
        "function": {
                "name": "bluebolt_manager",
                "description": "This function can perform multiple processes on Panamax Bluebolt devices in the network.  It can get the status of the device using the 'sendstatus' command, it can turn specific outlets or banks ON or OFF for a given ip and mac address pertaining to a panamax power supply device on the network by using the 'switch' command, it can power cycle a given outlet_number also. The function should return the outcome of the command and that is what you should report back with. Do not assume an outcome of a command.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ip_address": {
                            "type": "string",
                            "description": "The ip address of the bluebolt panamax power supply device that the user is refering to, this is required. Do not assume the ip_address."
                        },
                        "mac_address": {
                            "type": "string",
                            "description": "The mac address of the power supply device that the user is refering to, this is required. Do not assume the mac_address."
                        },
                        "command": {
                            "type": "string", "enum": ["sendstatus", "cycleoutlet","switch"],
                            "description": "the three commands this function takes are 'sendstatus' where the status of the device is returned, 'cycleoutlet' where a specified outlet_number is power cycled, 'switch' where a specified outlet_number is either turned 'ON' or 'OFF'. A command is required."
                        },
                        "outlet_number": {
                            "type": "string",
                            "description": "the outlet_number on the panamax power supply device that the user wishes to 'cycleoutlet' or 'switch'. This parameter can be blank for the 'sendstatus' command."
                        },
                        "state": {
                            "type": "string","enum": ["ON", "OFF"],
                            "description": "the state that the user wants the outlet or bank to be in for the 'switch' command. Can only be in all caps as either 'ON' or 'OFF'. This parameter will not be used for the 'sendstatus' and 'cycleoutlet' commands."
                        }
                    },
                    "required": ["ip_address","mac_address", "command", "outlet_number", "state"]
                },
        },
    },
    {
        "type": "function",
        "function": {
                "name": "wattbox_manager",
                "description": "This function can perform multiple processes on wattbox devices in the network.  It can get the status of the device using the 'command_type' of 'status', it can turn specific outlets ON or OFF for a given ip_address pertaining to a wattbox power supply device on the network by using the 'command_type' of 'on' or off', it can power cycle a given outlet_number by using the command_type 'power_reset'. Also, you can use 'outlet_number' '0' to run the command_types on all the outlets at the same time if needed. The function should return the outcome of the command and that is what you should report back with. Do not assume an outcome of a command.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ip_address": {
                            "type": "string",
                            "description": "The ip address of the wattbox power supply device that the user is refering to, this is required. Do not assume the ip_address."
                        },
                        "command_type": {
                            "type": "string", "enum": ["status","off","on","power_reset"],
                            "description": "the four commands this function takes are 'status' where the status of the device is returned, 'power_reset' where a specified outlet_number is power cycled, 'on' where a specified outlet_number is turned 'ON', 'off' where a specified outlet_number is turned 'OFF'. A command is required."
                        },
                        "outlet_number": {
                            "type": "string",
                            "description": "the outlet_number on the wattbox power supply device that the user wishes to run the 'command_type' on. This parameter can be blank for the 'status' command_type. This parameter can be '0' to send the command to all the outlets if the user specifies it"
                        }
                    },
                    "required": ["ip_address", "command_type"]
                },
        },
    },
    {
        "type": "function",
        "function": {
                "name": "hydrawise",
                "description": "Suspends all sprinkler / irrigatin activity for the time given in hours and minutes. Use this tool when the user would like to turn the sprinklers / irrigation system off for a given time.  If no time is given use the default time is 3 minutes",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hours": {
                            "type": "string",
                            "description": "The amount of hours to suspend the sprinkler / irrigation system specified by the user"
                        },
                        "minutes": {
                            "type": "string",
                            "description": "The amount of minutes to suspend the sprinkler / irrigation system specified by the user. if no minutes are mentioned use the default of 3 minutes"
                        }
                    }
                },
        },
    }
]


"""{
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
    },"""