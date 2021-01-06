import time

from apps.system.lib import asn1
from . import network


def get_optional_value(asn1_item_, transformer_=None):
    if transformer_ is None:
        if asn1_item_.hasValue():
            return asn1_item_
        return
    else:
        if asn1_item_.hasValue():
            return transformer_(asn1_item_)
        return


def get_optional_bytes(asn1_item_):
    return get_optional_value(asn1_item_, bytes)


def get_optional_int(asn1_item_):
    return get_optional_value(asn1_item_, int)


def get_optional_bool(asn1_item_):
    return get_optional_value(asn1_item_, bool)


def get_optional_str(asn1_item_):
    return get_optional_value(asn1_item_, str)


def get_optional_ip_address(asn1_item_):
    return get_optional_value(asn1_item_, network.IPAddress.create)


def copy_list_to_sequence_of(target_sequence_of_, source_list_,
                             transformer_=None):
    for item in source_list_:
        target_sequence_of_.append(
            item if transformer_ is None else transformer_(item)
        )


def sequence_of_to_list(sequence_of_, transformer_=None):
    if sequence_of_ is None:
        return
    else:
        result = []
        for item in sequence_of_:
            result.append(item if transformer_ is None else transformer_(item))

        return result


def to_date_and_time(value_):
    if isinstance(value_, asn1.NRST_DateAndTime):
        if value_.hasValue():
            return bytes(value_).decode()
    if isinstance(value_, str):
        return value_
    if isinstance(value_, time.struct_time):
        return time.strftime('%y%m%d%H%M%SZ', value_)
    else:
        if isinstance(value_, float):
            return time.strftime('%y%m%d%H%M%SZ', time.localtime(value_))
        return
