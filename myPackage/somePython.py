import numpy

def fahrToKelv(temp):
    '''
    takes a temperature `temp` in fahrenheit and returns it in Kelvin
    '''

    kelvin = 5./9. * (temp - 32.) + 273.15
    answer = "{} F to K is {}"

    return  answer.format(temp,kelvin)
