# Pwned

A command line interface for checking whether your online accounts have been
compromised using [have i been pwned?](https://haveibeenpwned.com/).

# Installation

## From PyPI

Since Pwned is distributed on [PyPI](https://pypi.org/), it's super simple to
install, provided you already have a Python installation:

```bash
~> pip install pwned
```

Note that this will install Pwned *globally*, which typically means that root
access should be required. If you wish to install Pwned for just the current
user, add the `--user` flag after `install`.

## From Source

Installing Pwned from source is slightly more involved and requires that
[Poetry](https://poetry.eustace.io/) is also installed:

```bash
~> git clone https://github.com/severen/pwned.git
~> cd pwned
~> poetry install
~> poetry build
~> pip install dist/*
```

Also note that just like before, you should add the `--user` flag after
`install` if you wish to install for just the current user.

# Changelog

The changelog can be found [here](CHANGELOG.md).
