# Zontahnos Agent

This is an agent ran as a docker container that will montior network endpoints. It is meant to be used with the zontahnos framework (https://github.com/sjjensen2004/zontahnos). It will take a list of hosts and log network status (up/down) and performance metrics to Zontahnos. This will allow you to monitor critical workloads from multiple different context (i.e., is the endpoint reachable from the DC, HQ, Branch office, etc.). 

**note** This is a beta applicaiton. It is not secuirty hardened and should be used at the users own risk.

## Setup

### Prerequisite
You must have the Zonthanos framework up and running. This agent is a collector which sends data to Zonthanos for visualization. 

### Clone the repository

`git clone git@github.com:sjjensen2004/zontahnos-agent.git`

### Update config.yaml
Populate config_example.yaml with the corresponding vars and then rename to config.yaml. 

### Docker magic
run `docker compose up --build

