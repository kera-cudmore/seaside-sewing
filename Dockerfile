# 1. Use a Python base image (using a slim version is smaller and faster)
FROM python:3.11-slim

# Set environment variables for the application
# This prevents Python from writing .pyc files (faster) and makes logging immediately available
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Define the working directory inside the container
WORKDIR /app

# 2. Install dependencies
# Copy only requirements file first to leverage Docker layer caching
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy the rest of the application code
# The .dockerignore file ensures we only copy what's needed
COPY . /app/

# 4. Run production commands (collectstatic and set the entrypoint)
# The ENTRYPOINT is what executes when the container starts.
# Use Gunicorn to serve the application on port 8000.
# Replace 'your_project_name' with the name of the folder containing settings.py and wsgi.py
# The Gunicorn worker count should be (2 * number_of_cores) + 1 for optimal performance.
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "seaside_sewing.wsgi:application"]

# 5. Expose the port Gunicorn is listening on (must match the Dokploy Container Port)
EXPOSE 8000