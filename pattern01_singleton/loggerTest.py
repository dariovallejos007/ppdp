from logger import Loggers

logger = Loggers()._create_logger()
#print(logger.logs_file)
logger._info("test")