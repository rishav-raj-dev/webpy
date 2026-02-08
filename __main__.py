"""
Main entry point for WebPy module
"""
import sys
import argparse
from server import run_server


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='WebPy - Live Python Code Execution Server',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
            Examples:
            python -m webpy                    # Start server on default port 5000
            python -m webpy --port 8080        # Start server on port 8080
            python -m webpy --host 0.0.0.0     # Allow external connections
            
            Make sure you have a file named 'main.py' in the current directory!
                    """
    )
    
    parser.add_argument(
        '--host',
        default='127.0.0.1',
        help='Host to bind to (default: 127.0.0.1)'
    )
    
    parser.add_argument(
        '--port',
        type=int,
        default=5000,
        help='Port to bind to (default: 5000)'
    )
    
    parser.add_argument(
        '--no-debug',
        action='store_true',
        help='Disable debug mode'
    )

    parser.add_argument(
        "--production",
        action='store_true',
        help='Run the server in the production mode.'
    )
    
    args = parser.parse_args()
    
    try:
        run_server(
            host=args.host,
            port=args.port,
            debug=not args.no_debug,
            production=args.production
        )
    except KeyboardInterrupt:
        print("\n\n👋 WebPy server stopped. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
