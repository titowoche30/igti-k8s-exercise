#! /usr/bin/env bash

aws --profile terraform ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 649165755582.dkr.ecr.us-east-1.amazonaws.com

docker build -t cwoche-kafka-repository kafka-strimzi-k8s-v1beta1/

docker tag cwoche-kafka-repository:latest 649165755582.dkr.ecr.us-east-1.amazonaws.com/cwoche-kafka-repository:latest

docker push 649165755582.dkr.ecr.us-east-1.amazonaws.com/cwoche-kafka-repository:latest