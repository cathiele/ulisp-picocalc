#!/usr/bin/env python3
"""
Pre-build script for PlatformIO
Copies ulisp-picocalc.ino from root to src/ directory and replaces
"// Forward references" with the content of additional-forward-references.c
"""

Import("env")
import os

# Get the project directory
project_dir = env.get("PROJECT_DIR")
source_file = os.path.join(project_dir, "ulisp-picocalc.ino")
target_file = os.path.join(project_dir, "src", "ulisp-picocalc.ino")
forward_refs_file = os.path.join(project_dir, "additional-forward-references.c")

print("=" * 60)
print("Pre-build: Preparing source file")
print(f"Source: {source_file}")
print(f"Target: {target_file}")
print("=" * 60)

# Read the source file
with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Read the forward references content
with open(forward_refs_file, 'r', encoding='utf-8') as f:
    forward_refs_content = f.read()

# Replace the placeholder with forward references
content = content.replace("// Forward references", forward_refs_content.rstrip())

# Ensure src directory exists
os.makedirs(os.path.dirname(target_file), exist_ok=True)

# Write the modified content to the target file
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Source file prepared successfully!")
print("=" * 60)
