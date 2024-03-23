FROM traefik:2.11.0
RUN mkdir -p /etc/traefik/acme \
  && touch /etc/traefik/acme/acme.json \
  && chmod 600 /etc/traefik/acme/acme.json
COPY ./compose/local/traefik/traefik.yml /etc/traefik
