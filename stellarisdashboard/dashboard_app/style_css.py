import logging

from flask import render_template, request, redirect, make_response

from stellarisdashboard import config
from stellarisdashboard.dashboard_app import flask_app

logger = logging.getLogger(__name__)

@flask_app.route("/style.css")
def default_css_page():
    settings = {}
    resp = make_response(render_template("style.css", config=config.CONFIG))
    resp.cache_control.max_age = 24*60*60
    resp.mimetype = "text/css"
    return resp