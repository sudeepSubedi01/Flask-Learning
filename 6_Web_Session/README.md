# Web Session
- A web session is a way to store data temporarily between different requests made by the same user on a web application. 
- This allows the server to remember information about a user's interactions across multiple pages or visits, creating a continuous, personalized experience.
- Information about the interaction between user and the application during each visit can be stored at:<br>
  1. Client side: in cookies
  2. Server side: in database 

# Cookies
- Cookies are small text files stored by a web browser on a user's device (computer, phone, etc.) when they visit a website.
- They allow websites to remember information about the user across multiple visits or interactions, providing a more personalized and consistent experience. 

# Working of Web Sessions
1. When a user visits a website with http request, a session is created on the server to track the user’s actions. The server generates a unique session ID and associates it with the session data(login info, shopping cart info) and sends to the client.
2. This session ID is stored on client side as a **cookie** in a text file.
3. For each subsequent request made by the user (like clicking a new page or submitting a form), the browser sends the session ID cookie back to the server.
4. The server uses this session ID to retrieve the corresponding session data, allowing it to recognize the user and persist information between requests.
5. This session is deleted from the browser when session ends either by Timeout, Manual Logout, Browser closing etc.

# HTTP is stateless
- It means that each http request made by client to a server is completely independent.
- The server doesnt retain any information about the client between different request.
- Every request is treated as if it were a new one, with no memory of any previous interactions.

# HTTP, Session and Cookie
The HTTP request I send to the server is stateless, which means that when I request something, my login credentials or session data aren’t inherently stored on the server between requests. To maintain continuity, the server sends a session ID, which the client stores in a cookie. This session ID allows the server to identify my session and link it to stored data without me needing to log in again.

# Types of sessions based on STORAGE LOCATION
1. Client-Side Session
    - In a client-side session, session data is stored directly on the client's device, typically within a cookie or local storage. 
    - Data is stored on the client's browser and in each request session data is sent to the server
    - Less secure because session data is exposed to the client.
    - By default, Flask uses client side session.
2. Server-Side Session
    - In a server-side session, session data is stored on the server, and only a reference (such as a session ID) is stored on the client. Here’s how it works:
    - Data is stored on server and the server creates and maintains a session object containing user-specific data.
    - The client only stores a session ID and is sent with each request.

# Types of sessions based on DURATION
1. Persistent Sessions
   - These sessions remain active for a very long period of time.
   - Ends only when user manually terminates the session.
2. Non-Persistent Sessions
   - These sessions last for a very short period, probably a single application visit.
   - Session ends when application/browser is closed

# Types of sessions based on SECURITY MECHANISM
1. Authenticated Sessions
   - Sessions are created only after the user has been authenticated (via login credentials)
2. Anonymous Sessions
   - Sessions are created even if the user hasn't been authenticated
   - Useful for maintaining state information without authentication (as a Guest)
   - Eg. browsing online retail stores

# How to enhance security and integrity of session data being stored?
1. Session ID:
   - The session ID should be long and randomly generated
   - The session ID should be changed periodically during a session
   - The session ID shouldn't be exposed as part of any URL

2. Secure Cookies
   - Set the flag **HttpOnly** and **Secure** and the attribute **SameSite** while setting cookies over HTTP
   - **HttpOnly** prevents client-side scripts (JavaScript) from accessing browser cookies, thus preventing XSS (cross-site scripting) attacks
   - **Secure** ensures that cookies are sent over the HTTPS domain, preventing interception over unsecured connections 
   - **SameSite** helps prevent chances of CSRF attacks
   - **Set-Cookie: sessionId=abc123; HttpOnly; Secure; SameSite=Strict**

3. Session Timeout
   - Ending sessions after a predefined period of inactivity
   - Terminating sessions after a fixed duration, regardless of activity
   - Helps reduce the time window available for attackers

4. Logging & Monitoring
   - Maintain logs of session creation, access, termination & various events to detect any unusual activity
   - Implement real-time monitoring systems to analyse logs and detect anomalies as they occur
   - Use automated tools to generate alerts for suspicious activities, enabling prompt investigation and response

5. Additional Measures
   - Implement MFA (multi-factor authentication) for security of sessions
   - Prompt users to confirm any and all critical actions within a session
   - Notify users before session timeout due to inactivity, if they want to extend a session. This can improve user experience while maintaining security.

# How is client side sessions executed in the code?
1. When the user logs in and `validate_on_submit()` returns `True`, the username entered by the user in the login form is stored in Flask’s `session` object under the key `user_name`. This session data is stored on the client side as a cookie.
   
2. Before rendering the about and contact pages, it checks if the session is active by verifying the presence of `user_name` in `session`. If `user_name` is not in `session`, it assumes the user is not logged in.

3. If the session doesn’t exist, the user is redirected to the login page. The current URL is captured by `next=request.url` and passed as a parameter to the login page, so the user can be redirected back to their original page after a successful login.

4. Once the session is successfully created (by setting `session['user_name']`), the user is redirected to their originally requested page (specified by `next_url`) or to the home page if no `next` URL is provided.

5. Each time the user visits a page requiring login (like about or contact), the application checks if the session exists by confirming that `user_name` is in `session`.

6. By default, the session cookie will be deleted when the browser is closed, unless configured otherwise (e.g., by setting `PERMANENT_SESSION_LIFETIME` in Flask’s configuration).

# How to view cookie in browser?
1. Create a session first
2. Inspect -> Application -> Cookie
3. All created sessions are listed. The cookies are in base64 format.


# How is client side sessions executed in the code?
1. Server side session is implemented using Flask's extension `flask_session` with the configuration pip install Flask-Session `SESSION_TYPE = 'filesystem'`.

2. Import flask_session package and initialize it by `Session(app)`.

3. The configuration `app.config['SESSION_TYPE'] = 'filesystem'` specifies that session data will be saved to the server’s filesystem rather than as client-side cookies. This is useful for storing more sensitive data securely on the server.

4. When the user successfully logs in, their username is saved to `session['user_name']`. Unlike client-side sessions, this data is stored on the server (e.g., in a temporary file on the server’s filesystem) and not exposed directly to the client.


