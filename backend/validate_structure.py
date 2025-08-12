#!/usr/bin/env python3
"""
Validate backend code structure and test basic functionality
"""

import os
import sys
from pathlib import Path

def test_file_structure():
    """Test if all required files exist"""
    print("Testing backend file structure...")
    
    required_files = [
        "app/__init__.py",
        "app/main.py",
        "app/core/__init__.py", 
        "app/core/config.py",
        "app/core/database.py",
        "app/api/__init__.py",
        "app/api/chess.py",
        "app/api/openings.py",
        "app/api/ai.py",
        "app/services/__init__.py",
        "app/services/chess_service.py",
        "app/services/opening_service.py",
        "requirements.txt"
    ]
    
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path}")
            missing_files.append(file_path)
    
    return len(missing_files) == 0

def test_syntax():
    """Test Python syntax in key files"""
    print("\nTesting Python syntax...")
    
    py_files = [
        "app/core/config.py",
        "app/main.py", 
        "app/api/chess.py",
        "app/services/chess_service.py"
    ]
    
    syntax_errors = []
    for file_path in py_files:
        try:
            with open(file_path, 'r') as f:
                compile(f.read(), file_path, 'exec')
            print(f"✓ {file_path} - syntax OK")
        except SyntaxError as e:
            print(f"✗ {file_path} - syntax error: {e}")
            syntax_errors.append(file_path)
        except FileNotFoundError:
            print(f"✗ {file_path} - file not found")
            syntax_errors.append(file_path)
    
    return len(syntax_errors) == 0

def test_api_endpoints():
    """Test API endpoint definitions"""
    print("\nTesting API endpoint structure...")
    
    try:
        with open("app/api/chess.py", 'r') as f:
            chess_api = f.read()
            
        endpoints_found = {
            "validate-move": "/validate-move" in chess_api,
            "analyze": "/analyze" in chess_api,
            "legal-moves": "/legal-moves" in chess_api
        }
        
        for endpoint, found in endpoints_found.items():
            status = "✓" if found else "✗"
            print(f"{status} {endpoint} endpoint")
            
        return all(endpoints_found.values())
    except Exception as e:
        print(f"✗ Error testing endpoints: {e}")
        return False

def create_mock_server():
    """Create a simple mock server for testing"""
    mock_server = '''#!/usr/bin/env python3
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
        print("\\nServer stopped")
'''
    
    with open("mock_server.py", "w") as f:
        f.write(mock_server)
    
    print("Created mock_server.py for testing")

if __name__ == "__main__":
    print("Chess Opening Trainer Backend - Structure Validation")
    print("=" * 60)
    
    structure_ok = test_file_structure()
    syntax_ok = test_syntax()
    endpoints_ok = test_api_endpoints()
    
    print("\\n" + "=" * 60)
    print("VALIDATION SUMMARY:")
    print("=" * 60)
    
    print(f"File Structure: {'✓ PASS' if structure_ok else '✗ FAIL'}")
    print(f"Syntax Check:   {'✓ PASS' if syntax_ok else '✗ FAIL'}")
    print(f"API Endpoints:  {'✓ PASS' if endpoints_ok else '✗ FAIL'}")
    
    if structure_ok and syntax_ok and endpoints_ok:
        print("\\n🎉 Backend structure is valid!")
        print("\\nTo run the full backend:")
        print("1. Install dependencies: pip3 install -r requirements.txt")  
        print("2. Start server: python3 -m uvicorn app.main:app --reload")
        
        create_mock_server()
        print("\\nTo test with mock server:")
        print("python3 mock_server.py")
    else:
        print("\\n⚠️  Backend structure needs fixes before running")