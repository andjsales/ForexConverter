from flask import Flask, render_template, request, flash
import os
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

base_url = 'http://api.exchangerate.host/'
api_key = os.getenv("API_KEY_ENV_VAR")
print("API Key:", api_key)


def get_supported_currencies(api_key):
    """
    Display currencies supported by API
    """

    response = requests.get(f"{base_url}list?access_key={api_key}")
    data = response.json()
    return data.get('currencies', {})


def convert_currency(convert_from, convert_to, amount):
    """
    Conversion of currency
    """

    response = requests.get(
        f"{base_url}convert?from={convert_from}&to={convert_to}&amount={amount}&access_key={api_key}")
    data = response.json()
    result = data.get('result')

    if result is not None:
        return round(float(result), 2)
    else:
        flash_error_message(response)
        return None


def flash_error_message(response):
    """
    Flash error if status_code receives an error.
    """

    error_data = response.json().get('error', {})
    error_code = error_data.get('code', 0)
    convert_from = request.form['convert_from'].upper()
    convert_to = request.form['convert_to'].upper()
    amount = request.form['amount']
    if error_code == 400:
        flash("Bad Request")
    elif error_code == 401:
        flash(f"Not a valid currency: '{convert_from}'")
    elif error_code == 402:
        flash(f"Not a valid currency: '{convert_to}'")
    elif error_code == 403:
        flash(f"Not a valid number: '{amount}'")
    elif error_code == 404:
        flash("Not Found")
    else:
        flash("An error occurred")


# @app.route('/', methods=['GET', 'POST'])
# def homepage():
#     """
#     Displays currency
#     """

#     converted_amount = None
#     result_message = None
#     supported_currencies = get_supported_currencies(api_key)

#     if request.method == 'POST':
#         convert_from = request.form['convert_from'].upper()
#         convert_to = request.form['convert_to'].upper()
#         amount = request.form['amount']

#         converted_amount = convert_currency(convert_from, convert_to, amount)

#         if converted_amount is not None:
#             result_message = f"{amount} {convert_from} is equivalent to {converted_amount} {convert_to}."
#         else:
#             result_message = "Conversion failed:"

#     return render_template('index.html', converted_amount=converted_amount, result_message=result_message, supported_currencies=supported_currencies)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        convert_from = request.form.get('convert_from', '').upper()
        convert_to = request.form.get('convert_to', '').upper()
        amount = request.form.get('amount', '0')

        print(
            f"Converting from {convert_from} to {convert_to} amount {amount}")

        converted_amount = convert_currency(convert_from, convert_to, amount)
        if converted_amount is not None:
            result_message = f"{amount} {convert_from} is equivalent to {converted_amount} {convert_to}."
        else:
            result_message = "Conversion failed or error occurred."

        # Ensure to return the template with the result message and supported currencies
        supported_currencies = get_supported_currencies(api_key)
        return render_template('index.html', result_message=result_message, supported_currencies=supported_currencies)

    # For GET requests
    supported_currencies = get_supported_currencies(api_key)
    return render_template('index.html', supported_currencies=supported_currencies)


if __name__ == '__main__':
    app.run(debug=True)
