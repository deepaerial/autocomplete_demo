#!/bin/bash

if command -v poetry &> /dev/null
then
    echo "Poetry is installed, checking if .venv exists..."
    if [ ! -d ".venv" ]; then
        echo ".venv not found, running 'poetry install'..."
        poetry install
    fi
    echo "Running the script with poetry..."
    poetry run python -m t9autocomplete_demo
else
    echo "Poetry is not installed, checking for Docker..."
    # Check if Docker is installed
    if command -v docker &> /dev/null
    then
        echo "Docker is installed, building and running the Docker image..."
        docker build -t t9autocomplete_demo .
        docker run -it t9autocomplete_demo
    else
        echo "Neither Poetry nor Docker is installed. Please install one of them to run project."
        exit 1
    fi
fi