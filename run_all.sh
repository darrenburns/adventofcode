#!/bin/bash

# Change to the aoc24 directory (assuming the script is in the parent directory)
cd "$(dirname "$0")/aoc24" || exit 1

# Find all Python files starting with "day" and sort them numerically
for file in $(ls day[0-9]*.py | sort -V); do
    echo "Running $file..."
    python3 "$file"
    echo "----------------------------------------"
done 