import logging

# to output logging modules:
# print(dir(logging))

# Create and configure logger:
# level specifies the level of messages that can get output
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = 
r'C:\Users\ilarbi\personal\python3-beginner\learn2.log',
level = logging.DEBUG,
# level = logging.ERROR,
format = LOG_FORMAT,
filemode = 'w')
logger = logging.getLogger()

# Test message of all levels:
logger.debug('This is a hermless debug message.')
logger.info("This is some useful info.")
logger.warning("This is your final warning. You know I give you life.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")
