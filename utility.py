from dateutil import parser, tz


# Handle Time
def unix_time(time: str, utc: bool = True):
    """Accepts time as a string and returns unix time."""

    t = parser.parse(time)
    if utc:
        t = t.replace(tzinfo=tz.gettz('UTC'))  # if the time given is in utc format, set the timezone

    return '{0:08x}'.format(int(t.timestamp()))


# Little endian
def little_endian(hexa: str):
    """Returns an integer corresponding to little endian representation."""

    return int.from_bytes(bytearray.fromhex(hexa.replace('0x', '')), byteorder='little')
