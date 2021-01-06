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


class ValidateSubscribersTask(base.ASN1Constructable):

    def __init__(self, items_):
        self.items = items_

    def __dir__(self):
        return [
            'items']

    def to_asn1(self):
        task = asn1.NRST_AbonentsTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
                )
            )
        )
        body = task.getComponentByName('validate-abonents-task')
        for item in self.items:
            choice = asn1.NRST_RequestedIdentifierParameters()
            if isinstance(item, operations.LogicalOperation):
                choice.setComponentByName('separator', item.code)
            else:
                item.copy_to(choice.getComponentByName('find-mask'))
            body.append(choice)

        return task


class ValidateIdentifiersTask(base.ASN1Constructable):

    def __init__(self, items_):
        self.items = items_

    def __dir__(self):
        return ['items']

    def to_asn1(self):
        task = asn1.NRST_AbonentsTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
                )
            )
        )
        body = task.getComponentByName('validate-identifiers')
        for item in self.items:
            choice = asn1.NRST_RequestedAbonentsParameters()
            if isinstance(item, operations.LogicalOperation):
                choice.setComponentByName('separator', item.code)
            else:
                component = choice.getComponentByName('find-mask')
                if isinstance(item, RequestedPerson):
                    predicate = asn1.NRST_RequestedPerson()
                    item.copy_to(predicate)
                    component.setComponentByName(
                        'id', asn1.sorm_request_abonent_person
                    )
                    component.setComponentByName(
                        'data', univ.Any(der_encode(predicate))
                    )
                else:
                    if isinstance(item, RequestedOrganization):
                        predicate = asn1.NRST_RequestedOrganization()
                        item.copy_to(predicate)
                        component.setComponentByName(
                            'id', asn1.sorm_request_abonent_organization
                        )
                        component.setComponentByName(
                            'data', univ.Any(der_encode(predicate))
                        )
                    else:
                        raise exceptions.GeneralFault(
                            'an invalid object type "{0}" in the "{1}" class'.format(
                                item.__class__.__name__, self.__class__.__name__)
                        )
            body.append(choice)

        return task


class ValidateServicesTask(base.ASN1Constructable):

    def __init__(self, items_):
        self.items = items_

    def __dir__(self):
        return ['items']

    def to_asn1(self):
        task = asn1.NRST_AbonentsTask(
            tagSet=(
                tag.initTagSet(
                    tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
                )
            )
        )
        body = task.getComponentByName('validate-services')
        for item in self.items:
            choice = asn1.NRST_ValidateServicesParameters()
            if isinstance(item, operations.LogicalOperation):
                choice.setComponentByName('separator', item.code)
            else:
                component = choice.getComponentByName('find-mask')
                if isinstance(item, str):
                    component.setComponentByName('contract', item)
                else:
                    if isinstance(
                            item, identifiers.RequestedPagerIdentifier
                    ) or isinstance(
                        item, identifiers.RequestedPstnIdentifier
                    ) or isinstance(
                        item, identifiers.RequestedGsmIdentifier
                    ) or isinstance(
                        item, identifiers.RequestedCdmaIdentifier
                    ) or isinstance(
                        item, identifiers.RequestedVoipIdentifier
                    ) or isinstance(
                        item, identifiers.RequestedDataNetworkIdentifier
                    ):
                        identifier = asn1.NRST_RequestedIdentifier(
                            tagSet=(
                                tag.initTagSet(
                                    tag.Tag(
                                        tag.tagClassContext,
                                        tag.tagFormatConstructed,
                                        1
                                    )
                                )
                            )
                        )
                        item.copy_to(identifier)
                        component.setComponentByName('identifier', identifier)
                    else:
                        raise exceptions.GeneralFault(
                            'an invalid object type "{0}" in the "{1}" class'.format(
                                item.__class__.__name__, self.__class__.__name__
                            )
                        )
            body.append(choice)

        return task


class RequestedOrganization(base.ASN1Copyable):

    def __init__(self, full_name_=None, address_=None,
                 tax_reference_number_=None, internal_user_=None,
                 contract_=None):
        if full_name_ is None:
            if address_ is None:
                if tax_reference_number_ is None:
                    if internal_user_ is None:
                        if contract_ is None:
                            raise exceptions.GeneralFault(
                                'no one parameter is defined for the "{0}" class'.format(
                                    self.__class__.__name__
                                )
                            )
        self.full_name = full_name_
        self.address = address_
        self.tax_reference_number = tax_reference_number_
        self.internal_user = internal_user_
        self.contract = contract_

    def __dir__(self):
        return [
            'full_name', 'address', 'tax_reference_number', 'internal_user',
            'contract'
        ]

    def copy_to(self, target_):
        self.set_component(target_, 'full-name', self.full_name)
        self.set_component(target_, 'address', self.address)
        self.set_component(target_, 'inn', self.tax_reference_number)
        self.set_component(target_, 'internal-user', self.internal_user)
        self.set_component(target_, 'contract', self.contract)


class RequestedDocument(base.ASN1Copyable):

    def __init__(self, document_type_id_=None, document_serial_=None,
                 document_number_=None):
        if document_type_id_ is None:
            if document_serial_ is None:
                if document_number_ is None:
                    raise exceptions.GeneralFault(
                        'no one parameter is defined for the "{0}" class'.format(
                            self.__class__.__name__
                        )
                    )
        self.document_type_id = document_type_id_
        self.document_serial = document_serial_
        self.document_number = document_number_

    def __dir__(self):
        return [
            'document_type_id', 'document_serial', 'document_number'
        ]

    def copy_to(self, target_):
        self.set_component(target_, 'doc-type-id', self.document_type_id)
        self.set_component(target_, 'passport-serial', self.document_serial)
        self.set_component(target_, 'passport-number', self.document_number)


class RequestedPerson(base.ASN1Copyable):

    def __init__(self, given_name_=None, patronymic_name_=None, surname_=None,
                 document_info_=None, address_=None, icc_=None,
                 contract_=None):
        if given_name_ is None:
            if patronymic_name_ is None:
                if surname_ is None:
                    if document_info_ is None:
                        if address_ is None:
                            if icc_ is None:
                                if contract_ is None:
                                    raise exceptions.GeneralFault(
                                        'no one parameter is defined for the "{0}" class'.format(
                                            self.__class__.__name__
                                        )
                                    )
        self.given_name = given_name_
        self.patronymic_name = patronymic_name_
        self.surname = surname_
        self.document_info = document_info_
        self.address = address_
        self.icc = icc_
        self.contract = contract_

    def __dir__(self):
        return [
            'given_name', 'patronymic_name', 'surname', 'document_info',
            'address', 'icc', 'contract'
        ]

    def copy_to(self, target_):
        self.set_component(target_, 'given-name', self.given_name)
        self.set_component(target_, 'initial', self.patronymic_name)
        self.set_component(target_, 'family-name', self.surname)
        self.set_component(target_, 'passport-info', self.document_info)
        self.set_component(target_, 'address', self.address)
        self.set_component(target_, 'icc', self.icc)
        self.set_component(target_, 'contract', self.contract)
