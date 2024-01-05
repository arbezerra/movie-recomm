FROM node:20-alpine as builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . ./
RUN npm run build

FROM node:20-alpine AS prod
USER node
WORKDIR /app
COPY --from=builder --chown=node:node /app/build build/
COPY --from=builder --chown=node:node /app/node_modules node_modules/
COPY --chown=node:node package.json .
ENV PORT=5173
# ENV BODY_SIZE_LIMIT=0
ENV NODE_ENV=production
CMD ["node", "build"]
