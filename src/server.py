from flask import Flask
from flask import send_from_directory

import os
import settings as s

__server__ = Flask(__name__)

@__server__.route('/')
def main():
    return ("Hello from flask")

@__server__.route('/stream/<path:numstream>/<path:filename>')
def assets(code_stream, filename):
    path = os.path.join(s.get_path_folder_streaming(), f"live_{code_stream}")
	return send_from_directory(path, filename)