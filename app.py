import os
import random
from flask import Flask

from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    #created a class
    left_class = "left"
    right_class = "right"

 #created a random.randit statement with import random, to switch between 0,1
    if random.randint(0,1):
        left_class = "right"
        right_class = "left"

    index_file = open('1.3-demo.html', 'r')



    my_html = index_file.read()


#'left_class is pulling from the previous var that I created on line 11 & 'right class from line 12
    my_html = my_html.replace("{{left}}", left_class)
    my_html = my_html.replace("{{right}}", right_class)


    index_file.close()

    return  my_html