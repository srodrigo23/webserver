from flask import Flask
from flask import send_from_directory

import os
import settings as s

app = Flask(__name__)

@app.route('/')
def main():
    return("Web Server")

@app.route('/<path:id_camera>/<path:folder_stream>/<path:filename>')
def streamming(id_camera, folder_stream, filename):
    """ Method to serve video fragments to HLS player"""
    source_path = s.get_path_folder_streaming()
    stream_folder_name = s.get_stream_folder_name()
    path = os.path.join(source_path, id_camera, stream_folder_name)
    return send_from_directory(path, filename)