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
