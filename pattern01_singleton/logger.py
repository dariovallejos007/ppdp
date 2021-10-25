import os
import inspect
import datetime


class Loggers():
    """
    """
    def __init__(self) -> None:
        """
        """
        self.calling_file      =  inspect.stack()[-1][1] #see this: https://stackoverflow.com/a/6628348

    def _create_logger(self):
        """
        """
        return Loggers._Logger(self)

    class _Logger(object):
        """
        """
        def __init__(self, logger) -> None:
            self.logger            =  logger
            self.calling_file      =  self.logger.calling_file
            self.calling_from      =  os.path.dirname(self.calling_file)
            self.calling_filename  =  os.path.basename(self.calling_file)
            self.logs_file         =  os.path.join(self.calling_from, f"({self.calling_filename})"+".log")
        
        def _write_log(self, level, message):
            """
            """
            with open(self.logs_file, "a") as f:
                utcIsoTime = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
                f.write(f"{self.calling_file}, {utcIsoTime} <<{level}: {message}>>#####\n")
        
        def _critical(self, message):
            self._write_log("CRITICAL", message)

        def _error(self, message):
            self._write_log("ERROR", message)

        def _warning(self, message):
            self._write_log("WARNING", message)

        def _info(self, message):
            self._write_log("INFO", message)
        
        def _debug(self, message):
            self._write_log("DEBUG", message)