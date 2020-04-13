#!/bin/bash

#config_result=`sudo docker-compose logs config`
config_result=`sudo docker logs config-app`
echo $config_result
[[ $config_result =~ "Config success!" ]] || exit -1