#!/bin/bash
# script to display response size for URL passes to script
curl -s -w %{size_download}"\n" "$1" -o /dev/null
