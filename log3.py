import logging

logging.basicConfig(filename="D://pythonproject//log//test.log",
                    format='%(asctime)s:%(levelname)s: %(message)s',
                    level=logging.ERROR
                    )

logging.debug("debug")
logging.info("info")
logging.warning(("warning"))
logging.error("error")
logging.critical("critical")
