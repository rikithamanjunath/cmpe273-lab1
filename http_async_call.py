import asyncio
import requests

url = 'https://webhook.site/bb7dcdbc-f5b3-4e09-8d47-3036c0e23011'

async def custom_sleep():
    # Control is passed to the event loop to start next thread while one is put to sleep
    await asyncio.sleep(1)

async def makeCall(name):
    print("Starting " + name )
    r = requests.get(url)
    await custom_sleep()
    print(name + " Date header : " + r.headers.get('Date'))
    print("Ending " + name)

loop = asyncio.get_event_loop()

print("ASynchronous Calls \n")

tasks = [
    asyncio.ensure_future(makeCall("Http Call 1")),
    asyncio.ensure_future(makeCall("Http Call 2")),
    asyncio.ensure_future(makeCall("Http Call 3"))
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


# Another way of implementing Asynchronous calls

# import requests
# import time
# from multiprocessing import Pool

# url = 'https://webhook.site/bb7dcdbc-f5b3-4e09-8d47-3036c0e23011'

# print("ASynchronous calls")
# def makeCall( thread):
#     time.sleep(1)
#     r = requests.get(url)
#     print("Http call " + thread.__str__()+" \t"+ r.headers.get('Date'))

# with Pool(3) as p:
#   p.map( makeCall,[1,2,3])
