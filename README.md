# Middleware-bGames-TerrariaMod
This code corresponds to middleware between the bGames framework and the bGames Terraria mod. It is responsible for redirecting REST API requests to the server hosted at a given address (which must be hardcoded into the script). Additionally, it serves other functions for different developments such as sensors and other sources of information.

# Run them following commands in the terminal:
 docker build -t middleware .
 docker run -p 5000:5000 middleware
