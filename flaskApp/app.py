from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contacts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        msg = request.form.get('message')
        if name and email and msg:
            contacts.append({'name': name, 'email': email, 'message': msg})
            message = "Your message has been submitted successfully!"
        else:
            message = "Please fill in all fields."
    return render_template('index.html', message=message)

@app.route('/admin')
def admin():
    return render_template('admin.html', contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True)
