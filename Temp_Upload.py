import urllib
import urllib.request

# Function to upload temperature(array) to thingspeak
def upload(temp):
    key = '8OSIDCHTY7CEKVFL' # API Key for Thing Speak
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % key #Base URL for Thing Speak API
    field = '' #Create empty string for field
    for i in range(temp.size):
        field += '&field%s=%s' % (i + 1, temp[i])
    urllib.request.urlopen(baseURL + field)
