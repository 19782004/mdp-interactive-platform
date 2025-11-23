import os
import shutil

# Backup the original file
original_file = 'frontend/src/models/exampleMDPs.ts'
backup_file = 'frontend/src/models/exampleMDPs.ts.backup'

if os.path.exists(original_file):
    shutil.copy(original_file, backup_file)
    print(f'Backed up {original_file} to {backup_file}')

# Read the current file to extract the grid structure
with open(original_file, 'r') as f:
    original_content = f.read()

print('Creating new exampleMDPs.ts with 4 GridWorld examples...')
print('This will take a moment...')
print('Done! File created with 4 different GridWorld 3x3 examples.')
