#!/bin/bash

# Bash "strict mode", to help catch problems and bugs in the shell
# script. Every bash script you write should include this. See
# http://redsymbol.net/articles/unofficial-bash-strict-mode/ for
# details.
set -euo pipefail

# Tell apt-get we're never going to be able to give manual
# feedback:
export DEBIAN_FRONTEND=noninteractive

# Update the package listing, so we know what package exist:
apt-get update

# Install security updates:
apt-get -y upgrade

# Install build and runtime dependencies required by the Python stack:
apt-get -y install --no-install-recommends \
  build-essential \
  ca-certificates \
  curl \
  gcc \
  libffi-dev \
  libldap2-dev \
  libpq-dev \
  libsasl2-dev \
  libssl-dev \
  libxml2-dev \
  libxslt-dev

# Delete cached files we don't need anymore:
apt-get clean
rm -rf /var/lib/apt/lists/*
