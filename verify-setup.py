#!/usr/bin/env python
"""
Setup Verification Script
Checks that all required modules and dependencies are properly configured.
"""

import sys
import os
from pathlib import Path

print("=" * 70)
print("GitHub Stats Spark - Setup Verification")
print("=" * 70)
print()

errors = []
warnings = []
success = []

# Check 1: Python version
print("[1/8] Checking Python version...")
if sys.version_info >= (3, 11):
    success.append(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
else:
    errors.append(f"✗ Python 3.11+ required (found {sys.version_info.major}.{sys.version_info.minor})")

# Check 2: Required modules
print("[2/8] Checking required Python modules...")
required_modules = [
    'yaml',
    'github',
    'svgwrite',
    'anthropic',
    'tenacity'
]

for module in required_modules:
    try:
        __import__(module)
        success.append(f"✓ Module '{module}' installed")
    except ImportError:
        errors.append(f"✗ Module '{module}' not found - run: pip install -r requirements.txt")

# Check 3: Spark modules
print("[3/8] Checking Stats Spark modules...")
spark_modules = [
    'spark.config',
    'spark.fetcher',
    'spark.calculator',
    'spark.dashboard_generator',
    'spark.models.dashboard_data',
]

sys.path.insert(0, str(Path(__file__).parent / 'src'))

for module in spark_modules:
    try:
        __import__(module)
        success.append(f"✓ Module '{module}' importable")
    except ImportError as e:
        errors.append(f"✗ Module '{module}' import failed: {e}")

# Check 4: Configuration file
print("[4/8] Checking configuration files...")
config_file = Path('config/spark.yml')
if config_file.exists():
    success.append(f"✓ Configuration file exists: {config_file}")
else:
    errors.append(f"✗ Configuration file not found: {config_file}")

# Check 5: GitHub token
print("[5/8] Checking GitHub token...")
github_token = os.getenv('GITHUB_TOKEN')
if github_token:
    success.append(f"✓ GITHUB_TOKEN environment variable set (length: {len(github_token)})")
else:
    warnings.append("⚠ GITHUB_TOKEN not set - dashboard generation will fail")
    warnings.append("  Set it: $env:GITHUB_TOKEN='your_token_here' (PowerShell)")

# Check 6: Output directories
print("[6/8] Checking output directories...")
dirs_to_check = [
    Path('docs/data'),
    Path('frontend/src'),
    Path('frontend/public'),
]

for dir_path in dirs_to_check:
    if dir_path.exists():
        success.append(f"✓ Directory exists: {dir_path}")
    else:
        warnings.append(f"⚠ Directory missing: {dir_path} (will be created on generation)")

# Check 7: Frontend dependencies
print("[7/8] Checking frontend setup...")
package_json = Path('frontend/package.json')
node_modules = Path('frontend/node_modules')

if package_json.exists():
    success.append(f"✓ package.json exists")
    if node_modules.exists():
        success.append(f"✓ node_modules installed")
    else:
        warnings.append(f"⚠ node_modules not found - run: cd frontend && npm install")
else:
    errors.append(f"✗ frontend/package.json not found")

# Check 8: CLI command
print("[8/8] Checking CLI command...")
try:
    from spark.cli import main
    success.append("✓ CLI command importable")
except ImportError as e:
    errors.append(f"✗ CLI import failed: {e}")

# Print results
print()
print("=" * 70)
print("Verification Results")
print("=" * 70)
print()

if success:
    print("✓ SUCCESS:")
    for msg in success:
        print(f"  {msg}")
    print()

if warnings:
    print("⚠ WARNINGS:")
    for msg in warnings:
        print(f"  {msg}")
    print()

if errors:
    print("✗ ERRORS:")
    for msg in errors:
        print(f"  {msg}")
    print()
    print("=" * 70)
    print("Setup has errors - please fix them before running dashboard generation")
    print("=" * 70)
    sys.exit(1)
else:
    print("=" * 70)
    print("✓ All checks passed! Ready to generate dashboard")
    print("=" * 70)
    print()
    print("Next steps:")
    print("  1. Backend: python -m spark.cli generate --user USERNAME --dashboard --verbose")
    print("  2. Frontend: cd frontend && npm run dev")
    print("  3. Open: http://localhost:5173")
    print()
    sys.exit(0)
