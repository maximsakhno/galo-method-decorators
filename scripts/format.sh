#!/bin/bash

set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place galo_method_decorators tests
black galo_method_decorators tests
isort galo_method_decorators tests
