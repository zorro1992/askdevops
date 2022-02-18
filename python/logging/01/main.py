import logging

#logging.basicConfig(filename="log.txt",level=logging.WARNING,filemode='a')
#logging.basicConfig()
logging.basicConfig(filename="log.txt",level=logging.DEBUG,filemode='a')
print('Logging example 01')
logging.critical('This is the ciritcal')
logging.error('This is the error')
logging.warning('This is the warning')
logging.info('This is the info')
logging.debug('This is the debug')
