#!/bin/bash

################################################################################
# General setup
################################################################################

################################################################################
# Checks
################################################################################
# This script must be sourced
if [ $0 != "-bash" ]; then
    echo "ERROR :: Must source file"
    exit 1
fi

PROG_DIR="$(basename $PWD)"
if [ "$PROG_DIR" != "UnitTestsPractice" ]; then
    echo "ERROR :: Must run setup script from top level directory (UnitTestsPractice)"
    echo "INFO :: Currently running from $PROG_DIR"
    return
fi


################################################################################
# Setup python environment
################################################################################
export PYTHONPATH="${PYTHONPATH}:$PWD/python"

echo "YAY END OF SCRIPT"
