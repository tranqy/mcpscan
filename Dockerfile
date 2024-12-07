# Use an official Python runtime as a parent image
FROM node:latest

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Copy the src directory contents into the container at /app/src
COPY src/ /app

RUN apt update && apt install -y python3.11 python3-pip python-is-python3 python3.11-venv


ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run run_all.py when the container launches
CMD ["python3", "run_all.py"]
