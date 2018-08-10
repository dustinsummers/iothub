import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
from .CLI import main

main()
