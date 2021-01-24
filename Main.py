from Parser import Parser
from Morse import Character, Pause
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from urllib.parse import unquote

def SendToLED(message):
    print(message)
class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        message = unquote(self.path[1:])
        p = Parser()
        coll = p.Parse(message)
        morseStr = ""
        signalStr = ""

        ## Output in 'signal' format
        for char in coll:
            
            l = len(char.units)
            if type(char) is Character:
                morseStr += "." if l == 1 else "-"
                for _ in range(0, l):
                    signalStr += "-"
            elif type(char) is Pause:
                for _ in range(0, l):
                    signalStr += " "
                if l > 1:
                    morseStr += " "
                if l > 6:
                    morseStr += "/ "         

        SendToLED(signalStr)
        
        self._set_response()

        # Output a rep of the signal
        self.wfile.write(signalStr.encode('utf-8'))

        self.wfile.write("<br/>".encode('utf-8'))
        self.wfile.write("<br/>".encode('utf-8'))

        # Output as morse
        self.wfile.write(morseStr.encode('utf-8'))

        self.wfile.write("<br/>".encode('utf-8'))
        self.wfile.write("<br/>".encode('utf-8'))

        # Just output the message
        self.wfile.write(message.encode("utf-8"))


def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()