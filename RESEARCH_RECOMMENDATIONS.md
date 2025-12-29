# Research Recommendations: AI-Powered Repository Analysis

**Project**: GitHub Stats Spark - AI Repository Summary Feature
**Date**: 2025-12-28
**Context**: Feature specification for AI-powered repository summaries (spec: `specs/001-ai-repo-summary/spec.md`)

This document provides comprehensive research findings and actionable recommendations for implementing AI-powered repository analysis, technology stack version detection, and commit history analysis.

---

## Table of Contents

1. [AI-Powered Summary Generation](#1-ai-powered-summary-generation)
2. [Technology Stack Version Detection](#2-technology-stack-version-detection)
3. [Commit History Analysis](#3-commit-history-analysis)
4. [Integration Recommendations](#4-integration-recommendations)

---

## 1. AI-Powered Summary Generation

### Overview

Generating high-quality repository summaries requires combining README content, commit patterns, and metadata into coherent insights. This section examines API options, prompt strategies, and practical considerations.

### 1.1 AI API/SDK Recommendations

#### Option A: Anthropic Claude (RECOMMENDED for this project)

**Why Recommended:**
- **Context Window**: Claude 3.5 Sonnet supports 200K tokens (enough for large READMEs + commit history)
- **Cost**: $3/million input tokens, $15/million output tokens (cheaper than GPT-4)
- **Quality**: Excellent at technical content analysis and summarization
- **Rate Limits**: 50 requests/minute (tier 1), 5,000/minute (tier 4)
- **Python SDK**: Official `anthropic` library with async support

**Implementation:**
```python
import anthropic
import os
from typing import Dict, List, Optional

class ClaudeRepositorySummarizer:
    """Generate repository summaries using Claude API."""

    def __init__(self, api_key: Optional[str] = None):
        self.client = anthropic.Anthropic(
            api_key=api_key or os.environ.get("ANTHROPIC_API_KEY")
        )
        self.model = "claude-3-5-sonnet-20241022"
        self.max_tokens = 1024  # For summaries

    def summarize_repository(
        self,
        repo_name: str,
        readme_content: str,
        commit_history: List[Dict],
        metadata: Dict
    ) -> Dict[str, str]:
        """Generate comprehensive repository summary.

        Returns:
            Dict with 'short_summary', 'purpose', 'tech_stack', 'activity_status'
        """
        prompt = self._build_prompt(repo_name, readme_content, commit_history, metadata)

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                messages=[{"role": "user", "content": prompt}]
            )

            return self._parse_response(message.content[0].text)

        except anthropic.APIError as e:
            # Handle rate limits, errors
            return self._fallback_summary(repo_name, metadata)

    def _build_prompt(
        self,
        repo_name: str,
        readme: str,
        commits: List[Dict],
        metadata: Dict
    ) -> str:
        """Build optimized prompt for repository analysis."""

        # Truncate README if needed (keep first 10K chars)
        readme_excerpt = readme[:10000] if len(readme) > 10000 else readme

        # Sample commits intelligently (first 5, last 5, and random middle 10)
        commit_sample = self._sample_commits(commits, max_count=20)

        return f"""Analyze this GitHub repository and provide a concise summary.

Repository: {repo_name}
Created: {metadata.get('created_at')}
Last Updated: {metadata.get('updated_at')}
Stars: {metadata.get('stars', 0)}
Primary Language: {metadata.get('language', 'Unknown')}

README Content:
{readme_excerpt}

Recent Commit History (sampled):
{self._format_commits(commit_sample)}

Provide a structured analysis:

1. SHORT_SUMMARY (1-2 sentences): What this repository does
2. PURPOSE: Main use case and target audience
3. TECH_STACK: Key technologies, frameworks, and dependencies identified
4. ACTIVITY_STATUS: Current maintenance status based on commit patterns

Format your response as:
SHORT_SUMMARY: [summary]
PURPOSE: [purpose]
TECH_STACK: [stack]
ACTIVITY_STATUS: [status]"""

    def _sample_commits(self, commits: List[Dict], max_count: int = 20) -> List[Dict]:
        """Intelligently sample commits for context."""
        if len(commits) <= max_count:
            return commits

        # First 5, last 5, and random middle 10
        first_5 = commits[:5]
        last_5 = commits[-5:]

        middle_commits = commits[5:-5]
        import random
        middle_sample = random.sample(middle_commits, min(10, len(middle_commits)))

        return first_5 + middle_sample + last_5

    def _format_commits(self, commits: List[Dict]) -> str:
        """Format commits for prompt."""
        lines = []
        for commit in commits[:20]:  # Limit to 20 for context
            date = commit.get('date', 'unknown')[:10]  # YYYY-MM-DD
            message = commit.get('message', '')[:80]  # Truncate long messages
            lines.append(f"- {date}: {message}")
        return "\n".join(lines)

    def _parse_response(self, response_text: str) -> Dict[str, str]:
        """Parse structured response from Claude."""
        result = {
            'short_summary': '',
            'purpose': '',
            'tech_stack': '',
            'activity_status': ''
        }

        for line in response_text.split('\n'):
            if line.startswith('SHORT_SUMMARY:'):
                result['short_summary'] = line.replace('SHORT_SUMMARY:', '').strip()
            elif line.startswith('PURPOSE:'):
                result['purpose'] = line.replace('PURPOSE:', '').strip()
            elif line.startswith('TECH_STACK:'):
                result['tech_stack'] = line.replace('TECH_STACK:', '').strip()
            elif line.startswith('ACTIVITY_STATUS:'):
                result['activity_status'] = line.replace('ACTIVITY_STATUS:', '').strip()

        return result

    def _fallback_summary(self, repo_name: str, metadata: Dict) -> Dict[str, str]:
        """Generate basic summary when API fails."""
        return {
            'short_summary': f"{repo_name} - A {metadata.get('language', 'software')} project",
            'purpose': 'Description unavailable',
            'tech_stack': metadata.get('language', 'Unknown'),
            'activity_status': 'Unable to determine activity status'
        }

# Usage
summarizer = ClaudeRepositorySummarizer()
summary = summarizer.summarize_repository(
    repo_name="github-stats-spark",
    readme_content=readme_text,
    commit_history=commits,
    metadata={'created_at': '2025-01-01', 'stars': 150, 'language': 'Python'}
)
```

**Dependencies:**
```python
# requirements.txt addition
anthropic>=0.20.0  # Official Claude SDK
```

**Cost Estimation (for 50 repositories):**
- Input: ~5K tokens/repo × 50 = 250K tokens = $0.75
- Output: ~500 tokens/repo × 50 = 25K tokens = $0.38
- **Total: ~$1.13 per full report generation**

---

#### Option B: OpenAI GPT-4 (Alternative)

**Pros:**
- Very well-known, extensive documentation
- GPT-4 Turbo: 128K context window
- Structured outputs with JSON mode

**Cons:**
- More expensive ($10/million input, $30/million output)
- Lower context window than Claude
- Higher rate limit concerns for free tier

**Implementation Pattern:**
```python
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "system", "content": "You are a technical repository analyst."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=1024,
    response_format={"type": "json_object"}  # Structured output
)
```

**Dependencies:**
```python
openai>=1.0.0  # Official OpenAI SDK
```

---

#### Option C: Local Models (llama.cpp + Llama 3.1)

**Best for:**
- Privacy-sensitive scenarios
- Offline operation
- Zero API costs after initial setup

**Cons:**
- Requires GPU/significant CPU
- Quality may be lower than commercial APIs
- Longer processing time

**Implementation:**
```python
from llama_cpp import Llama

# Download model once: Llama-3.1-8B-Instruct-Q4_K_M.gguf
llm = Llama(
    model_path="models/Llama-3.1-8B-Instruct-Q4_K_M.gguf",
    n_ctx=8192,  # Context window
    n_gpu_layers=-1  # Use GPU if available
)

response = llm.create_chat_completion(
    messages=[{"role": "user", "content": prompt}],
    max_tokens=512
)
```

**Dependencies:**
```python
llama-cpp-python>=0.2.0  # With GPU support: pip install llama-cpp-python[cuda]
```

---

### 1.2 Prompt Engineering Strategies

#### Strategy 1: Structured Output Format (RECOMMENDED)

Force the model to return consistent, parseable output:

```python
PROMPT_TEMPLATE = """Analyze this GitHub repository and provide a structured summary.

Repository: {repo_name}
Stars: {stars} | Forks: {forks} | Language: {language}
Created: {created_at} | Last Update: {updated_at}

README (excerpt):
{readme_excerpt}

Recent Activity (last 10 commits):
{commit_summary}

Dependencies Detected:
{dependencies}

---

Return ONLY a JSON object with these exact fields:
{{
  "summary": "1-2 sentence description of what this repository does",
  "purpose": "Primary use case and target audience",
  "technologies": ["list", "of", "key", "technologies"],
  "maintenance_status": "active|maintained|stale|archived",
  "notable_features": ["feature1", "feature2"],
  "tech_currency": "current|slightly outdated|significantly outdated|unknown"
}}"""
```

**Why This Works:**
- Consistent parsing (JSON)
- Enforces structure
- Easy to validate and use downstream

---

#### Strategy 2: Few-Shot Examples

Include example summaries to guide the model:

```python
FEW_SHOT_EXAMPLES = """
Example 1:
Repository: react-native
Summary: Cross-platform mobile framework for building native apps using React
Purpose: Enable web developers to build iOS and Android apps with JavaScript
Technologies: JavaScript, React, Native Modules, Metro bundler
Status: active

Example 2:
Repository: fastapi
Summary: Modern, fast web framework for building APIs with Python based on type hints
Purpose: Rapid API development with automatic OpenAPI documentation
Technologies: Python, Starlette, Pydantic, async/await
Status: active
---

Now analyze this repository:
{repository_details}
"""
```

---

#### Strategy 3: Chain-of-Thought Analysis

For complex repositories, break analysis into steps:

```python
COT_PROMPT = """Analyze this repository step-by-step:

Step 1: What problem does this solve? (based on README)
Step 2: Who is the target user? (developers, end-users, enterprises?)
Step 3: What are the core technologies? (languages, frameworks, databases)
Step 4: How active is development? (commit frequency, last update)
Step 5: How mature is the project? (stars, forks, age, breaking changes)

Repository Data:
{repo_data}

Provide your step-by-step analysis, then conclude with a final summary."""
```

---

### 1.3 Context Window Management

#### Challenge: Large READMEs and Commit Histories

**Solution: Intelligent Truncation and Summarization**

```python
def prepare_context(
    readme: str,
    commits: List[Dict],
    max_readme_chars: int = 10000,
    max_commits: int = 20
) -> Dict[str, str]:
    """Prepare repository context for LLM with size limits."""

    # 1. README Truncation Strategy
    if len(readme) > max_readme_chars:
        # Keep first 8K chars (intro, usage) + last 2K (recent updates)
        readme_context = readme[:8000] + "\n...[truncated]...\n" + readme[-2000:]
    else:
        readme_context = readme

    # 2. Commit Sampling Strategy
    if len(commits) > max_commits:
        # Take first 5, last 10, and 5 random middle commits
        commit_sample = (
            commits[:5] +
            commits[len(commits)//2-2:len(commits)//2+3] +
            commits[-10:]
        )
    else:
        commit_sample = commits

    # 3. Commit Summarization (group by time periods)
    commit_summary = summarize_commit_patterns(commit_sample)

    return {
        'readme': readme_context,
        'commits': commit_summary
    }

def summarize_commit_patterns(commits: List[Dict]) -> str:
    """Convert commit list to high-level pattern description."""

    if not commits:
        return "No commit history available"

    # Group commits by time period
    recent = [c for c in commits if is_within_days(c['date'], 30)]
    older = [c for c in commits if not is_within_days(c['date'], 30)]

    summary_lines = []

    if recent:
        summary_lines.append(f"Recent activity (30 days): {len(recent)} commits")
        recent_messages = [c['message'][:50] for c in recent[:3]]
        summary_lines.append(f"  Recent work: {', '.join(recent_messages)}")

    if older:
        summary_lines.append(f"Historical commits: {len(older)}")

    return "\n".join(summary_lines)
```

---

### 1.4 Rate Limits and Cost Management

#### Rate Limit Handling

```python
import time
from typing import Optional
import anthropic

class RateLimitedSummarizer:
    """Repository summarizer with rate limit handling."""

    def __init__(self, api_key: str, requests_per_minute: int = 50):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.rpm = requests_per_minute
        self.last_request_time = 0
        self.request_interval = 60.0 / requests_per_minute

    def summarize_with_backoff(
        self,
        repo_data: Dict,
        max_retries: int = 3
    ) -> Optional[Dict]:
        """Make API call with rate limiting and exponential backoff."""

        for attempt in range(max_retries):
            # Rate limiting
            self._wait_for_rate_limit()

            try:
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1024,
                    messages=[{"role": "user", "content": self._build_prompt(repo_data)}]
                )

                return self._parse_response(response.content[0].text)

            except anthropic.RateLimitError as e:
                wait_time = (2 ** attempt) * 5  # Exponential backoff: 5s, 10s, 20s
                print(f"Rate limit hit, waiting {wait_time}s...")
                time.sleep(wait_time)

            except anthropic.APIError as e:
                print(f"API error: {e}")
                return None

        return None  # Failed after retries

    def _wait_for_rate_limit(self):
        """Ensure we don't exceed requests per minute."""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time

        if time_since_last < self.request_interval:
            time.sleep(self.request_interval - time_since_last)

        self.last_request_time = time.time()
```

#### Cost Optimization Strategies

```python
# Strategy 1: Batch processing with caching
class CachedSummarizer:
    """Cache AI-generated summaries to avoid duplicate API calls."""

    def __init__(self, cache_dir: str = ".ai_cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)

    def get_summary(self, repo_name: str, repo_hash: str) -> Optional[Dict]:
        """Check cache before making API call."""
        cache_file = self.cache_dir / f"{repo_name}_{repo_hash}.json"

        if cache_file.exists():
            # Check if cache is still valid (e.g., < 7 days old)
            if time.time() - cache_file.stat().st_mtime < 7 * 24 * 3600:
                with open(cache_file) as f:
                    return json.load(f)

        return None

    def save_summary(self, repo_name: str, repo_hash: str, summary: Dict):
        """Save summary to cache."""
        cache_file = self.cache_dir / f"{repo_name}_{repo_hash}.json"
        with open(cache_file, 'w') as f:
            json.dump(summary, f)

# Strategy 2: Use cheaper models for simple repos
def select_model(repo_metadata: Dict) -> str:
    """Choose model based on repository complexity."""

    # Simple repos (< 1K stars, < 100 commits) -> use cheaper model
    if repo_metadata['stars'] < 1000 and repo_metadata['commit_count'] < 100:
        return "claude-3-haiku-20240307"  # $0.25/$1.25 per million tokens

    # Complex repos -> use smarter model
    return "claude-3-5-sonnet-20241022"
```

---

### 1.5 Fallback Strategies When AI is Unavailable

#### Graceful Degradation

```python
class HybridSummarizer:
    """Repository summarizer with AI and rule-based fallbacks."""

    def __init__(self, ai_summarizer: Optional[ClaudeRepositorySummarizer] = None):
        self.ai = ai_summarizer

    def generate_summary(
        self,
        repo_name: str,
        readme: str,
        metadata: Dict,
        commits: List[Dict]
    ) -> Dict[str, str]:
        """Generate summary with fallback to rule-based approach."""

        # Try AI first
        if self.ai:
            try:
                return self.ai.summarize_repository(repo_name, readme, commits, metadata)
            except Exception as e:
                print(f"AI summarization failed: {e}, falling back to rules")

        # Fallback: Rule-based summary
        return self._rule_based_summary(repo_name, readme, metadata, commits)

    def _rule_based_summary(
        self,
        repo_name: str,
        readme: str,
        metadata: Dict,
        commits: List[Dict]
    ) -> Dict[str, str]:
        """Generate summary using heuristics and patterns."""

        # Extract first paragraph from README as summary
        first_paragraph = self._extract_first_paragraph(readme)

        # Identify technologies from file extensions and keywords
        tech_stack = self._detect_technologies(metadata, readme)

        # Determine activity status from commits
        activity_status = self._determine_activity_status(commits, metadata)

        return {
            'short_summary': first_paragraph or f"{repo_name} - A {metadata.get('language')} project",
            'purpose': 'See README for details',
            'tech_stack': ', '.join(tech_stack),
            'activity_status': activity_status
        }

    def _extract_first_paragraph(self, readme: str) -> str:
        """Extract first meaningful paragraph from README."""
        lines = readme.strip().split('\n')

        # Skip title, badges, empty lines
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('[!['):
                # Found first paragraph
                return line[:200]  # Truncate to 200 chars

        return ""

    def _detect_technologies(self, metadata: Dict, readme: str) -> List[str]:
        """Detect technologies from metadata and README."""
        technologies = set()

        # Add primary language
        if metadata.get('language'):
            technologies.add(metadata['language'])

        # Scan README for common tech keywords
        tech_keywords = {
            'react', 'vue', 'angular', 'django', 'flask', 'fastapi',
            'tensorflow', 'pytorch', 'kubernetes', 'docker', 'postgres',
            'mongodb', 'redis', 'typescript', 'graphql', 'rest api'
        }

        readme_lower = readme.lower()
        for keyword in tech_keywords:
            if keyword in readme_lower:
                technologies.add(keyword.title())

        return sorted(list(technologies))[:5]  # Top 5

    def _determine_activity_status(
        self,
        commits: List[Dict],
        metadata: Dict
    ) -> str:
        """Determine repository activity status."""

        if not commits:
            return "inactive"

        # Check last commit date
        from datetime import datetime, timedelta

        last_commit_date = datetime.fromisoformat(
            commits[-1]['date'].replace('Z', '+00:00')
        )
        days_since = (datetime.now(last_commit_date.tzinfo) - last_commit_date).days

        if days_since < 30:
            return "actively maintained"
        elif days_since < 180:
            return "maintained"
        elif days_since < 365:
            return "sporadically maintained"
        else:
            return "stale"
```

---

### 1.6 Recommended Implementation for This Project

**Tiered Approach:**

1. **Primary**: Claude 3.5 Sonnet for high-quality summaries
2. **Fallback 1**: Claude 3 Haiku for cost savings on simple repos
3. **Fallback 2**: Rule-based extraction if API fails or quota exceeded

**Integration Points:**

```python
# In src/spark/ai_summarizer.py (new file)
from spark.cache import APICache
from spark.logger import get_logger

class RepositorySummarizer:
    """AI-powered repository summary generator with fallbacks."""

    def __init__(
        self,
        anthropic_api_key: Optional[str] = None,
        cache: Optional[AICache] = None
    ):
        self.logger = get_logger()
        self.cache = cache or AICache(cache_dir=".ai_cache", ttl_hours=168)  # 7 days

        # Initialize AI client if available
        try:
            self.ai_client = ClaudeRepositorySummarizer(api_key=anthropic_api_key)
            self.logger.info("AI summarization enabled (Claude)")
        except Exception as e:
            self.logger.warn(f"AI client unavailable: {e}, using rule-based fallback")
            self.ai_client = None

    def summarize_repositories(
        self,
        repositories: List[Dict],
        readme_contents: Dict[str, str],
        commit_histories: Dict[str, List[Dict]]
    ) -> Dict[str, Dict[str, str]]:
        """Generate summaries for multiple repositories.

        Returns:
            Dict mapping repo name to summary dict
        """
        summaries = {}

        for repo in repositories:
            repo_name = repo['name']
            self.logger.info(f"Generating summary for {repo_name}")

            # Check cache first
            cache_key = f"summary_{repo_name}_{repo['updated_at']}"
            cached = self.cache.get(cache_key)

            if cached:
                summaries[repo_name] = cached
                continue

            # Generate summary
            summary = self._generate_single_summary(
                repo_name=repo_name,
                readme=readme_contents.get(repo_name, ''),
                metadata=repo,
                commits=commit_histories.get(repo_name, [])
            )

            # Cache result
            self.cache.set(cache_key, summary)
            summaries[repo_name] = summary

        return summaries

    def _generate_single_summary(
        self,
        repo_name: str,
        readme: str,
        metadata: Dict,
        commits: List[Dict]
    ) -> Dict[str, str]:
        """Generate summary with AI or fallback to rules."""

        if self.ai_client:
            try:
                return self.ai_client.summarize_repository(
                    repo_name, readme, commits, metadata
                )
            except Exception as e:
                self.logger.warn(f"AI summary failed for {repo_name}: {e}")

        # Fallback to rule-based
        return self._rule_based_summary(repo_name, readme, metadata, commits)
```

---

## 2. Technology Stack Version Detection

### Overview

Identifying outdated dependencies is critical for understanding repository maintenance status. This section covers parsing strategies, version APIs, and comparison algorithms.

### 2.1 Dependency File Parsing

#### Multi-Ecosystem Support

```python
from typing import Dict, List, Optional
from pathlib import Path
import re
import json
import tomli  # For TOML parsing (pyproject.toml)

class DependencyParser:
    """Parse dependency files across multiple ecosystems."""

    SUPPORTED_FILES = {
        'package.json': 'parse_npm',
        'requirements.txt': 'parse_python_requirements',
        'pyproject.toml': 'parse_pyproject',
        'Pipfile': 'parse_pipfile',
        'Gemfile': 'parse_ruby',
        'go.mod': 'parse_go',
        'pom.xml': 'parse_maven',
        'build.gradle': 'parse_gradle',
        'Cargo.toml': 'parse_rust',
        'composer.json': 'parse_php',
    }

    def detect_dependencies(
        self,
        repo_path: str,
        repo_contents: Dict[str, str]  # filename -> content
    ) -> Dict[str, List[Dict]]:
        """Detect and parse all dependency files.

        Returns:
            Dict mapping ecosystem to list of dependencies
            Example: {'npm': [{'name': 'react', 'version': '^18.0.0'}], ...}
        """
        dependencies = {}

        for filename, content in repo_contents.items():
            parser_method = self.SUPPORTED_FILES.get(filename)
            if parser_method:
                ecosystem_deps = getattr(self, parser_method)(content)
                ecosystem = self._get_ecosystem(filename)
                dependencies[ecosystem] = ecosystem_deps

        return dependencies

    def parse_npm(self, content: str) -> List[Dict]:
        """Parse package.json dependencies."""
        try:
            data = json.loads(content)
            deps = []

            # Combine dependencies and devDependencies
            for dep_type in ['dependencies', 'devDependencies']:
                for name, version in data.get(dep_type, {}).items():
                    deps.append({
                        'name': name,
                        'version': self._clean_version(version),
                        'type': dep_type
                    })

            return deps
        except json.JSONDecodeError:
            return []

    def parse_python_requirements(self, content: str) -> List[Dict]:
        """Parse requirements.txt format."""
        deps = []

        for line in content.split('\n'):
            line = line.strip()

            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue

            # Skip -e editable installs
            if line.startswith('-e '):
                continue

            # Parse package==version or package>=version
            match = re.match(r'^([a-zA-Z0-9-_\.]+)\s*([><=!]+)\s*([0-9\.]+.*?)$', line)
            if match:
                deps.append({
                    'name': match.group(1),
                    'version': match.group(3),
                    'operator': match.group(2)
                })
            else:
                # Package without version
                if re.match(r'^[a-zA-Z0-9-_\.]+$', line):
                    deps.append({'name': line, 'version': None})

        return deps

    def parse_pyproject(self, content: str) -> List[Dict]:
        """Parse pyproject.toml (Poetry, etc.)."""
        try:
            data = tomli.loads(content)
            deps = []

            # Poetry format
            if 'tool' in data and 'poetry' in data['tool']:
                poetry_deps = data['tool']['poetry'].get('dependencies', {})
                for name, version in poetry_deps.items():
                    if name == 'python':
                        continue  # Skip python version

                    # Handle dict format: {version = "^1.0", optional = true}
                    if isinstance(version, dict):
                        version = version.get('version', '')

                    deps.append({'name': name, 'version': self._clean_version(version)})

            # PEP 621 format
            elif 'project' in data:
                for dep_str in data['project'].get('dependencies', []):
                    match = re.match(r'^([a-zA-Z0-9-_\.]+)\s*([><=!]+)\s*([0-9\.]+.*?)$', dep_str)
                    if match:
                        deps.append({
                            'name': match.group(1),
                            'version': match.group(3)
                        })

            return deps
        except Exception:
            return []

    def parse_ruby(self, content: str) -> List[Dict]:
        """Parse Gemfile."""
        deps = []

        for line in content.split('\n'):
            # Match: gem 'rails', '~> 6.1.0'
            match = re.match(r"gem\s+['\"]([^'\"]+)['\"]\s*,\s*['\"]([^'\"]+)['\"]", line)
            if match:
                deps.append({
                    'name': match.group(1),
                    'version': self._clean_version(match.group(2))
                })

        return deps

    def parse_go(self, content: str) -> List[Dict]:
        """Parse go.mod."""
        deps = []

        in_require_block = False
        for line in content.split('\n'):
            line = line.strip()

            if line == 'require (':
                in_require_block = True
                continue
            elif line == ')':
                in_require_block = False
                continue

            if in_require_block or line.startswith('require '):
                # Match: github.com/pkg/errors v0.9.1
                match = re.match(r'([^\s]+)\s+v([0-9\.]+)', line)
                if match:
                    deps.append({
                        'name': match.group(1),
                        'version': match.group(2)
                    })

        return deps

    def _clean_version(self, version: str) -> str:
        """Remove semver operators (^, ~, >=, etc.)."""
        return re.sub(r'^[\^~>=<]+', '', version.strip())

    def _get_ecosystem(self, filename: str) -> str:
        """Map filename to ecosystem name."""
        mapping = {
            'package.json': 'npm',
            'requirements.txt': 'python',
            'pyproject.toml': 'python',
            'Pipfile': 'python',
            'Gemfile': 'ruby',
            'go.mod': 'go',
            'Cargo.toml': 'rust',
            'composer.json': 'php',
        }
        return mapping.get(filename, 'unknown')
```

**Dependencies:**
```python
# requirements.txt addition
tomli>=2.0.0  # TOML parser for pyproject.toml
```

---

### 2.2 Version Registry APIs

#### NPM Registry API

```python
import requests
from typing import Optional, Dict

class NPMVersionChecker:
    """Check latest versions from NPM registry."""

    BASE_URL = "https://registry.npmjs.org"

    def get_latest_version(self, package_name: str) -> Optional[str]:
        """Get latest version from NPM registry.

        Returns:
            Latest version string or None if not found
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}/{package_name}",
                timeout=5
            )
            response.raise_for_status()

            data = response.json()
            return data.get('dist-tags', {}).get('latest')

        except requests.RequestException:
            return None

    def get_all_versions(self, package_name: str) -> List[str]:
        """Get all published versions."""
        try:
            response = requests.get(f"{self.BASE_URL}/{package_name}", timeout=5)
            response.raise_for_status()

            data = response.json()
            return list(data.get('versions', {}).keys())

        except requests.RequestException:
            return []
```

---

#### PyPI API

```python
class PyPIVersionChecker:
    """Check latest versions from PyPI."""

    BASE_URL = "https://pypi.org/pypi"

    def get_latest_version(self, package_name: str) -> Optional[str]:
        """Get latest version from PyPI.

        Returns:
            Latest version string or None if not found
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}/{package_name}/json",
                timeout=5
            )
            response.raise_for_status()

            data = response.json()
            return data.get('info', {}).get('version')

        except requests.RequestException:
            return None
```

---

#### RubyGems API

```python
class RubyGemsVersionChecker:
    """Check latest versions from RubyGems."""

    BASE_URL = "https://rubygems.org/api/v1"

    def get_latest_version(self, gem_name: str) -> Optional[str]:
        """Get latest version from RubyGems."""
        try:
            response = requests.get(
                f"{self.BASE_URL}/gems/{gem_name}.json",
                timeout=5
            )
            response.raise_for_status()

            data = response.json()
            return data.get('version')

        except requests.RequestException:
            return None
```

---

#### Go Proxy

```python
class GoProxyVersionChecker:
    """Check latest versions from Go module proxy."""

    BASE_URL = "https://proxy.golang.org"

    def get_latest_version(self, module_path: str) -> Optional[str]:
        """Get latest version from Go proxy.

        Args:
            module_path: e.g., "github.com/pkg/errors"
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}/{module_path}/@latest",
                timeout=5
            )
            response.raise_for_status()

            data = response.json()
            return data.get('Version', '').lstrip('v')  # Remove 'v' prefix

        except requests.RequestException:
            return None
```

---

### 2.3 Version Comparison Algorithm (Semver)

```python
from typing import Tuple
import re

class SemanticVersion:
    """Semantic version parser and comparator."""

    def __init__(self, version_string: str):
        """Parse semantic version string.

        Args:
            version_string: e.g., "1.2.3", "2.0.0-beta.1", "3.1.4+build.123"
        """
        self.original = version_string
        self.major, self.minor, self.patch = self._parse(version_string)

    def _parse(self, version: str) -> Tuple[int, int, int]:
        """Parse version into major.minor.patch."""
        # Remove 'v' prefix if present
        version = version.lstrip('v')

        # Remove pre-release and build metadata
        version = re.split(r'[-+]', version)[0]

        # Split into parts
        parts = version.split('.')

        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0

        return major, minor, patch

    def __lt__(self, other: 'SemanticVersion') -> bool:
        """Less than comparison."""
        return (self.major, self.minor, self.patch) < (other.major, other.minor, other.patch)

    def __eq__(self, other: 'SemanticVersion') -> bool:
        """Equality comparison."""
        return (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch)

    def __repr__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    def major_versions_behind(self, latest: 'SemanticVersion') -> int:
        """Calculate how many major versions behind."""
        return max(0, latest.major - self.major)

    def is_current(self, latest: 'SemanticVersion', tolerance: int = 2) -> bool:
        """Check if version is current (within tolerance of major versions).

        Args:
            latest: Latest available version
            tolerance: Number of major versions considered acceptable

        Returns:
            True if current or within tolerance
        """
        return self.major_versions_behind(latest) <= tolerance

# Usage
current = SemanticVersion("1.2.3")
latest = SemanticVersion("3.0.0")

print(current < latest)  # True
print(current.major_versions_behind(latest))  # 2
print(current.is_current(latest, tolerance=2))  # True
```

---

### 2.4 Unified Version Checker

```python
class TechnologyStackChecker:
    """Unified version checker across all ecosystems."""

    def __init__(self):
        self.checkers = {
            'npm': NPMVersionChecker(),
            'python': PyPIVersionChecker(),
            'ruby': RubyGemsVersionChecker(),
            'go': GoProxyVersionChecker(),
        }

    def check_dependencies(
        self,
        dependencies: Dict[str, List[Dict]]
    ) -> Dict[str, List[Dict]]:
        """Check versions for all dependencies.

        Args:
            dependencies: Output from DependencyParser.detect_dependencies()

        Returns:
            Enriched dependencies with 'latest_version' and 'status' fields
        """
        results = {}

        for ecosystem, deps in dependencies.items():
            checker = self.checkers.get(ecosystem)
            if not checker:
                results[ecosystem] = deps
                continue

            enriched_deps = []
            for dep in deps:
                latest = checker.get_latest_version(dep['name'])

                if latest and dep.get('version'):
                    current = SemanticVersion(dep['version'])
                    latest_ver = SemanticVersion(latest)

                    status = self._determine_status(current, latest_ver)
                else:
                    status = 'unknown'

                enriched_deps.append({
                    **dep,
                    'latest_version': latest,
                    'status': status
                })

            results[ecosystem] = enriched_deps

        return results

    def _determine_status(
        self,
        current: SemanticVersion,
        latest: SemanticVersion
    ) -> str:
        """Determine currency status.

        Returns:
            'current', 'outdated', or 'very outdated'
        """
        if current == latest:
            return 'current'
        elif current.major_versions_behind(latest) == 0:
            return 'outdated'  # Minor/patch behind
        elif current.major_versions_behind(latest) <= 2:
            return 'outdated'  # 1-2 major versions behind
        else:
            return 'very outdated'  # 3+ major versions behind

    def summarize_tech_currency(
        self,
        checked_dependencies: Dict[str, List[Dict]]
    ) -> str:
        """Generate human-readable tech currency summary.

        Returns:
            String like "Mostly current (80% up-to-date)"
        """
        total = 0
        current_count = 0

        for ecosystem, deps in checked_dependencies.items():
            for dep in deps:
                total += 1
                if dep.get('status') == 'current':
                    current_count += 1

        if total == 0:
            return "Unable to determine"

        percent = int((current_count / total) * 100)

        if percent >= 80:
            return f"Mostly current ({percent}% up-to-date)"
        elif percent >= 50:
            return f"Some outdated dependencies ({percent}% up-to-date)"
        else:
            return f"Significantly outdated ({percent}% up-to-date)"
```

---

### 2.5 GitHub API Integration for Dependency Detection

```python
class GitHubDependencyFetcher:
    """Fetch dependency files from GitHub repositories."""

    def __init__(self, github_client):
        self.github = github_client

    def fetch_dependency_files(
        self,
        username: str,
        repo_name: str
    ) -> Dict[str, str]:
        """Fetch all dependency files from a repository.

        Returns:
            Dict mapping filename to file content
        """
        dependency_files = {}

        try:
            repo = self.github.get_repo(f"{username}/{repo_name}")

            # List of files to check
            files_to_check = [
                'package.json',
                'requirements.txt',
                'pyproject.toml',
                'Pipfile',
                'Gemfile',
                'go.mod',
                'Cargo.toml',
                'composer.json'
            ]

            for filename in files_to_check:
                try:
                    file_content = repo.get_contents(filename)
                    if not file_content.is_dir():
                        content = file_content.decoded_content.decode('utf-8')
                        dependency_files[filename] = content
                except:
                    # File doesn't exist, skip
                    continue

            return dependency_files

        except Exception as e:
            print(f"Failed to fetch dependencies for {repo_name}: {e}")
            return {}
```

---

## 3. Commit History Analysis

### Overview

Analyzing commit histories efficiently is crucial for pattern detection and performance. This section covers pagination, sampling, and optimization techniques.

### 3.1 GitHub API Pagination Best Practices

#### Efficient Pagination with PyGithub

```python
from github import Github
from typing import List, Dict, Iterator
import time

class CommitHistoryAnalyzer:
    """Efficiently analyze commit histories with pagination."""

    def __init__(self, github_client: Github):
        self.github = github_client

    def fetch_all_commits(
        self,
        username: str,
        repo_name: str,
        author: Optional[str] = None,
        max_commits: Optional[int] = None
    ) -> List[Dict]:
        """Fetch commits with efficient pagination.

        Args:
            username: Repository owner
            repo_name: Repository name
            author: Filter by author (optional)
            max_commits: Limit total commits (None = all)

        Returns:
            List of commit dictionaries
        """
        try:
            repo = self.github.get_repo(f"{username}/{repo_name}")

            commits = []
            page_size = 100  # GitHub max per page

            # Use PaginatedList iteration
            commit_iterator = repo.get_commits(author=author)

            for commit in commit_iterator:
                commits.append({
                    'sha': commit.sha,
                    'message': commit.commit.message,
                    'author': commit.commit.author.name if commit.commit.author else 'Unknown',
                    'date': commit.commit.author.date.isoformat() if commit.commit.author else None,
                    'repo': repo_name
                })

                # Stop if max reached
                if max_commits and len(commits) >= max_commits:
                    break

            return commits

        except Exception as e:
            print(f"Failed to fetch commits for {repo_name}: {e}")
            return []

    def fetch_commits_with_rate_limit_handling(
        self,
        username: str,
        repo_name: str,
        max_commits: int = 1000
    ) -> List[Dict]:
        """Fetch commits with automatic rate limit handling."""

        commits = []
        page = 0
        per_page = 100

        while len(commits) < max_commits:
            # Check rate limit
            rate_limit = self.github.get_rate_limit()
            if rate_limit.core.remaining < 10:
                # Wait for reset
                wait_time = (rate_limit.core.reset - datetime.now()).total_seconds() + 10
                print(f"Rate limit low, waiting {wait_time}s...")
                time.sleep(wait_time)

            try:
                repo = self.github.get_repo(f"{username}/{repo_name}")
                page_commits = repo.get_commits().get_page(page)

                if not page_commits:
                    break  # No more commits

                for commit in page_commits:
                    commits.append({
                        'sha': commit.sha,
                        'message': commit.commit.message,
                        'author': commit.commit.author.name if commit.commit.author else 'Unknown',
                        'date': commit.commit.author.date.isoformat() if commit.commit.author else None,
                        'repo': repo_name
                    })

                    if len(commits) >= max_commits:
                        break

                page += 1

            except Exception as e:
                print(f"Error fetching page {page}: {e}")
                break

        return commits
```

---

### 3.2 Sampling Strategies for Large Repositories

#### Intelligent Commit Sampling

```python
class CommitSampler:
    """Sample commits intelligently from large repositories."""

    @staticmethod
    def stratified_sample(
        commits: List[Dict],
        max_samples: int = 500,
        include_recent: int = 50
    ) -> List[Dict]:
        """Stratified sampling: recent commits + distributed historical.

        Args:
            commits: Full commit list (chronologically ordered)
            max_samples: Maximum commits to return
            include_recent: Number of recent commits to always include

        Returns:
            Sampled commits preserving temporal distribution
        """
        if len(commits) <= max_samples:
            return commits

        # Always include most recent commits
        recent = commits[-include_recent:]

        # Sample from historical commits
        historical = commits[:-include_recent]
        historical_sample_size = max_samples - include_recent

        # Stratified sampling by time periods
        if len(historical) > historical_sample_size:
            # Divide into time buckets
            bucket_size = len(historical) // historical_sample_size
            sampled_historical = [
                historical[i * bucket_size]
                for i in range(historical_sample_size)
            ]
        else:
            sampled_historical = historical

        return sampled_historical + recent

    @staticmethod
    def importance_sample(
        commits: List[Dict],
        max_samples: int = 500
    ) -> List[Dict]:
        """Sample commits based on importance (merge commits, large changes).

        This requires additional API calls to get commit details,
        so use sparingly.
        """
        # Prioritize:
        # 1. Merge commits (likely important features)
        # 2. Commits with many file changes
        # 3. Commits with release tags

        important_commits = []
        regular_commits = []

        for commit in commits:
            message = commit.get('message', '').lower()

            # Identify important commits
            if any(keyword in message for keyword in ['merge', 'release', 'version']):
                important_commits.append(commit)
            else:
                regular_commits.append(commit)

        # Combine important + sample of regular
        if len(important_commits) >= max_samples:
            return important_commits[:max_samples]

        remaining = max_samples - len(important_commits)
        sampled_regular = regular_commits[::len(regular_commits)//remaining][:remaining]

        return important_commits + sampled_regular
```

---

### 3.3 Pattern Detection from Commit History

#### Frequency Analysis

```python
from datetime import datetime, timedelta
from collections import defaultdict, Counter

class CommitPatternAnalyzer:
    """Detect patterns in commit history."""

    def analyze_frequency(self, commits: List[Dict]) -> Dict[str, Any]:
        """Analyze commit frequency patterns.

        Returns:
            Dict with frequency metrics
        """
        if not commits:
            return {'commits_per_day': 0, 'commits_per_week': 0}

        # Parse dates
        dates = []
        for commit in commits:
            if commit.get('date'):
                date = datetime.fromisoformat(commit['date'].replace('Z', '+00:00'))
                dates.append(date.date())

        if not dates:
            return {'commits_per_day': 0, 'commits_per_week': 0}

        # Calculate time span
        oldest = min(dates)
        newest = max(dates)
        days = (newest - oldest).days + 1
        weeks = days / 7

        # Calculate frequencies
        commits_per_day = len(commits) / days if days > 0 else 0
        commits_per_week = len(commits) / weeks if weeks > 0 else 0

        return {
            'total_commits': len(commits),
            'first_commit': oldest.isoformat(),
            'last_commit': newest.isoformat(),
            'days_active': days,
            'commits_per_day': round(commits_per_day, 2),
            'commits_per_week': round(commits_per_week, 2),
        }

    def analyze_time_of_day(self, commits: List[Dict]) -> Dict[str, Any]:
        """Analyze what times of day commits are made."""
        hour_counts = defaultdict(int)

        for commit in commits:
            if commit.get('date'):
                date = datetime.fromisoformat(commit['date'].replace('Z', '+00:00'))
                hour_counts[date.hour] += 1

        # Find peak hours
        if hour_counts:
            peak_hour = max(hour_counts.items(), key=lambda x: x[1])[0]
        else:
            peak_hour = None

        # Categorize
        total = sum(hour_counts.values())
        night_commits = sum(hour_counts[h] for h in range(22, 24)) + sum(hour_counts[h] for h in range(0, 5))

        if night_commits > total * 0.4:
            pattern = "night_owl"
        else:
            pattern = "daytime"

        return {
            'hour_distribution': dict(hour_counts),
            'peak_hour': peak_hour,
            'pattern': pattern
        }

    def analyze_consistency(self, commits: List[Dict]) -> Dict[str, float]:
        """Analyze commit consistency (regularity of contributions).

        Returns:
            Consistency score (0-100) and metrics
        """
        if not commits:
            return {'consistency_score': 0, 'active_weeks': 0}

        # Group commits by week
        week_counts = defaultdict(int)

        for commit in commits:
            if commit.get('date'):
                date = datetime.fromisoformat(commit['date'].replace('Z', '+00:00'))
                week_key = f"{date.year}-W{date.isocalendar()[1]:02d}"
                week_counts[week_key] += 1

        if not week_counts:
            return {'consistency_score': 0, 'active_weeks': 0}

        # Calculate coefficient of variation (lower = more consistent)
        weekly_counts = list(week_counts.values())
        mean = sum(weekly_counts) / len(weekly_counts)

        if mean == 0:
            return {'consistency_score': 0, 'active_weeks': 0}

        variance = sum((x - mean) ** 2 for x in weekly_counts) / len(weekly_counts)
        std_dev = variance ** 0.5
        cv = std_dev / mean

        # Convert to 0-100 score (lower CV = higher consistency)
        consistency_score = max(0, min(100, 100 * (1 - min(cv / 2, 1))))

        return {
            'consistency_score': round(consistency_score, 1),
            'active_weeks': len(week_counts),
            'avg_commits_per_week': round(mean, 1),
            'coefficient_of_variation': round(cv, 2)
        }

    def detect_bursts(self, commits: List[Dict], threshold: int = 10) -> List[Dict]:
        """Detect burst periods (high commit activity).

        Args:
            threshold: Minimum commits per day to qualify as burst

        Returns:
            List of burst periods with start/end dates
        """
        # Group commits by day
        day_counts = defaultdict(int)

        for commit in commits:
            if commit.get('date'):
                date = datetime.fromisoformat(commit['date'].replace('Z', '+00:00'))
                day_counts[date.date()] = day_counts[date.date()] + 1

        # Find burst days
        bursts = []
        for day, count in day_counts.items():
            if count >= threshold:
                bursts.append({
                    'date': day.isoformat(),
                    'commits': count
                })

        return sorted(bursts, key=lambda x: x['date'])
```

---

### 3.4 Performance Optimization

#### Caching Strategies

```python
from spark.cache import APICache
import hashlib

class OptimizedCommitFetcher:
    """Optimized commit fetching with caching and batching."""

    def __init__(self, github_client: Github, cache: APICache):
        self.github = github_client
        self.cache = cache

    def fetch_commits_cached(
        self,
        username: str,
        repo_name: str,
        max_commits: int = 1000
    ) -> List[Dict]:
        """Fetch commits with intelligent caching.

        Cache key includes repo + last_updated to invalidate on new commits.
        """
        # Get repo metadata
        repo = self.github.get_repo(f"{username}/{repo_name}")
        last_updated = repo.updated_at.isoformat()

        # Create cache key
        cache_key = f"commits_{username}_{repo_name}_{last_updated}"

        # Check cache
        cached = self.cache.get(cache_key)
        if cached:
            return cached

        # Fetch from API
        analyzer = CommitHistoryAnalyzer(self.github)
        commits = analyzer.fetch_all_commits(username, repo_name, max_commits=max_commits)

        # Cache result (7 days TTL)
        self.cache.set(cache_key, commits)

        return commits

    def batch_fetch_commits(
        self,
        repositories: List[Dict],
        username: str,
        max_commits_per_repo: int = 100
    ) -> Dict[str, List[Dict]]:
        """Fetch commits for multiple repositories in batch.

        Returns:
            Dict mapping repo name to commits list
        """
        all_commits = {}

        for i, repo in enumerate(repositories):
            repo_name = repo['name']

            # Progress indicator
            print(f"Fetching commits for {repo_name} ({i+1}/{len(repositories)})")

            commits = self.fetch_commits_cached(
                username,
                repo_name,
                max_commits=max_commits_per_repo
            )

            all_commits[repo_name] = commits

            # Rate limit protection
            if i % 10 == 0:
                self._check_rate_limit()

        return all_commits

    def _check_rate_limit(self):
        """Check and wait if rate limit is low."""
        rate_limit = self.github.get_rate_limit()

        if rate_limit.core.remaining < 100:
            wait_time = (rate_limit.core.reset - datetime.now()).total_seconds() + 10
            print(f"Rate limit low ({rate_limit.core.remaining}), waiting {wait_time}s...")
            time.sleep(wait_time)
```

---

#### Parallel Fetching (for large-scale analysis)

```python
import concurrent.futures
from typing import Callable

class ParallelCommitFetcher:
    """Fetch commits in parallel for better performance."""

    def __init__(self, github_client: Github, max_workers: int = 5):
        self.github = github_client
        self.max_workers = max_workers

    def fetch_commits_parallel(
        self,
        repositories: List[Dict],
        username: str,
        max_commits_per_repo: int = 100
    ) -> Dict[str, List[Dict]]:
        """Fetch commits for multiple repos in parallel.

        Note: Be careful with rate limits when using parallel fetching.
        """
        results = {}

        def fetch_single_repo(repo: Dict) -> Tuple[str, List[Dict]]:
            """Fetch commits for a single repository."""
            repo_name = repo['name']
            analyzer = CommitHistoryAnalyzer(self.github)
            commits = analyzer.fetch_all_commits(
                username,
                repo_name,
                max_commits=max_commits_per_repo
            )
            return (repo_name, commits)

        # Use ThreadPoolExecutor (GitHub API is I/O bound)
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            future_to_repo = {
                executor.submit(fetch_single_repo, repo): repo
                for repo in repositories
            }

            # Collect results as they complete
            for future in concurrent.futures.as_completed(future_to_repo):
                try:
                    repo_name, commits = future.result()
                    results[repo_name] = commits
                    print(f"Completed: {repo_name} ({len(commits)} commits)")
                except Exception as e:
                    repo = future_to_repo[future]
                    print(f"Failed to fetch {repo['name']}: {e}")
                    results[repo['name']] = []

        return results
```

---

## 4. Integration Recommendations

### 4.1 Unified Architecture

```python
# Proposed file structure
"""
src/spark/
├── ai/
│   ├── __init__.py
│   ├── summarizer.py        # Claude integration
│   ├── prompts.py            # Prompt templates
│   └── fallback.py           # Rule-based fallback
├── dependencies/
│   ├── __init__.py
│   ├── parser.py             # Multi-ecosystem parsing
│   ├── version_checker.py    # Registry APIs
│   └── semver.py             # Version comparison
├── analysis/
│   ├── __init__.py
│   ├── commit_analyzer.py    # Pattern detection
│   ├── sampler.py            # Commit sampling
│   └── patterns.py           # Pattern algorithms
└── report/
    ├── __init__.py
    ├── generator.py          # Markdown report generation
    └── templates.py          # Report templates
"""
```

---

### 4.2 Configuration Updates

```yaml
# config/spark.yml additions

ai:
  enabled: true
  provider: "anthropic"  # anthropic | openai | local
  model: "claude-3-5-sonnet-20241022"
  fallback_to_rules: true
  cache_ttl_days: 7
  max_tokens: 1024

dependencies:
  check_versions: true
  ecosystems:
    - npm
    - python
    - ruby
    - go
  tolerance_major_versions: 2  # 2 major versions behind = "outdated"

commit_analysis:
  max_commits_per_repo: 1000
  sampling_strategy: "stratified"  # stratified | importance | none
  enable_pattern_detection: true
```

---

### 4.3 Dependencies to Add

```python
# requirements.txt additions

# AI Summarization
anthropic>=0.20.0          # Claude API (recommended)
# openai>=1.0.0            # Alternative: OpenAI API
# llama-cpp-python>=0.2.0  # Alternative: Local models

# Dependency Parsing
tomli>=2.0.0               # TOML parser for pyproject.toml

# HTTP with retries
requests>=2.31.0           # Already present, ensure version

# Async support (optional, for parallel fetching)
aiohttp>=3.9.0
```

---

### 4.4 Implementation Priority

#### Phase 1: MVP (Week 1)
1. ✅ Rule-based summarization (fallback)
2. ✅ Basic dependency parsing (package.json, requirements.txt)
3. ✅ Commit frequency analysis

#### Phase 2: AI Integration (Week 2)
1. ✅ Claude API integration
2. ✅ Prompt engineering and testing
3. ✅ Caching and rate limiting

#### Phase 3: Advanced Features (Week 3)
1. ✅ Multi-ecosystem dependency support
2. ✅ Version currency assessment
3. ✅ Pattern detection (time of day, bursts, consistency)

#### Phase 4: Optimization (Week 4)
1. ✅ Performance tuning
2. ✅ Parallel fetching
3. ✅ Cost optimization

---

### 4.5 Testing Strategy

```python
# tests/unit/test_ai_summarizer.py
def test_claude_summarization():
    """Test Claude API summarization."""
    summarizer = ClaudeRepositorySummarizer(api_key=os.environ['ANTHROPIC_API_KEY'])

    summary = summarizer.summarize_repository(
        repo_name="test-repo",
        readme_content="This is a test README",
        commit_history=[],
        metadata={'stars': 10, 'language': 'Python'}
    )

    assert 'short_summary' in summary
    assert 'tech_stack' in summary

# tests/unit/test_dependency_parser.py
def test_npm_parsing():
    """Test package.json parsing."""
    parser = DependencyParser()

    package_json = '''
    {
      "dependencies": {
        "react": "^18.0.0",
        "express": "~4.18.0"
      }
    }
    '''

    deps = parser.parse_npm(package_json)

    assert len(deps) == 2
    assert deps[0]['name'] == 'react'
    assert deps[0]['version'] == '18.0.0'

# tests/integration/test_full_workflow.py
def test_generate_ai_powered_report():
    """Test full AI-powered report generation."""
    # This would test the entire pipeline end-to-end
    pass
```

---

## 5. Summary and Quick Recommendations

### TL;DR - What to Use

| Feature | Recommended Tool/Approach | Why |
|---------|---------------------------|-----|
| **AI Summarization** | Anthropic Claude 3.5 Sonnet | Best balance of cost, quality, and context window (200K tokens) |
| **Fallback** | Rule-based extraction | Graceful degradation when API unavailable |
| **Dependency Parsing** | Custom parsers per ecosystem | Full control, no external dependencies |
| **Version APIs** | Native registry APIs (npm, PyPI, etc.) | Official, reliable, free |
| **Version Comparison** | Custom SemanticVersion class | Lightweight, no dependencies |
| **Commit Fetching** | PyGithub with caching | Already in use, efficient pagination |
| **Sampling** | Stratified sampling | Preserves temporal distribution |
| **Pattern Detection** | Statistical analysis (CV, frequencies) | Accurate, interpretable |

---

### Cost Estimates

**For 50 repositories:**
- AI Summarization: ~$1.13 (Claude)
- Version API calls: $0 (all free public APIs)
- GitHub API: $0 (within free tier with token)
- **Total: ~$1.13 per report**

**For 500 repositories (user with many repos):**
- AI Summarization: ~$11.30
- **Total: ~$11.30 per report**

---

### Performance Targets

| Operation | Target Time | Notes |
|-----------|-------------|-------|
| Fetch 50 repos metadata | <30s | With caching |
| Fetch commits (50 repos × 100 commits) | 1-2 min | With pagination |
| Parse dependencies (50 repos) | <10s | Local parsing |
| Check versions (50 repos × 10 deps) | 1-2 min | API calls, can parallelize |
| Generate AI summaries (50 repos) | 2-3 min | Rate limited to 50 req/min |
| **Total report generation** | **5-8 minutes** | For 50 repos, first run |
| **Cached report generation** | **<1 minute** | With valid cache |

---

### Next Steps

1. **Week 1**: Implement rule-based fallback and basic dependency parsing
2. **Week 2**: Add Claude AI integration with prompt templates
3. **Week 3**: Expand to multi-ecosystem dependency support
4. **Week 4**: Optimize performance and add parallel fetching

---

### References and Resources

**AI APIs:**
- [Anthropic Claude API Docs](https://docs.anthropic.com)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [llama.cpp GitHub](https://github.com/ggerganov/llama.cpp)

**Version APIs:**
- [NPM Registry API](https://github.com/npm/registry/blob/master/docs/REGISTRY-API.md)
- [PyPI JSON API](https://warehouse.pypa.io/api-reference/json.html)
- [RubyGems API](https://guides.rubygems.org/rubygems-org-api/)
- [Go Module Proxy](https://go.dev/ref/mod#module-proxy)

**Semantic Versioning:**
- [Semver.org](https://semver.org)
- [Python semver library](https://pypi.org/project/semver/)

**GitHub API:**
- [PyGithub Documentation](https://pygithub.readthedocs.io)
- [GitHub REST API](https://docs.github.com/en/rest)

---

**Document Version**: 1.0
**Last Updated**: 2025-12-28
**Author**: Research Analysis for GitHub Stats Spark
