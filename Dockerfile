# Use a base image
FROM registry.access.redhat.com/ubi8/ubi-minimal:latest

# Set the working directory
WORKDIR /app

# Copy the source code into the container
COPY . .

# Define the command to run when the container starts
CMD ["echo", "Hello, World!"]
