#! /usr/bin/env bash

aws --profile terraform ecr create-repository \
    --repository-name cwoche-kafka-repository \
    --image-scanning-configuration scanOnPush=true \
    --region us-east-1