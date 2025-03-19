import sounddevice as sd
import numpy as np
import wave
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import gmplot

# Recording Settings
DURATION = 10                # seconds
SAMPLE_RATE = 44100          #sample rate
CHANNELS = 1                 #Channel 1(MONO) || Channel 2(stereo)

# Function to record audio
def record_audio(filename, duration, sample_rate, channels):
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype=np.int16)
    sd.wait()                  # Wait for recording to finish
    # Save as WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)  #mono audio
        wf.setsampwidth(2)      #16-bit audio
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())    # save the recorded audio
    print(f"Audio saved as {filename}")

# Function to get current location
def get_location():
    geolocator = Nominatim(user_agent="geo_locator")
    try:
        location = geolocator.geocode("your location")
        if location:
            latitude = location.latitude
            longitude = location.longitude
            address = location.address
            return latitude, longitude, address
        else:
            return None, None, "Location not found"
    except GeocoderTimedOut:
        return None, None, "Geolocation service timed out"  #it's optional
  
if __name__ == "__main__":
    audio_filename = "recorded_audio.wav"
    record_audio(audio_filename, DURATION, SAMPLE_RATE, CHANNELS)
    # Fetch location for latitude, longitude, address
    latitude, longitude, address = get_location()
    # Display location
    if latitude is not None and longitude is not None:
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        lat = latitude                          #save latitude in variable
        lon = longitude                         # also longitude
        print(f"Address: {address}")            # Optional
        gmap1 = gmplot.GoogleMapPlotter(lat,lon,13 )  #in 13 is view country view ,,if you need street view replace 13 into 16
        gmap1.draw( "c:\\User\\auloca.html" )     # Pass the absolute path

    else:
        print(f"Error: {address}")              #Optional

