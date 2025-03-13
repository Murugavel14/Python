import requests
import time  # For delay

THINGSPEAK_WRITE_API_KEY = "WRITE_YOUR_API_KEY"  # Replace with your key
THINGSPEAK_CHANNEL_URL = "https://api.thingspeak.com/update"

payload = {
      'api_key': THINGSPEAK_WRITE_API_KEY,
      'field1': "Hello World" # You write text or numbers 
}
response = requests.get(THINGSPEAK_CHANNEL_URL, params=payload)
    
    if response.status_code == 200: # 200 is default for Thinkspeak
        print(f"Sent {i} to ThinkSpeak successfully! Response: {response.text}")
    else:
        print(f"Failed to send {i} to ThinkSpeak. Status Code: {response.status_code}, Response: {response.text}")
time.sleep(15)  # ThinkSpeak requires at least 15 seconds between updates
