# 🐍 WebPy - Turn Any Python Script into a Web App Instantly

> **Stop worrying about backends and frontends.** WebPy transforms your CLI Python scripts into interactive web applications with **zero configuration**. Perfect for sharing demos, teaching Python, or rapid prototyping.

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🎯 Why WebPy?

Ever built a cool Python script but struggled to share it with non-technical people? WebPy solves this:

```python
# Your CLI script
name = input("What's your name? ")
age = input("How old are you? ")
print(f"Hello {name}, you're {age} years old!")
```

**Without WebPy:** "Um, open terminal, install Python, run `python script.py`..."  
**With WebPy:** "Just visit this link!" → Beautiful web interface, no terminal needed! 🎉

### 🚀 Use Cases

- **📊 Share Data Analysis Scripts** - Let anyone run your analysis without Python knowledge
- **🧮 Deploy Quick Tools** - Calculators, converters, generators as web apps
- **👨‍🏫 Teaching Python** - Students see output instantly in browser
- **🎮 Interactive Demos** - Show your Python projects to clients/recruiters
- **⚡ Rapid Prototyping** - Test ideas without building full web apps
- **🔧 Internal Tools** - Company scripts accessible via browser

### ✨ Key Features

- 🌐 **CLI → Web Instantly** - No backend/frontend coding needed
- 📝 **Full `input()` Support** - Interactive forms automatically generated
- 🎨 **Beautiful UI** - Professional interface out of the box
- 🔄 **Live Code Updates** - Edit script, refresh browser, see changes
- 📱 **Mobile Friendly** - Works perfectly on phones and tablets
- 🔒 **Isolated Execution** - Clean slate on every run
- ⚡ **Zero Configuration** - Just run and go

---

## 🚀 Quick Start (60 Seconds)

### Installation

```bash
# Clone the repository
git clone https://github.com/rishav-raj-dev/webpy.git
cd webpy

# Install dependencies
pip install -r requirements.txt
```

### Create Your First Web App

```python
# main.py
name = input("What's your name? ")
print(f"Hello, {name}! Welcome to WebPy!")

age = input("How old are you? ")
print(f"Wow, {age} years old! That's awesome!")

print("\n✅ Thanks for using WebPy!")
```

### Run It

```bash
python -m webpy
```

### Open Browser

Visit: **`http://localhost:5000`**

**That's it!** Your CLI script is now a web app! 🎉

---

## 📖 How It Works

WebPy automatically:
1. ✅ Detects `print()` statements → Displays output beautifully
2. ✅ Detects `input()` calls → Generates web forms
3. ✅ Handles multiple inputs → One at a time, step by step
4. ✅ Shows previous inputs → User sees their answers
5. ✅ Re-executes on refresh → Clean slate every time

**No changes to your Python code needed!**

---

## 💻 Examples

### Example 1: Calculator

```python
# calculator.py
print("🧮 Simple Calculator\n")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
op = input("Operation (+, -, *, /): ")

n1, n2 = float(num1), float(num2)

if op == "+":
    result = n1 + n2
elif op == "-":
    result = n1 - n2
elif op == "*":
    result = n1 * n2
elif op == "/":
    result = n1 / n2 if n2 != 0 else "Error"

print(f"\n✅ Result: {n1} {op} {n2} = {result}")
```

Run: `python -m webpy`  
**Result:** Professional calculator web app! 🧮

### Example 2: Quiz App

```python
# quiz.py
print("📚 Python Quiz\n")

q1 = input("What does 'print()' do? ")
if "output" in q1.lower():
    print("✅ Correct!")
else:
    print("❌ Try again!")

q2 = input("What is 5 + 3? ")
if q2 == "8":
    print("✅ Perfect!")
else:
    print("❌ The answer is 8")

print("\n🎉 Quiz completed!")
```

**Result:** Interactive quiz accessible from any browser! 📝

### Example 3: Data Analyzer

```python
# analyzer.py
print("📊 Data Analyzer\n")

data = input("Enter numbers (comma-separated): ")
numbers = [float(x.strip()) for x in data.split(",")]

print(f"Count: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers)/len(numbers):.2f}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
```

**Result:** Data analysis tool anyone can use! 📈

---

## 🎨 Features in Detail

### ✅ Print Statement Capture

All `print()` output is beautifully formatted:

```python
print("=" * 40)
print("My Output")
print("=" * 40)
```

Displays with:
- 🎨 Monospace font
- 🌙 Dark theme output area
- 📱 Responsive layout
- ✨ Syntax-aware formatting

### ✅ Interactive Input Forms

```python
name = input("Your name: ")
email = input("Your email: ")
```

Automatically generates:
- 📝 Labeled input fields
- ➡️ Submit button (mobile-friendly)
- ⌨️ Enter key support (desktop)
- ✅ Shows previous inputs
- 📱 Fully responsive

### ✅ One Input at a Time

Instead of overwhelming users with all inputs at once:

```
Step 1: What's your name? [____] → Submit
       ↓
Step 2: ✅ Name: John
        How old are you? [____] → Submit
       ↓
Step 3: ✅ Name: John
        ✅ Age: 25
        [Final Output]
```


## 🔧 Advanced Usage

### Command Line Options

WebPy supports several command-line flags to customize how the server runs:

```bash
# Basic usage (default: localhost:5000, debug mode on)
python -m webpy

# Custom port
python -m webpy --port 8080

# Custom host (allow external connections)
python -m webpy --host 0.0.0.0

# Disable debug mode
python -m webpy --no-debug

# Production mode (uses Waitress server instead of Flask dev server)
python -m webpy --production

# Combine options
python -m webpy --host 0.0.0.0 --port 8080 --production
```

#### Available Flags:

| Flag | Default | Description |
|------|---------|-------------|
| `--host` | `127.0.0.1` | Host to bind to. Use `0.0.0.0` to allow external connections |
| `--port` | `5000` | Port to bind to (any available port number) |
| `--no-debug` | Debug on | Disable Flask debug mode (auto-reload, detailed errors) |
| `--production` | Off | Run in production mode using Waitress WSGI server |

**Examples:**

```bash
# Development on different port
python -m webpy --port 3000

# Share with your team on local network
python -m webpy --host 0.0.0.0 --port 5000

# Production deployment
python -m webpy --host 0.0.0.0 --port 8000 --production --no-debug
```

### Share on Local Network

1. Start with: `python -m webpy --host 0.0.0.0`
2. Find your IP: `ifconfig` (Mac/Linux) or `ipconfig` (Windows)
3. Share link: `http://YOUR_IP:5000`
4. Anyone on your network can access! 🌐

### Deploy to Production

**Option 1: Use built-in production mode (Recommended)**

```bash
# WebPy includes Waitress for production
python -m webpy --host 0.0.0.0 --port 8000 --production --no-debug
```

**Option 2: Use Gunicorn (Linux/Mac)**

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 webpy.server:app
```

---

## 📦 Project Structure

```
webpy/
├── webpy_v2_mobile.py       # Main application (mobile-friendly)
├── requirements.txt         # Dependencies (just Flask!)
├── README.md               # This file
├── examples/               # Example scripts
│   ├── calculator.py
│   ├── quiz.py
│   └── analyzer.py
└── main.py           # Your Python script goes here
```

---

## 🎓 Use Cases & Ideas

### For Teachers
- **Live Coding Demos** - Students see output instantly
- **Interactive Lessons** - No setup, just share a link
- **Homework Checker** - Students submit via web interface

### For Developers
- **Quick Prototypes** - Test ideas without full stack
- **Internal Tools** - Share scripts with team
- **Client Demos** - Professional presentation of CLI tools

### For Learners
- **Instant Feedback** - See results immediately
- **No Setup Hassle** - Just code and run
- **Share Progress** - Show friends your projects

### For Data Scientists
- **Analysis Tools** - Let others run your analysis
- **Calculators** - Share formulas as web apps
- **Visualizations** - Quick data explorers

---

## ⚙️ Configuration

### File Setup

Place your Python script as `main.py` in the same directory:

```
webpy/
├── webpy_v2_mobile.py
└── main.py  ← Your script
```

### Customization

Edit `webpy_v2_mobile.py` to customize:
- UI colors and styling
- Server port and host
- Error messages
- Timeout settings

---

## 🐛 Troubleshooting

### Script Not Found

```
Error: File "main.py" not found
```

**Solution:** Create `main.py` in the same directory as `webpy_v2_mobile.py`

### Port Already in Use

```
Error: Address already in use
```

**Solution:** Use a different port: `--port 8080`

### Import Errors

```
ModuleNotFoundError: No module named 'pandas'
```

**Solution:** Install missing packages: `pip install pandas`

### Mobile Submit Button Not Working

**Solution:** Make sure you're using `webpy_v2_mobile.py` (not older versions)

---

## ⚠️ Security Notes

### For Local Use ✅

WebPy is **safe** for:
- Personal projects on your computer
- Local network sharing (trusted users)
- Teaching in controlled environments
- Internal company tools

### For Public Deployment ⚠️

If deploying publicly, implement:
- 🔐 User authentication
- 🛡️ Code sandboxing
- ⏱️ Execution timeouts
- 📊 Rate limiting
- 🔒 HTTPS/SSL
- 📝 Audit logging

**Never expose to internet without security measures!**

---

## 🛣️ Roadmap

### Current Version (v2.0) ✅
- ✅ Print statement capture
- ✅ Interactive input() support
- ✅ Mobile-friendly interface
- ✅ One input at a time
- ✅ Clean slate execution
- ✅ Beautiful UI

### Planned Features
- [ ] In-browser code editor
- [ ] File upload support
- [ ] Multiple script support
- [ ] Execution history
- [ ] Download output
- [ ] Dark/light theme toggle
- [ ] Syntax highlighting
- [ ] Auto-refresh option
- [ ] Code persistence
- [ ] User sessions

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**TL;DR:** Free to use, modify, and distribute. Just keep the license notice.

---

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/) - Micro web framework
- Inspired by the need to share Python scripts easily
- Made for learners, teachers, and developers worldwide

---

## 📧 Support & Contact

- 🐛 **Found a bug?** [Open an issue](https://github.com/rishav-raj-dev/webpy/issues)
- 💡 **Have an idea?** [Start a discussion](https://github.com/rishav-raj-dev/webpy/discussions)
- ⭐ **Like the project?** Give it a star!

---

## 🌟 Star History

If you find WebPy useful, please ⭐ star the repository! It helps others discover the project.

---

## 📊 Quick Comparison

| Need | Traditional Way | WebPy Way |
|------|----------------|-----------|
| **Share a script** | Send `.py` file, explain setup | Share a link |
| **Collect input** | Parse `sys.argv` or `input()` | Auto-generated forms |
| **Display output** | Terminal text | Beautiful web UI |
| **Make it pretty** | Learn CSS/HTML/JS | Already done |
| **Mobile access** | Doesn't work | Fully responsive |
| **Setup time** | Hours/days | 60 seconds |

---

## 🚀 Get Started Now!

```bash
git clone https://github.com/rishav-raj-dev/webpy.git
cd webpy
pip install -r requirements.txt
echo 'print("Hello WebPy!")' > main.py
python -m webpy
```

**Visit `http://localhost:5000` and see your script running! 🎉**

---

<div align="center">

**Made with ❤️ for the Python community**

**Stop building backends. Start building features.** 🐍✨

[⭐ Star](https://github.com/rishav-raj-dev/webpy) • [🐛 Report Bug](https://github.com/rishav-raj-dev/webpy/issues) • [💡 Request Feature](https://github.com/rishav-raj-dev/webpy/issues)

</div>