from . import logger
import sys, time


rslt_passed = 'passed'
rslt_suspect = 'suspect'
rslt_failed = 'failed'
tagn_auto = 'auto'


class ScenarioDescriptor:

    def __init__(self, name_, tags_, info_method_, run_method_):
        self.name = name_
        self.tags = tags_
        self.info_method = info_method_
        self.run_method = run_method_


class Processor:

    def __init__(self, available_scenarios_, tags_, names_, settings_):
        self.lg = logger.instance()
        self.run_results = []
        self.available_scenarios = available_scenarios_
        self.tags = tags_ if tags_ is not None else []
        self.names = names_ if names_ is not None else []
        self.settings = settings_

    def chose_scenarios(self, tags_, names_, enable_non_auto_when_empty_=False):
        chosen = []
        if len(tags_) == 0 and len(names_) == 0:
            for item in self.available_scenarios:
                if enable_non_auto_when_empty_ or tagn_auto in item.tags:
                    chosen.append(item)

            return chosen
        else:
            for item in self.available_scenarios:
                if item.name in names_ or len(set(tags_).intersection(item.tags)) != 0:
                    chosen.append(item)

            return chosen

    def list(self):
        for item in self.chose_scenarios(self.tags, self.names, True):
            print('{0:64} tags: {1}'.format(item.name, ', '.join(item.tags)))

    def info(self):
        for item in self.chose_scenarios(self.tags, self.names, True):
            print('{0}:'.format(item.name))
            print('{0}'.format('-' * (len(item.name) + 1)))
            if item.info_method is None:
                print('    no info provided')
            else:
                info = item.info_method()
                for line in info.splitlines():
                    print('    {0}'.format(line))
            print('')

    def run(self):
        emulation_id = int(time.time())
        self.lg.info(
            '{0} {1:08x} Starting  {0}'.format('=' * 35, emulation_id)
        )
        try:
            try:
                for item in self.chose_scenarios(self.tags, self.names):
                    self.run_scenario(item.name, item.run_method)

                self.lg.info('Report:')
                for result in self.run_results:
                    self.lg.info('    {0} {1}'.format(
                        (str(result[0]) + ' ').ljust(85 - len(result[1]), '.'),
                        result[1])
                    )

            except Exception as e:
                self.lg.critical(
                    'Unexpected error occurred: {0}'.format(str(e))
                )
                self.lg.log_back_trace(
                    logger.llvl_critical, sys.exc_info()[2]
                )

        finally:
            self.lg.info('{0} {1:08x} Finishing {0}'.format('=' * 35, emulation_id))

        file_names = self.lg.get_file_names()
        self.lg.info(
            "Use to cut out log records: sed -n '/{0:08x} Starting/,/{0:08x} Finishing/p' {1}".format(
                emulation_id, file_names[0] if len(file_names) > 0 else 'LOG_FILE_NAME'
            )
        )

    def run_scenario(self, name_, function_):
        self.lg.info(f'>>>>>>> Starting the "{name_}" scenario...')
        try:
            self.run_results.append((name_, function_(self.settings)))
        except Exception as e:
            self.run_results.append((name_, rslt_failed))
            self.lg.error(f'Unexpected error occurred while execution the "{name_}" scenario: {str(e)}')
            self.lg.log_back_trace(logger.llvl_critical, sys.exc_info()[2])

        self.lg.info(f'<<<<<<< The "{name_}" scenario has been finished')
