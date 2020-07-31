from ckaccess import app
from flask import request
import requests

@app.route('/')
def test_service():
    service_url = request.args.get('service_url', '')
    try:
        r = requests.get(service_url)
        return 'Testing Service for %s!  for status %d ' % (
            service_url, r.status_code)
    except:
         return 'Could not reach Service %s!' % service_url
