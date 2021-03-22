import urllib
import urllib.request
from APIKEY import key #API Key for THing Speak

# Function to upload temperature(array) to thingspeak
def upload(temp):
    # key = '8OSIDCHTY7CEKVFL'
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % key #Base URL for Thing Speak API
    field = '' #Create empty string for field
    for i in range(temp.size):
        field += '&field%s=%s' % (i + 1, temp[i]) #Input Field Number and Corresponding Temperature Value
    urllib.request.urlopen(baseURL + field)
