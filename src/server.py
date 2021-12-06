from flask import Flask
from flask import send_from_directory

import os
import settings as s

__server__ = Flask(__name__)

@__server__.route('/')
def main():
    return ("Hello from flask")

@__server__.route('/stream/<path:code_stream>/<path:filename>')
def assets(code_stream, filename):
    """
    TODO: this method need sto change from the camera needing
    """
    path = os.path.join(s.get_path_folder_streaming(), code_stream)
    return send_from_directory(path, filename)