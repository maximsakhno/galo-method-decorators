#!/bin/bash

set -x
set -e

mypy galo_method_decorators tests
flake8 galo_method_decorators tests
black galo_method_decorators tests --check
isort galo_method_decorators tests --check-only
bandit galo_method_decorators -r
