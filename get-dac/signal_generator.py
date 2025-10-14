import numpy as np
import time

def get_sin_wave_amplitude(freq, time):
    return (np.sin(2*np.pi*freq*time) + 1)*0.5

def wait_for_sampling_peroid(sampling_frequency):
    time_sleep=float(1.0/sampling_frequency)
    time.sleep(time_sleep)

def get_triangle_amplitude(freq, time, amplitide):
    t = 1/freq
    x = time % t
    if x<=t/2:
        return 2*freq*x
    else:
        return 1 - (2*freq) * (x-t/2)

