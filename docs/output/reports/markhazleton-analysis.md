# GitHub Profile: markhazleton

**Generated**: 2026-03-29 14:59:26 UTC
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

👥 0 contributors | 🌐 5 languages | 💾 12087 KB | 🚀 61.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: github-stats-spark

## Repository Overview

**github-stats-spark** is a comprehensive GitHub analytics and visualization platform that automatically generates beautiful SVG profile statistics and AI-powered repository analysis reports. The project combines automated data collection via the GitHub API, intelligent visualization generation, and Claude AI integration to transform raw GitHub activity into actionable insights and professional-grade visualizations that developers can embed in their profiles.

## Core Functionality

The system operates across three primary domains:

1. **SVG Profile Statistics Generator**: Automatically creates embeddable SVG visualizations including contribution heatmaps, language breakdowns, commit streaks, and a proprietary "Spark Score" (0-100 metric weighing consistency 40%, volume 35%, and collaboration 25%). Updates run nightly via GitHub Actions.

2. **AI-Powered Repository Analysis**: Leverages Claude Haiku to generate technical summaries for analyzed repositories with a 97%+ success rate, implementing a three-tier fallback system (Claude → README extraction → metadata). Implements intelligent ranking combining popularity (30%), activity with time-decay analysis (45%), and health signals (25%).

3. **Interactive Mobile-First Dashboard**: A responsive web interface deployed via GitHub Pages featuring repository comparison tools, "needs attention" ranking based on security alerts and staleness metrics, Chart.js visualizations, and WCAG 2.1 AA accessibility compliance with target <2s First Contentful Paint on 3G connections.

## Technical Architecture

Built with **Python 3.11+** as the primary backend language, the project utilizes PyGithub for API interactions, svgwrite for SVG generation, and PyYAML for configuration management. The frontend comprises JavaScript, HTML, and CSS with responsive design patterns optimized for mobile viewports (320px-768px). Key technical features include intelligent API rate-limit handling with exponential backoff, IndexedDB caching for offline support, and modular architecture enabling extensibility.

## Distinguishing Characteristics

**github-stats-spark** differentiates itself through several innovations: the composite "Spark Score" metric that uniquely balances multiple dimensions of developer activity, schema versioning (currently 2.2.0) that tracks dependency coverage and maintenance attention signals, and sophisticated time-decay algorithms for activity weighting. The mobile-first dashboard implements native interaction patterns (bottom-sheet navigation, swipe gestures) while maintaining accessibility standards, and the three-tier AI summarization fallback ensures consistent output quality across repositories with varying documentation completeness.

## Use Cases & Target Audience

Designed for developers showcasing GitHub portfolios professionally, technical leads analyzing team productivity patterns, open-source maintainers tracking project momentum, and teams evaluating repository health at scale. The automated GitHub Actions workflow and zero-maintenance design appeal to developers seeking professional-grade analytics without ongoing operational overhead.

**Activity Assessment**: Highly active (184 commits/90d, accelerating pattern) with recent updates, though the repository's creation date anomaly (2025-12-28) suggests metadata inconsistency. Tech stack currency scores 69/100, indicating solid but not cutting-edge dependency currency.

**Technology Stack Currency**: ✅ 69/100
**Dependencies**: 10 total (1 current, 9 outdated)

**Created**: 2025-12-28
**Last Modified**: 2026-03-29

---

### #2. [mark-hazleton-s-notes](https://github.com/markhazleton/mark-hazleton-s-notes)

Stars: 0 | Forks: 0 | Language: TypeScript | 131 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 297052 KB | 🚀 43.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: mark-hazleton-s-notes

This repository is a full-featured personal technical blog and portfolio site for Mark Hazleton, a Solutions Architect, built with a modern React and TypeScript stack (React 19, Vite 7, Tailwind CSS, shadcn/ui, Radix UI) and deployed to Azure Static Web Apps. The site combines long-form technical content on cloud architecture and engineering practices with a dynamic project portfolio, live GitHub repository metrics, YouTube video integration, and comprehensive SEO assets (sitemaps, RSS/Media RSS feeds with optimized images, Open Graph metadata). The architecture employs a sophisticated multi-stage build pipeline that includes Markdown-to-JSON content generation, static site prerendering via SSR, image optimization (WebP conversion, thumbnail generation), and remote data fetching (GitHub stats from a separate repository) to keep metrics fresh without client-side API calls. Key architectural patterns include content separation (Markdown files with YAML frontmatter), build-time data aggregation, static output generation to a `docs/` directory, and a fallback strategy for development environments that fetch remote JSON when local files aren't available. The project stands out for its production-grade content infrastructure—supporting RSS feeds with Media RSS namespace, video sitemaps, repository detail pages with live metrics, and automated image optimization—making it suitable as both a personal brand platform and a reference implementation for building content-rich, SEO-optimized static sites with React. The codebase is highly active (131 commits in both 90 and 365-day windows with accelerating velocity) and includes extensive developer documentation, making it valuable for engineers seeking patterns for combining JAMstack principles with real-time data integration and complex content workflows.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 60 total (60 current, 0 outdated)

**Created**: 2026-01-10
**Last Modified**: 2026-03-20

---

### #3. [MuseumSpark](https://github.com/markhazleton/MuseumSpark)

Stars: 0 | Forks: 0 | Language: Python | 74 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 23233 KB | 🚀 24.7 commits/month

**Quality**: ❌ License | ✅ Docs

# MuseumSpark - Technical Summary

**MuseumSpark** is an intelligent travel planning platform that transforms the Walker Art Center Reciprocal Program membership into a data-rich museum discovery and itinerary optimization tool for art enthusiasts across North America. The project curates 1,269+ museums through a sophisticated multi-phase enrichment pipeline that combines data from Wikidata, Wikipedia, museum websites, and expert scoring to provide priority-ranked recommendations based on collection strength, historical context, and reputation. The architecture employs a hybrid static/dynamic approach with a modern React 19 + Vite frontend hosted on GitHub Pages for current phases, paired with a robust Python 3.11+ backend pipeline using Pydantic for schema validation, BeautifulSoup for web scraping, and JSON Schema for data quality assurance. The platform's unique value proposition lies in its "Never Replace Known With Null" data governance principle and progressive enrichment methodology—currently at 0.08% completion—that systematically layers contextual data through nine distinct phases before calculating priority scores and enabling AI-assisted personalization in Phase 4. Target users are art lovers seeking strategic museum visits with time constraints, from 2-hour layover discoveries to weekend art tours, with planned features including user authentication, favorite tracking, itinerary generation, and Claude/OpenAI-powered travel recommendations launching in Q4 2026. The project demonstrates deliberate architectural planning, having recently accelerated to 74 commits in 90 days while maintaining transparent progress dashboards and rigorous data validation throughout its active development lifecycle.

**Created**: 2026-01-15
**Last Modified**: 2026-03-27

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

### #9. [SupportSpark](https://github.com/markhazleton/SupportSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 43 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 1210 KB | 🚀 14.3 commits/month

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

### #10. [JsBootSpark](https://github.com/markhazleton/JsBootSpark)

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

### #11. [WebSpark](https://github.com/markhazleton/WebSpark)

Stars: 1 | Forks: 0 | Language: C# | 14 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 69023 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ❌ Docs

# WebSpark Technical Summary

**WebSpark** is a comprehensive .NET 9-based web application suite comprising three integrated tools—PromptSpark (LLM prompt optimization), RecipeSpark (recipe management), and TriviaSpark (quiz creation platform)—built on ASP.NET Core MVC with Bootstrap 5 styling. The platform implements a sophisticated modular architecture spanning seven functional areas (PromptSpark, RecipeSpark, TriviaSpark, WebCMS, AsyncSpark, Admin, Identity) that provides scalability and extensibility across distinct business domains. A standout feature is its **spec-driven development workflow** powered by SpecKit commands, which enforces rigorous specifications, implementation planning, task breakdown, and crucially, an adversarial risk assessment phase that catches showstopper issues, ASP.NET Core anti-patterns, security vulnerabilities, and performance killers before code implementation begins—significantly reducing production risk. The codebase demonstrates strong SEO optimization capabilities including dynamic meta tags, JSON-LD structured data, canonical URL management, XML sitemaps, multi-engine verification, Google Analytics 4 integration with custom dimensions, and Application Insights-based SEO audit logging, all supported by 47 passing test cases. This project targets developers and organizations seeking a well-architected, quality-focused web application platform with modern technologies (C#, HTML, SCSS, JavaScript) and a disciplined development governance model that prioritizes risk mitigation and specification compliance over rapid feature delivery.

**Created**: 2024-01-11
**Last Modified**: 2026-01-29

---

### #12. [ReactSparkPortfolio](https://github.com/markhazleton/ReactSparkPortfolio)

Stars: 0 | Forks: 0 | Language: CSS | 23 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 43828 KB | 🚀 7.7 commits/month

**Quality**: ❌ License | ✅ Docs

# ReactSparkPortfolio - Technical Summary

**ReactSparkPortfolio** is a production-ready, enterprise-grade developer portfolio application built with React 19, TypeScript, and Vite that demonstrates modern frontend engineering best practices and cloud-native deployment patterns. The application serves as both a personal portfolio showcase and a comprehensive reference implementation, featuring real-time capabilities through SignalR integration, dynamic content from external APIs (weather, RSS feeds, jokes), responsive Bootstrap 5-based UI with dark/light theme support, and full type safety via strict TypeScript implementation. The tech stack emphasizes performance optimization through Vite's fast bundling, code splitting with lazy-loaded components, and strategic use of the React Context API for state management, complemented by utility libraries like axios, date-fns, and xml2js for specialized functionality. The architecture employs a frontend-first pattern with Azure Static Web Apps hosting, Azure Functions for serverless APIs, and GitHub Actions CI/CD automation, while maintaining intentionally permissive Content Security Policy to support external content integration from markhazleton.com and third-party services. Key differentiators include comprehensive accessibility compliance (WCAG 2.1 AA), dual deployment support (Azure + GitHub Pages), interactive mapping with Leaflet, and extensive documentation covering security, CSP configuration, and development practices. This project is ideal for developers seeking a modern, scalable portfolio template, reference implementation for React enterprise patterns, or benchmark for TypeScript-first full-stack development practices.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 46 total (46 current, 0 outdated)

**Created**: 2024-10-11
**Last Modified**: 2026-03-07

---

### #13. [WebProjectMechanics](https://github.com/markhazleton/WebProjectMechanics)

Stars: 3 | Forks: 0 | Language: Visual Basic .NET | 9 commits (90d)

👥 0 contributors | 🌐 10 languages | 💾 52407 KB | 🚀 3.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebProjectMechanics

**WebProjectMechanics** is a multi-tenant, multi-domain content management system undergoing a modernization effort, migrating a 20+ year legacy ASP.NET Web Forms/MS Access application to a contemporary .NET 9/SQLite architecture. The system manages 36+ domains from a single application instance through a plugin-based architecture that supports multiple content domains (CMS pages, mineral collections, recipes), with each tenant isolated via dedicated SQLite database files rather than logical tenant ID columns, and publishes all public content as pre-rendered static HTML served by Caddy for optimal performance and minimal infrastructure costs (~$10/month on Azure Linux).

The architecture emphasizes clean separation of concerns through layered modules—**WPM.Core** (shared contracts), **WPM.Infrastructure** (core services), domain-specific plugins (**CMS**, **Minerals**, **Recipes**), and an **ASP.NET Core Minimal API** host—with comprehensive infrastructure for data migration from the legacy system, automated testing via xUnit, and extensive architectural documentation detailing the greenfield implementation plan. Built on a modern tech stack including Entity Framework Core 9 for data access, Scriban for templating, GitHub Actions for CI/CD, and Caddy 2 for reverse proxying with automatic SSL, the project demonstrates cost-conscious infrastructure design and strong software engineering practices with clear phasing and documentation for a complex legacy modernization effort.

**Created**: 2017-09-19
**Last Modified**: 2026-02-19

---

### #14. [Texecon](https://github.com/markhazleton/Texecon)

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

### #15. [KeyPressCounter](https://github.com/markhazleton/KeyPressCounter)

Stars: 2 | Forks: 1 | Language: C# | 3 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 46575 KB | 🚀 1.0 commits/month

**Quality**: ❌ License | ✅ Docs

# KeyPressCounter – Technical Summary

**KeyPressCounter** is a lightweight Windows system tray utility built in C# (.NET 10.0) that monitors keyboard and mouse activity alongside real-time system performance metrics in the background without recording keystroke content or transmitting data. The application provides comprehensive input statistics (keystroke/click counts, peak activity rates, idle detection), a real-time performance dashboard with 60-second rolling graphs for CPU and memory usage, hardware information via WMI, and process monitoring capabilities—all exposed through a three-tab WinForms interface accessible via double-clicking the tray icon. The architecture leverages **SharpHook** for global input event hooking, **System.Management** for WMI hardware queries, native Windows Performance Counters for system metrics, and **User32 P/Invoke** for idle time detection, with thread-safe counters and configurable JSON-based settings that persist in `%APPDATA%`. Key design strengths include single-instance enforcement, automatic daily log rotation at midnight, configurable idle-period filtering (default 5 minutes), registry-based Windows startup integration, and a context menu providing quick access to system tools (Task Manager, Resource Monitor, Performance Monitor). The project targets power users and productivity monitors who need passive activity tracking and performance visibility without compromised privacy, offering practical features like activity logging at 60-second intervals, peak rate metrics, and longest idle period tracking—all maintained with a 50/100 tech stack currency score and recent activity suggesting active development despite modest GitHub visibility (2 stars).

**Technology Stack Currency**: ✅ 66/100
**Dependencies**: 3 total (3 current, 0 outdated)

**Created**: 2024-03-07
**Last Modified**: 2026-03-09

---

### #16. [react-native-web-start](https://github.com/markhazleton/react-native-web-start)

Stars: 0 | Forks: 0 | Language: PowerShell | 14 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2045 KB | 🚀 4.7 commits/month

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

### #17. [sql2csv](https://github.com/markhazleton/sql2csv)

Stars: 0 | Forks: 0 | Language: C# | 6 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2041 KB | 🚀 2.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: sql2csv

**sql2csv** is a comprehensive .NET 10 toolkit designed for SQLite database manipulation and analysis, offering both command-line and web-based interfaces for discovering databases, exporting data, schema inspection, and C# code generation. The project follows a modular architecture with a shared core library (`Sql2Csv.Core`) that powers multiple frontends: a CLI application (`sql2csv.console`) for automation and scripting, an ASP.NET Core MVC web UI (`sql2csv.web`) with file upload and persistence capabilities, and an experimental data exploration app (`DataSpark.Web`). Key capabilities include bulk table-to-CSV export with filtering options, multi-format schema reporting (text/JSON/Markdown), automatic C# Data Transfer Object (DTO) generation from database schemas, and file management operations in the web interface, all supported by comprehensive test coverage (MSTest) and performance benchmarking (BenchmarkDotNet). The technology stack spans C# (54%), HTML/CSS/JavaScript for the frontend, and integrates Node.js tooling for web asset building, reflecting a full-stack approach to database introspection and data transformation. The project demonstrates mature engineering practices including CI/CD automation (GitHub Actions), code coverage tracking, and structured development workflows (CONTRIBUTING.md guidelines), making it particularly valuable for developers needing to reverse-engineer SQLite databases, migrate data to CSV formats, or generate strongly-typed models for C# applications without manual schema analysis.

**Created**: 2017-11-06
**Last Modified**: 2026-01-12

---

### #18. [markhazleton](https://github.com/markhazleton/markhazleton)

Stars: 0 | Forks: 0 | Language: Unknown | 16 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 6603 KB | 🚀 5.3 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: markhazleton Repository

This repository serves as Mark Hazleton's personal portfolio and learning archive—a curated collection of technical projects documenting his continuous professional development across multiple technology domains. The repository showcases several featured initiatives, including **Spec-Kit-Spark** (a pragmatic fork of GitHub SpecKit for brownfield development) and **ReactSpark** (a React application built with Vite and deployed on Azure Static Web Applications), demonstrating expertise across full-stack development, cloud infrastructure, and framework implementation. The tech stack spans modern web technologies (React, Vite), cloud platforms (Azure DevOps, Azure Static Web Apps), .NET ecosystem (NuGet packages), and API development tools (RESTful services, Postman), with a focus on practical, production-ready solutions. The project emphasizes pragmatic software architecture and evolutionary development patterns, as evidenced by his published articles on framework adoption, API load testing (RESTRunner), and brownfield modernization strategies. The repository is notable for its integration of blogging, GitHub statistics visualization, and professional networking links, creating a comprehensive personal knowledge base that extends beyond code to include strategic insights on software governance, accountability, and outcome-focused development. This multi-faceted approach targets intermediate-to-senior software developers and architects seeking practical examples of modern development practices, cloud deployment patterns, and the methodological thinking behind building maintainable systems.

**Created**: 2021-04-17
**Last Modified**: 2026-03-20

---

### #19. [TeachSpark](https://github.com/markhazleton/TeachSpark)

Stars: 0 | Forks: 0 | Language: C# | 13 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 29786 KB | 🚀 4.3 commits/month

**Quality**: ❌ License | ✅ Docs

# TeachSpark - Technical Summary

**TeachSpark** is a modern, full-stack LLM-powered educational platform built with .NET 10 MVC on the backend and a contemporary webpack-based frontend, designed to deliver personalized, AI-driven learning experiences through intelligent content adaptation and real-time feedback. The architecture combines C# backend services (29.7% of codebase) with a sophisticated frontend stack leveraging HTML, CSS, and JavaScript (28.5%, 25.6%, and 2.2% respectively), integrated through a robust webpack 5 build system that provides hot module replacement, code splitting, and asset optimization for production deployments. Key technical differentiators include automated code quality enforcement via Husky and lint-staged pre-commit hooks, comprehensive analytics capabilities for progress tracking, and a responsive, modern UX built on Bootstrap 5 with SCSS styling pipelines—all orchestrated through clean architecture principles and Entity Framework Core for data persistence. The project demonstrates mature DevOps practices with ESLint, Prettier, and Stylelint configuration, automated pre-commit validation, and a well-documented webpack build system supporting multiple development modes (dev, watch, analyze). With 44 total commits over the past year and recent accelerating activity (13 commits in the last 90 days), the project targets educators and learners seeking an intelligent alternative to traditional learning management systems by leveraging large language models to dynamically personalize curriculum delivery based on individual learning patterns. The high tech stack currency score (90/100) and modern dependency ecosystem (.NET 10, Node.js 18+) position TeachSpark as a contemporary solution for adaptive education, appealing to institutions and platforms looking to integrate AI-powered personalization into their learning infrastructure.

**Technology Stack Currency**: ✅ 90/100
**Dependencies**: 3 total (2 current, 1 outdated)

**Created**: 2025-06-19
**Last Modified**: 2026-03-29

---

### #20. [markhazleton.github.io](https://github.com/markhazleton/markhazleton.github.io)

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

### #21. [FastEndpointApi](https://github.com/markhazleton/FastEndpointApi)

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

### #22. [MechanicsOfMotherhood](https://github.com/markhazleton/MechanicsOfMotherhood)

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

### #23. [DataAnalysisDemo](https://github.com/markhazleton/DataAnalysisDemo)

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

### #24. [ConcurrentProcessing](https://github.com/markhazleton/ConcurrentProcessing)

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

### #25. [PromptSpark.Chat](https://github.com/markhazleton/PromptSpark.Chat)

Stars: 0 | Forks: 0 | Language: C# | 10 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 19888 KB | 🚀 3.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: PromptSpark.Chat

**PromptSpark.Chat** is an ASP.NET Core-based real-time conversational workflow application designed to guide users through multi-step interactive processes using a modern chat interface. The application leverages **SignalR** for bidirectional real-time communication, **Adaptive Cards** for structured interactive UI elements, and **ConcurrentDictionary** for thread-safe server-side conversation state management, enabling users to maintain progress across page refreshes without data loss. Built with a clean separation of concerns across Controllers, Services, Models, and Views layers, the architecture demonstrates enterprise-ready patterns including optional AI integration via chat completion services for handling out-of-workflow questions, along with JSON-based workflow configuration for defining branching logic through node graphs. The technology stack combines C# backend logic (31.5%) with frontend styling using SCSS/CSS (31.2%) and JavaScript (8.9%), creating a full-stack web application suitable for customer onboarding, guided surveys, decision trees, and interactive tutorials. The project is uniquely positioned for organizations needing dynamic, conversational user experiences with minimal overhead, as it eliminates the need for complex workflow engines while providing flexible branching capabilities and optional AI augmentation. Target users include SaaS platforms, customer support automation systems, interactive training applications, and business process automation tools where maintaining conversational context and guiding users through defined workflows is critical.

**Created**: 2024-12-31
**Last Modified**: 2026-02-10

---

### #26. [WebSpark.ArtSpark](https://github.com/markhazleton/WebSpark.ArtSpark)

Stars: 0 | Forks: 0 | Language: C# | 7 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3658 KB | 🚀 2.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.ArtSpark

**WebSpark.ArtSpark** is a comprehensive .NET 10.0 solution that provides complete client library coverage for the Art Institute of Chicago's public REST API, encompassing all 33 endpoints across 6 major resource categories (Collections, Shop, Mobile, Publications, etc.). The solution consists of four interconnected projects: a strongly-typed async API client library with IIIF image support and Elasticsearch integration, an innovative AI agent system featuring multiple personas (Artwork, Artist, Curator, Historian) powered by OpenAI's GPT-4o with vision capabilities and hot-reloadable prompt configuration, an interactive ASP.NET Core web demo application with user authentication and personal collection management, and a command-line utility for developer access. The architecture emphasizes modern .NET practices including System.Text.Json deserialization with proper naming policies, async/await patterns throughout, minimal external dependencies, and separation of concerns across projects, while the AI components add conversational intelligence with persistent chat history, visual analysis, and content filtering guardrails. The primary use cases are developers integrating Art Institute data into applications, museum enthusiasts exploring artworks through AI-powered conversations, and organizations seeking a reference implementation of clean .NET architecture with AI integration. While currently unmaintained (declining activity with only 7 commits in the last 90 days), the project demonstrates sophisticated integration of REST APIs, machine learning services, and enterprise web application patterns, making it valuable both as a practical tool and educational reference for advanced .NET development.

**Created**: 2023-01-30
**Last Modified**: 2026-01-12

---

### #27. [AsyncSpark](https://github.com/markhazleton/AsyncSpark)

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

### #28. [WebSpark.Bootswatch](https://github.com/markhazleton/WebSpark.Bootswatch)

Stars: 0 | Forks: 0 | Language: HTML | 5 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7124 KB | 🚀 1.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.Bootswatch

**WebSpark.Bootswatch** is a .NET 10-exclusive Razor Class Library that provides seamless integration of Bootswatch themes into ASP.NET Core applications, enabling dynamic theme switching and light/dark mode support with built-in caching mechanisms. The library abstracts Bootstrap 5's theming complexity through extension methods and tag helpers (e.g., `<bootswatch-theme-switcher />`), allowing developers to implement responsive, modern UI themes with minimal configuration while maintaining comprehensive error handling and fallback strategies. Built primarily with HTML (63.8%), C# (28.6%), and supporting PowerShell/JavaScript utilities, the project follows a modern dependency-focused architecture that prioritizes latest-generation packages and security patches over broad framework compatibility—a deliberate design choice reflected in version 2.0's exclusive .NET 10 targeting and deprecation of .NET 8/9 support. The library leverages the `StyleCache` service for high-performance CSS delivery and integrates with `WebSpark.HttpClientUtility` as a core dependency, demonstrating a modular ecosystem approach to shared utilities. Key architectural patterns include service injection through extension methods, caching abstractions, and tag helper encapsulation, making it production-ready for enterprise ASP.NET Core applications requiring flexible, performant theming without heavy manual configuration. This project is particularly valuable for development teams needing rapid theme deployment across multiple ASP.NET Core applications while maintaining performance standards and staying aligned with current .NET framework evolution.

**Created**: 2022-08-24
**Last Modified**: 2026-01-12

---

### #29. [WebSpark.PrismSpark](https://github.com/markhazleton/WebSpark.PrismSpark)

Stars: 0 | Forks: 0 | Language: C# | 14 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 2272 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ✅ Docs

# WebSpark.PrismSpark - Technical Summary

**WebSpark.PrismSpark** is a high-performance C#/.NET port of the popular PrismJS syntax highlighting library, designed to provide server-side code tokenization, syntax highlighting, and theming for .NET applications with support for 24 programming languages (C#, Python, JavaScript, Rust, Go, and more). The project leverages a modular architecture featuring a comprehensive plugin system (line numbers, copy-to-clipboard, toolbars), event-driven hooks for customization, and a flexible theme engine with built-in CSS generation, all optimized for async processing and caching to handle large-scale code highlighting efficiently. Built for .NET 10.0 LTS with backward compatibility to .NET 9.0, it integrates seamlessly into ASP.NET MVC/Razor applications through dependency injection and includes advanced features such as line-specific highlighting, custom CSS classes, and context metadata preservation. The codebase demonstrates strong software engineering practices with a comprehensive 52-test MSTest suite covering grammars, tokenization, and integration scenarios, while the interactive demo web application provides real-time syntax highlighting, a live code editor with validation and formatting, and language-specific showcases. PrismSpark differentiates itself by bringing Prism's powerful, extensible JavaScript highlighting capabilities to server-side .NET environments, eliminating the need for client-side JavaScript execution and enabling better performance, security, and integration with enterprise .NET applications—making it ideal for documentation generators, code review platforms, blog engines, and any .NET application requiring sophisticated syntax highlighting.

**Created**: 2025-05-27
**Last Modified**: 2026-02-11

---

### #30. [TaskListProcessor](https://github.com/markhazleton/TaskListProcessor)

Stars: 0 | Forks: 0 | Language: C# | 3 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 1070 KB | 🚀 1.0 commits/month

**Quality**: ❌ License | ✅ Docs

# TaskListProcessor - Technical Summary

**TaskListProcessor** is an enterprise-grade .NET 10.0 library designed to orchestrate complex asynchronous operations with sophisticated fault tolerance, observability, and task coordination capabilities. Built as a production-ready framework, it provides developers with a comprehensive solution for managing concurrent task execution through advanced patterns including circuit breakers, dependency injection, priority-based scheduling, and topological task dependency resolution. The library implements modern architectural patterns (decorator pattern, interface segregation, SOLID principles) with native integration for OpenTelemetry telemetry, Microsoft.Extensions.Logging, and structured logging frameworks like Serilog, enabling enterprise-grade monitoring and diagnostics in high-throughput systems.

Key distinguishing features include type-safe result handling with comprehensive error categorization, lock-free concurrent collections for thread-safe operations, object pooling for memory optimization, and support for streaming results via async enumerables for real-time processing. The project demonstrates mature software engineering practices with extensive documentation spanning quick-start guides, intermediate tutorials on DI/circuit breakers/scheduling, advanced optimization topics, performance benchmarks, and health check capabilities suitable for microservice architectures. Written primarily in C# (94.4%) with auxiliary PowerShell and Python scripts, the actively maintained codebase (31 commits annually) targets developers building resilient, observable distributed systems, API aggregators, workflow orchestrators, and data processing pipelines where fault isolation and operational visibility are critical requirements.

**Created**: 2023-11-09
**Last Modified**: 2026-01-12

---

### #31. [DocSpecSpark](https://github.com/markhazleton/DocSpecSpark)

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

### #32. [HttpClientDecoratorPattern](https://github.com/markhazleton/HttpClientDecoratorPattern)

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

### #33. [Yelp.Api](https://github.com/markhazleton/Yelp.Api)

Stars: 0 | Forks: 0 | Language: C# | 1 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 462 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: Yelp.API

**Yelp.API** is a C# class library that provides a managed wrapper around Yelp's v3 Fusion API, enabling .NET developers to seamlessly integrate local business search and review functionality into their applications targeting .NET 6 and later frameworks. The library abstracts the complexity of REST API calls to Yelp's backend, offering both simplified convenience methods (e.g., `SearchBusinessesAllAsync()`) and advanced query capabilities through structured `SearchRequest` objects, allowing developers to search millions of businesses across 32 countries with support for filtering by location, search terms, result limits, and operational status. Built primarily in C# (53.1%) with supplementary web assets (CSS, HTML, JavaScript), the project demonstrates a clean separation of concerns with a client-based architecture that handles authentication via API key injection and asynchronous operations for non-blocking I/O. The codebase employs modern async/await patterns and appears to follow standard .NET library conventions with organized model classes for request/response handling, making it accessible for both simple and complex business discovery scenarios. While currently unmaintained (zero recent activity over 90+ days), the library targets developers building .NET applications requiring Yelp business intelligence, review data, and location-based search functionality—useful for applications in travel, food delivery, local commerce, and business intelligence domains. The straightforward integration API and credential management approach via .NET secrets management make it a practical choice for teams already invested in the Microsoft development ecosystem.

**Created**: 2022-08-10
**Last Modified**: 2026-01-12

---

### #34. [DecisionSpark](https://github.com/markhazleton/DecisionSpark)

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

### #35. [InquirySpark](https://github.com/markhazleton/InquirySpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 9371 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# InquirySpark - Technical Summary

**InquirySpark** is a modern .NET 10-based survey and inquiry management system designed as a read-only data exploration platform, featuring a responsive MVC admin interface built with Bootstrap 5 and DataTables for intuitive data visualization and management. The architecture leverages Entity Framework Core 10 with SQLite as the persistence layer, operated strictly in read-only mode to ensure data immutability, making it ideal for audit-safe analytics and reporting scenarios where schema integrity is paramount. The solution is composed of modular components—including an admin UI layer (InquirySpark.Admin), a data access abstraction layer (InquirySpark.Repository), and shared domain models (InquirySpark.Common)—all enforced with nullable reference types, comprehensive XML documentation, and automated npm asset pipeline integration for a zero-CDN-dependency deployment model. Its key distinguishing feature is the elimination of SQL Server dependency in favor of lightweight, file-based SQLite databases with immutable connection strings, reducing infrastructure overhead while maintaining full EF Core capabilities and testability through MSTest integration tests. The project targets developers and organizations requiring self-contained survey platforms with strict data governance, read-only reporting requirements, or proof-of-concept implementations where minimal external dependencies are desirable, supported by comprehensive documentation covering Bootstrap templates, DataTables configuration, and SQLite asset management.

**Created**: 2023-10-24
**Last Modified**: 2025-12-07

---

### #36. [TriviaSpark](https://github.com/markhazleton/TriviaSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 27238 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# TriviaSpark - Technical Summary

**TriviaSpark** is a multiplayer trivia game application developed as an experimental project using ChatGPT assistance, designed to integrate with public Trivia APIs to deliver competitive gaming experiences across web and mobile platforms. The application is built primarily with **C# (.NET)** for backend logic (61.1%), complemented by **HTML, CSS, and JavaScript** (26.5%, 12.3%, and 0.1% respectively) for frontend presentation, suggesting an ASP.NET or Blazor-based architecture with traditional web technologies. Core features include user registration and authentication systems, a leaderboard ranking system for competitive gameplay, admin-level question database management, and a customizable UI designed to support both web and mobile clients while maintaining a modern, interactive interface. The application follows a standard multi-tier web application pattern, consuming external Trivia APIs to populate dynamic question sets and managing user sessions, scores, and rankings through backend persistence. The project is notable as a case study in AI-assisted development, demonstrating ChatGPT's capability to scaffold functional applications while targeting a broad demographic (ages 18-95) of tech-savvy trivia enthusiasts seeking competitive gaming experiences. However, the repository shows minimal recent activity (zero commits in 90 days, declining engagement), suggesting the project may be in maintenance mode or has stalled in active development despite its ambitious scope covering both web and mobile deployment targets.

**Created**: 2023-02-22
**Last Modified**: 2025-12-02

---

### #37. [PHPDocSpark](https://github.com/markhazleton/PHPDocSpark)

Stars: 0 | Forks: 0 | Language: PHP | 0 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 2727 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: PHPDocSpark

## Overview
PHPDocSpark is a modern PHP documentation and data exploration platform designed as both a production application and comprehensive educational reference implementation. It demonstrates hybrid architecture patterns by combining traditional server-side PHP 8.2+ with a contemporary Vite-powered asset pipeline, showcasing how to build scalable web applications that leverage the strengths of both backend and frontend tooling.

## Key Features & Capabilities
The platform provides comprehensive documentation management with Markdown-based content support, full-text search with relevance scoring, and auto-generated navigation. It includes interactive data analysis tools featuring CSV processing with field statistics, sortable/filterable DataTables integration, and dynamic Chart.js visualizations. Additional capabilities encompass GitHub API integration with caching strategies, SQLite-based CRUD operations for contact management, responsive Bootstrap 5.3 design, and external API integration (JokeAPI demo) with error handling and rate limiting.

## Technology Stack
The backend utilizes PHP 8.2+ with SQLite 3.x for embedded database functionality and Parsedown for Markdown processing. The frontend leverages Vite 7.1+ as the build tool with Sass preprocessing, Bootstrap 5.3 for responsive design, DataTables 2.3+ for enhanced table interactions, Chart.js for data visualization, and ESLint/Prettier for code quality. DevOps infrastructure includes Azure Pipelines for CI/CD automation and Azure Web Apps for production hosting on Linux containers.

## Architecture & Design Patterns
The project employs a front-controller PHP routing pattern with output buffering for template inheritance, creating a clean separation between page logic and layout composition. Assets flow through Vite's hot module replacement pipeline during development and are optimized for production distribution. Data access patterns support multiple sources—SQLite database, Markdown file system, JSON caching, and external APIs—unified behind feature-specific PHP scripts that handle business logic independently from presentation concerns.

## Distinctive Aspects
PHPDocSpark stands out as an intentionally educational project that serves dual purposes: a functional documentation platform deployed to Azure Web Apps and a detailed reference implementation demonstrating modern PHP development practices. The codebase explicitly showcases contemporary patterns (PHP 8.2+ features, responsive design, asset optimization) while maintaining simplicity that enables learning rather than overwhelming with excessive abstraction, making it valuable for developers transitioning from legacy PHP to modern frameworks.

## Target Audience & Use Cases
The platform targets PHP developers seeking modern workflow patterns, full-stack developers interested in hybrid architectures, technical writers managing documentation, and students learning web development best practices. It serves as both a functioning portfolio/documentation site and a reference implementation for building internal tools, documentation platforms, or data exploration dashboards that benefit from PHP's ecosystem while demanding contemporary frontend experiences.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2023-09-08
**Last Modified**: 2025-08-18

---


---

## Report Metadata

- **Generation Time**: 6.7 seconds
- **SVGs Generated**: 6/6
- **Total API Calls**: 0
- **Total AI Tokens**: 90,405
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
*Last updated: 2026-03-29*