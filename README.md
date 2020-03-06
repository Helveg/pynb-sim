# pynb-sim
Widgets &amp; tools for large scale simulations inside of Python jupyter notebooks

## Usage

pynbsim can be used in any Python Jupyter notebook. Add a cell to your notebook with the
following code:

```python
import sys
%%capture --no-display
!{sys.executable} -m pip install pynb-sim
import pynbsim; pynbsim.widget()
```
