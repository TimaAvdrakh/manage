from . import unformatted

from apps.system.lib import (
    exceptions,
    asn1,
)


def create_typed_message(raw_message_, payload_):
    component = payload_.getComponent()
    if isinstance(component, asn1.NRST_RawResponse):
        response = component.getComponent()
        if isinstance(response, asn1.NRST_DataTypesResponse):
            return unformatted.DataTypesResponse.create(
                raw_message_, response
            )
        if isinstance(response, asn1.NRST_DataStartResponse):
            return unformatted.DataStartResponse.create(
                raw_message_, bool(response)
            )
        if isinstance(response, asn1.NRST_DataStopResponse):
            return unformatted.DataStopResponse.create(
                raw_message_, bool(response)
            )
        raise exceptions.GeneralFault(
            f'unable to chose response by "{response.getName()}" name'
        )
    else:
        if isinstance(component, asn1.NRST_RawReport):
            return unformatted.RawReport.create(raw_message_, component)
    raise exceptions.GeneralFault(
        f'unable to chose unformatted message by "{payload_.getName()}" name'
    )
