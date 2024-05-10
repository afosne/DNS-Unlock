import ipaddress
import requests
from bs4 import BeautifulSoup
import concurrent.futures

def check_website(ip):
    try:
        response = requests.get(f"http://{ip}")
        soup = BeautifulSoup(response.text, 'html.parser')
        if "Backend not available" in soup.body.text:
            print(f"Website with IP {ip} has 'Backend not available' in body.")
    except Exception as e:
        print(f"Error checking website with IP {ip}: {e}")

# Replace with your actual IP range and individual IP addresses
ip_range = "192.0.2.0/24"
individual_ips = ["203.0.113.0", "203.0.113.1"]

with concurrent.futures.ThreadPoolExecutor() as executor:
    # Check IP range
    for ip in ipaddress.IPv4Network(ip_range):
        executor.submit(check_website, str(ip))
    # Check individual IP addresses
    for ip in individual_ips:
        executor.submit(check_website, ip)
