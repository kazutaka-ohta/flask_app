# cording: utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return 'Hallo World' 
    return render_template('index.html')

if __name__ == '__main__':
    app.run()



