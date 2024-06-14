# FROM python:latest
# ENV PYTHONUNBUFFERED 1
# ENV PIP_ROOT_USER_ACTION=ignore
# WORKDIR /backendservice
# COPY requirements.txt /backendservice/requirements.txt
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# COPY . /backendservice/


# Use a specific Python version
FROM python:latest

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore

# Set the working directory
WORKDIR /backendservice

# Copy and install requirements
COPY requirements.txt /backendservice/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the application code
COPY . /backendservice/
