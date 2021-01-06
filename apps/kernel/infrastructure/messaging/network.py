import ipaddress

from . import base
from apps.system.lib import asn1
from . import tools


class MACAddress(object):

    def __init__(self, address_):
        if isinstance(address_, bytes):
            hex_string = address_.hex()
            self.address = ':'.join(
                hex_string[i:i + 2] for i in range(0, len(hex_string), 2)
            )
        else:
            self.address = address_

    def __repr__(self):
        return self.address

    def __bytes__(self):
        return bytes.fromhex(self.address.replace(':', ''))


class IPAddress(base.ASN1Copyable):

    @staticmethod
    def create(address_: asn1.NRST_IPAddress):
        return IPAddress(bytes(address_.getComponent()))

    def __init__(self, address_):
        if isinstance(
                address_, ipaddress.IPv4Address
        ) or isinstance(address_, ipaddress.IPv6Address):
            self.address = address_
        else:
            self.address = ipaddress.ip_address(address_)

    def __repr__(self):
        return str(self.address)

    def copy_to(self, target_):
        if isinstance(self.address, ipaddress.IPv4Address):
            target_.setComponentByName(
                'ipv4', ipaddress.v4_int_to_packed(int(self.address))
            )
        else:
            target_.setComponentByName(
                'ipv6', ipaddress.v6_int_to_packed(int(self.address))
            )


class IPMask(base.ASN1Copyable):

    @staticmethod
    def create(mask_: asn1.NRST_IPMask):
        return IPMask(bytes(mask_.getComponent()))

    def __init__(self, mask_):
        if isinstance(
                mask_, ipaddress.IPv4Address
        ) or isinstance(mask_, ipaddress.IPv6Address):
            self.mask = mask_
        else:
            self.mask = ipaddress.ip_address(mask_)

    def __repr__(self):
        return str(self.mask)

    def copy_to(self, target_: asn1.NRST_IPMask):
        if isinstance(self.mask, ipaddress.IPv4Address):
            target_.setComponentByName(
                'ipv4-mask', ipaddress.v4_int_to_packed(int(self.mask))
            )
        else:
            target_.setComponentByName(
                'ipv6-mask', ipaddress.v6_int_to_packed(int(self.mask))
            )


class DataNetworkATM(base.ASN1Copyable):

    @staticmethod
    def create(payload_: asn1.NRST_DataNetworkATM):
        return DataNetworkATM(
            payload_['vpi'], tools.get_optional_bytes(payload_['vci'])
        )

    def __init__(self, vpi_: bytes, vci_: bytes):
        self.vpi = vpi_
        self.vci = vci_

    def __repr__(self):
        if self.vci is not None:
            return '{0}(vpi: 0x{1}, vci:0x{2})'.format(
                self.__class__.__name__, self.vpi.hex(), self.vci.hex()
            )
        else:
            return '{0}(vpi: 0x{1})'.format(
                self.__class__.__name__, self.vpi.hex()
            )

    def copy_to(self, target_):
        self.set_component(target_, 'vpi', self.vpi)
        self.set_component(target_, 'vci', self.vci)


class DataNetworkEquipment(base.ASN1ChoiceBase):

    @staticmethod
    def create(payload_: asn1.NRST_DataNetworkEquipment):
        if payload_.getName() == 'mac':
            return DataNetworkEquipment(
                'mac', MACAddress(bytes(payload_.getComponent()))
            )
        else:
            return DataNetworkEquipment(
                'atm', DataNetworkATM.create(payload_.getComponent())
            )

    def __init__(self, name_, value_):
        super().__init__(asn1.NRST_DataNetworkEquipment(), name_, value_)

    def copy_to(self, target_):
        self.set_component(
            target_,
            self.component_name,
            self.component_value if not isinstance(
                self.component_value, MACAddress
            ) else bytes(self.component_value)
        )


class Bunch(base.ASN1ChoiceBase):

    @staticmethod
    def create(payload_: asn1.NRST_Bunch):
        if payload_.getName() == 'gsm':
            return Bunch('gsm', int(payload_.getComponent()))
        else:
            return Bunch(
                'cdma-umts',
                DataNetworkEquipment.create(payload_.getComponent())
            )

    def __init__(self, name_, value_):
        super(Bunch, self).__init__(asn1.NRST_Bunch(), name_, value_)

    def copy_to(self, target_):
        self.set_component(target_, self.component_name, self.component_value)


class NetworkPeerInfo(base.ASN1Copyable):

    @staticmethod
    def create(payload_: asn1.NRST_NetworkPeerInfo):
        return NetworkPeerInfo(
            IPAddress.create(payload_['ip-address']),
            tools.get_optional_value(
                payload_['ip-port'],
                lambda octets: int(octets[0]) * 256 + int(octets[1])
            )
        )

    def __init__(self, address_, port_):
        self.address = address_
        self.port = port_

    def __dir__(self):
        return ['address', 'port']

    def copy_to(self, target_: asn1.NRST_NetworkPeerInfo):
        self.set_component(target_, 'ip-address', self.address)
        self.set_component(target_, 'ip-port', self.port)


class DataVoipNumber(base.ASN1Copyable):

    @staticmethod
    def create(payload_: asn1.NRST_DataVoipNumber):
        return DataVoipNumber(
            str(payload_['original-number']),
            tools.get_optional_str(payload_['translated-number']),
            tools.get_optional_str(payload_['e164-number'])
        )

    def __init__(self, original_number_, translated_number_, e164_number_):
        self.original_number = original_number_
        self.translated_number = translated_number_
        self.e164_number = e164_number_

    def __dir__(self):
        return [
            'original_number', 'translated_number', 'e164_number'
        ]

    def copy_to(self, target_: asn1.NRST_DataVoipNumber):
        self.set_component(target_, 'original-number', self.original_number)
        self.set_component(
            target_, 'translated-number', self.translated_number
        )
        self.set_component(target_, 'e164_number', self.e164_number)
