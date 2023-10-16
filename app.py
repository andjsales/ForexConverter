from flask import Flask, render_template, request, flash
import os
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

base_url = 'http://api.exchangerate.host/'
os.environ['API_KEY_ENV_VAR'] = 'daff0b9b4d855f63c2ad3a313e0425d8'
api_key = os.getenv("API_KEY_ENV_VAR")

print("Fetching supported currencies...")  # Debug statement
response = requests.get(
    f"http://api.exchangerate.host/list?access_key={api_key}")
if response.status_code == 200:
    data = response.json()
    supported_currencies = data.get('currencies', {})
    print(supported_currencies)
else:
    supported_currencies = {}
    print("Could not load supported currencies.")


@app.route('/', methods=['GET', 'POST'])
def homepage():
    """display the currenvy converter"""

    converted_amount = None
    result_message = None

    if request.method == 'POST':
        convert_from = request.form['convert_from'].upper()
        convert_to = request.form['convert_to'].upper()
        amount = request.form['amount']

        response = requests.get(
            f"{base_url}convert?from={convert_from}&to={convert_to}&amount={amount}&access_key={api_key}")
        data = response.json()
        error_data = response.json().get('error', {})
        error_code = error_data.get('code', 0)

        if error_code == 401:
            flash(f"Not a valid currency: {convert_from}")

        elif error_code == 402:
            flash(f"Not a valid currency: {convert_to}")

        elif error_code == 403:
            flash(f"Not a valid number: {amount}")

        else:
            converted_amount = round(float(data.get('result', 'N/A')), 2)
            result_message = f"{amount} {convert_from} is equivalent to {converted_amount} {convert_to}."

    print("Fetching supported currencies...")  # Debug statement
    response = requests.get(
        f"http://api.exchangerate.host/list?access_key={api_key}")
    if response.status_code == 200:
        data = response.json()
        supported_currencies = data.get('currencies', {})
        print(supported_currencies)
    else:
        supported_currencies = {}
        print("Could not load supported currencies.")

    return render_template('index.html', converted_amount=converted_amount, result_message=result_message, supported_currencies=supported_currencies)


if __name__ == '__main__':
    app.run(debug=True)
