FROM node:18 as angular
WORKDIR /app
COPY package.json /app
RUN npm install --silent
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=angular app/dist/frontend /usr/share/nginx/html
