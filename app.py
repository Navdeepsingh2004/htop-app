from flask import Flask
import os
import datetime
import subprocess
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your full name
    username = os.getlogin()
    ist_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S IST')
    top_output = subprocess.getoutput('top -b -n 1')

    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
