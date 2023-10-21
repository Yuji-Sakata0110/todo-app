# frontend
FROM node:16
WORKDIR /code/
COPY ./package*.json /code/
RUN yarn install
COPY . /code/
RUN yarn build
EXPOSE 3000
CMD ["yarn", "start"]
