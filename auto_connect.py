import time
import pywifi
from pywifi import const

def connect():
    wifi = pywifi.PyWiFi()  # Reference to the PyWiFi attribute of the pywifi object.
    iface = wifi.interfaces()[0]    # Returns a list of Wi-Fi interfaces connected to the computer.
    Name = iface.name() # Get the name of the obtained Wi-Fi interface.

    iface.disconnect()
    
    # Create profile
    profile = pywifi.Profile()
    profile.ssid = 'TELLO-9B2E90'
    #profile.auth = const.AUTH_ALG_OPEN
    #profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    
    #iface.remove_all_network_profiles() # Function to remove all network profiles from the Wi-Fi interface.
    tmp_profile = iface.add_network_profile(profile)    # Function to add a new network profile to the Wi-Fi interface.
    iface.connect(tmp_profile)  # Connect to the internet.

    # Display "Connection Successful" or "Connection Failed".
    print("Connecting.")
    for i in range(100):
        time.sleep(1)
        if iface.status() == const.IFACE_CONNECTED:
            print('Connected!')
            break
        print("reonnecting...")
    else:
        print('Failed Connecting.')

if __name__ == "__main__":
    connect()