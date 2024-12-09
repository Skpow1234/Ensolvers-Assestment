
#!/bin/bash

# Script to setup and run the application (backend and frontend)

# Helper function for colored output
function print_message {
    echo -e "\033[1;32m$1\033[0m"
}

# Ensure script is running in bash/zsh
if [[ -z "$BASH_VERSION" && -z "$ZSH_VERSION" ]]; then
    echo "This script must be run in bash or zsh."
    exit 1
fi

print_message "Starting application setup..."

# Navigate to the backend directory
print_message "Setting up the backend..."
cd backend

# Check and install Python dependencies
if [ ! -d "venv" ]; then
    print_message "Creating virtual environment..."
    python3 -m venv venv
fi
source venv/bin/activate
print_message "Installing Python dependencies..."
pip install -r requirements.txt

# Run Alembic migrations to set up the database
print_message "Setting up the database schema..."
alembic upgrade head

# Start the backend server
print_message "Starting the backend server..."
uvicorn app.main:app --reload &
backend_pid=$!

# Navigate to the frontend directory
cd ../frontend

# Check and install Node.js dependencies
if [ ! -d "node_modules" ]; then
    print_message "Installing frontend dependencies..."
    npm install
fi

# Start the frontend server
print_message "Starting the frontend server..."
npm start &
frontend_pid=$!

# Wait for the backend and frontend processes to terminate
trap "kill $backend_pid $frontend_pid" EXIT

# Print completion message
print_message "Application is running. Access the frontend at http://localhost:3000"
wait
