#!/bin/bash
docker run -it --rm --name mosquitto -h mosquitto -p 1883:1883 --network=influx_default eclipse-mosquitto
