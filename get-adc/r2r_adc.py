import time
import RPi.GPIO as GPIO
class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range=dynamic_range
        self.verbose=verbose
        self.compare_time=compare_time
        self.bits_gpio=[26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio=21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    
    def number_to_dac(self, number):
            signal=[int(element) for element in bin(number)[2:].zfill(8)]
            GPIO.output(self.bits_gpio, signal)
            return signal
    def sequential_counting_adc(self):
        for value in range(256):
            signal=self.number_to_dac(value)
            time.sleep(self.compare_time)
            comp_value = GPIO.input(self.comp_gpio)
            print("ADC value = {:^3} -> {}".format(value, signal))
            if comp_value==1:
                return value
        return 255
    def get_sc_voltage(self, value):
        voltage = value / 256*self.dynamic_range
        return voltage
        
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        

if __name__=="__main__":
    adc = R2R_ADC(3.3)
    try:
        while True:
            value = adc.sequential_counting_adc()
            voltage = adc.get_sc_voltage(value)
            print ("ADC value = {:^3}, input voltage = {:.2f}".format(value, voltage))
    finally:
        adc.deinit()
        GPIO.cleanup()

        