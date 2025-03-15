import requests
url=str(input("Enter the url or the ip address: "))
response = requests.head(url)
if response.status_code==200:
    print("Server available ")
elif response.status_code==400:
    print("Server not found")
elif response.status_code==301:
    print("Site moved permanently")
else:
    print("Can't determine the status of the Server")
