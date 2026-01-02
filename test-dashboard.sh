#!/bin/bash
# Quick Test Script for GitHub Stats Spark Dashboard
# This script sets up sample data and starts the development server

echo -e "\033[1;36mGitHub Stats Spark - Dashboard Quick Test\033[0m"
echo -e "\033[1;36m==========================================\033[0m"
echo ""

# Step 1: Create sample data directory
echo -e "\033[1;33m[1/4] Creating data directory...\033[0m"
mkdir -p docs/data

# Step 2: Create sample JSON data
echo -e "\033[1;33m[2/4] Creating sample repository data...\033[0m"
cat > docs/data/repositories.json << 'EOF'
{
  "repositories": [
    {
      "name": "github-stats-spark",
      "language": "Python",
      "created_at": "2024-01-15T10:00:00Z",
      "last_commit_date": "2024-12-20T15:30:00Z",
      "first_commit_date": "2024-01-20T08:00:00Z",
      "commit_count": 342,
      "avg_commit_size": 45.2,
      "largest_commit": {
        "sha": "abc1234",
        "date": "2024-06-15T12:00:00Z",
        "size": 1250,
        "files_changed": 15,
        "lines_added": 800,
        "lines_deleted": 435
      },
      "smallest_commit": {
        "sha": "def5678",
        "date": "2024-03-10T09:00:00Z",
        "size": 3,
        "files_changed": 1,
        "lines_added": 2,
        "lines_deleted": 0
      },
      "stars": 42,
      "forks": 8,
      "url": "https://github.com/markhazleton/github-stats-spark",
      "description": "Interactive GitHub repository analytics and visualization tool"
    },
    {
      "name": "portfolio-website",
      "language": "JavaScript",
      "created_at": "2023-06-01T10:00:00Z",
      "last_commit_date": "2024-11-20T15:30:00Z",
      "first_commit_date": "2023-06-05T08:00:00Z",
      "commit_count": 567,
      "avg_commit_size": 62.8,
      "largest_commit": {
        "sha": "ghi9012",
        "date": "2024-05-20T12:00:00Z",
        "size": 2100,
        "files_changed": 25,
        "lines_added": 1200,
        "lines_deleted": 875
      },
      "smallest_commit": {
        "sha": "jkl3456",
        "date": "2023-08-10T09:00:00Z",
        "size": 2,
        "files_changed": 1,
        "lines_added": 1,
        "lines_deleted": 0
      },
      "stars": 128,
      "forks": 23,
      "url": "https://github.com/markhazleton/portfolio-website",
      "description": "Personal portfolio and blog built with React"
    },
    {
      "name": "data-analysis-toolkit",
      "language": "Python",
      "created_at": "2022-03-12T10:00:00Z",
      "last_commit_date": "2024-10-15T15:30:00Z",
      "first_commit_date": "2022-03-20T08:00:00Z",
      "commit_count": 789,
      "avg_commit_size": 38.5,
      "largest_commit": {
        "sha": "mno7890",
        "date": "2023-12-05T12:00:00Z",
        "size": 1850,
        "files_changed": 18,
        "lines_added": 1100,
        "lines_deleted": 732
      },
      "smallest_commit": {
        "sha": "pqr1234",
        "date": "2022-05-08T09:00:00Z",
        "size": 1,
        "files_changed": 1,
        "lines_added": 1,
        "lines_deleted": 0
      },
      "stars": 256,
      "forks": 45,
      "url": "https://github.com/markhazleton/data-analysis-toolkit",
      "description": "Python toolkit for data science and machine learning workflows"
    },
    {
      "name": "typescript-starter",
      "language": "TypeScript",
      "created_at": "2024-08-01T10:00:00Z",
      "last_commit_date": "2024-12-18T15:30:00Z",
      "first_commit_date": "2024-08-05T08:00:00Z",
      "commit_count": 123,
      "avg_commit_size": 52.1,
      "largest_commit": {
        "sha": "stu5678",
        "date": "2024-10-22T12:00:00Z",
        "size": 980,
        "files_changed": 12,
        "lines_added": 650,
        "lines_deleted": 318
      },
      "smallest_commit": {
        "sha": "vwx9012",
        "date": "2024-08-15T09:00:00Z",
        "size": 4,
        "files_changed": 1,
        "lines_added": 3,
        "lines_deleted": 0
      },
      "stars": 67,
      "forks": 12,
      "url": "https://github.com/markhazleton/typescript-starter",
      "description": "Modern TypeScript project starter template with best practices"
    }
  ],
  "profile": {
    "username": "markhazleton",
    "avatar_url": "https://github.com/markhazleton.png",
    "public_repos_count": 4,
    "profile_url": "https://github.com/markhazleton",
    "total_stars": 493,
    "total_forks": 88
  },
  "metadata": {
    "generated_at": "2024-12-20T12:00:00Z",
    "schema_version": "1.0.0",
    "repository_count": 4,
    "data_source": "Sample Data"
  }
}
EOF

echo -e "   \033[1;32m✓ Sample data created at docs/data/repositories.json\033[0m"

# Step 3: Check if node_modules exists
echo -e "\033[1;33m[3/4] Checking frontend dependencies...\033[0m"
if [ ! -d "frontend/node_modules" ]; then
    echo -e "   Installing frontend dependencies (this may take a minute)..."
    cd frontend
    npm install
    cd ..
    echo -e "   \033[1;32m✓ Dependencies installed\033[0m"
else
    echo -e "   \033[1;32m✓ Dependencies already installed\033[0m"
fi

# Step 4: Start development server
echo -e "\033[1;33m[4/4] Starting development server...\033[0m"
echo ""
echo -e "\033[1;36m==========================================\033[0m"
echo -e "\033[1;32mDashboard starting at http://localhost:5173\033[0m"
echo -e "\033[1;36m==========================================\033[0m"
echo ""
echo -e "\033[1;37mWhat to test:\033[0m"
echo -e "\033[0;37m  • Table displays 4 sample repositories\033[0m"
echo -e "\033[0;37m  • Click column headers to sort\033[0m"
echo -e "\033[0;37m  • Use language filter dropdown\033[0m"
echo -e "\033[0;37m  • Hover over metrics for tooltips\033[0m"
echo -e "\033[0;37m  • Click repository names to open GitHub\033[0m"
echo ""
echo -e "\033[1;33mPress Ctrl+C to stop the server\033[0m"
echo ""

cd frontend
npm run dev
