#! /usr/bin/env bash

eksctl --profile terraform create cluster \
--name my-cluster-cwoche-modulo2 \
--region us-east-1 \
--instance-types=m5.xlarge \
--managed \
--spot \
--nodes=2 \
--asg-access \
--nodes-min=2 \
--nodes-max=3 \
--nodegroup-name=node-group-cwoche-modulo2 \
--with-oidc \
--ssh-access \
--ssh-public-key terraform \
--alb-ingress-access \
--node-private-networking \
--full-ecr-access \