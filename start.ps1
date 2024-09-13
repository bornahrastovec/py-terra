Write-Host "Spinning up docker containers..."

docker compose build
docker compose up -d --force-recreate
