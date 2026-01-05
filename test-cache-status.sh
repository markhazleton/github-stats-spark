#!/usr/bin/env bash
# Test script for cache status tracking functionality
# This script demonstrates the new cache status features

echo "==============================================="
echo "Cache Status Tracking Test Script"
echo "==============================================="
echo ""

# Ensure virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️  Virtual environment not detected. Activating..."
    source .venv/bin/activate
fi

username="markhazleton"

# Step 1: Update cache status in repositories file
echo "Step 1: Updating cache status for all repositories..."
echo "-----------------------------------------------"
spark cache --update-status --user $username
if [ $? -ne 0 ]; then
    echo "❌ Failed to update cache status"
    exit 1
fi
echo ""

# Step 2: Show cache statistics
echo "Step 2: Displaying cache statistics..."
echo "-----------------------------------------------"
spark cache --status --user $username
if [ $? -ne 0 ]; then
    echo "❌ Failed to get cache statistics"
    exit 1
fi
echo ""

# Step 3: List repositories needing refresh
echo "Step 3: Listing repositories that need refresh..."
echo "-----------------------------------------------"
spark cache --list-refresh-needed --user $username
if [ $? -ne 0 ]; then
    echo "❌ Failed to list refresh-needed repos"
    exit 1
fi
echo ""

# Step 4: Show general cache info
echo "Step 4: General cache information..."
echo "-----------------------------------------------"
spark cache --info
echo ""

# Step 5: Verify repositories cache file has cache_status
echo "Step 5: Verifying cache_status in repositories file..."
echo "-----------------------------------------------"
repos_cache_file=".cache/repositories_${username}_True_False.json"
if [ -f "$repos_cache_file" ]; then
    echo "✅ cache_status found in repository entry:"
    python3 -c "
import json
with open('$repos_cache_file', 'r') as f:
    data = json.load(f)
    first_repo = data['value'][0]
    if 'cache_status' in first_repo:
        cs = first_repo['cache_status']
        print(f\"   Repository: {first_repo['name']}\")
        print(f\"   Has cache: {cs.get('has_cache')}\")
        print(f\"   Refresh needed: {cs.get('refresh_needed')}\")
        print(f\"   Cache date: {cs.get('cache_date')}\")
        if cs.get('cache_age_hours'):
            print(f\"   Cache age: {cs['cache_age_hours']:.2f} hours\")
        if cs.get('refresh_reasons'):
            print(f\"   Refresh reasons: {', '.join(cs['refresh_reasons'])}\")
    else:
        print('❌ cache_status not found in repository entry')
"
else
    echo "❌ Repositories cache file not found: $repos_cache_file"
fi
echo ""

echo "==============================================="
echo "✅ Cache Status Test Complete!"
echo "==============================================="
echo ""
echo "Next steps:"
echo "  • Run 'spark unified --user $username' to do a full refresh"
echo "  • The system will now skip repos where refresh_needed = false"
echo "  • Check .cache/repositories_${username}_True_False.json for detailed cache status"
echo ""
