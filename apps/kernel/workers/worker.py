from __future__ import print_function
import os
import time

from apps.system.lib import logger
from apps.kernel.infrastructure.messaging import (
    common,
    network,
)
from apps.kernel.infrastructure import (
    sessions,
    task_manager,
)
from apps.kernel.infrastructure.messaging.task.payload.general import (
    addresses,
)
from apps.kernel.infrastructure.messaging.task.payload import (
    subscriber,
    connection,
    payment,
    dictionary,
)
from apps.kernel.infrastructure.messaging.task.payload.subscriber import (
    identifiers,
    operations,
)


class Worker:
    all_dictionaries = {
        '100': 'bunches',
        '103': 'switches',
        '104': 'gates',
        '105': 'call types',
        '106': 'supplement services',
        '107': 'pay types',
        '108': 'termination causes',
        '109': 'ip numbering plans',
        '110': 'phone numbering plans',
        '111': 'document types',
        '112': 'telcos',
        '113': 'ip data points',
        '114': 'special numbers',
        '115': 'bunches map',
        '132': 'ss7 signal point codes'
    }

    def __init__(self, host: str, ports: [],
                 inactivity_timeout_=60,
                 max_data_length_=1000, data_packet_window_size_=5,
                 data_load_timeout_=60, request_response_timeout_=60,
                 data_packet_response_timeout_=60
                 ):
        self._host = host
        self._ports = ports
        self.lg = logger.instance()
        self.supported_dictionaries = {}

        self.channel_parameters = sessions.ChannelParameters(
            inactivity_timeout_,
            max_data_length_,
            data_packet_window_size_,
            data_load_timeout_,
            request_response_timeout_,
            data_packet_response_timeout_
        )

    def run(self):
        print(self._host, self._ports)
        logger.initialize(os.path.join('data', 'logs', 'app.log'), 'debug')

        report_limit = 1000

        ports = list(map(lambda x: int(x), self._ports))
        session = sessions.Session(self._host, ports)

        session.initialize(self.channel_parameters)

        tm = task_manager.TaskManager(session)
        # find_range = common.FindRange('200101102957Z', '210114102957Z')
        find_range = common.FindRange(None, None)

        # try:
        # tm.create_tasks([
        # task_manager.TaskCreationRequest(
        #     'Any {0} NAT connections'.format(report_limit), None, find_range,
        #     report_limit, connection.ValidateDataTask([
        #         connection.RequestedAddressTranslation(
        #             connection.RequestedAddressTranslation.public_ip, 2
        #         )])),
        # task_manager.TaskCreationRequest(
        #     f'Any {report_limit} HTTP connections',
        #     None,
        #     find_range,
        #     report_limit,
        #     connection.ValidateDataTask([
        #         connection.RequestedResource(connection.RequestedResource.url, '**')
        #     ])),

        # task_manager.TaskCreationRequest(
        #     'looking for subscribers by any login',
        #     None,
        #     find_range,
        #     None,
        #     subscriber.ValidateSubscribersTask([
        #         identifiers.RequestedDataNetworkIdentifier('login', '**'),
        #         operations.OR,
        #         identifiers.RequestedPstnIdentifier('**')
        #     ]))
        # ])

        #     print(tm.tasks)
        #     info = tm.wait_for_tasks_completion(timeout_=600)
        #     report_records = info[0].report_records
        #     logging_step = int(report_records * 0.05)
        #
        #     tm.load_tasks(info)
        #     loaded_records = 0
        #     left_records_to_log = logging_step
        #     blocks = []
        #     while loaded_records < info[0].report_records:
        #         print(info)
        #         block = tm.wait_for_tasks_report(timeout=60)
        #         loaded_records += len(block.records)
        #         tm.send_report_block_confirmation(2, block.message_id)
        #         left_records_to_log -= len(block.records)
        #         print(block)
        #         blocks.append(block)
        #         if left_records_to_log <= 0:
        #             print(f'{loaded_records} of {report_records} records have been loaded')
        #             left_records_to_log = logging_step
        #
        #     print(f'ALL BLOCKS: {blocks}')
        #
        #     # with open('data/output/report.txt', 'r') as fout:
        #     #     fout.writelines(blocks)
        #
        #     # i = 0
        #     # while True:
        #     #     print(f'{self._host}) Hi mir: {i}')
        #     #     if i > 20:
        #     #         break
        #     #
        #     #     i += 1
        #     #     time.sleep(1)
        #
        # except Exception as e:
        #     print(f'OU NOU! {e}')
        # finally:
        #     tm.drop_tasks()

        try:

            tasks_info = tm.wait_for_tasks_completion(timeout_=301)
            total_records = 0
            loaded_records = 0
            loading_statistics = {}
            for info in sorted(tasks_info, key=(lambda task: task.request_id)):
                report_records = info.report_records if info.report_records is not None else 0
                total_records += report_records
                loading_statistics[info.task_id] = [
                    info.name, 0, report_records, False]
                print(
                    'The task #{0} "{1}" created '.format(
                        info.task_id, info.name
                    ).ljust(90, '.') + ' {0} records'.format(report_records)
                )

            tm.load_tasks()
            while loaded_records < total_records:
                block = tm.wait_for_tasks_report(timeout=60)

                for r in block.records:
                    print('\n\n')
                    print(dir(r))
                    print(r)

                loaded_records += len(block.records)
                loading_statistics[block.task_id][1] += len(block.records)
                tm.send_report_block_confirmation(2, block.message_id)
                if loading_statistics[block.task_id][1] >= loading_statistics[block.task_id][2]:
                    if loading_statistics[block.task_id][3] or loading_statistics[block.task_id][1] > \
                            loading_statistics[block.task_id][2]:
                        print(
                            'Too many report records returned for the task #{0} "{1}"'.format(block.task_id,
                                                                                              loading_statistics[
                                                                                                  block.task_id][0]))
                    else:
                        loading_statistics[block.task_id][3] = True
                        print(
                            'Report records of the task #{0} "{1}" have been completely loaded'.format(block.task_id,
                                                                                                       loading_statistics[
                                                                                                           block.task_id][
                                                                                                           0]))
        except Exception as e:
            print(e)

        finally:
            tm.drop_tasks()
        session.finalize()
        print(f'{self._host}) Goodbye:')
