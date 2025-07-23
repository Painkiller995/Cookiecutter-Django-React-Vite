# Use an official node runtime as a parent image
FROM docker.io/node:22.14-bookworm-slim

# Install required system packages and pnpm
RUN apt-get update \
  && apt-get install --no-install-recommends -y curl ca-certificates gnupg \
  && curl -fsSL https://get.pnpm.io/install.sh | bash - \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Add pnpm to PATH
ENV PATH="/root/.local/share/pnpm:${PATH}"

# Define build environment and application home directory arguments
ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app

# Set the working directory for the container
WORKDIR ${APP_HOME}

# Copy frontend package.json and optionally pnpm-lock.yaml
COPY ./frontend/package.json ./frontend/pnpm-lock.yaml* ./

# Install Node.js dependencies using pnpm
RUN pnpm install

# Copy the application startup script and make it executable
COPY ./compose/local/node/start /start
RUN sed -i 's/\r$//g' /start && chmod +x /start

# Copy application code to the working directory
COPY frontend/ ${APP_HOME}