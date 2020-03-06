# pynb-sim
Widgets &amp; tools for large scale simulations inside of Python jupyter notebooks

## Usage

pynbsim can be used in any Python Jupyter notebook. Add a cell to your notebook with the
following code:

```python
%%capture --no-display
!pip install dbbs-scaffold
import pynbsim; pynbsim.widget()
```
