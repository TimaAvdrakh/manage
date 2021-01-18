from pyasn1.type import tag
from pyasn1.type import univ
from pyasn1.codec.der.encoder import encode as der_encode

from apps.kernel.infrastructure.messaging import base
from apps.system.lib import (
    asn1,
    exceptions,
)
from .general import operations
from .general import identifiers
from .general import addresses


class BankTransactionTask(base.ASN1Constructable):

    def __init__(self, items_):
        self.items = items_

    def __dir__(self):
        return ['items']

    def to_asn1(self):
        task = asn1.SkrPaymentsTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
                )
            )
        )
        task['id'] = asn1.sorm_request_payment_bank_transaction
        task['data'] = univ.Any(self.encode_data())
        return task

    def encode_data(self):
        body = asn1.SkrRequestedBankTransactionPays()
        for item in self.items:
            choice = asn1.SkrRequestedBankTransactionPaysParameters()
            if isinstance(item, operations.LogicalOperation):
                choice.setComponentByName('separator', item.code)
            else:
                if isinstance(item, BankAccount):
                    choice.setComponentByName('bank-account', str(item))
                else:
                    if isinstance(item, BankName):
                        choice.setComponentByName('bank-name', str(item))
                    else:
                        raise exceptions.GeneralFault(
                            f'Invalid item "{0}" specified in "{1}"'.format(
                                item.__class__.__name__, self.__class__.__name__
                            )
                        )
            body.append(choice)

        return der_encode(body)


class ExpressCardTask(base.ASN1Constructable):

    def __init__(self, items_):
        self.items = items_

    def __dir__(self):
        return ['items']

    def to_asn1(self):
        task = asn1.SkrPaymentsTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
                )
            )
        )
        task['id'] = asn1.sorm_request_payment_express_pays
        task['data'] = univ.Any(self.encode_data())
        return task

    def encode_data(self):
        body = asn1.SkrRequestedExpressPays()
        for item in self.items:
            choice = asn1.SkrRequestedExpressPaysParameters()
            if isinstance(item, operations.LogicalOperation):
                choice.setComponentByName('separator', item.code)
            else:
                if isinstance(item, ExpressCardNumber):
                    choice.setComponentByName('express-card', str(item))
                else:
                    raise exceptions.GeneralFault(
                        'Invalid item "{0}" specified in "{1}"'.format(
                            item.__class__.__name__, self.__class__.__name__
                        )
                    )
            body.append(choice)

        return der_encode(body)


class PublicTerminalTask(base.ASN1Constructable):

    def __init__(self, items_):
        self.items = items_

    def __dir__(self):
        return ['items']

    def to_asn1(self):
        task = asn1.SkrPaymentsTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
                )
            )
        )
        task['id'] = asn1.sorm_request_payment_terminal_pays
        task['data'] = univ.Any(self.encode_data())
        return task

    def encode_data(self):
        body = asn1.SkrRequestedTerminalPays()
        for item in self.items:
            choice = asn1.SkrRequestedTerminalPaysParameters()
            if isinstance(item, operations.LogicalOperation):
                choice.setComponentByName('separator', item.code)
            else:
                if isinstance(item, PaymentTerminalId):
                    choice.setComponentByName('terminal-id', str(item))
                else:
                    if isinstance(item, PaymentTerminalNumber):
                        choice.setComponentByName('terminal-number', str(item))
                    else:
                        if isinstance(item, addresses.RequestedAddress):
                            item.copy_to(
                                choice.getComponentByName('terminal-address')
                            )
                        else:
                            raise exceptions.GeneralFault(
                                'Invalid item "{0}" specified in "{1}"'.format(
                                    item.__class__.__name__, self.__class__.__name__
                                )
                            )
            body.append(choice)

        return der_encode(body)


class ServiceCenterTask(base.ASN1Constructable):

    def __init__(self, items_):
        self.items = items_

    def __dir__(self):
        return [
            'items']

    def to_asn1(self):
        task = asn1.SkrPaymentsTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
                )
            )
        )
        task['id'] = asn1.sorm_request_payment_service_center
        task['data'] = univ.Any(self.encode_data())
        return task

    def encode_data(self):
        body = asn1.SkrRequestedServiceCenterPays()
        for item in self.items:
            choice = asn1.SkrRequestedServiceCenterPaysParameters()
            if isinstance(item, operations.LogicalOperation):
                choice.setComponentByName('separator', item.code)
            else:
                if isinstance(item, ServiceCenterId):
                    choice.setComponentByName('center-id', str(item))
                else:
                    if isinstance(item, addresses.RequestedAddress):
                        item.copy_to(
                            choice.getComponentByName('center-address')
                        )
                    else:
                        raise exceptions.GeneralFault(
                            'Invalid item "{0}" specified in "{1}"'.format(
                                item.__class__.__name__, self.__class__.__name__
                            )
                        )
            body.append(choice)

        return der_encode(body)


class CrossAccountTask(base.ASN1Constructable):

    def __init__(self, items_):
        self.items = items_

    def __dir__(self):
        return ['items']

    def to_asn1(self):
        task = asn1.SkrPaymentsTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
                )
            )
        )
        task['id'] = asn1.sorm_request_payment_cross_account
        task['data'] = univ.Any(self.encode_data())
        return task

    def encode_data(self):
        body = asn1.SkrRequestedCrossAccountPays()
        for item in self.items:
            choice = asn1.SkrRequestedCrossAccountPaysParameters()
            if isinstance(item, operations.LogicalOperation):
                choice.setComponentByName('separator', item.code)
            else:
                if isinstance(item, RequestedSenderIdentifier):
                    item.copy_to(
                        choice.getComponentByName('source-identifier')
                    )
                else:
                    if isinstance(item, RequestedReceiverIdentifier):
                        item.copy_to(
                            choice.getComponentByName('dest-identifier')
                        )
                    else:
                        raise exceptions.GeneralFault(
                            'Invalid item "{0}" specified in "{1}"'.format(
                                item.__class__.__name__, self.__class__.__name__
                            )
                        )
            body.append(choice)

        return der_encode(body)


class TelephoneCardTask(base.ASN1Constructable):

    def __init__(self, items_):
        self.items = items_

    def __dir__(self):
        return ['items']

    def to_asn1(self):
        task = asn1.SkrPaymentsTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
                )
            )
        )
        task['id'] = asn1.sorm_request_payment_telephone_card
        task['data'] = univ.Any(self.encode_data())
        return task

    def encode_data(self):
        body = asn1.SkrRequestedTelephoneCardPays()
        for item in self.items:
            choice = asn1.SkrRequestedTelephoneCardPaysParameters()
            if isinstance(item, operations.LogicalOperation):
                choice.setComponentByName('separator', item.code)
            else:
                if isinstance(item, PhoneCardNumber):
                    choice.setComponentByName('card-number', str(item))
                else:
                    raise exceptions.GeneralFault(
                        'Invalid item "{0}" specified in "{1}"'.format(
                            item.__class__.__name__, self.__class__.__name__
                        )
                    )
            body.append(choice)

        return der_encode(body)


class BalanceFillUpTask(base.ASN1Constructable):

    def __init__(self, items_):
        self.items = items_

    def __dir__(self):
        return [
            'items']

    def to_asn1(self):
        task = asn1.SkrPaymentsTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
                )
            )
        )
        task['id'] = asn1.sorm_request_payment_balance_fillups
        task['data'] = univ.Any(self.encode_data())
        return task

    def encode_data(self):
        body = asn1.SkrRequestedBalanceFillups()
        for item in self.items:
            choice = asn1.SkrRequestedBalanceFillupsParameters()
            if isinstance(item, operations.LogicalOperation):
                choice.setComponentByName('separator', item.code)
            else:
                if isinstance(
                        item, identifiers.RequestedCdmaIdentifier
                ) or isinstance(
                    item, identifiers.RequestedDataNetworkIdentifier
                ) or isinstance(
                    item, identifiers.RequestedGsmIdentifier
                ) or isinstance(
                    item, identifiers.RequestedPstnIdentifier
                ) or isinstance(
                    item, identifiers.RequestedPagerIdentifier
                ) or isinstance(item, identifiers.RequestedVoipIdentifier):
                    item.copy_to(choice.getComponentByName('identifier'))
                else:
                    raise exceptions.GeneralFault(
                        'Invalid item "{0}" specified in "{1}"'.format(
                            item.__class__.__name__, self.__class__.__name__
                        )
                    )
            body.append(choice)

        return der_encode(body)


class BankDivisionTransferTask(base.ASN1Constructable):

    def __init__(self, items_):
        self.items = items_

    def __dir__(self):
        return [
            'items']

    def to_asn1(self):
        task = asn1.SkrPaymentsTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
                )
            )
        )
        task['id'] = asn1.sorm_request_payment_bank_division_transfer
        task['data'] = univ.Any(self.encode_data())
        return task

    def encode_data(self):
        body = asn1.SkrRequestedBankDivisionTransferPays()
        for item in self.items:
            choice = asn1.SkrRequestedTransferParameters()
            if isinstance(item, operations.LogicalOperation):
                choice.setComponentByName('separator', item.code)
            else:
                if isinstance(
                        item, identifiers.RequestedCdmaIdentifier
                ) or isinstance(
                    item, identifiers.RequestedDataNetworkIdentifier
                ) or isinstance(
                    item, identifiers.RequestedGsmIdentifier
                ) or isinstance(
                    item, identifiers.RequestedPstnIdentifier
                ) or isinstance(
                    item, identifiers.RequestedPagerIdentifier
                ) or isinstance(item, identifiers.RequestedVoipIdentifier):
                    item.copy_to(
                        choice.getComponentByName('source-identifier')
                    )
                else:
                    raise exceptions.GeneralFault(
                        'Invalid item "{0}" specified in "{1}"'.format(
                            item.__class__.__name__, self.__class__.__name__
                        )
                    )
            body.append(choice)

        return der_encode(body)


class BankCardTransferTask(base.ASN1Constructable):

    def __init__(self, items_):
        self.items = items_

    def __dir__(self):
        return [
            'items']

    def to_asn1(self):
        task = asn1.SkrPaymentsTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
                )
            )
        )
        task['id'] = asn1.sorm_request_payment_bank_card_transfer
        task['data'] = univ.Any(self.encode_data())
        return task

    def encode_data(self):
        body = asn1.SkrRequestedBankCardTransferPays()
        for item in self.items:
            choice = asn1.SkrRequestedTransferParameters()
            if isinstance(item, operations.LogicalOperation):
                choice.setComponentByName('separator', item.code)
            else:
                if isinstance(
                        item, identifiers.RequestedCdmaIdentifier
                ) or isinstance(
                    item, identifiers.RequestedDataNetworkIdentifier
                ) or isinstance(
                    item, identifiers.RequestedGsmIdentifier
                ) or isinstance(
                    item, identifiers.RequestedPstnIdentifier
                ) or isinstance(
                    item, identifiers.RequestedPagerIdentifier
                ) or isinstance(item, identifiers.RequestedVoipIdentifier):
                    item.copy_to(
                        choice.getComponentByName('source-identifier')
                    )
                else:
                    raise exceptions.GeneralFault(
                        'Invalid item "{0}" specified in "{1}"'.format(
                            item.__class__.__name__, self.__class__.__name__
                        )
                    )
            body.append(choice)

        return der_encode(body)


class BankAccountTransferTask(base.ASN1Constructable):

    def __init__(self, items_):
        self.items = items_

    def __dir__(self):
        return [
            'items']

    def to_asn1(self):
        task = asn1.SkrPaymentsTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
                )
            )
        )
        task['id'] = asn1.sorm_request_payment_bank_account_transfer
        task['data'] = univ.Any(self.encode_data())
        return task

    def encode_data(self):
        body = asn1.SkrRequestedBankCardTransferPays()
        for item in self.items:
            choice = asn1.SkrRequestedTransferParameters()
            if isinstance(item, operations.LogicalOperation):
                choice.setComponentByName('separator', item.code)
            else:
                if isinstance(
                        item, identifiers.RequestedCdmaIdentifier
                ) or isinstance(
                    item, identifiers.RequestedDataNetworkIdentifier
                ) or isinstance(
                    item, identifiers.RequestedGsmIdentifier
                ) or isinstance(
                    item, identifiers.RequestedPstnIdentifier
                ) or isinstance(
                    item, identifiers.RequestedPagerIdentifier
                ) or isinstance(item, identifiers.RequestedVoipIdentifier):
                    item.copy_to(
                        choice.getComponentByName('source-identifier')
                    )
                else:
                    raise exceptions.GeneralFault(
                        'Invalid item "{0}" specified in "{1}"'.format(
                            item.__class__.__name__, self.__class__.__name__
                        )
                    )
            body.append(choice)

        return der_encode(body)


class BankName(base.NamedString):

    def __init__(self, value_):
        super().__init__(value_)


class BankAccount(base.NamedString):

    def __init__(self, value_):
        super().__init__(value_)


class CardNumber(base.NamedString):

    def __init__(self, value_):
        super().__init__(value_)


ExpressCardNumber = CardNumber
PhoneCardNumber = CardNumber


class PaymentTerminalId(base.NamedString):

    def __init__(self, value_):
        super().__init__(value_)


class PaymentTerminalNumber(base.NamedString):

    def __init__(self, value_):
        super().__init__(value_)


class ServiceCenterId(base.NamedString):

    def __init__(self, value_):
        super().__init__(value_)


class RequestedSenderIdentifier(identifiers.RequestedIdentifier):

    def __init__(self, identifier_):
        super().__init__(identifier_)


class RequestedReceiverIdentifier(identifiers.RequestedIdentifier):

    def __init__(self, identifier_):
        super().__init__(identifier_)
