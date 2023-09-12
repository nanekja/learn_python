import logging

################################  Example-1 ##########################################################

logging.basicConfig(level=logging.INFO)   # here we are setting the logging level

logging.debug('This message will be ignored')  # because the debug statement is beneath the threshold of info, it doesn't get printed
logging.info('This should be logged')
logging.warning('And this, too')

# The default, if we don't set a level at all is warning

################################  Example-2 ##########################################################

logging.basicConfig(level=logging.INFO, filename='./oops/6_efficiency_testing/example.log', filemode='w')   # here we are setting the logging level and sending to a file

logging.debug('This message will be ignored')  # because the debug statement is beneath the threshold of info, it doesn't get printed
logging.info('This should be logged')
logging.warning('And this, too')

################################  Example-3 ##########################################################

logging.basicConfig(format='%(asctime)s %(levelname)s:%(messages)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)   # here we are setting the logging level and sending to a file

logging.debug('This message will be ignored')  # because the debug statement is beneath the threshold of info, it doesn't get printed
logging.info('This should be logged')
logging.warning('And this, too')