#!/bin/bash
echo 'Installing Docker'
yum update -y
yum -y install git
amazon-linux-extras install docker
service docker start
usermod -a -G docker ec2-user
docker info


