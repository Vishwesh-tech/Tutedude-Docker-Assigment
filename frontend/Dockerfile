FROM node:18-slim

WORKDIR /app

ENV BACKEND_URL=http://backend:5000/submit

COPY package*.json ./
RUN npm install --production

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
