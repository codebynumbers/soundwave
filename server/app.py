from flask import current_app, Flask, jsonify, request
import pyglet


app = Flask(__name__)
app.config.from_pyfile('settings.conf', silent=True)

@app.route('/play/')
def play():
    token = request.args.get('token')
    if not token == current_app.config['SLACK_TOKEN']:
        return 'Invalid token'

    name = request.args.get('text')
    if not name:
        return'No sound provided'

    try:
        music = pyglet.media.load('clips/{}.wav'.format(name))
        music.play()
    except:
        return "Sound play failure"

    return "Sound play detected"


if __name__ == "__main__":
    app.run()
