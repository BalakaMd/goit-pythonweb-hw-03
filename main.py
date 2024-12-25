import urllib
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime
import json
import os
from jinja2 import Environment, FileSystemLoader

# Налаштування Jinja2
env = Environment(loader=FileSystemLoader('.'))

# Порт для роботи сервера
PORT = 3000

file_path = 'storage/data.json'

class HttpHandler(BaseHTTPRequestHandler):
    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def send_static_file(self, filename, content_type):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
        with open(filename, 'rb') as file:
            self.wfile.write(file.read())

    def send_rendered_template(self, template_name, context, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        template = env.get_template(template_name)
        html = template.render(**context)
        self.wfile.write(html.encode())

    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        if pr_url.path == '/':
            self.send_html_file('index.html')
        elif pr_url.path == '/message':
            self.send_html_file('message.html')
        elif pr_url.path == '/style.css':
            self.send_static_file('style.css', 'text/css')
        elif self.path == '/logo.png':
            self.send_static_file('logo.png', 'image/png')
        elif self.path == '/read':
            with open('storage/data.json', 'r') as file:
                data = json.load(file)
            self.send_rendered_template('read_template.html', {'messages': data})
        else:
            self.send_html_file('error.html', 404)

    def do_POST(self):
        if self.path == '/message':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed_data = parse_qs(post_data)

            username = parsed_data.get('username', [''])[0]
            message = parsed_data.get('message', [''])[0]

            timestamp = str(datetime.now())

            data = {
                timestamp: {
                    "username": username,
                    "message": message
                }
            }

            if not os.path.exists('storage'):
                os.makedirs('storage')

            if os.path.exists('storage/data.json'):
                with open('storage/data.json', 'r') as file:
                    existing_data = json.load(file)
                existing_data.update(data)
                data = existing_data

            with open('storage/data.json', 'w') as file:
                json.dump(data, file, indent=2)

            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()


def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ('', PORT)
    http = server_class(server_address, handler_class)
    print(f'Starting server on port {PORT}...')
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == '__main__':
    run()
