# GitHub Profile: markhazleton

**Generated**: 2026-03-30 04:59:38 UTC
**Report Version**: 1.0.0
**Repositories Analyzed**: 37
**AI Summary Rate**: 100.0%

> 💡 **Navigation**: [Profile Overview](#profile-overview) | [Top Repositories](#top-37-repositories) | [Metadata](#report-metadata)

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

## Top 37 Repositories

### #1. [github-stats-spark](https://github.com/markhazleton/github-stats-spark)

Stars: 0 | Forks: 0 | Language: Python | 184 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 12140 KB | 🚀 61.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Stats Spark ⚡ - Technical Analysis

## Executive Summary

Stats Spark is a sophisticated GitHub analytics and visualization platform that transforms raw GitHub activity into professionally-rendered SVG dashboards and AI-powered repository insights. The project combines automated data collection via the GitHub API with intelligent analysis and interactive web-based visualization to provide developers, teams, and open-source maintainers with actionable intelligence about coding patterns, repository health, and technology usage trends.

## Architecture & Technical Approach

### Core Components

**Python Backend Stack (49.1%)**
- **PyGithub**: Primary GitHub API client for automated data collection
- **PyYAML**: Configuration management system supporting flexible YAML-based settings
- **svgwrite**: Programmatic SVG generation for embeddable profile statistics
- **requests + python-dateutil**: HTTP requests and temporal data handling for historical analysis
- Modular design with CLI support for local development and testing before CI/CD deployment

**Frontend Technologies (31.9%)**
- **JavaScript (21.9%)**: Interactive dashboard functionality
- **HTML/CSS (11.0%)**: Responsive mobile-first UI (320px-768px viewport optimization)
- **Chart.js + react-chartjs-2**: Interactive visualizations with touch-optimized tooltips
- **Dexie/IndexedDB**: Offline-capable caching with 7-day data retention

**Infrastructure & Automation (18.0%)**
- **PowerShell (18.0%)**: GitHub Actions workflow orchestration
- **GitHub Pages**: Automatic deployment pipeline with Lighthouse CI performance monitoring
- **Scheduled Automation**: Midnight UTC Sunday execution for weekly updates

## Key Features & Capabilities

### 1. **Dual Visualization Strategy**

**SVG Profile Statistics** (6 embeddable categories):
- **Spark Score Algorithm**: Proprietary 0-100 metric (40% consistency + 35% volume + 25% collaboration)
- **Contribution Heatmap**: GitHub-style calendar with intensity visualization
- **Language Distribution**: Technology stack breakdown with diversity metrics
- **Streak Tracking**: Current/longest consecutive contribution streaks
- **Fun Stats Module**: 8 personality-driven achievements with time-based coding patterns
- **Release Cadence**: Sparkline trends showing activity breadth across repositories

**Interactive Dashboard**:
- Mobile-native bottom sheet navigation and swipe gestures
- Drill-down repository analysis with commit history and dependency tracking
- "Needs Attention" ranking combining security alerts, PR backlog, dependency drift, and staleness
- CSV/JSON export functionality for external analysis

### 2. **AI-Powered Intelligence Layer**

- **Claude Haiku Integration**: Automated technical summaries with 97%+ success rate
- **Three-Tier Fallback Strategy**: Claude → README extraction → basic metadata ensures coverage
- **Composite Repository Ranking**: Weighted algorithm (30% popularity/45% activity/25% health) balances established projects with active development
- **Dependency Insights**: Schema 2.2.0 tracks version coverage, registry resolution, and maintenance signals

### 3. **Enterprise-Grade Reliability**

- **Smart API Caching**: Intelligent GitHub API optimization reducing rate-limit pressure
- **Exponential Backoff Retry Logic**: Graceful handling of 403/429 responses
- **Performance Optimization**: Sub-5-minute analysis for 500+ repositories with Lighthouse CI targeting <2s First Contentful Paint
- **WCAG 2.1 AA Compliance**: Full accessibility support with keyboard navigation and screen reader compatibility

## Activity & Development Velocity

- **Recent Commits**: 184 (90d) and 203 (365d) indicate consistent, accelerating development
- **Repository Size**: 12.1 MB with balanced language distribution suggests well-organized codebase
- **Tech Stack Currency**: 69/100 score reflects modern Python, JavaScript, and CI/CD practices
- **Creation Date**: December 2025 indicates recent launch with immediate community-scale ambitions

## Target Use Cases

1. **Developer Portfolio Enhancement**: Automatically updated profile README with professional statistics
2. **Team Analytics**: Repository health monitoring and productivity pattern analysis
3. **Open Source Maintainability**: Community engagement tracking and release cadence visualization
4. **Technical Leadership**: Developer profiling with technology diversity and contribution classification insights

## Notable Implementation Decisions

- **YAML Configuration**: Flexible, version-control-friendly configuration approach
- **SVG Over Raster**: Resolution-independent embeddable graphics supporting theme customization
- **Offline-First Dashboard**: IndexedDB caching enables functionality without continuous API connectivity
- **Modular Architecture**: Extensible design allowing custom analysis and visualization components

## Conclusion

Stats Spark represents a production-ready analytics solution that bridges GitHub's raw data with meaningful visualizations and AI-driven insights. Its combination of automated weekly updates, enterprise-grade reliability patterns, mobile-optimized dashboard, and intelligent repository ranking makes it particularly valuable for open-source maintainers and technical leaders seeking to understand development patterns at scale. The project demonstrates strong engineering practices through comprehensive error handling, accessibility compliance, and performance optimization.

**Technology Stack Currency**: ✅ 69/100
**Dependencies**: 10 total (1 current, 9 outdated)

**Created**: 2025-12-28
**Last Modified**: 2026-03-30

---

### #2. [mark-hazleton-s-notes](https://github.com/markhazleton/mark-hazleton-s-notes)

Stars: 0 | Forks: 0 | Language: TypeScript | 137 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 299394 KB | 🚀 45.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Mark Hazleton's Notes

This repository is a modern, feature-rich personal portfolio and blog site built for a Technical Solutions Architect, combining long-form technical writing, project portfolio showcase, and live GitHub activity metrics. The site is constructed with **React 19 + TypeScript** using **Vite 7** for SSR rendering and static prerendering, styled with **Tailwind CSS** and **shadcn/ui** components, and deployed to **Azure Static Web Apps** via automated GitHub Actions workflows. The architecture employs a sophisticated multi-stage build pipeline that generates metadata from Markdown content, fetches live GitHub repository statistics, optimizes images for RSS feeds (with Media RSS namespace support), and prerenders all routes to static HTML for maximum performance and SEO compliance, with output written to the `docs/` directory. Key differentiators include a dedicated `/github` page with live repository metrics fetched from external sources, a `/videos` page backed by build-time YouTube data with auto-generated video sitemaps, comprehensive RSS feed generation with optimized media, and a well-organized developer documentation structure (`.documentation/`) separate from published content. The project demonstrates production-grade practices including TypeScript strict typing, comprehensive SEO asset generation (sitemap.xml, robots.txt, canonical URLs, Open Graph tags), environment-based configuration, and clear content management workflows for blogs and projects. This is an ideal reference implementation for developers building personal brands or technical portfolio sites that require sophisticated content management, live data integration, and enterprise-grade deployment practices while maintaining clean separation between development tools, published content, and static build output.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 61 total (61 current, 0 outdated)

**Created**: 2026-01-10
**Last Modified**: 2026-03-29

---

### #3. [MuseumSpark](https://github.com/markhazleton/MuseumSpark)

Stars: 0 | Forks: 0 | Language: Python | 77 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 23795 KB | 🚀 25.7 commits/month

**Quality**: ❌ License | ✅ Docs

# MuseumSpark - Technical Summary

**MuseumSpark** is an intelligent travel planning platform designed to help art enthusiasts discover and prioritize museum visits across North America, built on the Walker Art Center Reciprocal Program's membership list of 1,269 museums. The project leverages a sophisticated multi-phase data enrichment pipeline that synthesizes information from Wikidata, Wikipedia, museum websites, and manual curation to create priority-ranked museum recommendations based on collection strength (Impressionist, Modern, and Contemporary art), historical significance, and travel logistics. The architecture employs a modern full-stack approach with a React 19 + Vite + Tailwind CSS frontend deployed on GitHub Pages for rapid browsing and filtering, paired with a Python 3.11+ backend pipeline using Pydantic 2 for strict data validation, JSON Schema for quality assurance, and BeautifulSoup4 for intelligent web scraping and content extraction. The project demonstrates sophisticated software engineering practices including automated quality checks with "never replace known with null" data governance, a comprehensive state-machine-based enrichment workflow (spanning 11+ sequential phases), and evidence-tracked validation to maintain data integrity across distributed sources. Currently in Phase 1 (80% complete) with only 0.08% of museums fully enriched, MuseumSpark showcases an ambitious roadmap toward an AI-powered travel companion (Phase 4) featuring FastAPI backend, user authentication, personalized itinerary generation, and LLM-assisted content analysis. The project targets art-focused travelers seeking strategic museum planning tools and demonstrates strong potential as a niche travel planning platform that combines domain expertise (art curation), data science (enrichment pipeline), and modern web technologies into a cohesive information product.

**Created**: 2026-01-15
**Last Modified**: 2026-03-29

---

### #4. [UISampleSpark](https://github.com/markhazleton/UISampleSpark)

Stars: 8 | Forks: 4 | Language: HTML | 86 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 30884 KB | 🚀 28.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: UISampleSpark

**UISampleSpark** is an educational .NET 10 (ASP.NET Core) reference application that provides a comprehensive comparison of modern front-end UI technologies by implementing the same Employee/Department domain across seven distinct patterns: MVC, Razor Pages, vanilla JavaScript SPA, React 18, Vue 3, htmx, and Blazor Server. The project serves as both a learning resource and architectural showcase, demonstrating clean layered architecture with dependency injection, repository/service patterns, and comprehensive unit testing across domain and data layers, while incorporating production-ready DevOps practices including GitHub Actions CI/CD, Docker containerization, Application Insights telemetry, and Azure deployment automation.

The application features a rich technology stack built on ASP.NET Core with Entity Framework Core, OpenAPI/Swagger documentation, dynamic Bootswatch theme switching with light/dark mode support, REST API endpoints secured via API keys, and specialized demos including PivotTable.js for reporting and TreeView components. Its architecture emphasizes separation of concerns through dedicated projects (`UISampleSpark.UI`, `UISampleSpark.Core`, `UISampleSpark.Data`) and leverages custom NuGet packages (`WebSpark.Bootswatch`, `WebSpark.HttpClientUtility`) for theming and HTTP utilities, enabling both in-browser JSX compilation (React via Babel standalone) and server-side rendering (Blazor, htmx) side-by-side.

What makes UISampleSpark noteworthy is its sustained evolution from 2019 through 2025—tracking major .NET versions through .NET 10—combined with its pragmatic demonstration of how different UI paradigms (hypermedia-driven htmx vs. reactive SPAs vs. real-time SignalR-backed Blazor) solve identical business problems, making it invaluable for architects and developers evaluating framework trade-offs. The repository is highly active with accelerating commit velocity, professional-grade CI/CD pipelines, live production deployments on Windows IIS and Docker Hub, and comprehensive documentation including CHANGELOG milestones and git commit velocity reports, positioning it as a mature reference implementation ideal for organizations modernizing legacy ASP.NET applications or making strategic UI technology choices.

**Created**: 2019-04-25
**Last Modified**: 2026-03-29

---

### #5. [WebSpark.HttpClientUtility](https://github.com/markhazleton/WebSpark.HttpClientUtility)

Stars: 0 | Forks: 0 | Language: C# | 51 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2405 KB | 🚀 17.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.HttpClientUtility

**WebSpark.HttpClientUtility** is a modern, production-ready .NET HTTP client wrapper library that abstracts away boilerplate setup for HttpClient configuration in .NET 8-10 LTS applications. It provides enterprise-grade resilience patterns (Polly-integrated retry and circuit breaker policies), intelligent response caching, automatic correlation ID tracking, structured logging with rich context, and built-in OpenTelemetry observability—all accessible through a single `AddHttpClientUtility()` dependency injection call rather than requiring 50+ lines of manual setup code. The library is distributed as two focused NuGet packages: the core **WebSpark.HttpClientUtility** (163 KB) for standard HTTP operations with authentication and telemetry support, and **WebSpark.HttpClientUtility.Crawler** (75 KB) for web scraping scenarios with robots.txt parsing and sitemap generation capabilities.

The project demonstrates production-grade engineering practices including comprehensive automated test coverage across multiple .NET versions, Source Link debugging support, AOT and IL trimming readiness, zero-warning builds with strict code quality enforcement, semantic versioning compliance, and a zero-breaking-changes guarantee within major versions. It targets microservices architectures, background workers, and web scraping applications where developers need resilience and observability without framework complexity, positioning itself between minimal raw HttpClient setup and opinionated alternatives like Refit or RestSharp. The codebase is highly active (51 commits in 90 days) with consistent maintenance patterns, MIT licensed for commercial use, and backed by comprehensive GitHub Pages documentation and long-term LTS support aligned with Microsoft's .NET release cycles.

**Created**: 2025-05-03
**Last Modified**: 2026-03-17

---

### #6. [git-spark](https://github.com/markhazleton/git-spark)

Stars: 0 | Forks: 0 | Language: TypeScript | 28 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2012 KB | 🚀 9.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Git Spark - Technical Summary

**Git Spark** is a TypeScript-based Git repository analytics and reporting tool that analyzes commit history to generate interactive HTML dashboards and multi-format reports revealing contributor activity patterns, code change metrics, and development trends. The project provides both a CLI interface and Node.js API, allowing users to analyze repositories across configurable date ranges with features including contributor statistics, file-level change analysis, daily activity trends, and customizable export formats (HTML, JSON, CSV, Markdown). The tech stack leverages modern Node.js tooling with CLI support via Commander.js, terminal UI enhancements through Chalk and Ora spinners, and semantic versioning utilities, while the HTML reports employ security-first practices with Content Security Policy (SHA-256 hashed scripts), embedded analytics data for air-gapped workflows, and accessibility features including ARIA compliance and dark mode support. The codebase is organized with TypeScript (67.5%), PowerShell deployment scripts (16.3%), and embedded HTML templates (14.7%), targeting Node.js 20.19.0+ environments with a relatively modest dependency footprint of 19 packages. This tool is particularly valuable for engineering leaders, security auditors, and development teams seeking to understand repository health metrics, knowledge concentration risks, and governance signals without external API dependencies—making it suitable for enterprise environments with strict data residency or air-gapped deployment constraints. Despite zero current adoption (0 stars/forks), the project demonstrates active development with 28 commits in the last 90 days and comprehensive documentation including an interactive demo, though declining activity patterns suggest recent momentum changes.

**Technology Stack Currency**: ✅ 90/100
**Dependencies**: 19 total (14 current, 5 outdated)

**Created**: 2025-09-29
**Last Modified**: 2026-03-26

---

### #7. [TailwindSpark](https://github.com/markhazleton/TailwindSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 47 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 4687 KB | 🚀 15.7 commits/month

**Quality**: ❌ License | ✅ Docs

# TailwindSpark - Technical Summary

**TailwindSpark** is a production-ready, comprehensive Tailwind CSS design system and component showcase built as a modern React TypeScript monorepo. It demonstrates best practices in modern web development by combining React 19.1, TypeScript 5.9, Tailwind CSS 4.1, and Vite 7.1 into a fully-featured, accessible, and performant design system with interactive examples including dashboards, e-commerce flows, and marketing pages.

The project employs a Turborepo 2.7 monorepo architecture with shared packages for design tokens and reusable UI components, enabling efficient code organization and build optimization across multiple applications. Key features include a complete component library, WCAG 2.1 AA accessibility compliance with keyboard navigation support, dark mode with system preference detection, real-time Web Vitals monitoring, SEO optimization, and comprehensive testing infrastructure with Vitest and Jest-axe.

TailwindSpark stands out through its emphasis on development quality and production-readiness: 100% TypeScript with strict type checking, automated CI/CD pipelines via GitHub Actions, integrated performance monitoring, security scanning via CodeQL and Dependabot, and extensive accessibility testing throughout the codebase. The technology stack is cutting-edge with strong currency (React concurrent features, Tailwind CSS v4's @theme directive and CSS variables, modern tooling chains), and the project demonstrates advanced patterns like code splitting, lazy loading with Suspense, error boundaries, and intelligent service worker caching strategies.

Designed primarily for developers, designers, and organizations seeking a reference implementation of modern React architecture and design system practices, TailwindSpark serves as both a showcase of Tailwind CSS v4 capabilities and a solid foundation for building scalable, accessible, performant web applications with enterprise-grade tooling and quality standards.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2025-07-29
**Last Modified**: 2026-03-26

---

### #8. [RESTRunner](https://github.com/markhazleton/RESTRunner)

Stars: 2 | Forks: 1 | Language: C# | 38 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 1031 KB | 🚀 12.7 commits/month

**Quality**: ❌ License | ✅ Docs

# RESTRunner - Technical Summary

**RESTRunner** is a comprehensive .NET 10 (LTS) solution designed for executing, analyzing, and benchmarking REST API tests, with native support for importing and executing Postman collections at scale. The platform provides both a console application and interactive Razor Pages web interface, enabling developers and QA teams to perform automated regression testing, load testing, and performance analysis across multiple API instances with detailed statistical reporting and CSV export capabilities.

The project leverages modern .NET technologies (C# with MSTest v4 analyzers, HttpClientUtility for HTTP operations, and integrated Postman collection parsing) to deliver a multi-faceted testing toolkit that includes features such as response time percentile calculations, success rate metrics, configurable load testing parameters, and built-in sample CRUD APIs for demonstration purposes. The architecture appears to follow a layered design pattern with separate Domain, Web, and Console projects, enabling clean separation of concerns and testability—evidenced by comprehensive test coverage (21/21 tests passing with 100% pass rate) and a modular codebase spanning 1031 KB across C# (46.3%), HTML (35.1%), and PowerShell scripts (18.5%).

What distinguishes RESTRunner is its focus on **performance optimization and maintenance**, with the recent v10.0.0 upgrade delivering 19% faster builds (5.1s → 4.1s) and 25% faster test execution (0.8s → 0.6s) through strategic .NET 10 adoption, 93% of dependencies maintained at latest versions with zero security vulnerabilities, and comprehensive upgrade documentation. The project is actively maintained (38 commits in 90 days, 63 in 365 days) with a strong engineering culture defined in its engineering constitution, making it suitable for organizations requiring production-grade REST API testing, performance benchmarking, regression validation, and load testing capabilities in compliance-sensitive environments.

**Created**: 2021-09-30
**Last Modified**: 2026-03-26

---

### #9. [ReactSparkPortfolio](https://github.com/markhazleton/ReactSparkPortfolio)

Stars: 0 | Forks: 0 | Language: CSS | 31 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 44427 KB | 🚀 10.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: ReactSparkPortfolio

**ReactSparkPortfolio** is a production-ready, enterprise-grade developer portfolio application built with React 19, TypeScript, and Vite that serves as both a personal showcase and a comprehensive reference implementation for modern web development practices. The application demonstrates advanced frontend engineering with features including real-time SignalR chat with AI personalities, live weather integration with interactive Leaflet maps, dynamic RSS feed aggregation, and a searchable portfolio pulled from external sources—all deployed across Azure Static Web Apps and GitHub Pages with automated CI/CD pipelines.

The project leverages a sophisticated modern tech stack centered on **React 19 + TypeScript 5.9 + Vite 7.0** for the frontend, complemented by **Bootstrap 5.3 + custom SCSS**, **Axios** for HTTP communication, **React Router 7.7** for client-side navigation, and **SignalR 9.0** for real-time capabilities. The architecture follows a frontend-centric design pattern that orchestrates multiple external APIs (OpenWeather, JokeAPI, custom WebSpark backend) and implements responsive, accessible UI components with WCAG 2.1 AA compliance and dark/light theme switching.

What distinguishes this project is its **dual-deployment strategy** with intentionally permissive Content Security Policy (CSP) documentation, comprehensive TypeScript strict mode implementation across 46 dependencies, and extensive self-documentation including security guidelines, deployment patterns, and architectural diagrams. The codebase demonstrates professional development practices through modular component architecture, lazy loading with code splitting for performance optimization, semantic HTML with ARIA accessibility standards, and a highly active commit history (31 commits in 90 days) indicating ongoing maintenance and improvement, making it valuable for developers seeking production patterns for scalable React applications and cloud-native deployment strategies.

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

**KeyPressCounter** is a lightweight Windows system tray utility built in C# (.NET 10.0) that monitors keyboard and mouse input activity while simultaneously tracking real-time system performance metrics, running silently in the background without recording keystrokes or transmitting data. The application leverages SharpHook for global input hooking, Windows Performance Counters for CPU/memory/disk/network monitoring, and WMI (System.Management) for hardware interrogation, combining these capabilities into a three-tab statistics dashboard with persistent activity/summary logging and configurable idle-period filtering.

The architecture demonstrates solid Windows desktop application patterns: **CustomApplicationContext** manages the system tray integration and event lifecycle, **Counter** provides thread-safe metrics with per-interval peak tracking via lock-protected operations, **SystemPerformanceMonitor** abstracts seven performance counters with static hardware caching, and **StatsForm** renders real-time dashboards including 60-second anti-aliased GDI+ line graphs for CPU and memory trends. Key features include peak activity metrics (max keystrokes/clicks per minute), inactivity detection with configurable thresholds, top-10 process ranking by resource consumption, and dual logging streams (activity every 60 seconds + daily summary resets at midnight), all persisted to JSON configuration at `%APPDATA%\MWH.KeyPressCounter\config.json`.

What distinguishes KeyPressCounter is its privacy-first design—it counts inputs without storing identities or content—combined with comprehensive system monitoring in a single unobtrusive tray application, making it valuable for productivity tracking, workload analysis, and system health awareness without the data privacy concerns of keystroke loggers. The project exhibits mature maintenance patterns (6 commits in 90 days, single-instance enforcement, registry-based Windows startup integration) and targets Windows 10+ users seeking transparency into their input patterns and hardware utilization.

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

**SupportSpark** is a compassionate support network platform built with modern web technologies that enables people navigating life's challenging moments (health issues, transitions, personal journeys) to share updates with trusted circles through a role-based, invitation-only system. Members post journey updates while supporters read and respond in threaded conversations, solving the exhaustion of individually updating multiple people during difficult times.

The application employs a full-stack TypeScript architecture with **React 19 + Vite** frontend featuring accessible shadcn/ui components styled with Tailwind CSS 4, paired with an **Express 5** backend that handles authentication via Passport.js, server state management through TanStack React Query, and runtime type safety via Zod validation across shared TypeScript schemas. The project demonstrates strong architectural discipline with end-to-end type safety, a clear separation between client/server/shared code, and comprehensive documentation including deployment guidance—particularly notable is its Windows 11 + IIS production deployment strategy using iisnode and PowerShell automation.

Key distinguishing features include a **demo mode** with browser-based localStorage persistence (no backend required), a calming teal/sage UI design intentionally crafted for sensitive moments, and role-based access controls where members and supporters have distinctly different capabilities. The codebase shows active development (43 commits in 90 days with accelerating velocity), though with a tech currency score of 50/100 suggesting some dependencies may benefit from updates. Target users are individuals requiring discrete support coordination and their care networks—a niche but emotionally significant use case that differentiates it from generic social platforms.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 98 total (98 current, 0 outdated)

**Created**: 2026-02-01
**Last Modified**: 2026-03-29

---

### #12. [JsBootSpark](https://github.com/markhazleton/JsBootSpark)

Stars: 0 | Forks: 0 | Language: JavaScript | 22 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 3537 KB | 🚀 7.3 commits/month

**Quality**: ❌ License | ✅ Docs

# JsBootSpark — Technical Summary

**JsBootSpark is a production-ready, full-stack starter kit for building modern web applications, combining Express.js backend with Bootstrap 5 frontend and EJS templating.** The project provides a comprehensive foundation for developers to quickly scaffold responsive, feature-rich web applications with best practices built-in, including security middleware (Helmet.js), performance optimization (compression), and a modern development experience with hot-reload capabilities and SASS compilation. The technology stack integrates Express 5.1.0, Bootstrap 5.3.7, EJS 3.1.10, and Node.js 18+, along with supporting libraries for CSV parsing, data tables, and icon management (bootstrap-icons, bootstrap-table). Its architecture emphasizes deployment flexibility through multiple channels—GitHub Pages integration, Docker containerization, CI/CD pipelines, and static site generation—while supporting dynamic content generation from templates and CSV data sources for scalability. The project is distinguished by its comprehensive documentation spanning quick-start guides, developer resources, architectural decision records, and AI-assisted development sessions, making it particularly valuable for teams seeking both a rapid prototyping platform and a learning resource for modern full-stack JavaScript development patterns. Target users range from junior developers learning full-stack practices to experienced teams needing a well-structured, maintainable starter template with production-ready security, testing infrastructure, and deployment automation already configured.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 30 total (30 current, 0 outdated)

**Created**: 2022-06-06
**Last Modified**: 2026-01-31

---

### #13. [WebSpark](https://github.com/markhazleton/WebSpark)

Stars: 1 | Forks: 0 | Language: C# | 14 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 69023 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ❌ Docs

# WebSpark Technical Summary

**WebSpark** is a comprehensive .NET 9-based web application suite comprising three integrated tools—PromptSpark (LLM prompt optimization), RecipeSpark (recipe management), and TriviaSpark (quiz creation platform)—built on ASP.NET Core MVC with Bootstrap 5 styling. The platform implements a sophisticated modular architecture spanning seven functional areas (PromptSpark, RecipeSpark, TriviaSpark, WebCMS, AsyncSpark, Admin, Identity) that provides scalability and extensibility across distinct business domains. A standout feature is its **spec-driven development workflow** powered by SpecKit commands, which enforces rigorous specifications, implementation planning, task breakdown, and crucially, an adversarial risk assessment phase that catches showstopper issues, ASP.NET Core anti-patterns, security vulnerabilities, and performance killers before code implementation begins—significantly reducing production risk. The codebase demonstrates strong SEO optimization capabilities including dynamic meta tags, JSON-LD structured data, canonical URL management, XML sitemaps, multi-engine verification, Google Analytics 4 integration with custom dimensions, and Application Insights-based SEO audit logging, all supported by 47 passing test cases. This project targets developers and organizations seeking a well-architected, quality-focused web application platform with modern technologies (C#, HTML, SCSS, JavaScript) and a disciplined development governance model that prioritizes risk mitigation and specification compliance over rapid feature delivery.

**Created**: 2024-01-11
**Last Modified**: 2026-01-29

---

### #14. [WebProjectMechanics](https://github.com/markhazleton/WebProjectMechanics)

Stars: 3 | Forks: 0 | Language: Visual Basic .NET | 9 commits (90d)

👥 0 contributors | 🌐 10 languages | 💾 52407 KB | 🚀 3.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebProjectMechanics

**WebProjectMechanics** is a multi-tenant, multi-domain content management system undergoing a modernization effort, migrating a 20+ year legacy ASP.NET Web Forms/MS Access application to a contemporary .NET 9/SQLite architecture. The system manages 36+ domains from a single application instance through a plugin-based architecture that supports multiple content domains (CMS pages, mineral collections, recipes), with each tenant isolated via dedicated SQLite database files rather than logical tenant ID columns, and publishes all public content as pre-rendered static HTML served by Caddy for optimal performance and minimal infrastructure costs (~$10/month on Azure Linux).

The architecture emphasizes clean separation of concerns through layered modules—**WPM.Core** (shared contracts), **WPM.Infrastructure** (core services), domain-specific plugins (**CMS**, **Minerals**, **Recipes**), and an **ASP.NET Core Minimal API** host—with comprehensive infrastructure for data migration from the legacy system, automated testing via xUnit, and extensive architectural documentation detailing the greenfield implementation plan. Built on a modern tech stack including Entity Framework Core 9 for data access, Scriban for templating, GitHub Actions for CI/CD, and Caddy 2 for reverse proxying with automatic SSL, the project demonstrates cost-conscious infrastructure design and strong software engineering practices with clear phasing and documentation for a complex legacy modernization effort.

**Created**: 2017-09-19
**Last Modified**: 2026-02-19

---

### #15. [PromptSpark.Chat](https://github.com/markhazleton/PromptSpark.Chat)

Stars: 0 | Forks: 0 | Language: C# | 29 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 19200 KB | 🚀 9.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: PromptSpark.Chat

**PromptSpark.Chat** is a real-time conversational workflow application built on ASP.NET Core and SignalR that enables users to navigate multi-step interactive processes through a dynamic chat interface, with support for branching logic, Adaptive Cards for rich UI components, and optional AI-driven responses for out-of-workflow questions. The application employs a server-side state management architecture using thread-safe ConcurrentDictionary to persist conversation data across page refreshes, ensuring users can resume workflows without losing progress, while the frontend leverages SCSS, HTML, and JavaScript (9.1% of codebase) to provide responsive client-side interactions. Key architectural patterns include a modular service layer for workflow management and AI integration, Razor-based MVC views for templating, and SignalR hubs for bidirectional real-time communication between clients and servers, demonstrating clean separation of concerns. The project's technical uniqueness lies in its combination of workflow orchestration with Adaptive Cards—a structured, declarative UI standard—enabling both guided user flows and flexible branching paths without tight coupling to specific UI implementations. The codebase is notably recent (created December 2024) with accelerating activity (29 commits in 90 days), suggesting active development, and targets scenarios ranging from customer support workflows and guided onboarding processes to dynamic questionnaire systems that benefit from both deterministic workflow paths and AI-enhanced fallback handling. Developers looking to implement interactive, state-aware multi-step user experiences in .NET environments will find this project valuable as both a reference implementation and extensible foundation.

**Created**: 2024-12-31
**Last Modified**: 2026-03-30

---

### #16. [Texecon](https://github.com/markhazleton/Texecon)

Stars: 0 | Forks: 0 | Language: HTML | 23 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 2983 KB | 🚀 7.7 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: TexEcon

**TexEcon** is a modern static React application designed to deliver expert economic analysis and commentary on the Texas economy, deployed as a performant GitHub Pages site with a sophisticated build pipeline that integrates headless CMS content management. The project implements a hybrid architecture combining static site generation (SSG) with client-side routing, enabling SEO-optimized pre-rendered pages alongside progressive enhancement through Wouter-based navigation, while maintaining content freshness through automated build-time API integration with WebSpark CMS and fallback caching mechanisms. Built with React 19, TypeScript, Vite 7.1, and Tailwind CSS 4.1, the stack emphasizes type safety, development velocity, and performance optimization through tree-shaking, code splitting, and Core Web Vitals focus. The architecture employs a comprehensive build pipeline featuring content fetching, dynamic sitemap generation, static page rendering, and build ID-based cache busting to handle dynamic routes (team profiles, economic analyses) within GitHub Pages' static constraints. Notable design patterns include build-time content management with graceful degradation, structured data implementation for SEO, and environment-agnostic configuration supporting both custom domains and GitHub Pages base paths. This solution targets economic analysts, policymakers, and stakeholders seeking Texas economic insights who benefit from fast load times, excellent SEO ranking potential, and reliable content availability through intelligent fallback systems.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 37 total (37 current, 0 outdated)

**Created**: 2025-09-03
**Last Modified**: 2026-03-28

---

### #17. [react-native-web-start](https://github.com/markhazleton/react-native-web-start)

Stars: 0 | Forks: 0 | Language: PowerShell | 14 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2054 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: react-native-web-start

This is a **production-ready, enterprise-grade starter template** for building cross-platform applications that run on Web, iOS, and Android from a single TypeScript/React codebase using React Native Web, Vite, and modern tooling. The project leverages a monorepo structure (`packages/shared`, `packages/web`, `packages/mobile`) to maximize code reuse across platforms while providing platform-specific optimizations, with the shared layer containing all core components, services, and business logic that compile differently for web (via React Native Web) and native mobile (via React Native/Metro).

**Key capabilities** include Vite-powered HMR development for lightning-fast iteration, strict TypeScript configuration for type safety, Tailwind CSS with Sass preprocessing for responsive adaptive UI, in-app markdown documentation browser, built-in HTTP client with error handling, GitHub Pages CI/CD automation, and comprehensive build scripts for asset management and bundle optimization. The architecture uses Metro bundler for mobile, standard Vite for web, and implements code splitting, tree-shaking, and PWA-ready features for production deployments.

**Tech stack** centers on React 19.2.3, React Native 0.83.1, React Native Web 0.21.2, Vite 7.3.1, TypeScript 5.9.3, Tailwind CSS 4.1.18, and the Marked library for markdown rendering, demonstrating a modern, actively maintained technology choice (50/100 currency score indicates some dependencies could be fresher). The primary language is PowerShell (57.4%) reflecting build automation scripts, with TypeScript (20.8%), JavaScript (12.1%), HTML, and CSS comprising the application code.

Ideal for teams and developers seeking a **"write once, deploy everywhere" solution** who need to maintain consistent UI/UX across web and mobile platforms while minimizing code duplication, maintaining enterprise-grade code quality through TypeScript and linting, and rapidly iterating with Vite's development experience—particularly valuable for startups, agencies, and enterprises building cross-platform consumer applications or internal tools.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 49 total (49 current, 0 outdated)

**Created**: 2025-07-26
**Last Modified**: 2026-03-29

---

### #18. [sql2csv](https://github.com/markhazleton/sql2csv)

Stars: 0 | Forks: 0 | Language: C# | 6 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2078 KB | 🚀 2.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: sql2csv

**sql2csv** is a comprehensive .NET 10 toolkit designed for SQLite database manipulation and analysis, offering both command-line and web-based interfaces for discovering databases, exporting data, schema inspection, and C# code generation. The project follows a modular architecture with a shared core library (`Sql2Csv.Core`) that powers multiple frontends: a CLI application (`sql2csv.console`) for automation and scripting, an ASP.NET Core MVC web UI (`sql2csv.web`) with file upload and persistence capabilities, and an experimental data exploration app (`DataSpark.Web`). Key capabilities include bulk table-to-CSV export with filtering options, multi-format schema reporting (text/JSON/Markdown), automatic C# Data Transfer Object (DTO) generation from database schemas, and file management operations in the web interface, all supported by comprehensive test coverage (MSTest) and performance benchmarking (BenchmarkDotNet). The technology stack spans C# (54%), HTML/CSS/JavaScript for the frontend, and integrates Node.js tooling for web asset building, reflecting a full-stack approach to database introspection and data transformation. The project demonstrates mature engineering practices including CI/CD automation (GitHub Actions), code coverage tracking, and structured development workflows (CONTRIBUTING.md guidelines), making it particularly valuable for developers needing to reverse-engineer SQLite databases, migrate data to CSV formats, or generate strongly-typed models for C# applications without manual schema analysis.

**Created**: 2017-11-06
**Last Modified**: 2026-01-12

---

### #19. [InquirySpark](https://github.com/markhazleton/InquirySpark)

Stars: 0 | Forks: 0 | Language: C# | 4 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 9653 KB | 🚀 1.3 commits/month

**Quality**: ❌ License | ✅ Docs

# InquirySpark - Technical Summary

**InquirySpark** is a modern .NET 10 survey and inquiry management system that combines a Bootstrap 5-based MVC admin interface with Entity Framework Core 10 persistence using read-only SQLite databases, eliminating the need for SQL Server infrastructure. The solution is architecturally composed of modular layers—including an admin UI project, a repository/data access layer with EF Core abstractions, shared domain models, and a comprehensive MSTest unit test suite—all enforced with nullable reference types and XML documentation for type safety and maintainability. Its unique value proposition lies in its immutable, file-based SQLite approach with strict read-only mode enforcement, making it ideal for distributed survey applications where data integrity and portability are paramount without requiring heavyweight database servers. The tech stack spans C#, HTML, T-SQL, PowerShell, and TypeScript, with automated npm asset pipelines and DataTables integration providing a polished, responsive user interface without CDN dependencies. The project targets developers and organizations seeking lightweight, self-contained survey/inquiry platforms that can be deployed across multiple environments with minimal infrastructure overhead, particularly in scenarios where offline or distributed data persistence is beneficial. Though showing declining activity (4 commits in 90 days, 0 stars/forks), the codebase demonstrates mature engineering practices with comprehensive documentation, clear contribution guidelines, and well-organized specification tracking for ongoing feature development.

**Created**: 2023-10-24
**Last Modified**: 2026-03-30

---

### #20. [markhazleton](https://github.com/markhazleton/markhazleton)

Stars: 0 | Forks: 0 | Language: Unknown | 16 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 6603 KB | 🚀 5.3 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: markhazleton Repository

This repository serves as Mark Hazleton's personal portfolio and learning archive—a curated collection of technical projects documenting his continuous professional development across multiple technology domains. The repository showcases several featured initiatives, including **Spec-Kit-Spark** (a pragmatic fork of GitHub SpecKit for brownfield development) and **ReactSpark** (a React application built with Vite and deployed on Azure Static Web Applications), demonstrating expertise across full-stack development, cloud infrastructure, and framework implementation. The tech stack spans modern web technologies (React, Vite), cloud platforms (Azure DevOps, Azure Static Web Apps), .NET ecosystem (NuGet packages), and API development tools (RESTful services, Postman), with a focus on practical, production-ready solutions. The project emphasizes pragmatic software architecture and evolutionary development patterns, as evidenced by his published articles on framework adoption, API load testing (RESTRunner), and brownfield modernization strategies. The repository is notable for its integration of blogging, GitHub statistics visualization, and professional networking links, creating a comprehensive personal knowledge base that extends beyond code to include strategic insights on software governance, accountability, and outcome-focused development. This multi-faceted approach targets intermediate-to-senior software developers and architects seeking practical examples of modern development practices, cloud deployment patterns, and the methodological thinking behind building maintainable systems.

**Created**: 2021-04-17
**Last Modified**: 2026-03-20

---

### #21. [PHPDocSpark](https://github.com/markhazleton/PHPDocSpark)

Stars: 0 | Forks: 0 | Language: PHP | 6 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 2884 KB | 🚀 2.0 commits/month

**Quality**: ❌ License | ✅ Docs

# PHPDocSpark: Technical Summary

**PHPDocSpark** is a modern, open-source PHP documentation and data exploration platform designed as both a functional web application and a comprehensive reference implementation for contemporary PHP development practices. The project demonstrates hybrid architecture by combining traditional server-side PHP 8.2+ with a modern Vite-powered client-side build pipeline, creating a seamless integration of backend logic and optimized frontend assets.

The platform offers comprehensive content management capabilities including Markdown-based documentation with recursive directory scanning, full-text search with relevance scoring, and interactive data analysis tools featuring CSV parsing, DataTables integration, and Chart.js visualizations. It includes practical features such as GitHub API integration with caching strategies, SQLite database with CRUD operations, a contact management system, and responsive Bootstrap 5.3 UI with icon libraries—all served through a clean front-controller routing pattern with output buffering for template inheritance.

The technology stack emphasizes modern tooling and best practices: PHP with Parsedown for Markdown parsing, Vite 7.1+ for asset bundling with hot module replacement, Sass for advanced CSS preprocessing, ESLint/Prettier for code quality, and Azure Pipelines for CI/CD automation deployed to Azure Web Apps. The architecture is educationally-focused, serving as a reference implementation for developers learning PHP modernization patterns, API integration, caching optimization, and responsive design methodologies.

PHPDocSpark targets PHP developers exploring contemporary workflows, full-stack engineers interested in hybrid architectures, technical writers managing documentation platforms, and development teams seeking production-ready reference implementations. With 2.8MB codebase across 27 dependencies, active maintenance (6 commits in 90 days, accelerating activity), and dual deployment endpoints (Azure and canonical domain), it represents a well-structured, actively-maintained example of professional PHP application architecture suitable for both learning and real-world documentation management scenarios.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2023-09-08
**Last Modified**: 2026-03-30

---

### #22. [TeachSpark](https://github.com/markhazleton/TeachSpark)

Stars: 0 | Forks: 0 | Language: C# | 13 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 29808 KB | 🚀 4.3 commits/month

**Quality**: ❌ License | ✅ Docs

# TeachSpark - Technical Summary

**TeachSpark** is a modern, full-stack LLM-powered educational platform built with .NET 10 MVC on the backend and a contemporary webpack-based frontend, designed to deliver personalized, AI-driven learning experiences through intelligent content adaptation and real-time feedback. The architecture combines C# backend services (29.7% of codebase) with a sophisticated frontend stack leveraging HTML, CSS, and JavaScript (28.5%, 25.6%, and 2.2% respectively), integrated through a robust webpack 5 build system that provides hot module replacement, code splitting, and asset optimization for production deployments. Key technical differentiators include automated code quality enforcement via Husky and lint-staged pre-commit hooks, comprehensive analytics capabilities for progress tracking, and a responsive, modern UX built on Bootstrap 5 with SCSS styling pipelines—all orchestrated through clean architecture principles and Entity Framework Core for data persistence. The project demonstrates mature DevOps practices with ESLint, Prettier, and Stylelint configuration, automated pre-commit validation, and a well-documented webpack build system supporting multiple development modes (dev, watch, analyze). With 44 total commits over the past year and recent accelerating activity (13 commits in the last 90 days), the project targets educators and learners seeking an intelligent alternative to traditional learning management systems by leveraging large language models to dynamically personalize curriculum delivery based on individual learning patterns. The high tech stack currency score (90/100) and modern dependency ecosystem (.NET 10, Node.js 18+) position TeachSpark as a contemporary solution for adaptive education, appealing to institutions and platforms looking to integrate AI-powered personalization into their learning infrastructure.

**Technology Stack Currency**: ✅ 90/100
**Dependencies**: 3 total (2 current, 1 outdated)

**Created**: 2025-06-19
**Last Modified**: 2026-03-29

---

### #23. [markhazleton.github.io](https://github.com/markhazleton/markhazleton.github.io)

Stars: 0 | Forks: 0 | Language: SCSS | 1 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 152 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: markhazleton.github.io

This repository is Mark Hazleton's personal portfolio and blog website built with Jekyll, a static site generator, and hosted on GitHub Pages. The site features a customized Minima theme with dark/light mode toggle support, modern styling implemented through SCSS/CSS without external frameworks, and automated CI/CD deployment via GitHub Actions. The tech stack leverages Ruby 3.2.2 with Jekyll 3.10.0, integrated with key dependencies including github-pages for hosting compatibility and platform-specific gems like wdm for Windows file monitoring. The architecture follows Jekyll's conventional structure with separated concerns across layouts, includes, and Sass stylesheets, enabling maintainable content management through a straightforward Markdown-based post workflow with front matter configuration. The project demonstrates declining activity (1 commit in 90 days vs. 16 over a year) but maintains functional deployment automation, making it suitable for personal branding, technical blogging, and portfolio showcasing. This template is ideal for developers seeking a lightweight, dependency-light alternative to JavaScript-heavy static site generators, with particular appeal to those already familiar with Ruby or GitHub's hosting ecosystem.

**Technology Stack Currency**: ✅ 56/100
**Dependencies**: 3 total (2 current, 1 outdated)

**Created**: 2021-04-18
**Last Modified**: 2026-01-12

---

### #24. [FastEndpointApi](https://github.com/markhazleton/FastEndpointApi)

Stars: 2 | Forks: 1 | Language: HTML | 1 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 137 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: FastEndpointApi Repository

## Overview
FastEndpointApi is an educational demonstration project showcasing the FastEndpoints framework—a lightweight, high-performance REST API framework for ASP.NET Core that implements the REPR (Request-Endpoint-Response) pattern. The project features a complete Person Management API with CRUD operations, serving as a practical guide for developers learning to build clean, maintainable APIs with minimal boilerplate code.

## Key Features & Capabilities
The repository demonstrates comprehensive REST API patterns including full CRUD operations on Person entities, an in-memory data store for simplicity, smart request/response mapping, dependency injection integration, reusable base endpoint classes, HATEOAS hypermedia links, and interactive Swagger/OpenAPI documentation. The project includes both backend API endpoints and interactive frontend HTML pages for testing, with static HTML UI samples for index, documentation, and testing interfaces.

## Technology Stack & Architecture
Built on .NET 10.0 with FastEndpoints 7.1.1 as the core framework, the project leverages FastEndpoints.Swagger for API documentation, Bogus for realistic test data generation, and Bootstrap 5.3.3 for frontend UI. The architecture follows clean separation of concerns with a service layer abstraction, dependency injection patterns, and the REPR architectural pattern that contrasts with traditional MVC and Minimal APIs approaches.

## Unique Characteristics
The repository stands out by providing production-ready code patterns deployed to Azure Web Apps with an active CI/CD pipeline via GitHub Actions, offering both a fully functional demo and a detailed learning resource. The inclusion of HATEOAS implementation, comprehensive documentation linked to a detailed article, and static HTML test pages makes it exceptionally accessible for developers new to FastEndpoints.

## Target Audience & Use Cases
This project is ideal for ASP.NET Core developers seeking to streamline API development, those evaluating FastEndpoints as an alternative to Minimal APIs or MVC controllers, and teams interested in adopting REPR pattern principles. It serves both as a reference implementation and hands-on learning tool, with a live Azure-hosted demo enabling immediate experimentation without local setup.

**Created**: 2024-04-06
**Last Modified**: 2026-01-12

---

### #25. [MechanicsOfMotherhood](https://github.com/markhazleton/MechanicsOfMotherhood)

Stars: 0 | Forks: 0 | Language: TypeScript | 14 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 6719 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Mechanics of Motherhood

**Mechanics of Motherhood** is a modern, production-ready recipe management and discovery platform built as a Progressive Web Application (PWA) specifically designed for busy working mothers. The application serves as a curated recipe portal featuring 108+ recipes across 14 categories with smart search, filtering, ratings, and nutritional information, accessible via a custom domain at mechanicsofmotherhood.com with a GitHub Pages fallback.

The project leverages a contemporary React 19 + TypeScript frontend built with Vite, styled using Tailwind CSS and Shadcn/ui components, and powered by TanStack React Query for efficient server state management and offline caching capabilities. The architecture integrates real-time data from two APIs—RecipeSpark (recipe data) and WebCMS (content management)—with automated fallback to mock data, ensuring robust offline functionality and graceful degradation. Key technical achievements include mobile-first responsive design optimized for low-bandwidth networks, WCAG accessibility compliance, automated CI/CD deployment via GitHub Actions, SEO optimization with structured data and dynamic sitemaps, and performance metrics exceeding 95 Lighthouse scores with sub-3-second build times.

The project employs a sophisticated data quality pipeline with automated validation scripts, custom DNS and SSL configuration, and strategic code-splitting resulting in a gzipped bundle size of approximately 130KB, demonstrating attention to performance optimization critical for mobile users. The monolithic single-page application (SPA) pattern with Wouter routing eliminates backend infrastructure complexity while the TypeScript-first approach (53.2% of codebase) ensures type safety across the entire stack, complemented by supporting build automation scripts written in PowerShell. This is an actively maintained, well-architected example of a niche-focused web application that combines modern development practices with practical UX considerations for its target demographic.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 42 total (42 current, 0 outdated)

**Created**: 2025-09-01
**Last Modified**: 2026-03-09

---

### #26. [DataAnalysisDemo](https://github.com/markhazleton/DataAnalysisDemo)

Stars: 0 | Forks: 0 | Language: Visual Basic .NET | 0 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 12992 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: DataAnalysisDemo (DAWPM)

**DataAnalysisDemo** is a comprehensive web-based analytics platform built on ASP.NET WebForms 4.8 that transforms CSV data files into interactive visualizations, pivot tables, and statistical analyses. The application serves as a sophisticated data exploration tool, enabling users to upload CSV files and dynamically generate column statistics, customizable charts (15+ types), drag-and-drop pivot tables with multiple aggregation functions, and advanced data tables with search/filtering capabilities. The tech stack combines a legacy ASP.NET backend (VB.NET) with a modern frontend architecture using Bootstrap 5.3.8, jQuery 3.7.1, DataTables 2.3.3, D3.js, and C3.js for visualizations, alongside a contemporary Webpack-based build system for client-side asset bundling and npm dependency management. The architecture demonstrates a hybrid approach—leveraging WebForms for server-side logic while implementing modern ES6+ JavaScript, responsive design patterns, and a structured webpack pipeline to overcome traditional ASP.NET limitations. Key differentiators include the custom GenericParser library for efficient CSV processing, a theme system with dynamic Bootstrap theme switching, state management for pivot configurations via localStorage, and performance monitoring built into the analytics engine, making it well-suited for business analysts, data scientists, and organizations needing rapid exploratory data analysis without heavy ETL tools. Despite minimal recent activity (declining commit history over 90 days), the project maintains a relatively current tech stack score of 77/100 and represents a practical demonstration of modern data visualization patterns in legacy enterprise frameworks.

**Technology Stack Currency**: ✅ 77/100
**Dependencies**: 24 total (10 current, 14 outdated)

**Created**: 2023-04-20
**Last Modified**: 2025-12-03

---

### #27. [ConcurrentProcessing](https://github.com/markhazleton/ConcurrentProcessing)

Stars: 0 | Forks: 0 | Language: C# | 2 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 145 KB | 🚀 0.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: ConcurrentProcessing

**ConcurrentProcessing** is a demonstration framework for .NET 10 that provides a production-ready, high-performance concurrent task processing engine built on semaphore-based throttling and the Task Parallel Library (TPL). The project showcases advanced C# concurrent programming patterns through a generic, extensible `ConcurrentProcessor<T>` abstract base class that enables developers to implement custom parallel workloads with fine-grained control over concurrency limits, automatic performance metrics collection, and detailed statistical analysis of task execution times, wait periods, and throughput. The architecture employs well-established design patterns—including Template Method for customization, Factory Pattern for task ID generation, and Resource Pool Pattern for semaphore management—to provide a type-safe, reusable framework that scales efficiently from single-digit to 1000+ concurrent tasks. Key differentiators include built-in performance telemetry with min/max/average calculations, minimal memory overhead optimized for .NET 10 runtime, and comprehensive documentation coupled with an educational blog article that makes it valuable for learning concurrent programming fundamentals alongside production scenarios. The project targets C# developers seeking to understand concurrent programming best practices, implement scalable batch processing systems, or leverage modern language features (C# 12+) in real-world applications, with a maintained but gradually declining commit activity pattern suggesting a stable, feature-complete state.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 2 total (2 current, 0 outdated)

**Created**: 2023-09-18
**Last Modified**: 2026-01-22

---

### #28. [WebSpark.ArtSpark](https://github.com/markhazleton/WebSpark.ArtSpark)

Stars: 0 | Forks: 0 | Language: C# | 7 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3658 KB | 🚀 2.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.ArtSpark

**WebSpark.ArtSpark** is a comprehensive .NET 10.0 solution that provides complete client library coverage for the Art Institute of Chicago's public REST API, encompassing all 33 endpoints across 6 major resource categories (Collections, Shop, Mobile, Publications, etc.). The solution consists of four interconnected projects: a strongly-typed async API client library with IIIF image support and Elasticsearch integration, an innovative AI agent system featuring multiple personas (Artwork, Artist, Curator, Historian) powered by OpenAI's GPT-4o with vision capabilities and hot-reloadable prompt configuration, an interactive ASP.NET Core web demo application with user authentication and personal collection management, and a command-line utility for developer access. The architecture emphasizes modern .NET practices including System.Text.Json deserialization with proper naming policies, async/await patterns throughout, minimal external dependencies, and separation of concerns across projects, while the AI components add conversational intelligence with persistent chat history, visual analysis, and content filtering guardrails. The primary use cases are developers integrating Art Institute data into applications, museum enthusiasts exploring artworks through AI-powered conversations, and organizations seeking a reference implementation of clean .NET architecture with AI integration. While currently unmaintained (declining activity with only 7 commits in the last 90 days), the project demonstrates sophisticated integration of REST APIs, machine learning services, and enterprise web application patterns, making it valuable both as a practical tool and educational reference for advanced .NET development.

**Created**: 2023-01-30
**Last Modified**: 2026-01-12

---

### #29. [AsyncSpark](https://github.com/markhazleton/AsyncSpark)

Stars: 0 | Forks: 0 | Language: C# | 9 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 1925 KB | 🚀 3.0 commits/month

**Quality**: ❌ License | ✅ Docs

# AsyncSpark - Technical Summary

AsyncSpark is a production-ready reference implementation demonstrating enterprise-grade async/await patterns in .NET 10, designed to serve as both a learning resource and architectural blueprint for modern asynchronous programming. The project implements eight core async patterns—including ConfigureAwait(false) usage, CancellationToken threading, Task.WhenAll parallelization, SemaphoreSlim throttling, Polly resilience policies, decorator-based cross-cutting concerns, and fire-and-forget safety mechanisms—with each pattern fully documented, tested (80% code coverage enforced), and linked to production code examples.

The repository enforces a novel "constitution-driven development" approach using formalized coding standards, automated compliance auditing, and SpecKit agents that validate pull requests and perform codebase audits against architectural principles. Built on ASP.NET Core with .NET 10 features (nullable reference types, primary constructors, file-scoped namespaces), the application provides interactive API documentation via Scalar (OpenAPI 3.1), integrates real-world external API patterns through OpenWeatherMap service integration, and demonstrates resilience patterns including retry policies, timeouts, and circuit breakers.

Key technologies include C# with MSTest + Moq for testing, dependency injection via ASP.NET Core's built-in container, Azure Web Apps for deployment, and GitHub Actions for CI/CD with automated constitution compliance checks. The architecture emphasizes clean design principles through interface-based services, decorator pattern implementation for telemetry and cross-cutting concerns, and strict enforcement of async best practices (no .Result/.Wait() blocking calls, proper CancellationToken propagation throughout call chains).

AsyncSpark is uniquely positioned as both an educational platform for learning advanced async patterns and a governance framework demonstrating how to enforce architectural standards at scale through automated auditing and CI/CD validation. It targets enterprise developers, architects designing async-first systems, and teams seeking to establish constitution-driven development practices, offering a live demo at asyncspark.azurewebsites.net alongside comprehensive documentation, audit reports, and code examples.

**Created**: 2022-08-07
**Last Modified**: 2026-02-10

---

### #30. [WebSpark.Bootswatch](https://github.com/markhazleton/WebSpark.Bootswatch)

Stars: 0 | Forks: 0 | Language: HTML | 5 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7124 KB | 🚀 1.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.Bootswatch

**WebSpark.Bootswatch** is a .NET 10-exclusive Razor Class Library that provides seamless integration of Bootswatch themes into ASP.NET Core applications, enabling dynamic theme switching and light/dark mode support with built-in caching mechanisms. The library abstracts Bootstrap 5's theming complexity through extension methods and tag helpers (e.g., `<bootswatch-theme-switcher />`), allowing developers to implement responsive, modern UI themes with minimal configuration while maintaining comprehensive error handling and fallback strategies. Built primarily with HTML (63.8%), C# (28.6%), and supporting PowerShell/JavaScript utilities, the project follows a modern dependency-focused architecture that prioritizes latest-generation packages and security patches over broad framework compatibility—a deliberate design choice reflected in version 2.0's exclusive .NET 10 targeting and deprecation of .NET 8/9 support. The library leverages the `StyleCache` service for high-performance CSS delivery and integrates with `WebSpark.HttpClientUtility` as a core dependency, demonstrating a modular ecosystem approach to shared utilities. Key architectural patterns include service injection through extension methods, caching abstractions, and tag helper encapsulation, making it production-ready for enterprise ASP.NET Core applications requiring flexible, performant theming without heavy manual configuration. This project is particularly valuable for development teams needing rapid theme deployment across multiple ASP.NET Core applications while maintaining performance standards and staying aligned with current .NET framework evolution.

**Created**: 2022-08-24
**Last Modified**: 2026-01-12

---

### #31. [WebSpark.PrismSpark](https://github.com/markhazleton/WebSpark.PrismSpark)

Stars: 0 | Forks: 0 | Language: C# | 14 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 2272 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ✅ Docs

# WebSpark.PrismSpark - Technical Summary

**WebSpark.PrismSpark** is a high-performance C#/.NET port of the popular PrismJS syntax highlighting library, designed to provide server-side code tokenization, syntax highlighting, and theming for .NET applications with support for 24 programming languages (C#, Python, JavaScript, Rust, Go, and more). The project leverages a modular architecture featuring a comprehensive plugin system (line numbers, copy-to-clipboard, toolbars), event-driven hooks for customization, and a flexible theme engine with built-in CSS generation, all optimized for async processing and caching to handle large-scale code highlighting efficiently. Built for .NET 10.0 LTS with backward compatibility to .NET 9.0, it integrates seamlessly into ASP.NET MVC/Razor applications through dependency injection and includes advanced features such as line-specific highlighting, custom CSS classes, and context metadata preservation. The codebase demonstrates strong software engineering practices with a comprehensive 52-test MSTest suite covering grammars, tokenization, and integration scenarios, while the interactive demo web application provides real-time syntax highlighting, a live code editor with validation and formatting, and language-specific showcases. PrismSpark differentiates itself by bringing Prism's powerful, extensible JavaScript highlighting capabilities to server-side .NET environments, eliminating the need for client-side JavaScript execution and enabling better performance, security, and integration with enterprise .NET applications—making it ideal for documentation generators, code review platforms, blog engines, and any .NET application requiring sophisticated syntax highlighting.

**Created**: 2025-05-27
**Last Modified**: 2026-02-11

---

### #32. [TaskListProcessor](https://github.com/markhazleton/TaskListProcessor)

Stars: 0 | Forks: 0 | Language: C# | 3 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 1070 KB | 🚀 1.0 commits/month

**Quality**: ❌ License | ✅ Docs

# TaskListProcessor - Technical Summary

**TaskListProcessor** is an enterprise-grade .NET 10.0 library designed to orchestrate complex asynchronous operations with sophisticated fault tolerance, observability, and task coordination capabilities. Built as a production-ready framework, it provides developers with a comprehensive solution for managing concurrent task execution through advanced patterns including circuit breakers, dependency injection, priority-based scheduling, and topological task dependency resolution. The library implements modern architectural patterns (decorator pattern, interface segregation, SOLID principles) with native integration for OpenTelemetry telemetry, Microsoft.Extensions.Logging, and structured logging frameworks like Serilog, enabling enterprise-grade monitoring and diagnostics in high-throughput systems.

Key distinguishing features include type-safe result handling with comprehensive error categorization, lock-free concurrent collections for thread-safe operations, object pooling for memory optimization, and support for streaming results via async enumerables for real-time processing. The project demonstrates mature software engineering practices with extensive documentation spanning quick-start guides, intermediate tutorials on DI/circuit breakers/scheduling, advanced optimization topics, performance benchmarks, and health check capabilities suitable for microservice architectures. Written primarily in C# (94.4%) with auxiliary PowerShell and Python scripts, the actively maintained codebase (31 commits annually) targets developers building resilient, observable distributed systems, API aggregators, workflow orchestrators, and data processing pipelines where fault isolation and operational visibility are critical requirements.

**Created**: 2023-11-09
**Last Modified**: 2026-01-12

---

### #33. [DocSpecSpark](https://github.com/markhazleton/DocSpecSpark)

Stars: 0 | Forks: 0 | Language: Python | 2 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 181 KB | 🚀 0.7 commits/month

**Quality**: ❌ License | ✅ Docs

# DocSpecSpark – Technical Summary

DocSpecSpark is a document-first framework and CLI tool that automates the initialization and management of company documentation repositories by rendering markdown documents from reusable, profile-specific templates and publishing them as static sites with versioned release bundles. The project provides a complete pipeline—from bootstrap scaffolding through build, preview, and publication—with profile-aware template catalogs (supporting nonprofit, startup, manufacturing, enterprise, and healthcare verticals) that configure documentation structure via YAML constitution files and guarantee consistent documentation quality across organizations of varying sizes and sectors.

Built primarily in Python with a modern CLI stack (Typer for command interface, Rich for terminal output, markdown-it-py for rendering, and PyYAML for configuration), DocSpecSpark employs a filesystem-backed template architecture where the framework payload (`.DocSpecSpark/`) is bundled into initialized repositories, enabling offline operation and decoupled evolution of documentation standards from the CLI tool itself. The architecture separates concerns through distinct CLI commands (`init`, `create`, `build`, `serve`, `publish`) that operate on workspaces, with GitHub Actions integration for automated publication to GitHub Pages and a release packaging system that snapshots versioned documentation as distributable archives.

The framework is particularly notable for its profile-driven approach—rather than offering generic templates, it selects and configures template sets based on organizational context (defined during `docspec init`), allowing the tool to scale from small businesses to large enterprises while maintaining sensible defaults aligned with domain-specific practices. Target users include technical teams, documentation leads, and DevOps engineers seeking to standardize and automate company documentation workflows, reduce boilerplate authoring, and establish a single source of truth with versioned release bundles and consistent publishing pipelines.

**Technology Stack Currency**: ✅ 67/100
**Dependencies**: 4 total (1 current, 3 outdated)

**Created**: 2026-03-07
**Last Modified**: 2026-03-08

---

### #34. [HttpClientDecoratorPattern](https://github.com/markhazleton/HttpClientDecoratorPattern)

Stars: 0 | Forks: 0 | Language: HTML | 1 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 2675 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: HttpClientDecoratorPattern Repository

## Overview
This repository is a production-ready implementation of the Decorator Design Pattern applied to .NET's HttpClient, designed to enhance HTTP operations with cross-cutting concerns like telemetry, caching, and resilience without modifying core client code. It serves as both a reference implementation and live demonstration of the **WebSpark.HttpClientUtility** NuGet package, providing enterprise-grade patterns for robust HTTP communication in .NET 10 applications.

## Key Features & Capabilities
The project implements a sophisticated decorator chain architecture featuring:
- **Telemetry & Observability**: Automatic request/response timing, correlation ID propagation, structured logging, and performance metrics
- **Performance Optimization**: Configurable memory caching with hit/miss tracking, response size monitoring, and SemaphoreSlim-based concurrency control
- **Resilience Patterns**: Circuit breaker implementation, exponential backoff retry policies, timeout management, and full Polly integration
- **Interactive Demo UI**: Real-time Bootswatch theme switching, responsive design, and multiple example integrations (Joke API, NASA APOD, Art Institute, circuit breaker demonstrations)

## Technology Stack & Architecture
Built with **C# (.NET 10)**, **HTML/CSS/JavaScript**, and leveraging **Polly** for resilience policies, the architecture employs a layered decorator pattern where each decorator wraps an `IHttpRequestResultService` interface to compose functionality—base HTTP service → Polly decorator → Telemetry decorator → Cache decorator. The implementation uses dependency injection throughout and includes a live Azure-hosted demonstration with SignalR support for real-time updates.

## Design Significance
The Decorator Pattern approach solves traditional HttpClient enhancement challenges by adhering to SOLID principles—enabling dynamic behavior addition, clean separation of concerns, high testability through DI, and maintainable code composition. The strongly-typed `HttpRequestResult<T>` container provides comprehensive request/response metadata including cache status, duration, size, correlation IDs, and status codes, making observability and debugging straightforward.

## Target Use Cases
This project is ideal for enterprise developers building distributed systems requiring robust HTTP clients with monitoring, resilience, and performance optimization; it provides both educational value as a design pattern reference and practical utility through its reusable NuGet package. The live demo and extensive documentation make it valuable for teams implementing microservices, API integrations, or systems requiring production-grade resilience patterns.

**Created**: 2023-02-09
**Last Modified**: 2026-01-12

---

### #35. [Yelp.Api](https://github.com/markhazleton/Yelp.Api)

Stars: 0 | Forks: 0 | Language: C# | 1 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 462 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: Yelp.API

**Yelp.API** is a C# class library that provides a managed wrapper around Yelp's v3 Fusion API, enabling .NET developers to seamlessly integrate local business search and review functionality into their applications targeting .NET 6 and later frameworks. The library abstracts the complexity of REST API calls to Yelp's backend, offering both simplified convenience methods (e.g., `SearchBusinessesAllAsync()`) and advanced query capabilities through structured `SearchRequest` objects, allowing developers to search millions of businesses across 32 countries with support for filtering by location, search terms, result limits, and operational status. Built primarily in C# (53.1%) with supplementary web assets (CSS, HTML, JavaScript), the project demonstrates a clean separation of concerns with a client-based architecture that handles authentication via API key injection and asynchronous operations for non-blocking I/O. The codebase employs modern async/await patterns and appears to follow standard .NET library conventions with organized model classes for request/response handling, making it accessible for both simple and complex business discovery scenarios. While currently unmaintained (zero recent activity over 90+ days), the library targets developers building .NET applications requiring Yelp business intelligence, review data, and location-based search functionality—useful for applications in travel, food delivery, local commerce, and business intelligence domains. The straightforward integration API and credential management approach via .NET secrets management make it a practical choice for teams already invested in the Microsoft development ecosystem.

**Created**: 2022-08-10
**Last Modified**: 2026-01-12

---

### #36. [DecisionSpark](https://github.com/markhazleton/DecisionSpark)

Stars: 0 | Forks: 0 | Language: C# | 14 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 519 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: DecisionSpark

DecisionSpark is a sophisticated .NET 10 web application that implements a conversational decision routing engine—essentially an intelligent system for guiding users through minimal, targeted questions to reach optimal recommendations based on configurable rules. The project combines a RESTful API with an interactive Razor Pages web interface, enabling both programmatic and user-friendly access to dynamic decision-making workflows that require no code modifications to adapt to new scenarios.

The architecture leverages several key technologies and patterns: **OpenAI integration** for natural language question generation and answer parsing, **Serilog** for structured logging, **Swagger/OpenAPI** for API documentation, and a **config-driven design** using JSON-based decision specifications that define questions, rules, traits, and outcomes. Core components include a SessionStore for conversation persistence, RoutingEvaluator for rule-based outcome determination, TraitParser for extracting structured data from natural language responses, and QuestionGenerator for dynamic prompt creation—allowing the engine to adapt questioning strategies without hardcoding logic.

The system is particularly well-suited for decision support applications such as recommendation engines (technology stack selection, activity planning), guided troubleshooting flows, and domain-specific advisors where minimal user input should yield optimal suggestions. The file-based session management and modular service architecture make it scalable and suitable for both small deployments and enterprise scenarios, while the comprehensive API documentation and interactive web UI lower barriers to integration and testing for developers and stakeholders alike.

**Created**: 2025-10-29
**Last Modified**: 2025-12-27

---

### #37. [TriviaSpark](https://github.com/markhazleton/TriviaSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 27238 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# TriviaSpark - Technical Summary

**TriviaSpark** is a multiplayer trivia game application developed as an experimental project using ChatGPT assistance, designed to integrate with public Trivia APIs to deliver competitive gaming experiences across web and mobile platforms. The application is built primarily with **C# (.NET)** for backend logic (61.1%), complemented by **HTML, CSS, and JavaScript** (26.5%, 12.3%, and 0.1% respectively) for frontend presentation, suggesting an ASP.NET or Blazor-based architecture with traditional web technologies. Core features include user registration and authentication systems, a leaderboard ranking system for competitive gameplay, admin-level question database management, and a customizable UI designed to support both web and mobile clients while maintaining a modern, interactive interface. The application follows a standard multi-tier web application pattern, consuming external Trivia APIs to populate dynamic question sets and managing user sessions, scores, and rankings through backend persistence. The project is notable as a case study in AI-assisted development, demonstrating ChatGPT's capability to scaffold functional applications while targeting a broad demographic (ages 18-95) of tech-savvy trivia enthusiasts seeking competitive gaming experiences. However, the repository shows minimal recent activity (zero commits in 90 days, declining engagement), suggesting the project may be in maintenance mode or has stalled in active development despite its ambitious scope covering both web and mobile deployment targets.

**Created**: 2023-02-22
**Last Modified**: 2025-12-02

---


---

## Report Metadata

- **Generation Time**: 6.6 seconds
- **SVGs Generated**: 6/6
- **Total API Calls**: 0
- **Total AI Tokens**: 90,944
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
*Last updated: 2026-03-30*