#!/bin/bash
# Test script for unified data generation
# This script tests the new unified data generator that merges all CLI commands

echo "=================================================================="
echo "Testing Unified Data Generation"
echo "=================================================================="
echo ""

# Check if virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
fi

# Check for GitHub token
if [ -z "$GITHUB_TOKEN" ]; then
    echo "ERROR: GITHUB_TOKEN environment variable not set"
    echo "Please set your GitHub Personal Access Token:"
    echo '  export GITHUB_TOKEN="your_token_here"'
    exit 1
fi

# Test 1: Display help
echo "Test 1: Display unified command help"
echo "------------------------------------------------------------------"
python -m spark.cli unified --help
echo ""

# Test 2: Generate unified data for a test user (without AI summaries for speed)
echo "Test 2: Generate unified data for markhazleton"
echo "------------------------------------------------------------------"
python -m spark.cli unified \
    --user markhazleton \
    --output-dir data \
    --verbose

echo ""

# Test 3: Check if output file was created
echo "Test 3: Verify output file"
echo "------------------------------------------------------------------"
output_file="data/repositories.json"
if [ -f "$output_file" ]; then
    echo "✅ Output file created: $output_file"
    
    # Display file size
    file_size=$(du -h "$output_file" | cut -f1)
    echo "   File size: $file_size"
    
    # Parse and display summary using Python
    echo ""
    python -c "
import json
with open('$output_file', 'r') as f:
    data = json.load(f)
print('   Data Summary:')
print(f'   - Repositories: {len(data[\"repositories\"])}')
print(f'   - Username: {data[\"profile\"][\"username\"]}')
print(f'   - Schema Version: {data[\"metadata\"][\"schema_version\"]}')
print(f'   - Generated At: {data[\"metadata\"][\"generated_at\"]}')

if len(data['repositories']) > 0:
    repo = data['repositories'][0]
    print('')
    print('   Sample Repository (first):')
    print(f'   - Name: {repo[\"name\"]}')
    print(f'   - Language: {repo[\"language\"]}')
    print(f'   - Stars: {repo[\"stars\"]}')
    if 'commit_history' in repo:
        print(f'   - Commits: {repo[\"commit_history\"][\"total_commits\"]}')
    if repo.get('rank'):
        print(f'   - Rank: {repo[\"rank\"]}')
        print(f'   - Score: {repo[\"composite_score\"]}')
    if repo.get('tech_stack'):
        print(f'   - Dependencies: {repo[\"tech_stack\"][\"total_dependencies\"]}')
        print(f'   - Currency Score: {repo[\"tech_stack\"][\"currency_score\"]}/100')
" 2>/dev/null || echo "⚠️  Could not parse JSON"
    
else
    echo "❌ Output file not found: $output_file"
fi

echo ""
echo "=================================================================="
echo "Testing Complete!"
echo "=================================================================="
echo ""
echo "Next steps:"
echo "1. Review the generated data/repositories.json file"
echo "2. Test with --include-ai-summaries flag (requires Anthropic API key)"
echo "3. Use the unified data in your frontend application"
echo ""
