# GitHub Profile: markhazleton

**Generated**: 2026-04-02 15:47:30 UTC
**Report Version**: 1.0.0
**Repositories Analyzed**: 32
**AI Summary Rate**: 90.6%

> 💡 **Navigation**: [Profile Overview](#profile-overview) | [Top Repositories](#top-32-repositories) | [Metadata](#report-metadata)

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

## Top 32 Repositories

### #1. [WebSpark.HttpClientUtility](https://github.com/markhazleton/WebSpark.HttpClientUtility)

Stars: 0 | Forks: 0 | Language: C# | 75 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2672 KB | 🚀 25.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.HttpClientUtility

## Overview & Purpose

WebSpark.HttpClientUtility is a production-ready .NET library that provides a drop-in HttpClient wrapper designed to eliminate boilerplate HTTP setup code in .NET 8-10 LTS applications. It abstracts away complex infrastructure concerns—resilience patterns, caching, logging, and distributed tracing—into a single `AddHttpClientUtility()` configuration call, enabling developers to implement enterprise-grade HTTP communication with minimal code complexity.

## Core Features & Capabilities

The library integrates **Polly-based resilience patterns** (retry policies and circuit breakers), **in-memory response caching** with configurable TTLs, **automatic correlation ID generation** for distributed request tracing, and **built-in OpenTelemetry instrumentation** for structured observability. It provides an `IHttpRequestResultService` abstraction that handles typed HTTP responses, error management, and request/response metadata tracking. The ecosystem includes two focused NuGet packages: the core utility (163 KB) and an optional Crawler extension (75 KB) for web scraping with robots.txt parsing and sitemap generation capabilities.

## Technology Stack & Architecture

Built entirely in C# with PowerShell build automation, the project targets modern .NET with explicit support for .NET 8, 9, and 10 LTS frameworks. It leverages Microsoft's dependency injection container, ILogger abstractions, and ActivitySource for OpenTelemetry compliance. The design follows the **service-based pattern** with fluent configuration options, enabling both minimal one-line setup and granular control for advanced scenarios. The codebase demonstrates production-grade practices including Source Link support, Native AOT/IL trimming annotations, and zero-warning strict compilation.

## What Makes It Unique

Unlike raw HttpClient (requires 50+ lines of manual setup), Refit (declarative but opinionated), or RestSharp (lower-level abstraction), WebSpark fills the "configured resilience out-of-the-box" niche with zero boilerplate. Its commitment to semantic versioning, backward compatibility within major versions, and comprehensive automated test coverage across .NET versions signals production maturity. The integrated crawler package adds differentiation for teams building data aggregation or web intelligence solutions.

## Target Users & Use Cases

Ideal for microservice architectures requiring distributed tracing, background worker jobs needing resilience without manual Polly configuration, and web scraping applications. Not suited for projects requiring declarative type-safe API clients (use Refit instead), legacy .NET Framework support, or maximum low-level control. The project's 75 commits in 90 days and consistent activity pattern indicate active maintenance and community investment.

**Created**: 2025-05-03
**Last Modified**: 2026-03-31

---

### #2. [github-stats-spark](https://github.com/markhazleton/github-stats-spark)

Stars: 0 | Forks: 0 | Language: Python | 171 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 14902 KB | 🚀 57.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: github-stats-spark

## Project Overview

**Stats Spark** is a comprehensive GitHub analytics and visualization platform that automatically generates SVG-based profile statistics and AI-powered repository analysis reports. The project transforms raw GitHub activity data into actionable insights through intelligent algorithms and beautiful visualizations, designed for developers, teams, and open-source maintainers to showcase and analyze development patterns.

## Core Architecture & Components

The repository employs a **modular, multi-tier architecture**:

1. **Backend Analytics Engine (Python 3.11+)**
   - PyGithub integration for GitHub API access with smart rate-limit handling and exponential backoff
   - PyYAML-based configuration system for flexible, environment-specific settings
   - Multi-algorithm ranking system (30% popularity, 45% activity with time-decay, 25% health metrics)
   - Claude Haiku AI integration for generating technical summaries with 97%+ success rate and three-tier fallback logic

2. **SVG Visualization Generator (Python + svgwrite)**
   - Automated generation of 6 visual categories: overview dashboard, commit heatmap, language statistics, streak tracking, personality-driven fun stats, and release cadence
   - Dynamic Spark Score calculation (0-100 metric: 40% consistency, 35% volume, 25% collaboration)
   - Theme customization (dark/light/custom) with WCAG AA accessibility compliance
   - Weekly automation via GitHub Actions at UTC midnight on Sundays

3. **Interactive Frontend Dashboard (JavaScript/React)**
   - Mobile-first responsive design optimized for 320px-768px viewports with 44x44px touch targets
   - Chart.js + react-chartjs-2 for interactive data visualization
   - IndexedDB caching with Dexie library for 7-day offline access and performance optimization
   - Bottom-sheet navigation patterns, swipe gestures, and drill-down repository details
   - Lighthouse CI configuration targeting <2s First Contentful Paint with 0.9+ performance scores

4. **Reporting System (Markdown Generation)**
   - GitHub-flavored markdown output with embedded visualizations
   - Composite intelligent ranking blending popularity, activity recency, and health signals
   - Attention scoring combining PR backlog, security alerts, staleness, and dependency drift
   - Dependency coverage tracking with version resolution and unknown-gap identification

## Key Technical Features

**Smart Data Processing:**
- Efficient API optimization with caching strategies handling up to 500 repositories in under 5 minutes
- Pattern recognition algorithms for identifying coding time preferences (night owl, early bird, daytime coder)
- Time-decay weighted activity analysis across 90d/180d/365d windows
- Streak calculation and consistency tracking

**Developer Profiling:**
- Technology stack diversity metrics and specialization classification
- Contribution pattern analysis (creator, contributor, maintainer classification)
- Account longevity tracking with experience-based badges
- Observable trend extraction for long-term development focus

**Enterprise Capabilities:**
- YAML-based extensible configuration system
- Local CLI development environment for pre-deployment testing
- Flexible GitHub Pages automated deployment pipeline
- Modular architecture enabling easy customization

## Technology Stack & Currency Score

**Primary Stack:** Python (50.6%), JavaScript (21.3%), PowerShell (17.5%), CSS (9.5%), HTML (1.2%)

**Key Dependencies:** PyGithub, PyYAML, svgwrite, requests, python-dateutil, Chart.js, react-chartjs-2, Dexie

**Tech Currency: 69/100** - Modern Python/JavaScript stack with current libraries; some opportunities for dependency updates to cutting-edge versions.

## Activity & Maturity Profile

- **Highly Active & Accelerating:** 171 commits in 90 days, 209 commits in 365 days indicating rapid development velocity
- **Recently Updated:** Continuous improvements and feature additions
- **Zero External Visibility:** 0 stars/forks/contributors suggests this is either a newly launched project or private portfolio tool
- **Substantial Codebase:** 14.8 MB repository size indicates comprehensive implementation

## Target Use Cases & Value Proposition

Stats Spark addresses distinct personas: individual developers showcasing GitHub portfolios, technical leaders analyzing team productivity metrics, open-source maintainers tracking project momentum, and organizations conducting repository health assessments. The combination of automated weekly updates, AI-powered insights, mobile-optimized dashboards, and enterprise-grade architecture creates a unique value proposition for GitHub-centric development workflows.

**Technology Stack Currency**: ✅ 69/100
**Dependencies**: 10 total (1 current, 9 outdated)

**Created**: 2025-12-28
**Last Modified**: 2026-04-01

---

### #3. [mark-hazleton-s-notes](https://github.com/markhazleton/mark-hazleton-s-notes)

Stars: 0 | Forks: 0 | Language: TypeScript | 141 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 292877 KB | 🚀 47.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Mark Hazleton's Notes

This is a fully-featured personal portfolio and blog site for a Technical Solutions Architect, built as a modern React application with a sophisticated static site generation (SSG) pipeline. The site delivers long-form technical writing on cloud architecture and engineering practices, an interactive project portfolio, live GitHub repository metrics, and video content—all statically prerendered for optimal performance and SEO. The tech stack combines React 19 with Vite 7, TypeScript, Tailwind CSS, and Radix UI components, paired with a custom build orchestration system that generates SEO assets, optimizes images for RSS feeds, and integrates live data from external sources (GitHub repository statistics) at build time. The architecture demonstrates advanced patterns including SSR/static hybrid rendering, build-time data fetching and transformation, content-driven prerendering of dynamic routes (blog posts, project pages, repository details), and automated metadata generation from Markdown sources—all deployed to Azure Static Web Apps with continuous integration via GitHub Actions. What distinguishes this project is its comprehensive content strategy: it combines Markdown-based articles with generated metadata (articles.json, projects.json), implements full RSS/sitemap generation with Media RSS namespace support for rich feed images, and maintains a live GitHub integration that refreshes repository metrics without requiring client-side API calls. The site serves as both a technical demonstration of modern web development practices (edge caching via Azure, SEO optimization, responsive design with shadcn/ui) and a content platform, making it ideal for architects and technical leaders who want a portfolio that showcases both expertise and engineering rigor.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 61 total (61 current, 0 outdated)

**Created**: 2026-01-10
**Last Modified**: 2026-04-02

---

### #4. [MuseumSpark](https://github.com/markhazleton/MuseumSpark)

Stars: 0 | Forks: 0 | Language: Python | 77 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 23795 KB | 🚀 25.7 commits/month

**Quality**: ❌ License | ✅ Docs

# MuseumSpark - Technical Summary

## Overview
**MuseumSpark** is an intelligent museum discovery and travel planning platform designed to transform the Walker Art Center Reciprocal Program membership directory into a data-rich, personalized travel companion for art enthusiasts across North America. The project currently tracks 1,269 museums and is in active Phase 1 development, with an ambitious roadmap extending through Q4 2026 to include AI-powered personalization, trip planning, and user account management.

## Key Features & Architecture
The platform combines a modern **React 19 + Vite frontend** (deployed via GitHub Pages) with a sophisticated **Python-based data enrichment pipeline** that ingests and validates museum data through multiple phases. Core capabilities include: comprehensive museum browsing with state/province filtering and full-text search, detailed museum profiles with contact information and collection metadata, real-time data quality dashboards tracking enrichment progress (currently 0.08% complete), and multi-phase JSON Schema validation ensuring data integrity. The data pipeline orchestrates content from Wikidata, Wikipedia, museum websites, and specialized CSV lookups through nine enrichment phases, with planned integration of Claude/OpenAI agents (Phase 2.5–3) for AI-assisted collection analysis and scoring.

## Technology & Design Patterns
The tech stack leverages **Python 3.11+ with Pydantic 2** for rigorous data validation, **BeautifulSoup4** for web scraping, **TypeScript** for type-safe scripting, and **Tailwind CSS 4** for responsive UI styling. The architecture follows a **multi-phase enrichment pattern** with clear data quality rules (notably "Never Replace Known With Null"), JSON Schema validation checkpoints, and evidence tracking to ensure provenance and auditability. Future phases (Phase 4) will introduce a **FastAPI backend with SQLite persistence** and PydanticAI for structured LLM interactions.

## Unique Aspects & Use Cases
What distinguishes MuseumSpark is its **specialized focus on art museum curation and strategic travel optimization**—rather than a generic directory, it prioritizes museums by collection strength (Impressionist, Modern, Contemporary), historical significance, and reputation while providing visit duration estimates and nearby clustering. The project is designed for art enthusiasts planning anything from 2-hour layover visits to multi-day museum tours, making it invaluable for travelers seeking to maximize cultural experiences within time and geographic constraints. The transparent, publicly tracked enrichment dashboard and commitment to data quality assurance also serve as a community resource showing real-time progress toward a comprehensive North American art museum database.

**Created**: 2026-01-15
**Last Modified**: 2026-03-29

---

### #5. [UISampleSpark](https://github.com/markhazleton/UISampleSpark)

Stars: 8 | Forks: 4 | Language: HTML | 86 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 30884 KB | 🚀 28.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: UISampleSpark

**UISampleSpark** is a comprehensive educational reference application built on .NET 10 and ASP.NET Core that demonstrates multiple modern web UI architectural patterns and technologies using a common Employee/Department domain model. The repository implements seven distinct UI approaches—MVC with AJAX, Razor Pages, vanilla JavaScript SPA, React 18, Vue 3, htmx, and Blazor Server—allowing developers to compare implementation patterns, performance characteristics, and developer experience across different front-end paradigms. The application features a robust backend with REST/OpenAPI endpoints, Entity Framework Core data access, dependency injection, unit testing infrastructure, dynamic Bootswatch theming with real-time theme switching, and comprehensive CI/CD automation via GitHub Actions with Docker containerization and Azure deployment support. Architecturally, the project employs clean separation of concerns through layered projects (UI, Core, Data, Tests), repository patterns, service abstractions, and health checks with Application Insights observability. The codebase is actively maintained with accelerating activity (86 commits in 90 days), represents five years of evolution from .NET Core through .NET 10, and is uniquely valuable as both a learning resource for comparing UI technologies and a reference implementation demonstrating modern ASP.NET Core best practices including API key security, pagination, validation, and containerized deployment. Primary audiences include .NET developers evaluating front-end frameworks, architects designing polyglot UI solutions, and teams establishing CI/CD and cloud deployment patterns for web applications.

**Created**: 2019-04-25
**Last Modified**: 2026-03-29

---

### #6. [git-spark](https://github.com/markhazleton/git-spark)

Stars: 0 | Forks: 0 | Language: TypeScript | 37 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 1256 KB | 🚀 12.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Git Spark - Technical Summary

**Git Spark** is a TypeScript-based Git repository analytics and reporting tool that analyzes commit history to generate interactive HTML dashboards with insights into contributor activity, code changes, and development patterns. The project provides both a CLI tool and Node.js API, enabling users to export analysis results in multiple formats (HTML, JSON, CSV, Markdown) with features including daily trend visualizations, contributor statistics, file change analysis, and customizable reporting periods. The tech stack leverages modern TypeScript tooling with dependencies like Commander (CLI), Ora (spinners), Chalk (styling), and Boxen (formatting), demonstrating high currency (95/100) and active development with 37 commits in the last 90 days across a hybrid language codebase (63.7% TypeScript, 21.1% PowerShell, 13.8% HTML). The architecture emphasizes security and accessibility through strict Content Security Policy implementation, SHA-256 hashed inline scripts, self-contained reports suitable for air-gapped environments, ARIA compliance, and transparent metric documentation with honest explanations of analytical limitations. The tool targets enterprise and development teams seeking code health insights, governance analysis, risk factor visualization (churn, recency, ownership, knowledge concentration), and conventional commit adherence tracking without external API dependencies. Notably, the project includes progressive enhancement patterns (incremental pagination, dark mode with localStorage persistence), configurable email redaction for privacy-sensitive audits, and an interactive HTML report dashboard that supports dataset toggles and one-click data export capabilities, making it valuable for code review processes, team analytics, and audit workflows.

**Technology Stack Currency**: ✅ 95/100
**Dependencies**: 19 total (16 current, 3 outdated)

**Created**: 2025-09-29
**Last Modified**: 2026-03-30

---

### #7. [TailwindSpark](https://github.com/markhazleton/TailwindSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 47 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 5068 KB | 🚀 15.7 commits/month

**Quality**: ❌ License | ✅ Docs

# TailwindSpark - Technical Summary

**TailwindSpark** is a comprehensive Tailwind CSS design system and component showcase built as a modern React TypeScript monorepo, serving as both a production-ready UI framework and an educational reference for modern web development practices. The project demonstrates a complete design system implementation using Tailwind CSS v4 with @theme directives and CSS custom properties, featuring a rich library of interactive components (buttons, forms, cards, modals, dashboards, e-commerce flows) alongside a showcase application with analytics, user management, and performance monitoring capabilities.

The technical stack is modern and cutting-edge, leveraging React 19.1 with concurrent features, TypeScript 5.9 in strict mode, Vite 7.1 for HMR and optimized builds, and Turborepo 2.7 for monorepo package management, complemented by Vitest for testing, React Router 7.9 for routing, and Lucide React for a consistent icon system. The architecture employs a well-structured monorepo pattern with shared packages (design-tokens and ui-components) consumed by the main demo application, enabling code reuse, consistent theming, and scalable component development across the organization.

What distinguishes TailwindSpark is its commitment to production-grade quality and developer experience: it includes automated CI/CD pipelines via GitHub Actions, comprehensive accessibility compliance (WCAG 2.1 AA), real-time Web Vitals monitoring, security scanning with CodeQL and Dependabot, type-safe component development, and dark mode support with CSS variable theming. The project targets frontend developers, design system teams, and organizations seeking a reference implementation for building scalable, accessible, and performant React applications with Tailwind CSS, while also serving as Mark Hazleton's portfolio piece demonstrating full-stack modern web development expertise.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2025-07-29
**Last Modified**: 2026-03-26

---

### #8. [RequestSpark](https://github.com/markhazleton/RequestSpark)

Stars: 2 | Forks: 1 | Language: C# | 46 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 947 KB | 🚀 15.3 commits/month

**Quality**: ❌ License | ✅ Docs

# RequestSpark - Technical Summary

RequestSpark is a comprehensive .NET 10 (LTS) application for executing, analyzing, and benchmarking REST APIs through Postman collection integration and automated testing workflows. The solution provides dual interfaces—a console application and a Razor Pages web UI—enabling users to import Postman collections, run regression tests, perform load testing, and generate detailed performance reports with statistical analysis (percentiles, success rates, response time comparisons). The architecture is modular, consisting of core domain logic (RequestSpark.Domain), a dedicated Postman import service (RequestSpark.PostmanImport), console and web presentation layers, and comprehensive test suites (Domain.Tests, Web.Tests), all built on modern C# with MSTest v4 quality analyzers and zero known vulnerabilities. The project distinguishes itself through significant performance optimizations (19% faster builds, 25% faster test execution on .NET 10), high test coverage (21/21 passing tests), and production-ready features like CSV export, built-in sample CRUD APIs for demonstration, and configurable load testing parameters. RequestSpark targets quality assurance teams, API developers, and DevOps engineers who need robust, open-source tooling for API validation, performance benchmarking, and regression testing without proprietary dependencies, while maintaining an accelerating development pace (46 commits in 90 days) and clear governance documented in repository constitution guidelines.

**Created**: 2021-09-30
**Last Modified**: 2026-03-31

---

### #9. [ReactSparkPortfolio](https://github.com/markhazleton/ReactSparkPortfolio)

Stars: 0 | Forks: 0 | Language: CSS | 33 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 42270 KB | 🚀 11.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: ReactSparkPortfolio

**ReactSparkPortfolio** is a production-ready, enterprise-grade developer portfolio application built with React 19, TypeScript, and Vite that demonstrates modern frontend engineering best practices and cloud-native deployment patterns. The project showcases a comprehensive tech stack including Bootstrap 5 for responsive UI, SCSS for advanced styling with theme switching, SignalR for real-time chat capabilities, and integration with multiple external APIs (OpenWeather, JokeAPI, RSS feeds) via a serverless architecture. The application employs a modular component-based architecture with strict TypeScript type safety, implements WCAG 2.1 AA accessibility compliance, and leverages advanced optimization techniques including lazy loading, code splitting, and Vite's lightning-fast build system to deliver high performance across all devices. Key distinctive features include real-time communication via SignalR, dynamic RSS feed integration, interactive weather widgets with Leaflet maps, and dual deployment strategies across Azure Static Web Apps and GitHub Pages with automated CI/CD via GitHub Actions. The 42MB codebase (CSS 37.4%, TypeScript 32.3%, PowerShell 24.6%) demonstrates a highly active development pattern with 33 recent commits over 90 days, positioning it as both a functional personal portfolio and a comprehensive reference implementation for scalable, maintainable enterprise web applications suitable for developers, architects, and organizations seeking best-practice patterns for modern React development and cloud deployment.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 46 total (46 current, 0 outdated)

**Created**: 2024-10-11
**Last Modified**: 2026-03-30

---

### #10. [KeyPressCounter](https://github.com/markhazleton/KeyPressCounter)

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

### #11. [SupportSpark](https://github.com/markhazleton/SupportSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 43 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 1232 KB | 🚀 14.3 commits/month

**Quality**: ❌ License | ❌ Docs

# SupportSpark - Technical Summary

**SupportSpark** is a compassionate support network platform built with modern web technologies that enables people to share life journey updates with trusted circles during challenging times. The application implements a role-based architecture where members create and manage conversation updates while supporters receive invitations, read updates in real-time, and provide threaded responses—solving the exhaustion of manually keeping loved ones informed during health challenges, life transitions, or personal crises.

The tech stack leverages **React 19 with Vite** for the frontend, **Express 5** for the backend, **TypeScript** (strict mode) for end-to-end type safety, and **Tailwind CSS 4** with shadcn/ui and Radix primitives for an accessible, calming interface. The application uses **TanStack React Query** for intelligent server state management, **Passport.js** for authentication via sessions, **Zod** for runtime validation, and **Framer Motion** for purposeful animations—demonstrating a mature, production-ready architecture with clear separation of concerns (client/server/shared folders with unified type contracts).

Notably, SupportSpark is optimized for **Windows 11 + IIS deployment** using iisnode, with fully automated PowerShell deployment scripts and comprehensive IIS configuration via web.config, while also offering a client-side GitHub Pages preview that runs entirely in localStorage for zero-friction exploration. The project exhibits high activity (43 commits in 90 days with accelerating patterns), strong organizational governance documented in a constitution, and thoughtful UX design specifically for sensitive contexts—making it uniquely positioned as a purpose-driven platform addressing an underserved emotional need rather than generic social networking or messaging.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 98 total (98 current, 0 outdated)

**Created**: 2026-02-01
**Last Modified**: 2026-03-29

---

### #12. [JsBootSpark](https://github.com/markhazleton/JsBootSpark)

Stars: 0 | Forks: 0 | Language: JavaScript | 22 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 3548 KB | 🚀 7.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: JsBootSpark

**JsBootSpark** is a production-ready, full-stack starter kit designed to accelerate modern web application development by combining Express.js backend with Bootstrap 5 frontend, complete with hot-reload development capabilities, comprehensive documentation, and automated deployment pipelines. The project serves as a boilerplate for developers seeking a batteries-included foundation featuring security middleware (Helmet.js, rate limiting, CSP), responsive UI components with dark/light mode toggle, SASS preprocessing, and a robust build system that includes static site generation (100+ pages from templates), CSV-to-JSON data conversion, and GitHub Pages/Docker deployment support. Built with Node.js 18+, it leverages EJS templating, ESLint/Prettier code formatting, Jest testing frameworks, and Service Worker integration for PWA functionality, making it suitable for everything from simple content sites to complex single-page applications. The architecture emphasizes developer experience through Docker containerization, automated GitHub Actions CI/CD pipelines, and extensive documentation organized by audience (quick-start guides, security policies, contributor guidelines), alongside AI-assisted development sessions tracked in Copilot directories. What distinguishes JsBootSpark is its hybrid approach combining static and dynamic generation capabilities, SEO optimization with structured data, subdirectory deployment handling, and performance-first philosophy with compression middleware and responsive image optimization. The project targets full-stack JavaScript developers, development teams, and organizations seeking to rapidly prototype or deploy web applications without sacrificing production-grade security, performance monitoring, and maintainability standards.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 30 total (30 current, 0 outdated)

**Created**: 2022-06-06
**Last Modified**: 2026-01-31

---

### #13. [Texecon](https://github.com/markhazleton/Texecon)

Stars: 0 | Forks: 0 | Language: HTML | 29 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 3225 KB | 🚀 9.7 commits/month

**Quality**: ❌ License | ❌ Docs

# TexEcon Technical Summary

**TexEcon** is a modern static React application designed to deliver expert economic analysis and commentary on the Texas economy, optimized for deployment on GitHub Pages with a focus on SEO performance and content freshness. The project implements a sophisticated build-time content management system that fetches dynamic content from a WebSpark headless CMS API during compilation, with intelligent fallback mechanisms to cached data, enabling static site generation with pre-rendered pages while maintaining content currency without runtime API calls. Built on React 19, TypeScript, Vite 7.1, and Tailwind CSS, the application leverages Radix UI and shadcn/ui for accessible component primitives, Wouter for lightweight client-side routing, and implements advanced SEO capabilities including structured data, dynamic sitemap generation, and Core Web Vitals optimization. The architecture demonstrates a hybrid static-dynamic approach through its multi-stage build pipeline (content fetch → sitemap generation → Vite compilation → static page generation) that achieves the performance benefits of static sites while supporting dynamic content routes and progressive enhancement with HTML fallbacks. This design pattern is particularly noteworthy for balancing the need for fresh, CMS-driven content with the deployment simplicity, security, and performance characteristics of GitHub Pages, making it an excellent reference implementation for content-heavy applications requiring both scalability and search engine optimization without traditional server infrastructure.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 37 total (37 current, 0 outdated)

**Created**: 2025-09-03
**Last Modified**: 2026-03-30

---

### #14. [WebSpark](https://github.com/markhazleton/WebSpark)

Stars: 1 | Forks: 0 | Language: C# | 12 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 69023 KB | 🚀 4.0 commits/month

**Quality**: ❌ License | ❌ Docs

# WebSpark Technical Summary

**WebSpark** is a comprehensive .NET 9-based web application suite comprising three specialized tools: PromptSpark (LLM prompt optimization), RecipeSpark (recipe management), and TriviaSpark (quiz creation platform). Built on ASP.NET Core MVC with Bootstrap 5, the project features a modular seven-area architecture (PromptSpark, RecipeSpark, TriviaSpark, WebCMS, AsyncSpark, Admin, Identity) designed for scalability and versatility across multiple business domains. The repository uniquely emphasizes **spec-driven development** with an automated SpecKit workflow that includes rigorous adversarial risk assessment (`/speckit.critic` command) to identify showstoppers, security vulnerabilities, performance issues, and operational gaps before implementation—enforcing quality gates and reducing production risk. Additional notable capabilities include comprehensive SEO optimization features (dynamic meta tags, JSON-LD structured data, XML sitemaps, Google Analytics 4 integration, Core Web Vitals monitoring, and SEO audit logging via Application Insights) with 47 passing tests validating implementation quality. The codebase is actively maintained with modern web standards, organized through feature-branch-based specifications, and represents an enterprise-grade approach to managing complexity across multiple interconnected web applications while maintaining strict architectural governance.

**Created**: 2024-01-11
**Last Modified**: 2026-01-29

---

### #15. [WebProjectMechanics](https://github.com/markhazleton/WebProjectMechanics)

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

### #16. [PromptSpark.Chat](https://github.com/markhazleton/PromptSpark.Chat)

Stars: 0 | Forks: 0 | Language: C# | 29 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 19200 KB | 🚀 9.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: PromptSpark.Chat

**PromptSpark.Chat** is a real-time conversational workflow application built on ASP.NET Core and SignalR that enables users to navigate multi-step guided processes through an interactive chat interface powered by Adaptive Cards. The application demonstrates a practical implementation of dynamic workflow orchestration with branching logic, combining server-side conversation state persistence using thread-safe ConcurrentDictionary with real-time client-server communication to maintain continuity across browser sessions. Key technical features include JSON-based workflow configuration for defining node-based conversation flows, optional AI integration via chat completion services for handling out-of-scope inquiries, and a responsive frontend utilizing SCSS/CSS and JavaScript alongside Razor views for structured UI rendering. The architecture follows an MVC pattern with clear separation of concerns across Controllers, Services, and Models, leveraging SignalR hubs for efficient bidirectional communication rather than traditional polling. This project is particularly valuable for organizations requiring configurable, low-overhead workflow automation platforms—such as customer onboarding, guided troubleshooting, form collection, or interactive surveys—where minimal infrastructure overhead and flexible branching logic are priorities over heavy BPM suites. The recently accelerating activity and clean, well-documented codebase make it suitable for developers seeking a production-ready template for implementing conversational interfaces with ASP.NET Core, though its zero stars and single-contributor status suggest it may be a newer or internal project not yet widely discovered by the broader community.

**Created**: 2024-12-31
**Last Modified**: 2026-03-30

---

### #17. [DataSpark](https://github.com/markhazleton/DataSpark)

Stars: 0 | Forks: 0 | Language: HTML | 19 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 2075 KB | 🚀 6.3 commits/month

**Quality**: ❌ License | ✅ Docs

# DataSpark Technical Summary

DataSpark is a comprehensive .NET 10 toolkit designed for SQLite database analysis and code generation, offering both command-line and web-based interfaces for developers and data analysts. The project provides core functionality for discovering SQLite files, exporting tables to CSV, generating schema reports in multiple formats (text, JSON, Markdown), and automatically generating C# Data Transfer Objects (DTOs) from database schemas. Built with a modular architecture, it consists of a reusable core library (DataSpark.Core) shared between a CLI application (DataSpark.Console) and an ASP.NET Core MVC web UI (DataSpark.Web), complemented by comprehensive MSTest unit tests and BenchmarkDotNet performance benchmarks. The web interface adds user-friendly functionality including file upload capabilities, interactive table analysis, CSV export workflows, and persistent file management, while the CLI caters to automation and scripting scenarios. The project demonstrates solid engineering practices with continuous integration via GitHub Actions, code coverage tracking, semantic versioning support for .NET 10, and clear separation of concerns across projects. This toolkit targets developers who need to quickly integrate legacy SQLite databases into modern .NET applications or require batch processing capabilities for database schema extraction and data export tasks.

**Created**: 2017-11-06
**Last Modified**: 2026-04-01

---

### #18. [markhazleton](https://github.com/markhazleton/markhazleton)

Stars: 0 | Forks: 0 | Language: Unknown | 16 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 6604 KB | 🚀 5.3 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: markhazleton Repository

This repository serves as Mark Hazleton's personal portfolio and learning archive, functioning as a curated collection of technical projects and professional development work rather than a single monolithic application. The repository showcases multiple featured projects including **Spec-Kit-Spark** (a modernized fork of GitHub SpecKit for brownfield development) and **ReactSpark** (a React/Vite-based web application hosted on Azure Static Web Applications), alongside integration with a personal blog platform documenting architectural decisions and software development methodology. The tech stack spans full-stack development with emphasis on .NET/C# backend work (evidenced by NuGet package development and Azure DevOps integration), React/TypeScript frontend frameworks, and cloud-native deployment on Azure, complemented by API testing and load testing tools like RESTRunner. The repository demonstrates a pragmatic, evolution-focused development philosophy centered on outcomes over features, with automated GitHub statistics visualization and CI/CD practices that reflect enterprise-grade development patterns. This project is particularly noteworthy for its transparent documentation of learning progression, architectural evolution, and multi-user collaboration patterns, making it valuable for developers seeking insights into professional software architecture, team-based development practices, and continuous improvement methodologies. The target audience includes software architects, senior developers, and technical leads interested in brownfield modernization, API development practices, and sustainable software engineering approaches.

**Created**: 2021-04-17
**Last Modified**: 2026-04-02

---

### #19. [react-native-web-start](https://github.com/markhazleton/react-native-web-start)

Stars: 0 | Forks: 0 | Language: PowerShell | 18 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2067 KB | 🚀 6.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: react-native-web-start

## Overview
**react-native-web-start** is a production-ready, enterprise-grade starter template that enables developers to build truly cross-platform applications (Web, iOS, Android) from a single TypeScript codebase using React Native Web and Vite. The project provides a comprehensive monorepo structure with shared components, automated build pipelines, and modern tooling that eliminates the traditional friction of maintaining separate web and mobile codebases while maintaining platform-specific optimizations.

## Key Features & Capabilities
The template emphasizes developer experience with lightning-fast Vite-powered development cycles featuring Hot Module Replacement, full TypeScript strict mode support, and sophisticated asset management through custom build scripts. It includes production-ready utilities such as a built-in markdown documentation browser, API integration patterns, responsive design systems powered by Tailwind CSS 4.1.18, and comprehensive GitHub Pages deployment automation with CI/CD workflows. The architecture implements a clean monorepo pattern (`packages/shared`, `packages/web`, `packages/mobile`) that enforces single-source-of-truth principles while supporting platform-specific customizations through Metro bundler configuration for mobile and Vite's plugin system for web.

## Technology Stack & Architecture
The project leverages a modern, well-curated tech stack: React 19.2.3 with React Native 0.83.1 for cross-platform compatibility, Vite 7.3.1 as the primary build orchestrator, TypeScript 5.9.3 for type safety, Metro 0.83.1 for mobile bundling, and Tailwind CSS 4.1.18 with Sass 1.97.2 for styling. The codebase demonstrates sophisticated build automation through custom Node.js scripts (build.js, copy-docs.js, generate-build-info.js) that manage asset pipelines, documentation synchronization, and dynamic build metadata generation, reflecting enterprise-level DevOps considerations.

## Unique Value Proposition
What distinguishes this template is its maturity and production-readiness—it's not merely a proof-of-concept but includes features like security integration (Dependabot), performance monitoring capabilities, PWA support, SEO optimization, comprehensive in-app documentation infrastructure, and proven GitHub Pages deployment automation. The 49-dependency ecosystem is carefully balanced for minimal bloat while maintaining sufficient abstraction for real-world applications, and the consistent development activity (18 commits in 90 days, 71 in 365 days) indicates active maintenance and community responsiveness.

## Target Users & Use Cases
This template is ideal for teams seeking to maximize code reuse across web and mobile platforms without sacrificing platform-specific optimizations, particularly organizations prioritizing TypeScript-first development, fast iteration cycles, and modern DevOps practices. It serves startups building MVP products requiring multi-platform presence, enterprises standardizing on React Native Web for internal tools, and developers transitioning from traditional web stacks to cross-platform development.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 49 total (49 current, 0 outdated)

**Created**: 2025-07-26
**Last Modified**: 2026-03-31

---

### #20. [InquirySpark](https://github.com/markhazleton/InquirySpark)

Stars: 0 | Forks: 0 | Language: C# | 9 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 9765 KB | 🚀 3.0 commits/month

**Quality**: ❌ License | ✅ Docs

# InquirySpark - Technical Summary

**InquirySpark** is a .NET 10–based survey and inquiry management system designed with an immutable, read-only SQLite persistence layer and a responsive Bootstrap 5 MVC admin interface for data exploration and reporting. The architecture leverages Entity Framework Core 10 with Microsoft.Data.Sqlite provider, enforcing read-only database connections to ensure data integrity and prevent unintended mutations, making it ideal for secure inquiry analytics and survey result management without the overhead of SQL Server. The solution is composed of modular layers—InquirySpark.Admin (UI/MVC), InquirySpark.Repository (EF Core abstractions), InquirySpark.Common (shared models and SDKs), and a comprehensive MSTest suite—with automated npm asset pipelines and strict nullable reference type enforcement for code quality. Notable design decisions include primary constructor dependency injection, centralized configuration via `SqliteOptionsConfigurator`, DataTables integration for dynamic table rendering, and pre-built immutable SQLite databases (`ControlSparkUser.db` and `InquirySpark.db`) distributed as assets, eliminating migration complexity and enabling zero-setup deployment. The project is well-documented with detailed specifications, architecture guides, and troubleshooting resources, targeting teams seeking a lightweight, self-contained inquiry platform without external database dependencies or infrastructure complexity. Its recent activity (9 commits in 90 days) and structured approach to feature specifications indicate active maintenance and a clear roadmap for future enhancements.

**Created**: 2023-10-24
**Last Modified**: 2026-03-30

---

### #21. [markhazleton.github.io](https://github.com/markhazleton/markhazleton.github.io)

Stars: 0 | Forks: 0 | Language: SCSS | 8 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 157 KB | 🚀 2.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: markhazleton.github.io

This repository is Mark Hazleton's personal website built with **Jekyll 3.10.0** and hosted on **GitHub Pages**, serving as a customizable blogging platform and portfolio site. The project utilizes a modified Minima theme with custom SCSS styling (39.4%), HTML layouts (30.1%), and CSS (29.8%), enabling responsive design and dark/light mode toggle functionality without relying on external CSS frameworks. The tech stack includes Ruby 3.2.2 for runtime, Bundler for dependency management, and GitHub Actions for automated CI/CD deployment triggered on pushes to the `sources` branch, with three core dependencies (github-pages, faraday-retry, wdm) optimized for cross-platform development. The site architecture follows Jekyll conventions with organized directories for posts, layouts, includes, and assets, supporting SEO optimization through proper front matter (title, date, categories, tags, excerpts) and markdown-based content management with built-in syntax highlighting for code snippets. The project demonstrates active maintenance (8 commits in 90 days, 23 in the past year) and provides comprehensive developer documentation for local setup across macOS, Windows, and Linux, as well as standardized workflows for creating and publishing blog posts via direct commits or feature branches. This implementation serves as a practical example of a modern static site generator setup, ideal for technical writers, developers, and professionals seeking a lightweight, Git-based blogging platform with full version control and automated deployment capabilities.

**Technology Stack Currency**: ✅ 56/100
**Dependencies**: 3 total (2 current, 1 outdated)

**Created**: 2021-04-18
**Last Modified**: 2026-04-01

---

### #22. [PHPDocSpark](https://github.com/markhazleton/PHPDocSpark)

Stars: 0 | Forks: 0 | Language: PHP | 6 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 2884 KB | 🚀 2.0 commits/month

**Quality**: ❌ License | ✅ Docs

# PHPDocSpark - Technical Summary

**PHPDocSpark** is a modern, open-source PHP documentation and data exploration platform that demonstrates contemporary full-stack web development practices by combining traditional server-side PHP with a modern Vite-based asset pipeline. The project serves as both a functional tool for managing markdown-based documentation with full-text search capabilities and an educational reference implementation showcasing hybrid architecture patterns, featuring interactive data visualization (Chart.js), CSV analysis tools, SQLite integration, GitHub API integration, and responsive Bootstrap 5 UI design. Built on PHP 8.2+ with Node.js tooling, it leverages Vite for hot module replacement during development, SCSS preprocessing, ESLint/Prettier for code quality, and Azure Pipelines for CI/CD deployment, demonstrating best practices in DevOps and modern PHP development workflows. The architecture employs a clean front-controller pattern with feature-based organization, output buffering for template composition, and intelligent caching strategies for API calls and file operations, making it equally valuable as a portfolio project, internal documentation platform, or learning resource for developers exploring modern PHP development alongside contemporary JavaScript tooling. Maintained with accelerating activity (42 commits in 365 days), it represents a mature, actively developed project targeting PHP developers, full-stack engineers, technical writers, and students seeking reference implementations for building scalable, maintainable web applications with professional-grade development infrastructure.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2023-09-08
**Last Modified**: 2026-03-30

---

### #23. [TeachSpark](https://github.com/markhazleton/TeachSpark)

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

### #24. [FastEndpointApi](https://github.com/markhazleton/FastEndpointApi)

Stars: 2 | Forks: 1 | Language: HTML | 1 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 137 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

Demo of FastEndpoints Nuget Packages Written in HTML. 2 stars, 1 forks. 1 commits in the last 90 days.

**Created**: 2024-04-06
**Last Modified**: 2026-03-30

---

### #25. [MechanicsOfMotherhood](https://github.com/markhazleton/MechanicsOfMotherhood)

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

### #28. [WebSpark.Bootswatch](https://github.com/markhazleton/WebSpark.Bootswatch)

Stars: 0 | Forks: 0 | Language: HTML | 5 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7124 KB | 🚀 1.7 commits/month

**Quality**: ❌ License | ✅ Docs

# WebSpark.Bootswatch - Technical Summary

**WebSpark.Bootswatch** is a .NET Razor Class Library that provides seamless integration of Bootswatch themes into ASP.NET Core applications, built on Bootstrap 5 to enable modern, responsive UI theming with dynamic switching and light/dark mode support. The library is architected as a production-ready component leveraging .NET 10 exclusively (version 2.0+), implementing caching mechanisms through the `StyleCache` service and providing Tag Helper support for simplified UI integration. Key technologies include C# (28.6%), HTML (63.8%), and JavaScript (2.6%), with dependencies on `WebSpark.HttpClientUtility` for HTTP operations and modern `Microsoft.Extensions.*` packages version 10.0.1+. The library employs a service-oriented pattern with extension methods for dependency injection, comprehensive error handling, fallback mechanisms, and full IntelliSense/XML documentation support for developer experience. Unique to this project is its strategic decision to target only .NET 10, prioritizing access to latest security patches and modern dependencies over broad framework compatibility, with a clear migration path provided for users on .NET 8/9 through version 1.34.0. This library targets ASP.NET Core developers building enterprise applications who require flexible, maintainable theming solutions with built-in performance optimization and the ability to dynamically switch between multiple professional Bootswatch themes without page reloads.

**Created**: 2022-08-24
**Last Modified**: 2026-01-12

---

### #29. [WebSpark.PrismSpark](https://github.com/markhazleton/WebSpark.PrismSpark)

Stars: 0 | Forks: 0 | Language: C# | 14 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 2272 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.PrismSpark

**WebSpark.PrismSpark** is a high-performance C#/.NET port of the popular PrismJS syntax highlighting library, designed to provide server-side code tokenization and HTML rendering for 24 programming languages with advanced theming and extensibility capabilities. The project leverages .NET 10.0 LTS with a modular architecture comprising core highlighting engines (`IHighlighter` interface), grammar-based tokenizers, a robust plugin system, and customizable theme management through `ThemeManager` and `CssGenerator` classes. Key architectural strengths include event-driven hooks for post-processing customization, support for enhanced options (line numbering, line highlighting, custom CSS classes), async processing for performance optimization, and a comprehensive MSTest suite with 52 tests ensuring reliability across grammar parsing, tokenization, and end-to-end integration workflows. The library is particularly well-suited for ASP.NET MVC/Razor applications through dependency injection patterns and includes interactive demo web components featuring a live code editor, real-time validation, and markdown integration via Markdig. What distinguishes this implementation is its .NET-native design combining PrismJS's linguistic flexibility with C# performance characteristics, extensive language support spanning web technologies (HTML, CSS, JavaScript), systems languages (C, C++, Rust, Go), and markup formats (Markdown, YAML, Pug), making it an ideal solution for documentation platforms, code review tools, educational applications, and any .NET-based system requiring server-rendered syntax highlighting without client-side JavaScript dependencies.

**Created**: 2025-05-27
**Last Modified**: 2026-02-11

---

### #30. [DocSpecSpark](https://github.com/markhazleton/DocSpecSpark)

Stars: 0 | Forks: 0 | Language: Python | 2 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 181 KB | 🚀 0.7 commits/month

**Quality**: ❌ License | ✅ Docs

Document Spec Kit Spark Written in Python. 2 commits in the last 90 days.

**Created**: 2026-03-07
**Last Modified**: 2026-03-08

---

### #31. [TriviaSpark](https://github.com/markhazleton/TriviaSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 27238 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# TriviaSpark - Technical Summary

**TriviaSpark** is a multiplayer trivia game application developed as an experiment in AI-assisted development using Chat GPT, designed to fetch questions from public Trivia APIs and deliver an interactive competitive gaming experience. The project is built primarily with C# backend logic (61.1%) alongside HTML (26.5%) and CSS (12.3%) for frontend presentation, suggesting an ASP.NET web application architecture with potential cross-platform capabilities targeting both web and mobile environments. Key features include user registration and authentication, a leaderboard system for competitive ranking, an admin interface for question database management, and a customizable UI to enhance user engagement—all designed to deliver real-time multiplayer trivia gameplay with an upbeat, modern, and competitive tone. The application leverages RESTful API integration with external trivia data sources, demonstrating separation of concerns between client-side interactivity and server-side business logic, though the minimal commit history (4 commits over 365 days, 0 in the last 90 days) indicates the project is in an exploratory or inactive state. The repository's primary value lies in its documentation of AI-assisted development practices and serves as a case study for building interactive gaming applications, targeting tech-savvy individuals aged 18-95 seeking competitive trivia entertainment. The project's relatively large codebase (27.2 MB) combined with declining activity suggests it represents a proof-of-concept or learning exercise that may have reached completion or been abandoned during development.

**Created**: 2023-02-22
**Last Modified**: 2025-12-02

---

### #32. [DecisionSpark](https://github.com/markhazleton/DecisionSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 519 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

Configuration-driven decision routing engine for conversational experiences Written in C#.

**Created**: 2025-10-29
**Last Modified**: 2025-12-27

---


---

## Report Metadata

- **Generation Time**: 9.4 seconds
- **SVGs Generated**: 6/6
- **Total API Calls**: 0
- **Total AI Tokens**: 72,205
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
*Last updated: 2026-04-02*