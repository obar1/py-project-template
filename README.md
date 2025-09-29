# pyproject-template

[![Makefile CI](https://github.com/obar1/pyproject-template/actions/workflows/makefile.yml/badge.svg)](https://github.com/obar1/pyproject-template/actions/workflows/makefile.yml)

simple py-project template
> class added just as placeholder for minimal test


## init
use make with uv
ex
```bash
make setup
```
`pre-commit`  will run check at each commit

> some devcontainer conf for auto setup in codespace

![alt text](image.png)

## snippets

### SET GCP
to auth in gcp project
```sh
chmod +x ./set_gcp.sh

./set_gcp.sh project_123

```sh
[here](./set_gcp.sh)

[here](/.devcontainer/)

### PLAYGROUND
> do ` << 1 ` :)

```txt
    # PLAYGROUND

    > here some space to familiarize with the code

    ```bash
    pwd
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # vsode
    mkdir -p .vscode
    cat > .vscode/settings.json <<'EOF'
    {
        "python.defaultInterpreterPath": ".venv/bin/python"
    }
    EOF
    rm -rf .venv
    export VIRTUAL_ENV="$(pwd)/.venv"

    uv venv .venv
    uv init
    uv add ipykernel

    touch 01.ipynb
    echo "restart vscode, if necessary"

    ```

    ## code and nb
    [here](./01.ipynb)

    ```
```
