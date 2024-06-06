from flask import Flask, render_template
import platform

app = Flask(__name__)

@app.route('/')
def get_node_name():
    node_name = platform.node()
    return render_template('index.html', node_name=node_name)

if __name__ == '__main__': 
    app.run(debug=True)
