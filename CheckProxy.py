import requests

def check_backend_availability(url):
    try:
        response = requests.get(url)
        if "Backend not available" in response.text:
            print("Backend not available")
        else:
            print("Backend is available")
    except requests.exceptions.RequestException as e:
        print("Error occurred:", str(e))

# 指定要检查的网页 URL
url = "http://59.36.231.138:6080/"

# 调用函数进行检查
check_backend_availability(url)
