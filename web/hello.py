def application(environ, start_response):
    data = '\n'.join(environ['QUERY_STRING'].split('&')).encode ('utf-8')
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])