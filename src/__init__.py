from server import __server__

import settings as s

def run_web_server(host, port):
    __server__.run(host=host, port=port, debug=True)
    
if __name__ == "__main__":
    run_web_server(s.get_host(), s.get_port())