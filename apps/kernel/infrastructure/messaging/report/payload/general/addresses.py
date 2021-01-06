from apps.system.lib import (
    basic,
    asn1,
)
from apps.kernel.infrastructure.messaging import tools


class ReportedAddress(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_ReportedAddress):
        info = payload_['address-info']
        return ReportedAddress(
            int(payload_['title']),
            str(info.getComponent()) if info.getName() == 'unstruct-info' else StructuredAddress.create(
                info.getComponent()
            )
        )

    def __init__(self, type_id_, address_):
        self.type_id = type_id_
        self.address = address_

    def __dir__(self):
        return [
            'type_id', 'address'
        ]


class StructuredAddress(basic.PrintableObject):

    @staticmethod
    def create(payload_: asn1.NRST_AddressStructInfoReport):
        return StructuredAddress(
            tools.get_optional_str(payload_['zip']),
            tools.get_optional_str(payload_['country']),
            tools.get_optional_str(payload_['region']),
            tools.get_optional_str(payload_['zone']),
            tools.get_optional_str(payload_['city']),
            tools.get_optional_str(payload_['street']),
            tools.get_optional_str(payload_['building']),
            tools.get_optional_str(payload_['build-sect']),
            tools.get_optional_str(payload_['apartment'])
        )

    def __init__(self, zip_, country_, region_, zone_, city_, street_,
                 building_, building_section_, apartment_):
        self.zip = zip_
        self.country = country_
        self.region = region_
        self.zone = zone_
        self.city = city_
        self.street = street_
        self.building = building_
        self.building_section = building_section_
        self.apartment = apartment_

    def __dir__(self):
        return [
            'zip', 'country', 'region', 'zone', 'city', 'street', 'building',
            'building_section', 'apartment'
        ]
