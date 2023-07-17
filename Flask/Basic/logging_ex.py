import logging

# 어느 로그까지 남길 것인지를 level로 설정 가능
# DEBUG > INFO > WARNING > ERROR > Critical
logging.basicConfig(filename='test.log', level=logging.ERROR)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')