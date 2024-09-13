#!/bin/bash
echo "Spinning up RabbitMQ running the python scripts in containers..."

docker compose build
docker compose -f ./docker-compose.yml up -d --force-recreate

$SHELL