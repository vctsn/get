import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt

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

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title('Зависимость напряжения от времени')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.xlim(0, max(time) if time else 1)
    plt.xlim(0, max_voltage)
    plt.grid(True, alpha=0.3)
    plt.show()
        

if __name__=="__main__":
    voltage_values=[]
    time_values=[]
    duration=3.0
    adc=R2R_ADC(3.3, verbose=False)
    try:
        start_time=time.time()
        while (time.time() - start_time) < duration:
            value = adc.sequential_counting_adc()
            voltage = adc.get_sc_voltage(value)
            voltage_values.append(voltage)
            current_time=time.time() - start_time
            time_values.append(current_time)
        plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
    finally:
        adc.deinit()
        GPIO.cleanup()