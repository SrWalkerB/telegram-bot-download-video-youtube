echo "Starting Deploy"

docker-compose down
docker-compose up -d

echo "Finish Deploy"