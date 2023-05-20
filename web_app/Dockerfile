# pulling the python image
FROM python:3-alpine

# copy app into the image
COPY . /usr/src/nothing-app

# set working directory
WORKDIR /usr/src/nothing-app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# configure the container to run commands using python iterpriter
ENTRYPOINT [ "python" ]

# run app: python app.py - doing this in compose file
# CMD [ "app.py" ]