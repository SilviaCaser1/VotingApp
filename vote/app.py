from flask import Flask, render_template, request, make_response, g
import os
import socket
import random
import json
import logging
from redis import Redis

option_a = os.getenv('OPTION_A', "Cats")
option_b = os.getenv('OPTION_B', "Dogs")
hostname = socket.gethostname()

app = Flask(__name__)

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.INFO)

# Configuración del cliente de Redis
if os.getenv("FLASK_ENV") == "testing":
    redis_client = MagicMock()
else:
    redis_client = redis.StrictRedis(host="redis", port=6379, decode_responses=True)

# Función para obtener una instancia de Redis (puede ser mockeada en los tests)
def get_redis():
    if not hasattr(g, "redis"):
        try:
            from redis import Redis  # Importar Redis solo si está disponible
            g.redis = Redis(host="redis", db=0, socket_timeout=5)
        except ImportError:
            g.redis = None
    return g.redis

@app.route("/", methods=['POST','GET'])
def hello():
    voter_id = request.cookies.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]

    vote = None

#    if request.method == "POST":
#        vote = request.form["vote"]
#        app.logger.info("Received vote for %s", vote)

#        redis = get_redis()
#        if redis:
#            data = json.dumps({"voter_id": voter_id, "vote": vote})
#            redis.rpush("votes", data)
    if request.method == "POST":
        vote = request.form.get("vote")
        if not vote:
            return "Missing vote", 400
        # Aquí puedes agregar lógica para manejar el voto
        redis_client.rpush("votes", vote)  # Almacenamos el voto en Redis (mockeado o real)
        return "Vote received", 200
    return render_template("index.html")
    
    resp = make_response(
        render_template(
            "index.html",
            option_a=option_a,
            option_b=option_b,
            hostname=hostname,
            vote=vote,
        )
    )
    resp.set_cookie('voter_id', voter_id)
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
