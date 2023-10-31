#!/usr/bin/env python3
'''
Basic Babel setup
'''

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    '''
    Configuration Class for Babel
    '''

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.before_request
def before_request() -> None:
    '''
    Executes before requets and performs routines
    '''
    user = get_user()
    g.user = user


def get_user() -> Union[Dict, None]:
    '''
    Obtains user from dictionary

    Args: N/A

    Returns: User
    '''
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@babel.localeselector
def get_locale() -> str:
    '''
    Function get_locale for a webpage

    Args: N/A

    Returns: Language best match to config
    '''
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    locale = query_table.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    user_details = getattr(g, 'user', None)
    if user_details and user_details['locale'] in app.config["LANGUAGES"]:
        return user_details['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    '''
    Obtains the timezone
    '''
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    '''
    Default app route

    Args: N/A

    Returns: HTML page
    '''
    g.time = format_datetime()
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
