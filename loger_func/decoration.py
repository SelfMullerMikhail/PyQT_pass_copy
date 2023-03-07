import sys, os, logging, logging.handlers
import datetime

sys.path.append(os.path.join('..', os.getcwd()))
from CONFUGURATION import ENCODING, LOGGING_LEVEL

def loggin_obj(name_function,  *args):
    SERVER_FORMATER = logging.Formatter(f"%(asctime)5s %(levelname)s %(message)s\naction: {name_function}.\nargs:{args}\n")
    PATH = f"{os.getcwd()}\\loger\\database_logs\\db_{datetime.date.today()}.log"

    STREAM_HANDLER = logging.StreamHandler(sys.stderr)
    STREAM_HANDLER.setFormatter(SERVER_FORMATER)
    LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding=ENCODING, interval=1, when="D")
    LOG_FILE.setFormatter(SERVER_FORMATER)

    CLIENT_LOGGER = logging.getLogger("func_checker")
    CLIENT_LOGGER.addHandler(LOG_FILE)
    CLIENT_LOGGER.setLevel(LOGGING_LEVEL)
    return CLIENT_LOGGER

def func_loger(func):    
    def decorate_finction(*args):
        name_function = func.__name__
        loger = loggin_obj(name_function, *args)
        try:
            loger.debug("")
            return func(*args) 
        except Exception as e:
            loger.error(str({e}))
    return decorate_finction




# Testing
if __name__ == "__main__":
    text = loggin_obj("ff")
    CLIENT_LOGGER = logging.getLogger("func_checker")
    CLIENT_LOGGER.critical("Critical Error")
    CLIENT_LOGGER.error("Error")
    CLIENT_LOGGER.debug("Testing information")
    CLIENT_LOGGER.info("Inforaminoly message")

