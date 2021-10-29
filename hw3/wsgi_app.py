import json
import urllib.parse
from datetime import datetime


def app(environ, start_response):
    """Application object"""
    time = datetime.now().isoformat(sep='#')
    # scheme[0]://netloc[1]/path[2];parameters[3]?query[4]#fragment[5]
    url = urllib.parse.urlunparse(['http', environ['SERVER_NAME'] + ':' + environ['SERVER_PORT'],
                                   environ['PATH_INFO'], '', environ['QUERY_STRING'], ''])
    byte_json_data = str.encode(json.dumps({'time': time, 'url': url}))

    status = '200 OK'
    response_headers = [
        ('Content-type', 'application/json'),
        ('Content-Length', str(len(byte_json_data)))
    ]
    start_response(status, response_headers)
    return iter([byte_json_data])
