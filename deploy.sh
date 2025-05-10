echo "Starting Deploy"

git pull origin master

docker-compose down
docker-compose up -d

echo "Finish Deploy"