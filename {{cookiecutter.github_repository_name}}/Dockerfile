# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./Pipfile Pipfile
COPY ./Pipfile.lock Pipfile.lock
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . code

# Expose port
EXPOSE 8000

# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - dost_backend.wsgi:application
