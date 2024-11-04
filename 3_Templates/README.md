# Templates
- Default folder name is templates templates

# render_template()
- used to render HTML templates for web application
- takes the name of an HTML file (like "index.html") as a parameter and returns it as the response when a route is accessed.

# Jinja
- templating engine used in Flask to dynamically generate HTML pages by embedding Python like expressions in HTML files
- Jinja allows to insert values from Python into HTML using double curly braces ({{ }})
- render_template('about.html', title = 'about'). Here title is called Template Context

# Template Inheritance
