#!/usr/bin/env python3
"""
WebPy v1.0 - Improved Standalone Version with input() Support
Run with: python webpy_v1_standalone.py

v1.0 Improvements:
- One input box at a time (not all at once)
- Press Enter to submit (no button needed)
- Input values stay visible after entry
- Fixed form resubmission issue on refresh
"""

import sys
import io
import importlib.util
from pathlib import Path
from flask import Flask, render_template_string, request, redirect, url_for, session
from datetime import datetime
import secrets
from waitress import serve

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebPy v1 - Live Python Execution</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container { max-width: 900px; margin: 0 auto; }
        .header {
            background: white;
            padding: 30px;
            border-radius: 10px 10px 0 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .header h1 { color: #667eea; font-size: 32px; margin-bottom: 10px; }
        .header .subtitle { color: #666; font-size: 14px; }
        .version-badge {
            display: inline-block;
            background: #4CAF50;
            color: white;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
            margin-left: 10px;
        }
        .info-bar {
            background: #f7f7f7;
            padding: 15px 30px;
            border-left: 4px solid #667eea;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 13px;
            color: #555;
            flex-wrap: wrap;
            gap: 10px;
        }
        .input-section {
            background: white;
            padding: 25px 30px;
            border-left: 4px solid #FF9800;
        }
        .input-section h3 { 
            color: #FF9800; 
            margin-bottom: 15px; 
            font-size: 16px; 
        }
        .previous-inputs {
            margin-bottom: 20px;
            padding: 15px;
            background: #f9f9f9;
            border-radius: 5px;
            border-left: 3px solid #4CAF50;
        }
        .previous-inputs h4 {
            font-size: 13px;
            color: #666;
            margin-bottom: 10px;
        }
        .previous-input-item {
            display: flex;
            gap: 10px;
            margin-bottom: 8px;
            font-size: 14px;
            flex-wrap: wrap;
        }
        .previous-input-label {
            font-weight: 600;
            color: #333;
            min-width: 150px;
        }
        .previous-input-value {
            color: #4CAF50;
            font-family: 'Courier New', monospace;
            font-weight: 600;
        }
        .input-group { 
            display: flex; 
            flex-direction: column; 
            gap: 10px; 
        }
        .input-group label { 
            font-weight: 600; 
            color: #333; 
            font-size: 15px; 
        }
        .input-row {
            display: flex;
            gap: 10px;
            align-items: stretch;
        }
        .input-group input {
            flex: 1;
            padding: 14px;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
            font-family: 'Courier New', monospace;
            transition: border-color 0.3s;
        }
        .input-group input:focus { 
            outline: none; 
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        .submit-btn {
            background: #667eea;
            color: white;
            border: none;
            padding: 14px 30px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            transition: background 0.3s;
            white-space: nowrap;
            min-width: 100px;
        }
        .submit-btn:hover { 
            background: #5568d3; 
        }
        .submit-btn:active {
            transform: scale(0.98);
        }
        .input-hint {
            font-size: 12px;
            color: #888;
            font-style: italic;
        }
        .output-container {
            background: #1e1e1e;
            padding: 30px;
            border-radius: 0 0 10px 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            min-height: 300px;
        }
        .output-title {
            color: #4CAF50;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 15px;
            font-family: 'Courier New', monospace;
        }
        .output {
            color: #f0f0f0;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.6;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        .error {
            color: #ff6b6b;
            background: rgba(255, 107, 107, 0.1);
            border-left: 3px solid #ff6b6b;
            padding: 15px;
            border-radius: 5px;
            margin-top: 10px;
        }
        .reload-btn {
            background: #667eea;
            color: white;
            border: none;
            padding: 8px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 13px;
            font-weight: 600;
            transition: background 0.3s;
            text-decoration: none;
            display: inline-block;
        }
        .reload-btn:hover { background: #5568d3; }
        .status {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
        }
        .status.success { background: #d4edda; color: #155724; }
        .status.error { background: #f8d7da; color: #721c24; }
        .status.waiting { background: #fff3cd; color: #856404; }
        .empty-output { color: #888; font-style: italic; }
        
        /* Mobile-specific styles */
        @media (max-width: 768px) {
            body { padding: 10px; }
            .header h1 { font-size: 24px; }
            .header { padding: 20px; }
            .input-section { padding: 20px; }
            .output-container { padding: 20px; }
            .input-row {
                flex-direction: column;
                gap: 10px;
            }
            .submit-btn {
                width: 100%;
                padding: 16px;
                font-size: 18px;
            }
            .input-group input {
                font-size: 16px;
                padding: 12px;
            }
            .previous-input-item {
                flex-direction: column;
                gap: 5px;
            }
            .previous-input-label {
                min-width: auto;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🐍 WebPy Live Executor <span class="version-badge">v1.0</span></h1>
            <p class="subtitle">Executes Python code with input() support on every refresh</p>
        </div>
        
        <div class="info-bar">
            <div>
                <strong>File:</strong> {{ filename }} &nbsp;|&nbsp; 
                <strong>Executed:</strong> {{ timestamp }}
            </div>
            <div>
                <span class="status {{ status_class }}">{{ status_text }}</span>
                <a href="/" class="reload-btn">↻ Reset</a>
            </div>
        </div>
        
        {% if needs_input %}
        <form method="POST" action="/submit" class="input-section">
            <h3>📝 Input Required</h3>
            
            {% if previous_inputs %}
            <div class="previous-inputs">
                <h4>✅ Previously entered:</h4>
                {% for prev_prompt, prev_value in previous_inputs %}
                <div class="previous-input-item">
                    <span class="previous-input-label">{{ prev_prompt if prev_prompt else 'Input' }}:</span>
                    <span class="previous-input-value">{{ prev_value }}</span>
                </div>
                {% endfor %}
            </div>
            {% endif %}
            
            <div class="input-group">
                <label for="current_input">{{ current_prompt if current_prompt else 'Enter value' }}</label>
                <div class="input-row">
                    <input type="text" 
                           id="current_input" 
                           name="current_input" 
                           placeholder="Type your answer..." 
                           required
                           autofocus
                           value="{{ last_value }}">
                    <button type="submit" class="submit-btn">→ Submit</button>
                </div>
            </div>
        </form>
        {% endif %}
        
        <div class="output-container">
            <div class="output-title">>>> OUTPUT</div>
            {% if output %}
                <div class="output">{{ output }}</div>
            {% else %}
                <div class="output empty-output">
                    {% if needs_input %}
                        Waiting for input...
                    {% else %}
                        No output. Add print() statements to your code.
                    {% endif %}
                </div>
            {% endif %}
            
            {% if error %}
                <div class="error">
                    <strong>❌ Error:</strong><br>
                    {{ error }}
                </div>
            {% endif %}
        </div>
    </div>
</body>
</html>
"""


class InputCapture:
    """Captures input() calls and their prompts"""
    def __init__(self, provided_inputs=None):
        self.prompts = []
        self.provided_inputs = provided_inputs or []
        self.input_index = 0
        
    def mock_input(self, prompt=""):
        """Mock input function"""
        self.prompts.append(prompt)
        
        if self.input_index < len(self.provided_inputs):
            value = self.provided_inputs[self.input_index]
            self.input_index += 1
            print(f"{prompt}{value}")
            return value
        else:
            raise NeedsInputException("Code requires user input")


class NeedsInputException(Exception):
    """Raised when code needs input from user"""
    pass


def execute_user_code(file_path, provided_inputs=None):
    """Execute user's Python code and capture print/input"""
    output = io.StringIO()
    error = None
    needs_input = False
    input_prompts = []
    
    old_stdout = sys.stdout
    sys.stdout = output
    
    input_capture = InputCapture(provided_inputs)
    
    import builtins
    old_input = builtins.input
    builtins.input = input_capture.mock_input
    
    try:
        spec = importlib.util.spec_from_file_location("user_code", file_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        else:
            error = f"Could not load file: {file_path}"
            
    except NeedsInputException:
        needs_input = True
        input_prompts = input_capture.prompts
        
    except Exception as e:
        error = f"{type(e).__name__}: {str(e)}\n\n"
        import traceback
        error += traceback.format_exc()
    
    finally:
        sys.stdout = old_stdout
        builtins.input = old_input
    
    return output.getvalue(), error, needs_input, input_prompts


@app.route('/', methods=['GET'])
def index():
    """Main route - GET only (fresh start)"""
    session.clear()
    
    user_code_path = Path('main.py')
    
    if not user_code_path.exists():
        return render_template_string(
            HTML_TEMPLATE,
            filename='main.py',
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            output='',
            error='File "main.py" not found.\n\nCreate main.py in the same directory.',
            status_class='error',
            status_text='FILE NOT FOUND',
            needs_input=False,
            current_prompt='',
            previous_inputs=[],
            last_value=''
        )
    
    output, error, needs_input, input_prompts = execute_user_code(user_code_path, [])
    
    if needs_input:
        session['provided_inputs'] = []
        session['all_prompts'] = input_prompts
        
        status_class = 'waiting'
        status_text = 'WAITING FOR INPUT'
        current_prompt = input_prompts[0] if input_prompts else 'Enter value'
    else:
        status_class = 'error' if error else 'success'
        status_text = 'ERROR' if error else 'SUCCESS'
        current_prompt = ''
    
    return render_template_string(
        HTML_TEMPLATE,
        filename='main.py',
        timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        output=output,
        error=error,
        status_class=status_class,
        status_text=status_text,
        needs_input=needs_input,
        current_prompt=current_prompt,
        previous_inputs=[],
        last_value=''
    )


@app.route('/submit', methods=['POST'])
def submit():
    """Handle input submission"""
    user_code_path = Path('main.py')
    
    current_value = request.form.get('current_input', '')
    
    provided_inputs = session.get('provided_inputs', [])
    all_prompts = session.get('all_prompts', [])
    
    provided_inputs.append(current_value)
    
    output, error, needs_input, new_prompts = execute_user_code(user_code_path, provided_inputs)
    
    if needs_input:
        session['provided_inputs'] = provided_inputs
        session['all_prompts'] = new_prompts
        
        previous_inputs_display = list(zip(all_prompts[:len(provided_inputs)], provided_inputs))
        
        current_input_index = len(provided_inputs)
        current_prompt = new_prompts[current_input_index] if current_input_index < len(new_prompts) else 'Enter value'
        
        return render_template_string(
            HTML_TEMPLATE,
            filename='main.py',
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            output=output,
            error=error,
            status_class='waiting',
            status_text='WAITING FOR INPUT',
            needs_input=True,
            current_prompt=current_prompt,
            previous_inputs=previous_inputs_display,
            last_value=''
        )
    else:
        session['final_output'] = output
        session['final_error'] = error
        session['execution_complete'] = True
        
        return redirect(url_for('show_result'))


@app.route('/result')
def show_result():
    """Show final result"""
    output = session.get('final_output', '')
    error = session.get('final_error', None)
    
    session.clear()
    
    status_class = 'error' if error else 'success'
    status_text = 'ERROR' if error else 'SUCCESS'
    
    return render_template_string(
        HTML_TEMPLATE,
        filename='main.py',
        timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        output=output,
        error=error,
        status_class=status_class,
        status_text=status_text,
        needs_input=False,
        current_prompt='',
        previous_inputs=[],
        last_value=''
    )


def run_server(host='127.0.0.1',port=5000,debug=True, production = False):
    print("\n" + "="*60)
    print("🚀 WebPy V1.0 Standalone Server Starting...")
    print("="*60)
    print(f"📁 Watching for: main.py")
    print(f"🌐 Server: http://127.0.0.1:{port}")
    print(f"💡 Open in your browser")
    print(f"✨ NEW: input() support enabled!")
    print("="*60 + "\n")

    if production:
        # Use Waitress (production WSGI server)
        print("🔒 Production mode: Waitress WSGI")
        serve(app, host=host, port=port, threads=4)
    else:
        # Use Flask dev server (with warning, that's OK!)
        print("⚠️  Development mode - not for production!")
        app.run(host=host, port=port, debug=debug)