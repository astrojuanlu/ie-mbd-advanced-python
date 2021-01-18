#!/usr/bin/env bash
# http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

export MAMBAFORGE_URL="https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh"

# Download installer
curl -L "${MAMBAFORGE_URL}" --output "/tmp/Mambaforge-Linux-x86_64.sh"

# Run it with special options to avoid prompts
# (accept license automatically)
bash "/tmp/Mambaforge-Linux-x86_64.sh" -b -p "${HOME}/mambaforge"

# Initialize conda for bash
"${HOME}/mambaforge/bin/conda" init

# Load new configuration
source "${HOME}/mambaforge/etc/profile.d/conda.sh"

# Test that everything works
conda info

# If there is an environment file, use it
if [[ -f "environment.yml" ]]
then
  conda env create
else
  echo "No environment.yml found, will not create environment"
fi

echo '--------------------'
echo "Run the following command to start using conda: "
echo 'exec $SHELL'
echo '--------------------'
