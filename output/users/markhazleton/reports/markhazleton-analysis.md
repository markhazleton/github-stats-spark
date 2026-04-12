# GitHub Profile: markhazleton

**Generated**: 2026-04-12 06:02:19 UTC
**Report Version**: 1.0.0
**Repositories Analyzed**: 33
**AI Summary Rate**: 100.0%

> 💡 **Navigation**: [Profile Overview](#profile-overview) | [Top Repositories](#top-33-repositories) | [Metadata](#report-metadata)

---

## Profile Overview

### Activity Dashboard

![Overview Statistics](../overview.svg)

### Commit Activity

![Commit Heatmap](../heatmap.svg)

![Coding Streaks](../streaks.svg)

### Technology Breakdown

![Language Distribution](../languages.svg)

![Fun Statistics](../fun.svg)

### Release Patterns

![Release Cadence](../release.svg)

---

## Top 33 Repositories

### #1. [devspark](https://github.com/markhazleton/devspark)

Stars: 0 | Forks: 0 | Language: PowerShell | 179 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 6534 KB | 🚀 59.7 commits/month

**Quality**: ❌ License | ✅ Docs

# DevSpark Technical Summary

**DevSpark** is a structured development workflow framework delivered as a collection of 25 markdown-based prompt templates designed to guide AI coding assistants (Claude, Copilot, Cursor, Gemini, and 13+ others) through a complete software development lifecycle—from requirements specification through release. Rather than being installed software, DevSpark operates as a "copy-paste" system of prompt files that establish repeatable processes without external dependencies, making it immediately usable in any project by simply placing markdown files into the repository.

The framework implements a multi-layered command architecture organized around core workflows (`/devspark.specify`, `/devspark.plan`, `/devspark.implement`, `/devspark.create-pr`) augmented by constitution-powered utilities for code review, auditing, refactoring, and release management. It features a sophisticated 3-tier prompt resolution system that cleanly separates stock templates (`.devspark/`), organizational customizations (`.documentation/`), and personal overrides, enabling safe upgrades and team-wide consistency without risk of configuration loss. The codebase combines PowerShell (38.1%), Shell (33.0%), and Python (28.9%) for cross-platform context-gathering scripts and an optional CLI tool built with Click and Pydantic for automated setup and repository management.

A distinctive feature is its optional **multi-app monorepo support**, which allows complex repositories with different platforms or governance requirements to maintain application-specific constitutions and rules through a registry system (`devspark.json`), while single-app projects require no additional configuration. The project maintains strong momentum (179 commits in 90 days, 707 in 365 days) with a modern tech stack score of 80/100, positioning it as a production-ready solution for teams seeking AI-assisted development with human-controlled governance and audit trails through markdown-first documentation rather than code-level abstractions.

**Technology Stack Currency**: ✅ 80/100
**Dependencies**: 3 total (1 current, 2 outdated)

**Created**: 2026-04-02
**Last Modified**: 2026-04-12

---

### #2. [TailwindSpark](https://github.com/markhazleton/TailwindSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 81 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 3973 KB | 🚀 27.0 commits/month

**Quality**: ❌ License | ✅ Docs

# TailwindSpark Technical Summary

**TailwindSpark** is a production-ready React TypeScript monorepo that serves as both a comprehensive Tailwind CSS showcase and a modern web development learning resource. The project demonstrates contemporary best practices through a multi-package architecture (using Turborepo) that includes a demo application, shared design token system leveraging Tailwind CSS 4's @theme directive, and a reusable UI component library—all built with strict TypeScript typing and maintaining a minimum 40% test coverage with WCAG AA accessibility compliance.

The repository is distinguished by its formal governance structure (documented constitution), automated development workflows (Dependabot dependency management, CI/CD pipeline, security scanning), and extensive documentation covering architecture, testing standards, and deployment strategies. It employs semantic design tokens and advanced component patterns to illustrate scalable design systems while maintaining production-quality code standards through ESLint, Vitest testing, and performance monitoring. Built with React 19.1.1, TypeScript 5.9, and Tailwind CSS 4.1.18, the project represents an actively maintained reference implementation (81 commits in 90 days with accelerating activity) ideal for developers seeking to understand modern React patterns, design system implementation, or production-ready monorepo architecture—serving both as an educational resource and a deployable showcase application accessible via live demo.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2025-07-29
**Last Modified**: 2026-04-11

---

### #3. [github-stats-spark](https://github.com/markhazleton/github-stats-spark)

Stars: 0 | Forks: 0 | Language: Python | 115 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 16167 KB | 🚀 38.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: github-stats-spark

## Repository Overview

**Stats Spark** is a comprehensive GitHub analytics platform that automatically generates beautiful SVG visualizations and AI-powered insights from GitHub activity data. The project serves as an automated profile statistics generator that transforms raw GitHub metrics into actionable intelligence through both visual dashboards and detailed markdown reports. It's designed for developers, teams, and open-source maintainers who want to showcase their GitHub activity professionally while gaining deeper insights into contribution patterns and repository health.

## Core Functionality

The system operates across three primary components:

1. **SVG Profile Statistics Generator**: Automatically creates embeddable visualizations including a Spark Score (0-100 composite metric), commit heatmaps, language breakdowns, streak tracking, and release cadence charts. Uses a weighted algorithm (40% consistency, 35% volume, 25% collaboration) to calculate the unique Spark Score metric.

2. **AI-Powered Repository Analysis**: Integrates Claude Haiku for intelligent repository summaries with a three-tier fallback system (AI generation → README extraction → metadata fallback), achieving 97%+ success rates. Implements composite ranking algorithms weighing popularity (30%), activity with time-decay windows (45%), and health signals (25%).

3. **Interactive Mobile-First Dashboard**: A React-based web application with touch-optimized interactions, bottom-sheet navigation, Chart.js visualizations, and offline support via IndexedDB/Dexie caching. Features a "Needs Attention" view that ranks repositories by security alerts, PR backlog, dependency drift, and staleness metrics.

## Technical Architecture

**Backend Stack**: Python 3.11+ with PyGithub for API interactions, PyYAML for configuration management, svgwrite for SVG generation, and python-dateutil for temporal analysis. The system implements smart caching, rate-limit handling with exponential backoff, and processes up to 500 repositories in under 5 minutes.

**Frontend Stack**: JavaScript/React with Chart.js for analytics visualizations, Dexie for offline-first IndexedDB caching, and CSS for WCAG 2.1 AA compliant theming (dark, light, and custom variants). Lighthouse CI targets <2s First Contentful Paint with 0.9+ performance scores.

**Deployment & Automation**: GitHub Actions workflow executes weekly at midnight UTC on Sundays for automated updates. Output includes SVG artifacts stored in GitHub Pages for profile README embedding, and comprehensive markdown reports with embedded visualizations. Supports flexible YAML-based configuration for customization and CLI tools for local development/testing.

## Distinctive Features

- **Spark Score Algorithm**: Proprietary weighted composite metric combining consistency, volume, and collaboration signals
- **Three-Tier AI Fallback**: Ensures summary generation even when primary AI service unavailable
- **Schema 2.2.0 Standardization**: Unified repository records tracking attention metrics, dependency coverage, and maintenance signals
- **Mobile-Native UX Patterns**: Swipe gestures, touch-optimized targets (44×44px), and responsive layouts (320-768px viewports)
- **Zero-Maintenance Setup**: Automated weekly updates via GitHub Actions with configurable parameters
- **Offline-First Architecture**: IndexedDB caching with 7-day retention for dashboard access without internet

## Project Health Metrics

The repository shows strong momentum with 115 commits over 90 days and 228 commits annually, demonstrating consistent development activity. With a tech stack currency score of 69/100, the project maintains modern dependencies while utilizing established libraries. The multilingual codebase (49.6% Python, 21.5% JavaScript, 18.9% PowerShell) reflects a full-stack development approach encompassing backend analytics, frontend visualization, and automation scripting. Despite zero stars/forks currently (likely due to recent creation on 2025-12-28), the project exhibits enterprise-ready patterns including comprehensive error handling, intelligent API optimization, and extensible modular architecture suitable for integration into larger GitHub analytics platforms.

**Technology Stack Currency**: ✅ 69/100
**Dependencies**: 10 total (1 current, 9 outdated)

**Created**: 2025-12-28
**Last Modified**: 2026-04-12

---

### #4. [WebSpark.HttpClientUtility](https://github.com/markhazleton/WebSpark.HttpClientUtility)

Stars: 0 | Forks: 0 | Language: C# | 65 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2736 KB | 🚀 21.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.HttpClientUtility

**WebSpark.HttpClientUtility** is a production-ready .NET 8-10 LTS wrapper library that abstracts away boilerplate HTTP client configuration by providing one-line dependency injection setup (`AddHttpClientUtility()`) that automatically integrates Polly-based resilience patterns (retries, circuit breakers), intelligent in-memory response caching, structured logging with correlation IDs, and OpenTelemetry distributed tracing—eliminating 50+ lines of manual setup code typically required for enterprise microservices. The library is distributed as two focused NuGet packages: the core **WebSpark.HttpClientUtility** (163 KB) for HTTP client utilities with authentication and telemetry support, and **WebSpark.HttpClientUtility.Crawler** (75 KB) extending it with web crawling, robots.txt parsing, and sitemap generation capabilities.

Built with architectural patterns emphasizing separation of concerns, the project uses dependency injection-friendly service abstractions (`IHttpRequestResultService`), provides strongly-typed generic request/response models, and implements comprehensive cross-cutting concerns (correlation tracking, observability, resilience) transparently without requiring consumer code changes. The codebase demonstrates production maturity through Source Link debugging support, Native AOT and IL-trimming compatibility annotations, semantic versioning with zero breaking-change guarantees within major versions, zero-warning strict compilation, and CI/CD automation across multiple .NET versions via GitHub Actions. 

The library targets microservices architects, background job workers, and web scraping scenarios where developers want enterprise-grade reliability and observability without maintaining complex Polly policies, custom logging middleware, or OpenTelemetry instrumentation boilerplate—positioning itself as a middle ground between raw `HttpClient` (maximum control, maximum complexity) and declarative alternatives like Refit (type-safe but less flexible for cross-cutting resilience patterns). With 65 commits over 90 days and consistent activity patterns, the project maintains active development and community engagement through GitHub Discussions, comprehensive documentation sites, and backward-compatible updates aligned with .NET LTS release cycles.

**Created**: 2025-05-03
**Last Modified**: 2026-03-31

---

### #5. [MuseumSpark](https://github.com/markhazleton/MuseumSpark)

Stars: 0 | Forks: 0 | Language: Python | 77 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 23887 KB | 🚀 25.7 commits/month

**Quality**: ❌ License | ✅ Docs

# MuseumSpark: Technical Summary

**MuseumSpark** is an intelligent travel planning platform that transforms the Walker Art Center Reciprocal Program membership list (1,269 museums across North America) into a data-rich resource for art enthusiasts. The project employs a sophisticated multi-phase data enrichment pipeline that systematically augments museum records through structured extraction from Wikidata, Wikipedia, official websites, and manual curation, with the ultimate goal of enabling priority-based travel recommendations powered by expert scoring and AI analysis.

The platform currently features a React 19 + Vite frontend deployed via GitHub Pages that provides comprehensive browsing, searching, and filtering across the museum dataset, complemented by a real-time progress dashboard tracking enrichment completion across multiple validation phases. The backend architecture leverages Python 3.11+ with Pydantic for schema validation and BeautifulSoup4 for web scraping, implementing a robust JSON Schema validation framework that enforces data quality rules (notably "never replace known with null") and maintains evidence tracking for all enriched fields.

The project follows a deliberately phased roadmap progressing from foundational data work (currently at Phase 0–1, with only 0.08% full enrichment) through expert scoring in Phase 2, AI-assisted content validation in Phase 2.5–3, and ultimately a full-featured FastAPI backend with user authentication and personalized trip planning capabilities in Phase 4. This demonstrates strong architectural foresight, separating concerns across data curation, frontend presentation, and future backend services while maintaining flexibility to evolve from static hosting to self-hosted infrastructure. The active development trajectory (77 commits in 90 days, accelerating activity) and transparent progress tracking reflect a well-organized, methodical approach to solving the complex problem of museum data standardization and intelligent travel planning for a niche but passionate user base.

**Created**: 2026-01-15
**Last Modified**: 2026-03-29

---

### #6. [UISampleSpark](https://github.com/markhazleton/UISampleSpark)

Stars: 8 | Forks: 4 | Language: HTML | 88 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 31056 KB | 🚀 29.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: UISampleSpark

**UISampleSpark** is an educational .NET 10 (ASP.NET Core) reference application that comprehensively demonstrates and compares multiple modern front-end UI frameworks and architectural patterns using a common Employee/Department domain model. The repository implements seven distinct UI approaches—MVC Controllers, Razor Pages, React 18 SPA, Vue 3 SPA, htmx, Blazor Server, and vanilla JavaScript SPA with DataTables—allowing developers to evaluate implementation trade-offs in rendering strategy, interactivity model, and developer experience side-by-side.

The application showcases enterprise-grade architecture including dependency injection, repository/service patterns, Entity Framework Core data access, REST/OpenAPI endpoints with Swagger documentation, comprehensive unit testing, and production-ready DevOps practices (GitHub Actions CI/CD, Docker containerization, Azure deployments). Key features include dynamic Bootswatch theme switching with light/dark modes, Bootstrap 5 responsive UI, API key authentication, Application Insights telemetry, health checks, and modal-based form interactions, with additional reporting capabilities via PivotTable.js visualizations.

The tech stack leverages .NET 10 with C#, ASP.NET Core, Entity Framework Core (InMemory), and a curated selection of NuGet packages including Swashbuckle for OpenAPI documentation, custom WebSpark utility libraries for HTTP clients and theme management, and Westwind Markdown rendering. The project demonstrates modern .NET development practices including minimal APIs, SignalR-based real-time updates via Blazor, and containerized deployment patterns, making it particularly valuable for architects and developers evaluating UI framework suitability, modernizing legacy ASP.NET applications, or establishing reference implementations for enterprise web applications.

**Created**: 2019-04-25
**Last Modified**: 2026-04-11

---

### #7. [git-spark](https://github.com/markhazleton/git-spark)

Stars: 0 | Forks: 0 | Language: TypeScript | 44 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 1539 KB | 🚀 14.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Git Spark - Technical Summary

**Git Spark** is a TypeScript-based Git repository analytics and reporting tool that analyzes commit history to generate comprehensive insights into contributor activity, code changes, and development patterns. The project provides both a command-line interface and Node.js API for analyzing repositories and exporting data in multiple formats (HTML, JSON, CSV, Markdown), with a primary focus on generating interactive HTML dashboards featuring charts, contributor statistics, file analysis, and governance metrics.

The tool offers advanced analytical capabilities including daily activity trends, contribution heatmaps, risk factor assessments, governance radar charts for conventional commit adherence, and file/directory change pattern analysis—all based purely on Git commit data without external dependencies or API calls. Key features include dark mode support with persistent preferences, one-click data export functionality, email redaction for privacy-sensitive audits, and progressive table pagination for handling large datasets efficiently.

Built with a modern tech stack (TypeScript, Commander.js for CLI, Chalk/Boxen for terminal UI, Ora for spinners, and Semver for versioning), Git Spark maintains a high tech currency score (88/100) and requires Node.js 20.19.0+. The architecture emphasizes security with strict Content Security Policy enforcement using SHA-256 hashed inline scripts, native SVG charts to avoid external dependencies, and fully self-contained reports suitable for air-gapped environments.

The project demonstrates active development with 163 commits over a year and consistent contribution patterns, making it suitable for teams requiring repository governance analysis, code health assessments, and audit trails. It serves as both a standalone analytics tool for development teams and a programmatic library for custom integrations, with particular utility for organizations needing transparent, offline-capable audit reports with comprehensive metric documentation explaining data limitations.

**Technology Stack Currency**: ✅ 88/100
**Dependencies**: 19 total (12 current, 7 outdated)

**Created**: 2025-09-29
**Last Modified**: 2026-04-06

---

### #8. [JsBootSpark](https://github.com/markhazleton/JsBootSpark)

Stars: 0 | Forks: 0 | Language: JavaScript | 45 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 3736 KB | 🚀 15.0 commits/month

**Quality**: ❌ License | ✅ Docs

# JsBootSpark - Technical Summary

**JsBootSpark** is a modern Bootstrap 5 + Express starter kit designed for rapid development and static site deployment to GitHub Pages, bridging local dynamic development with production-ready static output. The project implements a "static-first" architecture where Express serves as the development backend, while a build pipeline compiles templates (EJS), styles (SCSS), and scripts (JavaScript) into optimized static artifacts deployed to the `docs/` directory for GitHub Pages hosting. Built with Node.js 18+, the tech stack includes Bootstrap 5 for UI components, bootstrap-icons and bootstrap-table for enhanced functionality, Jest for testing, and a comprehensive build system (shell scripts) for CSS, JavaScript, and template processing. The architecture separates source files in `src/` from generated output, enforcing a clean build pipeline and preventing manual edits to production artifacts. What distinguishes this project is its explicit focus on developer experience—fast local development with modern tooling—combined with zero-cost static hosting, making it ideal for documentation sites, portfolio projects, and educational Bootstrap applications. The repository is actively maintained with clear documentation pathways for learners new to Bootstrap or JavaScript, positioning it as both a functional starter template and a learning resource for full-stack JavaScript development patterns.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 30 total (30 current, 0 outdated)

**Created**: 2022-06-06
**Last Modified**: 2026-04-06

---

### #9. [mark-hazleton-s-notes](https://github.com/markhazleton/mark-hazleton-s-notes)

Stars: 1 | Forks: 0 | Language: TypeScript | 154 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 300454 KB | 🚀 51.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Mark Hazleton's Notes

This repository is a full-featured personal website and portfolio platform for a Technical Solutions Architect, built with modern web technologies and optimized for content delivery, SEO, and live data integration. The site combines long-form blog content on cloud architecture and engineering practices, a project portfolio, dynamic GitHub repository metrics, and video galleries—all statically prerendered and deployed to Azure Static Web Apps. The tech stack leverages React 19 with Vite 7 for SSR and static prerendering, TypeScript for type safety, Tailwind CSS with shadcn/ui and Radix UI for component design, and React Markdown for content rendering, complemented by a sophisticated build pipeline that generates SEO assets (sitemaps, RSS feeds with Media RSS extensions, robots.txt) and optimizes images into WebP variants for performance.

The architecture employs a content-as-code approach with Markdown blog posts and JSON metadata files, coupled with a multi-stage build process that generates article indexes, downloads live repository data, optimizes media, and prerenders all routes to static HTML—enabling both dynamic client-side interactivity and instant server delivery without runtime dependencies. Key distinguishing features include live GitHub repository metrics fetched at build time from an external spark data feed, automated image optimization for RSS feeds (400x300px, <50KB), build-time YouTube metadata integration with video sitemaps, and comprehensive SEO infrastructure (canonical URLs, Open Graph, Twitter cards, dynamic RSS). The project demonstrates sophisticated patterns for hybrid static/dynamic content delivery, effective use of build-time data fetching and prerendering at scale, and clean separation between developer documentation (in `.documentation/`) and published site content, making it a reference implementation for content-heavy professional portfolios with integrated tooling and automation.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 62 total (62 current, 0 outdated)

**Created**: 2026-01-10
**Last Modified**: 2026-04-11

---

### #10. [RequestSpark](https://github.com/markhazleton/RequestSpark)

Stars: 2 | Forks: 1 | Language: C# | 46 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 947 KB | 🚀 15.3 commits/month

**Quality**: ❌ License | ✅ Docs

# RequestSpark - Technical Summary

RequestSpark is a comprehensive .NET 10 (LTS) application for executing, analyzing, and benchmarking REST APIs through Postman collection integration and automated testing workflows. The solution provides dual interfaces—a console application and a Razor Pages web UI—enabling users to import Postman collections, run regression tests, perform load testing, and generate detailed performance reports with statistical analysis (percentiles, success rates, response time comparisons). The architecture is modular, consisting of core domain logic (RequestSpark.Domain), a dedicated Postman import service (RequestSpark.PostmanImport), console and web presentation layers, and comprehensive test suites (Domain.Tests, Web.Tests), all built on modern C# with MSTest v4 quality analyzers and zero known vulnerabilities. The project distinguishes itself through significant performance optimizations (19% faster builds, 25% faster test execution on .NET 10), high test coverage (21/21 passing tests), and production-ready features like CSV export, built-in sample CRUD APIs for demonstration, and configurable load testing parameters. RequestSpark targets quality assurance teams, API developers, and DevOps engineers who need robust, open-source tooling for API validation, performance benchmarking, and regression testing without proprietary dependencies, while maintaining an accelerating development pace (46 commits in 90 days) and clear governance documented in repository constitution guidelines.

**Created**: 2021-09-30
**Last Modified**: 2026-03-31

---

### #11. [SupportSpark](https://github.com/markhazleton/SupportSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 43 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 1332 KB | 🚀 14.3 commits/month

**Quality**: ❌ License | ❌ Docs

# SupportSpark - Technical Summary

**SupportSpark** is a TypeScript-based support network platform designed to help individuals share life journey updates with their trusted circle during challenging times. The application provides a role-based system where members create and post updates while supporters receive invitations to view updates and engage through threaded conversations, solving the problem of repetitive communication during difficult life events.

The platform features a modern, full-stack architecture built on **React 19 + Vite** for the frontend with **Express 5** powering the backend, utilizing **TypeScript** with strict type checking throughout for end-to-end safety. The UI layer leverages **shadcn/ui** and Radix primitives for accessible, customizable components styled with **Tailwind CSS 4**, while state management uses **TanStack React Query** for efficient server-state caching and **Zod** for runtime validation. Authentication is handled through Passport.js with session-based security, and the application includes lightweight client-side routing via Wouter with Framer Motion animations for smooth user interactions.

The project is highly active (43 commits in 90 days with accelerating activity patterns) and uniquely targets **Windows 11 + IIS deployment** through an automated PowerShell script, building CommonJS output for iisnode compatibility rather than typical Docker/cloud deployments. A distinctive feature is its **GitHub Pages preview mode** that runs entirely client-side with localStorage persistence, allowing users to explore functionality without a backend server. The codebase demonstrates strong architectural patterns including shared schema validation across client and server, comprehensive documentation in a constitution-based governance model, and a calming teal/sage design system specifically tailored for sensitive emotional contexts. SupportSpark serves individuals navigating health challenges, life transitions, and personal journeys who need a distraction-free, invitation-only space to keep their support networks informed.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 98 total (98 current, 0 outdated)

**Created**: 2026-02-01
**Last Modified**: 2026-03-29

---

### #12. [ReactSparkPortfolio](https://github.com/markhazleton/ReactSparkPortfolio)

Stars: 0 | Forks: 0 | Language: CSS | 29 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 46450 KB | 🚀 9.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: ReactSparkPortfolio

**ReactSparkPortfolio** is a production-ready, enterprise-grade developer portfolio application built with React 19, TypeScript, and Vite that serves as both a personal showcase and a comprehensive reference implementation for modern web development practices. The application demonstrates full-stack capabilities including real-time communication via SignalR, weather integration with interactive mapping, RSS feed aggregation, and a searchable project portfolio, all deployed across Azure Static Web Apps and GitHub Pages with automated CI/CD pipelines. The tech stack leverages contemporary frontend tools (React Router, Bootstrap 5, SCSS, Axios) combined with cloud-native Azure services, implementing a decoupled architecture that separates the React frontend from serverless API endpoints while maintaining strict TypeScript type safety and WCAG 2.1 AA accessibility compliance. Key architectural features include lazy-loaded components for performance optimization, Context API-based state management, a permissive Content Security Policy to support dynamic external content sources, and dark/light theme switching with persistent user preferences. The codebase is notably distinguished by its comprehensive documentation structure, explicit security considerations (documented in CSP_README.md), responsive mobile-first design, and accelerating development velocity (29 commits in 90 days, 106 in 365 days), making it ideal for developers seeking a modern portfolio template, enterprise-grade architectural patterns, or a reference for serverless full-stack React applications.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 46 total (46 current, 0 outdated)

**Created**: 2024-10-11
**Last Modified**: 2026-04-06

---

### #13. [InquirySpark](https://github.com/markhazleton/InquirySpark)

Stars: 0 | Forks: 0 | Language: C# | 23 commits (90d)

👥 0 contributors | 🌐 8 languages | 💾 12011 KB | 🚀 7.7 commits/month

**Quality**: ❌ License | ✅ Docs

# InquirySpark - Technical Summary

**InquirySpark** is a .NET 10-based survey and inquiry management system designed with a read-only SQLite persistence model, featuring an MVC admin interface built with Bootstrap 5 and DataTables. The solution comprises four primary projects: an admin web application with an automated npm build pipeline, an Entity Framework Core 10 repository layer providing abstraction over SQLite operations, shared domain models and SDK objects, and a comprehensive MSTest unit test suite—all enforced with nullable reference types and XML documentation standards. The architecture emphasizes immutability and data integrity by operating SQLite databases exclusively in read-only mode (via connection string Mode=ReadOnly), eliminating the need for SQL Server and schema migrations while leveraging two pre-built databases (ControlSparkUser.db for ASP.NET Core Identity and InquirySpark.db for domain data) stored as versioned assets. Key technical features include centralized persistence configuration via SqliteOptionsConfigurator, primary constructor dependency injection patterns, and a CDN-free Bootstrap/DataTables implementation with Bootswatch theme switching, making it ideal for organizations requiring lightweight, self-contained survey solutions with audit-safe, immutable data stores. The project demonstrates active development with consistent commits and comprehensive documentation, targeting developers building survey platforms or inquiry systems on .NET with minimal external infrastructure dependencies.

**Created**: 2023-10-24
**Last Modified**: 2026-04-11

---

### #14. [Texecon](https://github.com/markhazleton/Texecon)

Stars: 0 | Forks: 0 | Language: HTML | 26 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 3325 KB | 🚀 8.7 commits/month

**Quality**: ❌ License | ❌ Docs

# TexEcon - Technical Summary

**TexEcon** is a modern static site generator for Texas economic analysis built as a React 19 application optimized for GitHub Pages deployment. The project implements a sophisticated build-time content management system that fetches fresh economic analysis and data from a WebSpark headless CMS API during compilation, with graceful fallback to cached content, ensuring both freshness and reliability. The architecture leverages Vite 7.1 for fast builds, TypeScript for type safety, and Tailwind CSS with Radix UI/shadcn/ui components to create an accessible, performant interface—notably employing static HTML generation for dynamic routes to achieve excellent SEO and Core Web Vitals scores despite being client-side routed with Wouter. Key technical differentiators include an intelligent build pipeline with content processing, automated sitemap generation, cache busting via build IDs, and progressive enhancement patterns that enable both static HTML fallbacks and interactive client-side experiences. The project demonstrates enterprise-grade practices for static site generation through its modular script architecture, environment-based configuration, and detailed build reporting for content integration workflows. This approach is particularly suited for content-rich websites requiring frequent updates (economic data, analysis) while maintaining the performance and SEO benefits of static hosting, making it ideal for organizations combining dynamic content management with CDN-friendly deployment strategies.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 37 total (37 current, 0 outdated)

**Created**: 2025-09-03
**Last Modified**: 2026-03-30

---

### #15. [markhazleton](https://github.com/markhazleton/markhazleton)

Stars: 0 | Forks: 0 | Language: Unknown | 20 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 6610 KB | 🚀 6.7 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: markhazleton Repository

This repository serves as a **personal portfolio and learning archive** that showcases Mark Hazleton's continuous skill development across multiple technologies and domains, functioning primarily as a hub linking to featured projects and technical content rather than containing a single codebase. The portfolio highlights two major projects: **DevSpark**, an agent-agnostic AI-powered development framework forked from GitHub SpecKit designed for brownfield/ongoing development with monorepo support and multi-user collaboration, and **ReactSpark**, a modern React application built with Vite and deployed on Azure Static Web Applications. The technical stack spans multiple domains including .NET/C# (evidenced by NuGet package case studies), React/TypeScript (frontend), Azure cloud services, and AI/ML integration frameworks, reflecting a polyglot development approach focused on practical, production-ready implementations. The repository demonstrates architectural expertise in monorepo governance, multi-agent AI collaboration patterns, and API testing infrastructure (RESTRunner), with emphasis on brownfield development scenarios and DevOps practices. DevSpark itself represents a significant fork evolution that transformed a template-based framework into a sophisticated tool for managing complex development workflows with agent abstraction, making it particularly valuable for teams working on multiple interconnected projects. The project targets full-stack developers, technical leads, and organizations seeking frameworks for AI-assisted development and brownfield modernization, supported by extensive technical documentation and case studies published through the accompanying blog.

**Created**: 2021-04-17
**Last Modified**: 2026-04-12

---

### #16. [WebSpark](https://github.com/markhazleton/WebSpark)

Stars: 1 | Forks: 0 | Language: C# | 12 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 69144 KB | 🚀 4.0 commits/month

**Quality**: ❌ License | ❌ Docs

# WebSpark Technical Summary

WebSpark is a modular .NET 9 web application suite comprising three primary tools—PromptSpark (LLM prompt optimization), RecipeSpark (recipe management), and TriviaSpark (quiz creation)—built with ASP.NET Core MVC, Bootstrap 5, and organized across seven scalable architectural areas. The project emphasizes production-grade quality through comprehensive SEO optimization capabilities including dynamic meta tags, JSON-LD schema markup, XML sitemaps, Google Analytics 4 integration, and Core Web Vitals monitoring, supported by extensive test coverage (47 passing SEO tests). A distinctive feature is its spec-driven development workflow powered by SpecKit commands (`/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.critic`, `/speckit.implement`, `/speckit.review`) that enforce rigorous specifications, implementation planning, and adversarial risk assessment before code execution, specifically designed to catch ASP.NET Core anti-patterns, security vulnerabilities, performance issues, and operational blindspots. The architecture balances flexibility through modular component design with governance through branch protection rules, branch naming conventions, and a documented constitution of architectural principles. While early-stage (1 star, created January 2024), the project demonstrates sophisticated engineering discipline targeting developers and organizations seeking to build scalable, SEO-aware web applications with built-in risk mitigation and quality gates throughout the development lifecycle.

**Created**: 2024-01-11
**Last Modified**: 2026-01-29

---

### #17. [WebProjectMechanics](https://github.com/markhazleton/WebProjectMechanics)

Stars: 3 | Forks: 0 | Language: Visual Basic .NET | 9 commits (90d)

👥 0 contributors | 🌐 10 languages | 💾 52407 KB | 🚀 3.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebProjectMechanics

**WebProjectMechanics** is a greenfield rebuild of a 20+ year legacy multi-tenant content management system, designed to serve 36+ domains from a single application instance while maintaining cost efficiency (~$10/month on Azure Linux). The system uses a plugin-based architecture with isolated SQLite databases per tenant and a publish-to-static model that pre-renders all public content as HTML served by Caddy, eliminating database queries for end users and maximizing performance and availability.

The project is built on modern .NET 9 with ASP.NET Core Minimal APIs and Entity Framework Core, featuring a clean modular structure with domain-specific plugins (CMS, Mineral Collection, Recipes) and a shared infrastructure layer. Architecture patterns include physical data isolation (per-site SQLite files rather than multi-tenant columns), a clear separation between API and static content delivery, and infrastructure-as-code deployment using Caddy for reverse proxying and automatic SSL termination on Linux.

What distinguishes this project is its pragmatic approach to supporting legacy complexity: it documents the complete legacy system specification while systematically migrating to cloud-native patterns, combines multiple language support (VB.NET, C#, JavaScript, XSLT, ASP.NET), and demonstrates cost-conscious hosting decisions suitable for small-to-medium multi-tenant SaaS platforms. The target audience includes web hosting providers, content publishers, and organizations managing multiple domain properties, while the implementation plan and comprehensive documentation make it valuable as a reference architecture for legacy system modernization projects.

**Created**: 2017-09-19
**Last Modified**: 2026-02-19

---

### #18. [PromptSpark.Chat](https://github.com/markhazleton/PromptSpark.Chat)

Stars: 0 | Forks: 0 | Language: C# | 29 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 19307 KB | 🚀 9.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: PromptSpark.Chat

**PromptSpark.Chat** is a real-time conversational workflow application built on ASP.NET Core that enables users to navigate multi-step processes through an interactive chat interface enhanced with Adaptive Cards. The application leverages **SignalR** for bidirectional real-time communication, a **ConcurrentDictionary-based** in-memory state store for thread-safe conversation persistence, and optional AI integration via chat completion services to handle dynamic questions beyond predefined workflows. The frontend is composed of HTML, SCSS, JavaScript, and CSS (29.9%-31.4% of the codebase), while the C# backend (31.4%) implements MVC controllers, workflow engines, and service layers that support branching logic through JSON-defined node structures. The architecture emphasizes simplicity and minimal overhead by combining straightforward workflow definitions (JSON-based node graphs) with server-side session management, allowing users to refresh without losing progress while supporting scalability through Azure SignalR Service for high-concurrency deployments. This project is particularly valuable for organizations seeking to build guided user experiences, customer onboarding flows, support chatbots, or interactive surveys with both deterministic branching paths and fallback AI responses, making it applicable across fintech, healthcare, SaaS, and enterprise automation domains.

**Created**: 2024-12-31
**Last Modified**: 2026-03-30

---

### #19. [react-native-web-start](https://github.com/markhazleton/react-native-web-start)

Stars: 0 | Forks: 0 | Language: PowerShell | 23 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2770 KB | 🚀 7.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: react-native-web-start

## Overview
**react-native-web-start** is a production-ready, enterprise-grade starter template designed to enable cross-platform application development using React Native, React Native Web, Vite, and TypeScript. The project provides a comprehensive foundation for building applications that run seamlessly on web, iOS, and Android platforms from a single codebase, with the primary entry point being a PowerShell-based build and deployment automation system.

## Key Features & Capabilities
The repository delivers a modern development experience through several core capabilities: true cross-platform code sharing via a monorepo structure (shared, web, and mobile packages), lightning-fast development with Vite's HMR capabilities, full TypeScript strict mode support, and production-ready features including API integration, responsive Tailwind CSS styling with Sass preprocessing, and an in-app markdown documentation browser. It includes comprehensive build automation scripts for asset management, documentation synchronization, and GitHub Pages deployment with CI/CD integration, along with testing infrastructure through Jest configuration and code quality tools (ESLint, Prettier).

## Technology Stack
The stack combines React 19.2.5 and React Native 0.85.0 for component development, Vite 8.0.8 as the primary build tool for web, Metro for React Native bundling, TypeScript 6.0.2 for type safety, Tailwind CSS 4.2.2 with Sass 1.99.0 for styling, and the Marked library for markdown processing. The architecture leverages native Fetch API for HTTP communication and includes 50 total dependencies carefully curated for production stability.

## Architectural Approach
The project employs a well-organized monorepo structure with clear separation of concerns: a shared package containing reusable components and business logic, separate web and mobile configuration packages, and centralized asset management. The build pipeline includes sophisticated automation (build.js, copy-assets.js, copy-docs.js, generate-build-info.js) demonstrating infrastructure-as-code practices, and the inclusion of comprehensive documentation alongside the codebase suggests a documentation-first development philosophy.

## Unique Strengths
What distinguishes this template is its comprehensive approach to solving the cross-platform development challenge with modern tooling—combining the performance benefits of Vite with React Native's code reusability, eliminating the need for `--legacy-peer-deps` through validated dependency management, and providing GitHub Pages integration with automated deployment. The inclusion of in-app documentation browsing and bundle analysis capabilities reflects a developer experience focus that goes beyond basic scaffolding.

## Target Audience & Use Cases
This template is ideal for teams and individual developers seeking to build and maintain cross-platform applications with minimal codebase duplication, particularly those targeting web-first distribution with native mobile extensions. It serves startups and enterprises needing rapid development cycles with type safety, CI/CD integration, and production-ready infrastructure without building these systems from scratch.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 50 total (50 current, 0 outdated)

**Created**: 2025-07-26
**Last Modified**: 2026-04-12

---

### #20. [KeyPressCounter](https://github.com/markhazleton/KeyPressCounter)

Stars: 2 | Forks: 1 | Language: C# | 6 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 46596 KB | 🚀 2.0 commits/month

**Quality**: ❌ License | ✅ Docs

# KeyPressCounter - Technical Summary

**KeyPressCounter** is a lightweight Windows system tray utility written in C# (.NET 10.0) that monitors keyboard and mouse input activity alongside real-time system performance metrics without recording keystroke content or transmitting data. The application provides comprehensive activity tracking through features including keystroke/click counting, peak activity metrics, inactivity detection, real-time CPU/memory monitoring with 60-second rolling graphs, process monitoring, and configurable activity logging with daily summaries. The architecture leverages SharpHook for global input event hooking, Windows Performance Counters and WMI (via System.Management) for hardware/performance data, and P/Invoke wrappers for idle detection, while implementing thread-safe counters with interval-based peak tracking and a three-tab WinForms dashboard interface. The project demonstrates solid Windows desktop development practices including single-instance enforcement, registry-based startup registration, JSON-based configuration persistence, and proper resource management through IDisposable patterns, making it suitable for users seeking transparent activity monitoring and system performance insights. With 46 MB in size, 20 commits over a year, and maintained status, this is a mature utility targeting system administrators, productivity analysts, or users needing to understand their input patterns and system resource consumption in real-time.

**Technology Stack Currency**: ✅ 57/100
**Dependencies**: 4 total (3 current, 1 outdated)

**Created**: 2024-03-07
**Last Modified**: 2026-03-30

---

### #21. [markhazleton.github.io](https://github.com/markhazleton/markhazleton.github.io)

Stars: 0 | Forks: 0 | Language: SCSS | 8 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 161 KB | 🚀 2.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: markhazleton.github.io

This repository is a personal portfolio and blog website built with Jekyll and hosted on GitHub Pages, serving as Mark Hazleton's professional web presence. The site is built on a customized Minima theme with a modern tech stack including Ruby 3.2.2, Jekyll 3.10.0, and a carefully balanced mix of SCSS (39.4%), HTML (30.1%), and CSS (29.8%), providing responsive styling without external framework dependencies. Key features include automated dark/light mode toggling, emoji support, optimized SEO capabilities with excerpt-based meta descriptions, and a structured content management system with dedicated directories for blog posts, drafts, and reusable template components. The project employs a GitHub Actions CI/CD workflow that automatically builds and deploys the site to GitHub Pages whenever commits are pushed to the sources branch, ensuring seamless content publication. Notable architectural decisions include the use of custom layouts and includes for component reusability, front matter standardization for metadata management, and support for both direct publishing and feature branch workflows for content creation. This setup makes it an ideal template for developers and technical professionals seeking to maintain a personal blog and portfolio site with minimal overhead, leveraging GitHub's free hosting and Jekyll's static site generation capabilities while maintaining full version control and automated deployment.

**Technology Stack Currency**: ✅ 56/100
**Dependencies**: 3 total (2 current, 1 outdated)

**Created**: 2021-04-18
**Last Modified**: 2026-04-01

---

### #22. [DataSpark](https://github.com/markhazleton/DataSpark)

Stars: 0 | Forks: 0 | Language: HTML | 19 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 2075 KB | 🚀 6.3 commits/month

**Quality**: ❌ License | ✅ Docs

# DataSpark Technical Summary

DataSpark is a comprehensive .NET 10 toolkit designed for SQLite database analysis and code generation, offering both command-line and web-based interfaces for developers and data analysts. The project provides core functionality for discovering SQLite files, exporting tables to CSV, generating schema reports in multiple formats (text, JSON, Markdown), and automatically generating C# Data Transfer Objects (DTOs) from database schemas. Built with a modular architecture, it consists of a reusable core library (DataSpark.Core) shared between a CLI application (DataSpark.Console) and an ASP.NET Core MVC web UI (DataSpark.Web), complemented by comprehensive MSTest unit tests and BenchmarkDotNet performance benchmarks. The web interface adds user-friendly functionality including file upload capabilities, interactive table analysis, CSV export workflows, and persistent file management, while the CLI caters to automation and scripting scenarios. The project demonstrates solid engineering practices with continuous integration via GitHub Actions, code coverage tracking, semantic versioning support for .NET 10, and clear separation of concerns across projects. This toolkit targets developers who need to quickly integrate legacy SQLite databases into modern .NET applications or require batch processing capabilities for database schema extraction and data export tasks.

**Created**: 2017-11-06
**Last Modified**: 2026-04-01

---

### #23. [PHPDocSpark](https://github.com/markhazleton/PHPDocSpark)

Stars: 0 | Forks: 0 | Language: PHP | 6 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 2935 KB | 🚀 2.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: PHPDocSpark

**PHPDocSpark** is an open-source PHP documentation and data exploration platform that demonstrates modern hybrid web development by combining PHP 8.2+ server-side logic with a contemporary Vite-based asset pipeline. The application serves as both a functional tool and comprehensive reference implementation, showcasing best practices for building documentation management systems, interactive data analysis tools, and responsive web interfaces. It integrates markdown-based content management with full-text search, SQLite database operations, interactive DataTables and Chart.js visualizations, GitHub API integration, and external service consumption—all wrapped in a Bootstrap 5.3 responsive UI with SCSS styling and JavaScript interactivity.

The architecture employs a hybrid pattern using a PHP front controller routing system that combines traditional server-side templating with modern client-side asset optimization, featuring automated build processes via Vite that handle minification, source maps, and hot module replacement during development. Technically, it leverages PHP with Parsedown for markdown parsing, SQLite for zero-configuration data persistence, jQuery for DOM manipulation, and a comprehensive npm-based toolchain including ESLint for code quality and Azure Pipelines for CI/CD automation. The project's unique value lies in its educational focus as a reference implementation for full-stack PHP developers, offering tangible patterns for content indexing, API caching strategies, responsive design, data profiling, and DevOps workflows rather than solving a single specialized problem.

Targeted toward PHP developers modernizing their workflows, full-stack engineers exploring hybrid architectures, technical teams building internal tools, and students learning contemporary web development practices, PHPDocSpark is maintained with current activity (6 commits in 90 days, accelerating patterns) and deployed on Azure Web Apps, positioned as part of the broader WebSpark professional portfolio suite at markhazleton.com.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2023-09-08
**Last Modified**: 2026-03-30

---

### #24. [FastEndpointApi](https://github.com/markhazleton/FastEndpointApi)

Stars: 2 | Forks: 1 | Language: HTML | 1 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 137 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: FastEndpointApi Repository

This repository is a comprehensive educational demo and reference implementation of the **FastEndpoints framework**, a lightweight REST API framework for ASP.NET Core that implements the REPR (Request-Endpoint-Response) pattern. The project showcases a complete Person Management API built with .NET 10.0 and FastEndpoints 7.1.1, demonstrating modern API development practices including CRUD operations, dependency injection, smart data mapping, HATEOAS implementation, and OpenAPI/Swagger integration for interactive documentation.

The technology stack combines FastEndpoints as the core framework with complementary tools including FastEndpoints.Swagger for API documentation, Bogus for test data generation, and Bootstrap 5.3.3 for the frontend UI, while leveraging GitHub Actions for CI/CD automation and Azure Web Apps for cloud deployment. The codebase is structured around clean architectural principles with clear separation of concerns, featuring service layers, reusable base endpoint classes, and request/response DTOs that minimize boilerplate code while maintaining high performance and maintainability.

This project serves as both a working demo application (live on Azure) and an educational resource for developers looking to adopt FastEndpoints as an alternative to Minimal APIs or MVC controllers, providing hands-on examples of how to build scalable, well-documented REST APIs with reduced complexity. The repository includes static HTML pages for interactive testing, comprehensive documentation with a detailed article walkthrough, and a fully functional API with endpoints accessible through both Swagger UI and custom web interfaces, making it ideal for developers seeking practical patterns and best practices in modern ASP.NET Core API development.

**Created**: 2024-04-06
**Last Modified**: 2026-03-30

---

### #25. [TeachSpark](https://github.com/markhazleton/TeachSpark)

Stars: 0 | Forks: 0 | Language: C# | 13 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 29808 KB | 🚀 4.3 commits/month

**Quality**: ❌ License | ✅ Docs

# TeachSpark - Technical Summary

**TeachSpark** is a modern, LLM-powered educational platform built on .NET 10 MVC that delivers personalized, adaptive learning experiences through intelligent content delivery and real-time feedback mechanisms. The application combines a robust C# backend leveraging Clean Architecture principles with Entity Framework Core for data persistence, alongside a sophisticated frontend built with Webpack 5, ES6+ JavaScript, and SCSS—enabling responsive, high-performance user interfaces with features like hot module replacement and code splitting. Key capabilities include AI-driven learning path personalization, comprehensive progress analytics, interactive curriculum content, and a modern responsive design, all underpinned by a well-engineered build system featuring automated asset optimization, bundle analysis, and integrated code quality tooling (ESLint, Prettier, Stylelint) enforced via Husky git hooks. The project demonstrates production-grade development practices with clean separation of concerns between frontend and backend, standardized tooling configurations (including webpack bundle analyzer), and a structured approach to maintaining code quality through pre-commit automation and staged linting. The active development status (13 commits in 90 days, accelerating activity pattern) and high tech stack currency score (90/100) indicate a well-maintained, contemporary codebase targeting educators and learners seeking intelligent, adaptive educational solutions that leverage large language model capabilities to enhance pedagogical outcomes.

**Technology Stack Currency**: ✅ 90/100
**Dependencies**: 3 total (2 current, 1 outdated)

**Created**: 2025-06-19
**Last Modified**: 2026-03-29

---

### #26. [AsyncSpark](https://github.com/markhazleton/AsyncSpark)

Stars: 0 | Forks: 0 | Language: C# | 9 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 1925 KB | 🚀 3.0 commits/month

**Quality**: ❌ License | ✅ Docs

# AsyncSpark: Technical Summary

**AsyncSpark** is a production-ready reference implementation demonstrating enterprise-grade asynchronous programming patterns in .NET 10, built on a novel "constitution-driven development" methodology that formalizes coding standards and enforces them through automated compliance auditing. The project serves as both an educational resource and a working example of modern async/await best practices, featuring 80% mandatory code coverage enforcement, comprehensive resilience patterns via Polly integration, and clean architecture principles including dependency injection and decorator-based cross-cutting concerns. The technology stack leverages ASP.NET Core with interactive Scalar-powered API documentation, MSTest + Moq for unit testing, and structured logging, while demonstrating eight core async patterns: ConfigureAwait(false) usage in libraries, CancellationToken threading, Task.WhenAll parallelization, SemaphoreSlim throttling, fire-and-forget safety, and avoidance of blocking calls—each with corresponding test coverage and interactive API endpoints for experimentation. What distinguishes AsyncSpark is its formalized constitution (.NET 10 standards, async best practices, 80% test coverage, interface-based architecture, and resilience requirements) coupled with automated enforcement mechanisms including CI/CD validation, GitHub Actions-based audits, and SpecKit-powered compliance reporting that monitors adherence across the codebase. The project targets .NET developers seeking enterprise patterns, architects designing async-heavy systems, and teams adopting constitution-driven development workflows, offering both a live Azure-hosted demo and comprehensive documentation guiding learners through complex concurrency scenarios via working code examples and API integration tests.

**Created**: 2022-08-07
**Last Modified**: 2026-02-10

---

### #27. [WebSpark.ArtSpark](https://github.com/markhazleton/WebSpark.ArtSpark)

Stars: 0 | Forks: 0 | Language: C# | 1 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3658 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# WebSpark.ArtSpark - Technical Summary

## Overview

WebSpark.ArtSpark is a comprehensive .NET solution that provides complete programmatic access to the Art Institute of Chicago's public REST API, complemented by an innovative AI chat system featuring multiple conversational personas. The repository contains four interconnected projects: a full-featured API client library covering all 33 endpoints, an AI agent system powered by OpenAI's GPT-4o with vision capabilities, an interactive ASP.NET Core web demo application with user authentication and collection management, and a command-line utility for developers. This solution demonstrates modern .NET 10.0 best practices including async/await patterns, strongly-typed models with System.Text.Json deserialization, IIIF image URL construction for high-quality artwork display, and flexible querying with pagination and field selection.

## Key Technical Features

The platform excels through its **revolutionary AI chat system** that brings artworks to life by implementing multiple personas (Artwork, Artist, Curator, Historian) with persistent conversation memory, content filtering guardrails, and AI-powered visual analysis. The architecture employs **externalized prompt management** with hot-reload capabilities in development mode, allowing real-time AI behavior customization without code changes. The demo application showcases enterprise-grade features including ASP.NET Core Identity-based user authentication with SQLite persistence, personal artwork collections, responsive Bootstrap 5 UI with 26+ Bootswatch themes, SEO-optimized slug-based routing, and dynamic random collection showcasing on the homepage. The client library maintains a minimal dependency footprint while providing comprehensive API coverage across six major categories (Collections, Shop, Mobile, Digital Scholarly Catalogs, Static Archive, and Aggregations) with proper HTTP status handling and error management.

## Notable Architecture & Status

The solution demonstrates solid software engineering principles through clean separation of concerns, dependency injection patterns, and configuration management via appsettings.json with user-secrets support for sensitive credentials. However, the project shows **declining activity** with only 1 commit in the past 90 days against 57 total commits in the past year, suggesting maintenance rather than active development, though it remains functionally complete and well-documented. The repository is particularly well-suited for educational purposes, museum/cultural institution digital initiatives, and developers seeking to understand modern .NET client library design, AI integration patterns, and responsive web application development in ASP.NET Core.

**Created**: 2023-01-30
**Last Modified**: 2026-01-12

---

### #28. [MechanicsOfMotherhood](https://github.com/markhazleton/MechanicsOfMotherhood)

Stars: 0 | Forks: 0 | Language: TypeScript | 14 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 6719 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Mechanics of Motherhood

**Mechanics of Motherhood** is a modern, production-ready recipe management web application specifically designed for busy working mothers, featuring 108+ curated recipes with smart search, filtering, and categorization capabilities. Built with React 19 and TypeScript, the application implements a sophisticated frontend architecture leveraging Vite for optimized builds, TanStack Query for server state management, Tailwind CSS with Shadcn/ui component library for industrial-themed UI design, and Wouter for lightweight client-side routing. The platform integrates with real-world APIs (RecipeSpark and WebCMS) for live recipe and content data while maintaining offline PWA capabilities through intelligent caching strategies, achieving Lighthouse scores above 95 and bundle sizes around 130KB gzipped. The project demonstrates strong software engineering practices with automated CI/CD pipelines via GitHub Actions, data quality validation systems, comprehensive SEO optimization including structured data and dynamic sitemaps, and a mobile-first responsive design optimized for 3G networks across all device types. This repository showcases contemporary full-stack development patterns including TypeScript for type safety, automated deployment workflows, real-time API integration with graceful fallbacks, and performance-first optimization—making it exemplary of professional production-grade web application development while addressing the specific niche of recipe management for time-constrained users.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 42 total (42 current, 0 outdated)

**Created**: 2025-09-01
**Last Modified**: 2026-03-09

---

### #29. [WebSpark.Bootswatch](https://github.com/markhazleton/WebSpark.Bootswatch)

Stars: 0 | Forks: 0 | Language: HTML | 5 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7124 KB | 🚀 1.7 commits/month

**Quality**: ❌ License | ✅ Docs

# WebSpark.Bootswatch - Technical Summary

**WebSpark.Bootswatch** is a .NET Razor Class Library that provides seamless integration of Bootswatch themes into ASP.NET Core applications, built on Bootstrap 5 to enable modern, responsive UI theming with dynamic switching and light/dark mode support. The library is architected as a production-ready component leveraging .NET 10 exclusively (version 2.0+), implementing caching mechanisms through the `StyleCache` service and providing Tag Helper support for simplified UI integration. Key technologies include C# (28.6%), HTML (63.8%), and JavaScript (2.6%), with dependencies on `WebSpark.HttpClientUtility` for HTTP operations and modern `Microsoft.Extensions.*` packages version 10.0.1+. The library employs a service-oriented pattern with extension methods for dependency injection, comprehensive error handling, fallback mechanisms, and full IntelliSense/XML documentation support for developer experience. Unique to this project is its strategic decision to target only .NET 10, prioritizing access to latest security patches and modern dependencies over broad framework compatibility, with a clear migration path provided for users on .NET 8/9 through version 1.34.0. This library targets ASP.NET Core developers building enterprise applications who require flexible, maintainable theming solutions with built-in performance optimization and the ability to dynamically switch between multiple professional Bootswatch themes without page reloads.

**Created**: 2022-08-24
**Last Modified**: 2026-01-12

---

### #30. [DocSpecSpark](https://github.com/markhazleton/DocSpecSpark)

Stars: 0 | Forks: 0 | Language: Python | 6 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 210 KB | 🚀 2.0 commits/month

**Quality**: ❌ License | ✅ Docs

# DocSpecSpark Technical Summary

DocSpark is an AI-assisted documentation system framework that provides a structured workflow for creating, reviewing, and publishing markdown-based documentation through repeatable prompt templates and lightweight CLI tooling. The core product consists of 21 document workflow prompts, helper templates, and context-gathering scripts (PowerShell/Bash) designed to guide AI assistants through a complete documentation lifecycle, with an optional Python CLI built using Typer and Rich for automated bootstrap installation into target repositories. The project implements a sophisticated separation-of-concerns architecture distinguishing between framework-managed assets (`.docspark/`) and user-owned artifacts (`.documentation/`), with intelligent prompt/script resolution cascading through git-user-specific, project-level, and default locations to enable personalization and upgrades. DocSpark features 21+ slash commands spanning core workflows (`/specify`, `/plan`, `/implement`, `/publish`), constitution-powered operations (`/pr-review`, `/site-audit`, `/evolve-constitution`), and quality assurance processes (`/clarify`, `/analyze`, `/checklist`), alongside publication scaffolding for static sites (MkDocs, GitHub Pages). The framework is uniquely positioned as an abstraction layer that decouples AI assistance workflows from specific coding assistants (GitHub Copilot, Claude, Cursor), making documentation generation agent-agnostic while maintaining consistency through markdown-driven prompts rather than code generation. Target users are technical teams and organizations seeking to systematize documentation practices across projects using their preferred AI coding assistants without vendor lock-in.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 2 total (0 current, 2 outdated)

**Created**: 2026-03-07
**Last Modified**: 2026-04-03

---

### #31. [WebSpark.PrismSpark](https://github.com/markhazleton/WebSpark.PrismSpark)

Stars: 0 | Forks: 0 | Language: C# | 14 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 2272 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.PrismSpark

**WebSpark.PrismSpark** is a high-performance C#/.NET port of the popular PrismJS syntax highlighting library, designed to provide server-side code tokenization and HTML rendering for 24 programming languages with advanced theming and extensibility capabilities. The project leverages .NET 10.0 LTS with a modular architecture comprising core highlighting engines (`IHighlighter` interface), grammar-based tokenizers, a robust plugin system, and customizable theme management through `ThemeManager` and `CssGenerator` classes. Key architectural strengths include event-driven hooks for post-processing customization, support for enhanced options (line numbering, line highlighting, custom CSS classes), async processing for performance optimization, and a comprehensive MSTest suite with 52 tests ensuring reliability across grammar parsing, tokenization, and end-to-end integration workflows. The library is particularly well-suited for ASP.NET MVC/Razor applications through dependency injection patterns and includes interactive demo web components featuring a live code editor, real-time validation, and markdown integration via Markdig. What distinguishes this implementation is its .NET-native design combining PrismJS's linguistic flexibility with C# performance characteristics, extensive language support spanning web technologies (HTML, CSS, JavaScript), systems languages (C, C++, Rust, Go), and markup formats (Markdown, YAML, Pug), making it an ideal solution for documentation platforms, code review tools, educational applications, and any .NET-based system requiring server-rendered syntax highlighting without client-side JavaScript dependencies.

**Created**: 2025-05-27
**Last Modified**: 2026-02-11

---

### #32. [TriviaSpark](https://github.com/markhazleton/TriviaSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 27238 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# TriviaSpark - Technical Summary

**TriviaSpark** is a multiplayer trivia game application developed as an experiment in AI-assisted development using Chat GPT, designed to fetch questions from public Trivia APIs and deliver an interactive competitive gaming experience. The project is built primarily with C# backend logic (61.1%) alongside HTML (26.5%) and CSS (12.3%) for frontend presentation, suggesting an ASP.NET web application architecture with potential cross-platform capabilities targeting both web and mobile environments. Key features include user registration and authentication, a leaderboard system for competitive ranking, an admin interface for question database management, and a customizable UI to enhance user engagement—all designed to deliver real-time multiplayer trivia gameplay with an upbeat, modern, and competitive tone. The application leverages RESTful API integration with external trivia data sources, demonstrating separation of concerns between client-side interactivity and server-side business logic, though the minimal commit history (4 commits over 365 days, 0 in the last 90 days) indicates the project is in an exploratory or inactive state. The repository's primary value lies in its documentation of AI-assisted development practices and serves as a case study for building interactive gaming applications, targeting tech-savvy individuals aged 18-95 seeking competitive trivia entertainment. The project's relatively large codebase (27.2 MB) combined with declining activity suggests it represents a proof-of-concept or learning exercise that may have reached completion or been abandoned during development.

**Created**: 2023-02-22
**Last Modified**: 2025-12-02

---

### #33. [DecisionSpark](https://github.com/markhazleton/DecisionSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 519 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# DecisionSpark - Technical Summary

**DecisionSpark** is a .NET 10 web application that implements a sophisticated, configuration-driven decision routing engine designed to guide users through intelligent conversational flows with minimal questioning. The engine combines a RESTful API with an interactive Razor Pages web interface to collect user inputs, evaluate responses against JSON-based rule configurations, and recommend optimal outcomes—making it well-suited for recommendation systems, decision support tools, and guided workflows across domains like technology stack selection, activity planning, and diagnostic flows.

The system features a modular architecture built on several core services: a **DecisionSpecLoader** that manages JSON-based decision specifications without requiring code changes, a **RoutingEvaluator** that applies rule-based logic to determine outcomes, a **TraitParser** for extracting structured data from user responses, and an **OpenAIQuestionGenerator** that leverages OpenAI/Azure OpenAI integration to generate natural language questions dynamically. Session management is handled through a file-based persistence layer, while the API layer provides comprehensive Swagger/OpenAPI documentation for interactive testing and third-party integration.

Key technical differentiators include its **conversation-driven design** with multiple question types (text input, single-select, multi-select), **intelligent rule evaluation** supporting derived traits and tie-breaking mechanisms, and **graceful degradation** with OpenAI fallback capabilities for question generation. The project demonstrates strong engineering practices with Serilog structured logging (console and rolling file outputs), API key authentication via custom headers, and a clean separation of concerns across service layers.

However, the repository shows **minimal activity** with zero commits in the last 90 days and only 18 commits over the past year, suggesting this is either an early-stage project, a proof-of-concept, or potentially abandoned. With zero stars, forks, and contributors, it lacks community engagement, and the declining activity pattern indicates the project may not be actively maintained—making it suitable primarily for educational purposes, internal organizational use, or as a foundation for custom development rather than relying on ongoing support.

**Created**: 2025-10-29
**Last Modified**: 2025-12-27

---


---

## Report Metadata

- **Generation Time**: 5.8 seconds
- **SVGs Generated**: 6/6
- **Total API Calls**: 0
- **Total AI Tokens**: 79,975
- **Success Rate**: 100.0%

### Data Sources

- GitHub API (public repositories only)
- Anthropic Claude API (repository summaries)
- Dependency package registries (npm, PyPI, RubyGems, Go, Maven, NuGet)

### Report Details

- **Composite Score Weights**: Popularity 30% • Activity 45% • Health 25%
- **Technology Currency**: Calculated from latest versions in package registries
- **AI Model**: claude-haiku-4-5

---

*Generated by [Stats Spark](https://github.com/markhazleton/github-stats-spark)*
*Last updated: 2026-04-12*