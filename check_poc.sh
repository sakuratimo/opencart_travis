#!/bin/bash

poc_result=`sudo docker-compose logs poc-app`
echo $poc_result
[[ $poc_result =~ "PoC success!" ]] || exit -1