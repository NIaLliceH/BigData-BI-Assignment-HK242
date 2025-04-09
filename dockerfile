# Use the official Jupyter PySpark Notebook image as the base image
FROM jupyter/pyspark-notebook:latest

# Set the working directory in the container
WORKDIR /code

# Copy any necessary files into the container (if needed)
# COPY ./your-local-files /home/jovyan/work/
# Check if ./data_model and ./clean_datasets exist and copy them into the container
RUN test -d ./data_model && cp -r ./data_model /code/ || echo "data_model directory not found"

RUN test -d ./clean_datasets && cp -r ./clean_datasets /code/ || echo "clean_datasets directory not found"

# COPY ./requirements.txt ./

# RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir pandas numpy scikit-learn

# Install additional Python packages if required
# RUN pip install <package-name>

# Expose the default Jupyter Notebook port
EXPOSE 8888

# Command to start the Jupyter Notebook server
# docker run -p 8888:8888 jupyter/base-notebook
# CMD ["docker", "run", "-p", "8888:8888", "jupyter/pyspark-notebook:latest"]