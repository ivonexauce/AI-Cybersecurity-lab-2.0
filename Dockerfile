# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app/

# Install basic tools
RUN apt-get update && apt-get install -y \
    curl git build-essential jq wget gnupg lsb-release \
    ca-certificates software-properties-common unzip

# Install Suricata
RUN add-apt-repository ppa:oisf/suricata-stable && \
    apt-get update && apt-get install -y suricata

# Install Zeek
RUN curl -fsSL https://download.opensuse.org/repositories/security:zeek/xUbuntu_20.04/Release.key | gpg --dearmor > /etc/apt/trusted.gpg.d/zeek.gpg && \
    echo "deb https://download.opensuse.org/repositories/security:/zeek/xUbuntu_20.04/ /" > /etc/apt/sources.list.d/zeek.list && \
    apt-get update && apt-get install -y zeek

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Mythril (smart contract auditing)
RUN pip install mythril

# Install Slither (needs solc)
RUN apt-get install -y solc
RUN pip install slither-analyzer

# Expose default ports if needed (optional)
EXPOSE 5000

# Default command
CMD ["bash"]
