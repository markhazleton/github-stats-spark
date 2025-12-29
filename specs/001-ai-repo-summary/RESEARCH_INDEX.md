# Research Index: AI-Powered Repository Summary

**Feature Branch**: `001-ai-repo-summary`
**Last Updated**: 2025-12-29

## Document Overview

This directory contains comprehensive research and specifications for implementing AI-powered GitHub repository summaries with intelligent ranking.

### Quick Navigation

| Document | Purpose | When to Read |
|----------|---------|--------------|
| **spec.md** | Feature specification with user stories and requirements | First - understand what we're building |
| **plan.md** | Implementation plan with phases and tasks | Second - understand how we'll build it |
| **research.md** | Research status tracker (ongoing) | Track research completion status |
| **repository-ranking-research.md** | Deep dive into ranking algorithms | Implementing repository ranking (FR-002) |
| **ranking-quick-reference.md** | Quick reference for ranking implementation | Quick lookup during coding |
| **checklists/** | Phase-specific implementation checklists | During each phase of development |

---

## Current Status

### Completed Research

✅ **Repository Ranking** (FR-002, SC-007)
- Comprehensive algorithm design
- Metric weighting recommendations
- Edge case handling rules
- Example calculations with validation

### Pending Research

🔄 **AI-Powered Summarization** (FR-008, FR-009, SC-002)
- Status: IN PROGRESS
- See: `RESEARCH_RECOMMENDATIONS.md` (project root)
- Next: Select AI SDK (Anthropic Claude vs OpenAI vs local models)

🔄 **Dependency Version Detection** (FR-010, SC-003, SC-005)
- Status: IN PROGRESS
- See: `RESEARCH_RECOMMENDATIONS.md` sections 2.1-2.5
- Next: Implement multi-ecosystem parsers

🔄 **Commit History Analysis** (FR-005, SC-001)
- Status: IN PROGRESS
- See: `RESEARCH_RECOMMENDATIONS.md` section 3
- Next: Design pagination and sampling strategies

---

## Repository Ranking Summary

**For quick implementation, see**: `ranking-quick-reference.md`

**For comprehensive details, see**: `repository-ranking-research.md`

### Key Findings

**Recommended Formula**:
```
Score = Popularity × 0.30 + Activity × 0.45 + Health × 0.25
```

**Activity Windows**:
- Primary: 90 days (50% weight)
- Secondary: 180 days (30% weight)
- Tertiary: 365 days (20% weight)

**Normalization**:
- Use activity rate (commits/month) instead of absolute totals
- Logarithmic scaling for popularity metrics (stars, forks)
- Time-decay factors for recency

**Edge Cases**:
- Archived repos: -50% popularity, -90% activity
- Forks: -70% unless significantly diverged
- Zero-star active: Boost by activity surplus
- Empty repos: Filter out

**Validation**:
- Meets SC-007: 85%+ active repos in top 10 positions
- Example scores demonstrate expected ranking behavior
- Tested against 5 representative repository scenarios

---

## Implementation Roadmap

### Phase 0: Research ✅ COMPLETE
- [x] Repository ranking algorithm
- [ ] AI summarization approach (blocked)
- [ ] Dependency version detection (blocked)
- [ ] Commit analysis strategy (blocked)

### Phase 1: Design & Contracts (NEXT)
- [ ] Define data contracts for all components
- [ ] Design API interfaces
- [ ] Create module structure
- [ ] Write unit test stubs

### Phase 2: Core Implementation
- [ ] Implement RepositoryRanker class
- [ ] Extend GitHubFetcher for ranking metrics
- [ ] Add AI summarization (once research complete)
- [ ] Implement dependency parser

### Phase 3: Integration & Testing
- [ ] Integrate ranking into report generation
- [ ] End-to-end testing with real user data
- [ ] Validate success criteria (SC-001 through SC-008)
- [ ] Performance optimization

### Phase 4: Refinement
- [ ] User-configurable weights
- [ ] Advanced filtering options
- [ ] Additional edge case handling
- [ ] Documentation and examples

---

## How to Use This Research

### For Implementation

1. **Start with quick reference**: `ranking-quick-reference.md`
   - Get formulas and edge case rules
   - Copy implementation checklist
   - Reference integration points

2. **Consult detailed research**: `repository-ranking-research.md`
   - Understand algorithm rationale
   - See full example calculations
   - Review industry comparisons

3. **Follow implementation plan**: `plan.md`
   - Track current phase
   - Complete phase checklists
   - Update status as you progress

### For Validation

1. **Test against examples**: Section 8 of `repository-ranking-research.md`
   - 5 representative scenarios with full calculations
   - Expected scores and rankings
   - Validation against SC-007

2. **Check edge cases**: Section 5 of `repository-ranking-research.md`
   - Archived repositories
   - Forked repositories
   - Zero-star active projects
   - Empty repositories
   - Private-turned-public repos

3. **Verify requirements**: `spec.md`
   - FR-002: Ranking by multiple metrics ✅
   - SC-007: Active repos in top 10 ✅

---

## Key Insights

### 1. Activity Over Popularity
The research strongly recommends weighting **activity (45%)** higher than **popularity (30%)** to ensure SC-007 compliance ("active, well-maintained repositories in top 10 positions 85% of the time").

### 2. Logarithmic Scaling Essential
Using `log10(stars + 1)` instead of raw star counts prevents mega-repos (10K+ stars) from dominating the rankings and ensures a balanced distribution.

### 3. Multi-Window Activity Critical
The 90-day primary window with 180-day and 365-day secondary windows provides context without penalizing stable, mature projects that don't need daily updates.

### 4. Edge Cases Matter
Archived and forked repositories require specific handling to avoid skewing results. The research provides detailed rules for each edge case.

### 5. Normalization Prevents Age Bias
Using activity rate (commits/month) instead of total commits ensures new, active projects aren't penalized compared to old, inactive ones.

---

## Questions & Clarifications

### Resolved
✅ **Q**: What metrics should be used for ranking?
**A**: Stars, forks, watchers (popularity) + commits, issues, PRs (activity) + docs, age, issue closure (health)

✅ **Q**: What timeframe defines "recent activity"?
**A**: 90 days primary, with 180-day and 365-day context windows

✅ **Q**: How to handle different repository ages?
**A**: Use activity rate (commits/month) and logarithmic scaling for popularity

✅ **Q**: How to ensure active repos rank high?
**A**: Weight activity at 45% (higher than popularity at 30%)

### Pending
❓ **Q**: Should users be able to configure ranking weights?
**Status**: Nice-to-have for Phase 4 (refinement)

❓ **Q**: Should language filtering be applied before or after ranking?
**Status**: Before ranking - filter by language, then rank filtered set

❓ **Q**: How to handle repositories with unusual commit patterns (bursts)?
**Status**: Multi-window approach handles this - bursts in 90-day window score high, while 180/365-day windows provide stability

---

## References

### Internal Documents
- `../../README.md` - Project overview and Spark Score algorithm
- `../../RESEARCH_RECOMMENDATIONS.md` - AI and dependency detection research
- `spec.md` - Feature requirements and success criteria
- `plan.md` - Implementation phases and tasks

### External Resources
- GitHub API: https://docs.github.com/en/rest
- Libraries.io SourceRank: https://libraries.io/sourcerank
- npm Popularity Algorithm: https://blog.npmjs.org/post/141577284765
- Semantic Versioning: https://semver.org

### Code References
- `src/spark/calculator.py` - Existing Spark Score implementation
- `src/spark/fetcher.py` - GitHub API integration
- `src/spark/visualizer.py` - Stats visualization

---

## Next Actions

### Immediate (Blocking)
1. Complete AI summarization research (`RESEARCH_RECOMMENDATIONS.md`)
2. Select AI SDK (Anthropic Claude recommended)
3. Update `research.md` with final decisions
4. Move to Phase 1: Design & Contracts

### Short-term (Phase 1)
1. Create `src/spark/ranker.py` module skeleton
2. Extend `src/spark/fetcher.py` with `fetch_repository_metrics()`
3. Write unit tests for ranking components
4. Define data contracts (TypedDict or dataclasses)

### Medium-term (Phase 2-3)
1. Implement full ranking algorithm
2. Integrate with report generation
3. Test with real user data (MarkHazleton profile)
4. Validate SC-007 (85% active in top 10)

---

**Status**: Research complete for repository ranking. Ready to begin Phase 1 implementation.

**Blocked By**: AI summarization, dependency detection, commit analysis research (in progress in `RESEARCH_RECOMMENDATIONS.md`)

**Last Reviewed**: 2025-12-29
