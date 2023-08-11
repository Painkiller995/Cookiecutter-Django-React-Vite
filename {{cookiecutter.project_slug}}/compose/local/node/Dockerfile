# Use an official node runtime as a parent image
FROM node:18-bullseye-slim

# Install apt packages if needed (add package names if required)
RUN apt-get update && apt-get install --no-install-recommends -y

# Define build environment and application home directory arguments
ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app

# Set the working directory for the container
WORKDIR ${APP_HOME}

# Copy frontend package.json to install dependencies
COPY ./frontend/package.json /app/

# Install Node.js dependencies
RUN npm install

# Copy the application startup script and make it executable
COPY ./compose/local/node/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# Copy application code to the working directory
COPY frontend/ ${APP_HOME}