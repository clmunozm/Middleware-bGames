# Middleware-bGames-TerrariaMod
This code corresponds to middleware between the [bGames cloud module](https://github.com/clmunozm/bGames-module/) and the [bGames Terraria mod](https://github.com/clmunozm/bGames-Terraria/). It is responsible for redirecting REST API requests to the server hosted at a given address (which must be hardcoded into the script). Additionally, it serves other functions for different developments such as sensors and other sources of information.

# Run the middleware
## Prerequisites
* [Docker](https://docs.docker.com/get-docker/) version `24.0.4` or higher
* [Docker-Compose](https://docs.docker.com/compose/install/) version `1.29.0` or higher
  
## Run them following commands in the terminal:
```shell
 docker build -t middleware .
 docker run -p 5001:5001 middleware
```
