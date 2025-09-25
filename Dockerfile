# Base python image
FROM python:3.10

# Install and update system dependencies
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install --upgrade pip

# Install Python dependencies
RUN pip3 install numpy scipy matplotlib PyQt6 pyarrow pandas openpyxl

# Install dependencies
RUN apt-get update && apt-get install -y git python3-tk

# Create workspace
RUN mkdir workspace
WORKDIR /workspace