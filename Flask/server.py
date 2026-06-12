from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home_page():

    return "Hello World\n", 201
    # return render_template('index.html')
    # if request.method == 'GET':
    #     return "you made a get request\n"
    # elif request.method == 'POST':
    #     return "you made a post request\n"
    # else:
    #     return "you will never see this meesage"


@app.route('/about')
def about():
    return "<h1>about page</h1>"


@app.route('/about/<username>')
def about_page(username):
    return f"<h1>About Page for the user {username}</h1>"


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)


@app.route('/handle_url_params')
def handle_params():
    # return str(request.args)
    # return f"<h1>Hello {request.args.get('name')}</h1>"
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f"<h1>{greeting} {name}</h1>"
    else:
        return "some parameters are missing"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
