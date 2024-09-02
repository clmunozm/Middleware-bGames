# Middleware-bGames-TerrariaMod
This code corresponds to middleware between the [bGames cloud module](https://github.com/clmunozm/bGames-module/) and the [bGames Terraria mod](https://github.com/clmunozm/bGames-Terraria/). It is responsible for redirecting REST API requests to the server hosted at a given address (which must be hardcoded into the script). Additionally, it serves other functions for different developments such as sensors and other sources of information.

# Run them following commands in the terminal:
 docker build -t middleware .
 docker run -p 5001:5001 middleware
