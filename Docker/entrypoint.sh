#!/bin/bash --login
# The --login ensures the bash configuration is loaded,
# enabling Conda.

# Enable strict mode.
set -euo pipefail
# ... Run whatever commands ...

# Temporarily disable strict mode and activate conda:
set +euo pipefail
conda activate nilmtk-env

# Run jupyter notebook
jupyter notebook --notebook-dir=/home/work --ip='*' \
    --NotebookApp.token='' --NotebookApp.password='' \
    --port=8881 --no-browser --allow-root &

# Re-enable strict mode:
set -euo pipefail

# exec the final command:
exec "/bin/bash"
