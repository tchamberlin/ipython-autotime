# ipython-autotime
Time cells in IPython that take longer than 1 second (value is configurable)

## Installation:

```console
$ pip install git+https://github.com/tchamberlin/ipython-autotime
```

To auto-start with IPython, see https://ipython.readthedocs.io/en/stable/config/intro.html#setting-configurable-options

Example:

```shell
# Create default config file
ipython profile create
# modify config file
vim ~/.ipython/profile_default/ipython_config.py
# Set: c.InteractiveShellApp.extensions = ["autotime"] 
```

## Examples

```python
In [1]: %load_ext autotime
time: 264 µs (started: 2020-12-15 11:44:36 +01:00)

In [2]: x = 1
time: 416 µs (started: 2020-12-15 11:44:45 +01:00)

In [3]: x / 0
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-3-034eb0c6102b> in <module>
----> 1 x/0

ZeroDivisionError: division by zero
time: 88.7 ms (started: 2020-12-15 11:44:53 +01:00)

In [4]: import time

In [5]: time.sleep(0.1)

In [6]: time.sleep(1.1)
time: 1.1 s (started: 2022-12-07 15:57:14 -05:00)

In [7]: %threshold 0.5

In [8]: time.sleep(1.1)
time: 1.1 s (started: 2022-12-07 15:57:31 -05:00)

In [9]: time.sleep(0.1)

```

## Want to turn it off?

```python
In [4]: %unload_ext autotime
```
