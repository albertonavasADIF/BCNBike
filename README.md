# BCNBike
BigData Infraestructure to Manage Data From Public Bikes Stations

This Project consist on an implementation of a IoT Big Data Workflow for data provided for bike stations of the city of barcelona (BicIng). 

The implemented workflow for this prototype is based on:

Historic stations Data -> MQTT -> Telegraf -> InfluxDb -> Grafana
 
The data for the prototype can be obtained from: https://opendata-ajuntament.barcelona.cat/data/es/dataset/bicing

The proposed workflow for a real Digital systmem to apply this would consist on:

Ral Time IoT data from stations -> MQTT -> Telegraf -> InfluxDb -> Digital Twn (Predictive-Optimization/ Prospective-Emulation with Alternative Secenarios / Visualization /etc)

