import http.client, urllib
from .pushoverSecrets import token, user

def sendToPhone(message: str, url: str):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": token,
        "user": user,
        "title": "Pushover test",
        "message": message,
        "url": url,
        "priority": 0
    }), { "Content-type": "application/x-www-form-urlencoded" })


    conn.getresponse()