from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', total_tax=None)

@app.route('/calculate_tax', methods=['POST'])
def calculate_tax():
    amount = float(request.form['amount'])
    tax_rate = float(request.form['tax_rate'])
    total_tax = amount * (tax_rate / 100)
    return render_template('index.html', total_tax=round(total_tax, 2))

if __name__ == '__main__':
    app.run(debug=True)