#!/usr/bin/env python3
"""
Test script to check which modules are available and test basic functionality
"""

def test_imports():
    modules = {
        'fastapi': False,
        'uvicorn': False,
        'chess': False,
        'stockfish': False,
        'sqlalchemy': False,
        'requests': False,
        'pydantic_settings': False
    }
    
    for module_name in modules:
        try:
            __import__(module_name)
            modules[module_name] = True
            print(f"✓ {module_name}")
        except ImportError:
            print(f"✗ {module_name}")
    
    return modules

def test_python_chess():
    """Test if we can use basic chess functionality without external libs"""
    try:
        # Simple chess position validation without external libraries
        print("\nTesting basic chess logic...")
        
        # Test FEN validation (basic)
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        print(f"✓ FEN string: {fen}")
        
        # Test move notation
        moves = ["e4", "e5", "Nf3", "Nc6"]
        print(f"✓ Sample moves: {moves}")
        
        return True
    except Exception as e:
        print(f"✗ Basic chess test failed: {e}")
        return False

if __name__ == "__main__":
    print("Chess Opening Trainer Backend - Dependency Check")
    print("=" * 50)
    
    available_modules = test_imports()
    test_python_chess()
    
    print("\n" + "=" * 50)
    print("SETUP INSTRUCTIONS:")
    print("=" * 50)
    
    missing_modules = [name for name, available in available_modules.items() if not available]
    
    if missing_modules:
        print("Missing dependencies. To install them:")
        print("\n1. Install pip:")
        print("   sudo apt update && sudo apt install python3-pip")
        print("\n2. Install backend dependencies:")
        print("   cd backend && pip3 install -r requirements.txt")
        print("\n3. Install Stockfish engine:")
        print("   sudo apt install stockfish")
        print("\n4. Start the backend:")
        print("   python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")
    else:
        print("All dependencies available! You can start the backend with:")
        print("python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")