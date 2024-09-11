## About
This is part of Synaptech's Dawg Daze 2024 activity! \
Built by Catherine Rasgaitis

## Installation
For server device, run:
1. `cd synaptech_proj/server`
2. `pip install -r requirements.txt`

For client devices, run:
1. `cd synaptech_proj/client`
2. `pip install -r requirements.txt`

## Project instructions
Server: \
`python app.py --host=0.0.0.0 --port=5000` \
`python socket_server.py`

Clients: \
`python client.py 1` \
`python socket_client.py 1  # For Player 1` \
\
`python client.py 2`\
`python socket_client.py 2  # For Player 2`
