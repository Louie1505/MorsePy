import logging
import RPi.GPIO as GPIO
from Parser import Parser
from Morse import Character, Pause
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote
from time import sleep

def SendToLED(signal):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
     # Set pin 8 to be an output pin and set initial value to low (off)
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
    on = False

    for x in signal:
        on = not on
        GPIO.output(8, (GPIO.HIGH if on else GPIO.LOW))
        sleep(x)
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
        signal = []

        for char in coll:
            l = len(char.units)
            # We know the first signal is 'on' and every other/second signal is a pause so no need to differentiate, just store a list of lengths
            signal.append(l)
            if type(char) is Character:
                morseStr += "." if l == 1 else "-"
            elif type(char) is Pause:
                if l > 1:
                    morseStr += " "
                if l > 6:
                    morseStr += "/ "         
        
        self._set_response()

        # Output a rep of the signal
        self.wfile.write((''.join([str(x) for x in signal])).encode('utf-8'))

        self.wfile.write("<br/>".encode('utf-8'))
        self.wfile.write("<br/>".encode('utf-8'))

        # Output as morse
        self.wfile.write(morseStr.encode('utf-8'))

        self.wfile.write("<br/>".encode('utf-8'))
        self.wfile.write("<br/>".encode('utf-8'))

        # Just output the message
        self.wfile.write(message.encode("utf-8"))

        SendToLED(signal)


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