#!/usr/bin/env python3
"""
Mock server for testing backend structure without dependencies
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class MockChessHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path
        
        if path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"message": "Chess Opening Trainer API", "version": "1.0.0"}
            self.wfile.write(json.dumps(response).encode())
            
        elif path == "/api/openings/systems":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "systems": [
                    {
                        "name": "Stonewall Attack",
                        "description": "Aggressive pawn structure with f4, e3, d4, c3",
                        "key_moves": ["d4", "e3", "f4", "c3", "Bd3"],
                        "starting_fen": "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1"
                    }
                ]
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        self.send_response(501)  # Not implemented in mock
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"error": "Mock server - POST not implemented"}
        self.wfile.write(json.dumps(response).encode())

if __name__ == "__main__":
    server = HTTPServer(('localhost', 8000), MockChessHandler)
    print("Mock Chess API server running on http://localhost:8000")
    print("Available endpoints:")
    print("  GET  /")
    print("  GET  /api/openings/systems")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
