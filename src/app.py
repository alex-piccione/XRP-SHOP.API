from flask import Flask, Response
import logging as logger

logger.basicConfig(level="INFO")

app = Flask("xrp-shop API")

@app.route("/ping")
def ping():
    return "pong"

logger.info("Start Flask server")
app.run(host="0.0.0.0", port=5000) # use_reloader=True
