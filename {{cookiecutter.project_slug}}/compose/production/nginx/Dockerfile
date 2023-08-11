# Stage 1: Build the frontend
# Use an official node runtime as a parent image
FROM node:18-bullseye-slim AS build

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

# Copy application code to the working directory
COPY frontend/ ${APP_HOME}

# Build the frontend
RUN npm run build

# Stage 2: Serve the built frontend using Nginx
FROM nginx:1.21.1-alpine

# Create a non-root user
RUN addgroup --system nginxuser \
    && adduser --system --ingroup nginxuser nginxuser

# Give necessary permissions to the non-root user
RUN chown -R nginxuser:nginxuser /var/cache/nginx && \
    chown -R nginxuser:nginxuser /var/log/nginx && \
    chown -R nginxuser:nginxuser /etc/nginx/conf.d
RUN touch /var/run/nginx.pid && \
        chown -R nginxuser:nginxuser /var/run/nginx.pid

# Copy only the built assets from the build stage to Nginx's HTML directory
COPY --from=build /app/dist /usr/share/nginx/html

# Copy Nginx configuration
COPY ./compose/production/nginx/default.conf /etc/nginx/conf.d/default.conf

# Switch to the non-root user
USER nginxuser