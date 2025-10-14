import RPi.GPIO as GPIO
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.pwm_frequency = pwm_frequency
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.pwm=GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)


    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП 0.00-{dynamic_range:.2f} В")
            print("Устанавливаем 0.0 В")
            num = 0
        else:
            num = int(voltage/self.dynamic_range*100)
        return num

    def set_number(self, number):
        print(f'Коэффициент заполнения: {number}')
        self.pwm.ChangeDutyCycle(number)



if __name__=="__main__":
    pwm = None
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        while True:
            try:
                voltage=float(input("Введите напряжение в Вольтах: "))
                number = dac.set_voltage(voltage)
                dac.set_number(number)

            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")

    finally:
        dac.deinit()