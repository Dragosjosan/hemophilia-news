FROM oven/bun:1.3.14 AS build

# vite.config.ts resolves the design system at ../josanai-design, so mirror the
# repo layout: /app/frontend and /app/josanai-design.
WORKDIR /app/frontend

# Install dependencies separately so dependency layers can be reused.
COPY package.json bun.lock ./
RUN bun install --frozen-lockfile

# "design" is a named build context (the josanai-design submodule), see docker-compose.yml.
COPY --from=design . /app/josanai-design
COPY . .
RUN bun run build

FROM nginx:1.31.3-alpine-slim

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/frontend/dist /usr/share/nginx/html

EXPOSE 80
