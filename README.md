# Matched Filter CuPy
GPU-parallelised implementation of a matched filter algorithm.

This project features a parallelised version of the matched filter algorithm proposed in [this repository](https://github.com/luibo/matched-filter-py).

The parallelization is performed at GPU level by using [CuPy library](https://docs.cupy.dev/en/stable/index.html).

# Usage
The program can be simply executed with:
```
python main.py -f [path to input file]
```
from the main folder. Here some example input files are provided in the `/signal` folder.

For testing the case of unsuccesful detection, uncomment the following lines in `signal_generator.py`:
```
    # random_signal = np.random.normal(scale=1, size=len(time))
    # random_signal = random_signal + noise * scale_factor
```
and then make the function return `random_signal` instead of `noisy_signal`.

# Output
The program outputs a message of succesful or unsuccesful detection, together with the elapsed time for the GPU parallel computation.
