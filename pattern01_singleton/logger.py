import os
import inspect
import datetime


class Loggers():
    """
    Logger class that creates *.logs file for any python file from which this is called
    """
    def __init__(self) -> None:
        """
        init variable self.calling_file is automatically created whenever this Class is called
        self.calling_file   :  full OS path of the python file from which this Class is called
        """
        self.calling_file  =  inspect.stack()[-1][1] #see this: https://stackoverflow.com/a/6628348

    def _create_logger(self):
        """
        """
        return Loggers._Logger(self)

    class _Logger(object):
        """
        inner Class _Logger

        ATTRIBUTES:
        self.calling_file      :  same as outer Class Logger.calling_file
        self.calling_from      :  full OS path of the folder containing the python file calling this Class
        self.calling_filename  :  file name of the python file calling this Class
        self.logs_file         :  name of the logs file to be created

        METHODS:
        self._write_log  :  writes on the log file. to be used by the other log methods
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