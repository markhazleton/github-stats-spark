# GitHub Profile: markhazleton

**Generated**: 2026-03-15 00:52:42 UTC
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

Stars: 0 | Forks: 0 | Language: Python | 186 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 10486 KB | 🚀 62.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: github-stats-spark

## Overview

Stats Spark is a comprehensive GitHub analytics and visualization platform that automatically generates beautiful SVG profile statistics and AI-powered repository analysis reports. The project combines real-time GitHub API data collection with intelligent visualization generation and Claude Haiku AI integration to provide developers, teams, and open-source maintainers with actionable insights into their coding activity, technology usage patterns, and project health metrics.

## Core Functionality

The repository implements an end-to-end analytics pipeline featuring five distinct SVG visualization categories (overview dashboard, commit heatmaps, language statistics, streak tracking, and personality-driven fun stats), a proprietary "Spark Score" algorithm that combines consistency (40%), volume (35%), and collaboration metrics (25%), and AI-powered markdown report generation with intelligent repository ranking based on weighted popularity (30%), activity (45%), and health signals (25%). The system includes an interactive mobile-first JavaScript dashboard with Chart.js visualizations, bottom-sheet navigation patterns, and repository comparison functionality, complemented by a Python backend that handles GitHub API interactions, smart caching strategies, and rate-limit management with exponential backoff retry logic.

## Technology Stack & Architecture

The stack spans Python 3.11+ (49.5%) for backend processing using PyGithub, PyYAML, requests, and python-dateutil libraries, JavaScript/HTML/CSS (34.9% combined) for interactive dashboard components, and PowerShell (15.6%) for deployment and CI/CD automation. The architecture follows a modular design with separate concerns for API data collection, SVG rendering via svgwrite, AI integration via Claude API, and frontend visualization, deployed via GitHub Actions for daily automated updates and GitHub Pages for dashboard hosting with IndexedDB caching capabilities.

## Unique Value Propositions

Stats Spark distinguishes itself through its composite "Spark Score" metric uniquely combining consistency and collaboration signals rather than raw volume alone, a 97%+ success-rate AI summarization pipeline with intelligent three-tier fallback mechanisms (Claude → README extraction → metadata), enterprise-grade accessibility compliance (WCAG 2.1 AA), and performance-optimized mobile design achieving sub-2-second First Contentful Paint on 3G connections. The project exemplifies modern DevOps practices with smart API caching reducing calls by 80-95%, progressive web capabilities with offline support via IndexedDB, and seamless GitHub integration through automated daily workflows.

## Target Users & Use Cases

Ideal for individual developers seeking professional GitHub portfolio enhancement, engineering teams analyzing contributor productivity and technology diversity, technical leaders tracking repository health and project momentum, and open-source maintainers measuring community engagement and maintenance patterns. The zero-maintenance automation model (set once, updates forever) and flexible YAML configuration make it accessible to users of varying technical sophistication while retaining extensibility for advanced customization needs.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 10 total (10 current, 0 outdated)

**Created**: 2025-12-28
**Last Modified**: 2026-03-14

---

### #2. [mark-hazleton-s-notes](https://github.com/markhazleton/mark-hazleton-s-notes)

Stars: 0 | Forks: 0 | Language: TypeScript | 124 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 284650 KB | 🚀 41.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Mark Hazleton's Notes

This repository is a personal technical portfolio and blog site for Mark Hazleton, a Technical Solutions Architect, built as a modern full-stack web application using React 19, TypeScript, and Vite with server-side rendering (SSR) capabilities. The site combines long-form blog content on cloud architecture and engineering practices, a project portfolio with live GitHub repository metrics, video galleries, and comprehensive SEO assets—all statically prerendered and deployed to Azure Static Web Apps. The architecture employs a sophisticated multi-stage build pipeline that generates metadata from Markdown sources, fetches live GitHub data, optimizes images for RSS feeds (including automatic dimension extraction), and prerenders all routes to static HTML, enabling both dynamic client-side interactions and fast, static delivery. Key technologies include Tailwind CSS, Radix UI, React Markdown with GitHub Flavored Markdown support, and a custom build script ecosystem (generating sitemaps, RSS feeds, video sitemaps, and SEO metadata) that decouples content generation from deployment. The project is notable for its content-driven architecture—separating Markdown blog posts, JSON-based project metadata, and dynamically fetched GitHub statistics—combined with a rigorous build-time optimization strategy for images and search assets that prioritizes performance and discoverability. This is an ideal reference implementation for developers building content-heavy professional portfolios, technical blogs, or portfolio sites that require SEO optimization, RSS feed generation, and integration with external data sources like GitHub APIs.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 59 total (59 current, 0 outdated)

**Created**: 2026-01-10
**Last Modified**: 2026-03-14

---

### #3. [MuseumSpark](https://github.com/markhazleton/MuseumSpark)

Stars: 0 | Forks: 0 | Language: Python | 67 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 25019 KB | 🚀 22.3 commits/month

**Quality**: ❌ License | ✅ Docs

# MuseumSpark: Technical Summary

**MuseumSpark** is an intelligent travel planning platform designed to help art enthusiasts discover and optimize museum visits across North America by transforming the Walker Art Center Reciprocal Program membership list into a data-rich, priority-ranked resource. The project features a React 19 + Vite frontend with a comprehensive museum browser (currently tracking 1,269 museums), advanced search/filter capabilities, and a real-time data enrichment dashboard that visualizes progress across a multi-phase data pipeline. The architecture employs a sophisticated multi-source data enrichment strategy (Phases 0–3) leveraging Wikidata, Wikipedia, website scraping, and AI-assisted content extraction, with strict JSON Schema validation and a "never replace known with null" data quality principle to ensure data integrity across the dataset. The tech stack combines Python 3.11+ (Pydantic 2, BeautifulSoup4) for backend data processing with a modern frontend toolchain (React Router, Tailwind CSS 4), currently deployed as a static GitHub Pages site with plans to evolve into a full-featured FastAPI backend with user authentication, itinerary generation, and AI-powered personalization by Q4 2026. What distinguishes MuseumSpark is its commitment to transparency and scalability—the project openly tracks enrichment progress (currently 0.08% complete) while maintaining a clearly documented roadmap from data foundation through AI-assisted expert scoring to an interactive travel companion platform. The repository serves art lovers and frequent museum visitors seeking data-driven recommendations, visit optimization, and strategic trip planning across reciprocal member institutions.

**Created**: 2026-01-15
**Last Modified**: 2026-03-14

---

### #4. [UISampleSpark](https://github.com/markhazleton/UISampleSpark)

Stars: 8 | Forks: 4 | Language: HTML | 69 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 30730 KB | 🚀 23.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: UISampleSpark

**UISampleSpark** is a comprehensive .NET 10 (ASP.NET Core) educational reference application that demonstrates modern web UI architecture by implementing a common Employee/Department CRUD domain across seven distinct front-end technologies: traditional MVC, Razor Pages, React 18 SPA, Vue 3 SPA, htmx, Blazor Server, and vanilla JavaScript—enabling side-by-side comparison of UI patterns, state management, and rendering strategies. The application emphasizes clean architecture through dependency injection, repository/service abstractions, and comprehensive unit testing across domain and data layers, while incorporating production-grade concerns including Application Insights telemetry, health checks, Swagger/OpenAPI documentation, and GitHub Actions CI/CD pipelines with Docker containerization for deployment flexibility. Key technical features include dynamic Bootswatch theme switching with Bootstrap 5 styling, an in-memory Entity Framework Core data layer with mock data generation, REST API endpoints with OpenAPI specs, and advanced UI demonstrations such as PivotTable.js reporting and modal-based forms, all built on a layered project structure (Core, Data, UI, CLI) with active maintenance through five major .NET version migrations (5→10). This repository serves as both an educational resource for developers learning multiple UI frameworks and a reference implementation for enterprise ASP.NET Core applications, particularly valuable for teams evaluating technology choices or seeking best-practice examples of theming, containerization, and modern web application architecture patterns. The accelerating activity pattern (69 commits in 90 days) and recent .NET 10 adoption indicate active ongoing development and relevance to current framework versions.

**Created**: 2019-04-25
**Last Modified**: 2026-03-14

---

### #5. [git-spark](https://github.com/markhazleton/git-spark)

Stars: 0 | Forks: 0 | Language: TypeScript | 29 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 1884 KB | 🚀 9.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Git Spark - Technical Summary

**Git Spark** is a TypeScript-based Git repository analytics and reporting tool that analyzes commit history to generate interactive insights into contributor activity, code changes, and development patterns. The project provides both a command-line interface and Node.js API for comprehensive Git repository analysis, offering multiple output formats (HTML, JSON, CSV, Markdown) with rich visualization capabilities including timeline charts, contribution heatmaps, risk factor analysis, and governance metrics.

The core architecture leverages modern CLI tooling (Commander.js for CLI orchestration, Ora for progress indicators, Chalk for terminal styling) paired with a custom analytics engine that processes Git commit data to compute statistics around contributor behavior, file change patterns, and temporal trends. The interactive HTML reports feature security-first design patterns with Content Security Policy (CSP) compliance, native SVG charting (avoiding external dependencies), and client-side data export functionality, making reports self-contained artifacts suitable for air-gapped or sensitive review workflows.

Notable design decisions include email redaction capabilities for privacy-sensitive audits, timezone-aware daily trend calculations, configurable analysis periods via CLI flags or `.git-spark.json` configuration files, and honest metric documentation that explains data limitations inherent to Git-only analysis. The tech stack maintains relatively current dependencies (Node.js ≥20.19.0) with a 50/100 currency score, suggesting some dependencies could benefit from updates, though the core functionality remains solid with active recent development (29 commits in 90 days, though showing declining activity patterns).

**Target users** include development teams seeking governance insights, technical leads conducting code health assessments, and organizations requiring auditable analytics on repository activity—particularly those in regulated environments where self-contained, offline-capable reports are essential. The combination of CLI accessibility and programmatic API makes it suitable for integration into CI/CD pipelines, dashboard systems, or standalone analytics workflows.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 19 total (19 current, 0 outdated)

**Created**: 2025-09-29
**Last Modified**: 2026-03-14

---

### #6. [WebSpark.HttpClientUtility](https://github.com/markhazleton/WebSpark.HttpClientUtility)

Stars: 0 | Forks: 0 | Language: C# | 38 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2364 KB | 🚀 12.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.HttpClientUtility

## Overview
WebSpark.HttpClientUtility is a production-ready, enterprise-grade HttpClient wrapper library for .NET 8-10 LTS that dramatically simplifies HTTP client configuration by encapsulating resilience patterns, response caching, structured logging, and OpenTelemetry observability into a single `AddHttpClientUtility()` dependency injection call. Rather than requiring 50+ lines of boilerplate setup with manual Polly integration, correlation ID management, and telemetry configuration, developers can achieve comprehensive HTTP functionality with minimal code.

## Core Architecture & Key Features
The library implements a service-oriented architecture built around the `IHttpRequestResultService` interface, providing generic `HttpRequestResult<T>` response objects that unify success/error handling across synchronous and asynchronous operations. Built-in capabilities include Polly-based retry policies with configurable circuit breakers, intelligent in-memory response caching with TTL control, automatic correlation ID propagation for distributed tracing, structured logging with rich contextual metadata (request/response details, timing telemetry), and seamless OpenTelemetry ActivitySource instrumentation for production observability. The v2.0 architecture splits functionality into two modular NuGet packages—the core `WebSpark.HttpClientUtility` (163 KB) for standard HTTP operations and `WebSpark.HttpClientUtility.Crawler` (75 KB) for web scraping with robots.txt parsing and sitemap generation.

## Technical Implementation & Quality Standards
The codebase leverages modern .NET features including Source Link for symbol debugging, trimming and AOT (Ahead-of-Time) compilation readiness with appropriate code annotations, and semantic versioning with zero breaking changes within major versions. The project demonstrates exceptional production quality through 237+ unit tests with 100% pass rate across .NET 8, 9, and 10 frameworks, zero-warning strict builds (`TreatWarningsAsErrors=true`), continuous integration via GitHub Actions, and package validation baselines. The implementation supports multiple authentication patterns (Bearer tokens, API keys, custom headers) and provides middleware-compatible correlation ID injection for microservice environments.

## Target Use Cases & Differentiation
WebSpark is purpose-built for microservices architectures, distributed systems requiring automatic tracing correlation, background workers needing resilience without boilerplate, and web crawling scenarios—significantly reducing setup overhead compared to raw HttpClient or manual Polly configuration. Unlike Refit (which prioritizes type-safe declarative clients) or RestSharp (which requires manual resilience configuration), WebSpark prioritizes pragmatic, convention-over-configuration design with battle-tested defaults, making it ideal for teams prioritizing developer velocity and production observability. The project's active development cycle (38 commits over 90 days, 125 over 365 days), comprehensive documentation site, and long-term support commitment (18+ months per major version) position it as a reliable alternative for organizations standardizing on modern .NET LTS versions.

**Created**: 2025-05-03
**Last Modified**: 2026-03-15

---

### #7. [WebSpark](https://github.com/markhazleton/WebSpark)

Stars: 1 | Forks: 0 | Language: C# | 14 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 69023 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ❌ Docs

# WebSpark - Technical Summary

**WebSpark** is a modular .NET 9 web application suite comprising three specialized tools: PromptSpark (LLM prompt optimization), RecipeSpark (recipe management), and TriviaSpark (quiz platform), all built with ASP.NET Core MVC and Bootstrap 5. The architecture is notably sophisticated, featuring seven modular areas with comprehensive SEO optimization including dynamic meta tags, JSON-LD structured data, canonical URL management, XML sitemaps, multi-engine verification, and Google Analytics 4 integration with Core Web Vitals tracking—backed by 47 passing SEO tests. The project implements a rigorous **spec-driven development workflow** through SpecKit commands that enforce quality gates: developers must create specifications, implementation plans, task breakdowns, and crucially, undergo adversarial risk assessment (the `/speckit.critic` command) before coding begins, with automated detection of showstoppers including ASP.NET anti-patterns, security vulnerabilities, and performance issues. The codebase is primarily C# (47%), HTML (40.4%), and SCSS (7%), maintained with strict branch protection rules and a constitutional governance framework, making it suitable for teams prioritizing risk mitigation and quality assurance in enterprise web development. The project remains actively maintained (14 commits in 90 days) despite minimal current adoption, suggesting it's either in early stages or represents internal tooling that could serve as a reference implementation for production-grade .NET applications.

**Created**: 2024-01-11
**Last Modified**: 2026-01-29

---

### #8. [TailwindSpark](https://github.com/markhazleton/TailwindSpark)

Stars: 0 | Forks: 0 | Language: HTML | 32 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 3268 KB | 🚀 10.7 commits/month

**Quality**: ❌ License | ✅ Docs

# TailwindSpark - Technical Summary

**TailwindSpark** is a comprehensive, production-ready Tailwind CSS design system and component showcase built as a modern React TypeScript monorepo using Turborepo architecture. The project demonstrates advanced CSS utility-first design patterns with Tailwind CSS v4's @theme directive and design tokens, combined with React 19.1's concurrent features and TypeScript 5.9's strict type safety, all optimized through Vite 7.1 for rapid development and performant builds. The monorepo structure decouples shared design tokens and reusable UI components into separate packages, enabling modular code organization and scalable component distribution across multiple applications. Key features include a fully accessible (WCAG 2.1 AA) interactive component library, real-time Core Web Vitals monitoring, dark mode support, keyboard navigation with command shortcuts (Ctrl/Cmd + K), and multiple showcase applications (dashboard, e-commerce, marketing pages) demonstrating real-world usage patterns. The project prioritizes developer experience through comprehensive tooling including ESLint 9.39 + Prettier formatting, automated Vitest coverage reporting, security scanning via CodeQL, and CI/CD automation through GitHub Actions with Dependabot dependency management. TailwindSpark serves as both a reference implementation for modern web development best practices and a reusable design system foundation for enterprises and developers seeking to build accessible, performant, and maintainable web applications with contemporary web technologies.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2025-07-29
**Last Modified**: 2026-03-08

---

### #9. [KeyPressCounter](https://github.com/markhazleton/KeyPressCounter)

Stars: 2 | Forks: 1 | Language: C# | 3 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 46575 KB | 🚀 1.0 commits/month

**Quality**: ❌ License | ✅ Docs

# KeyPressCounter - Technical Summary

**KeyPressCounter** is a lightweight Windows system tray utility built in C# (.NET 10.0) that monitors keyboard and mouse activity alongside real-time system performance metrics, designed to run silently in the background without recording keystroke content or transmitting data. The application provides comprehensive input tracking (keystroke/click counts, peak activity rates, inactivity detection) and performance monitoring (CPU, memory, disk I/O, network throughput) through a three-tab WinForms dashboard with 60-second rolling graphs, hardware information via WMI, and configurable activity logging with daily summaries.

The architecture leverages **SharpHook** for global low-level input event hooking on background threads, **System.Management** for WMI-based hardware enumeration and Windows Performance Counters for real-time system metrics, and implements thread-safe counters with lock-protected increments to handle concurrent input events. Key design patterns include an `ApplicationContext` subclass managing tray integration and lifecycle, GDI+ anti-aliased graph rendering for historical data visualization, P/Invoke wrappers around `GetLastInputInfo` for idle detection, and JSON configuration persistence with Windows Registry synchronization for autostart capabilities.

Notable features include idle-period filtering with configurable thresholds, single-instance enforcement, direct access to Windows system tools (Task Manager, Resource Monitor, Performance Monitor), and comprehensive logging at user-configurable intervals with automatic daily summary generation at midnight. The project targets individual users and productivity analysts seeking passive activity monitoring and system performance awareness without privacy concerns, with declining recent activity (3 commits in 90 days) suggesting maintenance mode rather than active development, though the codebase demonstrates professional separation of concerns and Windows-native integration patterns suitable for production desktop applications.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 3 total (3 current, 0 outdated)

**Created**: 2024-03-07
**Last Modified**: 2026-03-09

---

### #10. [ReactSparkPortfolio](https://github.com/markhazleton/ReactSparkPortfolio)

Stars: 0 | Forks: 0 | Language: CSS | 24 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 43478 KB | 🚀 8.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: ReactSparkPortfolio

**ReactSparkPortfolio** is a production-ready, enterprise-grade developer portfolio application built with React 19, TypeScript, and Vite that demonstrates modern frontend engineering best practices and cloud-native deployment patterns. The project showcases a comprehensive tech stack including Bootstrap 5 for responsive UI, SCSS for advanced styling, SignalR for real-time functionality, and integrations with external APIs (OpenWeather, JokeAPI, RSS feeds) all orchestrated through a serverless architecture leveraging Azure Static Web Apps and Functions with GitHub Actions CI/CD automation. Key features include real-time chat powered by SignalR, interactive weather widgets with Leaflet maps, dynamic RSS feed integration, dark/light theme switching, and a searchable project showcase—all with full TypeScript type safety, WCAG 2.1 AA accessibility compliance, and optimized performance through code splitting and lazy loading. The architecture employs a frontend-only design that pulls content from external sources (markhazleton.com) with a deliberately permissive Content Security Policy to enable seamless integrations, while maintaining separation of concerns through React Context for state management, service layers for API communication, and component-based organization. This serves as both a personal portfolio and a reference implementation for developers seeking to understand scalable, maintainable web application patterns, making it particularly valuable for those interested in React best practices, TypeScript patterns, serverless architecture, or modern CI/CD workflows. The project's active development (24 commits in 90 days), comprehensive documentation, and dual deployment strategy (Azure + GitHub Pages) make it an exemplary showcase of production-quality frontend engineering suitable for portfolio demonstrations or organizational reference implementations.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 46 total (46 current, 0 outdated)

**Created**: 2024-10-11
**Last Modified**: 2026-03-07

---

### #11. [WebProjectMechanics](https://github.com/markhazleton/WebProjectMechanics)

Stars: 3 | Forks: 0 | Language: Visual Basic .NET | 9 commits (90d)

👥 0 contributors | 🌐 10 languages | 💾 52405 KB | 🚀 3.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebProjectMechanics

**WebProjectMechanics** is a greenfield rebuild of a multi-tenant, multi-domain content management system designed to serve 36+ websites from a single application instance while maintaining physical database isolation and cost-efficient hosting (~$10/month). The system publishes dynamic content as static HTML through a sophisticated plugin-based architecture that supports multiple content domains (CMS pages, Mineral Collection, Recipes) and uses per-site SQLite databases rather than traditional tenant ID columns, eliminating cross-tenant data concerns. Built on modern .NET 9 with ASP.NET Core Minimal APIs, Entity Framework Core 9, and Scriban templating, the architecture decouples content management from delivery by pre-rendering all public content and serving it via Caddy 2 with automatic SSL termination and reverse proxying on Ubuntu Linux. The repository includes comprehensive documentation of both the legacy 20+ year old ASP.NET Web Forms/MS Access system and a detailed implementation roadmap, with dedicated domain projects organized in a clean layered structure (Core, Infrastructure, API, and three domain modules) plus a migration tool for data transition. What distinguishes this project is its pragmatic approach to scaling a legacy system—avoiding expensive refactoring while achieving modern deployment patterns, cost optimization, and maintainability through thoughtful architectural decisions around data isolation and static site generation. Target users are organizations managing multiple related websites with moderate content complexity who need reliable hosting with minimal infrastructure overhead, making this particularly valuable as a case study in legacy system modernization and multi-tenant architecture patterns.

**Created**: 2017-09-19
**Last Modified**: 2026-02-19

---

### #12. [JsBootSpark](https://github.com/markhazleton/JsBootSpark)

Stars: 0 | Forks: 0 | Language: JavaScript | 22 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 3448 KB | 🚀 7.3 commits/month

**Quality**: ❌ License | ✅ Docs

# JsBootSpark - Technical Summary

**JsBootSpark** is a production-ready, full-stack starter kit designed to accelerate web application development by combining Express.js backend capabilities with Bootstrap 5.3 frontend components. The project serves as a comprehensive boilerplate that abstracts away common configuration and setup tasks, enabling developers to begin building feature-rich applications immediately without reinventing foundational infrastructure.

The platform demonstrates mature architectural decisions including hot-reload development workflows, SASS preprocessing, comprehensive security middleware (Helmet.js, rate limiting, CSP), and progressive web app capabilities with service worker support. It features 2,000+ Bootstrap Icons, dark/light mode toggling, responsive design patterns, and a component library with interactive examples, while backend capabilities include dynamic page generation from templates, CSV-to-JSON conversion for static data handling, and automated build optimization with performance tracking.

The tech stack leverages modern JavaScript tooling (Node.js 18+, Express 5.1+, EJS templating) with 30 dependencies carefully curated for production use, complemented by ESLint/Prettier for code consistency, Jest for testing, and Docker support for containerized deployment. The project implements an opinionated, DevOps-friendly architecture with GitHub Actions CI/CD integration, GitHub Pages deployment pipeline, subdirectory path conversion for flexible hosting, and automated static site generation capabilities that can produce 100+ pages from single templates.

The repository targets full-stack JavaScript developers, teams building internal tools, and organizations seeking accelerated prototyping workflows, offering documentation structured by audience (quick starts, developer guides, architectural decisions), real-time copilot session tracking, and a consistent activity pattern showing ongoing maintenance and feature development. Its 3,448 KB footprint and modular structure position it as an enterprise-friendly starter that balances convenience with minimal bloat while maintaining 50/100 tech stack currency with active dependency management.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 30 total (30 current, 0 outdated)

**Created**: 2022-06-06
**Last Modified**: 2026-01-31

---

### #13. [RESTRunner](https://github.com/markhazleton/RESTRunner)

Stars: 2 | Forks: 1 | Language: C# | 16 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 426 KB | 🚀 5.3 commits/month

**Quality**: ❌ License | ✅ Docs

# RESTRunner - Technical Summary

**RESTRunner** is a comprehensive .NET 10 (LTS) solution designed for automated REST API testing, performance benchmarking, and regression testing that imports and executes Postman collections at scale. The application provides dual interfaces—a console application for batch processing and a Razor Pages web application for interactive testing—enabling developers to validate APIs through load testing, performance analysis, and detailed statistical reporting with CSV export capabilities.

The project demonstrates strong engineering practices with a modular architecture spanning multiple layers: a domain model (RESTRunner.Domain) with comprehensive unit test coverage (21/21 tests, 100% pass rate), a web tier (RESTRunner.Web) built on ASP.NET Core Razor Pages, and specialized components for Postman collection parsing, HTTP client utilities, and performance metrics aggregation. Key features include configurable load testing parameters, response time percentile analysis, success rate tracking, a built-in sample CRUD API for demonstration, and integrated statistics generation.

RESTRunner recently underwent a significant upgrade to .NET 10 LTS, achieving notable performance improvements (19% faster builds at 4.1s, 25% faster test execution at 0.6s) while optimizing package dependencies from 17 to 15 packages with 93% at latest stable versions and zero security vulnerabilities. The technology stack leverages MSTest v4 with code quality analyzers, modern C# patterns, and framework-integrated libraries (System.Text.Json, security cryptography) to minimize external dependencies and maximize runtime efficiency.

The project is particularly valuable for QA engineers and API developers who need automated regression testing workflows, DevOps teams requiring performance benchmarking across multiple API instances, and organizations seeking to import existing Postman test collections into a scalable, performant .NET-based testing framework without vendor lock-in. Its active development pattern (16 commits in 90 days, accelerating activity) and comprehensive documentation including upgrade guides suggest ongoing maintenance and future feature expansion.

**Created**: 2021-09-30
**Last Modified**: 2026-01-12

---

### #14. [Texecon](https://github.com/markhazleton/Texecon)

Stars: 0 | Forks: 0 | Language: HTML | 16 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 4170 KB | 🚀 5.3 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: Texecon

**Texecon** is a modern static site generator for Texas economic analysis built as a React 19 application deployed to GitHub Pages, combining server-side content management with client-side performance optimization. The project implements a sophisticated build pipeline that fetches fresh content from a WebSpark headless CMS API during compilation, generates SEO-optimized static HTML pages with structured data and dynamic sitemaps, and provides progressive enhancement through Wouter-based client-side routing with HTML fallbacks. The tech stack leverages Vite 7.1 for fast builds, TypeScript for type safety, Tailwind CSS 4.1 for styling, and Radix UI/shadcn/ui component libraries for accessible, customizable interfaces—all optimized for Core Web Vitals and search engine performance. The architecture demonstrates advanced static site generation patterns including build-time API integration with graceful fallback caching, automatic TypeScript type generation from CMS responses, and cache-busting mechanisms for asset versioning. Unique to this project is its hybrid approach of pre-rendering dynamic content at build time while maintaining interactive client-side functionality, making it suitable for content-heavy sites requiring both SEO excellence and modern user experience. The project serves economic analysts, policy researchers, and stakeholders seeking data-driven insights into Texas's economy through a performant, maintainable platform that automatically updates content without requiring manual builds.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 40 total (40 current, 0 outdated)

**Created**: 2025-09-03
**Last Modified**: 2026-03-08

---

### #15. [MechanicsOfMotherhood](https://github.com/markhazleton/MechanicsOfMotherhood)

Stars: 0 | Forks: 0 | Language: TypeScript | 14 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 6719 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Mechanics of Motherhood

**Mechanics of Motherhood** is a modern recipe management platform built as a React 19 + TypeScript single-page application (SPA) designed specifically for busy working mothers seeking organized meal planning solutions. The platform features 108+ curated recipes with smart categorization, advanced search and filtering capabilities, and a mobile-first responsive design powered by Vite, Tailwind CSS, and Shadcn/ui component library. The architecture leverages TanStack React Query for efficient server state management and data caching, integrates with real-time APIs (RecipeSpark and WebCMS) for dynamic recipe content, and implements automated CI/CD pipelines via GitHub Actions for seamless deployment to a custom domain with GitHub Pages CDN distribution.

The project demonstrates production-ready best practices including comprehensive TypeScript type safety, WCAG accessibility compliance, PWA capabilities with offline support, automated data quality validation, SEO optimization with structured data and sitemaps, and Lighthouse performance scores exceeding 95 across all metrics. Key technical differentiators include a lightweight routing solution with Wouter, industrial-themed UI aesthetics, ~130KB gzipped bundle size with code splitting, and robust error handling with API fallback mechanisms to mock data. The codebase is well-structured with clear separation of concerns across components, pages, data layers, and utilities, making it maintainable and extensible for future enhancements or community contributions focused on recipe discovery, meal planning, and nutritional information management for its target demographic of time-constrained parents.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 42 total (42 current, 0 outdated)

**Created**: 2025-09-01
**Last Modified**: 2026-03-09

---

### #16. [ConcurrentProcessing](https://github.com/markhazleton/ConcurrentProcessing)

Stars: 0 | Forks: 0 | Language: C# | 19 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 145 KB | 🚀 6.3 commits/month

**Quality**: ❌ License | ✅ Docs

# ConcurrentProcessing - Technical Summary

**ConcurrentProcessing** is a production-ready, high-performance concurrent task processing framework for .NET 10 that provides fine-grained control over parallel task execution through semaphore-based throttling and built-in performance metrics. The framework centers around a generic abstract base class `ConcurrentProcessor<T>` that enables developers to implement custom task processing logic while automatically managing concurrency limits, tracking execution metrics (task duration, wait times, throughput), and performing statistical analysis—supporting use cases from 100 to 1000+ concurrent tasks with configurable parallelism. Built with modern C# 12+ features (primary constructors, pattern matching, nullable references) and leveraging the .NET 10 runtime optimizations, the architecture employs well-established design patterns including Template Method (for extensible processing), Resource Pool Pattern (semaphore management), and Factory Pattern (task ID generation) to maintain both flexibility and efficiency with minimal overhead. The project distinguishes itself as an educational resource that demonstrates best practices in concurrent programming and TPL (Task Parallel Library) usage while maintaining benchmarked performance characteristics showing near-linear scaling—achieving ~250ms total execution time for 100 tasks at 10 concurrent limit versus ~1500ms at single concurrency. Targeted at .NET developers seeking to build scalable, parallelized applications with measurable performance insights, it includes comprehensive documentation, CI/CD pipelines with automated build/test workflows, and includes an accompanying blog article for deeper architectural understanding and real-world application scenarios.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 2 total (2 current, 0 outdated)

**Created**: 2023-09-18
**Last Modified**: 2026-01-22

---

### #17. [PromptSpark.Chat](https://github.com/markhazleton/PromptSpark.Chat)

Stars: 0 | Forks: 0 | Language: C# | 10 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 19888 KB | 🚀 3.3 commits/month

**Quality**: ❌ License | ✅ Docs

# PromptSpark.Chat - Technical Summary

**PromptSpark.Chat** is a real-time conversational workflow engine built with ASP.NET Core and SignalR that enables users to navigate multi-step processes through an interactive chat interface powered by Adaptive Cards. The application provides server-side conversation persistence, allowing users to maintain their workflow progress across browser sessions without data loss, and supports optional AI integration for handling out-of-workflow queries through chat completion services. The architecture leverages a thread-safe ConcurrentDictionary for state management, JSON-based workflow definitions with branching logic, and real-time bidirectional communication via SignalR, demonstrating a lightweight yet scalable approach to guided user interactions and form workflows. The technology stack combines ASP.NET Core backend (31.5% C#) with a modern frontend composed of SCSS (30%), HTML (28.4%), and JavaScript (8.9%), offering both styling flexibility and interactivity across the chat UI. This solution is particularly well-suited for enterprise guidance systems, customer onboarding flows, interactive questionnaires, and decision-tree applications where maintaining context and providing responsive feedback are critical, while its modular workflow definition system allows non-developers to configure new processes without code changes. The project's recent acceleration in commits and active development pattern, combined with its comprehensive documentation and MIT licensing, positions it as a practical template for organizations building conversational AI or workflow automation features within the .NET ecosystem.

**Created**: 2024-12-31
**Last Modified**: 2026-02-10

---

### #18. [markhazleton](https://github.com/markhazleton/markhazleton)

Stars: 0 | Forks: 0 | Language: Unknown | 11 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 6595 KB | 🚀 3.7 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: markhazleton Repository

This repository serves as Mark Hazleton's personal portfolio and learning archive—a curated collection demonstrating his continuous skill development across modern web technologies and software architecture practices. The primary purpose is to showcase featured projects including **WebSpark** (a comprehensive web application hosting platform for demos) and **ReactSpark** (a React+Vite application deployed on Azure Static Web Applications), alongside a growing body of technical articles covering software development philosophy, DevOps practices, and AI-assisted development methodologies.

The repository demonstrates expertise across a diverse technology stack including React, Vite, Azure cloud services (Static Web Applications, DevOps), and modern CI/CD automation patterns, with an emphasis on pragmatic software engineering principles such as spec-driven development, fork management automation, and late-stage deployment governance. The architecture reflects a professional approach to full-stack development, with projects deployed on cloud platforms and integrated with industry-standard tools like Postman and Azure DevOps for API testing and project management.

What distinguishes this portfolio is its dual focus on both **technical execution** (working code, deployed applications) and **thought leadership** (published articles addressing strategic software development topics like accountability, evolution over revolution, and feature-to-outcome alignment), making it valuable for both practitioners seeking reference implementations and organizations evaluating senior engineering talent with architectural maturity.

**Created**: 2021-04-17
**Last Modified**: 2026-03-01

---

### #19. [FastEndpointApi](https://github.com/markhazleton/FastEndpointApi)

Stars: 2 | Forks: 1 | Language: HTML | 1 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 137 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: FastEndpointApi

**FastEndpointApi** is a comprehensive demonstration and educational project showcasing the FastEndpoints framework—a lightweight, high-performance REST API framework for ASP.NET Core that implements the REPR (Request-Endpoint-Response) pattern. The repository contains a fully functional Person Management API deployed to Azure, featuring complete CRUD operations, in-memory data persistence, service layer abstraction, and interactive Swagger documentation. Built with .NET 10.0 and FastEndpoints 7.1.1, the project leverages modern technologies including dependency injection, automatic request-response mapping, HATEOAS hypermedia links, and GitHub Actions CI/CD pipelines for automated deployment. The architecture emphasizes clean code principles and minimal boilerplate through endpoint-based organization rather than traditional MVC controllers, with integrated data seeding via Bogus and a Bootstrap 5-based HTML frontend for interactive API testing. This repository serves as both a learning resource and production-ready reference implementation for developers seeking to understand FastEndpoints' capabilities, particularly those looking to streamline ASP.NET Core API development while maintaining separation of concerns and high performance standards. The project is actively maintained with comprehensive documentation, live demo accessibility, and clear examples of advanced patterns like HATEOAS implementation and structured error handling.

**Created**: 2024-04-06
**Last Modified**: 2026-01-12

---

### #20. [SupportSpark](https://github.com/markhazleton/SupportSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 23 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 1856 KB | 🚀 7.7 commits/month

**Quality**: ❌ License | ❌ Docs

# SupportSpark: Technical Summary

**SupportSpark** is a TypeScript-based support network platform designed to help individuals share life journey updates with trusted circles during challenging times, addressing the burden of repetitive personal updates through a centralized, calming interface. The platform implements a role-based architecture where members create and manage journey conversations while supporters receive invitations to read updates and participate in threaded discussions, with features including invitation-only access control, real-time engagement tracking, and a demo mode for exploration without authentication.

The application employs a modern, full-stack TypeScript architecture with **React 19 + Vite** on the frontend, **Express 5** for the backend API, and **Tailwind CSS 4** with **Radix UI** and **shadcn/ui** components for an accessible, WCAG-compliant interface. State management leverages **TanStack React Query** for server-side caching, **Wouter** for lightweight routing, and **Zod** for end-to-end runtime type validation, while authentication uses **Passport.js** with session-based security and a JSON-based storage layer for data persistence.

What distinguishes SupportSpark is its intentional focus on compassionate UX design—featuring a calming teal/sage color scheme, distraction-free layout, and accessibility-first component primitives—combined with production-ready Windows/IIS deployment automation via PowerShell scripts and iisnode integration. The project maintains a documented governance model (constitution.md), architectural separation between client/server/shared code, and support for both client-side localStorage demo mode (GitHub Pages deployment) and server-backed production environments, making it suitable for healthcare, personal wellness, and community support use cases where sensitive communication infrastructure is required.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 97 total (97 current, 0 outdated)

**Created**: 2026-02-01
**Last Modified**: 2026-02-25

---

### #21. [sql2csv](https://github.com/markhazleton/sql2csv)

Stars: 0 | Forks: 0 | Language: C# | 6 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2004 KB | 🚀 2.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: sql2csv

**sql2csv** is a comprehensive .NET 10 toolkit for SQLite database analysis and data extraction, providing both command-line and web-based interfaces for discovering databases, exporting tables to CSV format, inspecting schemas, and automatically generating C# data transfer objects (DTOs). The solution follows a modular architecture with a shared core library (`Sql2Csv.Core`) serving dual CLI (`sql2csv.console`) and ASP.NET Core MVC web (`sql2csv.web`) frontends, complemented by dedicated projects for testing (MSTest) and performance benchmarking (BenchmarkDotNet). Key capabilities include recursive SQLite file discovery, selective or bulk table export with CSV serialization, multi-format schema reporting (text/JSON/Markdown), and intelligent C# DTO generation with customizable namespacing, enabling developers to rapidly integrate SQLite data into .NET applications. The project demonstrates modern .NET practices including configuration management via `appsettings.json`, comprehensive test coverage with CI/CD integration (GitHub Actions), and a hybrid tech stack combining C# backend logic with HTML/CSS/JavaScript frontend components, making it well-suited for database migration workflows, data integration pipelines, and rapid prototyping scenarios involving SQLite databases.

**Created**: 2017-11-06
**Last Modified**: 2026-01-12

---

### #22. [DocSpecSpark](https://github.com/markhazleton/DocSpecSpark)

Stars: 0 | Forks: 0 | Language: Python | 2 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 181 KB | 🚀 0.7 commits/month

**Quality**: ❌ License | ✅ Docs

# DocSpecSpark - Technical Summary

DocSpecSpark is a document-first framework and CLI tool that automates the initialization, generation, and publication of company documentation repositories with profile-based templating and static site generation capabilities. The project provides a comprehensive system for bootstrapping documentation infrastructure, including a Python-based CLI package (built with Typer for command structure), a modular framework payload with filesystem-backed templates, and a complete publication pipeline that renders markdown documents, builds static sites, and packages versioned release bundles for distribution. The architecture emphasizes profile-aware customization through YAML-driven configuration (constitution and config files), with concrete starter templates for diverse organizational contexts (nonprofits, startups, small manufacturers, enterprises, healthcare), allowing companies to scaffold documentation repositories tailored to their specific profile and governance needs. Key capabilities include document rendering from reusable templates, local site preview via `docspec serve`, automated GitHub Pages publication workflows, and versioned release snapshots that snapshot documentation states to `.DocSpecSpark/releases/` with corresponding zip distributions. The tech stack is modern and minimal—leveraging markdown-it-py for parsing, PyYAML for configuration management, Rich for CLI output formatting, and Typer for command definition—reflecting a pragmatic approach to documentation infrastructure without heavyweight dependencies. This tool is particularly valuable for organizations needing standardized, scalable documentation practices, offering an opinionated but flexible framework that balances template reusability with organizational customization, positioning it as a bridge between documentation-as-code philosophies and practical enterprise governance needs.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 4 total (4 current, 0 outdated)

**Created**: 2026-03-07
**Last Modified**: 2026-03-08

---

### #23. [WebSpark.ArtSpark](https://github.com/markhazleton/WebSpark.ArtSpark)

Stars: 0 | Forks: 0 | Language: C# | 7 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3658 KB | 🚀 2.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.ArtSpark

**WebSpark.ArtSpark** is a comprehensive .NET 10.0 solution that provides a complete client library and interactive web application for the Art Institute of Chicago's public REST API, implementing all 33 endpoints across 6 major categories with strongly-typed C# models and async/await patterns. The solution's standout feature is its revolutionary AI chat system with multiple personas (Artwork, Artist, Curator, Historian) that leverage OpenAI's Vision and language models to enable conversational interactions with artwork data, complete with persistent chat history, visual analysis capabilities, and externalized prompt management for hot-reloading persona definitions. The architecture comprises four main projects—a reusable Client library, an AI Agent system with configurable prompts and conversation memory, an ASP.NET Core MVC Demo application with user authentication/collections, and a Console utility—demonstrating modern .NET development practices including dependency injection, IIIF image URL construction, Elasticsearch integration, and JSON deserialization using System.Text.Json. Key technical highlights include minimal external dependencies, graceful HTTP error handling, flexible querying with pagination and field selection, responsive Bootstrap 5 UI with 26+ theme support, and SQLite-backed user persistence, all documented with a live demo at artspark.markhazleton.com. The project targets developers and cultural institutions seeking to build intelligent art discovery applications while showcasing best practices in .NET ecosystem development, API client design, and AI integration patterns.

**Created**: 2023-01-30
**Last Modified**: 2026-01-12

---

### #24. [markhazleton.github.io](https://github.com/markhazleton/markhazleton.github.io)

Stars: 0 | Forks: 0 | Language: SCSS | 1 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 144 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Mark Hazleton's Personal Jekyll Site

This repository is a personal portfolio and blog website built with **Jekyll**, a static site generator, and hosted on **GitHub Pages** at markhazleton.com. The site leverages a customized Minima theme with bespoke layouts, includes, and styling written in SCSS/CSS, providing a lightweight, performant alternative to heavy frontend frameworks while maintaining modern aesthetics including dark/light mode toggle functionality and emoji support.

The tech stack consists of **Ruby 3.2.2** with Jekyll 3.10.0 as the core engine, automated deployment via **GitHub Actions** CI/CD pipeline, and three key dependencies (github-pages, faraday-retry, wdm) for dependency management and Windows development support. The codebase is well-structured with clear separation of concerns—markdown-based posts in `_posts/`, reusable Liquid template components in `_includes/`, and modularized SCSS architecture for maintainability.

The repository demonstrates solid software engineering practices including comprehensive documentation for content creation workflows (with both direct-commit and feature-branch options), local development setup instructions across multiple operating systems, and version-controlled dependency management through Bundler. However, activity metrics reveal a declining maintenance pattern with only one commit in the past 90 days and 16 commits over the past year, coupled with a moderate tech currency score of 50/100, suggesting the project could benefit from dependency updates and more active maintenance, though its static nature means it remains functional despite reduced activity.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 3 total (3 current, 0 outdated)

**Created**: 2021-04-18
**Last Modified**: 2026-01-12

---

### #25. [AsyncSpark](https://github.com/markhazleton/AsyncSpark)

Stars: 0 | Forks: 0 | Language: C# | 9 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 1925 KB | 🚀 3.0 commits/month

**Quality**: ❌ License | ✅ Docs

# AsyncSpark - Technical Summary

AsyncSpark is a production-ready reference implementation demonstrating enterprise-grade async/await patterns in .NET 10, designed to serve as both a learning resource and architectural blueprint for building resilient, scalable distributed systems. The project implements comprehensive async best practices including ConfigureAwait(false) library usage, proper CancellationToken threading, Task.WhenAll parallelization, SemaphoreSlim throttling, and Polly-based resilience policies (retry, timeout, circuit breaker), with each pattern linked to specific code examples and unit tests. Built on ASP.NET Core with 80% code coverage enforcement, the architecture emphasizes dependency injection, the decorator pattern for cross-cutting concerns (telemetry, caching, logging), and clean separation between a core utility library, web API, weather service integration, and comprehensive test suite. The repository uniquely implements "constitution-driven development," a formalized governance model that enforces coding standards and architectural patterns through automated CI/CD audits, constitution compliance checks, and structured PR reviews—demonstrated through audit reports and SpecKit agent workflows. The project includes interactive Scalar-powered API documentation with live testing capabilities, exposing endpoints for cancellation patterns, concurrency comparisons, remote operations, and real OpenWeatherMap API integration, making it valuable for enterprise teams adopting async patterns and organizations seeking to implement automated compliance frameworks. The 9 recent commits and maintained activity level indicate ongoing refinement, with contributions spanning C# (43.1%), HTML (34.1%), PowerShell (18.8%), and supporting configuration files that collectively demonstrate modern .NET development practices with constitutional enforcement mechanisms.

**Created**: 2022-08-07
**Last Modified**: 2026-02-10

---

### #26. [WebSpark.Bootswatch](https://github.com/markhazleton/WebSpark.Bootswatch)

Stars: 0 | Forks: 0 | Language: HTML | 5 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7124 KB | 🚀 1.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.Bootswatch

**WebSpark.Bootswatch** is a .NET 10-exclusive Razor Class Library that provides seamless integration of Bootswatch themes into ASP.NET Core applications, enabling developers to quickly implement modern, responsive UI theming with Bootstrap 5 as the foundation. The library offers comprehensive theming capabilities including dynamic theme switching, light/dark mode support, and built-in caching mechanisms through the `StyleCache` service, while providing convenient abstractions via extension methods and custom tag helpers like `<bootswatch-theme-switcher />` for straightforward UI implementation. Built primarily with HTML (63.8%), C# (28.6%), and JavaScript (2.6%), the project leverages the Microsoft.Extensions ecosystem and the external `WebSpark.HttpClientUtility` package to handle HTTP operations and dependency injection patterns within the ASP.NET Core middleware pipeline.

The architecture emphasizes production-readiness with comprehensive error handling, fallback mechanisms, and full XML documentation support for IntelliSense integration, while the recent major version 2.0 release represents a strategic decision to prioritize latest package versions and .NET 10 performance improvements over broad framework compatibility—a trade-off that simplifies maintenance and reduces testing complexity. The library targets ASP.NET Core developers seeking an opinionated, batteries-included solution for theme management rather than implementing theming from scratch, with particular utility for multi-tenant applications or projects requiring flexible visual branding and accessibility support through light/dark mode variants. While currently showing declining activity (5 commits in 90 days), the project maintains active curation with clear versioning strategy and documented migration paths, making it suitable for enterprise applications that prioritize modern .NET versions and staying current with framework releases.

**Created**: 2022-08-24
**Last Modified**: 2026-01-12

---

### #27. [TaskListProcessor](https://github.com/markhazleton/TaskListProcessor)

Stars: 0 | Forks: 0 | Language: C# | 12 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 1070 KB | 🚀 4.0 commits/month

**Quality**: ❌ License | ✅ Docs

# TaskListProcessor - Technical Summary

**TaskListProcessor** is an enterprise-grade .NET 10.0 library designed for orchestrating complex asynchronous operations with production-ready resilience, observability, and scheduling capabilities. The library provides a comprehensive framework for coordinating concurrent tasks—such as API calls, database queries, and microservice interactions—while maintaining fault isolation through circuit breaker patterns, comprehensive telemetry via OpenTelemetry integration, and advanced scheduling with dependency resolution and priority-based execution.

The project implements sophisticated architectural patterns including dependency injection integration with .NET's native DI container, the decorator pattern for pluggable cross-cutting concerns, interface segregation following SOLID principles, and thread-safe concurrent processing with configurable concurrency limits and load balancing. Key capabilities encompass type-safe result handling with categorized error management, task dependency resolution with topological sorting, streaming results via async enumerables, timeout/cancellation support, and health check monitoring—all backed by rich telemetry for metrics, tracing, and structured logging compatible with Serilog and Microsoft.Extensions.Logging.

The codebase is primarily C# (94.4%) with supporting PowerShell and Python tooling, demonstrates active development with 31 commits over the past year and accelerating momentum, and is positioned as a pre-release NuGet package targeting developers building high-throughput, fault-tolerant systems in microservices, data processing pipelines, and distributed applications. The project differentiates itself through enterprise-grade patterns, comprehensive documentation across multiple learning paths (beginner to advanced), practical examples including an interactive web demo, and production-focused guidance on performance tuning, memory optimization, and battle-tested architectural strategies.

**Created**: 2023-11-09
**Last Modified**: 2026-01-12

---

### #28. [TeachSpark](https://github.com/markhazleton/TeachSpark)

Stars: 0 | Forks: 0 | Language: C# | 1 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 30771 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# TeachSpark - Technical Summary

**TeachSpark** is an LLM-powered educational platform built on .NET 10 MVC that delivers personalized, adaptive learning experiences through AI-driven content delivery and real-time feedback mechanisms. The application combines a robust C# backend leveraging clean architecture principles with Entity Framework Core with a modern frontend stack featuring Webpack 5, Bootstrap 5, and ES6+ JavaScript, creating a responsive, high-performance learning environment. Key capabilities include AI-powered content adaptation, dynamic curriculum delivery, personalized learning pathways, comprehensive progress analytics, and an optimized build system with hot module replacement for efficient development workflows. The architecture demonstrates strong DevOps practices through automated code quality enforcement via Husky pre-commit hooks, ESLint/Prettier/Stylelint integration, and webpack-based asset optimization with content hashing and code splitting. The project's maturity is evident in its comprehensive documentation, structured project layout, and well-defined contribution guidelines, though the tech stack currency score of 50/100 suggests some dependencies may benefit from updates. TeachSpark targets educators and learning institutions seeking intelligent, personalized educational solutions that leverage Large Language Models to adapt content delivery based on individual student learning patterns and preferences.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 3 total (3 current, 0 outdated)

**Created**: 2025-06-19
**Last Modified**: 2026-01-12

---

### #29. [WebSpark.PrismSpark](https://github.com/markhazleton/WebSpark.PrismSpark)

Stars: 0 | Forks: 0 | Language: C# | 14 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 2272 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.PrismSpark

**WebSpark.PrismSpark** is a high-performance C#/.NET port of the popular PrismJS syntax highlighting library, providing advanced code tokenization and HTML rendering for 24 programming languages with support for .NET 10.0 LTS. The project implements a sophisticated architecture featuring a grammar-based tokenization engine, extensible plugin and hook systems, and a theme manager that supports both built-in and custom CSS-based themes, enabling developers to integrate professional syntax highlighting into web applications, documentation platforms, and code editors. Built with performance as a core concern, the library offers async processing, caching mechanisms, and flexible options for line highlighting, custom CSS classes, and metadata-driven customization, while maintaining full compatibility with ASP.NET MVC/Razor views through dependency injection integration. The codebase is well-engineered with a comprehensive 52-test MSTest suite covering grammar creation, tokenization, HTML generation, and end-to-end integration workflows, along with interactive demo pages including a live editor and markdown renderer powered by Markdig. What distinguishes this project is its seamless .NET ecosystem integration through service registration patterns, rendering capabilities that go beyond tokenization to produce fully styled HTML output, and a developer-friendly API that balances simplicity for common use cases with deep extensibility for advanced scenarios. This makes it particularly valuable for .NET developers building documentation systems, code review platforms, educational tools, or any application requiring embeddable, themeable syntax highlighting without JavaScript dependencies.

**Created**: 2025-05-27
**Last Modified**: 2026-02-11

---

### #30. [DecisionSpark](https://github.com/markhazleton/DecisionSpark)

Stars: 0 | Forks: 0 | Language: C# | 14 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 519 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ✅ Docs

# DecisionSpark - Technical Summary

**DecisionSpark** is a .NET 10-based decision routing engine that implements an intelligent conversation system to guide users through minimal questioning and recommend optimal outcomes using a config-driven architecture. The system combines a RESTful API with an interactive Razor Pages web interface, leveraging OpenAI integration for natural language question generation and answer parsing while maintaining conversation state through file-based session persistence. The architecture features modular service components including a RoutingEvaluator for rule-based decision logic, TraitParser for structured data extraction, and DecisionSpecLoader for JSON-based configuration management, enabling domain-specific decision flows without code modifications. Key capabilities include support for multiple question types (text, single-select, multi-select), Swagger/OpenAPI documentation, structured logging via Serilog, and intelligent rule evaluation with derived traits and tie-breaking mechanisms for complex decision scenarios. The project targets practical use cases such as activity planning (e.g., "Family Saturday Planner") and technical decision-making (e.g., "Tech Stack Advisor"), making it suitable for applications requiring interactive guidance systems, recommendation engines, or conversational decision support. Despite having zero stars and contributors at launch (created October 2025), the repository shows active development momentum with 14 commits over 90 days and 18 over the past year, indicating ongoing refinement and feature acceleration.

**Created**: 2025-10-29
**Last Modified**: 2025-12-27

---

### #31. [HttpClientDecoratorPattern](https://github.com/markhazleton/HttpClientDecoratorPattern)

Stars: 0 | Forks: 0 | Language: HTML | 1 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 2675 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: HttpClientDecoratorPattern

## Overview & Purpose
This repository is a production-ready implementation and reference guide for the Decorator Design Pattern applied to .NET HttpClient operations, published as the [WebSpark.HttpClientUtility](https://www.nuget.org/packages/WebSpark.HttpClientUtility/) NuGet package. It demonstrates how to elegantly compose cross-cutting concerns (telemetry, caching, resilience) around HTTP requests while maintaining clean architecture, testability, and SOLID principles.

## Key Features & Capabilities
The project implements a sophisticated decorator chain architecture that layers multiple concerns: a **Telemetry Decorator** for structured logging and performance metrics; a **Cache Decorator** for smart memory caching with configurable TTL and hit/miss tracking; and a **Polly Decorator** providing circuit breaker and retry policies with exponential backoff. The solution includes a responsive ASP.NET Core demonstration web application with real-world API integrations (NASA, Art Institute, Joke API) and advanced features like domain crawling with SignalR real-time updates, concurrent request throttling via SemaphoreSlim, and 26+ Bootswatch theme integration for modern UI presentation.

## Technology Stack & Architecture
Built on **.NET 10** with **C#**, **HTML/CSS**, and **JavaScript**, the project leverages **ASP.NET Core** for the web interface, **Polly** for resilience policies, **Serilog** for structured logging, **dependency injection** patterns, and **SignalR** for real-time communications. The architecture employs the Decorator Pattern through a composable chain where each decorator wraps `IHttpRequestResultService`, enabling clean separation of concerns and easy addition of new functionality without modifying existing code.

## What Makes It Unique
Unlike monolithic HttpClient wrapper implementations, this pattern-based approach provides genuine extensibility through composition rather than inheritance, addresses enterprise concerns (correlation IDs for distributed tracing, detailed telemetry, performance optimization), and serves dual purposes as both a production-ready NuGet package and an interactive reference implementation with comprehensive live demonstration pages showcasing real-world scenarios.

## Target Audience & Use Cases
Ideal for enterprise .NET developers building microservices, distributed systems, or applications requiring robust HTTP communication with built-in observability, resilience, and caching—from financial systems requiring circuit breakers and retry logic to data-heavy applications benefiting from strategic caching and request throttling.

**Created**: 2023-02-09
**Last Modified**: 2026-01-12

---

### #32. [Yelp.Api](https://github.com/markhazleton/Yelp.Api)

Stars: 0 | Forks: 0 | Language: C# | 1 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 462 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: Yelp.Api

**Yelp.Api** is a C# class library that provides a .NET wrapper for Yelp's v3 Fusion API, enabling developers to integrate comprehensive local business search and review functionality into .NET 6+ applications. The library abstracts the complexity of direct API calls by offering both simple convenience methods (e.g., `SearchBusinessesAllAsync()`) and advanced query capabilities through a `SearchRequest` object pattern, allowing developers to access business data, reviews, and information across over one million businesses in 32 countries. Built with C# (53.1%) as the primary language and supplemented with CSS, HTML, and a Dockerfile for deployment, the project follows a clean client-wrapper architecture pattern that hides HTTP communication details while exposing intuitive async/await-based methods for seamless integration into modern .NET applications. The codebase demonstrates good practices for API client libraries, including authentication via API key management through secrets files and support for both simple and parameterized search scenarios. While currently showing minimal GitHub visibility (0 stars/forks), the project maintains active development with recent commits and appears designed primarily for .NET developers seeking to leverage Yelp's business intelligence data without managing raw HTTP requests and JSON serialization. This library is particularly valuable for applications requiring location-based business discovery, ratings, and review aggregation features.

**Created**: 2022-08-10
**Last Modified**: 2026-01-12

---

### #33. [react-native-web-start](https://github.com/markhazleton/react-native-web-start)

Stars: 0 | Forks: 0 | Language: TypeScript | 1 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3184 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: react-native-web-start

## Overview
**react-native-web-start** is a production-ready, enterprise-grade starter template for building cross-platform applications using React Native Web, Vite, and TypeScript. It enables developers to write a single codebase that deploys across web (via browser), iOS, and Android platforms, eliminating code duplication while maintaining platform-specific optimizations.

## Core Functionality & Features
The project provides a comprehensive development environment with true cross-platform capability, featuring modern tooling including Vite for lightning-fast development with HMR, full TypeScript support with strict type checking, responsive adaptive UI design with Tailwind CSS and Sass preprocessing, built-in markdown documentation browser, and production-ready API integration with error handling. It includes automated CI/CD deployment to GitHub Pages, performance monitoring with bundle analysis, PWA capabilities, and comprehensive build automation scripts for asset management and documentation synchronization.

## Technology Stack & Architecture
Built on React 19.2.3 with React Native 0.83.1 and React Native Web 0.21.2, the project uses Vite 7.3.1 as the primary build tool with Metro 0.83.1 for mobile bundling, TypeScript 5.9.3 for type safety, and Tailwind CSS 4.1.18 with Sass 1.97.2 for styling. The architecture follows a monorepo pattern with segregated `packages/` containing shared components, web-specific, and mobile-specific configurations, alongside organized asset management, build automation scripts, and comprehensive documentation systems.

## Design Patterns & Notable Architecture
The repository employs a single-source-of-truth approach with shared components and business logic in `packages/shared/`, platform-specific entry points (`src/main.tsx` for web, `index.js` for mobile), and sophisticated build automation that includes dynamic build metadata generation, documentation sync, and asset pipeline management. The structure enables maximum code reuse while accommodating platform-specific requirements through configuration-driven approaches rather than code branching.

## Unique Value Proposition
Unlike simple boilerplates, this starter provides an enterprise-ready foundation with integrated documentation browser, optimized production builds, GitHub Pages CI/CD automation, security integration via Dependabot, and comprehensive development tooling. The project maintains clear separation between web and mobile concerns while maximizing code sharing, making it particularly valuable for teams building applications targeting multiple platforms simultaneously.

## Target Users & Use Cases
Ideal for development teams and individual developers building consumer or enterprise applications requiring cross-platform deployment (web + mobile), teams migrating from platform-specific codebases to unified development, and organizations seeking a modern, type-safe development experience with minimal setup overhead. The project particularly suits startups and established companies looking to reduce time-to-market by eliminating redundant platform-specific implementations.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 49 total (49 current, 0 outdated)

**Created**: 2025-07-26
**Last Modified**: 2026-01-14

---

### #34. [InquirySpark](https://github.com/markhazleton/InquirySpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 9371 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# InquirySpark - Technical Summary

**InquirySpark** is a .NET 10-based survey and inquiry management system that combines a modern MVC admin interface with a read-only SQLite persistence layer, designed to eliminate SQL Server dependencies while maintaining enterprise-grade data integrity. The solution comprises four interconnected projects: an ASP.NET Core admin portal styled with Bootstrap 5 and DataTables, an Entity Framework Core 10 repository layer providing abstraction over immutable SQLite databases, shared domain models and SDK objects, and a comprehensive MSTest unit test suite—all enforced through nullable reference types, XML documentation standards, and automatic npm asset pipelines. Key architectural innovations include a `SqliteOptionsConfigurator` pattern for centralized connection management with read-only mode enforcement, primary constructor usage for dependency injection, and an immutable database strategy that prevents schema mutations while supporting simultaneous application instances. The technology stack spans C# (39.9%), HTML/Bootstrap UI (33.5%), T-SQL schema definitions (21.7%), PowerShell automation (3.7%), and JavaScript asset management (1.2%), with no external CDN dependencies and all front-end libraries bundled locally via npm. The project targets teams seeking lightweight, self-contained inquiry systems that prioritize data immutability, simplified deployment (no database server required), and compliance-friendly audit trails through read-only data access patterns. Despite minimal recent activity (zero commits in 90 days), the codebase demonstrates mature architectural decisions and comprehensive documentation, positioning it as a viable template for organizations migrating from traditional SQL Server-based survey platforms to containerizable, cloud-native alternatives.

**Created**: 2023-10-24
**Last Modified**: 2025-12-07

---

### #35. [TriviaSpark](https://github.com/markhazleton/TriviaSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 27238 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# TriviaSpark - Technical Summary

**TriviaSpark** is a multiplayer trivia game application developed as an experimental proof-of-concept using ChatGPT assistance, designed to integrate public Trivia APIs with web and mobile platforms. The application's core functionality encompasses user registration systems, real-time trivia gameplay with multiple-choice questions, competitive leaderboards, and admin-level question database management capabilities with customizable UI options. The tech stack is built primarily on **C# (61.1%)** for backend logic, complemented by **HTML (26.5%)**, **CSS (12.3%)**, and minimal **JavaScript (0.1%)**, suggesting an ASP.NET-based web application architecture with potential Xamarin or similar framework support for mobile deployment. The application follows a traditional three-tier architecture pattern with API integration layers for third-party trivia data sources, user management systems, and competitive ranking algorithms. Notably, this project serves as a documented case study in AI-assisted software development, with extensive external documentation chronicling the ChatGPT-driven development process, making it valuable as both a functional trivia platform and an educational resource. The target demographic spans tech-savvy users aged 18-95 seeking competitive, engaging trivia experiences, though the project currently shows minimal maintenance activity (0 commits in 90 days) and declining engagement patterns, indicating it may be in an archived or demonstration phase rather than active production use.

**Created**: 2023-02-22
**Last Modified**: 2025-12-02

---

### #36. [DataAnalysisDemo](https://github.com/markhazleton/DataAnalysisDemo)

Stars: 0 | Forks: 0 | Language: Visual Basic .NET | 0 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 12926 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: DataAnalysisDemo

**DataAnalysisDemo (DAWPM)** is a comprehensive ASP.NET WebForms 4.8 web application designed to transform CSV data files into interactive visualizations, pivot tables, and detailed analytics through a modern, responsive interface. The application combines a legacy VB.NET backend (69.8% of codebase) with a contemporary client-side architecture featuring Bootstrap 5.3.8, jQuery 3.7.1, DataTables 2.3.3, and advanced charting libraries (D3.js, C3.js, and Microsoft Chart Controls), demonstrating a pragmatic approach to modernizing enterprise web applications without complete framework migration.

Core functionality includes CSV file processing via a custom GenericParser library with real-time statistical analysis (min/max values, unique counts, data type detection), a drag-and-drop pivot table engine with multiple aggregation functions and export capabilities (Excel, CSV, JSON), and 15+ dynamic chart types with 3D/2D rendering options and PNG export. The architecture employs a modern build pipeline using Webpack 5 and npm for asset bundling, replacing traditional dependency management, while maintaining separation between client-side source files and built production assets, enabling efficient development workflows.

The project demonstrates advanced data processing patterns including memory-efficient streaming for large datasets, responsive Bootstrap 5 components for enhanced UX, and sophisticated client-side state management through localStorage for pivot configurations. With minimal recent activity (0 commits in 90 days, tech stack currency of 50/100), the codebase appears stable but aging, making it particularly valuable as an educational resource for developers working with legacy ASP.NET systems or those learning data visualization techniques with jQuery and modern JavaScript charting libraries.

Target users include analysts, data engineers, and business intelligence practitioners who need rapid exploration of CSV datasets without server-side infrastructure, as well as developers building data-driven applications seeking patterns for integrating modern frontend tooling with traditional ASP.NET WebForms backends.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 24 total (24 current, 0 outdated)

**Created**: 2023-04-20
**Last Modified**: 2025-12-03

---

### #37. [PHPDocSpark](https://github.com/markhazleton/PHPDocSpark)

Stars: 0 | Forks: 0 | Language: PHP | 0 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 2727 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# PHPDocSpark: Technical Summary

PHPDocSpark is an open-source PHP documentation and data exploration platform that demonstrates modern hybrid web development practices by integrating a traditional PHP 8.2+ backend with a contemporary Vite-powered asset pipeline. The project serves as a comprehensive reference implementation showcasing markdown-based documentation management with full-text search, interactive data visualization (CSV analysis, Chart.js integration), SQLite database operations, GitHub API integration, and responsive Bootstrap 5 UI components—all built on a clean architecture pattern that separates server-side logic from client-side asset compilation. Key architectural innovations include its dual-build system (PHP backend + Vite frontend toolchain), content caching mechanisms, API rate-limiting strategies, and Azure Pipeline deployment automation, making it equally valuable as an educational resource for developers learning modern PHP patterns and as a functional documentation platform for technical teams. The tech stack leverages DataTables for interactive grids, Parsedown for markdown parsing, SCSS for advanced styling, and comprehensive DevOps tooling (ESLint, Prettier, Azure hosting), targeting PHP developers, full-stack engineers, and technical writers seeking production-ready reference implementations. With 27 dependencies, minimal recent activity (0 commits in 90 days but 36 in the past year), and moderate tech stack currency (50/100), the project represents a stable, mature implementation that successfully demonstrates bridging traditional server-side PHP development with modern JavaScript tooling ecosystems.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2023-09-08
**Last Modified**: 2025-08-18

---


---

## Report Metadata

- **Generation Time**: 1.9 seconds
- **SVGs Generated**: 6/6
- **Total API Calls**: 0
- **Total AI Tokens**: 90,227
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
*Last updated: 2026-03-15*