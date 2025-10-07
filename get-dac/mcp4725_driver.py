import smbus
class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)
    
        self.address = address
        self.wm = 0x00
        self.pds = 0x00
    
        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")

        if not (0 <= number <= 4095):
            print("Число выходит за разраядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП 0.00-{dynamic_range:.2f} В")
            print("Устанавливаем 0.0 В")
            return 0
        a=int(voltage*4095/self.dynamic_range)
        self.set_number(a)
    
if __name__=="__main__":
    mcp=MCP4725(5.15, True)
    try:
        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                mcp.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
    finally:
        mcp.deinit()


