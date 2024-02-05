VALUE_MILLI = 1000
VALUE_CENTI = 100
VALUE_FEET_TO_METER = 0.3048
VALUE_YARD_TO_METER = 0.9144
VALUE_LEAGUE_TO_KILOMETER = 4.828


def km_to_m_or_m_to_mm(length):
    return length * VALUE_MILLI


def m_to_cm(length):
    return length * VALUE_CENTI


def ft_to_m(length):
    return length * VALUE_FEET_TO_METER


def yd_to_m(length):
    return length * VALUE_YARD_TO_METER


def league_to_km(length):
    return length * VALUE_LEAGUE_TO_KILOMETER


def m_to_km_or_mm_to_m(length):
    return length / VALUE_MILLI


def cm_to_m(length):
    return length / VALUE_CENTI


def m_to_ft(length):
    return length / VALUE_FEET_TO_METER


def m_to_yd(length):
    return length / VALUE_YARD_TO_METER


def km_to_league(length):
    return length / VALUE_LEAGUE_TO_KILOMETER
