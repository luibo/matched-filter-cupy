import numpy as np
import cupy as cp
import matplotlib.pyplot as plt

def generate_signals(filePath):
    snr = 10

    with open(filePath, 'r') as file:
        contents = file.read()
    
    signal = cp.array([float(x) for x in contents.split()])

    # Close the file
    file.close()

    noise = cp.random.normal(scale=1, size=len(signal))

    # Compute the power of the signal
    signal_power = cp.sum(cp.abs(signal)**2) / len(signal)

    # Compute the power of the noise
    noise_power = cp.sum(cp.abs(noise)**2) / len(noise)

    scale_factor = cp.sqrt(signal_power / noise_power / (10**(snr/10)))

    # Add the noise to the signal
    noisy_signal = signal + noise * scale_factor

    time = [t for t in range(len(signal))]

    # random_signal = np.random.normal(scale=1, size=len(time))
    # random_signal = random_signal + noise * scale_factor

    _, (ax1, ax2) = plt.subplots(2, 1)

    ax1.plot(time, signal)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Clean Signal Amplitude')
    ax1.set_title('Clean Signal Plot')

    ax2.plot(time, noisy_signal)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Noisy Signal Amplitude')
    ax2.set_title('Noisy Signal Plot')

    plt.tight_layout()
    plt.show()

    return signal, noisy_signal
