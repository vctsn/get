import r2r_dac as r2r
import signal_generator as sg
import time
amplitude = 3.2
signal_freq = 10
samp_freq = 1000

if __name__ == "__main__":
    try:
        dac=r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)
        while True:
            start_time=time.time()
            norm_voltage=sg.get_triangle_amplitude(signal_freq, start_time, amplitude)
            voltage = amplitude*norm_voltage
            num = dac.set_voltage(voltage)
            dac.set_number(num)
            sg.wait_for_sampling_peroid(samp_freq)
    
    finally:
        dac.deinit()