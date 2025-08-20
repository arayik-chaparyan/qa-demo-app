from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = 'qademo_secret_key'  # Change this to a random secret key in production

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forms')
def forms():
    return render_template('index.html')

@app.route('/automation-practice-form')
def practice_form():
    return render_template('index.html')

@app.route('/browser-windows')
def browser_windows():
    return render_template('index.html')

@app.route('/alerts')
def alerts():
    return render_template('index.html')

@app.route('/frames')
def frames():
    return render_template('index.html')

@app.route('/windows')
def windows():
    return render_template('index.html')

# Nested Frames
@app.route('/nestedframes')
def nested_frames():
    return render_template('index.html')

# Modal Dialogs
@app.route('/modal-dialogs')
def modal_dialogs():
    return render_template('index.html')

# Elements - Text Box
@app.route('/text-box')
def text_box():
    return render_template('index.html')

# Elements - Check Box
@app.route('/checkbox')
def checkbox():
    return render_template('index.html')

# Elements - Radio Button
@app.route('/radio-button')
def radio_button():
    return render_template('index.html')

# Elements - Web Tables
@app.route('/webtables')
def webtables():
    return render_template('index.html')

# Elements - Buttons
@app.route('/buttons')
def buttons():
    return render_template('index.html')

# Elements - Links
@app.route('/links')
def links():
    return render_template('index.html')

# Elements - Broken Links - Images
@app.route('/broken')
def broken():
    return render_template('index.html')

# Elements - Upload and Download
@app.route('/upload-download')
def upload_download():
    return render_template('index.html')

# Elements - Dynamic Properties
@app.route('/dynamic-properties')
def dynamic_properties():
    return render_template('index.html')

# Widgets - Accordian
@app.route('/accordian')
def accordian():
    return render_template('index.html')

# Widgets - Auto Complete
@app.route('/auto-complete')
def auto_complete():
    return render_template('index.html')

# Widgets - Date Picker
@app.route('/date-picker')
def date_picker():
    return render_template('index.html')

# Widgets - Slider
@app.route('/slider')
def slider():
    return render_template('index.html')

# Widgets - Progress Bar
@app.route('/progress-bar')
def progress_bar():
    return render_template('index.html')

# Widgets - Tabs
@app.route('/tabs')
def tabs():
    return render_template('index.html')

# Widgets - Tool Tips
@app.route('/tool-tips')
def tool_tips():
    return render_template('index.html')

# Widgets - Menu
@app.route('/menu')
def menu():
    return render_template('index.html')

# Widgets - Select Menu
@app.route('/select-menu')
def select_menu():
    return render_template('index.html')

# Interactions - Sortable
@app.route('/sortable')
def sortable():
    return render_template('index.html')

# Interactions - Selectable
@app.route('/selectable')
def selectable():
    return render_template('index.html')

# Interactions - Resizable
@app.route('/resizable')
def resizable():
    return render_template('index.html')

# Interactions - Droppable
@app.route('/droppable')
def droppable():
    return render_template('index.html')

# Interactions - Dragabble
@app.route('/dragabble')
def dragabble():
    return render_template('index.html')

# Book Store Application - Login
@app.route('/login')
def login():
    return render_template('index.html')

# Book Store Application - Register
@app.route('/register')
def register():
    return render_template('index.html')

# Book Store Application - Book Store
@app.route('/books')
def books():
    return render_template('index.html')

# Book Store Application - Profile
@app.route('/profile')
def profile():
    return render_template('index.html')

# Book Store Application - Book Store API
@app.route('/swagger')
def swagger():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
