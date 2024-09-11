from flask import Flask, request

app = Flask(__name__)

@app.route('/update_score', methods=['POST'])
def update_score():
    data = request.json
    player = data['player']
    score = data['score']
    print(f'Player {player} score: {score}')
    return "Score updated", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
