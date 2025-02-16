#!/bin/bash

# Before executing this script, make sure docker compose is running. Before running
# docker compose, set SWARMNODE_API_KEY and SWARMNODE_API_BASE for each container.

# If you want to run these in parallel, set a different SWARMNODE_API_KEY for each
# container so that the tests can run in parallel without interfering with each other
# (each api key must belong to a different user). In this case, just copy and paste
# the following commands into separate terminals, instead of running this script.