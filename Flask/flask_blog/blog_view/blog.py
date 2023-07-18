from flask import Flask, Blueprint, request, render_template

blog_abtest= Blueprint('blog', __name__)

@blog_abtest.route('/set_email', methods=['GET'])
def set_email():
    print(request.args.get['email'])


@blog_abtest.route('/test_blog')
def test_blog():
    return render_template('blog_A.html')

@blog_abtest.route('/')
def home():
    return "<h1>Home Page</h1>"