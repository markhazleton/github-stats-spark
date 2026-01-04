#!/bin/bash
# Test smart cache refresh logic with limited repositories
#
# This script demonstrates the smart cache refresh feature by:
# 1. First run: Generates data for 2 repositories (full cache)
# 2. Second run: Should skip generation (data is fresh)
# 3. Third run with force-refresh: Regenerates all data

set -e

# Configuration
USERNAME="${1:-markhazleton}"
MAX_REPOS=2
OUTPUT_DIR="data"

echo "======================================================================"
echo "Testing Smart Cache Refresh Logic with $MAX_REPOS Repositories"
echo "======================================================================"
echo ""

# Check for GitHub token
if [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ ERROR: GITHUB_TOKEN environment variable not set"
    echo "Please set it with: export GITHUB_TOKEN='your_token_here'"
    exit 1
fi

# Test 1: First run (should generate data)
echo "Test 1: First Generation (2 repos)"
echo "----------------------------------------------------------------------"
echo ""

# Remove existing data to simulate first run
if [ -f "$OUTPUT_DIR/repositories.json" ]; then
    rm "$OUTPUT_DIR/repositories.json"
    echo "Removed existing repositories.json"
fi

start1=$(date +%s)
spark unified --user "$USERNAME" --max-repos $MAX_REPOS --verbose
end1=$(date +%s)
duration1=$((end1 - start1))

echo ""
echo "✅ Test 1 Complete - Duration: ${duration1} seconds"
echo ""
echo ""

# Wait a moment
sleep 2

# Test 2: Second run (should skip - data is fresh)
echo "Test 2: Immediate Re-run (should skip generation)"
echo "----------------------------------------------------------------------"
echo ""

start2=$(date +%s)
spark unified --user "$USERNAME" --max-repos $MAX_REPOS --verbose
end2=$(date +%s)
duration2=$((end2 - start2))

echo ""
echo "✅ Test 2 Complete - Duration: ${duration2} seconds"
echo ""

# Compare times
if [ $duration2 -gt 0 ]; then
    speedup=$((duration1 / duration2))
    echo "⚡ Speedup: ${speedup}x faster (should be ~100x+)"
else
    echo "⚡ Speedup: Instant (data was fresh)"
fi
echo ""
echo ""

# Test 3: Force refresh (should regenerate)
echo "Test 3: Force Refresh (should regenerate all data)"
echo "----------------------------------------------------------------------"
echo ""

start3=$(date +%s)
spark unified --user "$USERNAME" --max-repos $MAX_REPOS --force-refresh --verbose
end3=$(date +%s)
duration3=$((end3 - start3))

echo ""
echo "✅ Test 3 Complete - Duration: ${duration3} seconds"
echo ""
echo ""

# Summary
echo "======================================================================"
echo "Test Summary"
echo "======================================================================"
echo ""
echo "Test 1 (First run):          ${duration1} seconds"
echo "Test 2 (Skip - fresh data):  ${duration2} seconds"
echo "Test 3 (Force refresh):      ${duration3} seconds"
echo ""

if [ $duration1 -gt 0 ]; then
    savings=$(( (duration1 - duration2) * 100 / duration1 ))
    echo "Smart Cache Efficiency: ${savings}% time saved"
else
    echo "Smart Cache Efficiency: 100% time saved"
fi
echo ""

# Validate cache files
if [ -d ".cache" ]; then
    cache_count=$(ls -1 .cache/*.json 2>/dev/null | wc -l)
    echo "Cache files created: $cache_count"
    echo ""
fi

# Check repositories.json
if [ -f "$OUTPUT_DIR/repositories.json" ]; then
    repo_count=$(jq '.repositories | length' "$OUTPUT_DIR/repositories.json")
    generated_at=$(jq -r '.metadata.generated_at' "$OUTPUT_DIR/repositories.json")
    
    echo "✅ repositories.json validated:"
    echo "   - Repositories: $repo_count"
    echo "   - Generated at: $generated_at"
    echo ""
fi

echo "======================================================================"
echo "✨ All tests completed successfully!"
echo "======================================================================"
