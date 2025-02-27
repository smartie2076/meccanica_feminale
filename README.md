# File structure

Presentations of the workshop at meccanica feminale

"Energy modelling and energy justice - incompatible concepts?" ([LINK](https://scientifica.de/bildungsangebote/meccanica-feminale/meccanica-feminale-2025/kursuebersicht/energy-system-modelling-and-energy-justice-incompatible-concepts/))

# Contents of this repository

Presentation slides, this Readme, input data, and figures are saved in following folders:

- [presentation](presentation)
- [README.md](README.md)
- [timeseries](timeseries)
- [figures](figures)

Two requirement files, one for jupyter notebooks (old oemof version), one for the oemof example (new oemof version): 
- [requirements_jupyter.txt](requirements_jupyter.txt) 
- [requirements_python_oemof.txt](requirements_python_oemof.txt)

A solver for oemof because installing the cbc-solver can be tricky. It is always safer, though, to download this one yourself.
- [cbc.exe](cbc.exe)

Five jupyter notebooks with increasing complexity:
- [demandlib.ipynb](demandlib.ipynb) For demandlib usage, generation of simple demand profile
- [1_dispatch.ipynb](1_dispatch.ipynb) Dispatch optimization with oemof-solph
- [2_investment_optimization.ipynb](2_investment_optimization.ipynb) Investment optimization with oemof-solph
- [3_micro_grid_basic_lp_file.ipynb](3_micro_grid_basic_lp_file.ipynb) Micro grid optimization with oemof-solph, generating LP file
  - [micro_grid_basic.lp](micro_grid_basic.lp) Linear equation system generated 
- [4_micro_grid_custom_constraint_renewable_minimum.ipynb](4_micro_grid_custom_constraint_renewable_minimum.ipynb) Micro grid optimization with oemof-solph with custom constraint
  - [micro_grid_custom_renewable_minimum.lp](micro_grid_custom_renewable_minimum.lp) Linear equation system with custom constraint

A python script that sets up a basic energy system with python (from interactive tutorial):
- [example_simple_energy_model_oemof.py](example_simple_energy_model_oemof.py)

# Jupyter notebooks

Use `pip install -r requirements_jupyter.txt`

Execute `jupyter notebook` in Terminal.
This opens a user interface to jupyter, with interactive programming environment.

# Python test code on oemof

Create second environment with `pip install -r requirements_python_oemof.txt`

Click on "play" button with correct environment activated, or run oemof example in terminal with: `python example_simple_energy_model_oemof.py`

# Further ressources

- Pycharm (community edition is free): https://www.jetbrains.com/de-de/pycharm/download/
- Cbc-solver: https://github.com/coin-or/Cbc/releases
- github Tutorial: https://docs.github.com/de/get-started/start-your-journey/hello-world

- Renewables.ninjas: https://www.renewables.ninja/
- oemof on github: https://github.com/oemof
  - Demandlib documentation: https://github.com/oemof/demandlib
  - Oemof-solph documentation: https://oemof-solph.readthedocs.io/en/latest/usage.html
  - Oemof-solph examples: https://github.com/oemof/oemof-solph/tree/dev/examples