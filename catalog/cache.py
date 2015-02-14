from django.core.cache import cache
import requests
import json


url = ''
# http://equallytrue.blogspot.com/2012/04/how-to-cache-outgoing-api-calls-in.html
def fetchJson(url):
    cached = cache.get(url)
    content = ""
    if not cached:
            r = requests.get(url)
            if(r.ok):
                cache.set(url, r.text)
                content = r.text
            else:
                # Write some proper error handling code here
                print "Error - status code: " + r.status_code  
    else:
        # Return the cached content
        content = cached
    return json.loads(content)

