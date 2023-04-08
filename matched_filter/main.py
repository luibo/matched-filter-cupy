import cupy as cp

def compute_threshold(s, h):
    print("\nComputing threshold...")

    s_energy = cp.sum(cp.square(s))
    h_energy = cp.sum(cp.square(h))

    inner_product = cp.dot(s, h)

    s_1 = s_energy - inner_product
    h_1 = inner_product - h_energy

    sum = s_1 + h_1

    return sum / 2



def matched_filter(s, h):
    diff = len(s) - len(h) # We assume that len(s) >= len(h)

    # Zero-padding of the input signal
    h = cp.pad(h, (0, diff), 'constant')

    # Compute the Fourier transform of padded_input and padded_filter
    S = cp.fft.fft(s)
    H = cp.fft.fft(h)

    # Compute the convolution of the two Fourier transforms
    Y = S * H

    # Compute the inverse Fourier transform of Y to obtain the time-domain output signal y
    y = cp.fft.ifft(Y)

    return y
