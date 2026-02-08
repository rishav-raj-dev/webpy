"""
WebPy - Live Python Code Execution Server

A simple web server that executes your Python code on every page refresh
and displays the output in your browser.

Usage:
    python -m webpy

Or programmatically:
    from webpy import run_server
    run_server()
"""

__version__ = '1.0.0'
__author__ = 'WebPy'

from .server import run_server, app

__all__ = ['run_server', 'app']
