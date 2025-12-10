# 1. Base image
FROM python:3.11

# 2. Set working directory
WORKDIR /app

# 3. Copy files
COPY . .

# 4. Install dependencies
RUN pip install flask

# 5. Expose port
EXPOSE 5000

# 6. Run the app
CMD ["python", "app.py"]
