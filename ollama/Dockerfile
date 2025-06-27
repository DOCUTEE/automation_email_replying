FROM ollama/ollama:latest

RUN apt update && apt install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

# Override the default ENTRYPOINT from ollama image
ENTRYPOINT ["/start.sh"]
