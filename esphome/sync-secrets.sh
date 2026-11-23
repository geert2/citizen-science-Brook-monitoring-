#!/usr/bin/env sh
# ESPHome reads secrets.yaml from the folder of the config being built.
# Edit esphome/secrets.yaml once, then run this to copy it next to every config.
set -e
cd "$(dirname "$0")"
[ -f secrets.yaml ] || { echo "Copy secrets.yaml.example to secrets.yaml and edit it first."; exit 1; }
cp secrets.yaml nodes/secrets.yaml
cp secrets.yaml gateway/secrets.yaml
echo "secrets.yaml copied to nodes/ and gateway/"
