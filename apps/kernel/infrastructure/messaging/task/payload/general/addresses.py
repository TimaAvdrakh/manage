from apps.system.lib import exceptions
from apps.kernel.infrastructure.messaging import base


class RequestedAddress(base.ASN1Copyable):

    def __init__(self, zip_=None, country_=None, region_=None, zone_=None,
                 city_=None, street_=None, building_=None,
                 building_section_=None, apartment_=None):
        if zip_ is None:
            if country_ is None:
                if region_ is None:
                    if zone_ is None:
                        if city_ is None:
                            if street_ is None:
                                if building_ is None:
                                    if building_section_ is None:
                                        if apartment_ is None:
                                            raise exceptions.GeneralFault(
                                                f'no one parameter is '
                                                f'defined for the "{self.__class__.__name__}" class'
                                            )
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

    def copy_to(self, target_):
        self.set_component(target_, 'zip', self.zip)
        self.set_component(target_, 'country', self.country)
        self.set_component(target_, 'region', self.region)
        self.set_component(target_, 'zone', self.zone)
        self.set_component(target_, 'city', self.city)
        self.set_component(target_, 'street', self.street)
        self.set_component(target_, 'building', self.building)
        self.set_component(target_, 'build-sect', self.building_section)
        self.set_component(target_, 'apartment', self.apartment)
