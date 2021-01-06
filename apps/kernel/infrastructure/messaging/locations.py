from apps.system.lib import exceptions
from . import base
from . import asn1
from . import network
from . import tools


class MobileLocation(base.ASN1Copyable):

    @staticmethod
    def create(payload_: asn1.NRST_MobileLocation):
        return MobileLocation(
            int(payload_['lac']),
            int(payload_['cell']),
            tools.get_optional_int(payload_['ta'])
        )

    def __init__(self, lac_, cell_, ta_):
        self.lac = lac_
        self.cell = cell_
        self.ta = ta_

    def __dir__(self):
        return [
         'lac', 'cell', 'ta']

    def copy_to(self, target_: asn1.NRST_MobileLocation):
        target_.setComponentByName('lac', self.lac)
        target_.setComponentByName('cell', self.cell)
        if self.ta is not None:
            target_.setComponentByName('ta', self.ta)


class WirelessLocation(base.ASN1Copyable):

    @staticmethod
    def create(payload_: asn1.NRST_WirelessLocation):
        return WirelessLocation(
            str(payload_['cell']), network.MACAddress(bytes(payload_['mac']))
        )

    def __init__(self, cell_, mac_):
        self.cell = cell_
        self.mac = mac_

    def __dir__(self):
        return [
         'cell', 'mac']

    def copy_to(self, target_: asn1.NRST_WirelessLocation):
        target_.setComponentByName('cell', self.cell)
        target_.setComponentByName('mac', bytes(self.mac))


class GeoLocation(base.ASN1Copyable):

    @staticmethod
    def create(payload_: asn1.NRST_GeoLocation):
        return GeoLocation(
            float(payload_['latitude-grade']),
            float(payload_['longitude-grade']),
            int(payload_['projection-type'])
        )

    def __init__(self, latitude_grade_, longitude_grade_, projection_type_):
        self.latitude_grade = latitude_grade_
        self.longitude_grade = longitude_grade_
        self.projection_type = projection_type_

    def __dir__(self):
        return [
         'latitude_grade', 'longitude_grade', 'projection_type']

    def copy_to(self, target_: asn1.NRST_GeoLocation):
        target_.setComponentByName('latitude-grade', self.latitude_grade)
        target_.setComponentByName('longitude-grade', self.longitude_grade)
        target_.setComponentByName('projection-type', self.projection_type)


class Location(base.ASN1ChoiceBase):

    @staticmethod
    def create(payload_: asn1.NRST_Location):
        name = payload_.getName()
        if name == 'mobile-location':
            return Location(name, MobileLocation.create(payload_.getComponent()))
        if name == 'wireless-location':
            return Location(name, WirelessLocation.create(payload_.getComponent()))
        if name == 'geo-location':
            return Location(name, GeoLocation.create(payload_.getComponent()))
        raise exceptions.GeneralFault(
            f'unable to create the "Location" class instance - unknown' +
            f' component name: "{name}"'
        )

    def __init__(self, component_name_, component_value_):
        super().__init__(
            asn1.NRST_Location(), component_name_, component_value_
        )

    def copy_to(self, target_: asn1.NRST_Location):
        target_.setComponentByName(self.component_name)
        self.component_value.copy_to(target_.getComponent())
