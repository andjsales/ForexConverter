API: https://exchangerate.host/dashboard

# Set up

Before running the application, you'll need to set up your API key for the ExchangeRate API.

1. Export the API key as an environment variable:
   ```bash
   export API_KEY_ENV_VAR='your_api_key'
   ```

# Usage

1. Create venv:  
   `python3 -m venv venv`  
   `source venv/bin/activate`

2. Install dependencies:  
   `pip install -r requirements.txt`

3. Set environment variables for development:  
   `export FLASK_APP=app.py`  
   `export FLASK_ENV=development`

4. Start server  
   `flask run`
