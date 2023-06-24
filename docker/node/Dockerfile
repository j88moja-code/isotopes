FROM node:18-alpine

WORKDIR /code/

ENV PATH /code/node_modules/.bin:$PATH

COPY client/package.json /code/package.json
RUN npm install --silent \
    && npm install react-scripts@3.0.1 -g --silent

COPY . /code/
