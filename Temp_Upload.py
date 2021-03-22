import urllib
import urllib.request
from APIKEY import key  # API Key for THing Speak

# Function to upload temperature(array) to thingspeak


def upload(temp):
    # Base URL for Thing Speak API
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % key
    field = ''  # Create empty string for field
    for i in range(temp.size):
        # Input Field Number and Corresponding Temperature Value
        field += '&field%s=%s' % (i + 1, temp[i])
    urllib.request.urlopen(baseURL + field)
