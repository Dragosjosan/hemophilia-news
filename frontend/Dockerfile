FROM oven/bun:1.3.14 AS build

WORKDIR /app/frontend

COPY package.json bun.lock ./
RUN bun install --frozen-lockfile

COPY --from=design . /app/josanai-design
COPY . .
RUN bun run build

FROM nginx:1.31.3-alpine-slim

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/frontend/dist /usr/share/nginx/html

EXPOSE 80
