# Build stage for React frontend
FROM node:18 AS build-stage
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Production stage
FROM python:3.9-slim
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Flask app
COPY app.py .

# Copy built frontend assets from build-stage
COPY --from=build-stage /app/frontend/dist ./frontend/dist

EXPOSE 5000

CMD ["python", "app.py"]
