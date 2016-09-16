from __future__ import print_function
import json
import urllib2
import sys

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python  show_bus_locations.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

api_key = sys.argv[1]
bus_line = sys.argv[2]

# store API url
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'%(api_key,bus_line)

# Wrangle data (code from Federica NYCweatherapi example)
response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# Store as JSON file (this code was taken from http://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file-in-python)
#with open('data.json', 'w') as outfile:
    #json.dump(data, outfile)

print ('Bus Line :', sys.argv[2])
print ('Number of Active Buses :',len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']))

for i in range(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])):
	print ('Bus', i, 'is at latitude', data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], 'and longitude', data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
