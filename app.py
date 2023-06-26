from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging
import traceback

import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


def scale(payload):
    """Scales Payload"""

    LOG.info("Scaling Payload: %s payload")
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict


@app.route("/")
def home():
    html = (
        "<h3>Sklearn Prediction Home: From Azure Pipelines (Continuous Delivery)</h3>"
    )
    return html.format(format)
