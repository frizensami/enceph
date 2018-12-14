FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN curl --silent --location https://deb.nodesource.com/setup_10.x | bash - && apt-get install --yes nodejs
RUN npm cache clean --force && rm -rf node_modules/
RUN npm install -g gulp
RUN npm cache clean --force && rm -rf node_modules/
ADD . /code/
# RUN npm install semantic-ui --save
# RUN cd semantic/
# RUN gulp build
