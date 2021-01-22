from __future__ import print_function
import time
import threading

from apps.system.lib import (
    exceptions,
    basic,
)

from apps.kernel.infrastructure import sessions
from apps.kernel.infrastructure.messaging.task import (
    create_task,
    data_ready,
    data_load,
    data_interrupt,
    data_drop,
)
from apps.kernel.infrastructure.messaging.report import report
from apps.kernel.infrastructure.messaging.report.payload import (
    dictionary as dictionary_report,
    subscriber as subscriber_report,
    payment as payment_report,
    connection as connection_report,
    data_content as data_content_report,
)


class TaskExecutionStatus:
    data_not_ready = 0
    data_ready = 1
    data_not_found = 2
    error = 3
    names = {
        data_not_ready: 'data-no-ready',
        data_ready: 'data-ready',
        data_not_found: 'data-not-found',
        error: 'error'
    }

    def __init__(self, code=data_not_ready):
        self.code = code

    def __repr__(self):
        return TaskExecutionStatus.names.get(
            self.code, f'unknown({self.code})'
        )


class TaskCreationRequest(basic.PrintableObject):

    def __init__(self, name, telco_codes, range, report_limit, body):
        self.name = name
        self.telco_codes = telco_codes
        self.range = range
        self.report_limit = report_limit
        self.body = body

    def __dir__(self):
        return [
         'name', 'telco_codes', 'range', 'report_limit', 'body'
        ]


class TaskInfo(basic.PrintableObject):

    def __init__(self, request_id, name):
        self.request_id = request_id
        self.name = name
        self.task_id = None
        self.status = TaskExecutionStatus()
        self.error_description = None
        self.report_limit_exceeded = None
        self.report_records = None
        self.report_data_blocks = None

    def __dir__(self):
        return [
            'request_id', 'task_id', 'name', 'status', 'error_description',
            'report_limit_exceeded', 'report_records', 'report_data_blocks'
        ]


class TaskManager:

    def __init__(self, session: sessions.Session):
        self.session = session
        self.tasks = {}
        self.task_creation_info = []
        self.waiting_responses = 0
        self.reports = {}
        self.cv_incoming_message = threading.Condition()
        self.session.channel(1).set_user_message_handler(
            create_task.CreateTaskResponse, self.handle_create_task_response
        )
        self.session.channel(1).set_user_message_handler(
            data_ready.DataReadyResponse, self.handle_data_ready_response
        )
        self.session.channel(1).set_user_message_handler(
            data_load.DataLoadResponse, self.handle_data_load_response
        )
        self.session.channel(1).set_user_message_handler(
            data_interrupt.DataInterruptResponse,
            self.handle_data_interrupt_response
        )
        self.session.channel(1).set_user_message_handler(
            data_drop.DataDropResponse,
            self.handle_data_drop_response
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.BunchesReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.SwitchesReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.GatesReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.CallTypesReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.SupplementServicesReport,
            self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.PayTypesReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.TerminationCausesReport,
            self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.IPNumberingPlansReport,
            self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.TelephoneNumberingPlansReport,
            self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.DocumentTypesReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.TelcosReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.IPDataPointsReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.BunchesMapReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.SpecialNumbersReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            dictionary_report.SS7SignalPointCodeReport,
            self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            subscriber_report.SubscriberReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            subscriber_report.ServiceReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            payment_report.BankTransactionReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            payment_report.ExpressCardReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            payment_report.PublicTerminalReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            payment_report.ServiceCenterReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            payment_report.CrossAccountReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            payment_report.TelephoneCardReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            payment_report.BalanceFillUpReport,
            self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            connection_report.PSTNConnectionReport,
            self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            connection_report.MobileConnectionReport,
            self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            connection_report.AAAConnectionReport,
            self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            connection_report.HTTPConnectionReport,
            self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            connection_report.EMailConnectionReport,
            self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            connection_report.IMConnectionReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            connection_report.VOIPConnectionReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            connection_report.FTPConnectionReport, self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            connection_report.TerminalConnectionReport,
            self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            connection_report.RawFlowsConnectionReport,
            self.handle_report_message
        )
        self.session.channel(2).set_user_message_handler(
            connection_report.NATConnectionReport, self.handle_report_message
        )
        self.session.channel(5).set_user_message_handler(
            data_content_report.RawRecordContentReport,
            self.handle_report_message
        )

    def create_tasks(self, task_creation_requests, timeout=None):
        self.task_creation_info = []
        create_requests = []
        for reqs in task_creation_requests:
            curr_create_reqs = create_task.CreateTaskRequest(
                reqs.telco_codes, reqs.range, reqs.report_limit, reqs.body
            )
            create_requests.append(curr_create_reqs)
            self.task_creation_info.append(
                TaskInfo(curr_create_reqs.message_id, reqs.name)
            )

        self.waiting_responses += len(create_requests)
        for reqs in create_requests:
            self.session.channel(1).send_request(reqs)

        self.wait_for_responses(time.time() + (
            timeout if timeout is not None else self.session.channel(1).channel_parameters.request_response_timeout
        ))
        return self.task_creation_info

    def wait_for_tasks_completion(self, tasks=None, timeout=None):
        list_of_task_id = self.construct_workable_task_id_list(tasks)
        if len(list_of_task_id) == 0:
            return []
        waiting_finish_time = time.time() + (timeout if timeout is not None else 60)
        while time.time() < waiting_finish_time:
            self.waiting_responses += 1
            self.session.channel(1).send_request(data_ready.DataReadyRequest())
            self.wait_for_responses(
                time.time() + min(
                    self.session.channel(1).channel_parameters.request_response_timeout,
                    waiting_finish_time - time.time()
                )
            )
            have_incomplete_tasks = False
            reported_info = []
            for task_id in list_of_task_id:
                task_info = self.tasks.get(task_id, None)
                if task_info is None:
                    reported_info.append(None)
                elif task_info.status.code != TaskExecutionStatus.data_not_ready:
                    reported_info.append(task_info)
                else:
                    have_incomplete_tasks = True
                    break

            if not have_incomplete_tasks:
                return reported_info
            time.sleep(1)

        raise exceptions.GeneralFault(
            'waiting for tasks completion timeout exceeded'
        )

    def load_tasks(self, tasks=None, timeout=None):
        list_of_task_id = self.construct_workable_task_id_list(tasks)
        if len(list_of_task_id) == 0:
            return []
        else:
            reported_info = []
            for task_id in list_of_task_id:
                task_info = self.tasks.get(task_id, None)
                reported_info.append(task_info)
                self.waiting_responses += 1 if task_info is not None else 0
            for task_info in reported_info:
                if task_info is not None:
                    self.session.channel(1).send_request(
                        data_load.DataLoadRequest(task_info.task_id)
                    )

            if timeout is None:
                timeout = self.session.channel(1).channel_parameters.request_response_timeout
            self.wait_for_responses(time.time() + timeout)
            return reported_info

    def interrupt_tasks(self, tasks=None, timeout=None):
        list_of_task_id = self.construct_workable_task_id_list(tasks)
        if len(list_of_task_id) == 0:
            return []
        for task_id in list_of_task_id:
            task_info = self.tasks.get(task_id, None)
            if task_info is not None:
                self.waiting_responses += 1
                self.session.channel(1).send_request(data_interrupt.DataInterruptRequest(task_info.task_id))

        if timeout is None:
            timeout = self.session.channel(1).channel_parameters.request_response_timeout

        self.wait_for_responses(time.time() + timeout)

    def drop_tasks(self, tasks=None, timeout=None):
        list_of_task_id = self.construct_workable_task_id_list(tasks)
        if len(list_of_task_id) == 0:
            return
        for task_id in list_of_task_id:
            task_info = self.tasks.get(task_id, None)
            if task_info is not None:
                self.waiting_responses += 1
                self.session.channel(1).send_request(
                    data_drop.DataDropRequest(task_info.task_id)
                )

        if timeout is None:
            timeout = self.session.channel(1).channel_parameters.request_response_timeout

        self.wait_for_responses(time.time() + timeout)

    def wait_for_tasks_report(self, tasks=None, timeout=None):
        list_of_task_id = self.construct_workable_task_id_list(tasks)
        if len(list_of_task_id) == 0:
            return []
        finish_time = time.time() + (timeout if timeout is not None else 0)
        while time.time() < finish_time:
            for task_id in list_of_task_id:
                report_blocks = self.reports.get(task_id, None)
                if report_blocks is not None and len(report_blocks) > 0:
                    return report_blocks.pop(0)
                continue

            with self.cv_incoming_message:
                self.cv_incoming_message.wait(1)

        raise exceptions.GeneralFault(
            'no task reports have been received in specified time'
        )

    def send_report_block_confirmation(self, channel_id, message_id,
                                       successful=True, broken_record=None,
                                       error_description=None):
        self.session.channel(
            channel_id
        ).send_message(
            report.Acknowledgement(
                message_id, successful, broken_record, error_description
            )
        )

    def construct_workable_task_id_list(self, tasks):
        workable_task_ids = []
        if tasks is None:
            for task_id in self.tasks.keys():
                workable_task_ids.append(task_id)

        else:
            if isinstance(tasks, int):
                workable_task_ids.append(tasks)
            else:
                if isinstance(tasks, TaskInfo):
                    workable_task_ids.append(tasks.task_id)
                else:
                    if isinstance(tasks, list) or isinstance(tasks, tuple):
                        for task in tasks:
                            if isinstance(task, int):
                                workable_task_ids.append(task)
                            else:
                                if isinstance(task, TaskInfo):
                                    workable_task_ids.append(task.task_id)
                                else:
                                    raise exceptions.GeneralFault(
                                        'invalid task description class: "{0}"'.format(task.__class__.__name__)
                                    )

                    else:
                        raise exceptions.GeneralFault(
                            f'invalid task description class: "{tasks.__class__.__name__}"'
                        )
        return workable_task_ids

    def wait_for_responses(self, finish_time):
        while time.time() < finish_time and self.waiting_responses > 0:
            with self.cv_incoming_message:
                self.cv_incoming_message.wait(1)

        if self.waiting_responses > 0:
            raise exceptions.GeneralFault(
                'not all sent requests have been completed in specified time'
            )

    def handle_create_task_response(self, chnl: sessions.Channel,
                                    reqs: create_task.CreateTaskRequest,
                                    resp: create_task.CreateTaskResponse):
        for task in self.task_creation_info:
            if task.request_id == reqs.message_id:
                if not resp.successful:
                    raise exceptions.GeneralFault(
                        'unable to create task: {0}, error - {1}'.format(
                            str(reqs), resp.error_description if resp.error_description is not None else 'unknown'
                        )
                    )
                task.task_id = resp.task_id
                self.tasks[task.task_id] = task
                break

        self.waiting_responses -= 1
        with self.cv_incoming_message:
            self.cv_incoming_message.notify_all()

    def handle_data_ready_response(self, chnl: sessions.Channel,
                                   reqs: data_ready.DataReadyRequest,
                                   resp: data_ready.DataReadyResponse):
        for task_status in resp.task_statuses:
            try:
                task_info = self.tasks[task_status.task_id]
                task_info.status.code = task_status.status
                task_info.error_description = task_status.error_description
                task_info.report_limit_exceeded = task_status.report_limit_exceeded
                task_info.report_records = task_status.report_records
            except KeyError:
                pass

        self.waiting_responses -= 1
        with self.cv_incoming_message:
            self.cv_incoming_message.notify_all()

    def handle_data_load_response(self, chnl: sessions.Channel,
                                  reqs: data_load.DataLoadRequest,
                                  resp: data_load.DataLoadResponse):
        if resp.error_description is not None:
            raise exceptions.GeneralFault(
                'unable to start loading the task #{0}, error - {1}'.format(
                    resp.task_id, resp.error_description
                )
            )
        task_info = self.tasks.get(resp.task_id, None)
        if task_info is not None:
            task_info.report_data_blocks = resp.data_blocks_number
        self.waiting_responses -= 1
        with self.cv_incoming_message:
            self.cv_incoming_message.notify_all()

    def handle_data_interrupt_response(self, chnl: sessions.Channel,
                                       reqs: data_interrupt.DataInterruptRequest,
                                       resp: data_interrupt.DataInterruptResponse):
        if not resp.successful:
            raise exceptions.GeneralFault(
                'unable to interrupt the task #{0}, error - {1}'.format(
                    reqs.task_id, resp.error_description if resp.error_description is not None else 'unknown'
                )
            )
        self.waiting_responses -= 1
        with self.cv_incoming_message:
            self.cv_incoming_message.notify_all()

    def handle_data_drop_response(self, chnl: sessions.Channel,
                                  reqs: data_drop.DataDropRequest,
                                  resp: data_drop.DataDropResponse):
        if not resp.successful:
            raise exceptions.GeneralFault(
                'unable to drop the task #{0}, error - {1}'.format(
                    resp.task_id,
                    resp.error_description if resp.error_description is not None else 'unknown'
                )
            )
        self.tasks.pop(resp.task_id, None)
        self.waiting_responses -= 1
        with self.cv_incoming_message:
            self.cv_incoming_message.notify_all()

    def handle_report_message(self, chnl, reqs, resp):
        report_blocks = self.reports.get(resp.task_id, None)
        if report_blocks is None:
            report_blocks = []
            self.reports[resp.task_id] = report_blocks
        report_blocks.append(resp)
        with self.cv_incoming_message:
            self.cv_incoming_message.notify_all()
