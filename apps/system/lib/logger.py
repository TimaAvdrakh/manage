import sys, logging, logging.handlers, traceback, os, errno

llvl_critical = logging.CRITICAL
llvl_error = logging.ERROR
llvl_warning = logging.WARNING
llvl_info = logging.INFO
llvl_diagnostic = logging.DEBUG + 5
llvl_debug = logging.DEBUG
llnm_critical = 'critical'
llnm_error = 'error'
llnm_warning = 'warning'
llnm_info = 'info'
llnm_diagnostic = 'diagnostic'
llnm_debug = 'debug'
level_name_to_level = {
    llnm_critical: llvl_critical,
    llnm_error: llvl_error,
    llnm_warning: llvl_warning,
    llnm_info: llvl_info,
    llnm_diagnostic: llvl_diagnostic,
    llnm_debug: llvl_debug
}


class Logger:

    def __init__(self, real_logger_):
        self.real_logger = real_logger_

    def set_level(self, level_):
        self.real_logger.setLevel(level_)

    def get_effective_level(self):
        return self.real_logger.getEffectiveLevel()

    def is_enabled_for(self, level_):
        return self.real_logger.isEnabledFor(level_)

    def log(self, level_, msg_):
        for line in msg_.splitlines():
            self.real_logger.log(level_, line)

    def critical(self, msg_):
        self.log(llvl_critical, msg_)

    def error(self, msg_):
        self.log(llvl_error, msg_)

    def warning(self, msg_):
        self.log(llvl_warning, msg_)

    def info(self, msg_):
        self.log(llvl_info, msg_)

    def diagnostic(self, msg_):
        self.log(llvl_diagnostic, msg_)

    def debug(self, msg_):
        self.log(llvl_debug, msg_)

    def log_memory_dump(self, level_, header_, data_):
        self.log(level_, header_)
        char_counter = 0
        cortage_counter = 0
        hex_line = ''
        char_line = ''
        for char in data_:
            byte = char if isinstance(char, int) else ord(char)
            hex_line += '{0:02x}'.format(byte)
            char_line += chr(byte) if 32 <= byte <= 127 else '.'
            char_counter += 1
            if char_counter == 4:
                char_counter = 0
                hex_line += ' '
                cortage_counter += 1
                if cortage_counter == 8:
                    self.log(
                        level_, '    {0} | {1}'.format(hex_line, char_line)
                    )
                    cortage_counter = 0
                    hex_line = ''
                    char_line = ''

        if len(hex_line) != 0:
            self.log(
                level_, '    {0} | {1}'.format(hex_line.ljust(72), char_line)
            )

    def log_back_trace(self, level_, tb_):
        stack = traceback.extract_tb(tb_)
        self.log(level_, 'Backtrace:')
        for item in stack:
            self.log(
                level_, '  ... {0}:{1} in "{2}" at "{3}"'.format(
                    '/'.join(
                        item[0].split('/')[-2:]), item[1], item[2], item[3]
                )
            )

    def flush(self):
        for handler in self.real_logger.handlers:
            handler.flush()

    def get_file_descriptors(self):
        fds = []
        for handler in self.real_logger.handlers:
            if isinstance(handler, logging.StreamHandler):
                fds.append(handler.stream.fileno())

        return fds

    def get_file_names(self):
        names = []
        for handler in self.real_logger.handlers:
            if hasattr(handler, 'baseFilename'):
                names.append(handler.baseFilename)

        return names


logger_instance = Logger(None)


def initialize(log_file_, llnm_):
    global logger_instance
    logging.addLevelName(llvl_diagnostic, 'DIAGNOSTIC')
    logger = logging.getLogger('main')
    logger.setLevel(llvl_debug)
    ch = logging.StreamHandler()
    ch.setFormatter(
        logging.Formatter(
            '[%(levelname)-10s]: %(message)s', '%d.%m.%Y-%H:%M:%S'
        )
    )
    ch.setLevel(llvl_info)
    logger.addHandler(ch)
    if log_file_ is not None:
        full_log_file_name = log_file_
    else:
        appl_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        log_file_path = os.path.join('/var/log', appl_name)
        log_file_name = appl_name + '.log'
        full_log_file_name = os.path.join(log_file_path, log_file_name)
    # try:
    #     os.makedirs(log_file_path)
    # except OSError as e:
    #     if e.errno != errno.EEXIST or not os.path.isdir(log_file_path):
    #         raise

    fh = logging.handlers.TimedRotatingFileHandler(
        full_log_file_name, when='midnight'
    )
    fh.setFormatter(logging.Formatter(
        '%(asctime)s [%(levelname)-10s]: %(message)s', '%d.%m.%Y-%H:%M:%S')
    )
    fh.setLevel(level_name_to_level[llnm_])
    logger.addHandler(fh)
    logger_instance = Logger(logger)


def instance():
    return logger_instance
