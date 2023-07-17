from flask import Flask
import requests

app = Flask(__name__)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler    # logging 핸들러 이름을 적어줌
    file_handler = RotatingFileHandler('sever_logging.log', maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.ERROR) # 어느 단계까지 적을것인지
    app.logger.addHandler(file_handler)
    
@app.errorhandler(404)      # 없는 페이지를 요청했을 때의 에러
def page_not_found(error):
    app.logger.error(error)
    return '<h1> 404 Error </h1>', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=False)