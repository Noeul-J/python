from flask import Flask, jsonify, request, render_template
app = Flask(__name__, static_url_path='/static')


@app.route('/login')
def login():
    email = request.args.get('email_address')
    passwd = request.args.get('passwd')
    
    print(email, passwd)

    if email == 'dave@gmail.com':
        return_data = {'auth': 'success'}
    else:
        return_data = {'auth': 'failed'}
    return jsonify(return_data)


@app.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('login_rawtest.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
