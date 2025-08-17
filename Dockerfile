FROM python:3.12

WORKDIR /university_api


# set env variablesæ
# Prevents python from writing pyc files to disc
ENV PYTHONDONTWIRITEBTYECODE 1 
# Prevents python from buffering stdout and stderr 
ENV PYTHONUNBUFFERED 1

# Copy the requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code to the working directory 
COPY . .

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


