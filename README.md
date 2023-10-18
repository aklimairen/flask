# what flask python module? 

Flask is a web application framework written in Python. It is a microframework without an ORM (Object Relational Manager) or similar features, and as such, has a compact and simple-to-extend core. Flask is based on the Werkzeg WSGI toolkit and the Jinja2 template engine. The Web Server Gateway Interface (Web Server Gateway Interface, WSGI) has been used as a standard for Python web application development.
The template engine and url routing are only two of its many fascinating features.

Werkzeug(toolkit) implements:
- requests
- response objects
- utility functions
- enables a web frame to be built on it

jinja2:
- A popular template engine for Python
- Allows to pass Python variables into HTML templates
`<h1>Hello {{ username }}</h1>`

# Why is Flask a good web framework choice?
- it is very pythonic as like as Django
- it is easy to get start
- it’s very explicit, which increases readability 

`from flask import Flask`

`app = Flask(__name__)`

    @app.route('/')
        def hello_world():
               return 'Hello World!
       
    if __name__ == '__main__':
    app.run()
