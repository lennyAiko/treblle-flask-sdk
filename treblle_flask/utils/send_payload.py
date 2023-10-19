import requests
from . import treblle_base_url

"""
Send payload to Treblle
@param { object } payload
@param { string } api_key
"""

async def send_payload(payload, api_key):
    treblle_headers = {
        'Content_Type': 'application/json',
        'X-API-Key': api_key
    }
    try:
        request = await requests.post(
            url=treblle_base_url(),
            data=payload, headers=treblle_headers,
            timeout=2
        )
        print("Treblle response code:", request.status_code,"\nTreblle response content:", request.content)
    except Exception as e:
        print('An error occured with request: \n', e)

if __name__ == '__main__':
    send_payload()