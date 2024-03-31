# BCNBike
BigData Infraestructure to Manage Data From Public Bikes Stations

This Project consist on an implementation of a IoT Big Data Workflow for data provided for bike stations of the city of barcelona (BicIng). 

The implemented workflow for this prototype is based on:

Historic stations Data -> MQTT -> Telegraf -> InfluxDb -> Grafana
 
The data for the prototype can be obtained from: https://opendata-ajuntament.barcelona.cat/data/es/dataset/bicing
A reduced (one-day) example is also avaliable the publisher folder.

The proposed workflow for a real Digital systmem to apply this would consist on:

Rael Time IoT data from stations -> MQTT -> Telegraf -> InfluxDb -> Digital Twn (Predictive-Optimization/ Prospective-Emulation with Alternative Secenarios / Visualization /etc)

Step to run the prototype in an ubuntu system:
 1. from influx folder: > docker-compose.yml
 2. from mosquitto folder: > sh init_grafana.sh
 3. from telegraf folder: > sh init_grafana.sh
 4. from publisher folder: > python3 launch.py
 5. for visualize data on Grafana Open a firefox tab and run: localhost:3000
 6. In Grafana upload dashboard 'Bike Stations-nnnnnnnnnnn.json' from the grafana folder 
