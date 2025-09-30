#!/usr/bin/env bash
set -eo pipefail

this_dir="$( cd "$( dirname "$0" )" && pwd )"

# use .venv311 if present, else .venv, else assume current shell venv
if [ -f "${this_dir}/.venv311/bin/activate" ]; then
  source "${this_dir}/.venv311/bin/activate"
elif [ -f "${this_dir}/.venv/bin/activate" ]; then
  source "${this_dir}/.venv/bin/activate"
fi

cd "${this_dir}/src/piper/train/vits/monotonic_align"
mkdir -p monotonic_align
rm -f core.c
cythonize -i core.pyx
mv core*.so monotonic_align/
