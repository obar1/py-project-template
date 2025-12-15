# pyproject-template

[![Makefile CI](https://github.com/obar1/py-project-template/actions/workflows/makefile.yml/badge.svg)](https://github.com/obar1/py-project-template/actions/workflows/makefile.yml)

simple py-project template
> class added just as placeholder for minimal test


## init
> init env and dependencies
```sh
make setup
```
`pre-commit`  will run check at each commit

> some devcontainer conf for auto setup in codespace

![](assets/630fffff-faf2-4db0-8b3d-9b72e290dd37.png)

## check
> check the code
```sh
make check
git add -A # to add fix and loop to make check
```
![](assets/4d62318e-7046-4cae-94d3-3e17ca906593.png)

## use

- [X] add file in [here](src/readme.md) and tests [here](tests/readme.md)


- [X] if `you dare` you could this repo in a cloud shell and use it
> be careful, gcp is watching you

![](assets/f335dd0e-350a-4f0d-9774-a042eee9e59.png)

and add nb code in
[here](nb/readme.md)

exm
[01](nb/01.ipynb)
