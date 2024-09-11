import requests
import json
import sys

import numpy as np
from pylsl import StreamInlet, resolve_byprop
from utils import get_eeg_data

server_url = 'http://128.208.1.139:5000/update_score'

BUFFER_LENGTH = 5
EPOCH_LENGTH = 1
OVERLAP_LENGTH = 0
SHIFT_LENGTH = EPOCH_LENGTH - OVERLAP_LENGTH
INDEX_CHANNEL = [3]

def eeg_setup():
    print('Looking for an EEG stream...')
    streams = resolve_byprop('type', 'EEG', timeout=5)
    print(streams)
    if len(streams) == 0:
        raise RuntimeError('Can\'t find EEG stream.')
    else:
        print('Found it!')
        print(streams)
        
    print("Start acquiring data")
    inlet = StreamInlet(streams[0], max_chunklen=12)
    return inlet

def send_score(player_id, score):
    data = {'player': player_id, 'score': score}
    response = requests.post(server_url, json=data)
    print(f'Server response: {response.text}')

# get player ID from the command line argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <player_id>")
        sys.exit(1)
    
    player_id = int(sys.argv[1])
    
    inlet = eeg_setup()
    
    while True:
        delta, theta, alpha, beta = get_eeg_data(inlet, 5)
        
        score = delta[-1]
        # score = 42  # replace eeg data thing
        send_score(player_id, score)
