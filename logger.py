import logging
from config import Config

_level = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}


class LoggerConfig(Config):
    def __init__(self, config: dict):
        """
        Generates a LoggerConfig with the correct attributes

        :param config: the loaded configuration of this object
        """
        self.name: str = None
        self.logger_level: str = None
        self.format: str = None
        self.use_file_handler: bool = None
        self.log_path: str = None
        self.log_file_level: str = None
        self.use_stream_handler: bool = None
        self.sep: str = None
        self.end: str = None

        super().__init__(config)


class Log:
    def __init__(self, logger: logging.Logger, sep, end):
        self.logger = logger
        self.sep = sep
        self.end = end

    def _gen_str(self, args, sep: str = None, end: str = None):
        if sep is None:
            sep = self.sep

        if end is None:
            end = self.end
        return sep.join(map(str, args)) + end

    def debug(self, *args, sep: str = None, end: str = None):
        self.logger.debug(self._gen_str(args, sep, end))

    def info(self, *args, sep: str = None, end: str = None):
        self.logger.info(self._gen_str(args, sep, end))

    def warning(self, *args, sep: str = None, end: str = None):
        self.logger.warning(self._gen_str(args, sep, end))

    def error(self, *args, sep: str = None, end: str = None):
        self.logger.error(self._gen_str(args, sep, end))

    def critical(self, *args, sep: str = None, end: str = None):
        self.logger.critical(self._gen_str(args, sep, end))


def create_logger(config: LoggerConfig):
    formatter = logging.Formatter(config.format)

    logger = logging.getLogger(config.name)
    logger.setLevel(_level.get(config.logger_level, logging.DEBUG))

    if config.use_file_handler:
        file_handler = logging.FileHandler(config.log_path)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(config.log_file_level)

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if config.use_stream_handler:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(config.logger_level)

        logger.addHandler(stream_handler)

    return Log(logger, config.sep, config.end)