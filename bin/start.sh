# Export .env file
export $(cat .env | xargs)

# Build docker images
docker compose -f bin/docker-compose.yml build