FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a workspace directory for editing project code
RUN mkdir /workspace

COPY src/ /app/src/

ENTRYPOINT ["python", "-m", "src.main"]
