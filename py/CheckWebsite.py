import requests
from bs4 import BeautifulSoup

def check_website(ip):
    try:
        response = requests.get(f"http://{ip}")
        soup = BeautifulSoup(response.text, 'html.parser')
        if "Backend not available" in soup.body.text:
            print(f"Website with IP {ip} has 'Backend not available' in body.")
    except Exception as e:
        print(f"Error checking website with IP {ip}: {e}")

# Replace with your actual IP range
ip_range = ["192.0.2.0", "192.0.2.1", "192.0.2.2"]
for ip in ip_range:
    check_website(ip)
