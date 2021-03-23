# the base image 
FROM python:3.8-alpine

# copy all the files from dir with Dockerfile and requirements.txt to /app folder in images app = alpine image . betyder folder man er i
COPY . /app

# cd into /app folder with (in this case only) the requirements.txt
WORKDIR /app

# install python modules
RUN pip install -r requirements.txt

# Change into / as starting point of container
WORKDIR /

# when container runs it should start in a ash terminal
CMD ["ash"]

# . betyder led efter dockerfil i den folder