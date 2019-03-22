import os
import docker
client = docker.from_env()

container =client.swarm.init()

os.system('docker swarm join-token manager')
print container
