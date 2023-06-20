# Export .env file
export $(cat .env | xargs)

# Install dependencies
sudo yum install -y docker docker-compose nginx git

# Copy nginx config
sudo cp app /etc/nginx/sites-available/app