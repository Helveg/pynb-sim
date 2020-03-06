__version__ = "0.1.2"
from .ji import widget
from .progress import ProgressFileReader


def simulate(command, progress_reader=None):
    from IPython.display import clear_output
    import subprocess, base64
    process = subprocess.Popen(command)

    if progress_reader:
        for progress_message in progress_reader.listen(process):
            clear_output()
            display("Simulated", progress_message.progression, "out of", progress_message.duration, "milliseconds")
