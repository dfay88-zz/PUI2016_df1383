from __future__ import print_function
import json
import urllib2
import sys
import csv

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python  show_bus_locations.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()

api_key = sys.argv[1]
bus_line = sys.argv[2]
file_name = sys.argv[3]

# store API url
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'%(api_key,bus_line)

# Wrangle data (code from Federica NYCweatherapi example)
response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# Code from http://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv-with-python
f = csv.writer(open(file_name, "wb+"))

f.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])

for i in range(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])):
    f.writerow([data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], 
                data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'],
                data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'],
                data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']])
