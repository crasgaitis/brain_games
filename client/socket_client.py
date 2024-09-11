import socket
import sys

def stream_data(data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('128.208.1.139', 6000))
    s.sendall(data.encode('utf-8'))
    s.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python socket_client.py <player_id>")
        sys.exit(1)
    
    player_id = int(sys.argv[1])
    eeg_data = f"eeg data for player {player_id}"
    stream_data(eeg_data)