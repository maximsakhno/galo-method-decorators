#!/bin/bash

set -x

pytest --cov galo_method_decorators --cov-report xml tests
