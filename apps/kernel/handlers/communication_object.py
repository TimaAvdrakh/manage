import pickle

from django.conf import settings
import redis

from apps.system.helpers import handler


from apps.kernel.infrastructure.messaging import (
    common,
    network,
)
from apps.kernel.infrastructure import task_manager
from apps.kernel.infrastructure.messaging.task.payload.general import (
    addresses,
)
from apps.kernel.infrastructure.messaging.task.payload import (
    subscriber,
    connection,
    payment,
)
from apps.kernel.infrastructure.messaging.task.payload.subscriber import (
    identifiers,
    operations,
)

redis_instance = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0
)


class CreateCommunicationObjectHandler(handler.AbstractHandler):
    foreign_request = None

    def exec(self):

        print(self._req.POST)
        print('Создание объекта комуникации')

        report_limit = 1000

        # find_range = common.FindRange('200101102957Z', '210114102957Z')
        find_range = common.FindRange(None, None)

        tasks = [
            task_manager.TaskCreationRequest(
                'looking for bank payments',
                None,
                find_range,
                1000,
                payment.BankTransactionTask([
                    payment.BankAccount('**'),
                    operations.OR,
                    payment.BankName('**')
                ])),
            task_manager.TaskCreationRequest(
                'looking for express card payments', None, find_range, 1000, payment.ExpressCardTask([
                    payment.ExpressCardNumber('1*')])),
            task_manager.TaskCreationRequest(
                'looking for telephone card payments', None, find_range, 1000, payment.TelephoneCardTask([
                    payment.PhoneCardNumber('12*')])),
            task_manager.TaskCreationRequest(
                'looking for public terminal payments', None, find_range, 1000, payment.PublicTerminalTask([
                    payment.PaymentTerminalId('**'),
                    operations.OR,
                    addresses.RequestedAddress(city_='**', street_='**')])),
            task_manager.TaskCreationRequest(
                'looking for service center payments', None, find_range, 1000, payment.ServiceCenterTask([
                    payment.ServiceCenterId('1*'),
                    operations.AND,
                    addresses.RequestedAddress(city_='**', street_='**')])),

            task_manager.TaskCreationRequest(
                'looking for subscribers by any login',
                None,
                find_range,
                None,
                subscriber.ValidateSubscribersTask([
                    identifiers.RequestedDataNetworkIdentifier('login', 'davion'),
                    # operations.OR,
                    # identifiers.RequestedPstnIdentifier('**')
                ])),

            task_manager.TaskCreationRequest(
                'Any {0} AAA connections'.format(report_limit),
                None,
                find_range,
                report_limit, connection.ValidateDataTask([
                    connection.RequestedAAA(connection.RequestedAAA.point_id, 1)
                ])),
            task_manager.TaskCreationRequest(
                'Any {0} HTTP connections'.format(report_limit), None, find_range,
                report_limit, connection.ValidateDataTask([
                    connection.RequestedResource(connection.RequestedResource.url, '**')
                ])),
            task_manager.TaskCreationRequest(
                'Any {0} E-Mail connections'.format(report_limit), None, find_range,
                report_limit, connection.ValidateDataTask([
                    connection.RequestedEmail(connection.RequestedEmail.receiver, '**'),
                    operations.OR,
                    connection.RequestedEmail(connection.RequestedEmail.sender, '**'),
                    operations.OR,
                    connection.RequestedEmail(connection.RequestedEmail.subject, '**'),
                    operations.OR,
                    connection.RequestedEmail(connection.RequestedEmail.message, '**')
                ])),
            task_manager.TaskCreationRequest(
                'Any {0} IM connections'.format(report_limit), None, find_range,
                report_limit, connection.ValidateDataTask([
                    connection.RequestedIm(connection.RequestedIm.sender_uin, '**'),
                    operations.OR,
                    connection.RequestedIm(connection.RequestedIm.message, '**')
                ])),
            task_manager.TaskCreationRequest(
                'Any {0} VOIP connections'.format(report_limit), None, find_range,
                report_limit, connection.ValidateDataTask([
                    connection.RequestedVoip(connection.RequestedVoip.voip_calling_number,
                                             network.DataVoipNumber('**', None, None))
                ])),
            task_manager.TaskCreationRequest(
                'Any {0} FTP connections'.format(report_limit), None, find_range,
                report_limit, connection.ValidateDataTask([
                    connection.RequestedFileTransfer(connection.RequestedFileTransfer.server_name, '**')])),
            task_manager.TaskCreationRequest(
                'Any {0} terminal connections'.format(report_limit), None, find_range,
                report_limit, connection.ValidateDataTask([
                    connection.RequestedTermAccess(connection.RequestedTermAccess.point_id, 1)
                ])),
            task_manager.TaskCreationRequest(
                'Any {0} raw flow connections'.format(report_limit), None, find_range,
                report_limit, connection.ValidateDataTask([
                    connection.RequestedRawFlow(connection.RequestedRawFlow.point_id, 1)
                ])),
            task_manager.TaskCreationRequest(
                'Any {0} NAT connections'.format(report_limit), None, find_range,
                report_limit, connection.ValidateDataTask([
                    connection.RequestedAddressTranslation(connection.RequestedAddressTranslation.point_id, 1)
                ]))
        ]

        self.foreign_request = pickle.dumps(tasks)


