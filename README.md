# CoutureCypher
A two stage encoder made with a mix of a caesar ciphers.

To initialize call the class with and object to either decrypt or encrypt

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Couture-Cypher.

```bash
pip install Couture-Cypher
```

## Utilization

```python
from Couture-Cypher import *

# Initializes with an initial string
cipher = cypher('initial-string')

# returns decrypted variation of the initial string
cipher.decrypt()

# returns encrypted variation of the initial string
cipher.encrypt()
```


## License

[MIT](https://choosealicense.com/licenses/mit/)
