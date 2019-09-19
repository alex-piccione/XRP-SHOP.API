from flask import Flask, Response

app = Flask("xrp-shop API")

@app.route("/ping")
def ping():

    return "pong"

app.run(host="0.0.0.0", port=8080)


