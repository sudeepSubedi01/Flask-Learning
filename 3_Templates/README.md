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
- feature that allows to create a base template and then extend it across multiple pages
- Blocks are placeholders in the base template that child templates can override or customize. Blocks are defined with {% block block_name %}...{% endblock %} in the base template.
- The {% extends 'base.html' %} tag is used in a child template to inherit the base template. By doing this, the child template can add or replace content in the predefined blocks from the base template.

# anchor tag
- whenever one clicks on the link, redirect to the corresponding page using url_for()