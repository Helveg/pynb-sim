from IPython.display import display, Javascript

def simulate(command, progress_reader=None):
    import subprocess, base64
    process = subprocess.Popen(command, shell=True)
    display(Javascript("""

    """))
    if progress_reader:
        for progress_message in progress_reader.listen(process):
            from IPython.display import display, Javascript
            display(HTML("Simulated " + str(progress_message.progression) + " out of " + str(progress_message.duration) + " milliseconds"))
        # progress
