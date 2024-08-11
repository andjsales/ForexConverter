### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python is used for backend data analysis, and runs on the server.
JavaScript is used for user handling and DOM manipulation

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

d.get('c', default_value)
if 'c' in d: value = dict['c']

- What is a unit test?

testing functionality for singular functions

- What is an integration test?

testing the flow of functions when working together

- What is the role of web application framework, like Flask?

serves as a web framework, routing the client to different pages, and data flow

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

route URL: for getting to important and specific data
URL query param: used when toggling optional filters

- How do you collect data from a URL placeholder parameter using Flask?

@app.route('/home/<param>')
return f"Hello there, <param>!"

- How do you collect data from the query string using Flask?

request.args.get('key')

- How do you collect data from the body of the request using Flask?

request.form()
request.json()

- What is a cookie and what kinds of things are they commonly used for?

a cookie is a small amount of data that is stored on user's device.
usually used for logged in info and filter preferences

- What is the session object in Flask?

it stores user-specific data through requests

- What does Flask's `jsonify()` do?

converts Python dictionaries into JSON responses
