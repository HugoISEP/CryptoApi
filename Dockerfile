# Based docker image
FROM python:3.9

# Define the working directory in the container
WORKDIR /code

# Copy the requirements.txt file (where dependencies are precised) inside the container
COPY ./requirements.txt /code/requirements.txt

# Install all dependencies required
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy code files in the container
COPY ./app /code/app

# Run the command in the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
