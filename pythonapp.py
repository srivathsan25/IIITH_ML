from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('projecthdfc.html')

@app.route('/submit', methods=['POST'])
def submit():
    
    data = request.form
    print("Received form data:", data)
    # Extract form data
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    loan_amount = data.get('loan_amount')
    income = data.get('income')
    employment_status = data.get('employment_status')
    loan_purpose = data.get('loan_purpose')

    # Here you would normally save data or process it
    # For demo, just display a confirmation

    return f"""
    <h2>Thank you, {name}!</h2>
    <p>Your loan application for ${loan_amount} has been received.</p>
    <p>We will contact you shortly at {email} or {phone}.</p>
    <a href="/">Back to form</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
