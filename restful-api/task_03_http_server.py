#!/usr/bin/python3
"""Module who Develop a simple API using
Python with the `http.server` module"""


import http.server
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """class set up a simple HTTP server"""

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)  # envoie le code de statut
            self.send_header("Content-Type", "text/plain")
            self.end_headers()  # termine les headers
            self.wfile.write(
                "Hello, this is a simple API!".encode())  # envoie le contenu

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps
                ({"name": "John", "age": 30, "city": "New York"})
                .encode()
                )

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode())

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())


if __name__ == "__main__":

    server = http.server.HTTPServer(("", 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
