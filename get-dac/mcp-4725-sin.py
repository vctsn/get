import mcp4725_driver as mcp
import signal_generator as sg
import time
amplitude = 3.3
signal_freq = 10
samp_freq = 1000

if __name__ == "__main__":
    try:
        dac=mcp.MCP4725(5, 0x61, True)
        while True:
            start_time=time.time()
            norm_voltage=sg.get_sin_wave_amplitude(signal_freq, start_time)
            voltage = amplitude*norm_voltage
            num = dac.set_voltage(voltage)
            dac.set_number(num)
            sg.wait_for_sampling_peroid(samp_freq)
    
    finally:
        dac.deinit()