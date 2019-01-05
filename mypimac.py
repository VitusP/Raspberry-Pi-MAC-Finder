#This is a code to view your pi mac address
#Writer: Vitus Putra
#Date: 01/05/2019

def getMAC(interface='wlan0'):
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]

print('Your Pi MAC Address: '+ getMAC('wlan0'))
