# Dynamic URL
A URL that if generated automatically based on certain user inputs

# URL Redirection
The process in which users visit a particular URL and they are navigated to a different URL. <br>
This is required because:
- If a page is deleted, users need to be redirected to another URL 
- If maintenance of a web page is going on, users can be redirected
- If website gets renamed, users can be redirected to appropriate URL

# Common Response Codes
3xx - Redirection
- 301 : Moved Permanently
- 302 : Redirected Temporarily
- 303 : Redirected Temporarily
- 307 : Redirected Temporarily
- 307 : Redirected Permanently

# redirect() function
- redirect(url to a website)
- redirect(endpoint)
- redirect(url_for(function name))

# url_for()
- generates url for a given function name
- using url_for() instead of hardcoding URLs is recommended, as it allows for flexibility if the route changes later.
- url_for(function_name, parameters)