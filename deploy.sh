#!/bin/bash

# Exit on error
set -e

# Configuration
APP_NAME="cafemenu"
APP_DIR="/var/www/$APP_NAME"
VENV_DIR="$APP_DIR/venv"
REPO_URL="your-repo-url"  # Replace with your repository URL

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}Starting deployment of $APP_NAME...${NC}"

# Create application directory if it doesn't exist
if [ ! -d "$APP_DIR" ]; then
    echo "Creating application directory..."
    sudo mkdir -p $APP_DIR
    sudo chown -R $USER:$USER $APP_DIR
fi

# Clone or update repository
if [ ! -d "$APP_DIR/.git" ]; then
    echo "Cloning repository..."
    git clone $REPO_URL $APP_DIR
else
    echo "Updating repository..."
    cd $APP_DIR
    git pull
fi

# Create and activate virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate virtual environment and install dependencies
echo "Installing dependencies..."
source $VENV_DIR/bin/activate
pip install -r $APP_DIR/requirements.txt

# Create necessary directories
echo "Creating necessary directories..."
sudo mkdir -p /var/log/gunicorn
sudo chown -R $USER:$USER /var/log/gunicorn

# Copy configuration files
echo "Copying configuration files..."
sudo cp $APP_DIR/cafemenu.nginx.conf /etc/nginx/sites-available/$APP_NAME
sudo cp $APP_DIR/cafemenu.service /etc/systemd/system/

# Enable and restart services
echo "Enabling and restarting services..."
sudo ln -sf /etc/nginx/sites-available/$APP_NAME /etc/nginx/sites-enabled/
sudo systemctl daemon-reload
sudo systemctl enable $APP_NAME
sudo systemctl restart $APP_NAME
sudo systemctl restart nginx

# Run Django commands
echo "Running Django commands..."
cd $APP_DIR
python manage.py migrate
python manage.py collectstatic --noinput

echo -e "${GREEN}Deployment completed successfully!${NC}"
echo "Please check the application status with:"
echo "sudo systemctl status $APP_NAME"
echo "sudo systemctl status nginx" 