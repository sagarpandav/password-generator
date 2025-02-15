from flask import Flask, render_template, jsonify, request
import random
import string
import os

app = Flask(__name__, static_folder='static', static_url_path='/gen-pass/static')

def generate_password(length=16, use_upper=True, use_lower=True, use_numbers=True, use_special=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += "@#$%&*?"

    if not characters:
        characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "@#$%&*?" for c in password)

    score = 0
    if length >= 12:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score <= 2:
        return "weak"
    elif score <= 3:
        return "moderate"
    elif score <= 4:
        return "strong"
    else:
        return "very strong"

@app.route('/gen-pass/')
def index():
    return render_template('index.html')

@app.route('/gen-pass/generate', methods=['POST'])
def generate():
    length = int(request.json.get('length', 16))
    use_upper = request.json.get('useUpper', True)
    use_lower = request.json.get('useLower', True)
    use_numbers = request.json.get('useNumbers', True)
    use_special = request.json.get('useSpecial', False)

    password = generate_password(length, use_upper, use_lower, use_numbers, use_special)
    strength = check_strength(password)

    return jsonify({
        'password': password,
        'strength': strength
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
