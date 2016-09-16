import json

with open('data.json') as data_file:    
    data = json.load(data_file)


print 'Bus Line :'
print 'Number of Active Buses :',len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])



for i in range(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])):
	print 'Bus', i, 'is at latitude', data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], 'and longitude', data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']

    

    
    