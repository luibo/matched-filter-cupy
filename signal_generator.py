import cupy as cp

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

    # random_signal = cp.random.normal(scale=1, size=len(time))
    # random_signal = random_signal + noise * scale_factor

    return signal, noisy_signal
