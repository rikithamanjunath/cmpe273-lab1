import time
import requests

url = 'https://webhook.site/bb7dcdbc-f5b3-4e09-8d47-3036c0e23011'

def custom_sleep():
    time.sleep(1)

# Function making http calls and printing Date header
def makeCall(name):
    print("Starting " + name )
    r = requests.get(url)
    custom_sleep()
    print(name + " : " + r.headers.get('Date'))
    print("Ending " + name+"\n")

print("Synchronous Calls \n")
makeCall("Http Call 1")
makeCall("Http Call 2")
makeCall("Http Call 3")
