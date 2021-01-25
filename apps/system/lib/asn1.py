from pyasn1.type import (
    univ,
    char,
    namedtype,
    namedval,
    tag,
    constraint,
    useful,
)


class SkrAbonentInfo(univ.Sequence):
    pass


SkrAbonentInfo.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class SkrInternalUsersRecord(univ.Sequence):
    pass


SkrInternalUsersRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'user-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType(
        'internal-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrInternalUsers(univ.SequenceOf):
    pass


SkrInternalUsers.componentType = SkrInternalUsersRecord()


class SkrAbonentOrganization(univ.Sequence):
    pass


SkrAbonentOrganization.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'full-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType(
        'inn',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.OptionalNamedType(
        'contact',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'phone-fax',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'internal-users',
        SkrInternalUsers().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.OptionalNamedType(
        'bank',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))
    ),
    namedtype.OptionalNamedType(
        'bank-account',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 30))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    )
)


class SkrIdentCardStructInfoReport(univ.Sequence):
    pass


SkrIdentCardStructInfoReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'ident-card-serial',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 16))
        )
    ),
    namedtype.NamedType(
        'ident-card-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 16))
        )
    ),
    namedtype.NamedType(
        'ident-card-description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    )
)


class SkrIdentCardInfoReport(univ.Choice):
    pass


SkrIdentCardInfoReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'struct-info',
        SkrIdentCardStructInfoReport().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'unstruct-info',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 1024))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrPassportInfoReport(univ.Sequence):
    pass


SkrPassportInfoReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'ident-card-info',
        SkrIdentCardInfoReport()
    ),
    namedtype.NamedType(
        'doc-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 65535))
        )
    )
)


class SkrPersonStructNameInfoReport(univ.Sequence):
    pass


SkrPersonStructNameInfoReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'given-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType(
        'initial',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType(
        'family-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrPersonNameInfoReport(univ.Choice):
    pass


SkrPersonNameInfoReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'struct-name',
        SkrPersonStructNameInfoReport().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'unstruct-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 1024))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrAbonentPerson(univ.Sequence):
    pass


SkrAbonentPerson.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'name-info',
        SkrPersonNameInfoReport()
    ),
    namedtype.OptionalNamedType(
        'birth-date', useful.GeneralizedTime()
    ),
    namedtype.NamedType(
        'passport-info',
        SkrPassportInfoReport()
    ),
    namedtype.OptionalNamedType(
        'bank',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'bank-account',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 30))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrReportedIdentifier(univ.Sequence):
    pass


SkrReportedIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class SkrTelcoID(univ.Integer):
    pass


SkrTelcoID.subtypeSpec = constraint.ValueRangeConstraint(0, 65535)


class SkrDateAndTime(useful.UTCTime):
    pass


class SkrAbonentService(univ.Sequence):
    pass


SkrAbonentService.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'service-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.OptionalNamedType('idents', SkrReportedIdentifier()),
    namedtype.NamedType(
        'contract',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.NamedType('end-time', SkrDateAndTime()),
    namedtype.OptionalNamedType(
        'parameter',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrActiveServices(univ.SequenceOf):
    pass


SkrActiveServices.componentType = SkrAbonentService()


class SkrAddressStructInfoReport(univ.Sequence):
    pass


SkrAddressStructInfoReport.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType(
        'zip',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'country',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'region',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.OptionalNamedType(
        'zone',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.OptionalNamedType(
        'city',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.OptionalNamedType(
        'street',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.OptionalNamedType(
        'building',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    ),
    namedtype.OptionalNamedType(
        'build-sect',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))
        )
    ),
    namedtype.OptionalNamedType(
        'apartment',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))
        )
    )
)


class SkrAddressInfoReport(univ.Choice):
    pass


SkrAddressInfoReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'struct-info',
        SkrAddressStructInfoReport().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'unstruct-info',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 1024))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrAddressType(univ.Enumerated):
    pass


SkrAddressType.namedValues = namedval.NamedValues(
    ('registered', 0),
    ('postal', 1),
    ('invoice', 2),
    ('device-location', 3),
    ('reserved', 4)
)


class SkrReportedAddress(univ.Sequence):
    pass


SkrReportedAddress.componentType = namedtype.NamedTypes(
    namedtype.NamedType('title', SkrAddressType()),
    namedtype.NamedType('address-info', SkrAddressInfoReport())
)


class SkrReportedAddresses(univ.SequenceOf):
    pass


SkrReportedAddresses.componentType = SkrReportedAddress()


class SkrActiveStatus(univ.Enumerated):
    pass


SkrActiveStatus.namedValues = namedval.NamedValues(
    ('active', 0),
    ('not-active', 1)
)


class SkrLineData(univ.Sequence):
    pass


SkrLineData.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType(
        'object',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'cross',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'block',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.OptionalNamedType(
        'pair',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.OptionalNamedType(
        'reserved', char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    )
)


class SkrWirelessLocation(univ.Sequence):
    pass


SkrWirelessLocation.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'cell', char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType(
        'mac',
        univ.OctetString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(6, 6))
        )
    )
)


class SkrGeoLocation(univ.Sequence):
    pass


SkrGeoLocation.componentType = namedtype.NamedTypes(
    namedtype.NamedType('latitude-grade', univ.Real()),
    namedtype.NamedType('longitude-grade', univ.Real()),
    namedtype.NamedType(
        'projection-type',
        univ.Enumerated(namedValues=(namedval.NamedValues(
            ('wgs84', 0),
            ('utm', 1),
            ('sgs85', 2)
        )))
    )
)


class SkrMobileLocation(univ.Sequence):
    pass


SkrMobileLocation.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'lac', univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 65535))
        )
    ),
    namedtype.NamedType(
        'cell',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.OptionalNamedType(
        'ta',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 63))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    )
)


class SkrLocation(univ.Choice):
    pass


SkrLocation.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'mobile-location', SkrMobileLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'wireless-location',
        SkrWirelessLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'geo-location',
        SkrGeoLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    )
)


class SkrNetworkType(univ.Enumerated):
    pass


SkrNetworkType.namedValues = namedval.NamedValues(
    ('not-specified', 0),
    ('mob-gsm', 1),
    ('mob-cdma', 2),
    ('fix-pstn', 3),
    ('data-ip', 4),
    ('data-srv', 5),
    ('data-ip-mob', 6),
    ('data-ip-wifi', 7),
    ('data-ip-max', 8),
    ('paging', 9),
    ('voip', 10)
)


class SkrStandard(SkrNetworkType):
    pass


class SkrAbonentsRecord(univ.Sequence):
    pass


SkrAbonentsRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('idents', SkrReportedIdentifier()),
    namedtype.NamedType('contract-date', SkrDateAndTime()),
    namedtype.NamedType(
        'contract',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType('actual-from', SkrDateAndTime()),
    namedtype.NamedType('actual-to', SkrDateAndTime()),
    namedtype.NamedType('abonent', SkrAbonentInfo()),
    namedtype.NamedType('status', SkrActiveStatus()),
    namedtype.OptionalNamedType(
        'attach',
        SkrDateAndTime().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'detach',
        SkrDateAndTime().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'last-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'services',
        SkrActiveServices().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.OptionalNamedType(
        'line-data',
        SkrLineData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'standard',
        SkrStandard().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.OptionalNamedType(
        'addresses',
        SkrReportedAddresses().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    )
)


class SkrAbonentsReport(univ.Sequence):
    pass


SkrAbonentsReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class SkrRequestedIdentifier(univ.Sequence):
    pass


SkrRequestedIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class SkrDataNetworkATM(univ.Sequence):
    pass


SkrDataNetworkATM.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'vpi',
        univ.OctetString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'vci',
        univ.OctetString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 2))
        )
    )
)


class SkrDataNetworkEquipment(univ.Choice):
    pass


SkrDataNetworkEquipment.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'mac',
        univ.OctetString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(6, 6))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'atm',
        SkrDataNetworkATM().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class SkrIPV4Address(univ.OctetString):
    pass


SkrIPV4Address.subtypeSpec = constraint.ValueSizeConstraint(4, 4)


class SkrIPV6Address(univ.OctetString):
    pass


SkrIPV6Address.subtypeSpec = constraint.ValueSizeConstraint(16, 16)


class SkrIPAddress(univ.Choice):
    pass


SkrIPAddress.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'ipv4',
        SkrIPV4Address().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'ipv6',
        SkrIPV6Address().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrRequestedDataNetworkIdentifier(univ.Choice):
    pass


SkrRequestedDataNetworkIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'user-equipment',
        SkrDataNetworkEquipment().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'login',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'ip-address',
        SkrIPAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'e-mail',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'voip-phone-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    )
)


class SkrRequestedPagerIdentifier(char.NumericString):
    pass


SkrRequestedPagerIdentifier.subtypeSpec = constraint.ValueSizeConstraint(2, 18)


class SkrRequestedPstnIdentifier(univ.Sequence):
    pass


SkrRequestedPstnIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'directory-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        )
    ),
    namedtype.OptionalNamedType(
        'internal-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        )
    )
)


class SkrRequestedGsmIdentifier(univ.Choice):
    pass


SkrRequestedGsmIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'directory-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'imsi',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)
            )
        )
    ),
    namedtype.NamedType(
        'imei',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrRequestedCdmaIdentifier(univ.Choice):
    pass


SkrRequestedCdmaIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'directory-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'imsi',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'esn',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)
            )
        )
    ),
    namedtype.NamedType(
        'min',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    )
)


class SkrRequestedVoipIdentifier(univ.Choice):
    pass


SkrRequestedVoipIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'ip-address',
        SkrIPAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'originator-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'calling-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrRecodedRequestedIdentifier(univ.Choice):
    pass


SkrRecodedRequestedIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'pager-identifier',
        SkrRequestedPagerIdentifier().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'pstn-identifier',
        SkrRequestedPstnIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'gsm-identifier',
        SkrRequestedGsmIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'cdma-identifier',
        SkrRequestedCdmaIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.NamedType(
        'data-network-identifier',
        SkrRequestedDataNetworkIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
            )
        )
    ),
    namedtype.NamedType(
        'voip-identifier',
        SkrRequestedVoipIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)
            )
        )
    )
)


class SkrValidateServicesParameter(univ.Choice):
    pass


SkrValidateServicesParameter.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'contract',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'identifier',
        SkrRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-identifier',
        SkrRecodedRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 101)
            )
        )
    )
)


class SkrLogicalOperation(univ.Enumerated):
    pass


SkrLogicalOperation.namedValues = namedval.NamedValues(
    ('operation-open-bracket', 0),
    ('operation-close-bracket', 1),
    ('operation-or', 2),
    ('operation-and', 3),
    ('operation-not', 4)
)


class SkrValidateServicesParameters(univ.Choice):
    pass


SkrValidateServicesParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        SkrLogicalOperation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)
            )
        )
    ),
    namedtype.NamedType(
        'find-mask',
        SkrValidateServicesParameter().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class SkrValidateServicesTask(univ.SequenceOf):
    pass


SkrValidateServicesTask.componentType = SkrValidateServicesParameters()


class SkrRequestedIdentifierParameters(univ.Choice):
    pass


SkrRequestedIdentifierParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        SkrLogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'find-mask',
        SkrRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-find-mask',
        SkrRecodedRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 100)
            )
        )
    )
)


class SkrRequestedIdentifiers(univ.SequenceOf):
    pass


SkrRequestedIdentifiers.componentType = SkrRequestedIdentifierParameters()


class SkrValidateAbonentsTask(SkrRequestedIdentifiers):
    pass


class SkrRequestedPassport(univ.Sequence):
    pass


SkrRequestedPassport.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType(
        'doc-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 65535))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'passport-serial',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 16))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'passport-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 16))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrRequestedAddress(univ.Sequence):
    pass


SkrRequestedAddress.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType(
        'zip',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'country',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'region',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.OptionalNamedType(
        'zone',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.OptionalNamedType(
        'city',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.OptionalNamedType(
        'street',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.OptionalNamedType(
        'building',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    ),
    namedtype.OptionalNamedType(
        'build-sect',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))
        )
    ),
    namedtype.OptionalNamedType(
        'apartment',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))
        )
    )
)


class SkrRequestedPerson(univ.Sequence):
    pass


SkrRequestedPerson.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType(
        'given-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'initial',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'family-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.OptionalNamedType(
        'passport-info',
        SkrRequestedPassport().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))
        )
    ),
    namedtype.OptionalNamedType(
        'address',
        SkrRequestedAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'icc',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(10, 20))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.OptionalNamedType(
        'contract',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6)))
    )
)


class SkrRequestedOrganization(univ.Sequence):
    pass


SkrRequestedOrganization.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType(
        'full-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'address',
        SkrRequestedAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'inn',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        ).subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'internal-user',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.OptionalNamedType(
        'contract',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    )
)


class SkrRecodedRequestedAbonent(univ.Choice):
    pass


SkrRecodedRequestedAbonent.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'person',
        SkrRequestedPerson().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'organization',
        SkrRequestedOrganization().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class SkrRequestedAbonent(univ.Sequence):
    pass


SkrRequestedAbonent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class SkrRequestedAbonentsParameters(univ.Choice):
    pass


SkrRequestedAbonentsParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        SkrLogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'find-mask',
        SkrRequestedAbonent().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-find-mask',
        SkrRecodedRequestedAbonent().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 100)
            )
        )
    )
)


class SkrRequestedAbonents(univ.SequenceOf):
    pass


SkrRequestedAbonents.componentType = SkrRequestedAbonentsParameters()


class SkrValidateIdentifiersTask(SkrRequestedAbonents):
    pass


class SkrAbonentsTask(univ.Choice):
    pass


SkrAbonentsTask.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'validate-abonents-task',
        SkrValidateAbonentsTask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'validate-identifiers',
        SkrValidateIdentifiersTask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'validate-services',
        SkrValidateServicesTask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrAcknowledgement(univ.Sequence):
    pass


SkrAcknowledgement.componentType = namedtype.NamedTypes(
    namedtype.NamedType('successful', univ.Boolean()),
    namedtype.OptionalNamedType('broken-record', univ.Integer()),
    namedtype.OptionalNamedType(
        'error-description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 1024))
        )
    )
)


class SkrAdjustmentRequest(univ.Sequence):
    pass


SkrAdjustmentRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'supports',
        univ.SequenceOf(componentType=(useful.ObjectDescriptor()))
    )
)


class SkrAdjustmentResponse(univ.Null):
    pass


class SkrAttributeType(univ.Enumerated):
    pass


SkrAttributeType.namedValues = namedval.NamedValues(
    ('date-time', 0),
    ('integer', 1),
    ('string', 2),
    ('boolean', 3),
    ('float', 4),
    ('location', 5),
    ('empty', 6)
)


class SkrValidateBalanceFillupRecord(univ.Sequence):
    pass


SkrValidateBalanceFillupRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'pay-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType('device-id', SkrReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.OptionalNamedType(
        'pay-parameters',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    )
)


class SkrBalanceFillupReportData(univ.SequenceOf):
    pass


SkrBalanceFillupReportData.componentType = SkrValidateBalanceFillupRecord()


class SkrValidateBankAccountTransferRecord(univ.Sequence):
    pass


SkrValidateBankAccountTransferRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('donated-id', SkrReportedIdentifier()),
    namedtype.NamedType(
        'bank-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType(
        'bank-account',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrBankAccountTransferReportData(univ.SequenceOf):
    pass


SkrBankAccountTransferReportData.componentType = SkrValidateBankAccountTransferRecord()


class SkrValidateBankCardTransferRecord(univ.Sequence):
    pass


SkrValidateBankCardTransferRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('donanted-id', SkrReportedIdentifier()),
    namedtype.NamedType(
        'bank-card-id',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 12))
        )
    ),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrBankCardTransferReportData(univ.SequenceOf):
    pass


SkrBankCardTransferReportData.componentType = SkrValidateBankCardTransferRecord()


class SkrValidateBankDivisionTransferRecord(univ.Sequence):
    pass


SkrValidateBankDivisionTransferRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('donanted-id', SkrReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'person-received',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    ),
    namedtype.NamedType(
        'bank-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType(
        'bank-division-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    ),
    namedtype.NamedType('bank-division-address', SkrReportedAddress()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrBankDivisionTransferReportData(univ.SequenceOf):
    pass


SkrBankDivisionTransferReportData.componentType = SkrValidateBankDivisionTransferRecord()


class SkrBankTransactionRecord(univ.Sequence):
    pass


SkrBankTransactionRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('device-id', SkrReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'bank-account',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType(
        'bank-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    ),
    namedtype.NamedType('bank-address', SkrReportedAddress()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrBankTransactionReportData(univ.SequenceOf):
    pass


SkrBankTransactionReportData.componentType = SkrBankTransactionRecord()


class SkrBroadbandWirelessParameters(univ.Sequence):
    pass


SkrBroadbandWirelessParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'azimuth',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(-1, 359))
        )
    ),
    namedtype.NamedType(
        'width',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 359))
        )
    ),
    namedtype.NamedType(
        'horizon-angle',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 359))
        )
    ),
    namedtype.OptionalNamedType(
        'power',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 25000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'frequency-start',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 10000000000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'frequency-stop',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 10000000000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.OptionalNamedType(
        'leaf-level',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(-45, 45))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.OptionalNamedType(
        'vertical-lift',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 100))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.OptionalNamedType(
        'gain-factor',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(-100, 100))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.OptionalNamedType(
        'polarization',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(-45, 45))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    )
)


class SkrWirelessAntenna(SkrBroadbandWirelessParameters):
    pass


class SkrBsCellType(univ.Enumerated):
    pass


SkrBsCellType.namedValues = namedval.NamedValues(
    ('macro', 0),
    ('micro', 1),
    ('pico', 2),
    ('femto', 3)
)


class SkrBsSetting(univ.Enumerated):
    pass


SkrBsSetting.namedValues = namedval.NamedValues(
    ('indoor', 0), ('outdoor', 1), ('underground', 2)
)


class SkrBsGeneration(univ.Enumerated):
    pass


SkrBsGeneration.namedValues = namedval.NamedValues(
    ('g2', 0), ('g3', 1), ('g4', 2), ('g5', 3)
)


class SkrGsmAntenna(univ.Sequence):
    pass


SkrGsmAntenna.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'azimut',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(-1, 359))
        )
    ),
    namedtype.NamedType(
        'width',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 359))
        )
    ),
    namedtype.NamedType(
        'horizon-angle',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 359))
        )
    ),
    namedtype.OptionalNamedType(
        'power',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 25000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'frequency',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 10000000000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'vertical-lift',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 100))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.OptionalNamedType(
        'gain-factor',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(-100, 100))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.OptionalNamedType(
        'polarization',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(-45, 45))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.OptionalNamedType(
        'setting',
        SkrBsSetting().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.OptionalNamedType(
        'thickness',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 359))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    ),
    namedtype.OptionalNamedType(
        'generation',
        SkrBsGeneration().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))
        )
    ),
    namedtype.OptionalNamedType(
        'controller-num',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))
        )
    ),
    namedtype.OptionalNamedType(
        'bcc-ncc',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))
        )
    ),
    namedtype.OptionalNamedType(
        'cell-type',
        SkrBsCellType().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'radiation-class',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))
        )
    ),
    namedtype.OptionalNamedType(
        'name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))
        )
    ),
    namedtype.OptionalNamedType(
        'channel',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class SkrCdmaAntenna(SkrBroadbandWirelessParameters):
    pass


class SkrBasicStationAntenna(univ.Choice):
    pass


SkrBasicStationAntenna.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'gsm-antenna',
        SkrGsmAntenna().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'cdma-antenna',
        univ.SequenceOf(
            componentType=(SkrCdmaAntenna())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'wireless-antenna',
        univ.SequenceOf(
            componentType=(SkrWirelessAntenna())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrIPPort(univ.OctetString):
    pass


SkrIPPort.subtypeSpec = constraint.ValueSizeConstraint(2, 2)


class SkrNetworkPeerInfo(univ.Sequence):
    pass


SkrNetworkPeerInfo.componentType = namedtype.NamedTypes(
    namedtype.NamedType('ip-address', SkrIPAddress()),
    namedtype.OptionalNamedType('ip-port', SkrIPPort())
)


class SkrIPList(univ.SequenceOf):
    pass


SkrIPList.componentType = SkrNetworkPeerInfo()


class SkrWirelessIdentifiers(univ.Sequence):
    pass


SkrWirelessIdentifiers.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'cell',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.OptionalNamedType('ip-list', SkrIPList()),
    namedtype.OptionalNamedType(
        'mac',
        univ.OctetString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(6, 6))
        )
    )
)


class SkrTelephoneIdentifiers(univ.Sequence):
    pass


SkrTelephoneIdentifiers.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'lac',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 65535))
        )
    ),
    namedtype.NamedType(
        'cell',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.OptionalNamedType(
        'cell-sign',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 18))
        )
    )
)


class SkrBasicStationIdentifiers(univ.Choice):
    pass


SkrBasicStationIdentifiers.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'telepone',
        SkrTelephoneIdentifiers().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'wireless',
        univ.SequenceOf(
            componentType=(SkrWirelessIdentifiers())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrBasicStationType(univ.Enumerated):
    pass


SkrBasicStationType.namedValues = namedval.NamedValues(
    ('gsm', 0),
    ('cdma', 1),
    ('umts', 2),
    ('wifi', 3),
    ('wimax', 4)
)


class SkrBasicStationSectorRecord(univ.Sequence):
    pass


SkrBasicStationSectorRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.NamedType('end-time', SkrDateAndTime()),
    namedtype.NamedType(
        'address',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType('sector-identifiers', SkrBasicStationIdentifiers()),
    namedtype.NamedType('antenna-configuration', SkrBasicStationAntenna()),
    namedtype.NamedType('station-type', SkrBasicStationType()),
    namedtype.OptionalNamedType(
        'structured-address',
        SkrReportedAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'location',
        SkrGeoLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class SkrBasicStationsSectorRecordsData(univ.SequenceOf):
    pass


SkrBasicStationsSectorRecordsData.componentType = SkrBasicStationSectorRecord()


class SkrBunch(univ.Choice):
    pass


SkrBunch.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'gsm',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'cdma-umts',
        SkrDataNetworkEquipment().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class SkrBunchMapPoint(univ.Sequence):
    pass


SkrBunchMapPoint.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType('bunch-id', SkrBunch())
)


class SkrBunchRecord(univ.Sequence):
    pass


SkrBunchRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('bunch-id', SkrBunch()),
    namedtype.NamedType(
        'switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType(
        'bunch-type',
        univ.Enumerated(
            namedValues=(
                namedval.NamedValues(
                    ('inbound', 0), ('outbound', 1), ('bidirectional', 3)
                )
            )
        )
    ),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.OptionalNamedType('end-time', SkrDateAndTime()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrBunchesMapRecord(univ.Sequence):
    pass


SkrBunchesMapRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('a-bunch', SkrBunchMapPoint()),
    namedtype.NamedType('b-bunch', SkrBunchMapPoint()),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.OptionalNamedType('end-time', SkrDateAndTime())
)


class SkrBunchesMapRecordsData(univ.SequenceOf):
    pass


SkrBunchesMapRecordsData.componentType = SkrBunchesMapRecord()


class SkrBunchesRecordsData(univ.SequenceOf):
    pass


SkrBunchesRecordsData.componentType = SkrBunchRecord()


class SkrCallsTypesRecord(univ.Sequence):
    pass


SkrCallsTypesRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'call-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.OptionalNamedType('end-time', SkrDateAndTime()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrCallTypesRecordsData(univ.SequenceOf):
    pass


SkrCallTypesRecordsData.componentType = SkrCallsTypesRecord()


class SkrCallsRecords(univ.Sequence):
    pass


SkrCallsRecords.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class SkrModuleId(univ.OctetString):
    pass


SkrModuleId.subtypeSpec = constraint.ValueSizeConstraint(8, 8)


class SkrRequestedHardwareModules(univ.SequenceOf):
    pass


SkrRequestedHardwareModules.componentType = SkrModuleId()


class SkrRequestedSoftwareModules(univ.SequenceOf):
    pass


SkrRequestedSoftwareModules.componentType = SkrModuleId()


class SkrRequestedModulesList(univ.Choice):
    pass


SkrRequestedModulesList.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'hw-modules',
        SkrRequestedHardwareModules().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'sw-modules',
        SkrRequestedSoftwareModules().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrCheckModuleRequest(SkrRequestedModulesList):
    pass


class SkrParameterValue(univ.Choice):
    pass


SkrParameterValue.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'string',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'integer',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 999999999))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'boolean',
        univ.Boolean().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrModuleParameter(univ.Sequence):
    pass


SkrModuleParameter.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'parameter-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType('read-only', univ.Boolean()),
    namedtype.NamedType('parameter-value', SkrParameterValue())
)


class SkrModuleParameters(univ.SequenceOf):
    pass


SkrModuleParameters.componentType = SkrModuleParameter()


class SkrSubmodulesList(univ.SequenceOf):
    pass


class SkrSormSoftwareModule(univ.Sequence):
    pass


SkrSubmodulesList.componentType = SkrSormSoftwareModule()
SkrSormSoftwareModule.componentType = namedtype.NamedTypes(
    namedtype.NamedType('module-id', SkrModuleId()),
    namedtype.NamedType('hardware-module-id', SkrModuleId()),
    namedtype.NamedType(
        'block-name',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1024))
        )
    ),
    namedtype.NamedType(
        'module-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    ),
    namedtype.NamedType(
        'module-type',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 512))
        )
    ),
    namedtype.NamedType('module-parameters', SkrModuleParameters()),
    namedtype.OptionalNamedType('sub-modules-list', SkrSubmodulesList())
)


class SkrSormSoftwareModules(univ.SequenceOf):
    pass


SkrSormSoftwareModules.componentType = SkrSormSoftwareModule()


class SkrHwParameterGroup(univ.Sequence):
    pass


SkrHwParameterGroup.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'group-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    ),
    namedtype.NamedType('module-parameters', SkrModuleParameters())
)


class SkrHwParameterGroups(univ.SequenceOf):
    pass


SkrHwParameterGroups.componentType = SkrHwParameterGroup()


class SkrSormHardwareModule(univ.Sequence):
    pass


SkrSormHardwareModule.componentType = namedtype.NamedTypes(
    namedtype.NamedType('module-id', SkrModuleId()),
    namedtype.NamedType(
        'block-name',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1024))
        )
    ),
    namedtype.NamedType(
        'module-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    ),
    namedtype.NamedType('module-parameters', SkrHwParameterGroups())
)


class SkrSormHardwareModules(univ.SequenceOf):
    pass


SkrSormHardwareModules.componentType = SkrSormHardwareModule()


class SkrCheckModuleResponse(univ.Choice):
    pass


SkrCheckModuleResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'hw-modules',
        SkrSormHardwareModules().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'sw-modules',
        SkrSormSoftwareModules().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrConfiguratedModule(univ.Choice):
    pass


SkrConfiguratedModule.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'sw-module',
        SkrSormSoftwareModule().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'hw-module',
        SkrSormHardwareModule().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class SkrConnectRequest(univ.Sequence):
    pass


SkrConnectRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'session-timeout',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(60, 2592000))
        )
    ),
    namedtype.NamedType(
        'max-data-length',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(10, 100000))
        )
    ),
    namedtype.NamedType(
        'data-packet-window-size',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(4, 256))
        )
    ),
    namedtype.NamedType(
        'data-load-timeout',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 60))
        )
    ),
    namedtype.NamedType(
        'request-response-timeout',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 60))
        )
    ),
    namedtype.NamedType(
        'data-packet-response-timeout',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 60))
        )
    ),
    namedtype.DefaultedNamedType(
        'time-offset',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(-1440, 1440))
        ).subtype(value=0)
    )
)


class SkrConnectResponse(univ.Sequence):
    pass


SkrConnectResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'confirmed-data-packet-window-size',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(4, 256))
        )
    ),
    namedtype.NamedType(
        'confirmed-session-timeout',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(60, 2592000))
        )
    ),
    namedtype.NamedType(
        'confirmed-data-load-timeout',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 60))
        )
    ),
    namedtype.NamedType(
        'confirmed-request-response-timeout',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 60))
        )
    ),
    namedtype.NamedType(
        'supports',
        univ.SequenceOf(componentType=(useful.ObjectDescriptor()))
    )
)


class SkrFindRange(univ.Sequence):
    pass


SkrFindRange.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType(
        'begin-find',
        SkrDateAndTime().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'end-find',
        SkrDateAndTime().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)
            )
        )
    )
)


class SkrStandardInterval(univ.Sequence):
    pass


SkrStandardInterval.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('standard', SkrNetworkType()),
    namedtype.NamedType('range', SkrFindRange()),
    namedtype.OptionalNamedType('count', univ.Integer())
)


class SkrConnectionsPresenseRecord(univ.Sequence):
    pass


SkrConnectionsPresenseRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('standard-interval', SkrStandardInterval()),
    namedtype.NamedType(
        'data-type',
        univ.Enumerated(namedValues=(namedval.NamedValues(
            ('telephone-pstn', 0),
            ('telephone-mobile', 1),
            ('pager', 2),
            ('data-aaa', 3),
            ('data-resource', 4),
            ('data-email', 5),
            ('data-im', 6),
            ('data-voip', 7),
            ('data-file', 8),
            ('data-term', 9),
            ('data-raw', 10),
            ('data-address-translations', 11)))
        )
    )
)


class SkrConnectionsPresenceData(univ.SequenceOf):
    pass


SkrConnectionsPresenceData.componentType = SkrConnectionsPresenseRecord()


class SkrConnectionsReport(SkrCallsRecords):
    pass


class SkrRequestedConnection(univ.Sequence):
    pass


SkrRequestedConnection.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class SkrVoipProtocol(univ.Enumerated):
    pass


SkrVoipProtocol.namedValues = namedval.NamedValues(
    ('sip', 0),
    ('h323', 1),
    ('iax', 2),
    ('skype', 100)
)


class SkrDataVoipNumber(univ.Sequence):
    pass


SkrDataVoipNumber.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'original-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    ),
    namedtype.OptionalNamedType(
        'translated-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'e164-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 15))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrRequestedVoipData(univ.Choice):
    pass


SkrRequestedVoipData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'client-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'server-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'duration',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 864000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'originator-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'call-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.NamedType(
        'voip-calling-number',
        SkrDataVoipNumber().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))
        )
    ),
    namedtype.NamedType(
        'voip-called-number',
        SkrDataVoipNumber().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7)
            )
        )
    ),
    namedtype.NamedType(
        'inbound-bunch',
        SkrBunch().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8)
            )
        )
    ),
    namedtype.NamedType(
        'outbound-bunch',
        SkrBunch().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9)
            )
        )
    ),
    namedtype.NamedType(
        'conference-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        ).subtype(implicitTag=(
            tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.NamedType(
        'protocol',
        SkrVoipProtocol().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))
        )
    ),
    namedtype.NamedType(
        'term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))
        )
    ),
    namedtype.NamedType(
        'abonent-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    ),
    namedtype.NamedType(
        'nat-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20)
            )
        )
    ),
    namedtype.NamedType(
        'location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21)
            )
        )
    )
)


class SkrRequestedConnectionMobileIdentifier(univ.Sequence):
    pass


SkrRequestedConnectionMobileIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class SkrPhoneAbonentType(univ.Enumerated):
    pass


SkrPhoneAbonentType.namedValues = namedval.NamedValues(
    ('local', 0),
    ('network', 1),
    ('roamer', 2),
    ('undefined', 3))


class SkrRecodedRequestedConnectionMobileIdentifier(univ.Choice):
    pass


SkrRecodedRequestedConnectionMobileIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'gsm-identifier',
        SkrRequestedGsmIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'cdma-identifier',
        SkrRequestedCdmaIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class SkrRequestedConnectionMobileData(univ.Choice):
    pass


SkrRequestedConnectionMobileData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'duration', univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 86399))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'call-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'supplement-service-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.NamedType(
        'in-abonent-type',
        SkrPhoneAbonentType().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'out-abonent-type',
        SkrPhoneAbonentType().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)
            )
        )
    ),
    namedtype.NamedType(
        'inbound-bunch',
        SkrBunch().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6)
            )
        )
    ),
    namedtype.NamedType(
        'outbound-bunch',
        SkrBunch().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7)
            )
        )
    ),
    namedtype.NamedType(
        'border-switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))
        )
    ),
    namedtype.NamedType(
        'roaming-partner-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))
        )
    ),
    namedtype.NamedType(
        'term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.NamedType(
        'in-info',
        SkrRequestedConnectionMobileIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-in-info',
        SkrRecodedRequestedConnectionMobileIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 111)
            )
        )
    ),
    namedtype.NamedType(
        'in-end-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12)
            )
        )
    ),
    namedtype.NamedType(
        'in-begin-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 13)
            )
        )
    ),
    namedtype.NamedType(
        'dialed-digits',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))
        )
    ),
    namedtype.NamedType(
        'out-info',
        SkrRequestedConnectionMobileIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-out-info',
        SkrRecodedRequestedConnectionMobileIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 115)
            )
        )
    ),
    namedtype.NamedType(
        'out-begin-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16)
            )
        )
    ),
    namedtype.NamedType(
        'out-end-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 17)
            )
        )
    ),
    namedtype.NamedType(
        'forwarding-identifier',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 18))
        )
    ),
    namedtype.NamedType(
        'message',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 40))
        )
    )
)


class SkrRequestedAddressTranslationsData(univ.Choice):
    pass


SkrRequestedAddressTranslationsData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'record-type',
        univ.Enumerated(
            namedValues=(namedval.NamedValues(
                ('session-start', 0),
                ('session-end', 1)
            ))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.NamedType(
        'private-ip',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.NamedType(
        'public-ip',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
            )
        )
    ),
    namedtype.NamedType(
        'destination-ip',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)
            )
        )
    ),
    namedtype.NamedType(
        'translation-type',
        univ.Enumerated(
            namedValues=(namedval.NamedValues(
                ('static-nat', 0),
                ('dynamic-nat', 1),
                ('source-nat', 2),
                ('destination-nat', 3),
                ('pat', 4)
            ))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    )
)


class SkrRequestedFileTransferData(univ.Choice):
    pass


SkrRequestedFileTransferData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'client-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'server-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'server-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'user-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'user-password',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.NamedType(
        'term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 16384))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    ),
    namedtype.NamedType(
        'abonent-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        ).subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7)
            )
        )
    ),
    namedtype.NamedType(
        'nat-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20)
            )
        )
    ), namedtype.NamedType(
        'location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21)
            )
        )
    )
)


class SkrRequestedConnectionPstnIdentifier(univ.Sequence):
    pass


SkrRequestedConnectionPstnIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', SkrRequestedPstnIdentifier())
)


class SkrRequestedConnectionPstnData(univ.Choice):
    pass


SkrRequestedConnectionPstnData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'duration', univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 86399))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'call-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'in-abonent-type',
        SkrPhoneAbonentType().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.NamedType(
        'out-abonent-type',
        SkrPhoneAbonentType().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'inbound-bunch',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))
    ),
    namedtype.NamedType(
        'outbound-bunch',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    ),
    namedtype.NamedType(
        'border-switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))
        )
    ),
    namedtype.NamedType(
        'term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))
        )
    ),
    namedtype.NamedType(
        'supplement-service-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))
        )
    ),
    namedtype.NamedType(
        'phone-card-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 20))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.NamedType(
        'in-info',
        SkrRequestedConnectionPstnIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.NamedType(
        'out-info',
        SkrRequestedConnectionPstnIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12)
            )
        )
    ),
    namedtype.NamedType(
        'forwarding-identifier',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    ),
    namedtype.NamedType(
        'message',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 20))
        )
    )
)


class SkrRequestedTermAccessData(univ.Choice):
    pass


SkrRequestedTermAccessData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'client-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'server-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'abonent-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'nat-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10)
            )
        )
    ),
    namedtype.NamedType(
        'location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.NamedType(
        'sni',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class SkrRequestedRawFlowsData(univ.Choice):
    pass


SkrRequestedRawFlowsData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))
    ),
    namedtype.NamedType(
        'protocol-code',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 65535))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'client-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'server-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.NamedType(
        'abonent-id',
        char.UTF8String().subtype(
            subtypeSpec=(
                constraint.ValueSizeConstraint(0, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'nat-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10)
            )
        )
    ),
    namedtype.NamedType(
        'location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.NamedType(
        'sni',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class SkrRequestedAAALoginData(univ.Choice):
    pass


SkrRequestedAAALoginData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'login-type',
        univ.Enumerated(
            namedValues=(namedval.NamedValues(
                ('connect', 0),
                ('disconnect', 1),
                ('update', 2))
            )
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'user-equipment',
        SkrDataNetworkEquipment().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'allocated-ip',
        SkrIPAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.NamedType(
        'user-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))
    ),
    namedtype.NamedType(
        'user-password',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.NamedType(
        'connect-type',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 65535))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    ),
    namedtype.NamedType(
        'calling-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))
        )
    ),
    namedtype.NamedType(
        'called-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))
        )
    ),
    namedtype.NamedType(
        'nas',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9)
            )
        )
    ),
    namedtype.NamedType(
        'apn',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.NamedType(
        'sgsn-ip',
        SkrIPAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.NamedType(
        'ggsn-ip',
        SkrIPAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12)
            )
        )
    ),
    namedtype.NamedType(
        'service-area-code',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 65535))
        ).subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13)
            )
        )
    ),
    namedtype.NamedType(
        'location-start',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14)
            )
        )
    ),
    namedtype.NamedType(
        'location-end',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15)
            )
        )
    ),
    namedtype.NamedType(
        'phone-card-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(20, 20))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 16))
        )
    ),
    namedtype.NamedType(
        'imsi',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 17))
        )
    ),
    namedtype.NamedType(
        'imei',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 18))
        )
    ),
    namedtype.NamedType(
        'esn',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 19))
        )
    ),
    namedtype.NamedType(
        'pool-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 20))
        )
    ),
    namedtype.NamedType(
        'mcc',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 21))
        )
    ),
    namedtype.NamedType(
        'mnc',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 22))
        )
    )
)


class SkrRequestedEmailData(univ.Choice):
    pass


SkrRequestedEmailData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'client-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'server-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'sender',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'receiver',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'cc',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.NamedType(
        'subject',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 2048))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6)))
    ),
    namedtype.NamedType(
        'attachements',
        univ.Boolean().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7)))
    ),
    namedtype.NamedType(
        'mail-server',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8)))
    ),
    namedtype.NamedType(
        'term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9)))
    ),
    namedtype.NamedType(
        'abonent-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10)))
    ),
    namedtype.NamedType(
        'message',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 20))
        )
    ),
    namedtype.NamedType(
        'nat-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21)
            )
        )
    ),
    namedtype.NamedType(
        'location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22)
            )
        )
    )
)


class SkrRequestedConnectionEntranceData(univ.Choice):
    pass


SkrRequestedConnectionEntranceData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'directory-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'imsi',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'ip-address',
        SkrIPAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'mac',
        univ.OctetString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(6, 6))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    )
)


class SkrHttpMethod(univ.Enumerated):
    pass


SkrHttpMethod.namedValues = namedval.NamedValues(
    ('get', 0),
    ('post', 1),
    ('put', 2),
    ('delete', 3)
)


class SkrRequestedResourceData(univ.Choice):
    pass


SkrRequestedResourceData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'client-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'server-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'url',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 8192))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'http-method',
        SkrHttpMethod().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.NamedType(
        'abonent-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    ),
    namedtype.NamedType(
        'nat-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10)
            )
        )
    ),
    namedtype.NamedType(
        'location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    )
)


class SkrIMProtocol(univ.Enumerated):
    pass


SkrIMProtocol.namedValues = namedval.NamedValues(
    ('icq', 0),
    ('aol', 1),
    ('msn', 2),
    ('yahoo', 3),
    ('web-mail', 4),
    ('skype', 5),
    ('irc', 6),
    ('jabber', 7),
    ('mra', 8),
    ('tencent', 9),
    ('airway', 10),
    ('mms', 98),
    ('sms', 99),
    ('vk', 100),
    ('facebook', 101),
    ('myspace', 102),
    ('twitter', 103),
    ('odnoklassniki', 104),
    ('moymir', 105),
    ('zello', 106)
)


class SkrRequestedImData(univ.Choice):
    pass


SkrRequestedImData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'client-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'server-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ), namedtype.NamedType(
        'user-login',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'user-password',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'sender-screen-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.NamedType(
        'sender-uin',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    ),
    namedtype.NamedType(
        'receiver-screen-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7)))
    ),
    namedtype.NamedType(
        'receiver-uin',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8)))
    ),
    namedtype.NamedType(
        'protocol',
        SkrIMProtocol().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9)))
    ),
    namedtype.NamedType(
        'term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.NamedType(
        'abonent-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))
        )
    ),
    namedtype.NamedType(
        'message',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 20))
        )
    ),
    namedtype.NamedType(
        'nat-info',
        SkrNetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21)
            )
        )
    ),
    namedtype.NamedType(
        'location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22)
            )
        )
    )
)


class SkrRecodedRequestedConnection(univ.Choice):
    pass


SkrRecodedRequestedConnection.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'pager-identifier',
        SkrRequestedPagerIdentifier().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'pstn',
        SkrRequestedConnectionPstnData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'mobile',
        SkrRequestedConnectionMobileData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'entrance',
        SkrRequestedConnectionEntranceData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ), namedtype.NamedType(
        'aaa-login',
        SkrRequestedAAALoginData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
            )
        )
    ),
    namedtype.NamedType(
        'resource',
        SkrRequestedResourceData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)
            )
        )
    ),
    namedtype.NamedType(
        'email',
        SkrRequestedEmailData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6)
            )
        )
    ),
    namedtype.NamedType(
        'im',
        SkrRequestedImData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7)
            )
        )
    ),
    namedtype.NamedType(
        'voip',
        SkrRequestedVoipData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8)
            )
        )
    ),
    namedtype.NamedType(
        'file-transfer',
        SkrRequestedFileTransferData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9)
            )
        )
    ),
    namedtype.NamedType(
        'term-access',
        SkrRequestedTermAccessData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10)
            )
        )
    ),
    namedtype.NamedType(
        'raw-flows',
        SkrRequestedRawFlowsData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.NamedType(
        'address-translations',
        SkrRequestedAddressTranslationsData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12)
            )
        )
    )
)


class SkrRequestedConnectionParameter(univ.Choice):
    pass


SkrRequestedConnectionParameter.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        SkrLogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'find-mask',
        SkrRequestedConnection().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-find-mask',
        SkrRecodedRequestedConnection().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 101)
            )
        )
    )
)


class SkrRequestedConnectionIdentifiers(univ.SequenceOf):
    pass


SkrRequestedConnectionIdentifiers.componentType = SkrRequestedConnectionParameter()


class SkrValidateEntranceTask(SkrRequestedConnectionIdentifiers):
    pass


class SkrValidateDataTask(SkrRequestedConnectionIdentifiers):
    pass


class SkrValidateConnectionsTask(SkrRequestedConnectionIdentifiers):
    pass


class SkrConnectionsTask(univ.Choice):
    pass


SkrConnectionsTask.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'validate-connections',
        SkrValidateConnectionsTask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'validate-data',
        SkrValidateDataTask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'validate-entrance',
        SkrValidateEntranceTask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrControlCommandType(univ.Enumerated):
    pass


SkrControlCommandType.namedValues = namedval.NamedValues(
    ('start', 0),
    ('stop', 1)
)


class SkrPortRange(univ.Sequence):
    pass


SkrPortRange.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'port-from',
        SkrIPPort().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'port-to',
        SkrIPPort().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrIPV6Mask(univ.OctetString):
    pass


SkrIPV6Mask.subtypeSpec = constraint.ValueSizeConstraint(16, 16)


class SkrIPV4Mask(univ.OctetString):
    pass


SkrIPV4Mask.subtypeSpec = constraint.ValueSizeConstraint(4, 4)


class SkrIPMask(univ.Choice):
    pass


SkrIPMask.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'ipv4-mask',
        SkrIPV4Mask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'ipv6-mask',
        SkrIPV6Mask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrIPFilterMask(univ.Sequence):
    pass


SkrIPFilterMask.componentType = namedtype.NamedTypes(
    namedtype.NamedType('mask', SkrIPMask()),
    namedtype.NamedType('mask-length', univ.Integer())
)


class SkrFilterSingleCriteria(univ.Choice):
    pass


SkrFilterSingleCriteria.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'ip-address',
        SkrIPAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'ip-port',
        SkrIPPort().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'port-range',
        SkrPortRange().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'vlan',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4096))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'mac',
        univ.OctetString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(6, 6))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))
    ),
    namedtype.NamedType(
        'mpls-tag',
        univ.Integer().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.NamedType(
        'sni',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    ),
    namedtype.NamedType(
        'http-content-type',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))
        )
    ),
    namedtype.NamedType(
        'protocol-group',
        univ.Integer().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))
        )
    ),
    namedtype.NamedType(
        'ip-protocol-number',
        univ.Integer().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))
        )
    ),
    namedtype.NamedType(
        'http-cookie',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.NamedType(
        'http-uri',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))
        )
    ),
    namedtype.NamedType(
        'ip-mask',
        SkrIPFilterMask().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12)
            )
        )
    )
)


class SkrFilterPairCriteria(univ.Sequence):
    pass


SkrFilterPairCriteria.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'criteria-a',
        SkrFilterSingleCriteria().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'criteria-b',
        SkrFilterSingleCriteria().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class SkrFilterParameter(univ.Choice):
    pass


SkrFilterParameter.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'single-criteria',
        SkrFilterSingleCriteria().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'pair-criteria',
        SkrFilterPairCriteria().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class SkrFilterParameters(univ.SequenceOf):
    pass


SkrFilterParameters.componentType = SkrFilterParameter()


class SkrFilterID(univ.Integer):
    pass


class SkrCreateFilterRequest(univ.Sequence):
    pass


SkrCreateFilterRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType('filter-id', SkrFilterID()),
    namedtype.NamedType('filter-parameters', SkrFilterParameters()),
    namedtype.DefaultedNamedType(
        'allow-only-mode', univ.Boolean().subtype(value=1)
    )
)


class SkrCreateFilterResponse(univ.Sequence):
    pass


SkrCreateFilterResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('filter-id', SkrFilterID()),
    namedtype.NamedType('successful', univ.Boolean()),
    namedtype.OptionalNamedType(
        'error-description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrTelcoList(univ.SequenceOf):
    pass


SkrTelcoList.componentType = SkrTelcoID()


class SkrDataContentID(char.UTF8String):
    pass


SkrDataContentID.subtypeSpec = constraint.ValueSizeConstraint(1, 512)


class SkrDataContentTask(SkrDataContentID):
    pass


class SkrPaymentsTask(univ.Sequence):
    pass


SkrPaymentsTask.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class SkrRequestedServiceCenterPaysParameters(univ.Choice):
    pass


SkrRequestedServiceCenterPaysParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        SkrLogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'center-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'center-address',
        SkrRequestedAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    )
)


class SkrRequestedServiceCenterPays(univ.SequenceOf):
    pass


SkrRequestedServiceCenterPays.componentType = SkrRequestedServiceCenterPaysParameters()


class SkrRequestedTransferParameters(univ.Choice):
    pass


SkrRequestedTransferParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        SkrLogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'source-identifier',
        SkrRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-source-identifier',
        SkrRecodedRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 101)
            )
        )
    )
)


class SkrRequestedBankDivisionTransferPays(univ.SequenceOf):
    pass


SkrRequestedBankDivisionTransferPays.componentType = SkrRequestedTransferParameters()


class SkrRequestedBankTransactionPaysParameters(univ.Choice):
    pass


SkrRequestedBankTransactionPaysParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        SkrLogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'bank-account',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))
    ),
    namedtype.NamedType(
        'bank-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrRequestedBankTransactionPays(univ.SequenceOf):
    pass


SkrRequestedBankTransactionPays.componentType = SkrRequestedBankTransactionPaysParameters()


class SkrRequestedExpressPaysParameters(univ.Choice):
    pass


SkrRequestedExpressPaysParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        SkrLogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'express-card',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 20))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrRequestedExpressPays(univ.SequenceOf):
    pass


SkrRequestedExpressPays.componentType = SkrRequestedExpressPaysParameters()


class SkrRequestedCrossAccountPaysParameters(univ.Choice):
    pass


SkrRequestedCrossAccountPaysParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        SkrLogicalOperation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)
            )
        )
    ),
    namedtype.NamedType(
        'source-identifier',
        SkrRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'dest-identifier',
        SkrRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-source-identifier',
        SkrRecodedRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 101)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-dest-identifier',
        SkrRecodedRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102)
            )
        )
    )
)


class SkrRequestedCrossAccountPays(univ.SequenceOf):
    pass


SkrRequestedCrossAccountPays.componentType = SkrRequestedCrossAccountPaysParameters()


class SkrRequestedBankAccountTransferPays(univ.SequenceOf):
    pass


SkrRequestedBankAccountTransferPays.componentType = SkrRequestedTransferParameters()


class SkrRequestedTerminalPaysParameters(univ.Choice):
    pass


SkrRequestedTerminalPaysParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        SkrLogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'terminal-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'terminal-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 20))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.NamedType(
        'terminal-address',
        SkrRequestedAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    )
)


class SkrRequestedTerminalPays(univ.SequenceOf):
    pass


SkrRequestedTerminalPays.componentType = SkrRequestedTerminalPaysParameters()


class SkrRequestedBalanceFillupsParameters(univ.Choice):
    pass


SkrRequestedBalanceFillupsParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        SkrLogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'identifier',
        SkrRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-identifier',
        SkrRecodedRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 101)
            )
        )
    )
)


class SkrRequestedBalanceFillups(univ.SequenceOf):
    pass


SkrRequestedBalanceFillups.componentType = SkrRequestedBalanceFillupsParameters()


class SkrRequestedTelephoneCardPaysParameters(univ.Choice):
    pass


SkrRequestedTelephoneCardPaysParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        SkrLogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'card-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 20))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrRequestedTelephoneCardPays(univ.SequenceOf):
    pass


SkrRequestedTelephoneCardPays.componentType = SkrRequestedTelephoneCardPaysParameters()


class SkrRequestedBankCardTransferPays(univ.SequenceOf):
    pass


SkrRequestedBankCardTransferPays.componentType = SkrRequestedTransferParameters()


class SkrRecodedPaymentsTask(univ.Choice):
    pass


SkrRecodedPaymentsTask.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'bank-transaction',
        SkrRequestedBankTransactionPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'express-card',
        SkrRequestedExpressPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'public-terminal',
        SkrRequestedTerminalPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.NamedType(
        'service-center',
        SkrRequestedServiceCenterPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'cross-account',
        SkrRequestedCrossAccountPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'telephone-card',
        SkrRequestedTelephoneCardPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.NamedType(
        'balance-fill-up',
        SkrRequestedBalanceFillups().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    ),
    namedtype.NamedType(
        'bank-division-transfer',
        SkrRequestedBankDivisionTransferPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))
        )
    ),
    namedtype.NamedType(
        'bank-card-transfer',
        SkrRequestedBankCardTransferPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))
        )
    ),
    namedtype.NamedType(
        'bank-account-transfer',
        SkrRequestedBankAccountTransferPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))
        )
    )
)


class SkrDictionaryTask(univ.Sequence):
    pass


SkrDictionaryTask.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', useful.ObjectDescriptor())
)


class SkrPresenseInfoData(univ.Enumerated):
    pass


SkrPresenseInfoData.namedValues = namedval.NamedValues(
    ('subscribers', 0),
    ('connections', 1),
    ('payments', 2),
    ('dictionaries', 3),
    ('locations', 4)
)


class SkrPresenseTask(univ.Sequence):
    pass


SkrPresenseTask.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', SkrPresenseInfoData())
)


class SkrRequestedLocationIdentifier(univ.Choice):
    pass


SkrRequestedLocationIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'directory-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'imsi',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'ip-address',
        SkrIPAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'imei',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    )
)


class SkrLocationTask(SkrRequestedLocationIdentifier):
    pass


class SkrCreateTaskRequest(univ.Sequence):
    pass


SkrCreateTaskRequest.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType(
        'telcos', SkrTelcoList().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'range',
        SkrFindRange().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'report-limit',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 10000000))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.NamedType(
        'task',
        univ.Choice(
            componentType=(
                namedtype.NamedTypes(
                    namedtype.NamedType(
                        'dictionary',
                        SkrDictionaryTask().subtype(
                            implicitTag=(
                                tag.Tag(
                                    tag.tagClassContext,
                                    tag.tagFormatConstructed,
                                    0
                                )
                            )
                        )
                    ),
                    namedtype.NamedType(
                        'abonents',
                        SkrAbonentsTask().subtype(
                            implicitTag=(
                                tag.Tag(
                                    tag.tagClassContext,
                                    tag.tagFormatConstructed,
                                    1
                                )
                            )
                        )
                    ),
                    namedtype.NamedType(
                        'connections',
                        SkrConnectionsTask().subtype(
                            implicitTag=(
                                tag.Tag(
                                    tag.tagClassContext,
                                    tag.tagFormatConstructed,
                                    2)
                            )
                        )
                    ),
                    namedtype.NamedType(
                        'location',
                        SkrLocationTask().subtype(
                            implicitTag=(
                                tag.Tag(
                                    tag.tagClassContext,
                                    tag.tagFormatConstructed,
                                    3
                                )
                            )
                        )
                    ),
                    namedtype.NamedType(
                        'payments',
                        SkrPaymentsTask().subtype(
                            implicitTag=(
                                tag.Tag(
                                    tag.tagClassContext,
                                    tag.tagFormatConstructed,
                                    4
                                )
                            )
                        )
                    ),
                    namedtype.NamedType(
                        'presense',
                        SkrPresenseTask().subtype(
                            implicitTag=(
                                tag.Tag(
                                    tag.tagClassContext,
                                    tag.tagFormatConstructed,
                                    6
                                )
                            )
                        )
                    ),
                    namedtype.NamedType(
                        'data-content',
                        SkrDataContentTask().subtype(
                            implicitTag=(
                                tag.Tag(
                                    tag.tagClassContext,
                                    tag.tagFormatSimple,
                                    9
                                )
                            )
                        )
                    ),
                    namedtype.NamedType(
                        'recoded-payments',
                        SkrRecodedPaymentsTask().subtype(
                            implicitTag=(
                                tag.Tag(
                                    tag.tagClassContext,
                                    tag.tagFormatConstructed,
                                    104
                                )
                            )
                        )
                    )
                )
            )
        ).subtype(
            explicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    )
)


class SkrTaskID(univ.Integer):
    pass


SkrTaskID.subtypeSpec = constraint.ValueRangeConstraint(0, 4294967295)


class SkrCreateTaskResponse(univ.Sequence):
    pass


SkrCreateTaskResponse.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('task-id', SkrTaskID()),
    namedtype.NamedType('successful', univ.Boolean()),
    namedtype.OptionalNamedType(
        'error-description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrCrossAccountRecord(univ.Sequence):
    pass


SkrCrossAccountRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('device-id', SkrReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType('donanted-id', SkrReportedIdentifier()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrCrossAccountReportData(univ.SequenceOf):
    pass


SkrCrossAccountReportData.componentType = SkrCrossAccountRecord()


class SkrDataAAARecordContent(univ.Sequence):
    pass


SkrDataAAARecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        )
    ),
    namedtype.NamedType('aaa-connection-time', SkrDateAndTime()),
    namedtype.NamedType(
        'aaa-login-type',
        univ.Enumerated(namedValues=(namedval.NamedValues(
            ('connect', 0),
            ('disconnect', 1),
            ('lac-update', 2)))
        )
    ),
    namedtype.NamedType(
        'aaa-session-id', char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType('aaa-allocated-ip', SkrIPAddress()),
    namedtype.NamedType(
        'aaa-user-name', char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType(
        'aaa-connect-type',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 65535))
        )
    ),
    namedtype.NamedType(
        'aaa-calling-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        )
    ),
    namedtype.NamedType(
        'aaa-called-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        )
    ),
    namedtype.NamedType('aaa-nas', SkrNetworkPeerInfo()),
    namedtype.NamedType('aaa-in-bytes-count', univ.Integer()),
    namedtype.NamedType('aaa-out-bytes-count', univ.Integer()),
    namedtype.OptionalNamedType(
        'aaa-user-password',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))
    ),
    namedtype.OptionalNamedType(
        'aaa-user-equipment',
        SkrDataNetworkEquipment().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'aaa-apn',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))
    ),
    namedtype.OptionalNamedType(
        'aaa-sgsn-ip',
        SkrIPAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'aaa-ggsn-ip',
        SkrIPAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'aaa-service-area-code',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 65535))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))
    ),
    namedtype.OptionalNamedType(
        'aaa-location-start',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'aaa-location-end',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'phone-card-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(20, 20))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8)))
    ),
    namedtype.OptionalNamedType(
        'aaa-imsi',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9)))
    ),
    namedtype.OptionalNamedType(
        'aaa-imei',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'aaa-esn',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(10, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))
        )
    ),
    namedtype.OptionalNamedType(
        'aaa-pool-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))
        )
    ),
    namedtype.OptionalNamedType(
        'aaa-mcc',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    ),
    namedtype.OptionalNamedType(
        'aaa-mnc',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 14))
        )
    ),
    namedtype.OptionalNamedType(
        'aaa-allocated-ip-mask',
        SkrIPMask().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15)
            )
        )
    )
)


class SkrDataAAARecordData(univ.SequenceOf):
    pass


SkrDataAAARecordData.componentType = SkrDataAAARecordContent()


class SkrDataAddressTranslationRecordContent(univ.Sequence):
    pass


SkrDataAddressTranslationRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        )
    ),
    namedtype.NamedType('translation-time', SkrDateAndTime()),
    namedtype.NamedType(
        'record-type',
        univ.Enumerated(
            namedValues=(
                namedval.NamedValues(('session-start', 0), ('session-end', 1))
            )
        )
    ),
    namedtype.NamedType('private-ip', SkrNetworkPeerInfo()),
    namedtype.NamedType('public-ip', SkrNetworkPeerInfo()),
    namedtype.NamedType('destination-ip', SkrNetworkPeerInfo()),
    namedtype.NamedType(
        'translation-type',
        univ.Enumerated(
            namedValues=(
                namedval.NamedValues(
                    ('static-nat', 0),
                    ('dynamic-nat', 1),
                    ('source-nat', 2),
                    ('destination-nat', 3),
                    ('pat', 4)
                )
            )
        )
    )
)


class SkrDataAddressTranslationRecordData(univ.SequenceOf):
    pass


SkrDataAddressTranslationRecordData.componentType = SkrDataAddressTranslationRecordContent()


class SkrDataContentRawDirection(univ.Enumerated):
    pass


SkrDataContentRawDirection.namedValues = namedval.NamedValues(
    ('client-server', 0),
    ('server-client', 1)
)


class SkrDataContentReport(univ.Sequence):
    pass


SkrDataContentReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class SkrDataDropRequest(SkrTaskID):
    pass


class SkrDataDropResponse(univ.Sequence):
    pass


SkrDataDropResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('task-id', SkrTaskID()),
    namedtype.NamedType('successful', univ.Boolean()),
    namedtype.OptionalNamedType(
        'error-description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrEmailEvent(univ.Enumerated):
    pass


SkrEmailEvent.namedValues = namedval.NamedValues(
    ('email-send', 1),
    ('email-receive', 2),
    ('email-download', 3),
    ('email-logon-attempt', 4),
    ('email-logon', 5),
    ('email-logon-failure', 6),
    ('email-logoff', 7),
    ('email-partial-download', 8)
)


class SkrIP_AAAResult(univ.Enumerated):
    pass


SkrIP_AAAResult.namedValues = namedval.NamedValues(
    ('aaaUnknown', 1),
    ('aaaFailed', 2),
    ('aaaSucceeded', 3)
)


class SkrIP_AAAInformation(univ.Sequence):
    pass


SkrIP_AAAInformation.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'username',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        )
    ),
    namedtype.OptionalNamedType('aaaResult', SkrIP_AAAResult()))


class SkrDataNetworkCdrHeaderData(univ.Sequence):
    pass


SkrDataNetworkCdrHeaderData.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('begin-connection-time', SkrDateAndTime()),
    namedtype.NamedType('end-connection-time', SkrDateAndTime()),
    namedtype.NamedType('client-info', SkrNetworkPeerInfo()),
    namedtype.NamedType('server-info', SkrNetworkPeerInfo()),
    namedtype.NamedType(
        'protocol-code',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 65535))
        )
    ),
    namedtype.OptionalNamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        )
    )
)


class SkrDataNetworkCdrHeader(univ.Sequence):
    pass


SkrDataNetworkCdrHeader.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', SkrDataNetworkCdrHeaderData())
)


class SkrDataEmailRecordContentAAA(univ.Sequence):
    pass


SkrDataEmailRecordContentAAA.componentType = namedtype.NamedTypes(
    namedtype.NamedType('mail-cdr-header', SkrDataNetworkCdrHeader()),
    namedtype.NamedType('mail-event', SkrEmailEvent()),
    namedtype.NamedType('mail-aaa-info', SkrIP_AAAInformation()),
    namedtype.OptionalNamedType(
        'mail-message',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'mail-nat-info',
        univ.SequenceOf(
            componentType=(SkrNetworkPeerInfo())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))
        )
    ),
    namedtype.OptionalNamedType(
        'mail-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'mail-data-content-id',
        SkrDataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class SkrEmailServers(univ.Sequence):
    pass


SkrEmailServers.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'data',
        univ.SequenceOf(
            componentType=char.UTF8String().subtype(
                subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
            )
        )
    )
)


class SkrEmailReceivers(univ.Sequence):
    pass


SkrEmailReceivers.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'data',
        univ.SequenceOf(
            componentType=char.UTF8String().subtype(
                subtypeSpec=(constraint.ValueSizeConstraint(1, 512)))
        )
    )
)


class SkrDataEmailRecordContentIPDR(univ.Sequence):
    pass


SkrDataEmailRecordContentIPDR.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'mail-cdr-header',
        SkrDataNetworkCdrHeader()
    ),
    namedtype.NamedType('mail-event', SkrEmailEvent()),
    namedtype.NamedType(
        'mail-sender',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    ),
    namedtype.NamedType('mail-receiver', SkrEmailReceivers()),
    namedtype.NamedType('mail-cc', SkrEmailReceivers()),
    namedtype.NamedType(
        'mail-subject',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 2048))
        )
    ),
    namedtype.NamedType(
        'mail-size',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType(
        'attachements',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1))
        )
    ),
    namedtype.NamedType('mail-servers', SkrEmailServers()),
    namedtype.NamedType(
        'mail-term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        )
    ),
    namedtype.OptionalNamedType(
        'mail-reply-to',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.OptionalNamedType(
        'mail-protocol',
        univ.Enumerated(namedValues=(namedval.NamedValues(
            ('smtp', 0),
            ('pop3', 1),
            ('imap', 2),
            ('web-mail', 3)))
        )
    ),
    namedtype.OptionalNamedType(
        'mail-abonent-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))
    ),
    namedtype.OptionalNamedType(
        'mail-message',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'mail-nat-info',
        univ.SequenceOf(
            componentType=(SkrNetworkPeerInfo())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))
        )
    ),
    namedtype.OptionalNamedType(
        'mail-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'mail-data-content-id',
        SkrDataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class SkrDataEmailRecordContent(univ.Choice):
    pass


SkrDataEmailRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'mail-aaa',
        SkrDataEmailRecordContentAAA().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'mail-ipdr',
        SkrDataEmailRecordContentIPDR().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class SkrDataEmailRecordData(univ.SequenceOf):
    pass


SkrDataEmailRecordData.componentType = SkrDataEmailRecordContent()


class SkrDataFileTransferRecordContent(univ.Sequence):
    pass


SkrDataFileTransferRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'file-cdr-header',
        SkrDataNetworkCdrHeader()
    ),
    namedtype.NamedType(
        'file-server-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType(
        'file-user-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 128))
        )
    ),
    namedtype.NamedType(
        'file-user-password',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 256))
        )
    ),
    namedtype.OptionalNamedType(
        'file-server-type', univ.Boolean()
    ),
    namedtype.NamedType(
        'file-in-bytes-count', univ.Integer()
    ),
    namedtype.NamedType('file-out-bytes-count', univ.Integer()),
    namedtype.NamedType(
        'file-term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        )
    ),
    namedtype.OptionalNamedType(
        'file-abonent-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'file-nat-info',
        univ.SequenceOf(
            componentType=(SkrNetworkPeerInfo())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'file-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'file-data-content-id',
        SkrDataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))
        )
    )
)


class SkrDataFileTransferRecordData(univ.SequenceOf):
    pass


SkrDataFileTransferRecordData.componentType = SkrDataFileTransferRecordContent()


class SkrImReceiver(univ.Sequence):
    pass


SkrImReceiver.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'im-receiver-screen-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType(
        'im-receiver-uin',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrImReceivers(univ.SequenceOf):
    pass


SkrImReceivers.componentType = SkrImReceiver()


class SkrImEvent(univ.Enumerated):
    pass


SkrImEvent.namedValues = namedval.NamedValues(
    ('im-undefined', 0),
    ('im-send', 1),
    ('im-receive', 2)
)


class SkrDataImRecordContent(univ.Sequence):
    pass


SkrDataImRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('im-cdr-header', SkrDataNetworkCdrHeader()),
    namedtype.NamedType(
        'im-user-login',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType(
        'im-user-password',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType(
        'im-sender-screen-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType(
        'im-sender-uin',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType('im-receivers', SkrImReceivers()),
    namedtype.NamedType(
        'im-size',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType(
        'im-term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        )
    ),
    namedtype.OptionalNamedType(
        'im-protocol',
        SkrIMProtocol().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'im-abonent-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))
    ),
    namedtype.OptionalNamedType(
        'im-event',
        SkrImEvent().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.OptionalNamedType(
        'im-message',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'im-nat-info',
        univ.SequenceOf(
            componentType=(SkrNetworkPeerInfo())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))
        )
    ),
    namedtype.OptionalNamedType(
        'im-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'im-data-content-id',
        SkrDataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class SkrDataImRecordData(univ.SequenceOf):
    pass


SkrDataImRecordData.componentType = SkrDataImRecordContent()


class SkrDataInterruptRequest(SkrTaskID):
    pass


class SkrMessageID(univ.Integer):
    pass


SkrMessageID.subtypeSpec = constraint.ValueRangeConstraint(0, 4294967295)


class SkrDataInterruptResponse(univ.Sequence):
    pass


SkrDataInterruptResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('request-id', SkrMessageID()),
    namedtype.NamedType('successful', univ.Boolean()),
    namedtype.OptionalNamedType(
        'data-blocks-available',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 999999999999))
        )
    ),
    namedtype.OptionalNamedType(
        'error-description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrDataLoadRequest(SkrTaskID):
    pass


class SkrDataLoadResponse(univ.Sequence):
    pass


SkrDataLoadResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('task-id', SkrTaskID()),
    namedtype.NamedType('data-exists', univ.Boolean()),
    namedtype.OptionalNamedType(
        'data-blocks-number',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 999999999999))
        )
    ),
    namedtype.OptionalNamedType(
        'error-description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrDataRawFlowsRecordContent(univ.Sequence):
    pass


SkrDataRawFlowsRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('flow-cdr-header', SkrDataNetworkCdrHeader()),
    namedtype.NamedType('flow-in-bytes-count', univ.Integer()),
    namedtype.NamedType('flow-out-bytes-count', univ.Integer()),
    namedtype.OptionalNamedType(
        'flow-protocol',
        univ.Enumerated(namedValues=(namedval.NamedValues(
            ('ip', 0),
            ('udp', 1),
            ('tcp', 2)))
        )
    ),
    namedtype.OptionalNamedType(
        'flow-abonent-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'flow-nat-info',
        univ.SequenceOf(
            componentType=(SkrNetworkPeerInfo())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'flow-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'flow-data-content-id',
        SkrDataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))
        )
    ),
    namedtype.OptionalNamedType(
        'sni',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class SkrDataRawFlowsRecordData(univ.SequenceOf):
    pass


SkrDataRawFlowsRecordData.componentType = SkrDataRawFlowsRecordContent()


class SkrDataReadyRequest(univ.Null):
    pass


class SkrTaskResultStatus(univ.Enumerated):
    pass


SkrTaskResultStatus.namedValues = namedval.NamedValues(
    ('data-not-ready', 0),
    ('data-ready', 1),
    ('data-not-found', 2),
    ('error', 3)
)


class SkrTaskResult(univ.Sequence):
    pass


SkrTaskResult.componentType = namedtype.NamedTypes(
    namedtype.NamedType('result', SkrTaskResultStatus()),
    namedtype.OptionalNamedType(
        'report-records-number',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 999999999999))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'report-limit-exeeded',
        univ.Boolean().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'error-description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrDataReadyTaskRecord(univ.Sequence):
    pass


SkrDataReadyTaskRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('task-id', SkrTaskID()),
    namedtype.NamedType('result', SkrTaskResult())
)


class SkrDataReadyResponse(univ.SequenceOf):
    pass


SkrDataReadyResponse.componentType = SkrDataReadyTaskRecord()


class SkrDataResourceRecordContent(univ.Sequence):
    pass


SkrDataResourceRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('res-cdr-header', SkrDataNetworkCdrHeader()),
    namedtype.NamedType(
        'res-url',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 8192))
        )
    ),
    namedtype.NamedType('res-bytes-count', univ.Integer()),
    namedtype.NamedType(
        'res-term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        )
    ),
    namedtype.OptionalNamedType(
        'res-aaa-info',
        SkrIP_AAAInformation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'res-http-method',
        SkrHttpMethod().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'res-abonent-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.OptionalNamedType(
        'res-nat-info',
        univ.SequenceOf(
            componentType=(SkrNetworkPeerInfo())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'res-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'res-data-content-id',
        SkrDataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))
        )
    )
)


class SkrDataResourceRecordData(univ.SequenceOf):
    pass


SkrDataResourceRecordData.componentType = SkrDataResourceRecordContent()


class SkrRawDataType(univ.Enumerated):
    pass


SkrRawDataType.namedValues = namedval.NamedValues(
    ('data-reports', 0),
    ('raw-cdr', 1),
    ('raw-ipdr', 2),
    ('raw-location', 10),
    ('raw-passive', 11)
)


class SkrDataStartRequest(univ.Sequence):
    pass


SkrDataStartRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType('time-from', SkrDateAndTime()),
    namedtype.NamedType('time-to', SkrDateAndTime()),
    namedtype.NamedType('raw-type', SkrRawDataType())
)


class SkrDataStartResponse(univ.Boolean):
    pass


class SkrDataStopRequest(univ.Null):
    pass


class SkrDataStopResponse(univ.Boolean):
    pass


class SkrDataTermAccessRecordContent(univ.Sequence):
    pass


SkrDataTermAccessRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('term-cdr-header', SkrDataNetworkCdrHeader()),
    namedtype.NamedType('term-in-bytes-count', univ.Integer()),
    namedtype.NamedType('term-out-bytes-count', univ.Integer()),
    namedtype.OptionalNamedType(
        'term-protocol',
        univ.Enumerated(
            namedValues=(
                namedval.NamedValues(('telnet', 0), ('ssh', 1), ('scp', 2))
            )
        )
    ),
    namedtype.OptionalNamedType(
        'term-abonent-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'term-nat-info',
        univ.SequenceOf(
            componentType=(SkrNetworkPeerInfo())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'term-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'term-data-content-id',
        SkrDataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))
        )
    ),
    namedtype.OptionalNamedType(
        'sni',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class SkrDataTermAccessRecordData(univ.SequenceOf):
    pass


SkrDataTermAccessRecordData.componentType = SkrDataTermAccessRecordContent()


class SkrDataTypesRequest(SkrRawDataType):
    pass


class SkrDataTypesResponse(univ.Sequence):
    pass


SkrDataTypesResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('successful', univ.Boolean()),
    namedtype.NamedType('selected-type', SkrRawDataType()),
    namedtype.NamedType('time-from', SkrDateAndTime()),
    namedtype.NamedType('time-to', SkrDateAndTime())
)


class SkrVoIPEvent(univ.Enumerated):
    pass


SkrVoIPEvent.namedValues = namedval.NamedValues(
    ('outgoing', 0),
    ('incoming', 1),
    ('unknown', 2)
)


class SkrDataVoipRecordContent(univ.Sequence):
    pass


SkrDataVoipRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('voip-cdr-header', SkrDataNetworkCdrHeader()),
    namedtype.NamedType(
        'voip-session-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        )
    ),
    namedtype.NamedType(
        'voip-conference-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType(
        'voip-duration',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 864000))
        )
    ),
    namedtype.NamedType(
        'voip-originator-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    ),
    namedtype.NamedType(
        'voip-call-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType('voip-calling-number', SkrDataVoipNumber()),
    namedtype.NamedType('voip-called-number', SkrDataVoipNumber()),
    namedtype.NamedType('voip-in-bytes-count', univ.Integer()),
    namedtype.NamedType('voip-out-bytes-count', univ.Integer()),
    namedtype.NamedType('voip-fax', univ.Boolean()),
    namedtype.NamedType(
        'voip-term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        )
    ),
    namedtype.OptionalNamedType(
        'inbound-bunch',
        SkrBunch().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'outbound-bunch',
        SkrBunch().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'voip-gateways',
        univ.SequenceOf(
            componentType=(SkrIPAddress())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.OptionalNamedType(
        'voip-protocol',
        SkrVoipProtocol().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.OptionalNamedType(
        'supplement-service-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.OptionalNamedType(
        'voip-abonent-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.OptionalNamedType(
        'voip-nat-info',
        univ.SequenceOf(
            componentType=(SkrNetworkPeerInfo())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'voip-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'voip-event',
        SkrVoIPEvent().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))
        )
    ),
    namedtype.OptionalNamedType(
        'voip-data-content-id',
        SkrDataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class SkrDataVoipRecordData(univ.SequenceOf):
    pass


SkrDataVoipRecordData.componentType = SkrDataVoipRecordContent()


class SkrDictionaryInfo(univ.Sequence):
    pass


SkrDictionaryInfo.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('dict', useful.ObjectDescriptor()),
    namedtype.NamedType(
        'count',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 4294967295))
        )
    ),
    namedtype.NamedType('change-dates', SkrFindRange())
)


class SkrDictionariesPresenceData(univ.SequenceOf):
    pass


SkrDictionariesPresenceData.componentType = SkrDictionaryInfo()


class SkrDictionaryReport(univ.Sequence):
    pass


SkrDictionaryReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class SkrDisconnectRequest(univ.Null):
    pass


class SkrDisconnectResponse(univ.Null):
    pass


class SkrDocTypesRecord(univ.Sequence):
    pass


SkrDocTypesRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'doc-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 65535))
        )
    ),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.OptionalNamedType('end-time', SkrDateAndTime()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrDocTypesRecordsData(univ.SequenceOf):
    pass


SkrDocTypesRecordsData.componentType = SkrDocTypesRecord()


class SkrDropFilterRequest(SkrFilterID):
    pass


class SkrDropFilterResponse(univ.Sequence):
    pass


SkrDropFilterResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('filter-id', SkrFilterID()),
    namedtype.NamedType('successful', univ.Boolean()),
    namedtype.OptionalNamedType(
        'error-description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrEntityId(univ.Integer):
    pass


SkrEntityId.subtypeSpec = constraint.ValueRangeConstraint(0, 4294967296)


class SkrExpressPaysRecord(univ.Sequence):
    pass


SkrExpressPaysRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('device-id', SkrReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'card-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrExpressCardReportData(univ.SequenceOf):
    pass


SkrExpressCardReportData.componentType = SkrExpressPaysRecord()


class SkrFilterMessageData(univ.Choice):
    pass


SkrFilterMessageData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'create-filter-request',
        SkrCreateFilterRequest().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'create-filter-response',
        SkrCreateFilterResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'drop-filter-request',
        SkrDropFilterRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.NamedType(
        'drop-filter-response',
        SkrDropFilterResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    )
)


class SkrGatesRecord(univ.Sequence):
    pass


SkrGatesRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'gate-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType('ip-list', SkrIPList()),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.OptionalNamedType('end-time', SkrDateAndTime()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType('address', SkrReportedAddress()),
    namedtype.NamedType(
        'gate-type',
        univ.Enumerated(namedValues=(namedval.NamedValues(
            ('sgsn', 0),
            ('ggsn', 1),
            ('smsc', 2),
            ('gmsc', 3),
            ('hss', 4),
            ('pstn', 5),
            ('voip-gw', 6),
            ('aaa', 7),
            ('nat', 8)))
        )
    )
)


class SkrGatesRecordsData(univ.SequenceOf):
    pass


SkrGatesRecordsData.componentType = SkrGatesRecord()


class SkrGetEntities(univ.Null):
    pass


class SkrNonFormalizedEntity(univ.Sequence):
    pass


SkrNonFormalizedEntity.componentType = namedtype.NamedTypes(
    namedtype.NamedType('entity-id', SkrEntityId()),
    namedtype.NamedType(
        'entity-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))

    )
)


class SkrGetEntitiesResponse(univ.SequenceOf):
    pass


SkrGetEntitiesResponse.componentType = SkrNonFormalizedEntity()


class SkrNonFormalizedEntityAttribute(univ.Sequence):
    pass


SkrNonFormalizedEntityAttribute.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'attribute-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType('attribute-type', SkrAttributeType())
)


class SkrGetEntityAttributesResponse(univ.Sequence):
    pass


SkrGetEntityAttributesResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('entity-id', SkrEntityId()),
    namedtype.NamedType(
        'entity-attributes',
        univ.SequenceOf(componentType=(SkrNonFormalizedEntityAttribute()))
    )
)


class SkrGetEntityAtttibutes(SkrEntityId):
    pass


class SkrGetModuleConfigRequest(univ.Choice):
    pass


SkrGetModuleConfigRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'hw-modules-list',
        SkrRequestedHardwareModules().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'sw-modules-list',
        SkrRequestedSoftwareModules().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrGetModuleConfigResponse(univ.Sequence):
    pass


SkrGetModuleConfigResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('hw-modules', SkrSormHardwareModules()),
    namedtype.NamedType('sw-modules', SkrSormSoftwareModules())
)


class SkrGetModuleTypesRequest(univ.Null):
    pass


class SkrModuleType(univ.Sequence):
    pass


SkrModuleType.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'module-type',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 512))
        )
    ),
    namedtype.NamedType(
        'type-description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    )
)


class SkrGetModuleTypesResponse(univ.SequenceOf):
    pass


SkrGetModuleTypesResponse.componentType = SkrModuleType()


class SkrGetStructureRequest(univ.Null):
    pass


class SkrGetStructureResponse(univ.Sequence):
    pass


SkrGetStructureResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('sw-modules', SkrSormHardwareModules()),
    namedtype.NamedType('hw-modules', SkrSormSoftwareModules())
)


class SkrIpDataPointRecord(univ.Sequence):
    pass


SkrIpDataPointRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        )
    ),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.OptionalNamedType('end-time', SkrDateAndTime())
)


class SkrIpDataPointsRecordsData(univ.SequenceOf):
    pass


SkrIpDataPointsRecordsData.componentType = SkrIpDataPointRecord()


class SkrIpNumberingPlanRecord(univ.Sequence):
    pass


SkrIpNumberingPlanRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType('network-address', SkrIPAddress()),
    namedtype.NamedType('network-mask', SkrIPMask()),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.OptionalNamedType('end-time', SkrDateAndTime()))


class SkrIpNumberingPlanRecordsData(univ.SequenceOf):
    pass


SkrIpNumberingPlanRecordsData.componentType = SkrIpNumberingPlanRecord()


class SkrLocationPresenceData(univ.SequenceOf):
    pass


SkrLocationPresenceData.componentType = SkrStandardInterval()


class SkrValidateLocationRecord(univ.Sequence):
    pass


SkrValidateLocationRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('connection-time', SkrDateAndTime()),
    namedtype.NamedType('ident', SkrReportedIdentifier()),
    namedtype.NamedType('connection-location', SkrLocation())
)


class SkrLocationReport(univ.SequenceOf):
    pass


SkrLocationReport.componentType = SkrValidateLocationRecord()


class SkrSetModuleConfigRequest(univ.Sequence):
    pass


SkrSetModuleConfigRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType('module-id', SkrModuleId()),
    namedtype.NamedType('module-config', SkrConfiguratedModule())
)


class SkrManagementRequest(univ.Choice):
    pass


SkrManagementRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'get-structure',
        SkrGetStructureRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'get-module-config',
        SkrGetModuleConfigRequest().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'set-module-config',
        SkrSetModuleConfigRequest().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'check-module',
        SkrCheckModuleRequest().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.NamedType(
        'get-module-types',
        SkrGetModuleTypesRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    )
)


class SkrSetModuleConfigResponse(SkrConfiguratedModule):
    pass


class SkrManagementResponse(univ.Choice):
    pass


SkrManagementResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'get-structure',
        SkrGetStructureResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'get-module-config',
        SkrGetModuleConfigResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'set-module-config',
        SkrSetModuleConfigResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'check-module',
        SkrCheckModuleResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.NamedType(
        'get-module-types',
        SkrGetModuleTypesResponse().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    )
)


class SkrManagementMessageData(univ.Choice):
    pass


SkrManagementMessageData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'request',
        SkrManagementRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))
        )
    ),
    namedtype.NamedType(
        'response',
        SkrManagementResponse().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))
        )
    )
)


class SkrMathOperation(univ.Enumerated):
    pass


SkrMathOperation.namedValues = namedval.NamedValues(
    ('equal', 0),
    ('less', 1),
    ('greater', 2),
    ('not-equal', 3),
    ('less-or-equal', 4),
    ('greater-or-equal', 5)
)


class SkrVersion(char.PrintableString):
    pass


vers = SkrVersion('0.0.1')


class SkrMessage(univ.Sequence):
    pass


SkrMessage.componentType = namedtype.NamedTypes(namedtype.DefaultedNamedType(
    'version',
    SkrVersion().subtype(value=vers)),
    namedtype.NamedType('message-id', SkrMessageID()),
    namedtype.NamedType('message-time', SkrDateAndTime()),
    namedtype.OptionalNamedType(
        'operator-name',
        char.PrintableString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class SkrMobileRecordContent(univ.Sequence):
    pass


SkrMobileRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('begin-connection-time', SkrDateAndTime()),
    namedtype.NamedType(
        'duration',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 86399))
        )
    ),
    namedtype.NamedType(
        'call-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType(
        'supplement-service-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType('in-abonent-type', SkrPhoneAbonentType()),
    namedtype.NamedType('out-abonent-type', SkrPhoneAbonentType()),
    namedtype.NamedType(
        'switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType(
        'term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        )
    ),
    namedtype.OptionalNamedType(
        'inbound-bunch',
        SkrBunch().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'outbound-bunch',
        SkrBunch().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'in-info',
        SkrReportedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'in-end-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'in-begin-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'out-info',
        SkrReportedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'out-begin-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'out-end-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'forwarding-identifier',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))
        )
    ),
    namedtype.OptionalNamedType(
        'roaming-partner-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))
        )
    ),
    namedtype.OptionalNamedType(
        'border-switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'message',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 40))
        )
    ),
    namedtype.OptionalNamedType(
        'data-content-id',
        SkrDataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 41))
        )
    )
)


class SkrMobileRecordData(univ.SequenceOf):
    pass


SkrMobileRecordData.componentType = SkrMobileRecordContent()


class SkrMobileSubscriberIdenityPlanRecord(univ.Sequence):
    pass


SkrMobileSubscriberIdenityPlanRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'mcc',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(3, 3))
        )
    ),
    namedtype.NamedType(
        'mnc',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(3, 3))
        )
    ),
    namedtype.NamedType(
        'area-code',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(3, 10))
        )
    ),
    namedtype.NamedType(
        'capacity-from',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 7))
        )
    ),
    namedtype.NamedType(
        'capacity-to',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 7))
        )
    ),
    namedtype.NamedType(
        'capacity-size',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 1000000))
        )
    ),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 255))
        )
    ),
    namedtype.NamedType(
        'region',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType(
        'city',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType('range-activation', SkrDateAndTime()),
    namedtype.OptionalNamedType(
        'range-deactivation',
        SkrDateAndTime().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'range-status',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrMobileSubscriberIdenityPlanRecordsData(univ.SequenceOf):
    pass


SkrMobileSubscriberIdenityPlanRecordsData.componentType = SkrMobileSubscriberIdenityPlanRecord()


class SkrNonFormalizedEntityAttributeData(univ.Choice):
    pass


SkrNonFormalizedEntityAttributeData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'datetime',
        SkrDateAndTime().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'integer',
        univ.Integer().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'string',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.NamedType(
        'boolean',
        univ.Boolean().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'float',
        univ.Real().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)
            )
        )
    ),
    namedtype.NamedType(
        'empty',
        univ.Null().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    )
)


class SkrNonFormalizedEntityCondition(univ.Sequence):
    pass


SkrNonFormalizedEntityCondition.componentType = namedtype.NamedTypes(
    namedtype.NamedType('attribute', SkrNonFormalizedEntityAttribute()),
    namedtype.NamedType('operation', SkrMathOperation()),
    namedtype.NamedType(
        'attribute-value',
        SkrNonFormalizedEntityAttributeData()
    )
)


class SkrNonFormalizedParameter(univ.Choice):
    pass


SkrNonFormalizedParameter.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        SkrLogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))
    ),
    namedtype.NamedType(
        'find-mask',
        SkrNonFormalizedEntityCondition().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))
        )
    )
)


class SkrNonFormalizedParameters(univ.SequenceOf):
    pass


SkrNonFormalizedParameters.componentType = SkrNonFormalizedParameter()


class SkrNonFormalizedPresenseInfo(univ.SequenceOf):
    pass


SkrNonFormalizedPresenseInfo.componentType = SkrStandardInterval()


class SkrNonFormalizedPresenseTask(SkrEntityId):
    pass


class SkrNonFormalizedPresenseTaskResponse(SkrCreateTaskResponse):
    pass


class SkrNonFormalizedRecord(univ.SequenceOf):
    pass


SkrNonFormalizedRecord.componentType = SkrNonFormalizedEntityAttributeData()


class SkrNonFormalizedRecords(univ.SequenceOf):
    pass


SkrNonFormalizedRecords.componentType = SkrNonFormalizedRecord()


class SkrNonFormalizedReport(univ.Choice):
    pass


SkrNonFormalizedReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'nonformalized-report',
        SkrNonFormalizedRecords().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'nonformalized-presense',
        SkrNonFormalizedPresenseInfo().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrValidateNonFormalizedTask(univ.Sequence):
    pass


SkrValidateNonFormalizedTask.componentType = namedtype.NamedTypes(
    namedtype.NamedType('entity-id', SkrEntityId()),
    namedtype.NamedType('parameters', SkrNonFormalizedParameters()),
    namedtype.OptionalNamedType('range', SkrFindRange()),
    namedtype.OptionalNamedType(
        'report-limit', univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 10000000))
        )
    )
)


class SkrNonFormalizedTaskRequest(univ.Choice):
    pass


SkrNonFormalizedTaskRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'get-entities',
        SkrGetEntities().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'get-attributes',
        SkrGetEntityAtttibutes().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'validate-task',
        SkrValidateNonFormalizedTask().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'validate-presense',
        SkrNonFormalizedPresenseTask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    )
)


class SkrValidateNonFormalizedTaskResponse(SkrCreateTaskResponse):
    pass


class SkrNonFormalizedTaskResponse(univ.Choice):
    pass


SkrNonFormalizedTaskResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'entities',
        SkrGetEntitiesResponse().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'entity-attributes',
        SkrGetEntityAttributesResponse().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))
        )
    ),
    namedtype.NamedType(
        'validate-task',
        SkrValidateNonFormalizedTaskResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'validate-presense',
        SkrNonFormalizedPresenseTaskResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    )
)


class SkrOID(useful.ObjectDescriptor):
    pass


class SkrPagerRecordContent(univ.Sequence):
    pass


SkrPagerRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'call-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType('connection-time', SkrDateAndTime()),
    namedtype.NamedType('info', SkrReportedIdentifier()),
    namedtype.NamedType(
        'in-bytes-count',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1024))
        )
    ),
    namedtype.NamedType(
        'term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        )
    )
)


class SkrPagerRecordData(univ.SequenceOf):
    pass


SkrPagerRecordData.componentType = SkrPagerRecordContent()


class SkrPayTypesRecord(univ.Sequence):
    pass


SkrPayTypesRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'pay-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.OptionalNamedType('end-time', SkrDateAndTime()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrPayTypesRecordsData(univ.SequenceOf):
    pass


SkrPayTypesRecordsData.componentType = SkrPayTypesRecord()


class SkrPaymentsPresenseData(univ.SequenceOf):
    pass


SkrPaymentsPresenseData.componentType = SkrStandardInterval()


class SkrPaymentsReport(univ.Sequence):
    pass


SkrPaymentsReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class SkrPresenseReport(univ.Sequence):
    pass


SkrPresenseReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class SkrPstnRecordContent(univ.Sequence):
    pass


SkrPstnRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('begin-connection-time', SkrDateAndTime()),
    namedtype.NamedType(
        'duration',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 86399))
        )
    ),
    namedtype.NamedType(
        'call-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType(
        'supplement-service-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType('in-abonent-type', SkrPhoneAbonentType()),
    namedtype.NamedType('out-abonent-type', SkrPhoneAbonentType()),
    namedtype.NamedType(
        'switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType(
        'inbound-bunch',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType(
        'outbound-bunch',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType(
        'term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        )
    ),
    namedtype.OptionalNamedType(
        'phone-card-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 20))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'in-info',
        SkrReportedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'dialed-digits',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.OptionalNamedType(
        'out-info',
        SkrReportedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'forwarding-identifier',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.OptionalNamedType(
        'border-switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.OptionalNamedType(
        'message',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'ss7-opc',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))
        )
    ),
    namedtype.OptionalNamedType(
        'ss7-dpc',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))
        )
    ),
    namedtype.OptionalNamedType(
        'data-content-id',
        SkrDataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class SkrPstnRecordData(univ.SequenceOf):
    pass


SkrPstnRecordData.componentType = SkrPstnRecordContent()


class SkrPublicTerminalRecord(univ.Sequence):
    pass


SkrPublicTerminalRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('device-id', SkrReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'terminal-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType(
        'terminal-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 20))
        )
    ),
    namedtype.NamedType('terminal-address', SkrReportedAddress()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.OptionalNamedType('location', SkrLocation())
)


class SkrPublicTerminalReportData(univ.SequenceOf):
    pass


SkrPublicTerminalReportData.componentType = SkrPublicTerminalRecord()


class SkrRawAcknowledgement(SkrAcknowledgement):
    pass


class SkrRawBytes(univ.OctetString):
    pass


SkrRawBytes.subtypeSpec = constraint.ValueSizeConstraint(1, 4096)


class SkrRawBytesBlock(univ.SequenceOf):
    pass


SkrRawBytesBlock.componentType = SkrRawBytes()


class SkrRawDataBlock(univ.Choice):
    pass


SkrRawDataBlock.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'reports',
        SkrCallsRecords().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'raw-cdr',
        SkrRawBytesBlock().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrRawRecordContent(univ.Sequence):
    pass


SkrRawRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('successful', univ.Boolean()),
    namedtype.OptionalNamedType(
        'data',
        univ.OctetString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 1048576))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'error',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 4096))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'codec-info',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 4096))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.OptionalNamedType(
        'direction',
        SkrDataContentRawDirection().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.OptionalNamedType(
        'channel',
        univ.Integer().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    )
)


class SkrRawReport(univ.Sequence):
    pass


SkrRawReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType('request-id', SkrMessageID()),
    namedtype.NamedType(
        'stream-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType(
        'total-blocks-number',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 999999999999))
        )
    ),
    namedtype.NamedType(
        'block-number',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 1000000000000))
        )
    ),
    namedtype.NamedType('report-block', SkrRawDataBlock())
)


class SkrRawRequestTask(univ.Choice):
    pass


SkrRawRequestTask.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'data-types-request',
        SkrDataTypesRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'data-start-request',
        SkrDataStartRequest().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'data-stop-request',
        SkrDataStopRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrRawRequest(univ.Sequence):
    pass


SkrRawRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telcos', SkrTelcoList()),
    namedtype.NamedType('raw-task', SkrRawRequestTask())
)


class SkrRawResponse(univ.Choice):
    pass


SkrRawResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'data-types-response',
        SkrDataTypesResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'data-start-response',
        SkrDataStartResponse().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'data-stop-response',
        SkrDataStopResponse().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrRecodedAbonentInfo(univ.Choice):
    pass


SkrRecodedAbonentInfo.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'person',
        SkrAbonentPerson().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'organization',
        SkrAbonentOrganization().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))
        )
    )
)


class SkrReportedPagerIdentifier(char.NumericString):
    pass


SkrReportedPagerIdentifier.subtypeSpec = constraint.ValueSizeConstraint(2, 18)


class SkrReportedDataNetworkIdentifier(univ.Sequence):
    pass


SkrReportedDataNetworkIdentifier.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType(
        'user-equipment',
        SkrDataNetworkEquipment().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'login',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'ip-address',
        SkrIPAddress().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))
        )
    ),
    namedtype.OptionalNamedType(
        'e-mail',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.OptionalNamedType(
        'pin',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 20))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.OptionalNamedType(
        'phone-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.OptionalNamedType(
        'user-domain',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    ),
    namedtype.OptionalNamedType(
        'reserved',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))
        )
    ),
    namedtype.OptionalNamedType(
        'ip-mask',
        SkrIPMask().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8)
            )
        )
    )
)


class SkrReportedCdmaIdentifier(univ.Sequence):
    pass


SkrReportedCdmaIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'directory-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        )
    ),
    namedtype.NamedType(
        'imsi',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        )
    ),
    namedtype.OptionalNamedType(
        'esn',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'min',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'icc',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(10, 20))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrReportedGsmIdentifier(univ.Sequence):
    pass


SkrReportedGsmIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'directory-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        )
    ),
    namedtype.NamedType(
        'imsi',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        )
    ),
    namedtype.OptionalNamedType(
        'imei',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 18))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'icc',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(10, 20))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrReportedPstnIdentifier(univ.Sequence):
    pass


SkrReportedPstnIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'directory-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        )
    ),
    namedtype.OptionalNamedType(
        'internal-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        )
    )
)


class SkrReportedVoipIdentifier(univ.Sequence):
    pass


SkrReportedVoipIdentifier.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType(
        'ip-address',
        SkrIPAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'originator-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'calling-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class SkrRecodedReportedIdentifier(univ.Choice):
    pass


SkrRecodedReportedIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'pager-identifier',
        SkrReportedPagerIdentifier().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'pstn-identifier',
        SkrReportedPstnIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'gsm-identifier',
        SkrReportedGsmIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'cdma-identifier',
        SkrReportedCdmaIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.NamedType(
        'data-network-identifier',
        SkrReportedDataNetworkIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
            )
        )
    ),
    namedtype.NamedType(
        'voip-identifier',
        SkrReportedVoipIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)
            )
        )
    )
)


class SkrRecodedAbonentService(univ.Sequence):
    pass


SkrRecodedAbonentService.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'service-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.OptionalNamedType('idents', SkrRecodedReportedIdentifier()),
    namedtype.NamedType(
        'contract',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.NamedType('end-time', SkrDateAndTime()),
    namedtype.OptionalNamedType(
        'parameter',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrRecodedActiveServices(univ.SequenceOf):
    pass


SkrRecodedActiveServices.componentType = SkrRecodedAbonentService()


class SkrRecodedAbonentsRecord(univ.Sequence):
    pass


SkrRecodedAbonentsRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('idents', SkrRecodedReportedIdentifier()),
    namedtype.NamedType('contract-date', SkrDateAndTime()),
    namedtype.NamedType(
        'contract',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType('actual-from', SkrDateAndTime()),
    namedtype.NamedType('actual-to', SkrDateAndTime()),
    namedtype.NamedType('abonent', SkrRecodedAbonentInfo()),
    namedtype.NamedType('status', SkrActiveStatus()),
    namedtype.OptionalNamedType(
        'attach',
        SkrDateAndTime().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'detach',
        SkrDateAndTime().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'last-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'services',
        SkrRecodedActiveServices().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.OptionalNamedType(
        'line-data',
        SkrLineData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'standard',
        SkrStandard().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.OptionalNamedType(
        'addresses',
        SkrReportedAddresses().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    )
)


class SkrRecodedBankTransactionRecord(univ.Sequence):
    pass


SkrRecodedBankTransactionRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('device-id', SkrRecodedReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'bank-account',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType(
        'bank-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    ),
    namedtype.NamedType('bank-address', SkrReportedAddress()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrRecodedCrossAccountRecord(univ.Sequence):
    pass


SkrRecodedCrossAccountRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('device-id', SkrRecodedReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType('donanted-id', SkrRecodedReportedIdentifier()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrRecodedExpressPaysRecord(univ.Sequence):
    pass


SkrRecodedExpressPaysRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('device-id', SkrRecodedReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'card-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrRecodedMobileRecordContent(univ.Sequence):
    pass


SkrRecodedMobileRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('begin-connection-time', SkrDateAndTime()),
    namedtype.NamedType(
        'duration',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 86399))
        )
    ),
    namedtype.NamedType(
        'call-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType(
        'supplement-service-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType('in-abonent-type', SkrPhoneAbonentType()),
    namedtype.NamedType('out-abonent-type', SkrPhoneAbonentType()),
    namedtype.NamedType(
        'switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType(
        'term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        )
    ),
    namedtype.OptionalNamedType(
        'inbound-bunch',
        SkrBunch().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'outbound-bunch',
        SkrBunch().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'in-info',
        SkrRecodedReportedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'in-end-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'in-begin-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'out-info',
        SkrRecodedReportedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'out-begin-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'out-end-location',
        SkrLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'forwarding-identifier',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))
        )
    ),
    namedtype.OptionalNamedType(
        'roaming-partner-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))
        )
    ),
    namedtype.OptionalNamedType(
        'border-switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'message',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 40))
        )
    ),
    namedtype.OptionalNamedType(
        'data-content-id',
        SkrDataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 41))
        )
    )
)


class SkrRecodedPagerRecordContent(univ.Sequence):
    pass


SkrRecodedPagerRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'call-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType('connection-time', SkrDateAndTime()),
    namedtype.NamedType('info', SkrRecodedReportedIdentifier()),
    namedtype.NamedType(
        'in-bytes-count',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1024))
        )
    ),
    namedtype.NamedType(
        'term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        )
    )
)


class SkrRecodedPstnRecordContent(univ.Sequence):
    pass


SkrRecodedPstnRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('begin-connection-time', SkrDateAndTime()),
    namedtype.NamedType(
        'duration',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 86399))
        )
    ),
    namedtype.NamedType(
        'call-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType(
        'supplement-service-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType('in-abonent-type', SkrPhoneAbonentType()),
    namedtype.NamedType('out-abonent-type', SkrPhoneAbonentType()),
    namedtype.NamedType(
        'switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType(
        'inbound-bunch',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType(
        'outbound-bunch',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType(
        'term-cause',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        )
    ),
    namedtype.OptionalNamedType(
        'phone-card-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 20))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'in-info',
        SkrRecodedReportedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'dialed-digits',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.OptionalNamedType(
        'out-info',
        SkrRecodedReportedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'forwarding-identifier',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.OptionalNamedType(
        'border-switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.OptionalNamedType(
        'message',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'ss7-opc',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))
        )
    ),
    namedtype.OptionalNamedType(
        'ss7-dpc',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))
        )
    ),
    namedtype.OptionalNamedType(
        'data-content-id',
        SkrDataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class SkrRecodedPublicTerminalRecord(univ.Sequence):
    pass


SkrRecodedPublicTerminalRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('device-id', SkrRecodedReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'terminal-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType(
        'terminal-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 20))
        )
    ),
    namedtype.NamedType('terminal-address', SkrReportedAddress()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.OptionalNamedType('location', SkrLocation())
)


class SkrRecodedReportAbonentData(univ.SequenceOf):
    pass


SkrRecodedReportAbonentData.componentType = SkrRecodedAbonentsRecord()


class SkrRecodedReportServiceData(univ.SequenceOf):
    pass


SkrRecodedReportServiceData.componentType = SkrRecodedAbonentService()


class SkrRecodedServiceCenterRecord(univ.Sequence):
    pass


SkrRecodedServiceCenterRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('device-id', SkrRecodedReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'center-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType('center-address', SkrReportedAddress()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrRecodedValidateBalanceFillupRecord(univ.Sequence):
    pass


SkrRecodedValidateBalanceFillupRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'pay-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType('device-id', SkrRecodedReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.OptionalNamedType(
        'pay-parameters',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    )
)


class SkrRecodedValidateBankAccountTransferRecord(univ.Sequence):
    pass


SkrRecodedValidateBankAccountTransferRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('donated-id', SkrRecodedReportedIdentifier()),
    namedtype.NamedType(
        'bank-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType(
        'bank-account',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType(
        'date-time-fillup',
        SkrDateAndTime()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrRecodedValidateBankCardTransferRecord(univ.Sequence):
    pass


SkrRecodedValidateBankCardTransferRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('donanted-id', SkrRecodedReportedIdentifier()),
    namedtype.NamedType(
        'bank-card-id',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 12))
        )
    ),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrRecodedValidateBankDivisionTransferRecord(univ.Sequence):
    pass


SkrRecodedValidateBankDivisionTransferRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('donanted-id', SkrRecodedReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'person-received',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    ),
    namedtype.NamedType(
        'bank-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType(
        'bank-division-name',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    ),
    namedtype.NamedType('bank-division-address', SkrReportedAddress()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrRecodedValidateLocationRecord(univ.Sequence):
    pass


SkrRecodedValidateLocationRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('connection-time', SkrDateAndTime()),
    namedtype.NamedType('ident', SkrRecodedReportedIdentifier()),
    namedtype.NamedType('connection-location', SkrLocation())
)


class SkrRecodedValidateTelephoneCardRecord(univ.Sequence):
    pass


SkrRecodedValidateTelephoneCardRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('activator-device-id', SkrRecodedReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'card-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 20))
        )
    ),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrReportDataBlock(univ.Choice):
    pass


SkrReportDataBlock.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'dictionary',
        SkrDictionaryReport().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'abonents',
        SkrAbonentsReport().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'connections',
        SkrConnectionsReport().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'locations',
        SkrLocationReport().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'payments',
        SkrPaymentsReport().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
            )
        )
    ),
    namedtype.NamedType(
        'presense',
        SkrPresenseReport().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6)
            )
        )
    ),
    namedtype.NamedType(
        'nonFormalized',
        SkrNonFormalizedReport().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7)
            )
        )
    ),
    namedtype.NamedType(
        'data-content',
        SkrDataContentReport().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10)
            )
        )
    )
)


class SkrReport(univ.Sequence):
    pass


SkrReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType('request-id', SkrMessageID()),
    namedtype.NamedType('task-id', SkrTaskID()),
    namedtype.NamedType('total-blocks-number', univ.Integer()),
    namedtype.NamedType('block-number', univ.Integer()),
    namedtype.NamedType('report-block', SkrReportDataBlock())
)


class SkrReportAbonentData(univ.SequenceOf):
    pass


SkrReportAbonentData.componentType = SkrAbonentsRecord()


class SkrReportDataContentRawData(univ.SequenceOf):
    pass


SkrReportDataContentRawData.componentType = SkrRawRecordContent()


class SkrReportMessageData(univ.Choice):
    pass


SkrReportMessageData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'report',
        SkrReport().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'ack',
        SkrAcknowledgement().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class SkrReportServiceData(univ.SequenceOf):
    pass


SkrReportServiceData.componentType = SkrAbonentService()


class SkrRoamingPartnerRecord(univ.Sequence):
    pass


SkrRoamingPartnerRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'roaming-id',
        univ.Integer().subtype(
            subtypeSpec=(
                constraint.ValueRangeConstraint(0, 4294967295)
            )
        )
    ),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.OptionalNamedType('end-time', SkrDateAndTime()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrRoamingPartnersRecordsData(univ.SequenceOf):
    pass


SkrRoamingPartnersRecordsData.componentType = SkrRoamingPartnerRecord()


class SkrServiceCenterRecord(univ.Sequence):
    pass


SkrServiceCenterRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('device-id', SkrReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'center-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType('center-address', SkrReportedAddress()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrServiceCenterReport(univ.SequenceOf):
    pass


SkrServiceCenterReport.componentType = SkrServiceCenterRecord()


class SkrSessionMessageData(univ.Choice):
    pass


SkrSessionMessageData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'connect',
        SkrConnectRequest().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'connect-response',
        SkrConnectResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'adjustment',
        SkrAdjustmentRequest().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'adjustment-response',
        SkrAdjustmentResponse().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'disconnect',
        SkrDisconnectRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'disconnect-response',
        SkrDisconnectResponse().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    )
)


class SkrSignalPointCodesRecord(univ.Sequence):
    pass


SkrSignalPointCodesRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'ss7-point-code',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 32))
        )
    ),
    namedtype.NamedType(
        'switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType(
        'begin-time',
        SkrDateAndTime()
    ),
    namedtype.OptionalNamedType(
        'end-time',
        SkrDateAndTime()
    ),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrSignalPointCodesRecordsData(univ.SequenceOf):
    pass


SkrSignalPointCodesRecordsData.componentType = SkrSignalPointCodesRecord()


class SkrSpecialNumberRecord(univ.Sequence):
    pass


SkrSpecialNumberRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'telco-id', SkrTelcoID()
    ),
    namedtype.NamedType(
        'directory-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 32))
        )
    ),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType(
        'begin-time', SkrDateAndTime()
    ),
    namedtype.OptionalNamedType(
        'end-time', SkrDateAndTime()
    ),
    namedtype.OptionalNamedType(
        'network-address', SkrIPAddress()
    )
)


class SkrSpecialNumbersRecordsData(univ.SequenceOf):
    pass


SkrSpecialNumbersRecordsData.componentType = SkrSpecialNumberRecord()


class SkrSubsPresenceData(univ.SequenceOf):
    pass


SkrSubsPresenceData.componentType = SkrStandardInterval()


class SkrSupplementServicesRecord(univ.Sequence):
    pass


SkrSupplementServicesRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'service-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType(
        'mnemonic',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.OptionalNamedType('end-time', SkrDateAndTime()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class SkrSupplementServicesRecordsData(univ.SequenceOf):
    pass


SkrSupplementServicesRecordsData.componentType = SkrSupplementServicesRecord()


class SkrSwitchesRecord(univ.Sequence):
    pass


SkrSwitchesRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.OptionalNamedType('end-time', SkrDateAndTime()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType('network-type', SkrNetworkType()),
    namedtype.NamedType('address', SkrReportedAddress()),
    namedtype.OptionalNamedType(
        'switch-sign',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 18))
        )
    ),
    namedtype.NamedType(
        'switch-type',
        univ.Enumerated(
            namedValues=(namedval.NamedValues(('internal', 0), ('border', 1)))
        )
    )
)


class SkrSwitchesRecordsData(univ.SequenceOf):
    pass


SkrSwitchesRecordsData.componentType = SkrSwitchesRecord()


class SkrTaskMessageData(univ.Choice):
    pass


SkrTaskMessageData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'data-ready-request',
        SkrDataReadyRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'data-ready-response',
        SkrDataReadyResponse().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'data-load-request',
        SkrDataLoadRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.NamedType(
        'data-load-response',
        SkrDataLoadResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.NamedType(
        'data-drop-request',
        SkrDataDropRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'data-drop-response',
        SkrDataDropResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)
            )
        )
    ),
    namedtype.NamedType(
        'data-interrupt-request',
        SkrDataInterruptRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    ),
    namedtype.NamedType(
        'data-interrupt-response',
        SkrDataInterruptResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7)
            )
        )
    ),
    namedtype.NamedType(
        'create-task-request',
        SkrCreateTaskRequest().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8)
            )
        )
    ),
    namedtype.NamedType(
        'create-task-response',
        SkrCreateTaskResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9)
            )
        )
    ),
    namedtype.NamedType(
        'non-formalized-task-request',
        SkrNonFormalizedTaskRequest().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10)
            )
        )
    ),
    namedtype.NamedType(
        'non-formalized-task-response',
        SkrNonFormalizedTaskResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    )
)


class SkrTelcosRecord(univ.Sequence):
    pass


SkrTelcosRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.OptionalNamedType('end-time', SkrDateAndTime()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.OptionalNamedType(
        'mcc',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(3, 3))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'mnc',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(3, 3))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrTelcosRecordsData(univ.SequenceOf):
    pass


SkrTelcosRecordsData.componentType = SkrTelcosRecord()


class SkrValidateTelephoneCardRecord(univ.Sequence):
    pass


SkrValidateTelephoneCardRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType('activator-device-id', SkrReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', SkrDateAndTime()),
    namedtype.NamedType(
        'card-number',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 20))
        )
    ),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class SkrTelephoneCardReportData(univ.SequenceOf):
    pass


SkrTelephoneCardReportData.componentType = SkrValidateTelephoneCardRecord()


class SkrTelephoneNumberingPlanRecord(univ.Sequence):
    pass


SkrTelephoneNumberingPlanRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'iso-3166-alpha-2',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 2))
        )
    ),
    namedtype.NamedType(
        'iso-3166-alpha-3',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(3, 3))
        )
    ),
    namedtype.NamedType(
        'country-code',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(3, 3))
        )
    ),
    namedtype.NamedType(
        'national-significant-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(14, 14))
        )
    ),
    namedtype.NamedType(
        'area-code-length',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 6))
        )
    ),
    namedtype.NamedType(
        'min-subscr-nr-length',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 15))
        )
    ),
    namedtype.NamedType(
        'max-subscr-nr-length',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 15))
        )
    ),
    namedtype.NamedType(
        'utc-min',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(-12, 12))
        )
    ),
    namedtype.NamedType(
        'utc-max',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(-12, 12))
        )
    ),
    namedtype.NamedType(
        'destination',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 255))
        )
    ),
    namedtype.NamedType('operator-type-id', SkrNetworkType()),
    namedtype.NamedType(
        'capacity-from', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 15)))),
    namedtype.NamedType(
        'capacity-to',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 15))
        )
    ),
    namedtype.NamedType(
        'capacity-size',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 1000000))
        )
    ),
    namedtype.NamedType(
        'location',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 255))
        )
    ),
    namedtype.NamedType(
        'registrar',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 255))
        )
    ),
    namedtype.NamedType('range-activation', SkrDateAndTime()),
    namedtype.NamedType(
        'mobile-country-code',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(3, 3))
        )
    ),
    namedtype.NamedType(
        'mobile-network-code',
        char.NumericString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(3, 3))
        )
    ),
    namedtype.OptionalNamedType(
        'range-deactivation',
        SkrDateAndTime().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'range-status',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 128))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.OptionalNamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(2, 255))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.OptionalNamedType(
        'operating-company-number',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 4))
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    )
)


class SkrTelephoneNumberingPlanRecordsData(univ.SequenceOf):
    pass


SkrTelephoneNumberingPlanRecordsData.componentType = SkrTelephoneNumberingPlanRecord()


class SkrTerminationCausesRecord(univ.Sequence):
    pass


SkrTerminationCausesRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', SkrTelcoID()),
    namedtype.NamedType(
        'termination-cause-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        )
    ),
    namedtype.NamedType('begin-time', SkrDateAndTime()),
    namedtype.OptionalNamedType('end-time', SkrDateAndTime()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType('network-type', SkrNetworkType())
)


class SkrTerminationCausesRecordsData(univ.SequenceOf):
    pass


SkrTerminationCausesRecordsData.componentType = SkrTerminationCausesRecord()


class SkrTrapType(univ.Enumerated):
    pass


SkrTrapType.namedValues = namedval.NamedValues(
    ('heartbeat', 0),
    ('restart-software', 1),
    ('unauthorized-access', 2),
    ('critical-error', 3),
    ('major-error', 4),
    ('minor-error', 5)
)


class SkrTrap(univ.Sequence):
    pass


SkrTrap.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'trap-type', SkrTrapType()
    ),
    namedtype.OptionalNamedType(
        'trap-message',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.OptionalNamedType('reference-message', SkrMessageID())
)


class SkrTrapAck(univ.Null):
    pass


class SkrTrapMessageData(univ.Choice):
    pass


SkrTrapMessageData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'trap',
        SkrTrap().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'trap-ack',
        SkrTrapAck().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class SkrUnformattedMessageData(univ.Choice):
    pass


SkrUnformattedMessageData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'request',
        SkrRawRequest().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'response',
        SkrRawResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'report',
        SkrRawReport().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'report-ack',
        SkrRawAcknowledgement().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    )
)


sorm_message_filter = SkrOID('286')
sorm_message_management = SkrOID('284')
sorm_message_report = SkrOID('283')
sorm_message_session = SkrOID('280')
sorm_message_task = SkrOID('282')
sorm_message_trap = SkrOID('281')
sorm_message_unformatted = SkrOID('285')
sorm_report_abonent_abonent = SkrOID('40')
sorm_report_abonent_organization = SkrOID('43')
sorm_report_abonent_person = SkrOID('42')
sorm_report_abonent_service = SkrOID('41')
sorm_report_connection_aaa_login = SkrOID('24')
sorm_report_connection_address_translations = SkrOID('32')
sorm_report_connection_email = SkrOID('26')
sorm_report_connection_file_transfer = SkrOID('29')
sorm_report_connection_im = SkrOID('27')
sorm_report_connection_ipdr_header = SkrOID('23')
sorm_report_connection_mobile = SkrOID('22')
sorm_report_connection_pager = SkrOID('20')
sorm_report_connection_pstn = SkrOID('21')
sorm_report_connection_raw_flows = SkrOID('31')
sorm_report_connection_resource = SkrOID('25')
sorm_report_connection_term_access = SkrOID('30')
sorm_report_connection_voip = SkrOID('28')
sorm_report_data_content_raw = SkrOID('50')
sorm_report_dictionary_basic_stations = SkrOID('101')
sorm_report_dictionary_bunches = SkrOID('100')
sorm_report_dictionary_bunches_map = SkrOID('115')
sorm_report_dictionary_call_types = SkrOID('105')
sorm_report_dictionary_doc_types = SkrOID('111')
sorm_report_dictionary_gates = SkrOID('104')
sorm_report_dictionary_ip_data_points = SkrOID('113')
sorm_report_dictionary_ip_numbering_plan = SkrOID('109')
sorm_report_dictionary_mobile_subscriber_identity_plan = SkrOID('116')
sorm_report_dictionary_pay_types = SkrOID('107')
sorm_report_dictionary_phone_numbering_plan = SkrOID('110')
sorm_report_dictionary_roaming_partners = SkrOID('102')
sorm_report_dictionary_signal_point_codes = SkrOID('132')
sorm_report_dictionary_special_numbers = SkrOID('114')
sorm_report_dictionary_supplement_services = SkrOID('106')
sorm_report_dictionary_switches = SkrOID('103')
sorm_report_dictionary_telcos = SkrOID('112')
sorm_report_dictionary_termination_causes = SkrOID('108')
sorm_report_identifier_cdma = SkrOID('4')
sorm_report_identifier_data_network = SkrOID('5')
sorm_report_identifier_gsm = SkrOID('3')
sorm_report_identifier_pager = SkrOID('1')
sorm_report_identifier_pstn = SkrOID('2')
sorm_report_identifier_voip = SkrOID('6')
sorm_report_location_geo = SkrOID('62')
sorm_report_location_mobile = SkrOID('60')
sorm_report_location_wireless = SkrOID('61')
sorm_report_payment_balance_fillups = SkrOID('86')
sorm_report_payment_bank_account_transfer = SkrOID('89')
sorm_report_payment_bank_card_transfer = SkrOID('88')
sorm_report_payment_bank_division_transfer = SkrOID('87')
sorm_report_payment_bank_transaction = SkrOID('80')
sorm_report_payment_cross_account = SkrOID('84')
sorm_report_payment_express_pays = SkrOID('81')
sorm_report_payment_service_center = SkrOID('83')
sorm_report_payment_telephone_card = SkrOID('85')
sorm_report_payment_terminal_pays = SkrOID('82')
sorm_report_presense_abonents = SkrOID('120')
sorm_report_presense_connections = SkrOID('121')
sorm_report_presense_dictionaries = SkrOID('123')
sorm_report_presense_locations = SkrOID('124')
sorm_report_presense_payments = SkrOID('122')
sorm_request_abonent_organization = SkrOID('181')
sorm_request_abonent_person = SkrOID('180')
sorm_request_connection_aaa_login = SkrOID('164')
sorm_request_connection_address_translations = SkrOID('173')
sorm_request_connection_email = SkrOID('166')
sorm_request_connection_entrance = SkrOID('172')
sorm_request_connection_file_transfer = SkrOID('169')
sorm_request_connection_im = SkrOID('167')
sorm_request_connection_mobile = SkrOID('162')
sorm_request_connection_pager = SkrOID('160')
sorm_request_connection_pstn = SkrOID('161')
sorm_request_connection_raw_flows = SkrOID('171')
sorm_request_connection_resource = SkrOID('165')
sorm_request_connection_term_access = SkrOID('170')
sorm_request_connection_voip = SkrOID('168')
sorm_request_dictionaries = SkrOID('240')
sorm_request_identifier_cdma = SkrOID('143')
sorm_request_identifier_data_network = SkrOID('144')
sorm_request_identifier_gsm = SkrOID('142')
sorm_request_identifier_pager = SkrOID('140')
sorm_request_identifier_pstn = SkrOID('141')
sorm_request_identifier_voip = SkrOID('145')
sorm_request_location = SkrOID('200')
sorm_request_payment_balance_fillups = SkrOID('226')
sorm_request_payment_bank_account_transfer = SkrOID('229')
sorm_request_payment_bank_card_transfer = SkrOID('228')
sorm_request_payment_bank_division_transfer = SkrOID('227')
sorm_request_payment_bank_transaction = SkrOID('220')
sorm_request_payment_cross_account = SkrOID('224')
sorm_request_payment_express_pays = SkrOID('221')
sorm_request_payment_service_center = SkrOID('223')
sorm_request_payment_telephone_card = SkrOID('225')
sorm_request_payment_terminal_pays = SkrOID('222')
sorm_request_presense = SkrOID('260')
