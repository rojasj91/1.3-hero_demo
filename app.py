import os
from flask import Flask

from flask import request

app = Flask(__name__)

@app.route("/")
def index():

    input_value = request.args.get('search-term')
    print(input_value)

    if not input_value:
        input_value = ""

    index_file = open('index.html', 'r')

    my_html = index_file.read()
    print(input_value)
    my_html = my_html.replace("{{input_value}}", input_value)

    index_file.close()

    return  my_html