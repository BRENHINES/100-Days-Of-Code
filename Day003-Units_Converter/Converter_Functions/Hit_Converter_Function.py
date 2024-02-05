def celcius_to_far(celcius_value):
    return (celcius_value - 32) * (5 / 9)


def celcius_to_kelvin(celcius_value):
    return celcius_value + 273.15


def far_to_celcius(far_value):
    return (far_value * (9 / 5)) + 32


def kelvin_to_celcius(kelvin_value):
    return kelvin_value - 273.15
