from config.logging_setting import *
logger = get_logger()
logger.debug("获取到了所有的规格与包装信息")
#
try:
    pass

except Exception as e:
    logger.error(e)