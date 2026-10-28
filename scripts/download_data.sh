#!/usr/bin/env bash
# Download the 2015 public Crunchbase export into data/raw/
set -euo pipefail
mkdir -p data/raw
for name in companies rounds investments acquisitions; do
  curl -sfL -o "data/raw/${name}.csv" \
    "https://raw.githubusercontent.com/notpeter/crunchbase-data/master/${name}.csv"
  echo "downloaded ${name}.csv"
done
