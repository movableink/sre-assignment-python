from typing import Dict, Any
import requests
from .config import Config

def lookup_ip(ip: str) -> Dict[str, Any]:
    """
    Look up geographical information for an IP address.
    
    Args:
        ip: The IP address to look up
        
    Returns:
        Dict containing geographical information about the IP
        
    Raises:
        requests.exceptions.RequestException: If the API request fails
    """
    headers = {}
    if Config.API_TOKEN:
        headers['Authorization'] = f'Bearer {Config.API_TOKEN}'
    
    response = requests.get(
        f"{Config.API_URL}/geoip/{ip}",
        headers=headers
    )
    
    response.raise_for_status()
    return response.json()
