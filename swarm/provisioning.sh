#!/bin/bash
echo 'Installing Docker'
yum update -y
yum -y install git
yum -y install python-pip
amazon-linux-extras install docker
service docker start
usermod -a -G docker ec2-user
docker info

pip install docker 

