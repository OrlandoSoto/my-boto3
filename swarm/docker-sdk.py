import docker
client = docker.from_env()

container =client.swarm.init()

print container

container.logs()