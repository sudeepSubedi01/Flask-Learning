# Cookie
- HTTP Cookie
- a small piece of data that is stored within the browser at the client side
- The main purpose of cookies is to store user preferences and session information, enabling a more personalized experience and maintaining user-specific data across multiple requests.
- Browsers use specific databases to store cookies.
- For example, Chrome and Firefox both utilize an SQLite database to store and manage cookies effectively.

# Working
- When user visits a web application and interacts with it, a HTTP request is sent to the server.
- The server generates an appropriate response message and sends it back to the application (browser), along with the session ID generated as well as a cookie header. This is done by the Set-Cookie header in the 'headers' part of the response message: 
`Set-Cookie:sessionId=abc123; Expires=Wed, 21 Oct 2023 07:28:00 GMT; Secure; F'`
- Once a cookie is stored, your browser automatically includes it in future requests to the same domain. This way, the server can recognize you and provide a consistent experience based on previously stored data.
- Cookies can either be session cookies, which expire once the browser is closed, or persistent cookies with a set expiration date. When the expiration date passes, the browser deletes the cookie automatically.
- The server can update cookie values by sending new cookies with modified data.

# Types of Cookie
1. First Party Cookies
   - These are cookies created and set by the website you are currently visiting.
   - Only accessible to the website that set the cookies. So more secure and protected.
   - Used for: storing user preferences, maintaining user session.

2. Third Party Cookies
   - These are cookies set by a domain other than the one you are currently visiting. Typically, they come from embedded elements such as ads, videos, or social media buttons.
   - Associtated with security concerns as it exposes users' browsing data to external parties.
   - Used for: 
      - Tracking user behavior across multiple websites.
      - Serving targeted advertisements based on browsing history.
      - Tailoring social media feeds by tracking user activity
      - Generating user profiles based on data collected about a user's activities across different websites

# What happens when we select 'Accept All Cookies' ?
- A user giving consent to store and use first-party and third-party cookies.
- Allows third-party companies to collect browsing data and activity across multiple websites. This helps with targeted ad generation, building user profiles.
- Higher risk of data leakage if the third-party companies are compromised.

# Measures to protect data stored in Cookies
1. Cookie Attributes
   - Use attributes and flags like `HttpOnly` and `SameSite`
   - Helps avoid CSRF and XSS attacks
2. Cookie Posioning
   - It means an attacker modifying the contents of cookies to gain unauthorized access to data
   - Encrypt cookie data using hashes
   - Avoid storing critical and sensitive information in cookies
3. Man-in-the-Middle Attacks
   - Attackers can intercept cookies and manipulate the communication between client and server
   - Ensure to use `Secure` attribute and https channels for communications
4. Consent
   - Read all terms and conditions before accepting all cookies
   - Minimize the use of third party cookies unless absolutely necessary
5. Similar to sessions
   - Cookies are a part of sessions
   - Cookies are generated with a session
   - Similar security considerations will apply 

# Setting and Getting Code Explaination
1. `make_response('welcome to set cookie')`: Creates an HTTP response object with the content "welcome to set cookie".
2. `response.set_cookie('name1', 'value1')`: Sets a cookie named name1 with a value of value1.
3. The `set_cookie` method attaches cookies to the response. When this response is sent to the client (browser), the cookies are stored on the client-side.
4. When the client visits `/get_cookie`, the browser automatically sends the stored cookies (if any) back to the server as part of the HTTP request headers.
5. `request.cookies.get('name1')`: Accesses the cookies sent in the request, Retrieves the value of the cookie named `name1`, If `name1` is not found, it returns `None` by default.