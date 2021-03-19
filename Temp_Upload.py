import urllib
import urllib.request


def upload(temp):  # Function to upload temperature(array) to thingspeak
    key = '8OSIDCHTY7CEKVFL'
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % key
    field = ''
    for i in range(temp.size):
        field += '&field%s=%s' % (i+1,temp[i])
    urllib.request.urlopen(baseURL + field)
    