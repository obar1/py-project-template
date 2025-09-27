# pyproject-template

[![Makefile CI](https://github.com/obar1/pyproject-template/actions/workflows/makefile.yml/badge.svg)](https://github.com/obar1/pyproject-template/actions/workflows/makefile.yml)

simple py-project template 
> class added just as placeholder for minimal test 


## init
use make with uv
ex
```bash
# Install uv first: https://docs.astral.sh/uv/getting-started/installation/
# curl -LsSf https://astral.sh/uv/install.sh | sh

make setup
source .venv/bin/activate  # uv uses .venv by default
pre-commit install # optional

# each time new code is ready for PRs :P
make refactor
```