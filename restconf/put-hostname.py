import requests
import urllib3

USER = 'cisco'
PASS = 'cisco'

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

url = "https://10.0.0.1/restconf/data/Cisco-IOS-XE-native:native/hostname"

payload = "{\"hostname\": \"RSTForum\"}"
headers = {
    'Accept': "application/yang-data+json",
    'Content-Type': "application/yang-data+json",
    'cache-control': "no-cache",
    }


print("----------------------")
print("RSTForum- Configuration Parameters:")
print("----------------------")
response = requests.request("PUT",url, auth=(USER, PASS), data=payload,
                            headers=headers, verify=False)
print(response.text)
print("----------------------")
print("RSTForum- Thanks you:")
print("----------------------")


