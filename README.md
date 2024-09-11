## Installation
For server device, run:
cd synaptech_proj/server
pip install -r requirements.txt

For client devices, run:
eval "$(/homes/iws/catraz/miniconda3/bin/conda shell.bash hook)"
cd synaptech_proj/client
pip install -r requirements.txt

## Project instructions
Server: 
python app.py --host=0.0.0.0 --port=5000
python socket_server.py

Client:
python client.py 1
python socket_client.py 1  # For Player 1

python client.py 2
python socket_client.py 2  # For Player 2
