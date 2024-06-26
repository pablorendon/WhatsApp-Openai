import requests
from config import LOCAL_SERVER_API_KEY, LOCAL_SERVER_ROOT_URL

import json
import requests


def get_all_network_clients():
    # Define the endpoint URL
    url = f"{LOCAL_SERVER_ROOT_URL}/ubiquiti/devices"
    
    # Define the headers, including the API key
    headers = {
        "Content-Type": "application/json",
        "x-api-key": LOCAL_SERVER_API_KEY
    }
    
    try:
        # Make the API request
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Serialize the JSON response into a string and remove all spaces
            compact_json = json.dumps(response.json(), separators=(',', ':'))
            return compact_json
        else:
            # Log or handle unsuccessful request appropriately
            print(f"Failed to fetch client devices. Status code: {response.status_code}")
            return {"error": f"Failed to fetch client devices. Status code: {response.status_code}"}
    except Exception as e:
        # Log or handle request exception appropriately
        print(f"Error making request to ubiquiti/devices: {e}")
        return {"error": f"Error making request to ubiquiti/devices: {e}"}


def get_all_ubiquiti_devices():
    # Define the endpoint URL
    url = f"{LOCAL_SERVER_ROOT_URL}/ubiquiti/list_all_ubiquiti_devices"
    
    # Define the headers, including the API key
    headers = {
        "Content-Type": "application/json",
        "x-api-key": LOCAL_SERVER_API_KEY
    }
    
    try:
        # Make the API request
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Serialize the JSON response into a string and remove all spaces
            compact_json = json.dumps(response.json(), separators=(',', ':'))
            return compact_json
        else:
            # Log or handle unsuccessful request appropriately
            print(f"Failed to fetch ubiquiti devices. Status code: {response.status_code}")
            return {"error": f"Failed to fetch ubiquiti devices. Status code: {response.status_code}"}
    except Exception as e:
        # Log or handle request exception appropriately
        print(f"Error making request to ubiquiti/devices: {e}")
        return {"error": f"Error making request to ubiquiti/devices: {e}"}


def power_cycle_port_ubiquiti(function_args: dict) -> str:
    switch_mac_address = function_args.get('switch_mac_address', 'None')
    port_number = function_args.get('port_number', 'None')

    # Define the endpoint URL
    url = f"{LOCAL_SERVER_ROOT_URL}/ubiquiti/powercycle"

    # Define the headers, including the API key
    headers = {
        "Content-Type": "application/json",
        "x-api-key": LOCAL_SERVER_API_KEY
    }

    # Define the request body with the dynamic IP address
    body = {
        "switch_mac_address": switch_mac_address,
        "port_number": port_number
        }


    try:
        # Make the POST request with the specified headers and body
        response = requests.post(url, headers=headers, json=body)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Return the JSON response
            return response.json()
        else:
            # Handle unsuccessful request appropriately
            print(f"Failed to power cycle port. Status code: {response.status_code}")
            return {"error": f"Failed to power cycle port. Status code: {response.status_code}"}
    except Exception as e:
        # Handle request exception appropriately
        print(f"Error making request to ubiquiti/powercycle: {e}")
        return {"error": f"Error making request to ubiquiti/powercycle: {e}"}


def usp_ubiquiti_manager(function_args: dict) -> str:
    usp_mac_address = function_args.get('usp_mac_address')
    action = function_args.get('action')
    outlet_number = function_args.get('outlet_number')

    # Define the endpoint URL
    url = f"{LOCAL_SERVER_ROOT_URL}/ubiquiti/usppowercycle"

    # Define the headers, including the API key
    headers = {
        "Content-Type": "application/json",
        "x-api-key": LOCAL_SERVER_API_KEY
    }

    # Define the request body with the dynamic IP address
    body = {
        "usp_mac_address": usp_mac_address,
        "action": action,
        "outlet_number": outlet_number
        }


    try:
        # Make the POST request with the specified headers and body
        response = requests.post(url, headers=headers, json=body)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Return the JSON response
            return response.json()
        else:
            # Handle unsuccessful request appropriately
            print(f"Failed to perform command. Status code: {response.status_code}")
            return {"error": f"Failed to perform command. Status code: {response.status_code}"}
    except Exception as e:
        # Handle request exception appropriately
        print(f"Error making request to /ubiquiti/usppowercycle: {e}")
        return {"error": f"Error making request to /ubiquiti/usppowercycle: {e}"}


def get_usp_ubiquiti_info(function_args: dict) -> str:
    usp_mac_address = function_args.get('usp_mac_address')

    # Define the endpoint URL
    url = f"{LOCAL_SERVER_ROOT_URL}/ubiquiti/uspinfo"

    # Define the headers, including the API key
    headers = {
        "Content-Type": "application/json",
        "x-api-key": LOCAL_SERVER_API_KEY
    }

    # Define the request body with the dynamic IP address
    body = {
        "usp_mac_address": usp_mac_address
        }


    try:
        # Make the POST request with the specified headers and body
        response = requests.get(url, headers=headers, json=body)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Return the JSON response
            return response.json()
        else:
            # Handle unsuccessful request appropriately
            print(f"Failed to perform command. Status code: {response.status_code}")
            return {"error": f"Failed to perform command. Status code: {response.status_code}"}
    except Exception as e:
        # Handle request exception appropriately
        print(f"Error making request to /ubiquiti/uspinfo: {e}")
        return {"error": f"Error making request to /ubiquiti/uspinfo: {e}"}


def ping_device_on_local_network(function_args: dict) -> str:
    ip_address = function_args.get('ip_address', 'None')
    
    # Define the endpoint URL
    url = f"{LOCAL_SERVER_ROOT_URL}/ping/status"

    # Define the headers, including the API key
    headers = {
        "Content-Type": "application/json",
        "x-api-key": LOCAL_SERVER_API_KEY
    }

    # Define the request body with the dynamic IP address
    body = {
        "ip_address": ip_address
    }

    try:
        # Make the POST request with the specified headers and body
        response = requests.post(url, headers=headers, json=body)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Return the JSON response
            return response.json()
        else:
            # Handle unsuccessful request appropriately
            print(f"Failed to ping device. Status code: {response.status_code}")
            return {"error": f"Failed to ping device. Status code: {response.status_code}"}
    except Exception as e:
        # Handle request exception appropriately
        print(f"Error making request to ping/status: {e}")
        return {"error": f"Error making request to ping/status: {e}"}


def bluebolt_manager(function_args: dict) -> str:
    ip_address = function_args.get('ip_address')
    mac_address = function_args.get('mac_address')
    command = function_args.get('command')
    outlet_number = function_args.get('outlet_number', 'None')
    state = function_args.get('state', 'None')

    # Define the endpoint URL
    url = f"{LOCAL_SERVER_ROOT_URL}/bluebolt/manager"

    # Define the headers, including the API key
    headers = {
        "Content-Type": "application/json",
        "x-api-key": LOCAL_SERVER_API_KEY
    }

    # Define the request body with the dynamic IP address
    body = {
        "ip_address": ip_address,
        "mac_address": mac_address,
        "command": command,
        "outlet_number": outlet_number,
        "state": state
        }


    try:
        # Make the POST request with the specified headers and body
        response = requests.post(url, headers=headers, json=body)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Return the JSON response
            return response.json()
        else:
            # Handle unsuccessful request appropriately
            print(f"Failed to perform command. Status code: {response.status_code}")
            return {"error": f"Failed to perform command. Status code: {response.status_code}"}
    except Exception as e:
        # Handle request exception appropriately
        print(f"Error making request to /bluebolt/manager: {e}")
        return {"error": f"Error making request to /bluebolt/manager: {e}"}


def wattbox_manager(function_args: dict) -> str:
    ip_address = function_args.get('ip_address')
    command_type = function_args.get('command_type')
    outlet_number = function_args.get('outlet_number', 'None')

    # Define the endpoint URL
    url = f"{LOCAL_SERVER_ROOT_URL}/wattbox/manager"

    # Define the headers, including the API key
    headers = {
        "Content-Type": "application/json",
        "x-api-key": LOCAL_SERVER_API_KEY
    }

    # Define the request body with the dynamic IP address
    body = {
        "ip_address": ip_address,
        "command_type": command_type,
        "outlet_number": outlet_number
        }


    try:
        # Make the POST request with the specified headers and body
        response = requests.post(url, headers=headers, json=body)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Return the JSON response
            return response.json()
        else:
            # Handle unsuccessful request appropriately
            print(f"Failed to perform command. Status code: {response.status_code}")
            return {"error": f"Failed to perform command. Status code: {response.status_code}"}
    except Exception as e:
        # Handle request exception appropriately
        print(f"Error making request to /wattbox/manager: {e}")
        return {"error": f"Error making request to /wattbox/manager: {e}"}


def hydrawise(function_args: dict) -> str:
    hours = function_args.get('hours', '0')
    minutes = function_args.get('minutes', '3')

    # Define the endpoint URL
    url = f"{LOCAL_SERVER_ROOT_URL}/hydrawise/suspendall"

    # Define the headers, including the API key
    headers = {
        "Content-Type": "application/json",
        "x-api-key": LOCAL_SERVER_API_KEY
    }

    # Define the request body with the dynamic IP address
    body = {
        "hours": hours,
        "minutes": minutes
        }


    try:
        # Make the POST request with the specified headers and body
        response = requests.post(url, headers=headers, json=body)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Return the JSON response
            return response.json()
        else:
            # Handle unsuccessful request appropriately
            print(f"Status code: {response.status_code}")
            return {"error": f"Status code: {response.status_code}"}
    except Exception as e:
        # Handle request exception appropriately
        print(f"Error making request to hydrawise/suspendall: {e}")
        return {"error": f"Error making request to hydrawise/suspendall: {e}"}






available_functions = {
    #"get_all_network_clients": get_all_network_clients,
    "power_cycle_port_ubiquiti": power_cycle_port_ubiquiti,
    "usp_ubiquiti_manager": usp_ubiquiti_manager,
    "get_usp_ubiquiti_info": get_usp_ubiquiti_info,
    "ping_device_on_local_network": ping_device_on_local_network,
    "bluebolt_manager": bluebolt_manager,
    "wattbox_manager": wattbox_manager,
    "hydrawise": hydrawise
}



if __name__ == "__main__":
    #print(LOCAL_SERVER_API_KEY)
    
    #####Test get_all_network_clients()
    #devices_info = get_all_network_clients()
    #print(devices_info)

    #####Test get_all_network_clients()
    #devices_info = get_all_ubiquiti_devices()
    #print(devices_info)

    #####Test ping_device_on_local_network(ip)
    #test_ip_address = "192.168.1.69"
    #ping_result = ping_device_on_local_network({"ip_address": test_ip_address})
    #print(ping_result)

    #####Test power_cycle_bluebolt
    '''test_args = {
        "ip_address": "192.168.80.56",  # Example IP, replace with an actual device IP on your network
        "outlet": "3",  # Example outlet number, replace with an actual outlet number if needed
        "delay": "5"  # Example delay, adjust as necessary
    }
    result = power_cycle_bluebolt(test_args)
    print(result)'''


    #####Test get_status_bluebolt
    '''test_args = {
        "ip_address": "192.168.80.56"
        }
    result = get_status_bluebolt(test_args)
    print(result)'''


    #####Test power_cycle_bluebolt
    '''test_args = {
        "ip_address": "192.168.80.56",  # Example IP, replace with an actual device IP on your network
        "outlet": "4",  # Example outlet number, replace with an actual outlet number if needed
        "state": "ON"  # Example delay, adjust as necessary
    }
    result = switch_on_off_bluebolt(test_args)
    print(result)'''


    #####Test power_cycle_bluebolt
    '''test_args = {
        "switch_mac_address": "ac:8b:a9:48:f8:3f",  
        "port_number": "16"
    }
    result = power_cycle_port_ubiquiti(test_args)
    print(result)'''

    #####Test wattbox status
    '''test_args = {
        "ip_address": "192.168.100.180",
        "command_type": "status"
        }
    result = wattbox_manager(test_args)
    print(result)'''


    #####Test ubiquiti_usp_manager
    '''test_args = {
        "usp_mac_address": "d8:b3:70:7e:08:53",
        "outlet_number": "20",
        "action": "cycle"
        }
    result = usp_ubiquiti_manager(test_args)
    print(result)'''

    #####Test get_usp_ubiquiti_info
    '''test_args = {
        "usp_mac_address": "d8:b3:70:7e:08:53"
        }
    result = get_usp_ubiquiti_info(test_args)
    print(result)'''

