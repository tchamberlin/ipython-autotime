from __future__ import print_function

from ._version import version as __version__

from time import strftime, localtime

from time import perf_counter

from IPython.core.magics.execution import _format_time as format_delta

from IPython.core.magic import Magics, magics_class, line_magic, cell_magic


def format_timestamp(struct_time):
    timestamp = strftime("%Y-%m-%d %H:%M:%S %z", struct_time)
    # add colon in %z (for datetime.fromisoformat, stackoverflow.com/q/44836581)
    return "{}:{}".format(timestamp[:-2], timestamp[-2:])


@magics_class
class LineWatcher(Magics):
    """Class that implements a basic timer.

    Notes
    -----
    * Register the `start` and `stop` methods with the IPython events API.
    """

    __slots__ = ["start_time", "timestamp"]

    @line_magic
    def threshold(self, line):
        try:
            self._threshold = float(line)
        except ValueError as error:
            raise ValueError(
                "Threshold should be set as a number of seconds (float)"
            ) from error

    def __init__(self, *args, threshold=1, **kwargs):
        self._threshold = threshold
        super().__init__(*args, **kwargs)

    def start(self):
        self.timestamp = localtime()
        self.start_time = perf_counter()

    def stop(self):
        delta = perf_counter() - self.start_time
        if delta > self._threshold:
            print(
                "time: {} (started: {})".format(
                    format_delta(delta),
                    format_timestamp(self.timestamp),
                )
            )


timer = LineWatcher()
start = timer.start
stop = timer.stop


def load_ipython_extension(ip):
    ip.register_magics(LineWatcher)
    start()
    ip.events.register("pre_run_cell", start)
    ip.events.register("post_run_cell", stop)


def unload_ipython_extension(ip):
    ip.events.unregister("pre_run_cell", start)
    ip.events.unregister("post_run_cell", stop)
