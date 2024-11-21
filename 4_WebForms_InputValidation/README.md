# CSRF Attack
- Cross-Site Request Forgery attack
- a type of web security vulnerability where a malicious website tricks a user's browser into making unwanted requests to another site where the user is authenticated.
- Such attacks are common when web applications take inputs from users

# WTForms
- wtforms for flask installation : `pip install -U Flask-WTF`
- Python library that simplifies working with web forms by providing a robust structure for defining, rendering, and validating form fields.
- used in Flask apps when combined with Flask-WTF, an extension that integrates WTForms into Flask, adding CSRF protection
- each form in WTForms is defined as a python class with that represent the input elements

# Flask-WTF, a module
- Flask extension that integrates WTForms with Flask, providing useful tools for handling web forms including CSRF protection
- Flask-WTF automatically generates a CSRF token for each form, preventing CSRF attacks by ensuring that form submissions come from trusted users and not external sites.
- in Flask, this is a module: `flask_wtf `(contains FlaskForm class)

# wtforms
- core module within `flask_wtf` that provides classes like StringField, PasswordField and validators necessary for creating and validating web forms

# FlaskForm
- class inside `flask_wtf` module
- base class for all forms in Flask-WTF
- we inherit from FlaskForm to define any custom forms
- validators: constraints to form inputs

# To use CSFR in Flask app
1. adding a SECRET_KEY to the app's configuration
   - in app.py: `app.config['SECRET_KEY'] = 'mysecretkey'`
2. In view function, initialize the form and handle form validation.
   - in app.py: 
   ```py
    if form.validate_on_submit():
        # Process the login here
        return redirect(url_for('home'))
   ```
3. Render the Form in the Template; Adding CSFR token for security in form
- use this in the template where the form is inside `<form> tag`

# Login Form, a custom class
- inherit from FlaskForm class and define fields like StringField, PasswordField

# methods=['GET','POST']
- specifies the HTTP methods allowed for the route

# What validate_on_submit() Does
1. Checks for a POST Request:
   - `validate_on_submit()` first checks if the form was submitted with a POST request.
   - This means it runs only if a user has actually submitted the form, avoiding unnecessary validation if a user just loaded the page.
2. Validates the Form:
   - After confirming the POST request, `validate_on_submit()` calls `form.validate()`, which runs all defined validators on each form field.
   - Validators might check if a field has input (DataRequired), if the input matches a certain format (Email), or other constraints as specified.
3. Returns True if Validation Passes:
   - If all validators pass and the method is POST, `validate_on_submit()` returns True, allowing the code following this check to proceed (typically processing the form data).
   - If validation fails, `validate_on_submit()` returns False, and error messages can be displayed on the form (Flask-WTF automatically associates error messages with the corresponding fields).

# Flask-Validator
- `pip install flask_validator`

# Flow of Execution of Program
1. When user visits `/signup` route, GET request is invoked and the view function inside `/signup` route (i.e. `def signup()`) now handles the request.
2. `s_form` is the instance of the `class SignUpForm()` which is a form created using Flask-WTF
3. `s_form.validate_on_submit()` returns false since the request is GET.
4. Template signup.html is rendered and is a empty form ready for user to enter data.
5. After filling the form (correctly or incorrectly) user clicks submit button, then a POST request is triggered on the same URL `/signup`.
6. `s_form = SignupForm()` creates a new instance of SignupForm that now contains the data submitted by the user.
7. `s_form.validate_on_submit()` checks: request method is POST? & calls `validate()` method which runs all the validators in the form. So if request method is POST and all the validations pass, it returns True. It then runs the if statements.
8. If the validation is false, the error message is displayed and templete is rendered.

# form.[label_name].errors
- Flask-WTF attribute that contains any validation error messages associated with the label_name field of the form
- all the validation errors are stored in attribute errors





RuntimeError: A secret key is required to use CSRF.