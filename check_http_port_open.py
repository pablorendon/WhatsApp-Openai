import socket

def check_port(url, port):
    """
    Checks if the specified port is open on the server associated with 'url'.
    
    url: URL of the server (without 'http://' or 'https://')
    port: Port number as an integer (commonly 80 for HTTP, 443 for HTTPS)
    """
    try:
        # Resolve the URL to an IP address
        ip = socket.gethostbyname(url)
        # Create a new socket using the default socket.AF_INET and socket.SOCK_STREAM
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)  # Timeout for the socket operation
        result = sock.connect_ex((ip, port))  # Connect, returns 0 if success
        sock.close()
        
        if result == 0:
            return True  # Port is open
        else:
            return False  # Port is closed
    except socket.error as err:
        print(f"Socket error: {err}")
        return False

# Example usage
url = "foose.z11.co"  # Enter the URL without the protocol
http_port = 8000
https_port = 443

if check_port(url, http_port):
    print(f"Port {http_port} is open on {url}.")
else:
    print(f"Port {http_port} is closed on {url}.")

if check_port(url, https_port):
    print(f"Port {https_port} is open on {url}.")
else:
    print(f"Port {https_port} is closed on {url}.")