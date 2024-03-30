#!/bin/bash
docker run -it --rm --network=influx_default -v /home/datascience/telegraf/telegraf.conf:/etc/telegraf/telegraf.conf --name telegraf telegraf
