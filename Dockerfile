FROM python:3.10-slim

WORKDIR /app

# Copy requirement list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else from the project
COPY . .

# Expose the default Streamlit port
EXPOSE 8501

# Run the app by default (it can be overriden)
CMD ["python3", "-m", "streamlit", "run", "dashboard/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
