from pyasn1.type import (
    univ,
    char,
    namedtype,
    namedval,
    tag,
    constraint,
    useful,
)


class NRST_AbonentInfo(univ.Sequence):
    pass


NRST_AbonentInfo.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)

class NRST_InternalUsersRecord(univ.Sequence):
    pass


NRST_InternalUsersRecord.componentType = namedtype.NamedTypes(
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

class NRST_InternalUsers(univ.SequenceOf):
    pass


NRST_InternalUsers.componentType = NRST_InternalUsersRecord()


class NRST_AbonentOrganization(univ.Sequence):
    pass


NRST_AbonentOrganization.componentType = namedtype.NamedTypes(
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
        NRST_InternalUsers().subtype(
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


class NRST_IdentCardStructInfoReport(univ.Sequence):
    pass


NRST_IdentCardStructInfoReport.componentType = namedtype.NamedTypes(
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


class NRST_IdentCardInfoReport(univ.Choice):
    pass


NRST_IdentCardInfoReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'struct-info',
        NRST_IdentCardStructInfoReport().subtype(
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


class NRST_PassportInfoReport(univ.Sequence):
    pass


NRST_PassportInfoReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'ident-card-info',
        NRST_IdentCardInfoReport()
    ),
    namedtype.NamedType(
        'doc-type-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 65535))
        )
    )
)


class NRST_PersonStructNameInfoReport(univ.Sequence):
    pass


NRST_PersonStructNameInfoReport.componentType = namedtype.NamedTypes(
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


class NRST_PersonNameInfoReport(univ.Choice):
    pass


NRST_PersonNameInfoReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'struct-name',
        NRST_PersonStructNameInfoReport().subtype(
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


class NRST_AbonentPerson(univ.Sequence):
    pass


NRST_AbonentPerson.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'name-info',
        NRST_PersonNameInfoReport()
    ),
    namedtype.OptionalNamedType(
        'birth-date', useful.GeneralizedTime()
    ),
    namedtype.NamedType(
        'passport-info',
        NRST_PassportInfoReport()
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


class NRST_ReportedIdentifier(univ.Sequence):
    pass


NRST_ReportedIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class NRST_TelcoID(univ.Integer):
    pass


NRST_TelcoID.subtypeSpec = constraint.ValueRangeConstraint(0, 65535)

class NRST_DateAndTime(useful.UTCTime):
    pass


class NRST_AbonentService(univ.Sequence):
    pass


NRST_AbonentService.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', NRST_TelcoID()),
    namedtype.NamedType(
        'service-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.OptionalNamedType('idents', NRST_ReportedIdentifier()),
    namedtype.NamedType(
        'contract',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    ),
    namedtype.NamedType('begin-time', NRST_DateAndTime()),
    namedtype.NamedType('end-time', NRST_DateAndTime()),
    namedtype.OptionalNamedType(
        'parameter',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class NRST_ActiveServices(univ.SequenceOf):
    pass


NRST_ActiveServices.componentType = NRST_AbonentService()

class NRST_AddressStructInfoReport(univ.Sequence):
    pass


NRST_AddressStructInfoReport.componentType = namedtype.NamedTypes(namedtype.OptionalNamedType('zip', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('country', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.OptionalNamedType('region', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))), namedtype.OptionalNamedType('zone', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))), namedtype.OptionalNamedType('city', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))), namedtype.OptionalNamedType('street', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))), namedtype.OptionalNamedType('building', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6)))), namedtype.OptionalNamedType('build-sect', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7)))), namedtype.OptionalNamedType('apartment', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8)))))

class NRST_AddressInfoReport(univ.Choice):
    pass


NRST_AddressInfoReport.componentType = namedtype.NamedTypes(namedtype.NamedType('struct-info', NRST_AddressStructInfoReport().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.NamedType('unstruct-info', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 1024))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))))

class NRST_AddressType(univ.Enumerated):
    pass


NRST_AddressType.namedValues = namedval.NamedValues(
    ('registered', 0),
    ('postal', 1),
    ('invoice', 2),
    ('device-location', 3),
    ('reserved', 4)
)

class NRST_ReportedAddress(univ.Sequence):
    pass


NRST_ReportedAddress.componentType = namedtype.NamedTypes(
    namedtype.NamedType('title', NRST_AddressType()),
    namedtype.NamedType('address-info', NRST_AddressInfoReport())
)


class NRST_ReportedAddresses(univ.SequenceOf):
    pass


NRST_ReportedAddresses.componentType = NRST_ReportedAddress()

class NRST_ActiveStatus(univ.Enumerated):
    pass


NRST_ActiveStatus.namedValues = namedval.NamedValues(
    ('active', 0),
    ('not-active', 1)
)

class NRST_LineData(univ.Sequence):
    pass


NRST_LineData.componentType = namedtype.NamedTypes(
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

class NRST_WirelessLocation(univ.Sequence):
    pass


NRST_WirelessLocation.componentType = namedtype.NamedTypes(
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


class NRST_GeoLocation(univ.Sequence):
    pass


NRST_GeoLocation.componentType = namedtype.NamedTypes(
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


class NRST_MobileLocation(univ.Sequence):
    pass


NRST_MobileLocation.componentType = namedtype.NamedTypes(
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


class NRST_Location(univ.Choice):
    pass


NRST_Location.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'mobile-location', NRST_MobileLocation().subtype(
        implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))
        )
    ),
    namedtype.NamedType(
        'wireless-location',
        NRST_WirelessLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'geo-location',
        NRST_GeoLocation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    )
)


class NRST_NetworkType(univ.Enumerated):
    pass


NRST_NetworkType.namedValues = namedval.NamedValues(
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

class NRST_Standard(NRST_NetworkType):
    pass


class NRST_AbonentsRecord(univ.Sequence):
    pass


NRST_AbonentsRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('idents', NRST_ReportedIdentifier()), namedtype.NamedType('contract-date', NRST_DateAndTime()), namedtype.NamedType('contract', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.NamedType('actual-from', NRST_DateAndTime()), namedtype.NamedType('actual-to', NRST_DateAndTime()), namedtype.NamedType('abonent', NRST_AbonentInfo()), namedtype.NamedType('status', NRST_ActiveStatus()), namedtype.OptionalNamedType('attach', NRST_DateAndTime().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('detach', NRST_DateAndTime().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.OptionalNamedType('last-location', NRST_Location().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)))), namedtype.OptionalNamedType('services', NRST_ActiveServices().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))), namedtype.OptionalNamedType('line-data', NRST_LineData().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)))), namedtype.OptionalNamedType('standard', NRST_Standard().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))), namedtype.OptionalNamedType('addresses', NRST_ReportedAddresses().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6)))))


class NRST_AbonentsReport(univ.Sequence):
    pass


NRST_AbonentsReport.componentType = namedtype.NamedTypes(namedtype.NamedType('id', useful.ObjectDescriptor()), namedtype.NamedType('data', univ.Any()))


class NRST_RequestedIdentifier(univ.Sequence):
    pass


NRST_RequestedIdentifier.componentType = namedtype.NamedTypes(namedtype.NamedType('id', useful.ObjectDescriptor()), namedtype.NamedType('data', univ.Any()))

class NRST_DataNetworkATM(univ.Sequence):
    pass


NRST_DataNetworkATM.componentType = namedtype.NamedTypes(namedtype.NamedType('vpi', univ.OctetString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 1)))), namedtype.OptionalNamedType('vci', univ.OctetString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 2)))))

class NRST_DataNetworkEquipment(univ.Choice):
    pass


NRST_DataNetworkEquipment.componentType = namedtype.NamedTypes(namedtype.NamedType('mac', univ.OctetString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(6, 6))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('atm', NRST_DataNetworkATM().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))))

class NRST_IPV4Address(univ.OctetString):
    pass


NRST_IPV4Address.subtypeSpec = constraint.ValueSizeConstraint(4, 4)

class NRST_IPV6Address(univ.OctetString):
    pass


NRST_IPV6Address.subtypeSpec = constraint.ValueSizeConstraint(16, 16)

class NRST_IPAddress(univ.Choice):
    pass


NRST_IPAddress.componentType = namedtype.NamedTypes(namedtype.NamedType('ipv4', NRST_IPV4Address().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('ipv6', NRST_IPV6Address().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))))

class NRST_RequestedDataNetworkIdentifier(univ.Choice):
    pass


NRST_RequestedDataNetworkIdentifier.componentType = namedtype.NamedTypes(namedtype.NamedType('user-equipment', NRST_DataNetworkEquipment().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.NamedType('login', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.NamedType('ip-address', NRST_IPAddress().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)))), namedtype.NamedType('e-mail', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))), namedtype.NamedType('voip-phone-number', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))))

class NRST_RequestedPagerIdentifier(char.NumericString):
    pass


NRST_RequestedPagerIdentifier.subtypeSpec = constraint.ValueSizeConstraint(2, 18)

class NRST_RequestedPstnIdentifier(univ.Sequence):
    pass


NRST_RequestedPstnIdentifier.componentType = namedtype.NamedTypes(namedtype.NamedType('directory-number', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 32)))), namedtype.OptionalNamedType('internal-number', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 32)))))

class NRST_RequestedGsmIdentifier(univ.Choice):
    pass


NRST_RequestedGsmIdentifier.componentType = namedtype.NamedTypes(namedtype.NamedType('directory-number', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('imsi', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 18))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.NamedType('imei', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 18))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))))

class NRST_RequestedCdmaIdentifier(univ.Choice):
    pass


NRST_RequestedCdmaIdentifier.componentType = namedtype.NamedTypes(namedtype.NamedType('directory-number', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('imsi', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 18))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.NamedType('esn', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 18))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))), namedtype.NamedType('min', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 18))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))))

class NRST_RequestedVoipIdentifier(univ.Choice):
    pass


NRST_RequestedVoipIdentifier.componentType = namedtype.NamedTypes(namedtype.NamedType('ip-address', NRST_IPAddress().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.NamedType('originator-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 512))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.NamedType('calling-number', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))))

class NRST_RecodedRequestedIdentifier(univ.Choice):
    pass


NRST_RecodedRequestedIdentifier.componentType = namedtype.NamedTypes(namedtype.NamedType('pager-identifier', NRST_RequestedPagerIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('pstn-identifier', NRST_RequestedPstnIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.NamedType('gsm-identifier', NRST_RequestedGsmIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)))), namedtype.NamedType('cdma-identifier', NRST_RequestedCdmaIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)))), namedtype.NamedType('data-network-identifier', NRST_RequestedDataNetworkIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)))), namedtype.NamedType('voip-identifier', NRST_RequestedVoipIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)))))

class NRST_ValidateServicesParameter(univ.Choice):
    pass


NRST_ValidateServicesParameter.componentType = namedtype.NamedTypes(namedtype.NamedType('contract', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('identifier', NRST_RequestedIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.NamedType('recoded-identifier', NRST_RecodedRequestedIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 101)))))

class NRST_LogicalOperation(univ.Enumerated):
    pass


NRST_LogicalOperation.namedValues = namedval.NamedValues(
    ('operation-open-bracket', 0),
    ('operation-close-bracket', 1),
    ('operation-or', 2),
    ('operation-and', 3),
    ('operation-not', 4)
)

class NRST_ValidateServicesParameters(univ.Choice):
    pass


NRST_ValidateServicesParameters.componentType = namedtype.NamedTypes(namedtype.NamedType('separator', NRST_LogicalOperation().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('find-mask', NRST_ValidateServicesParameter().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))))

class NRST_ValidateServicesTask(univ.SequenceOf):
    pass


NRST_ValidateServicesTask.componentType = NRST_ValidateServicesParameters()

class NRST_RequestedIdentifierParameters(univ.Choice):
    pass


NRST_RequestedIdentifierParameters.componentType = namedtype.NamedTypes(namedtype.NamedType('separator', NRST_LogicalOperation().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('find-mask', NRST_RequestedIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.NamedType('recoded-find-mask', NRST_RecodedRequestedIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 100)))))

class NRST_RequestedIdentifiers(univ.SequenceOf):
    pass


NRST_RequestedIdentifiers.componentType = NRST_RequestedIdentifierParameters()

class NRST_ValidateAbonentsTask(NRST_RequestedIdentifiers):
    pass


class NRST_RequestedPassport(univ.Sequence):
    pass


NRST_RequestedPassport.componentType = namedtype.NamedTypes(namedtype.OptionalNamedType('doc-type-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 65535))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('passport-serial', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 16))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.OptionalNamedType('passport-number', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 16))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))))

class NRST_RequestedAddress(univ.Sequence):
    pass


NRST_RequestedAddress.componentType = namedtype.NamedTypes(namedtype.OptionalNamedType('zip', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('country', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.OptionalNamedType('region', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))), namedtype.OptionalNamedType('zone', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))), namedtype.OptionalNamedType('city', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))), namedtype.OptionalNamedType('street', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))), namedtype.OptionalNamedType('building', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6)))), namedtype.OptionalNamedType('build-sect', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7)))), namedtype.OptionalNamedType('apartment', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8)))))

class NRST_RequestedPerson(univ.Sequence):
    pass


NRST_RequestedPerson.componentType = namedtype.NamedTypes(namedtype.OptionalNamedType('given-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('initial', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.OptionalNamedType('family-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))), namedtype.OptionalNamedType('passport-info', NRST_RequestedPassport().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)))), namedtype.OptionalNamedType('address', NRST_RequestedAddress().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)))), namedtype.OptionalNamedType('icc', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(10, 20))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))), namedtype.OptionalNamedType('contract', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6)))))

class NRST_RequestedOrganization(univ.Sequence):
    pass


NRST_RequestedOrganization.componentType = namedtype.NamedTypes(namedtype.OptionalNamedType('full-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('address', NRST_RequestedAddress().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.OptionalNamedType('inn', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))), namedtype.OptionalNamedType('internal-user', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))), namedtype.OptionalNamedType('contract', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))))

class NRST_RecodedRequestedAbonent(univ.Choice):
    pass


NRST_RecodedRequestedAbonent.componentType = namedtype.NamedTypes(namedtype.NamedType('person', NRST_RequestedPerson().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.NamedType('organization', NRST_RequestedOrganization().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))))

class NRST_RequestedAbonent(univ.Sequence):
    pass


NRST_RequestedAbonent.componentType = namedtype.NamedTypes(namedtype.NamedType('id', useful.ObjectDescriptor()), namedtype.NamedType('data', univ.Any()))

class NRST_RequestedAbonentsParameters(univ.Choice):
    pass


NRST_RequestedAbonentsParameters.componentType = namedtype.NamedTypes(namedtype.NamedType('separator', NRST_LogicalOperation().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('find-mask', NRST_RequestedAbonent().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.NamedType('recoded-find-mask', NRST_RecodedRequestedAbonent().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 100)))))

class NRST_RequestedAbonents(univ.SequenceOf):
    pass


NRST_RequestedAbonents.componentType = NRST_RequestedAbonentsParameters()

class NRST_ValidateIdentifiersTask(NRST_RequestedAbonents):
    pass


class NRST_AbonentsTask(univ.Choice):
    pass


NRST_AbonentsTask.componentType = namedtype.NamedTypes(namedtype.NamedType('validate-abonents-task', NRST_ValidateAbonentsTask().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('validate-identifiers', NRST_ValidateIdentifiersTask().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.NamedType('validate-services', NRST_ValidateServicesTask().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))))

class NRST_Acknowledgement(univ.Sequence):
    pass


NRST_Acknowledgement.componentType = namedtype.NamedTypes(namedtype.NamedType('successful', univ.Boolean()), namedtype.OptionalNamedType('broken-record', univ.Integer()), namedtype.OptionalNamedType('error-description', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 1024)))))

class NRST_AdjustmentRequest(univ.Sequence):
    pass


NRST_AdjustmentRequest.componentType = namedtype.NamedTypes(namedtype.NamedType('supports', univ.SequenceOf(componentType=(useful.ObjectDescriptor()))))

class NRST_AdjustmentResponse(univ.Null):
    pass


class NRST_AttributeType(univ.Enumerated):
    pass


NRST_AttributeType.namedValues = namedval.NamedValues(
    ('date-time', 0),
    ('integer', 1),
    ('string', 2),
    ('boolean', 3),
    ('float', 4),
    ('location', 5),
    ('empty', 6)
)

class NRST_ValidateBalanceFillupRecord(univ.Sequence):
    pass


NRST_ValidateBalanceFillupRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('pay-type-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('device-id', NRST_ReportedIdentifier()), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.OptionalNamedType('pay-parameters', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 512)))))

class NRST_BalanceFillupReportData(univ.SequenceOf):
    pass


NRST_BalanceFillupReportData.componentType = NRST_ValidateBalanceFillupRecord()

class NRST_ValidateBankAccountTransferRecord(univ.Sequence):
    pass


NRST_ValidateBankAccountTransferRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('donated-id', NRST_ReportedIdentifier()), namedtype.NamedType('bank-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))), namedtype.NamedType('bank-account', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))))

class NRST_BankAccountTransferReportData(univ.SequenceOf):
    pass


NRST_BankAccountTransferReportData.componentType = NRST_ValidateBankAccountTransferRecord()

class NRST_ValidateBankCardTransferRecord(univ.Sequence):
    pass


NRST_ValidateBankCardTransferRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('donanted-id', NRST_ReportedIdentifier()), namedtype.NamedType('bank-card-id', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 12)))), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))))

class NRST_BankCardTransferReportData(univ.SequenceOf):
    pass


NRST_BankCardTransferReportData.componentType = NRST_ValidateBankCardTransferRecord()

class NRST_ValidateBankDivisionTransferRecord(univ.Sequence):
    pass


NRST_ValidateBankDivisionTransferRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('donanted-id', NRST_ReportedIdentifier()), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('person-received', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 512)))), namedtype.NamedType('bank-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))), namedtype.NamedType('bank-division-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 512)))), namedtype.NamedType('bank-division-address', NRST_ReportedAddress()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))))

class NRST_BankDivisionTransferReportData(univ.SequenceOf):
    pass


NRST_BankDivisionTransferReportData.componentType = NRST_ValidateBankDivisionTransferRecord()

class NRST_BankTransactionRecord(univ.Sequence):
    pass


NRST_BankTransactionRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('device-id', NRST_ReportedIdentifier()), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('bank-account', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.NamedType('bank-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 512)))), namedtype.NamedType('bank-address', NRST_ReportedAddress()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))))

class NRST_BankTransactionReportData(univ.SequenceOf):
    pass


NRST_BankTransactionReportData.componentType = NRST_BankTransactionRecord()

class NRST_BroadbandWirelessParameters(univ.Sequence):
    pass


NRST_BroadbandWirelessParameters.componentType = namedtype.NamedTypes(namedtype.NamedType('azimuth', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(-1, 359)))), namedtype.NamedType('width', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 359)))), namedtype.NamedType('horizon-angle', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 359)))), namedtype.OptionalNamedType('power', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 25000))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('frequency-start', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 10000000000))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.OptionalNamedType('frequency-stop', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 10000000000))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))), namedtype.OptionalNamedType('leaf-level', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(-45, 45))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))), namedtype.OptionalNamedType('vertical-lift', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 100))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))), namedtype.OptionalNamedType('gain-factor', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(-100, 100))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))), namedtype.OptionalNamedType('polarization', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(-45, 45))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6)))))

class NRST_WirelessAntenna(NRST_BroadbandWirelessParameters):
    pass


class NRST_BsCellType(univ.Enumerated):
    pass


NRST_BsCellType.namedValues = namedval.NamedValues(
    ('macro', 0),
    ('micro', 1),
    ('pico', 2),
    ('femto', 3)
)

class NRST_BsSetting(univ.Enumerated):
    pass


NRST_BsSetting.namedValues = namedval.NamedValues(('indoor', 0), ('outdoor', 1), ('underground',
                                                                                  2))

class NRST_BsGeneration(univ.Enumerated):
    pass


NRST_BsGeneration.namedValues = namedval.NamedValues(('g2', 0), ('g3', 1), ('g4', 2), ('g5',
                                                                                       3))

class NRST_GsmAntenna(univ.Sequence):
    pass


NRST_GsmAntenna.componentType = namedtype.NamedTypes(namedtype.NamedType('azimut', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(-1, 359)))), namedtype.NamedType('width', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 359)))), namedtype.NamedType('horizon-angle', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 359)))), namedtype.OptionalNamedType('power', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 25000))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('frequency', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 10000000000))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.OptionalNamedType('vertical-lift', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 100))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))), namedtype.OptionalNamedType('gain-factor', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(-100, 100))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))), namedtype.OptionalNamedType('polarization', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(-45, 45))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))), namedtype.OptionalNamedType('setting', NRST_BsSetting().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))), namedtype.OptionalNamedType('thickness', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 359))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6)))), namedtype.OptionalNamedType('generation', NRST_BsGeneration().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7)))), namedtype.OptionalNamedType('controller-num', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8)))), namedtype.OptionalNamedType('bcc-ncc', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9)))), namedtype.OptionalNamedType('cell-type', NRST_BsCellType().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10)))), namedtype.OptionalNamedType('radiation-class', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11)))), namedtype.OptionalNamedType('name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12)))), namedtype.OptionalNamedType('channel', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13)))))

class NRST_CdmaAntenna(NRST_BroadbandWirelessParameters):
    pass


class NRST_BasicStationAntenna(univ.Choice):
    pass


NRST_BasicStationAntenna.componentType = namedtype.NamedTypes(namedtype.NamedType('gsm-antenna', NRST_GsmAntenna().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.NamedType('cdma-antenna', univ.SequenceOf(componentType=(NRST_CdmaAntenna())).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.NamedType('wireless-antenna', univ.SequenceOf(componentType=(NRST_WirelessAntenna())).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))))

class NRST_IPPort(univ.OctetString):
    pass


NRST_IPPort.subtypeSpec = constraint.ValueSizeConstraint(2, 2)

class NRST_NetworkPeerInfo(univ.Sequence):
    pass


NRST_NetworkPeerInfo.componentType = namedtype.NamedTypes(namedtype.NamedType('ip-address', NRST_IPAddress()), namedtype.OptionalNamedType('ip-port', NRST_IPPort()))

class NRST_IPList(univ.SequenceOf):
    pass


NRST_IPList.componentType = NRST_NetworkPeerInfo()

class NRST_WirelessIdentifiers(univ.Sequence):
    pass


NRST_WirelessIdentifiers.componentType = namedtype.NamedTypes(namedtype.NamedType('cell', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.OptionalNamedType('ip-list', NRST_IPList()), namedtype.OptionalNamedType('mac', univ.OctetString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(6, 6)))))

class NRST_TelephoneIdentifiers(univ.Sequence):
    pass


NRST_TelephoneIdentifiers.componentType = namedtype.NamedTypes(namedtype.NamedType('lac', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 65535)))), namedtype.NamedType('cell', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.OptionalNamedType('cell-sign', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 18)))))

class NRST_BasicStationIdentifiers(univ.Choice):
    pass


NRST_BasicStationIdentifiers.componentType = namedtype.NamedTypes(namedtype.NamedType('telepone', NRST_TelephoneIdentifiers().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.NamedType('wireless', univ.SequenceOf(componentType=(NRST_WirelessIdentifiers())).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))))

class NRST_BasicStationType(univ.Enumerated):
    pass


NRST_BasicStationType.namedValues = namedval.NamedValues(
    ('gsm', 0),
    ('cdma', 1),
    ('umts', 2),
    ('wifi', 3),
    ('wimax', 4)
)

class NRST_BasicStationSectorRecord(univ.Sequence):
    pass


NRST_BasicStationSectorRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('begin-time', NRST_DateAndTime()), namedtype.NamedType('end-time', NRST_DateAndTime()), namedtype.NamedType('address', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))), namedtype.NamedType('sector-identifiers', NRST_BasicStationIdentifiers()), namedtype.NamedType('antenna-configuration', NRST_BasicStationAntenna()), namedtype.NamedType('station-type', NRST_BasicStationType()), namedtype.OptionalNamedType('structured-address', NRST_ReportedAddress().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.OptionalNamedType('location', NRST_GeoLocation().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))))

class NRST_BasicStationsSectorRecordsData(univ.SequenceOf):
    pass


NRST_BasicStationsSectorRecordsData.componentType = NRST_BasicStationSectorRecord()

class NRST_Bunch(univ.Choice):
    pass


NRST_Bunch.componentType = namedtype.NamedTypes(namedtype.NamedType('gsm', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('cdma-umts', NRST_DataNetworkEquipment().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))))

class NRST_BunchMapPoint(univ.Sequence):
    pass


NRST_BunchMapPoint.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('switch-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128)))), namedtype.NamedType('bunch-id', NRST_Bunch()))

class NRST_BunchRecord(univ.Sequence):
    pass


NRST_BunchRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('bunch-id', NRST_Bunch()), namedtype.NamedType('switch-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128)))), namedtype.NamedType('bunch-type', univ.Enumerated(namedValues=(namedval.NamedValues(('inbound',
                                                                                                                                                                                                                                                                                                                                                              0), ('outbound',
                                                                                                                                                                                                                                                                                                                                                                   1), ('bidirectional',
                                                                                                                                                                                                                                                                                                                                                                        3))))), namedtype.NamedType('begin-time', NRST_DateAndTime()), namedtype.OptionalNamedType('end-time', NRST_DateAndTime()), namedtype.NamedType('description', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))))

class NRST_BunchesMapRecord(univ.Sequence):
    pass


NRST_BunchesMapRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('a-bunch', NRST_BunchMapPoint()), namedtype.NamedType('b-bunch', NRST_BunchMapPoint()), namedtype.NamedType('begin-time', NRST_DateAndTime()), namedtype.OptionalNamedType('end-time', NRST_DateAndTime()))


class NRST_BunchesMapRecordsData(univ.SequenceOf):
    pass


NRST_BunchesMapRecordsData.componentType = NRST_BunchesMapRecord()


class NRST_BunchesRecordsData(univ.SequenceOf):
    pass


NRST_BunchesRecordsData.componentType = NRST_BunchRecord()


class NRST_CallsTypesRecord(univ.Sequence):
    pass


NRST_CallsTypesRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('call-type-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('begin-time', NRST_DateAndTime()), namedtype.OptionalNamedType('end-time', NRST_DateAndTime()), namedtype.NamedType('description', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))))


class NRST_CallTypesRecordsData(univ.SequenceOf):
    pass


NRST_CallTypesRecordsData.componentType = NRST_CallsTypesRecord()


class NRST_CallsRecords(univ.Sequence):
    pass


NRST_CallsRecords.componentType = namedtype.NamedTypes(namedtype.NamedType('id', useful.ObjectDescriptor()), namedtype.NamedType('data', univ.Any()))


class NRST_ModuleId(univ.OctetString):
    pass


NRST_ModuleId.subtypeSpec = constraint.ValueSizeConstraint(8, 8)


class NRST_RequestedHardwareModules(univ.SequenceOf):
    pass


NRST_RequestedHardwareModules.componentType = NRST_ModuleId()


class NRST_RequestedSoftwareModules(univ.SequenceOf):
    pass


NRST_RequestedSoftwareModules.componentType = NRST_ModuleId()


class NRST_RequestedModulesList(univ.Choice):
    pass


NRST_RequestedModulesList.componentType = namedtype.NamedTypes(namedtype.NamedType('hw-modules', NRST_RequestedHardwareModules().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('sw-modules', NRST_RequestedSoftwareModules().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))))


class NRST_CheckModuleRequest(NRST_RequestedModulesList):
    pass


class NRST_ParameterValue(univ.Choice):
    pass


NRST_ParameterValue.componentType = namedtype.NamedTypes(namedtype.NamedType('string', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('integer', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 999999999))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.NamedType('boolean', univ.Boolean().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))))


class NRST_ModuleParameter(univ.Sequence):
    pass


NRST_ModuleParameter.componentType = namedtype.NamedTypes(namedtype.NamedType('parameter-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))), namedtype.NamedType('read-only', univ.Boolean()), namedtype.NamedType('parameter-value', NRST_ParameterValue()))


class NRST_ModuleParameters(univ.SequenceOf):
    pass


NRST_ModuleParameters.componentType = NRST_ModuleParameter()


class NRST_SubmodulesList(univ.SequenceOf):
    pass


class NRST_SormSoftwareModule(univ.Sequence):
    pass


NRST_SubmodulesList.componentType = NRST_SormSoftwareModule()
NRST_SormSoftwareModule.componentType = namedtype.NamedTypes(namedtype.NamedType('module-id', NRST_ModuleId()), namedtype.NamedType('hardware-module-id', NRST_ModuleId()), namedtype.NamedType('block-name', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 1024)))), namedtype.NamedType('module-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 512)))), namedtype.NamedType('module-type', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(1, 512)))), namedtype.NamedType('module-parameters', NRST_ModuleParameters()), namedtype.OptionalNamedType('sub-modules-list', NRST_SubmodulesList()))


class NRST_SormSoftwareModules(univ.SequenceOf):
    pass


NRST_SormSoftwareModules.componentType = NRST_SormSoftwareModule()


class NRST_HwParameterGroup(univ.Sequence):
    pass


NRST_HwParameterGroup.componentType = namedtype.NamedTypes(namedtype.NamedType('group-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 512)))), namedtype.NamedType('module-parameters', NRST_ModuleParameters()))


class NRST_HwParameterGroups(univ.SequenceOf):
    pass


NRST_HwParameterGroups.componentType = NRST_HwParameterGroup()


class NRST_SormHardwareModule(univ.Sequence):
    pass


NRST_SormHardwareModule.componentType = namedtype.NamedTypes(namedtype.NamedType('module-id', NRST_ModuleId()), namedtype.NamedType('block-name', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 1024)))), namedtype.NamedType('module-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 512)))), namedtype.NamedType('module-parameters', NRST_HwParameterGroups()))


class NRST_SormHardwareModules(univ.SequenceOf):
    pass


NRST_SormHardwareModules.componentType = NRST_SormHardwareModule()


class NRST_CheckModuleResponse(univ.Choice):
    pass


NRST_CheckModuleResponse.componentType = namedtype.NamedTypes(namedtype.NamedType('hw-modules', NRST_SormHardwareModules().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('sw-modules', NRST_SormSoftwareModules().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))))


class NRST_ConfiguratedModule(univ.Choice):
    pass


NRST_ConfiguratedModule.componentType = namedtype.NamedTypes(namedtype.NamedType('sw-module', NRST_SormSoftwareModule().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.NamedType('hw-module', NRST_SormHardwareModule().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))))


class NRST_ConnectRequest(univ.Sequence):
    pass


NRST_ConnectRequest.componentType = namedtype.NamedTypes(namedtype.NamedType('session-timeout', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(60, 2592000)))), namedtype.NamedType('max-data-length', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(10, 100000)))), namedtype.NamedType('data-packet-window-size', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(4, 256)))), namedtype.NamedType('data-load-timeout', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(1, 60)))), namedtype.NamedType('request-response-timeout', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(1, 60)))), namedtype.NamedType('data-packet-response-timeout', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(1, 60)))), namedtype.DefaultedNamedType('time-offset', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(-1440, 1440))).subtype(value=0)))


class NRST_ConnectResponse(univ.Sequence):
    pass


NRST_ConnectResponse.componentType = namedtype.NamedTypes(namedtype.NamedType('confirmed-data-packet-window-size', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(4, 256)))), namedtype.NamedType('confirmed-session-timeout', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(60, 2592000)))), namedtype.NamedType('confirmed-data-load-timeout', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(1, 60)))), namedtype.NamedType('confirmed-request-response-timeout', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(1, 60)))), namedtype.NamedType('supports', univ.SequenceOf(componentType=(useful.ObjectDescriptor()))))


class NRST_FindRange(univ.Sequence):
    pass


NRST_FindRange.componentType = namedtype.NamedTypes(namedtype.OptionalNamedType('begin-find', NRST_DateAndTime().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('end-find', NRST_DateAndTime().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))))


class NRST_StandardInterval(univ.Sequence):
    pass


NRST_StandardInterval.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('standard', NRST_NetworkType()), namedtype.NamedType('range', NRST_FindRange()), namedtype.OptionalNamedType('count', univ.Integer()))


class NRST_ConnectionsPresenseRecord(univ.Sequence):
    pass


NRST_ConnectionsPresenseRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('standard-interval', NRST_StandardInterval()),
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


class NRST_ConnectionsPresenceData(univ.SequenceOf):
    pass


NRST_ConnectionsPresenceData.componentType = NRST_ConnectionsPresenseRecord()


class NRST_ConnectionsReport(NRST_CallsRecords):
    pass


class NRST_RequestedConnection(univ.Sequence):
    pass


NRST_RequestedConnection.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class NRST_VoipProtocol(univ.Enumerated):
    pass


NRST_VoipProtocol.namedValues = namedval.NamedValues(
    ('sip', 0),
    ('h323', 1),
    ('iax', 2),
    ('skype', 100)
)


class NRST_DataVoipNumber(univ.Sequence):
    pass


NRST_DataVoipNumber.componentType = namedtype.NamedTypes(
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


class NRST_RequestedVoipData(univ.Choice):
    pass


NRST_RequestedVoipData.componentType = namedtype.NamedTypes(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'server-info',
        NRST_NetworkPeerInfo().subtype(
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
        NRST_DataVoipNumber().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))
        )
    ),
    namedtype.NamedType(
        'voip-called-number',
        NRST_DataVoipNumber().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7)
            )
        )
    ),
    namedtype.NamedType(
        'inbound-bunch',
        NRST_Bunch().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8)
            )
        )
    ),
    namedtype.NamedType(
        'outbound-bunch',
        NRST_Bunch().subtype(
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
        NRST_VoipProtocol().subtype(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20)
            )
        )
    ),
    namedtype.NamedType(
        'location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21)
            )
        )
    )
)


class NRST_RequestedConnectionMobileIdentifier(univ.Sequence):
    pass


NRST_RequestedConnectionMobileIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class NRST_PhoneAbonentType(univ.Enumerated):
    pass


NRST_PhoneAbonentType.namedValues = namedval.NamedValues(
    ('local', 0),
    ('network', 1),
    ('roamer', 2),
    ('undefined', 3))


class NRST_RecodedRequestedConnectionMobileIdentifier(univ.Choice):
    pass


NRST_RecodedRequestedConnectionMobileIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'gsm-identifier',
        NRST_RequestedGsmIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'cdma-identifier',
        NRST_RequestedCdmaIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class NRST_RequestedConnectionMobileData(univ.Choice):
    pass


NRST_RequestedConnectionMobileData.componentType = namedtype.NamedTypes(
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
        NRST_PhoneAbonentType().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'out-abonent-type',
        NRST_PhoneAbonentType().subtype(
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
        NRST_Bunch().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6)
            )
        )
    ),
    namedtype.NamedType(
        'outbound-bunch',
        NRST_Bunch().subtype(
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
        NRST_RequestedConnectionMobileIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-in-info',
        NRST_RecodedRequestedConnectionMobileIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 111)
            )
        )
    ),
    namedtype.NamedType(
        'in-end-location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12)
            )
        )
    ),
    namedtype.NamedType(
        'in-begin-location',
        NRST_Location().subtype(
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
        NRST_RequestedConnectionMobileIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-out-info',
        NRST_RecodedRequestedConnectionMobileIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 115)
            )
        )
    ),
    namedtype.NamedType(
        'out-begin-location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 16)
            )
        )
    ),
    namedtype.NamedType(
        'out-end-location',
        NRST_Location().subtype(
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


class NRST_RequestedAddressTranslationsData(univ.Choice):
    pass


NRST_RequestedAddressTranslationsData.componentType = namedtype.NamedTypes(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.NamedType(
        'public-ip',
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
            )
        )
    ),
    namedtype.NamedType(
        'destination-ip',
        NRST_NetworkPeerInfo().subtype(
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


class NRST_RequestedFileTransferData(univ.Choice):
    pass


NRST_RequestedFileTransferData.componentType = namedtype.NamedTypes(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'server-info',
        NRST_NetworkPeerInfo().subtype(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 20)
            )
        )
    ), namedtype.NamedType(
        'location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21)
            )
        )
    )
)


class NRST_RequestedConnectionPstnIdentifier(univ.Sequence):
    pass


NRST_RequestedConnectionPstnIdentifier.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', NRST_RequestedPstnIdentifier())
)


class NRST_RequestedConnectionPstnData(univ.Choice):
    pass


NRST_RequestedConnectionPstnData.componentType = namedtype.NamedTypes(
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
        NRST_PhoneAbonentType().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.NamedType(
        'out-abonent-type',
        NRST_PhoneAbonentType().subtype(
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
        NRST_RequestedConnectionPstnIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.NamedType(
        'out-info',
        NRST_RequestedConnectionPstnIdentifier().subtype(
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


class NRST_RequestedTermAccessData(univ.Choice):
    pass


NRST_RequestedTermAccessData.componentType = namedtype.NamedTypes(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'server-info',
        NRST_NetworkPeerInfo().subtype(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10)
            )
        )
    ),
    namedtype.NamedType(
        'location',
        NRST_Location().subtype(
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


class NRST_RequestedRawFlowsData(univ.Choice):
    pass


NRST_RequestedRawFlowsData.componentType = namedtype.NamedTypes(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'server-info',
        NRST_NetworkPeerInfo().subtype(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10)
            )
        )
    ),
    namedtype.NamedType(
        'location',
        NRST_Location().subtype(
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


class NRST_RequestedAAALoginData(univ.Choice):
    pass


NRST_RequestedAAALoginData.componentType = namedtype.NamedTypes(
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
        NRST_DataNetworkEquipment().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'allocated-ip',
        NRST_IPAddress().subtype(
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
        NRST_NetworkPeerInfo().subtype(
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
        NRST_IPAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.NamedType(
        'ggsn-ip',
        NRST_IPAddress().subtype(
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
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 14)
            )
        )
    ),
    namedtype.NamedType(
        'location-end',
        NRST_Location().subtype(
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


class NRST_RequestedEmailData(univ.Choice):
    pass


NRST_RequestedEmailData.componentType = namedtype.NamedTypes(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'server-info',
        NRST_NetworkPeerInfo().subtype(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21)
            )
        )
    ),
    namedtype.NamedType(
        'location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22)
            )
        )
    )
)


class NRST_RequestedConnectionEntranceData(univ.Choice):
    pass


NRST_RequestedConnectionEntranceData.componentType = namedtype.NamedTypes(
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
        NRST_IPAddress().subtype(
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


class NRST_HttpMethod(univ.Enumerated):
    pass


NRST_HttpMethod.namedValues = namedval.NamedValues(
    ('get', 0),
    ('post', 1),
    ('put', 2),
    ('delete', 3)
)


class NRST_RequestedResourceData(univ.Choice):
    pass


NRST_RequestedResourceData.componentType = namedtype.NamedTypes(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'server-info',
        NRST_NetworkPeerInfo().subtype(
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
        NRST_HttpMethod().subtype(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10)
            )
        )
    ),
    namedtype.NamedType(
        'location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    )
)


class NRST_IMProtocol(univ.Enumerated):
    pass


NRST_IMProtocol.namedValues = namedval.NamedValues(
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


class NRST_RequestedImData(univ.Choice):
    pass


NRST_RequestedImData.componentType = namedtype.NamedTypes(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'server-info',
        NRST_NetworkPeerInfo().subtype(
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
        NRST_IMProtocol().subtype(
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
        NRST_NetworkPeerInfo().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 21)
            )
        )
    ),
    namedtype.NamedType(
        'location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 22)
            )
        )
    )
)


class NRST_RecodedRequestedConnection(univ.Choice):
    pass


NRST_RecodedRequestedConnection.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'pager-identifier',
        NRST_RequestedPagerIdentifier().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'pstn',
        NRST_RequestedConnectionPstnData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'mobile',
        NRST_RequestedConnectionMobileData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'entrance',
        NRST_RequestedConnectionEntranceData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ), namedtype.NamedType(
        'aaa-login',
        NRST_RequestedAAALoginData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
            )
        )
    ),
    namedtype.NamedType(
        'resource',
        NRST_RequestedResourceData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)
            )
        )
    ),
    namedtype.NamedType(
        'email',
        NRST_RequestedEmailData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6)
            )
        )
    ),
    namedtype.NamedType(
        'im',
        NRST_RequestedImData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7)
            )
        )
    ),
    namedtype.NamedType(
        'voip',
        NRST_RequestedVoipData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8)
            )
        )
    ),
    namedtype.NamedType(
        'file-transfer',
        NRST_RequestedFileTransferData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9)
            )
        )
    ),
    namedtype.NamedType(
        'term-access',
        NRST_RequestedTermAccessData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10)
            )
        )
    ),
    namedtype.NamedType(
        'raw-flows',
        NRST_RequestedRawFlowsData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.NamedType(
        'address-translations',
        NRST_RequestedAddressTranslationsData().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12)
            )
        )
    )
)


class NRST_RequestedConnectionParameter(univ.Choice):
    pass


NRST_RequestedConnectionParameter.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        NRST_LogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'find-mask',
        NRST_RequestedConnection().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-find-mask',
        NRST_RecodedRequestedConnection().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 101)
            )
        )
    )
)


class NRST_RequestedConnectionIdentifiers(univ.SequenceOf):
    pass


NRST_RequestedConnectionIdentifiers.componentType = NRST_RequestedConnectionParameter()


class NRST_ValidateEntranceTask(NRST_RequestedConnectionIdentifiers):
    pass


class NRST_ValidateDataTask(NRST_RequestedConnectionIdentifiers):
    pass


class NRST_ValidateConnectionsTask(NRST_RequestedConnectionIdentifiers):
    pass


class NRST_ConnectionsTask(univ.Choice):
    pass


NRST_ConnectionsTask.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'validate-connections',
        NRST_ValidateConnectionsTask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'validate-data',
        NRST_ValidateDataTask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'validate-entrance',
        NRST_ValidateEntranceTask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    )
)


class NRST_ControlCommandType(univ.Enumerated):
    pass


NRST_ControlCommandType.namedValues = namedval.NamedValues(
    ('start', 0),
    ('stop', 1)
)


class NRST_PortRange(univ.Sequence):
    pass


NRST_PortRange.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'port-from',
        NRST_IPPort().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'port-to',
        NRST_IPPort().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class NRST_IPV6Mask(univ.OctetString):
    pass


NRST_IPV6Mask.subtypeSpec = constraint.ValueSizeConstraint(16, 16)


class NRST_IPV4Mask(univ.OctetString):
    pass


NRST_IPV4Mask.subtypeSpec = constraint.ValueSizeConstraint(4, 4)


class NRST_IPMask(univ.Choice):
    pass


NRST_IPMask.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'ipv4-mask',
        NRST_IPV4Mask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'ipv6-mask',
        NRST_IPV6Mask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class NRST_IPFilterMask(univ.Sequence):
    pass


NRST_IPFilterMask.componentType = namedtype.NamedTypes(
    namedtype.NamedType('mask', NRST_IPMask()),
    namedtype.NamedType('mask-length', univ.Integer())
)


class NRST_FilterSingleCriteria(univ.Choice):
    pass


NRST_FilterSingleCriteria.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'ip-address',
        NRST_IPAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'ip-port',
        NRST_IPPort().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'port-range',
        NRST_PortRange().subtype(
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
        NRST_IPFilterMask().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12)
            )
        )
    )
)


class NRST_FilterPairCriteria(univ.Sequence):
    pass


NRST_FilterPairCriteria.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'criteria-a',
        NRST_FilterSingleCriteria().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'criteria-b',
        NRST_FilterSingleCriteria().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class NRST_FilterParameter(univ.Choice):
    pass


NRST_FilterParameter.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'single-criteria',
        NRST_FilterSingleCriteria().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'pair-criteria',
        NRST_FilterPairCriteria().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class NRST_FilterParameters(univ.SequenceOf):
    pass


NRST_FilterParameters.componentType = NRST_FilterParameter()


class NRST_FilterID(univ.Integer):
    pass


class NRST_CreateFilterRequest(univ.Sequence):
    pass


NRST_CreateFilterRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType('filter-id', NRST_FilterID()),
    namedtype.NamedType('filter-parameters', NRST_FilterParameters()),
    namedtype.DefaultedNamedType(
        'allow-only-mode', univ.Boolean().subtype(value=1)
    )
)


class NRST_CreateFilterResponse(univ.Sequence):
    pass


NRST_CreateFilterResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('filter-id', NRST_FilterID()),
    namedtype.NamedType('successful', univ.Boolean()),
    namedtype.OptionalNamedType(
        'error-description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class NRST_TelcoList(univ.SequenceOf):
    pass


NRST_TelcoList.componentType = NRST_TelcoID()


class NRST_DataContentID(char.UTF8String):
    pass


NRST_DataContentID.subtypeSpec = constraint.ValueSizeConstraint(1, 512)


class NRST_DataContentTask(NRST_DataContentID):
    pass


class NRST_PaymentsTask(univ.Sequence):
    pass


NRST_PaymentsTask.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class NRST_RequestedServiceCenterPaysParameters(univ.Choice):
    pass


NRST_RequestedServiceCenterPaysParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        NRST_LogicalOperation().subtype(
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
        NRST_RequestedAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    )
)


class NRST_RequestedServiceCenterPays(univ.SequenceOf):
    pass


NRST_RequestedServiceCenterPays.componentType = NRST_RequestedServiceCenterPaysParameters()


class NRST_RequestedTransferParameters(univ.Choice):
    pass


NRST_RequestedTransferParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        NRST_LogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'source-identifier',
        NRST_RequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-source-identifier',
        NRST_RecodedRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 101)
            )
        )
    )
)


class NRST_RequestedBankDivisionTransferPays(univ.SequenceOf):
    pass


NRST_RequestedBankDivisionTransferPays.componentType = NRST_RequestedTransferParameters()


class NRST_RequestedBankTransactionPaysParameters(univ.Choice):
    pass


NRST_RequestedBankTransactionPaysParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        NRST_LogicalOperation().subtype(
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


class NRST_RequestedBankTransactionPays(univ.SequenceOf):
    pass


NRST_RequestedBankTransactionPays.componentType = NRST_RequestedBankTransactionPaysParameters()


class NRST_RequestedExpressPaysParameters(univ.Choice):
    pass


NRST_RequestedExpressPaysParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        NRST_LogicalOperation().subtype(
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


class NRST_RequestedExpressPays(univ.SequenceOf):
    pass


NRST_RequestedExpressPays.componentType = NRST_RequestedExpressPaysParameters()


class NRST_RequestedCrossAccountPaysParameters(univ.Choice):
    pass


NRST_RequestedCrossAccountPaysParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        NRST_LogicalOperation().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)
            )
        )
    ),
    namedtype.NamedType(
        'source-identifier',
        NRST_RequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'dest-identifier',
        NRST_RequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-source-identifier',
        NRST_RecodedRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 101)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-dest-identifier',
        NRST_RecodedRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 102)
            )
        )
    )
)


class NRST_RequestedCrossAccountPays(univ.SequenceOf):
    pass


NRST_RequestedCrossAccountPays.componentType = NRST_RequestedCrossAccountPaysParameters()


class NRST_RequestedBankAccountTransferPays(univ.SequenceOf):
    pass


NRST_RequestedBankAccountTransferPays.componentType = NRST_RequestedTransferParameters()


class NRST_RequestedTerminalPaysParameters(univ.Choice):
    pass


NRST_RequestedTerminalPaysParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        NRST_LogicalOperation().subtype(
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
        NRST_RequestedAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    )
)


class NRST_RequestedTerminalPays(univ.SequenceOf):
    pass


NRST_RequestedTerminalPays.componentType = NRST_RequestedTerminalPaysParameters()


class NRST_RequestedBalanceFillupsParameters(univ.Choice):
    pass


NRST_RequestedBalanceFillupsParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        NRST_LogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'identifier',
        NRST_RequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'recoded-identifier',
        NRST_RecodedRequestedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 101)
            )
        )
    )
)


class NRST_RequestedBalanceFillups(univ.SequenceOf):
    pass


NRST_RequestedBalanceFillups.componentType = NRST_RequestedBalanceFillupsParameters()


class NRST_RequestedTelephoneCardPaysParameters(univ.Choice):
    pass


NRST_RequestedTelephoneCardPaysParameters.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        NRST_LogicalOperation().subtype(
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


class NRST_RequestedTelephoneCardPays(univ.SequenceOf):
    pass


NRST_RequestedTelephoneCardPays.componentType = NRST_RequestedTelephoneCardPaysParameters()


class NRST_RequestedBankCardTransferPays(univ.SequenceOf):
    pass


NRST_RequestedBankCardTransferPays.componentType = NRST_RequestedTransferParameters()


class NRST_RecodedPaymentsTask(univ.Choice):
    pass


NRST_RecodedPaymentsTask.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'bank-transaction',
        NRST_RequestedBankTransactionPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'express-card',
        NRST_RequestedExpressPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'public-terminal',
        NRST_RequestedTerminalPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.NamedType(
        'service-center',
        NRST_RequestedServiceCenterPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'cross-account',
        NRST_RequestedCrossAccountPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'telephone-card',
        NRST_RequestedTelephoneCardPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5))
        )
    ),
    namedtype.NamedType(
        'balance-fill-up',
        NRST_RequestedBalanceFillups().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    ),
    namedtype.NamedType(
        'bank-division-transfer',
        NRST_RequestedBankDivisionTransferPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))
        )
    ),
    namedtype.NamedType(
        'bank-card-transfer',
        NRST_RequestedBankCardTransferPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8))
        )
    ),
    namedtype.NamedType(
        'bank-account-transfer',
        NRST_RequestedBankAccountTransferPays().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9))
        )
    )
)


class NRST_DictionaryTask(univ.Sequence):
    pass


NRST_DictionaryTask.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', useful.ObjectDescriptor())
)


class NRST_PresenseInfoData(univ.Enumerated):
    pass


NRST_PresenseInfoData.namedValues = namedval.NamedValues(
    ('subscribers', 0),
    ('connections', 1),
    ('payments', 2),
    ('dictionaries', 3),
    ('locations', 4)
)


class NRST_PresenseTask(univ.Sequence):
    pass


NRST_PresenseTask.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', NRST_PresenseInfoData())
)


class NRST_RequestedLocationIdentifier(univ.Choice):
    pass


NRST_RequestedLocationIdentifier.componentType = namedtype.NamedTypes(
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
        NRST_IPAddress().subtype(
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


class NRST_LocationTask(NRST_RequestedLocationIdentifier):
    pass


class NRST_CreateTaskRequest(univ.Sequence):
    pass


NRST_CreateTaskRequest.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType(
        'telcos', NRST_TelcoList().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.OptionalNamedType(
        'range',
        NRST_FindRange().subtype(
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
                        NRST_DictionaryTask().subtype(
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
                        NRST_AbonentsTask().subtype(
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
                        NRST_ConnectionsTask().subtype(
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
                        NRST_LocationTask().subtype(
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
                        NRST_PaymentsTask().subtype(
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
                        NRST_PresenseTask().subtype(
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
                        NRST_DataContentTask().subtype(
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
                        NRST_RecodedPaymentsTask().subtype(
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


class NRST_TaskID(univ.Integer):
    pass


NRST_TaskID.subtypeSpec = constraint.ValueRangeConstraint(0, 4294967295)


class NRST_CreateTaskResponse(univ.Sequence):
    pass


NRST_CreateTaskResponse.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('task-id', NRST_TaskID()),
    namedtype.NamedType('successful', univ.Boolean()),
    namedtype.OptionalNamedType(
        'error-description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class NRST_CrossAccountRecord(univ.Sequence):
    pass


NRST_CrossAccountRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', NRST_TelcoID()),
    namedtype.NamedType('device-id', NRST_ReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', NRST_DateAndTime()),
    namedtype.NamedType('donanted-id', NRST_ReportedIdentifier()),
    namedtype.NamedType(
        'amount',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 64))
        )
    )
)


class NRST_CrossAccountReportData(univ.SequenceOf):
    pass


NRST_CrossAccountReportData.componentType = NRST_CrossAccountRecord()


class NRST_DataAAARecordContent(univ.Sequence):
    pass


NRST_DataAAARecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', NRST_TelcoID()),
    namedtype.NamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        )
    ),
    namedtype.NamedType('aaa-connection-time', NRST_DateAndTime()),
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
    namedtype.NamedType('aaa-allocated-ip', NRST_IPAddress()),
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
    namedtype.NamedType('aaa-nas', NRST_NetworkPeerInfo()),
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
        NRST_DataNetworkEquipment().subtype(
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
        NRST_IPAddress().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'aaa-ggsn-ip',
        NRST_IPAddress().subtype(
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
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'aaa-location-end',
        NRST_Location().subtype(
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
        NRST_IPMask().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 15)
            )
        )
    )
)


class NRST_DataAAARecordData(univ.SequenceOf):
    pass


NRST_DataAAARecordData.componentType = NRST_DataAAARecordContent()


class NRST_DataAddressTranslationRecordContent(univ.Sequence):
    pass


NRST_DataAddressTranslationRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', NRST_TelcoID()),
    namedtype.NamedType(
        'point-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 1000))
        )
    ),
    namedtype.NamedType('translation-time', NRST_DateAndTime()),
    namedtype.NamedType(
        'record-type',
        univ.Enumerated(
            namedValues=(
                namedval.NamedValues(('session-start', 0), ('session-end', 1))
            )
        )
    ),
    namedtype.NamedType('private-ip', NRST_NetworkPeerInfo()),
    namedtype.NamedType('public-ip', NRST_NetworkPeerInfo()),
    namedtype.NamedType('destination-ip', NRST_NetworkPeerInfo()),
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


class NRST_DataAddressTranslationRecordData(univ.SequenceOf):
    pass


NRST_DataAddressTranslationRecordData.componentType = NRST_DataAddressTranslationRecordContent()


class NRST_DataContentRawDirection(univ.Enumerated):
    pass


NRST_DataContentRawDirection.namedValues = namedval.NamedValues(
    ('client-server', 0),
    ('server-client', 1)
)


class NRST_DataContentReport(univ.Sequence):
    pass


NRST_DataContentReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)


class NRST_DataDropRequest(NRST_TaskID):
    pass


class NRST_DataDropResponse(univ.Sequence):
    pass


NRST_DataDropResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('task-id', NRST_TaskID()),
    namedtype.NamedType('successful', univ.Boolean()),
    namedtype.OptionalNamedType(
        'error-description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class NRST_EmailEvent(univ.Enumerated):
    pass


NRST_EmailEvent.namedValues = namedval.NamedValues(
    ('email-send', 1),
    ('email-receive', 2),
    ('email-download', 3),
    ('email-logon-attempt', 4),
    ('email-logon', 5),
    ('email-logon-failure', 6),
    ('email-logoff', 7),
    ('email-partial-download', 8)
)


class NRST_IP_AAAResult(univ.Enumerated):
    pass


NRST_IP_AAAResult.namedValues = namedval.NamedValues(
    ('aaaUnknown', 1),
    ('aaaFailed', 2),
    ('aaaSucceeded', 3)
)


class NRST_IP_AAAInformation(univ.Sequence):
    pass


NRST_IP_AAAInformation.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'username',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
        )
    ),
    namedtype.OptionalNamedType('aaaResult', NRST_IP_AAAResult()))


class NRST_DataNetworkCdrHeaderData(univ.Sequence):
    pass


NRST_DataNetworkCdrHeaderData.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', NRST_TelcoID()),
    namedtype.NamedType('begin-connection-time', NRST_DateAndTime()),
    namedtype.NamedType('end-connection-time', NRST_DateAndTime()),
    namedtype.NamedType('client-info', NRST_NetworkPeerInfo()),
    namedtype.NamedType('server-info', NRST_NetworkPeerInfo()),
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


class NRST_DataNetworkCdrHeader(univ.Sequence):
    pass


NRST_DataNetworkCdrHeader.componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', NRST_DataNetworkCdrHeaderData())
)


class NRST_DataEmailRecordContentAAA(univ.Sequence):
    pass


NRST_DataEmailRecordContentAAA.componentType = namedtype.NamedTypes(
    namedtype.NamedType('mail-cdr-header', NRST_DataNetworkCdrHeader()),
    namedtype.NamedType('mail-event', NRST_EmailEvent()),
    namedtype.NamedType('mail-aaa-info', NRST_IP_AAAInformation()),
    namedtype.OptionalNamedType(
        'mail-message',
        char.UTF8String().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'mail-nat-info',
        univ.SequenceOf(
            componentType=(NRST_NetworkPeerInfo())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))
        )
    ),
    namedtype.OptionalNamedType(
        'mail-location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'mail-data-content-id',
        NRST_DataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class NRST_EmailServers(univ.Sequence):
    pass


NRST_EmailServers.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'data',
        univ.SequenceOf(
            componentType=char.UTF8String().subtype(
                subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
            )
        )
    )
)


class NRST_EmailReceivers(univ.Sequence):
    pass


NRST_EmailReceivers.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'data',
        univ.SequenceOf(
            componentType=char.UTF8String().subtype(
                subtypeSpec=(constraint.ValueSizeConstraint(1, 512)))
        )
    )
)


class NRST_DataEmailRecordContentIPDR(univ.Sequence):
    pass


NRST_DataEmailRecordContentIPDR.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'mail-cdr-header',
        NRST_DataNetworkCdrHeader()
    ),
    namedtype.NamedType('mail-event', NRST_EmailEvent()),
    namedtype.NamedType(
        'mail-sender',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 512))
        )
    ),
    namedtype.NamedType('mail-receiver', NRST_EmailReceivers()),
    namedtype.NamedType('mail-cc', NRST_EmailReceivers()),
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
    namedtype.NamedType('mail-servers', NRST_EmailServers()),
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
            componentType=(NRST_NetworkPeerInfo())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))
        )
    ),
    namedtype.OptionalNamedType(
        'mail-location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'mail-data-content-id',
        NRST_DataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class NRST_DataEmailRecordContent(univ.Choice):
    pass


NRST_DataEmailRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'mail-aaa',
        NRST_DataEmailRecordContentAAA().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'mail-ipdr',
        NRST_DataEmailRecordContentIPDR().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    )
)


class NRST_DataEmailRecordData(univ.SequenceOf):
    pass


NRST_DataEmailRecordData.componentType = NRST_DataEmailRecordContent()


class NRST_DataFileTransferRecordContent(univ.Sequence):
    pass


NRST_DataFileTransferRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'file-cdr-header',
        NRST_DataNetworkCdrHeader()
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
            componentType=(NRST_NetworkPeerInfo())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'file-location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'file-data-content-id',
        NRST_DataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))
        )
    )
)


class NRST_DataFileTransferRecordData(univ.SequenceOf):
    pass


NRST_DataFileTransferRecordData.componentType = NRST_DataFileTransferRecordContent()


class NRST_ImReceiver(univ.Sequence):
    pass


NRST_ImReceiver.componentType = namedtype.NamedTypes(
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


class NRST_ImReceivers(univ.SequenceOf):
    pass


NRST_ImReceivers.componentType = NRST_ImReceiver()


class NRST_ImEvent(univ.Enumerated):
    pass


NRST_ImEvent.namedValues = namedval.NamedValues(
    ('im-undefined', 0),
    ('im-send', 1),
    ('im-receive', 2)
)


class NRST_DataImRecordContent(univ.Sequence):
    pass


NRST_DataImRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('im-cdr-header', NRST_DataNetworkCdrHeader()),
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
    namedtype.NamedType('im-receivers', NRST_ImReceivers()),
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
        NRST_IMProtocol().subtype(
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
        NRST_ImEvent().subtype(
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
            componentType=(NRST_NetworkPeerInfo())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11))
        )
    ),
    namedtype.OptionalNamedType(
        'im-location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 12)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'im-data-content-id',
        NRST_DataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class NRST_DataImRecordData(univ.SequenceOf):
    pass


NRST_DataImRecordData.componentType = NRST_DataImRecordContent()


class NRST_DataInterruptRequest(NRST_TaskID):
    pass


class NRST_MessageID(univ.Integer):
    pass


NRST_MessageID.subtypeSpec = constraint.ValueRangeConstraint(0, 4294967295)


class NRST_DataInterruptResponse(univ.Sequence):
    pass


NRST_DataInterruptResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('request-id', NRST_MessageID()),
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


class NRST_DataLoadRequest(NRST_TaskID):
    pass


class NRST_DataLoadResponse(univ.Sequence):
    pass


NRST_DataLoadResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('task-id', NRST_TaskID()),
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


class NRST_DataRawFlowsRecordContent(univ.Sequence):
    pass


NRST_DataRawFlowsRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('flow-cdr-header', NRST_DataNetworkCdrHeader()),
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
            componentType=(NRST_NetworkPeerInfo())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'flow-location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'flow-data-content-id',
        NRST_DataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12))
        )
    ),
    namedtype.OptionalNamedType(
        'sni',
        char.UTF8String(
        ).subtype(subtypeSpec=(constraint.ValueSizeConstraint(0, 128))
        ).subtype(implicitTag=(
            tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13))
        )
    )
)


class NRST_DataRawFlowsRecordData(univ.SequenceOf):
    pass


NRST_DataRawFlowsRecordData.componentType = NRST_DataRawFlowsRecordContent()


class NRST_DataReadyRequest(univ.Null):
    pass


class NRST_TaskResultStatus(univ.Enumerated):
    pass


NRST_TaskResultStatus.namedValues = namedval.NamedValues(
    ('data-not-ready', 0),
    ('data-ready', 1),
    ('data-not-found', 2),
    ('error', 3)
)


class NRST_TaskResult(univ.Sequence):
    pass


NRST_TaskResult.componentType = namedtype.NamedTypes(namedtype.NamedType('result', NRST_TaskResultStatus()), namedtype.OptionalNamedType('report-records-number', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 999999999999))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('report-limit-exeeded', univ.Boolean().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.OptionalNamedType('error-description', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))))


class NRST_DataReadyTaskRecord(univ.Sequence):
    pass


NRST_DataReadyTaskRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('task-id', NRST_TaskID()), namedtype.NamedType('result', NRST_TaskResult()))


class NRST_DataReadyResponse(univ.SequenceOf):
    pass


NRST_DataReadyResponse.componentType = NRST_DataReadyTaskRecord()

class NRST_DataResourceRecordContent(univ.Sequence):
    pass


NRST_DataResourceRecordContent.componentType = namedtype.NamedTypes(namedtype.NamedType('res-cdr-header', NRST_DataNetworkCdrHeader()), namedtype.NamedType('res-url', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 8192)))), namedtype.NamedType('res-bytes-count', univ.Integer()), namedtype.NamedType('res-term-cause', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 16384)))), namedtype.OptionalNamedType('res-aaa-info', NRST_IP_AAAInformation().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.OptionalNamedType('res-http-method', NRST_HttpMethod().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.OptionalNamedType('res-abonent-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(0, 64))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))), namedtype.OptionalNamedType('res-nat-info', univ.SequenceOf(componentType=(NRST_NetworkPeerInfo())).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10)))), namedtype.OptionalNamedType('res-location', NRST_Location().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)))), namedtype.OptionalNamedType('res-data-content-id', NRST_DataContentID().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12)))))

class NRST_DataResourceRecordData(univ.SequenceOf):
    pass


NRST_DataResourceRecordData.componentType = NRST_DataResourceRecordContent()

class NRST_RawDataType(univ.Enumerated):
    pass


NRST_RawDataType.namedValues = namedval.NamedValues(
    ('data-reports', 0),
    ('raw-cdr', 1),
    ('raw-ipdr', 2),
    ('raw-location', 10),
    ('raw-passive', 11)
)


class NRST_DataStartRequest(univ.Sequence):
    pass


NRST_DataStartRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType('time-from', NRST_DateAndTime()),
    namedtype.NamedType('time-to', NRST_DateAndTime()),
    namedtype.NamedType('raw-type', NRST_RawDataType())
)


class NRST_DataStartResponse(univ.Boolean):
    pass


class NRST_DataStopRequest(univ.Null):
    pass


class NRST_DataStopResponse(univ.Boolean):
    pass


class NRST_DataTermAccessRecordContent(univ.Sequence):
    pass


NRST_DataTermAccessRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('term-cdr-header', NRST_DataNetworkCdrHeader()),
    namedtype.NamedType('term-in-bytes-count', univ.Integer()),
    namedtype.NamedType('term-out-bytes-count', univ.Integer()),
    namedtype.OptionalNamedType(
        'term-protocol',
        univ.Enumerated(namedValues=(namedval.NamedValues(
        ('telnet', 0), ('ssh', 1), ('scp', 2))))
    ),
    namedtype.OptionalNamedType(
        'term-abonent-id',
        char.UTF8String().subtype(
        subtypeSpec=(constraint.ValueSizeConstraint(0, 64))
    ).subtype(
        implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))
    ),
    namedtype.OptionalNamedType(
        'term-nat-info',
        univ.SequenceOf(
            componentType=(NRST_NetworkPeerInfo())
        ).subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))
        )
    ),
    namedtype.OptionalNamedType(
        'term-location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'term-data-content-id',
        NRST_DataContentID().subtype(
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


class NRST_DataTermAccessRecordData(univ.SequenceOf):
    pass


NRST_DataTermAccessRecordData.componentType = NRST_DataTermAccessRecordContent()


class NRST_DataTypesRequest(NRST_RawDataType):
    pass


class NRST_DataTypesResponse(univ.Sequence):
    pass


NRST_DataTypesResponse.componentType = namedtype.NamedTypes(namedtype.NamedType('successful', univ.Boolean()), namedtype.NamedType('selected-type', NRST_RawDataType()), namedtype.NamedType('time-from', NRST_DateAndTime()), namedtype.NamedType('time-to', NRST_DateAndTime()))

class NRST_VoIPEvent(univ.Enumerated):
    pass


NRST_VoIPEvent.namedValues = namedval.NamedValues(('outgoing', 0), ('incoming', 1), ('unknown',
                                                                                     2))

class NRST_DataVoipRecordContent(univ.Sequence):
    pass


NRST_DataVoipRecordContent.componentType = namedtype.NamedTypes(namedtype.NamedType('voip-cdr-header', NRST_DataNetworkCdrHeader()), namedtype.NamedType('voip-session-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(0, 64)))), namedtype.NamedType('voip-conference-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.NamedType('voip-duration', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 864000)))), namedtype.NamedType('voip-originator-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 512)))), namedtype.NamedType('voip-call-type-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('voip-calling-number', NRST_DataVoipNumber()), namedtype.NamedType('voip-called-number', NRST_DataVoipNumber()), namedtype.NamedType('voip-in-bytes-count', univ.Integer()), namedtype.NamedType('voip-out-bytes-count', univ.Integer()), namedtype.NamedType('voip-fax', univ.Boolean()), namedtype.NamedType('voip-term-cause', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 16384)))), namedtype.OptionalNamedType('inbound-bunch', NRST_Bunch().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.OptionalNamedType('outbound-bunch', NRST_Bunch().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.OptionalNamedType('voip-gateways', univ.SequenceOf(componentType=(NRST_IPAddress())).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))), namedtype.OptionalNamedType('voip-protocol', NRST_VoipProtocol().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))), namedtype.OptionalNamedType('supplement-service-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))), namedtype.OptionalNamedType('voip-abonent-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(0, 64))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))), namedtype.OptionalNamedType('voip-nat-info', univ.SequenceOf(componentType=(NRST_NetworkPeerInfo())).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10)))), namedtype.OptionalNamedType('voip-location', NRST_Location().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)))), namedtype.OptionalNamedType('voip-event', NRST_VoIPEvent().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12)))), namedtype.OptionalNamedType('voip-data-content-id', NRST_DataContentID().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13)))))

class NRST_DataVoipRecordData(univ.SequenceOf):
    pass


NRST_DataVoipRecordData.componentType = NRST_DataVoipRecordContent()

class NRST_DictionaryInfo(univ.Sequence):
    pass


NRST_DictionaryInfo.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('dict', useful.ObjectDescriptor()), namedtype.NamedType('count', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(1, 4294967295)))), namedtype.NamedType('change-dates', NRST_FindRange()))

class NRST_DictionariesPresenceData(univ.SequenceOf):
    pass


NRST_DictionariesPresenceData.componentType = NRST_DictionaryInfo()

class NRST_DictionaryReport(univ.Sequence):
    pass


NRST_DictionaryReport.componentType = namedtype.NamedTypes(namedtype.NamedType('id', useful.ObjectDescriptor()), namedtype.NamedType('data', univ.Any()))

class NRST_DisconnectRequest(univ.Null):
    pass


class NRST_DisconnectResponse(univ.Null):
    pass


class NRST_DocTypesRecord(univ.Sequence):
    pass


NRST_DocTypesRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('doc-type-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 65535)))), namedtype.NamedType('begin-time', NRST_DateAndTime()), namedtype.OptionalNamedType('end-time', NRST_DateAndTime()), namedtype.NamedType('description', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))))

class NRST_DocTypesRecordsData(univ.SequenceOf):
    pass


NRST_DocTypesRecordsData.componentType = NRST_DocTypesRecord()

class NRST_DropFilterRequest(NRST_FilterID):
    pass


class NRST_DropFilterResponse(univ.Sequence):
    pass


NRST_DropFilterResponse.componentType = namedtype.NamedTypes(namedtype.NamedType('filter-id', NRST_FilterID()), namedtype.NamedType('successful', univ.Boolean()), namedtype.OptionalNamedType('error-description', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))))

class NRST_EntityId(univ.Integer):
    pass


NRST_EntityId.subtypeSpec = constraint.ValueRangeConstraint(0, 4294967296)

class NRST_ExpressPaysRecord(univ.Sequence):
    pass


NRST_ExpressPaysRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('device-id', NRST_ReportedIdentifier()), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('card-number', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))))

class NRST_ExpressCardReportData(univ.SequenceOf):
    pass


NRST_ExpressCardReportData.componentType = NRST_ExpressPaysRecord()

class NRST_FilterMessageData(univ.Choice):
    pass


NRST_FilterMessageData.componentType = namedtype.NamedTypes(namedtype.NamedType('create-filter-request', NRST_CreateFilterRequest().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.NamedType('create-filter-response', NRST_CreateFilterResponse().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.NamedType('drop-filter-request', NRST_DropFilterRequest().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))), namedtype.NamedType('drop-filter-response', NRST_DropFilterResponse().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)))))

class NRST_GatesRecord(univ.Sequence):
    pass


NRST_GatesRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', NRST_TelcoID()),
    namedtype.NamedType(
        'gate-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))
        )
    ),
    namedtype.NamedType('ip-list', NRST_IPList()),
    namedtype.NamedType('begin-time', NRST_DateAndTime()),
    namedtype.OptionalNamedType('end-time', NRST_DateAndTime()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType('address', NRST_ReportedAddress()),
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

class NRST_GatesRecordsData(univ.SequenceOf):
    pass


NRST_GatesRecordsData.componentType = NRST_GatesRecord()

class NRST_GetEntities(univ.Null):
    pass


class NRST_NonFormalizedEntity(univ.Sequence):
    pass


NRST_NonFormalizedEntity.componentType = namedtype.NamedTypes(namedtype.NamedType('entity-id', NRST_EntityId()), namedtype.NamedType('entity-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))))

class NRST_GetEntitiesResponse(univ.SequenceOf):
    pass


NRST_GetEntitiesResponse.componentType = NRST_NonFormalizedEntity()

class NRST_NonFormalizedEntityAttribute(univ.Sequence):
    pass


NRST_NonFormalizedEntityAttribute.componentType = namedtype.NamedTypes(namedtype.NamedType('attribute-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))), namedtype.NamedType('attribute-type', NRST_AttributeType()))

class NRST_GetEntityAttributesResponse(univ.Sequence):
    pass


NRST_GetEntityAttributesResponse.componentType = namedtype.NamedTypes(namedtype.NamedType('entity-id', NRST_EntityId()), namedtype.NamedType('entity-attributes', univ.SequenceOf(componentType=(NRST_NonFormalizedEntityAttribute()))))

class NRST_GetEntityAtttibutes(NRST_EntityId):
    pass


class NRST_GetModuleConfigRequest(univ.Choice):
    pass


NRST_GetModuleConfigRequest.componentType = namedtype.NamedTypes(namedtype.NamedType('hw-modules-list', NRST_RequestedHardwareModules().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('sw-modules-list', NRST_RequestedSoftwareModules().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))))

class NRST_GetModuleConfigResponse(univ.Sequence):
    pass


NRST_GetModuleConfigResponse.componentType = namedtype.NamedTypes(namedtype.NamedType('hw-modules', NRST_SormHardwareModules()), namedtype.NamedType('sw-modules', NRST_SormSoftwareModules()))

class NRST_GetModuleTypesRequest(univ.Null):
    pass


class NRST_ModuleType(univ.Sequence):
    pass


NRST_ModuleType.componentType = namedtype.NamedTypes(namedtype.NamedType('module-type', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(1, 512)))), namedtype.NamedType('type-description', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128)))))

class NRST_GetModuleTypesResponse(univ.SequenceOf):
    pass


NRST_GetModuleTypesResponse.componentType = NRST_ModuleType()

class NRST_GetStructureRequest(univ.Null):
    pass


class NRST_GetStructureResponse(univ.Sequence):
    pass


NRST_GetStructureResponse.componentType = namedtype.NamedTypes(namedtype.NamedType('sw-modules', NRST_SormHardwareModules()), namedtype.NamedType('hw-modules', NRST_SormSoftwareModules()))

class NRST_IpDataPointRecord(univ.Sequence):
    pass


NRST_IpDataPointRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('point-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 1000)))), namedtype.NamedType('description', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))), namedtype.NamedType('begin-time', NRST_DateAndTime()), namedtype.OptionalNamedType('end-time', NRST_DateAndTime()))

class NRST_IpDataPointsRecordsData(univ.SequenceOf):
    pass


NRST_IpDataPointsRecordsData.componentType = NRST_IpDataPointRecord()

class NRST_IpNumberingPlanRecord(univ.Sequence):
    pass


NRST_IpNumberingPlanRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('description', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))), namedtype.NamedType('network-address', NRST_IPAddress()), namedtype.NamedType('network-mask', NRST_IPMask()), namedtype.NamedType('begin-time', NRST_DateAndTime()), namedtype.OptionalNamedType('end-time', NRST_DateAndTime()))

class NRST_IpNumberingPlanRecordsData(univ.SequenceOf):
    pass


NRST_IpNumberingPlanRecordsData.componentType = NRST_IpNumberingPlanRecord()

class NRST_LocationPresenceData(univ.SequenceOf):
    pass


NRST_LocationPresenceData.componentType = NRST_StandardInterval()

class NRST_ValidateLocationRecord(univ.Sequence):
    pass


NRST_ValidateLocationRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('connection-time', NRST_DateAndTime()), namedtype.NamedType('ident', NRST_ReportedIdentifier()), namedtype.NamedType('connection-location', NRST_Location()))

class NRST_LocationReport(univ.SequenceOf):
    pass


NRST_LocationReport.componentType = NRST_ValidateLocationRecord()

class NRST_SetModuleConfigRequest(univ.Sequence):
    pass


NRST_SetModuleConfigRequest.componentType = namedtype.NamedTypes(namedtype.NamedType('module-id', NRST_ModuleId()), namedtype.NamedType('module-config', NRST_ConfiguratedModule()))

class NRST_ManagementRequest(univ.Choice):
    pass


NRST_ManagementRequest.componentType = namedtype.NamedTypes(namedtype.NamedType('get-structure', NRST_GetStructureRequest().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('get-module-config', NRST_GetModuleConfigRequest().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.NamedType('set-module-config', NRST_SetModuleConfigRequest().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)))), namedtype.NamedType('check-module', NRST_CheckModuleRequest().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)))), namedtype.NamedType('get-module-types', NRST_GetModuleTypesRequest().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))))

class NRST_SetModuleConfigResponse(NRST_ConfiguratedModule):
    pass


class NRST_ManagementResponse(univ.Choice):
    pass


NRST_ManagementResponse.componentType = namedtype.NamedTypes(namedtype.NamedType('get-structure', NRST_GetStructureResponse().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.NamedType('get-module-config', NRST_GetModuleConfigResponse().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.NamedType('set-module-config', NRST_SetModuleConfigResponse().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)))), namedtype.NamedType('check-module', NRST_CheckModuleResponse().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)))), namedtype.NamedType('get-module-types', NRST_GetModuleTypesResponse().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))))


class NRST_ManagementMessageData(univ.Choice):
    pass


NRST_ManagementMessageData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'request',
        NRST_ManagementRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))
        )
    ),
    namedtype.NamedType(
        'response',
        NRST_ManagementResponse().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))
        )
    )
)


class NRST_MathOperation(univ.Enumerated):
    pass


NRST_MathOperation.namedValues = namedval.NamedValues(
    ('equal', 0),
    ('less', 1),
    ('greater', 2),
    ('not-equal', 3),
    ('less-or-equal', 4),
    ('greater-or-equal', 5)
)

class NRST_Version(char.PrintableString):
    pass


vers = NRST_Version('3.0.0')

class NRST_Message(univ.Sequence):
    pass


NRST_Message.componentType = namedtype.NamedTypes(namedtype.DefaultedNamedType(
    'version',
    NRST_Version().subtype(value=vers)),
    namedtype.NamedType('message-id', NRST_MessageID()),
    namedtype.NamedType('message-time', NRST_DateAndTime()),
    namedtype.OptionalNamedType(
        'operator-name',
        char.PrintableString().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType('id', useful.ObjectDescriptor()),
    namedtype.NamedType('data', univ.Any())
)

class NRST_MobileRecordContent(univ.Sequence):
    pass


NRST_MobileRecordContent.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', NRST_TelcoID()),
    namedtype.NamedType('begin-connection-time', NRST_DateAndTime()),
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
    namedtype.NamedType('in-abonent-type', NRST_PhoneAbonentType()),
    namedtype.NamedType('out-abonent-type', NRST_PhoneAbonentType()),
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
        NRST_Bunch().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'outbound-bunch',
        NRST_Bunch().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'in-info',
        NRST_ReportedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'in-end-location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'in-begin-location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'out-info',
        NRST_ReportedIdentifier().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'out-begin-location',
        NRST_Location().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6)
            )
        )
    ),
    namedtype.OptionalNamedType(
        'out-end-location',
        NRST_Location().subtype(
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
        NRST_DataContentID().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 41))
        )
    )
)


class NRST_MobileRecordData(univ.SequenceOf):
    pass


NRST_MobileRecordData.componentType = NRST_MobileRecordContent()


class NRST_MobileSubscriberIdenityPlanRecord(univ.Sequence):
    pass


NRST_MobileSubscriberIdenityPlanRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', NRST_TelcoID()),
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
    namedtype.NamedType('range-activation', NRST_DateAndTime()),
    namedtype.OptionalNamedType(
        'range-deactivation',
        NRST_DateAndTime().subtype(
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


class NRST_MobileSubscriberIdenityPlanRecordsData(univ.SequenceOf):
    pass


NRST_MobileSubscriberIdenityPlanRecordsData.componentType = NRST_MobileSubscriberIdenityPlanRecord()


class NRST_NonFormalizedEntityAttributeData(univ.Choice):
    pass


NRST_NonFormalizedEntityAttributeData.componentType = namedtype.NamedTypes(namedtype.NamedType('datetime', NRST_DateAndTime().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('integer', univ.Integer().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.NamedType('string', char.UTF8String().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))), namedtype.NamedType('boolean', univ.Boolean().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))), namedtype.NamedType('float', univ.Real().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))), namedtype.NamedType('location', NRST_Location().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)))), namedtype.NamedType('empty', univ.Null().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6)))))


class NRST_NonFormalizedEntityCondition(univ.Sequence):
    pass


NRST_NonFormalizedEntityCondition.componentType = namedtype.NamedTypes(namedtype.NamedType('attribute', NRST_NonFormalizedEntityAttribute()), namedtype.NamedType('operation', NRST_MathOperation()), namedtype.NamedType('attribute-value', NRST_NonFormalizedEntityAttributeData()))


class NRST_NonFormalizedParameter(univ.Choice):
    pass


NRST_NonFormalizedParameter.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'separator',
        NRST_LogicalOperation().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))
    ),
    namedtype.NamedType(
        'find-mask',
        NRST_NonFormalizedEntityCondition().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))
        )
    )
)


class NRST_NonFormalizedParameters(univ.SequenceOf):
    pass


NRST_NonFormalizedParameters.componentType = NRST_NonFormalizedParameter()

class NRST_NonFormalizedPresenseInfo(univ.SequenceOf):
    pass


NRST_NonFormalizedPresenseInfo.componentType = NRST_StandardInterval()

class NRST_NonFormalizedPresenseTask(NRST_EntityId):
    pass


class NRST_NonFormalizedPresenseTaskResponse(NRST_CreateTaskResponse):
    pass


class NRST_NonFormalizedRecord(univ.SequenceOf):
    pass


NRST_NonFormalizedRecord.componentType = NRST_NonFormalizedEntityAttributeData()

class NRST_NonFormalizedRecords(univ.SequenceOf):
    pass


NRST_NonFormalizedRecords.componentType = NRST_NonFormalizedRecord()

class NRST_NonFormalizedReport(univ.Choice):
    pass


NRST_NonFormalizedReport.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'nonformalized-report',
        NRST_NonFormalizedRecords().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))
    ),
    namedtype.NamedType(
        'nonformalized-presense',
        NRST_NonFormalizedPresenseInfo().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))
    )
)

class NRST_ValidateNonFormalizedTask(univ.Sequence):
    pass


NRST_ValidateNonFormalizedTask.componentType = namedtype.NamedTypes(
    namedtype.NamedType('entity-id', NRST_EntityId()),
    namedtype.NamedType('parameters', NRST_NonFormalizedParameters()),
    namedtype.OptionalNamedType('range', NRST_FindRange()),
    namedtype.OptionalNamedType(
        'report-limit', univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(1, 10000000))
        )
    )
)

class NRST_NonFormalizedTaskRequest(univ.Choice):
    pass


NRST_NonFormalizedTaskRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'get-entities',
        NRST_GetEntities().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'get-attributes',
        NRST_GetEntityAtttibutes().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'validate-task',
        NRST_ValidateNonFormalizedTask().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'validate-presense',
        NRST_NonFormalizedPresenseTask().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    )
)

class NRST_ValidateNonFormalizedTaskResponse(NRST_CreateTaskResponse):
    pass


class NRST_NonFormalizedTaskResponse(univ.Choice):
    pass


NRST_NonFormalizedTaskResponse.componentType = namedtype.NamedTypes(namedtype.NamedType('entities', NRST_GetEntitiesResponse().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('entity-attributes', NRST_GetEntityAttributesResponse().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.NamedType('validate-task', NRST_ValidateNonFormalizedTaskResponse().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)))), namedtype.NamedType('validate-presense', NRST_NonFormalizedPresenseTaskResponse().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)))))

class NRST_OID(useful.ObjectDescriptor):
    pass


class NRST_PagerRecordContent(univ.Sequence):
    pass


NRST_PagerRecordContent.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('call-type-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('connection-time', NRST_DateAndTime()), namedtype.NamedType('info', NRST_ReportedIdentifier()), namedtype.NamedType('in-bytes-count', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 1024)))), namedtype.NamedType('term-cause', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 16384)))))

class NRST_PagerRecordData(univ.SequenceOf):
    pass


NRST_PagerRecordData.componentType = NRST_PagerRecordContent()

class NRST_PayTypesRecord(univ.Sequence):
    pass


NRST_PayTypesRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('pay-type-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('begin-time', NRST_DateAndTime()), namedtype.OptionalNamedType('end-time', NRST_DateAndTime()), namedtype.NamedType('description', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))))

class NRST_PayTypesRecordsData(univ.SequenceOf):
    pass


NRST_PayTypesRecordsData.componentType = NRST_PayTypesRecord()

class NRST_PaymentsPresenseData(univ.SequenceOf):
    pass


NRST_PaymentsPresenseData.componentType = NRST_StandardInterval()

class NRST_PaymentsReport(univ.Sequence):
    pass


NRST_PaymentsReport.componentType = namedtype.NamedTypes(namedtype.NamedType('id', useful.ObjectDescriptor()), namedtype.NamedType('data', univ.Any()))

class NRST_PresenseReport(univ.Sequence):
    pass


NRST_PresenseReport.componentType = namedtype.NamedTypes(namedtype.NamedType('id', useful.ObjectDescriptor()), namedtype.NamedType('data', univ.Any()))

class NRST_PstnRecordContent(univ.Sequence):
    pass


NRST_PstnRecordContent.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('begin-connection-time', NRST_DateAndTime()), namedtype.NamedType('duration', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 86399)))), namedtype.NamedType('call-type-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('supplement-service-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('in-abonent-type', NRST_PhoneAbonentType()), namedtype.NamedType('out-abonent-type', NRST_PhoneAbonentType()), namedtype.NamedType('switch-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128)))), namedtype.NamedType('inbound-bunch', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('outbound-bunch', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('term-cause', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 16384)))), namedtype.OptionalNamedType('phone-card-number', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 20))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('in-info', NRST_ReportedIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.NamedType('dialed-digits', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))), namedtype.OptionalNamedType('out-info', NRST_ReportedIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)))), namedtype.OptionalNamedType('forwarding-identifier', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))), namedtype.OptionalNamedType('border-switch-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))), namedtype.OptionalNamedType('message', char.UTF8String().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10)))), namedtype.OptionalNamedType('ss7-opc', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11)))), namedtype.OptionalNamedType('ss7-dpc', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12)))), namedtype.OptionalNamedType('data-content-id', NRST_DataContentID().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13)))))

class NRST_PstnRecordData(univ.SequenceOf):
    pass


NRST_PstnRecordData.componentType = NRST_PstnRecordContent()

class NRST_PublicTerminalRecord(univ.Sequence):
    pass


NRST_PublicTerminalRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('device-id', NRST_ReportedIdentifier()), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('terminal-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.NamedType('terminal-number', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 20)))), namedtype.NamedType('terminal-address', NRST_ReportedAddress()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.OptionalNamedType('location', NRST_Location()))

class NRST_PublicTerminalReportData(univ.SequenceOf):
    pass


NRST_PublicTerminalReportData.componentType = NRST_PublicTerminalRecord()

class NRST_RawAcknowledgement(NRST_Acknowledgement):
    pass


class NRST_RawBytes(univ.OctetString):
    pass


NRST_RawBytes.subtypeSpec = constraint.ValueSizeConstraint(1, 4096)

class NRST_RawBytesBlock(univ.SequenceOf):
    pass


NRST_RawBytesBlock.componentType = NRST_RawBytes()

class NRST_RawDataBlock(univ.Choice):
    pass


NRST_RawDataBlock.componentType = namedtype.NamedTypes(namedtype.NamedType('reports', NRST_CallsRecords().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.NamedType('raw-cdr', NRST_RawBytesBlock().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))))

class NRST_RawRecordContent(univ.Sequence):
    pass


NRST_RawRecordContent.componentType = namedtype.NamedTypes(namedtype.NamedType('successful', univ.Boolean()), namedtype.OptionalNamedType('data', univ.OctetString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 1048576))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('error', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 4096))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.OptionalNamedType('codec-info', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 4096))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))), namedtype.OptionalNamedType('direction', NRST_DataContentRawDirection().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))), namedtype.OptionalNamedType('channel', univ.Integer().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))))

class NRST_RawReport(univ.Sequence):
    pass


NRST_RawReport.componentType = namedtype.NamedTypes(namedtype.NamedType('request-id', NRST_MessageID()), namedtype.NamedType('stream-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))), namedtype.NamedType('total-blocks-number', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 999999999999)))), namedtype.NamedType('block-number', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(1, 1000000000000)))), namedtype.NamedType('report-block', NRST_RawDataBlock()))

class NRST_RawRequestTask(univ.Choice):
    pass


NRST_RawRequestTask.componentType = namedtype.NamedTypes(namedtype.NamedType('data-types-request', NRST_DataTypesRequest().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('data-start-request', NRST_DataStartRequest().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.NamedType('data-stop-request', NRST_DataStopRequest().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))))

class NRST_RawRequest(univ.Sequence):
    pass


NRST_RawRequest.componentType = namedtype.NamedTypes(namedtype.NamedType('telcos', NRST_TelcoList()), namedtype.NamedType('raw-task', NRST_RawRequestTask()))

class NRST_RawResponse(univ.Choice):
    pass


NRST_RawResponse.componentType = namedtype.NamedTypes(namedtype.NamedType('data-types-response', NRST_DataTypesResponse().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.NamedType('data-start-response', NRST_DataStartResponse().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.NamedType('data-stop-response', NRST_DataStopResponse().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))))

class NRST_RecodedAbonentInfo(univ.Choice):
    pass


NRST_RecodedAbonentInfo.componentType = namedtype.NamedTypes(namedtype.NamedType('person', NRST_AbonentPerson().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.NamedType('organization', NRST_AbonentOrganization().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))))

class NRST_ReportedPagerIdentifier(char.NumericString):
    pass


NRST_ReportedPagerIdentifier.subtypeSpec = constraint.ValueSizeConstraint(2, 18)

class NRST_ReportedDataNetworkIdentifier(univ.Sequence):
    pass


NRST_ReportedDataNetworkIdentifier.componentType = namedtype.NamedTypes(namedtype.OptionalNamedType('user-equipment', NRST_DataNetworkEquipment().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.OptionalNamedType('login', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.OptionalNamedType('ip-address', NRST_IPAddress().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)))), namedtype.OptionalNamedType('e-mail', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))), namedtype.OptionalNamedType('pin', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 20))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))), namedtype.OptionalNamedType('phone-number', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))), namedtype.OptionalNamedType('user-domain', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 256))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6)))), namedtype.OptionalNamedType('reserved', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7)))), namedtype.OptionalNamedType('ip-mask', NRST_IPMask().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8)))))

class NRST_ReportedCdmaIdentifier(univ.Sequence):
    pass


NRST_ReportedCdmaIdentifier.componentType = namedtype.NamedTypes(namedtype.NamedType('directory-number', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 32)))), namedtype.NamedType('imsi', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 18)))), namedtype.OptionalNamedType('esn', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 18))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('min', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 18))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.OptionalNamedType('icc', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(10, 20))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))))

class NRST_ReportedGsmIdentifier(univ.Sequence):
    pass


NRST_ReportedGsmIdentifier.componentType = namedtype.NamedTypes(namedtype.NamedType('directory-number', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 32)))), namedtype.NamedType('imsi', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 18)))), namedtype.OptionalNamedType('imei', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 18))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('icc', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(10, 20))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))))

class NRST_ReportedPstnIdentifier(univ.Sequence):
    pass


NRST_ReportedPstnIdentifier.componentType = namedtype.NamedTypes(namedtype.NamedType('directory-number', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 32)))), namedtype.OptionalNamedType('internal-number', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 32)))))

class NRST_ReportedVoipIdentifier(univ.Sequence):
    pass


NRST_ReportedVoipIdentifier.componentType = namedtype.NamedTypes(namedtype.OptionalNamedType('ip-address', NRST_IPAddress().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.OptionalNamedType('originator-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 512))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.OptionalNamedType('calling-number', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))))

class NRST_RecodedReportedIdentifier(univ.Choice):
    pass


NRST_RecodedReportedIdentifier.componentType = namedtype.NamedTypes(namedtype.NamedType('pager-identifier', NRST_ReportedPagerIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.NamedType('pstn-identifier', NRST_ReportedPstnIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.NamedType('gsm-identifier', NRST_ReportedGsmIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)))), namedtype.NamedType('cdma-identifier', NRST_ReportedCdmaIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)))), namedtype.NamedType('data-network-identifier', NRST_ReportedDataNetworkIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)))), namedtype.NamedType('voip-identifier', NRST_ReportedVoipIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)))))

class NRST_RecodedAbonentService(univ.Sequence):
    pass


NRST_RecodedAbonentService.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('service-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.OptionalNamedType('idents', NRST_RecodedReportedIdentifier()), namedtype.NamedType('contract', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.NamedType('begin-time', NRST_DateAndTime()), namedtype.NamedType('end-time', NRST_DateAndTime()), namedtype.OptionalNamedType('parameter', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))))

class NRST_RecodedActiveServices(univ.SequenceOf):
    pass


NRST_RecodedActiveServices.componentType = NRST_RecodedAbonentService()

class NRST_RecodedAbonentsRecord(univ.Sequence):
    pass


NRST_RecodedAbonentsRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('idents', NRST_RecodedReportedIdentifier()), namedtype.NamedType('contract-date', NRST_DateAndTime()), namedtype.NamedType('contract', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.NamedType('actual-from', NRST_DateAndTime()), namedtype.NamedType('actual-to', NRST_DateAndTime()), namedtype.NamedType('abonent', NRST_RecodedAbonentInfo()), namedtype.NamedType('status', NRST_ActiveStatus()), namedtype.OptionalNamedType('attach', NRST_DateAndTime().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('detach', NRST_DateAndTime().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))), namedtype.OptionalNamedType('last-location', NRST_Location().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)))), namedtype.OptionalNamedType('services', NRST_RecodedActiveServices().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))), namedtype.OptionalNamedType('line-data', NRST_LineData().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)))), namedtype.OptionalNamedType('standard', NRST_Standard().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))), namedtype.OptionalNamedType('addresses', NRST_ReportedAddresses().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6)))))

class NRST_RecodedBankTransactionRecord(univ.Sequence):
    pass


NRST_RecodedBankTransactionRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('device-id', NRST_RecodedReportedIdentifier()), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('bank-account', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.NamedType('bank-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 512)))), namedtype.NamedType('bank-address', NRST_ReportedAddress()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))))

class NRST_RecodedCrossAccountRecord(univ.Sequence):
    pass


NRST_RecodedCrossAccountRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('device-id', NRST_RecodedReportedIdentifier()), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('donanted-id', NRST_RecodedReportedIdentifier()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))))

class NRST_RecodedExpressPaysRecord(univ.Sequence):
    pass


NRST_RecodedExpressPaysRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('device-id', NRST_RecodedReportedIdentifier()), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('card-number', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))))

class NRST_RecodedMobileRecordContent(univ.Sequence):
    pass


NRST_RecodedMobileRecordContent.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('begin-connection-time', NRST_DateAndTime()), namedtype.NamedType('duration', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 86399)))), namedtype.NamedType('call-type-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('supplement-service-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('in-abonent-type', NRST_PhoneAbonentType()), namedtype.NamedType('out-abonent-type', NRST_PhoneAbonentType()), namedtype.NamedType('switch-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128)))), namedtype.NamedType('term-cause', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 16384)))), namedtype.OptionalNamedType('inbound-bunch', NRST_Bunch().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.OptionalNamedType('outbound-bunch', NRST_Bunch().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.OptionalNamedType('in-info', NRST_RecodedReportedIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)))), namedtype.OptionalNamedType('in-end-location', NRST_Location().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)))), namedtype.OptionalNamedType('in-begin-location', NRST_Location().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)))), namedtype.OptionalNamedType('out-info', NRST_RecodedReportedIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)))), namedtype.OptionalNamedType('out-begin-location', NRST_Location().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6)))), namedtype.OptionalNamedType('out-end-location', NRST_Location().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7)))), namedtype.OptionalNamedType('forwarding-identifier', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 8)))), namedtype.OptionalNamedType('roaming-partner-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 9)))), namedtype.OptionalNamedType('border-switch-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10)))), namedtype.OptionalNamedType('message', char.UTF8String().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 40)))), namedtype.OptionalNamedType('data-content-id', NRST_DataContentID().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 41)))))

class NRST_RecodedPagerRecordContent(univ.Sequence):
    pass


NRST_RecodedPagerRecordContent.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('call-type-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('connection-time', NRST_DateAndTime()), namedtype.NamedType('info', NRST_RecodedReportedIdentifier()), namedtype.NamedType('in-bytes-count', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 1024)))), namedtype.NamedType('term-cause', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 16384)))))

class NRST_RecodedPstnRecordContent(univ.Sequence):
    pass


NRST_RecodedPstnRecordContent.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('begin-connection-time', NRST_DateAndTime()), namedtype.NamedType('duration', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 86399)))), namedtype.NamedType('call-type-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('supplement-service-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('in-abonent-type', NRST_PhoneAbonentType()), namedtype.NamedType('out-abonent-type', NRST_PhoneAbonentType()), namedtype.NamedType('switch-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128)))), namedtype.NamedType('inbound-bunch', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('outbound-bunch', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('term-cause', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 16384)))), namedtype.OptionalNamedType('phone-card-number', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 20))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))), namedtype.OptionalNamedType('in-info', NRST_RecodedReportedIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.NamedType('dialed-digits', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))), namedtype.OptionalNamedType('out-info', NRST_RecodedReportedIdentifier().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)))), namedtype.OptionalNamedType('forwarding-identifier', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)))), namedtype.OptionalNamedType('border-switch-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 128))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))), namedtype.OptionalNamedType('message', char.UTF8String().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10)))), namedtype.OptionalNamedType('ss7-opc', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11)))), namedtype.OptionalNamedType('ss7-dpc', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 32))).subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 12)))), namedtype.OptionalNamedType('data-content-id', NRST_DataContentID().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 13)))))

class NRST_RecodedPublicTerminalRecord(univ.Sequence):
    pass


NRST_RecodedPublicTerminalRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('device-id', NRST_RecodedReportedIdentifier()), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('terminal-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.NamedType('terminal-number', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 20)))), namedtype.NamedType('terminal-address', NRST_ReportedAddress()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.OptionalNamedType('location', NRST_Location()))

class NRST_RecodedReportAbonentData(univ.SequenceOf):
    pass


NRST_RecodedReportAbonentData.componentType = NRST_RecodedAbonentsRecord()

class NRST_RecodedReportServiceData(univ.SequenceOf):
    pass


NRST_RecodedReportServiceData.componentType = NRST_RecodedAbonentService()

class NRST_RecodedServiceCenterRecord(univ.Sequence):
    pass


NRST_RecodedServiceCenterRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('device-id', NRST_RecodedReportedIdentifier()), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('center-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.NamedType('center-address', NRST_ReportedAddress()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))))

class NRST_RecodedValidateBalanceFillupRecord(univ.Sequence):
    pass


NRST_RecodedValidateBalanceFillupRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('pay-type-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('device-id', NRST_RecodedReportedIdentifier()), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.OptionalNamedType('pay-parameters', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 512)))))

class NRST_RecodedValidateBankAccountTransferRecord(univ.Sequence):
    pass


NRST_RecodedValidateBankAccountTransferRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('donated-id', NRST_RecodedReportedIdentifier()), namedtype.NamedType('bank-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))), namedtype.NamedType('bank-account', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))))

class NRST_RecodedValidateBankCardTransferRecord(univ.Sequence):
    pass


NRST_RecodedValidateBankCardTransferRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('donanted-id', NRST_RecodedReportedIdentifier()), namedtype.NamedType('bank-card-id', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 12)))), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))))

class NRST_RecodedValidateBankDivisionTransferRecord(univ.Sequence):
    pass


NRST_RecodedValidateBankDivisionTransferRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('donanted-id', NRST_RecodedReportedIdentifier()), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('person-received', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 512)))), namedtype.NamedType('bank-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))), namedtype.NamedType('bank-division-name', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 512)))), namedtype.NamedType('bank-division-address', NRST_ReportedAddress()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))))

class NRST_RecodedValidateLocationRecord(univ.Sequence):
    pass


NRST_RecodedValidateLocationRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('connection-time', NRST_DateAndTime()), namedtype.NamedType('ident', NRST_RecodedReportedIdentifier()), namedtype.NamedType('connection-location', NRST_Location()))

class NRST_RecodedValidateTelephoneCardRecord(univ.Sequence):
    pass


NRST_RecodedValidateTelephoneCardRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('activator-device-id', NRST_RecodedReportedIdentifier()), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('card-number', char.NumericString().subtype(subtypeSpec=(constraint.ValueSizeConstraint(2, 20)))), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))))

class NRST_ReportDataBlock(univ.Choice):
    pass


NRST_ReportDataBlock.componentType = namedtype.NamedTypes(namedtype.NamedType('dictionary', NRST_DictionaryReport().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.NamedType('abonents', NRST_AbonentsReport().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))), namedtype.NamedType('connections', NRST_ConnectionsReport().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)))), namedtype.NamedType('locations', NRST_LocationReport().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))), namedtype.NamedType('payments', NRST_PaymentsReport().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4)))), namedtype.NamedType('presense', NRST_PresenseReport().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6)))), namedtype.NamedType('nonFormalized', NRST_NonFormalizedReport().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7)))), namedtype.NamedType('data-content', NRST_DataContentReport().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10)))))

class NRST_Report(univ.Sequence):
    pass


NRST_Report.componentType = namedtype.NamedTypes(namedtype.NamedType('request-id', NRST_MessageID()), namedtype.NamedType('task-id', NRST_TaskID()), namedtype.NamedType('total-blocks-number', univ.Integer()), namedtype.NamedType('block-number', univ.Integer()), namedtype.NamedType('report-block', NRST_ReportDataBlock()))

class NRST_ReportAbonentData(univ.SequenceOf):
    pass


NRST_ReportAbonentData.componentType = NRST_AbonentsRecord()

class NRST_ReportDataContentRawData(univ.SequenceOf):
    pass


NRST_ReportDataContentRawData.componentType = NRST_RawRecordContent()

class NRST_ReportMessageData(univ.Choice):
    pass


NRST_ReportMessageData.componentType = namedtype.NamedTypes(namedtype.NamedType('report', NRST_Report().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)))), namedtype.NamedType('ack', NRST_Acknowledgement().subtype(implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)))))

class NRST_ReportServiceData(univ.SequenceOf):
    pass


NRST_ReportServiceData.componentType = NRST_AbonentService()

class NRST_RoamingPartnerRecord(univ.Sequence):
    pass


NRST_RoamingPartnerRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('roaming-id', univ.Integer().subtype(subtypeSpec=(constraint.ValueRangeConstraint(0, 4294967295)))), namedtype.NamedType('begin-time', NRST_DateAndTime()), namedtype.OptionalNamedType('end-time', NRST_DateAndTime()), namedtype.NamedType('description', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 256)))))

class NRST_RoamingPartnersRecordsData(univ.SequenceOf):
    pass


NRST_RoamingPartnersRecordsData.componentType = NRST_RoamingPartnerRecord()

class NRST_ServiceCenterRecord(univ.Sequence):
    pass


NRST_ServiceCenterRecord.componentType = namedtype.NamedTypes(namedtype.NamedType('telco-id', NRST_TelcoID()), namedtype.NamedType('device-id', NRST_ReportedIdentifier()), namedtype.NamedType('date-time-fillup', NRST_DateAndTime()), namedtype.NamedType('center-id', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))), namedtype.NamedType('center-address', NRST_ReportedAddress()), namedtype.NamedType('amount', char.UTF8String().subtype(subtypeSpec=(constraint.ValueSizeConstraint(1, 64)))))


class NRST_ServiceCenterReport(univ.SequenceOf):
    pass


NRST_ServiceCenterReport.componentType = NRST_ServiceCenterRecord()


class NRST_SessionMessageData(univ.Choice):
    pass


NRST_SessionMessageData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'connect',
        NRST_ConnectRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))
        )
    ),
    namedtype.NamedType(
        'connect-response',
        NRST_ConnectResponse().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))
        )
    ),
    namedtype.NamedType(
        'adjustment',
        NRST_AdjustmentRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))
        )
    ),
    namedtype.NamedType(
        'adjustment-response',
        NRST_AdjustmentResponse().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))
        )
    ),
    namedtype.NamedType(
        'disconnect',
        NRST_DisconnectRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'disconnect-response',
        NRST_DisconnectResponse().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 5)))
    )
)


class NRST_SignalPointCodesRecord(univ.Sequence):
    pass


NRST_SignalPointCodesRecord.componentType = namedtype.NamedTypes(
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
        NRST_DateAndTime()
    ),
    namedtype.OptionalNamedType(
        'end-time',
        NRST_DateAndTime()
    ),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class NRST_SignalPointCodesRecordsData(univ.SequenceOf):
    pass


NRST_SignalPointCodesRecordsData.componentType = NRST_SignalPointCodesRecord()


class NRST_SpecialNumberRecord(univ.Sequence):
    pass


NRST_SpecialNumberRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'telco-id', NRST_TelcoID()
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
        'begin-time', NRST_DateAndTime()
    ),
    namedtype.OptionalNamedType(
        'end-time', NRST_DateAndTime()
    ),
    namedtype.OptionalNamedType(
        'network-address', NRST_IPAddress()
    )
)


class NRST_SpecialNumbersRecordsData(univ.SequenceOf):
    pass


NRST_SpecialNumbersRecordsData.componentType = NRST_SpecialNumberRecord()


class NRST_SubsPresenceData(univ.SequenceOf):
    pass


NRST_SubsPresenceData.componentType = NRST_StandardInterval()


class NRST_SupplementServicesRecord(univ.Sequence):
    pass


NRST_SupplementServicesRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', NRST_TelcoID()),
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
    namedtype.NamedType('begin-time', NRST_DateAndTime()),
    namedtype.OptionalNamedType('end-time', NRST_DateAndTime()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    )
)


class NRST_SupplementServicesRecordsData(univ.SequenceOf):
    pass


NRST_SupplementServicesRecordsData.componentType = NRST_SupplementServicesRecord()


class NRST_SwitchesRecord(univ.Sequence):
    pass


NRST_SwitchesRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', NRST_TelcoID()),
    namedtype.NamedType(
        'switch-id',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 128))
        )
    ),
    namedtype.NamedType('begin-time', NRST_DateAndTime()),
    namedtype.OptionalNamedType('end-time', NRST_DateAndTime()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType('network-type', NRST_NetworkType()),
    namedtype.NamedType('address', NRST_ReportedAddress()),
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


class NRST_SwitchesRecordsData(univ.SequenceOf):
    pass


NRST_SwitchesRecordsData.componentType = NRST_SwitchesRecord()


class NRST_TaskMessageData(univ.Choice):
    pass


NRST_TaskMessageData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'data-ready-request',
        NRST_DataReadyRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))
        )
    ),
    namedtype.NamedType(
        'data-ready-response',
        NRST_DataReadyResponse().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    ),
    namedtype.NamedType(
        'data-load-request',
        NRST_DataLoadRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))
        )
    ),
    namedtype.NamedType(
        'data-load-response',
        NRST_DataLoadResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    ),
    namedtype.NamedType(
        'data-drop-request',
        NRST_DataDropRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))
        )
    ),
    namedtype.NamedType(
        'data-drop-response',
        NRST_DataDropResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5)
            )
        )
    ),
    namedtype.NamedType(
        'data-interrupt-request',
        NRST_DataInterruptRequest().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 6))
        )
    ),
    namedtype.NamedType(
        'data-interrupt-response',
        NRST_DataInterruptResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 7)
            )
        )
    ),
    namedtype.NamedType(
        'create-task-request',
        NRST_CreateTaskRequest().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8)
            )
        )
    ),
    namedtype.NamedType(
        'create-task-response',
        NRST_CreateTaskResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9)
            )
        )
    ),
    namedtype.NamedType(
        'non-formalized-task-request',
        NRST_NonFormalizedTaskRequest().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 10)
            )
        )
    ),
    namedtype.NamedType(
        'non-formalized-task-response',
        NRST_NonFormalizedTaskResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 11)
            )
        )
    )
)


class NRST_TelcosRecord(univ.Sequence):
    pass


NRST_TelcosRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', NRST_TelcoID()),
    namedtype.NamedType('begin-time', NRST_DateAndTime()),
    namedtype.OptionalNamedType('end-time', NRST_DateAndTime()),
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


class NRST_TelcosRecordsData(univ.SequenceOf):
    pass


NRST_TelcosRecordsData.componentType = NRST_TelcosRecord()


class NRST_ValidateTelephoneCardRecord(univ.Sequence):
    pass


NRST_ValidateTelephoneCardRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', NRST_TelcoID()),
    namedtype.NamedType('activator-device-id', NRST_ReportedIdentifier()),
    namedtype.NamedType('date-time-fillup', NRST_DateAndTime()),
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


class NRST_TelephoneCardReportData(univ.SequenceOf):
    pass


NRST_TelephoneCardReportData.componentType = NRST_ValidateTelephoneCardRecord()


class NRST_TelephoneNumberingPlanRecord(univ.Sequence):
    pass


NRST_TelephoneNumberingPlanRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', NRST_TelcoID()),
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
    namedtype.NamedType('operator-type-id', NRST_NetworkType()),
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
    namedtype.NamedType('range-activation', NRST_DateAndTime()),
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
        NRST_DateAndTime().subtype(
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


class NRST_TelephoneNumberingPlanRecordsData(univ.SequenceOf):
    pass


NRST_TelephoneNumberingPlanRecordsData.componentType = NRST_TelephoneNumberingPlanRecord()


class NRST_TerminationCausesRecord(univ.Sequence):
    pass


NRST_TerminationCausesRecord.componentType = namedtype.NamedTypes(
    namedtype.NamedType('telco-id', NRST_TelcoID()),
    namedtype.NamedType(
        'termination-cause-id',
        univ.Integer().subtype(
            subtypeSpec=(constraint.ValueRangeConstraint(0, 16384))
        )
    ),
    namedtype.NamedType('begin-time', NRST_DateAndTime()),
    namedtype.OptionalNamedType('end-time', NRST_DateAndTime()),
    namedtype.NamedType(
        'description',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.NamedType('network-type', NRST_NetworkType())
)


class NRST_TerminationCausesRecordsData(univ.SequenceOf):
    pass


NRST_TerminationCausesRecordsData.componentType = NRST_TerminationCausesRecord()


class NRST_TrapType(univ.Enumerated):
    pass


NRST_TrapType.namedValues = namedval.NamedValues(
    ('heartbeat', 0),
    ('restart-software', 1),
    ('unauthorized-access', 2),
    ('critical-error', 3),
    ('major-error', 4),
    ('minor-error', 5)
)


class NRST_Trap(univ.Sequence):
    pass


NRST_Trap.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'trap-type', NRST_TrapType()
    ),
    namedtype.OptionalNamedType(
        'trap-message',
        char.UTF8String().subtype(
            subtypeSpec=(constraint.ValueSizeConstraint(1, 256))
        )
    ),
    namedtype.OptionalNamedType('reference-message', NRST_MessageID())
)


class NRST_TrapAck(univ.Null):
    pass


class NRST_TrapMessageData(univ.Choice):
    pass


NRST_TrapMessageData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'trap',
        NRST_Trap().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'trap-ack',
        NRST_TrapAck().subtype(
            implicitTag=(tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))
        )
    )
)


class NRST_UnformattedMessageData(univ.Choice):
    pass


NRST_UnformattedMessageData.componentType = namedtype.NamedTypes(
    namedtype.NamedType(
        'request',
        NRST_RawRequest().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0)
            )
        )
    ),
    namedtype.NamedType(
        'response',
        NRST_RawResponse().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1)
            )
        )
    ),
    namedtype.NamedType(
        'report',
        NRST_RawReport().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2)
            )
        )
    ),
    namedtype.NamedType(
        'report-ack',
        NRST_RawAcknowledgement().subtype(
            implicitTag=(
                tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)
            )
        )
    )
)


sorm_message_filter = NRST_OID('286')
sorm_message_management = NRST_OID('284')
sorm_message_report = NRST_OID('283')
sorm_message_session = NRST_OID('280')
sorm_message_task = NRST_OID('282')
sorm_message_trap = NRST_OID('281')
sorm_message_unformatted = NRST_OID('285')
sorm_report_abonent_abonent = NRST_OID('40')
sorm_report_abonent_organization = NRST_OID('43')
sorm_report_abonent_person = NRST_OID('42')
sorm_report_abonent_service = NRST_OID('41')
sorm_report_connection_aaa_login = NRST_OID('24')
sorm_report_connection_address_translations = NRST_OID('32')
sorm_report_connection_email = NRST_OID('26')
sorm_report_connection_file_transfer = NRST_OID('29')
sorm_report_connection_im = NRST_OID('27')
sorm_report_connection_ipdr_header = NRST_OID('23')
sorm_report_connection_mobile = NRST_OID('22')
sorm_report_connection_pager = NRST_OID('20')
sorm_report_connection_pstn = NRST_OID('21')
sorm_report_connection_raw_flows = NRST_OID('31')
sorm_report_connection_resource = NRST_OID('25')
sorm_report_connection_term_access = NRST_OID('30')
sorm_report_connection_voip = NRST_OID('28')
sorm_report_data_content_raw = NRST_OID('50')
sorm_report_dictionary_basic_stations = NRST_OID('101')
sorm_report_dictionary_bunches = NRST_OID('100')
sorm_report_dictionary_bunches_map = NRST_OID('115')
sorm_report_dictionary_call_types = NRST_OID('105')
sorm_report_dictionary_doc_types = NRST_OID('111')
sorm_report_dictionary_gates = NRST_OID('104')
sorm_report_dictionary_ip_data_points = NRST_OID('113')
sorm_report_dictionary_ip_numbering_plan = NRST_OID('109')
sorm_report_dictionary_mobile_subscriber_identity_plan = NRST_OID('116')
sorm_report_dictionary_pay_types = NRST_OID('107')
sorm_report_dictionary_phone_numbering_plan = NRST_OID('110')
sorm_report_dictionary_roaming_partners = NRST_OID('102')
sorm_report_dictionary_signal_point_codes = NRST_OID('132')
sorm_report_dictionary_special_numbers = NRST_OID('114')
sorm_report_dictionary_supplement_services = NRST_OID('106')
sorm_report_dictionary_switches = NRST_OID('103')
sorm_report_dictionary_telcos = NRST_OID('112')
sorm_report_dictionary_termination_causes = NRST_OID('108')
sorm_report_identifier_cdma = NRST_OID('4')
sorm_report_identifier_data_network = NRST_OID('5')
sorm_report_identifier_gsm = NRST_OID('3')
sorm_report_identifier_pager = NRST_OID('1')
sorm_report_identifier_pstn = NRST_OID('2')
sorm_report_identifier_voip = NRST_OID('6')
sorm_report_location_geo = NRST_OID('62')
sorm_report_location_mobile = NRST_OID('60')
sorm_report_location_wireless = NRST_OID('61')
sorm_report_payment_balance_fillups = NRST_OID('86')
sorm_report_payment_bank_account_transfer = NRST_OID('89')
sorm_report_payment_bank_card_transfer = NRST_OID('88')
sorm_report_payment_bank_division_transfer = NRST_OID('87')
sorm_report_payment_bank_transaction = NRST_OID('80')
sorm_report_payment_cross_account = NRST_OID('84')
sorm_report_payment_express_pays = NRST_OID('81')
sorm_report_payment_service_center = NRST_OID('83')
sorm_report_payment_telephone_card = NRST_OID('85')
sorm_report_payment_terminal_pays = NRST_OID('82')
sorm_report_presense_abonents = NRST_OID('120')
sorm_report_presense_connections = NRST_OID('121')
sorm_report_presense_dictionaries = NRST_OID('123')
sorm_report_presense_locations = NRST_OID('124')
sorm_report_presense_payments = NRST_OID('122')
sorm_request_abonent_organization = NRST_OID('181')
sorm_request_abonent_person = NRST_OID('180')
sorm_request_connection_aaa_login = NRST_OID('164')
sorm_request_connection_address_translations = NRST_OID('173')
sorm_request_connection_email = NRST_OID('166')
sorm_request_connection_entrance = NRST_OID('172')
sorm_request_connection_file_transfer = NRST_OID('169')
sorm_request_connection_im = NRST_OID('167')
sorm_request_connection_mobile = NRST_OID('162')
sorm_request_connection_pager = NRST_OID('160')
sorm_request_connection_pstn = NRST_OID('161')
sorm_request_connection_raw_flows = NRST_OID('171')
sorm_request_connection_resource = NRST_OID('165')
sorm_request_connection_term_access = NRST_OID('170')
sorm_request_connection_voip = NRST_OID('168')
sorm_request_dictionaries = NRST_OID('240')
sorm_request_identifier_cdma = NRST_OID('143')
sorm_request_identifier_data_network = NRST_OID('144')
sorm_request_identifier_gsm = NRST_OID('142')
sorm_request_identifier_pager = NRST_OID('140')
sorm_request_identifier_pstn = NRST_OID('141')
sorm_request_identifier_voip = NRST_OID('145')
sorm_request_location = NRST_OID('200')
sorm_request_payment_balance_fillups = NRST_OID('226')
sorm_request_payment_bank_account_transfer = NRST_OID('229')
sorm_request_payment_bank_card_transfer = NRST_OID('228')
sorm_request_payment_bank_division_transfer = NRST_OID('227')
sorm_request_payment_bank_transaction = NRST_OID('220')
sorm_request_payment_cross_account = NRST_OID('224')
sorm_request_payment_express_pays = NRST_OID('221')
sorm_request_payment_service_center = NRST_OID('223')
sorm_request_payment_telephone_card = NRST_OID('225')
sorm_request_payment_terminal_pays = NRST_OID('222')
sorm_request_presense = NRST_OID('260')
