from pushsafer import init, Client
import urllib3
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import http.client, urllib

urllib3.disable_warnings()
init("fZf2wDKtvbvUIJJYPp8Q")

#not used
def sendNot2(x):
    pic = x
    conn = http.client.HTTPSConnection("pushsafer.com:443")
    conn.request("POST", "/api",
      urllib.parse.urlencode({
        "k": "fZf2wDKtvbvUIJJYPp8Q",                # Your Private or Alias Key
        "m": "Motion not2",                   # Message Text
        "t": "Alert",                     # Title of message
        "i": "1",                      # Icon number 1-98
        "s": "0",                     # Sound number 0-28
        "v": "1",                 # Vibration number 0-3
        "p": pic,                   # Picture Data URL with Base64-encoded string
      }), { "Content-type": "application/x-www-form-urlencoded" })
    response = conn.getresponse()

    print(response.status, response.reason)
    data = response.read()
    print(data)
    
    # Passes info to pushsafer & sends notification to phone
def sendNot(x):
    url = "https://www.pushsafer.com/api"
    pic = x
    post_fields = {
        "t" : "Alert2",
        "m" : "Motion detected pic for details",
        "s" : "0",
        "v" : "1",
        "i" : "1",
        "c" : "",
        "d" : "29780",
        "u" : "https://www.pushsafer.com",
        "ut" : "Open Pushsafer",
        "k" : "fZf2wDKtvbvUIJJYPp8Q",
        "p" : pic
}
    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    
    
    #not used
def sendNotification(x):
    pic = x
    #Send Push notification to Phone

    Client("").send_message("Motion Detected Sensor: Main",
                        "Alert",
                        "29780",
                        "1",
                        "0",
                        "1",
                        "https://www.pushsafer.com",
                        "Open Pushsafer",
                        "0",
                        "0",
                        "120",
                        "1200",
                        "0",
                        pic,
                        "",
                        "")