# main script entry point
import matched_filter.main as matf
import signal_generator as sg
import argparse, os
import cupy as cp

def isFileInput(input):
    return os.path.exists(input)


def main():

    start_event = cp.cuda.Event()
    end_event = cp.cuda.Event()

    start_event.record()

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="path to input file", required = True)
    path = (parser.parse_args().file)

    if not isFileInput(path):
        print("Input file not compliant, quitting...")
        exit()

    filter_impulse_response, input_signal = sg.generate_signals(path)

    y = matf.matched_filter(input_signal, filter_impulse_response)

    threshold = matf.compute_threshold(input_signal, filter_impulse_response)
    print(f"\nthreshold: {threshold}")

    peak = cp.amax(y)
    print(f"output peak: {peak}")

    if peak > threshold:
        print("\n*** Reference signal detected in noisy input signal ***")
    else:
        print("\n*** Signal not detected ***")
    end_event.record()
    end_event.synchronize()
    elapsed_time_ms = cp.cuda.get_elapsed_time(start_event, end_event)
    print(f"Elapsed time: {elapsed_time_ms:-3f}ms")


if __name__ == '__main__':
    main()
    