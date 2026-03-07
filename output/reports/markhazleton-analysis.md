# GitHub Profile: markhazleton

**Generated**: 2026-03-07 15:23:31 UTC
**Report Version**: 1.0.0
**Repositories Analyzed**: 36
**AI Summary Rate**: 100.0%

> 💡 **Navigation**: [Profile Overview](#profile-overview) | [Top Repositories](#top-36-repositories) | [Metadata](#report-metadata)

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

## Top 36 Repositories

### #1. [github-stats-spark](https://github.com/markhazleton/github-stats-spark)

Stars: 0 | Forks: 0 | Language: Python | 164 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 12093 KB | 🚀 54.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: github-stats-spark

## Overview

Stats Spark is a comprehensive GitHub analytics and visualization platform that automatically generates professional SVG statistics and AI-powered repository analysis reports from GitHub user activity. The project combines real-time data collection via the GitHub API with intelligent analysis and beautiful visual rendering to provide developers, teams, and open-source maintainers with actionable insights into their coding patterns, technology usage, and project health.

## Key Features & Capabilities

The platform delivers three core components: (1) **SVG Profile Statistics** featuring automated daily updates with five visualization categories (overview dashboard, commit heatmap, language breakdown, streak tracking, and personality-driven achievements), including a proprietary "Spark Score" metric (0-100) that weighs consistency, volume, and collaboration; (2) **AI-Powered Repository Analysis** using Claude Haiku for intelligent technical summaries with a three-tier fallback system achieving 97%+ success rates, coupled with composite ranking algorithms that balance popularity (30%), recent activity (45%), and repository health (25%); and (3) **Interactive Mobile-First Dashboard** with responsive design (320px-768px viewports), touch-optimized controls, Chart.js visualizations, and multi-repository comparison capabilities.

## Technology Stack & Architecture

Built primarily in **Python 3.11+** (51.4%) with supporting JavaScript (25.8%), CSS (12.3%), PowerShell (8.8%), and HTML (1.7%), the project leverages **PyGithub** for API access, **PyYAML** for configuration management, **svgwrite** for vector graphics generation, **requests** for HTTP operations, and **python-dateutil** for temporal analysis. The architecture employs intelligent caching mechanisms to reduce API calls by 80-95%, implements exponential backoff rate-limit handling, and uses GitHub Actions workflows for automated midnight UTC updates. The modular design separates concerns between data collection, analysis, visualization rendering, and web presentation layers.

## Notable Features & Differentiation

The project stands out through its sophisticated composite scoring algorithms that move beyond simple metrics counting, enterprise-grade caching strategies optimized for GitHub's API constraints, and integration of generative AI for repository summarization rather than basic metadata extraction. The interactive dashboard implements accessibility best practices (WCAG 2.1 AA compliance with screen reader support), mobile-optimized UX patterns, and performance targets (<2s First Contentful Paint on 3G), while the personality-driven fun stats system adds engagement through coded achievements based on coding patterns. The platform supports zero-maintenance operation—configure once and receive automatic daily updates indefinitely through GitHub Pages deployment.

## Target Users & Use Cases

Stats Spark serves developers seeking professional GitHub portfolio enhancements, technical teams analyzing contributor productivity and technology diversity, open-source maintainers tracking project momentum and community engagement, and technical leaders evaluating development patterns across portfolios. Its accessibility and automation make it particularly valuable for maintaining up-to-date community presence without ongoing manual effort, while the enterprise-ready architecture supports organizational deployment with flexible YAML configuration and modular extensibility for custom implementations.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 10 total (10 current, 0 outdated)

**Created**: 2025-12-28
**Last Modified**: 2026-03-07

---

### #2. [mark-hazleton-s-notes](https://github.com/markhazleton/mark-hazleton-s-notes)

Stars: 0 | Forks: 0 | Language: TypeScript | 114 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 278351 KB | 🚀 38.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Mark Hazleton's Notes

This repository is a modern full-stack personal portfolio and technical blog site built for Mark Hazleton, a Technical Solutions Architect, combining long-form writing on cloud architecture and engineering practices with a live GitHub metrics dashboard and project portfolio. The architecture leverages React 19 with TypeScript and Vite 7 to deliver server-side rendering (SSR) capabilities alongside static prerendering, generating a fully optimized static site published to Azure Static Web Apps at markhazleton.com. Key features include a Markdown-based blog content pipeline with automatic RSS feed generation (including Media RSS namespace for optimized image thumbnails), live repository metrics fetched from an external data source, SEO optimization through dynamic sitemap and canonical URL management, and a responsive UI built with Tailwind CSS, shadcn/ui, and Radix UI components. The build pipeline employs sophisticated automation scripts for image optimization (WebP conversion, thumbnail generation), SEO asset generation, and dynamic HTML prerendering across all routes, ensuring fast first-paint performance by inlining repository stats during the build phase. What distinguishes this project is its production-grade architecture balancing developer experience (local dev server, type safety, linting) with content management simplicity (JSON metadata + Markdown files) and sophisticated performance optimization (static prerendering, image optimization, cached GitHub data), making it a reference implementation for technical personal brands. The project targets developers, architects, and technical professionals seeking an example of modern JAMstack practices combined with real-world content delivery and live data integration patterns.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 59 total (59 current, 0 outdated)

**Created**: 2026-01-10
**Last Modified**: 2026-03-07

---

### #3. [MuseumSpark](https://github.com/markhazleton/MuseumSpark)

Stars: 0 | Forks: 0 | Language: Python | 62 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 21243 KB | 🚀 20.7 commits/month

**Quality**: ❌ License | ✅ Docs

# MuseumSpark: Technical Summary

**MuseumSpark** is an intelligent museum discovery and travel planning platform that transforms the Walker Art Center Reciprocal Program's membership directory into a data-rich, curated resource for art enthusiasts across North America. The project maintains a dataset of 1,269 museums with multi-phase enrichment pipelines that progressively augment records with structured metadata from Wikidata, Wikipedia, official websites, and expert scoring systems—currently at 0.08% enrichment completion, reflecting its nascent but highly active development stage. The architecture employs a hybrid frontend-backend approach using React 19 with Vite for a static browsing experience deployed on GitHub Pages, while leveraging Python 3.11+ with Pydantic for robust data validation, schema enforcement, and ETL orchestration across multiple external data sources. Key differentiators include a transparent data quality dashboard tracking enrichment progress, a formalized JSON Schema validation pipeline enforcing data integrity, and a strategic roadmap toward AI-assisted content generation and personalized trip planning (Phase 4) with FastAPI backend and LLM-powered museum analysis. The project demonstrates sophisticated engineering practices including multi-phase enrichment strategies, evidence-based data quality rules ("Never Replace Known With Null"), and automated metadata extraction through web scraping and structured API integration. Target users are art-focused travelers seeking intelligent museum recommendations, curated itineraries, and strategic visit planning across North America, with the platform evolving from a static discovery tool to an interactive, AI-enhanced travel companion by Q4 2026.

**Created**: 2026-01-15
**Last Modified**: 2026-02-20

---

### #4. [UISampleSpark](https://github.com/markhazleton/UISampleSpark)

Stars: 8 | Forks: 4 | Language: HTML | 54 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 30713 KB | 🚀 18.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: UISampleSpark

**UISampleSpark** is a comprehensive educational .NET 10 (ASP.NET Core) web application that serves as a comparative reference implementation for modern front-end UI patterns and technologies. The project demonstrates seven distinct UI approaches—MVC, Razor Pages, vanilla JavaScript SPA, React 18, Vue 3, htmx, and Blazor Server—all operating against a shared Employee/Department domain model, enabling side-by-side evaluation of architectural trade-offs and developer experience across different paradigms.

The application showcases production-grade practices including RESTful API design with Swagger/OpenAPI documentation, Entity Framework Core with an in-memory database, service-based repository patterns with dependency injection, and a sophisticated Bootstrap 5-based theming system with dynamic Bootswatch theme switching capabilities. The technology stack spans C#, HTML, JavaScript, and CSS, leveraging modern libraries such as React 18 with hooks, Vue 3 Composition API, and htmx for server-driven hypermedia interactions, while the backend utilizes Application Insights for observability and health check endpoints.

Architecturally, the project emphasizes clean separation of concerns through layered organization (UI, Core domain models, Data layer with EF Core services) combined with comprehensive unit testing projects, automated CI/CD pipelines via GitHub Actions (including Docker image builds and CodeQL security analysis), and multi-platform deployment examples targeting both Azure App Service and containerized environments. UISampleSpark is designed primarily for educational purposes, making it invaluable for developers seeking to understand comparative UI framework patterns, ASP.NET Core best practices, cloud deployment strategies, and DevOps automation—with its active maintenance history (54 commits in 90 days, progression from .NET 5 through .NET 10) demonstrating sustained commitment to staying current with the .NET platform evolution.

**Created**: 2019-04-25
**Last Modified**: 2026-02-08

---

### #5. [git-spark](https://github.com/markhazleton/git-spark)

Stars: 0 | Forks: 0 | Language: TypeScript | 15 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 1582 KB | 🚀 5.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Git Spark - Technical Summary

**Git Spark** is a TypeScript-based CLI tool and Node.js library that analyzes Git repository commit history to generate interactive analytics reports and insights into contributor activity, code changes, and development patterns. The project provides multiple output formats (HTML, JSON, CSV, Markdown) with a sophisticated interactive HTML dashboard featuring multi-series timeline charts, contribution heatmaps, risk factor analysis, governance metrics, and dark mode support, all delivered as self-contained, security-hardened artifacts with strict Content Security Policy implementation and no external dependencies for rendering.

The tool combines a command-line interface (powered by Commander.js) with a programmatic API, offering flexible analysis options including date-range filtering, author/path filtering, timezone-aware daily trend analysis, email redaction for privacy, and optional Azure DevOps integration for pull request analytics. The architecture leverages modern TypeScript practices with progress indication (Ora spinners), formatted console output (Chalk, Boxen), and semantic versioning support, while maintaining a relatively minimal dependency footprint (19 total dependencies) for a data processing application of this scope.

Key differentiators include its focus on Git-only data sources for analytical integrity (avoiding speculation beyond what commits reveal), progressive UI patterns for handling large datasets efficiently, transparent metric documentation explaining limitations, and air-gapped compatibility with fully embedded analytics requiring no external API calls during report viewing. The project targets development teams, engineering managers, and governance-focused organizations seeking repository health assessments and contributor activity tracking, with an active development status showing 125 commits over the past year despite minimal current adoption (0 stars/forks), suggesting it's a relatively new or niche offering still building visibility.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 19 total (19 current, 0 outdated)

**Created**: 2025-09-29
**Last Modified**: 2026-02-20

---

### #6. [JsBootSpark](https://github.com/markhazleton/JsBootSpark)

Stars: 0 | Forks: 0 | Language: JavaScript | 22 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 3448 KB | 🚀 7.3 commits/month

**Quality**: ❌ License | ✅ Docs

# JsBootSpark: Technical Summary

## Overview

JsBootSpark is a production-ready, full-stack starter kit designed to accelerate development of modern, responsive web applications by combining Express.js backend with Bootstrap 5 frontend. The project serves as a comprehensive boilerplate that eliminates repetitive setup work while maintaining best practices for security, performance, and developer experience.

## Key Features & Capabilities

The starter kit provides an extensive feature set including hot-reload development environments, dark/light mode theming with system preference detection, and a 2,000+ Bootstrap Icons library. It implements security best practices through Helmet.js integration, rate limiting, and input validation, while offering performance optimization via compression middleware and responsive image handling. Notable capabilities include dynamic page generation from single templates, CSV-to-JSON conversion for data management, automated CI/CD pipelines with GitHub Actions, and Docker containerization for consistent deployment across environments.

## Technology Stack

The project leverages **Node.js 18+** with **Express.js 5.1.0** for the backend, **Bootstrap 5.3.7** and **SASS** for frontend styling, and **EJS 3.1.10** as the template engine. The tech stack includes testing infrastructure (Jest), code quality tools (ESLint, Prettier), and deployment integrations (GitHub Pages, Docker). The codebase is written primarily in JavaScript (66.8%) with EJS templates (21.1%), PowerShell build scripts (9.8%), and minimal TypeScript/SCSS.

## Architectural Approach

The project follows a modular, component-driven architecture that emphasizes reusability and maintainability. It implements separation of concerns with dedicated template engines, middleware for cross-cutting concerns (compression, security), and a structured build system supporting both static site generation and dynamic page rendering. The infrastructure-as-code approach via Docker and GitHub Actions enables reproducible deployments and seamless CI/CD integration.

## Unique Characteristics

JsBootSpark stands out through its **dual-mode capability**—supporting both static site generation for performance-critical deployments and dynamic rendering for interactive applications. The automated build system generates 100+ pages from a single template, reducing maintenance overhead, while the CSV-to-JSON conversion simplifies data-driven content. The project includes comprehensive AI-assisted development documentation through Copilot sessions, providing decision context and architectural planning artifacts alongside traditional documentation.

## Target Users & Use Cases

Ideal for teams building SaaS platforms, internal tools, marketing websites, and dashboard applications requiring rapid prototyping without sacrificing production quality. The starter kit particularly benefits full-stack JavaScript developers, small teams lacking DevOps infrastructure, and organizations prioritizing rapid time-to-market while maintaining security and performance standards. Its 90-day activity pattern and consistent 22-commit recent history indicate active maintenance and refinement.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 30 total (30 current, 0 outdated)

**Created**: 2022-06-06
**Last Modified**: 2026-01-31

---

### #7. [TailwindSpark](https://github.com/markhazleton/TailwindSpark)

Stars: 0 | Forks: 0 | Language: HTML | 28 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 3305 KB | 🚀 9.3 commits/month

**Quality**: ❌ License | ✅ Docs

# TailwindSpark - Technical Summary

**TailwindSpark** is a comprehensive, production-ready design system and component showcase built as a modern React TypeScript monorepo that demonstrates Tailwind CSS v4 capabilities and best practices. The project serves as both a portfolio piece and a reusable foundation, featuring a complete design system with shared packages (design tokens and UI components), an interactive demo application, and extensive documentation—all organized using Turborepo for optimized builds and developer experience.

The repository showcases advanced modern web development practices including React 19.1 with concurrent features, TypeScript 5.9 strict mode, Vite 7.1 for lightning-fast HMR, and Tailwind CSS 4.1.18 with CSS custom properties. Key features include a fully responsive design system with dark mode support, WCAG 2.1 AA accessibility compliance, real-time performance monitoring via Web Vitals, keyboard navigation with search shortcuts, interactive component demonstrations (buttons, forms, cards, modals, dashboards), and multiple showcase sections covering e-commerce, marketing, analytics, and user management patterns.

The architecture employs monorepo patterns with shared packages, automated testing using Vitest with coverage reporting, comprehensive linting and type checking (ESLint 9.39 + Prettier 3.7), and a complete CI/CD pipeline via GitHub Actions that handles automated testing, building, and deployment to GitHub Pages. The project distinguishes itself through 100% TypeScript implementation with strict type safety, accessibility testing with jest-axe, security scanning with CodeQL and Dependabot, performance monitoring with bundle analysis, and production-ready features like error boundaries, service worker offline support, SEO optimization, and resource optimization with CDN preconnections.

Designed for developers, designers, and teams seeking a modern, well-documented design system foundation, TailwindSpark serves as both an educational resource for contemporary React/TypeScript/Tailwind patterns and a ready-to-fork starter for building scalable web applications with enterprise-grade quality standards and developer experience.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 26 total (26 current, 0 outdated)

**Created**: 2025-07-29
**Last Modified**: 2026-03-03

---

### #8. [WebSpark.HttpClientUtility](https://github.com/markhazleton/WebSpark.HttpClientUtility)

Stars: 0 | Forks: 0 | Language: C# | 18 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2336 KB | 🚀 6.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.HttpClientUtility

## Overview & Purpose

WebSpark.HttpClientUtility is a production-ready, opinionated wrapper around .NET's HttpClient that dramatically reduces boilerplate setup for enterprise HTTP communication. It abstracts away complex resilience, caching, correlation tracking, and observability concerns into a single-line DI registration (`AddHttpClientUtility()`), enabling developers to implement reliable distributed HTTP calls without manually wiring Polly policies, logging middleware, or OpenTelemetry instrumentation.

## Core Features & Capabilities

The library provides integrated resilience patterns (retry and circuit breaker via Polly), intelligent in-memory response caching with configurable TTL, automatic correlation ID generation for request tracing across service boundaries, structured logging with rich contextual data, and built-in OpenTelemetry tracing for observability in microservice architectures. As of v2.0, the project splits into two focused NuGet packages: the core `WebSpark.HttpClientUtility` (163 KB) for HTTP utilities and a separate `WebSpark.HttpClientUtility.Crawler` package (75 KB) for web scraping, robots.txt parsing, and sitemap generation—allowing consumers to install only what they need.

## Technology Stack & Architecture

Built exclusively for modern .NET LTS (8, 9, 10), the library is implemented in C# (73.2% of codebase) with comprehensive test coverage (237+ unit tests across three frameworks achieving 100% pass rate). The architecture leverages dependency injection patterns, sealed classes for trimming/AOT compatibility, and follows semantic versioning with strict backward compatibility guarantees. Supporting infrastructure includes GitHub Actions CI/CD, Source Link for debuggable symbol packages (.snupkg), package baseline validation, and zero-warning builds enforced via `TreatWarningsAsErrors=true`.

## Design Philosophy & Differentiators

The project embraces a "convention over configuration" approach, providing sensible defaults while remaining configurable for advanced scenarios—positioning it between raw HttpClient (maximum control, maximum boilerplate) and declarative frameworks like Refit (type-safe but less flexible). It explicitly targets microservices and distributed systems where correlation IDs and tracing are prerequisites, differentiating from general-purpose clients by bundling these observability concerns as first-class citizens rather than afterthoughts.

## Target Users & Use Cases

Ideal for teams building resilient microservices architectures, background workers, and web crawlers within organizations standardized on .NET 8+ LTS. The library suits scenarios requiring automatic rate-limit compliance through caching, structured correlation tracing across service boundaries, and production-grade error handling—without accepting the declarative constraints of Refit or the manual complexity of raw HttpClient + Polly composition.

## Project Health

Despite zero GitHub stars/forks and recent activity decline (18 commits in 90 days vs. 105 in 365 days), the project demonstrates strong engineering discipline: MIT-licensed, actively maintained, backed by comprehensive testing infrastructure, and publicly documented. The declining commit frequency suggests maturity and stability rather than abandonment, with the repository serving as a production utility likely used internally or by a focused audience.

**Created**: 2025-05-03
**Last Modified**: 2026-02-27

---

### #9. [ReactSparkPortfolio](https://github.com/markhazleton/ReactSparkPortfolio)

Stars: 0 | Forks: 0 | Language: CSS | 24 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 43361 KB | 🚀 8.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: ReactSparkPortfolio

**ReactSparkPortfolio** is a production-ready, enterprise-grade developer portfolio application built with React 19, TypeScript, and Vite that demonstrates modern frontend engineering best practices and cloud-native deployment patterns. The project serves dual purposes as both a personal portfolio showcase and a comprehensive reference implementation for scalable web applications, featuring real-time capabilities via SignalR, responsive UI with Bootstrap 5 and custom SCSS styling, and a microservices-oriented architecture integrating external APIs (OpenWeather, JokeAPI, RSS feeds) through a serverless backend powered by Azure Functions and Static Web Apps.

Key technical features include full TypeScript implementation with strict type safety, lazy-loaded components with code splitting for optimal performance, dark/light theme switching with persistent state management via React Context API, WCAG 2.1 AA accessibility compliance, and dual deployment strategies across Azure Static Web Apps and GitHub Pages with automated CI/CD via GitHub Actions. The architecture employs a frontend-first design that pulls dynamic content from external sources (markhazleton.com API), implements a CSP-aware content security strategy, and integrates interactive elements like real-time chat, live weather widgets with Leaflet maps, and searchable project portfolios with XML parsing for RSS feeds.

The technology stack emphasizes modern tooling and developer experience, leveraging Vite for extremely fast builds, ESLint and Prettier for code quality, date-fns for date utilities, axios for HTTP requests, and a comprehensive documentation structure covering security, deployment, and architectural decisions. The project is notable for its attention to production-grade concerns—including detailed security documentation addressing Content Security Policy complexities, semantic HTML and ARIA implementation for accessibility, and structured data with JSON-LD for SEO optimization—making it an ideal reference for developers seeking to understand enterprise React patterns, serverless architectures, and cloud-native deployment practices.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 46 total (46 current, 0 outdated)

**Created**: 2024-10-11
**Last Modified**: 2026-03-07

---

### #10. [WebSpark](https://github.com/markhazleton/WebSpark)

Stars: 1 | Forks: 0 | Language: C# | 25 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 69006 KB | 🚀 8.3 commits/month

**Quality**: ❌ License | ❌ Docs

Based on the detailed README and repository information, here's a comprehensive technical summary of WebSpark:

WebSpark is an ambitious, modular web application suite built with .NET 9 and Bootstrap 5, focusing on creating specialized web tools across multiple domains including prompt management, recipe tracking, and quiz creation. The project stands out for its rigorous spec-driven development workflow, which implements a comprehensive SpecKit command system that guides feature development through systematic specification, planning, risk assessment, implementation, and review stages. The architecture is designed to be scalable and versatile, spanning seven distinct modular areas (PromptSpark, RecipeSpark, TriviaSpark, WebCMS, AsyncSpark, Admin, Identity) with a strong emphasis on modern web technologies and advanced SEO optimization.

Key technical highlights include:
- Advanced SEO optimization with comprehensive metadata management
- Structured data implementation using Schema.org
- Multi-engine webmaster tool integration
- Performance monitoring with Web Vitals tracking
- Automated risk assessment through the innovative `/speckit.critic` command
- Strict branch protection and specification-driven development workflow

The project's unique selling point is its meticulous approach to feature development, leveraging automated tools to minimize technical debt, identify potential risks early, and ensure high-quality, production-ready code. By implementing a thorough specification and validation process, WebSpark aims to reduce implementation risks and maintain a high standard of software engineering practices.

Technologies used include:
- Backend: .NET 9, ASP.NET Core MVC
- Frontend: Bootstrap 5
- Languages: C#, HTML, SCSS, JavaScript
- Development Workflow: Custom SpecKit command system
- SEO & Performance: Schema.org, Google Analytics 4, Application Insights

The repository demonstrates a sophisticated approach to web application development, combining modular design, comprehensive SEO strategies, and a robust development workflow that prioritizes quality and risk mitigation.

**Created**: 2024-01-11
**Last Modified**: 2026-01-29

---

### #11. [WebProjectMechanics](https://github.com/markhazleton/WebProjectMechanics)

Stars: 3 | Forks: 0 | Language: Visual Basic .NET | 9 commits (90d)

👥 0 contributors | 🌐 10 languages | 💾 52405 KB | 🚀 3.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebProjectMechanics

**WebProjectMechanics** is a multi-tenant, multi-domain content management system undergoing a greenfield rebuild from legacy ASP.NET Web Forms to modern .NET 9, designed to serve 36+ independent websites from a single application instance by publishing pre-rendered static HTML from SQLite databases. The system employs a plugin-based architecture with domain-specific modules (CMS, Mineral Collection, Recipes) and uses physical database file isolation rather than traditional tenant ID columns, eliminating the need for tenant-aware queries throughout the codebase. Built on ASP.NET Core 9 Minimal APIs with Scriban templating, Caddy as a reverse proxy with auto-SSL, and EF Core 9 for data access, the architecture prioritizes simplicity and cost-efficiency by running on a single ~$10/month Azure Linux VM while delegating static file serving and SSL termination to Caddy. The repository includes comprehensive documentation of both the legacy system and implementation roadmap, a data migration tool for transitioning from MS Access, and an organized project structure with shared core libraries, domain-specific implementations, and test coverage via xUnit. This approach is notable for its pragmatic tenant isolation strategy and publish-to-static pattern, which trades runtime flexibility for guaranteed performance, security isolation, and reduced infrastructure complexity—making it well-suited for small-to-medium multi-site operations requiring high availability at minimal operational cost.

**Created**: 2017-09-19
**Last Modified**: 2026-02-19

---

### #12. [RESTRunner](https://github.com/markhazleton/RESTRunner)

Stars: 2 | Forks: 1 | Language: C# | 16 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 426 KB | 🚀 5.3 commits/month

**Quality**: ❌ License | ✅ Docs

RESTRunner is a comprehensive .NET 10 solution designed for automated REST API testing, performance benchmarking, and regression testing, with a primary focus on integrating Postman collections into a robust testing framework. The project offers a multi-faceted approach to API validation, featuring capabilities such as automated test execution, performance analysis, load testing, and detailed reporting through both console and web interfaces. Built using C# and leveraging .NET 10's latest performance improvements, the framework supports cross-platform testing, provides interactive web-based testing via Razor Pages, and includes a sample CRUD API for demonstration purposes. Its architecture emphasizes modularity, performance optimization, and comprehensive test coverage, with notable features like CSV result exports, response time percentile tracking, and built-in performance metrics. RESTRunner is particularly valuable for developers, QA engineers, and API developers seeking a modern, high-performance testing solution that can seamlessly integrate existing Postman collections and provide in-depth insights into API behavior and performance characteristics.

**Created**: 2021-09-30
**Last Modified**: 2026-01-12

---

### #13. [ConcurrentProcessing](https://github.com/markhazleton/ConcurrentProcessing)

Stars: 0 | Forks: 0 | Language: C# | 19 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 145 KB | 🚀 6.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: ConcurrentProcessing

**ConcurrentProcessing** is a production-ready, high-performance concurrent task processing framework built for .NET 10 that provides fine-grained control over parallel task execution through a generic, extensible abstract base class architecture. The framework leverages semaphore-based throttling to precisely manage concurrency limits while maintaining comprehensive performance metrics tracking, including task duration, wait times, and throughput analysis—enabling developers to execute and monitor large-scale parallel operations with minimal overhead. Built entirely in C# with a focus on modern .NET features (C# 12+ primary constructors, nullable reference types, pattern matching), the architecture implements the Template Method and Resource Pool patterns, allowing users to inherit from `ConcurrentProcessor<T>` and customize processing logic while the framework handles concurrency orchestration, metric collection, and statistical analysis automatically. The project is particularly notable for its dual purpose as both a demonstration of advanced concurrent programming patterns and a reusable framework, complemented by comprehensive CI/CD pipelines (GitHub Actions), detailed documentation, and educational resources that make it valuable for developers learning TPL (Task Parallel Library) concepts and concurrent system design. Benchmark results demonstrate linear scalability with configurable concurrency—processing 100 tasks at 10x concurrency achieves ~250ms total execution versus ~1500ms at sequential rates—making it suitable for CPU-bound workloads, I/O-bound operations, and scenarios requiring controlled parallelism with detailed performance observability.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 2 total (2 current, 0 outdated)

**Created**: 2023-09-18
**Last Modified**: 2026-01-22

---

### #14. [markhazleton](https://github.com/markhazleton/markhazleton)

Stars: 0 | Forks: 0 | Language: Unknown | 11 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 6595 KB | 🚀 3.7 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: markhazleton Repository

This repository serves as Mark Hazleton's personal portfolio and learning archive, functioning as a curated collection of demonstration projects and technical explorations that showcase continuous professional development across multiple technology domains. The primary offering is a hub linking to feature projects including **WebSpark** (a comprehensive web application framework for hosting demo applications) and **ReactSpark** (a modern React application built with Vite and deployed on Azure Static Web Applications), alongside an integrated blog documenting technical insights on software development practices, AI-assisted development, and architectural decision-making. The technology stack demonstrates expertise across web development (React, Vite), cloud platforms (Azure), API design (Postman integration), and DevOps practices (Azure DevOps), with a clear emphasis on modern full-stack development patterns and deployment automation. The repository architecture employs GitHub Actions for dynamic content generation (as evidenced by the stats spark visualizations) and follows a hub-and-spoke model where this repository serves as a central aggregator linking to specialized learning projects rather than containing monolithic application code. What distinguishes this repository is its explicit framing as a **lifelong learning journal**—each project represents a deliberate exploration into specific technologies or architectural patterns, making it valuable for both personal skill documentation and community-oriented knowledge sharing on topics ranging from spec-driven AI development to fork management automation. The project targets intermediate-to-advanced developers and technical leaders interested in pragmatic software development approaches, governance practices, and modern development methodologies.

**Created**: 2021-04-17
**Last Modified**: 2026-03-01

---

### #15. [SupportSpark](https://github.com/markhazleton/SupportSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 23 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 1856 KB | 🚀 7.7 commits/month

**Quality**: ❌ License | ❌ Docs

# SupportSpark - Technical Summary

**SupportSpark** is a compassionate web platform designed to help individuals managing life challenges (health issues, transitions, personal journeys) maintain connection with their support network by sharing updates efficiently. Members create and post journey updates while invited supporters view updates and provide encouragement through organized threaded conversations, eliminating the exhaustion of communicating separately with multiple people.

The application employs a modern full-stack TypeScript architecture with **React 19 + Vite** on the frontend leveraging **shadcn/ui and Radix** components styled with **Tailwind CSS 4** for an accessible, calming interface, paired with an **Express 5** backend using **Passport.js** for authentication and **Zod** for runtime validation. State management utilizes **TanStack React Query** for server synchronization, **Wouter** for lightweight routing, and **Framer Motion** for smooth animations, with data persisted through a JSON-based storage layer in development.

The architecture emphasizes role-based access control (members vs. supporters), invitation-only networks for privacy, and type safety throughout the stack with strict TypeScript and shared schemas between client and server. Notable features include a fully client-side demo mode running in localStorage for GitHub Pages preview, comprehensive IIS/Windows Server deployment automation via PowerShell, and responsive design with WCAG compliance.

The project is particularly distinguished by its intentional, compassionate UX design philosophy—prioritizing a distraction-free, calming aesthetic with teal/sage color schemes appropriate for sensitive moments. With 97 total dependencies, active development momentum (23 commits in 90 days), and production-ready Windows IIS deployment scripts, SupportSpark targets caregivers, patients, and support networks seeking a dignified digital space for maintaining meaningful connection during vulnerable life periods.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 97 total (97 current, 0 outdated)

**Created**: 2026-02-01
**Last Modified**: 2026-02-25

---

### #16. [KeyPressCounter](https://github.com/markhazleton/KeyPressCounter)

Stars: 2 | Forks: 1 | Language: C# | 13 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 46573 KB | 🚀 4.3 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary of the KeyPressCounter repository:

KeyPressCounter is a sophisticated Windows utility designed for comprehensive system and user activity monitoring, leveraging .NET 10.0 and low-level system APIs to track keyboard/mouse interactions, system performance metrics, and resource utilization in real-time. The application employs a multi-layered monitoring approach using technologies like SharpHook for global input event tracking, Windows Performance Counters for system metrics, and WMI (Windows Management Instrumentation) for hardware information retrieval, creating a robust system tray application that provides granular insights into user behavior and computational resource consumption. Its architecture emphasizes privacy-conscious tracking, with features like idle time filtering, local data storage, and detailed logging, making it a powerful tool for productivity analysis, system diagnostics, and performance optimization. The project demonstrates advanced Windows system integration techniques, including registry management, single-instance protection, and seamless system tray interaction, with a modular design that allows for extensive customization of monitoring parameters and logging behaviors. Unique strengths include its comprehensive metrics collection, minimal system overhead, and user-friendly graphical interface that transforms complex system data into digestible visualizations and statistics. Ideal for system administrators, developers, researchers, and power users seeking deep insights into computer usage patterns and system performance characteristics.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 4 total (4 current, 0 outdated)

**Created**: 2024-03-07
**Last Modified**: 2026-02-23

---

### #17. [sql2csv](https://github.com/markhazleton/sql2csv)

Stars: 0 | Forks: 0 | Language: C# | 6 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2004 KB | 🚀 2.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: sql2csv

**sql2csv** is a comprehensive .NET 10 toolkit designed for SQLite database analysis and data extraction, offering both command-line and web-based interfaces for discovering databases, exporting tables to CSV format, inspecting schemas, and generating C# data transfer objects (DTOs). The project follows a modular architecture with separated concerns: a core library (`Sql2Csv.Core`) providing shared business logic, a console CLI for batch operations, an ASP.NET Core MVC web application for interactive analysis and file management, and supporting projects for testing and performance benchmarking. Built with modern .NET practices, the solution includes comprehensive test coverage (with coverage badges), BenchmarkDotNet performance analysis, and Node.js-based frontend asset management for the web UI, enabling both programmatic and user-friendly interaction with SQLite databases. The toolkit is particularly valuable for developers and data analysts who need to rapidly extract, transform, and document database contents, generate domain models automatically, or perform batch database discovery and export operations across directory structures. Its dual-interface approach (CLI for automation/scripting and web UI for interactive exploration) combined with schema reporting in multiple formats (JSON, Markdown, text) and DTO generation makes it a practical utility for data migration, documentation, and onboarding scenarios.

**Created**: 2017-11-06
**Last Modified**: 2026-01-12

---

### #18. [WebSpark.ArtSpark](https://github.com/markhazleton/WebSpark.ArtSpark)

Stars: 0 | Forks: 0 | Language: C# | 31 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3658 KB | 🚀 10.3 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary of the WebSpark.ArtSpark repository:

WebSpark.ArtSpark is a sophisticated .NET ecosystem designed to comprehensively interact with the Art Institute of Chicago's public REST API, providing a complete client library, advanced AI chat system, and demonstration applications. The solution leverages modern .NET 10.0 technologies to create a multi-project architecture that includes a strongly-typed API client, an innovative AI-powered conversational agent, a web demo application, and a console utility, with full coverage of 33 API endpoints across six major categories. Utilizing advanced features like async/await programming, System.Text.Json deserialization, and OpenAI integration, the project offers developers and art enthusiasts a powerful toolkit for exploring, searching, and interacting with museum collections through a robust, extensible platform. The repository stands out through its revolutionary AI chat capabilities, which enable contextual conversations with multiple personas (Artwork, Artist, Curator, Historian) and provide intelligent, culturally sensitive interactions with art metadata, making it a unique solution for digital cultural engagement that bridges technological innovation with art education and exploration.

Key technical highlights include:
- Complete API client with comprehensive endpoint coverage
- AI-powered conversational system with multiple intelligent personas
- Modern .NET architecture with minimal external dependencies
- Advanced features like IIIF image support and Elasticsearch integration
- Flexible querying, async programming, and error handling
- OpenAI Vision integration for image analysis

The project is particularly noteworthy for art technologists, museum researchers, and developers interested in creating intelligent, interactive cultural exploration platforms.

**Created**: 2023-01-30
**Last Modified**: 2026-01-12

---

### #19. [AsyncSpark](https://github.com/markhazleton/AsyncSpark)

Stars: 0 | Forks: 0 | Language: C# | 15 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 1925 KB | 🚀 5.0 commits/month

**Quality**: ❌ License | ✅ Docs

Technical Summary for AsyncSpark:

AsyncSpark is a sophisticated reference implementation and learning platform for advanced asynchronous programming patterns in .NET, designed to demonstrate enterprise-grade async/await techniques with rigorous development standards. The project provides a comprehensive showcase of modern .NET async best practices, including ConfigureAwait(false) usage, proper CancellationToken handling, parallel execution strategies, resilience patterns via Polly, and clean architecture principles, all enforced through an innovative "constitution-driven development" approach. Leveraging .NET 10, the repository implements a multi-project solution with web API, console, and test projects that illustrate complex async scenarios across weather service integration, concurrency management, and remote API interactions, with a strong emphasis on code quality, automated testing (targeting 80% coverage), and interactive API documentation powered by Scalar. What sets AsyncSpark apart is its holistic approach to async programming education, combining technical implementation, architectural best practices, automated compliance checking, and comprehensive documentation into a single, meticulously crafted reference implementation that serves both as a learning resource and a production-ready template for developers seeking to master asynchronous programming in modern .NET environments.

Key Technical Highlights:
- Framework: .NET 10
- Architecture: Clean Architecture, Dependency Injection
- Async Patterns: ConfigureAwait(false), CancellationToken, Task.WhenAll
- Resilience: Polly integration (retry, timeout, circuit breaker)
- Testing: MSTest, 80% code coverage requirement
- Documentation: Scalar-powered interactive API explorer
- Unique Approach: Constitution-driven development with automated audits

**Created**: 2022-08-07
**Last Modified**: 2026-02-10

---

### #20. [FastEndpointApi](https://github.com/markhazleton/FastEndpointApi)

Stars: 2 | Forks: 1 | Language: HTML | 7 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 137 KB | 🚀 2.3 commits/month

**Quality**: ❌ License | ✅ Docs

Technical Summary of FastEndpointApi Repository:

FastEndpointApi is a demonstration project showcasing the FastEndpoints framework for building high-performance, minimalistic REST APIs in ASP.NET Core, focusing on a Person Management system that implements CRUD operations with a clean, lightweight architectural approach. The project leverages the REPR (Request-Endpoint-Response) pattern to create streamlined API endpoints with minimal boilerplate code, utilizing technologies like .NET 10.0, Bogus for data generation, and integrated Swagger documentation. By implementing a complete API with features such as in-memory data storage, dependency injection, and HATEOAS-style link generation, the repository serves as both a practical tutorial and a reference implementation for developers looking to adopt a more modern, efficient approach to API development. The project stands out by emphasizing code simplicity, maintainability, and performance, providing a comprehensive example of how FastEndpoints can significantly reduce complexity in ASP.NET Core API design while maintaining robust functionality. It is particularly valuable for .NET developers seeking to modernize their API development practices, offering a real-world template for building clean, efficient web services with minimal overhead.

**Created**: 2024-04-06
**Last Modified**: 2026-01-12

---

### #21. [PromptSpark.Chat](https://github.com/markhazleton/PromptSpark.Chat)

Stars: 0 | Forks: 0 | Language: C# | 10 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 19796 KB | 🚀 3.3 commits/month

**Quality**: ❌ License | ✅ Docs

# PromptSpark.Chat - Technical Summary

**PromptSpark.Chat** is an ASP.NET Core-based conversational workflow application designed to guide users through multi-step interactive processes using real-time communication and adaptive UI components. The application leverages **ASP.NET Core**, **SignalR**, and **Adaptive Cards** to deliver a dynamic chat interface where users can enter information, select workflows, and progress through branching decision trees with immediate feedback and optional AI-driven responses for out-of-scope questions. The architecture employs a server-side, thread-safe state management approach using `ConcurrentDictionary` to persist conversation data, enabling users to refresh their browser without losing progress—a critical feature for production workflow applications. Key features include interactive Adaptive Cards for structured input collection, real-time bidirectional communication via SignalR, configurable JSON-based workflow definitions that support complex branching logic, and optional integration with chat completion services for AI-augmented responses. The codebase demonstrates clean separation of concerns through Controllers, Services, and Views layers, with support for easy workflow customization through external JSON configuration files. This solution targets enterprise and SaaS applications requiring guided user interactions, conversational task automation, or dynamic form completion workflows, offering a lightweight yet extensible foundation that can scale via Azure SignalR Service and supports deployment across cloud and on-premise environments.

**Created**: 2024-12-31
**Last Modified**: 2026-02-10

---

### #22. [Texecon](https://github.com/markhazleton/Texecon)

Stars: 0 | Forks: 0 | Language: HTML | 3 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 2957 KB | 🚀 1.0 commits/month

**Quality**: ❌ License | ❌ Docs

# TexEcon - Technical Summary

**TexEcon** is a modern static site generator for economic analysis and commentary on the Texas economy, built as a React 19 application deployed to GitHub Pages with advanced SEO and performance optimization. The project implements a sophisticated content management pipeline that fetches fresh analysis from a WebSpark headless CMS API during build time, with intelligent fallback caching and automatic TypeScript type generation to ensure type-safe content handling. The architecture employs a multi-stage build process (clean → content fetch → sitemap generation → Vite compilation → static page generation) to deliver pre-rendered HTML files for optimal SEO and Core Web Vitals performance, while maintaining client-side routing via Wouter for seamless user interactions and progressive enhancement. The tech stack leverages React 19 with TypeScript, Vite 7.1 for fast builds, Tailwind CSS 4.1 for styling, and Radix UI primitives with shadcn/ui components for accessible, production-grade UI elements. This approach is particularly noteworthy for combining the benefits of static site generation with dynamic content sourcing, supporting custom domain deployment (texecon.com) while maintaining GitHub Pages compatibility through configurable base path handling. The project targets economic analysis professionals and policy researchers seeking performant, SEO-friendly content distribution with minimal hosting complexity, making it an excellent reference implementation for headless CMS integration with modern static site generation frameworks.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 50 total (50 current, 0 outdated)

**Created**: 2025-09-03
**Last Modified**: 2026-01-04

---

### #23. [WebSpark.Bootswatch](https://github.com/markhazleton/WebSpark.Bootswatch)

Stars: 0 | Forks: 0 | Language: HTML | 19 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7124 KB | 🚀 6.3 commits/month

**Quality**: ❌ License | ✅ Docs

WebSpark.Bootswatch is a .NET Razor Class Library designed to seamlessly integrate Bootswatch themes into ASP.NET Core applications, providing a robust theming solution built on Bootstrap 5 with advanced capabilities like dynamic theme switching, light/dark mode support, and comprehensive caching mechanisms. The library targets .NET 10.0 exclusively, offering high-performance theme management through features like `StyleCache` service, tag helper support, and responsive design with automatic theme detection and switching. Architecturally, it leverages modern .NET framework features, dependency injection, and extension methods to simplify theme integration, with a focus on providing a production-ready, easily configurable theming system that supports all official Bootswatch themes and custom theme implementations. Its unique value proposition lies in its comprehensive approach to theme management, offering developers a turnkey solution for creating visually dynamic and responsive web applications with minimal configuration overhead. The library is primarily targeted at ASP.NET Core developers seeking a sophisticated, performance-oriented theming solution with extensive customization options and built-in best practices for UI styling and responsiveness.

**Created**: 2022-08-24
**Last Modified**: 2026-01-12

---

### #24. [MechanicsOfMotherhood](https://github.com/markhazleton/MechanicsOfMotherhood)

Stars: 0 | Forks: 0 | Language: TypeScript | 8 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 5888 KB | 🚀 2.7 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a technical summary of the Mechanics of Motherhood repository:

Mechanics of Motherhood is a sophisticated recipe management platform specifically designed for busy working mothers, leveraging modern web technologies to provide a comprehensive culinary organization solution. The application is built using React 19 with TypeScript, featuring a mobile-first responsive design that offers 108+ curated recipes across 14 categories, with advanced features like smart search, recipe filtering, nutritional information, and community ratings. The project showcases a robust technical architecture utilizing Vite for build optimization, TanStack Query for data management, Tailwind CSS for styling, and integrates with RecipeSpark and WebCMS APIs to deliver real-time, high-quality recipe data. Its unique value proposition lies in its industrial-themed design, progressive web app capabilities, offline support, and a focus on creating an intuitive, performance-optimized user experience specifically tailored to the needs of working mothers. The application demonstrates enterprise-grade development practices, including automated CI/CD with GitHub Actions, comprehensive test coverage, SEO optimization, and a modular, type-safe codebase that prioritizes both developer experience and end-user functionality.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 46 total (46 current, 0 outdated)

**Created**: 2025-09-01
**Last Modified**: 2026-01-31

---

### #25. [WebSpark.PrismSpark](https://github.com/markhazleton/WebSpark.PrismSpark)

Stars: 0 | Forks: 0 | Language: C# | 14 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 2272 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ✅ Docs

WebSpark.PrismSpark is a high-performance, extensible C# and .NET library for syntax highlighting, inspired by the popular PrismJS JavaScript library, designed to provide advanced code tokenization and rendering across 24 programming languages. The library offers a comprehensive syntax highlighting solution with a robust plugin system, theme generation, and extensive customization options, leveraging .NET 10.0's capabilities and providing deep integration with ASP.NET Web MVC through dependency injection and service registration. Its architecture emphasizes performance, extensibility, and developer experience, featuring async processing, caching mechanisms, context-aware highlighting, and a flexible hook and plugin system that allows developers to extend and customize syntax highlighting behaviors dynamically. The project stands out by offering a feature-rich, type-safe alternative to JavaScript-based syntax highlighters, with built-in support for line numbering, copy-to-clipboard functionality, theming, and advanced rendering options that cater to developers working in .NET ecosystems who require sophisticated code presentation capabilities. Targeting web developers, documentation authors, and technical content creators, WebSpark.PrismSpark provides a powerful, native .NET solution for transforming raw code into beautifully formatted, semantically highlighted representations across multiple programming languages.

**Created**: 2025-05-27
**Last Modified**: 2026-02-11

---

### #26. [markhazleton.github.io](https://github.com/markhazleton/markhazleton.github.io)

Stars: 0 | Forks: 0 | Language: SCSS | 1 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 144 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: markhazleton.github.io

This is Mark Hazleton's personal portfolio and blog website built with **Jekyll**, a static site generator, and hosted on GitHub Pages with automated deployment via GitHub Actions. The project leverages a customized Minima theme with SCSS-based styling (36.8% of codebase) combined with custom HTML (34.6%) and CSS (27.9%), providing a lightweight, performant alternative to database-driven solutions without external frontend frameworks. Key features include dark/light mode toggle functionality, emoji support, SEO optimization capabilities, and a structured blogging system with support for categories, tags, and featured images through Jekyll's front matter configuration. The tech stack is relatively modern but showing signs of technical debt, with Ruby 3.2.2 and Jekyll 3.10.0, though the repository itself maintains a declining activity pattern (1 commit in 90 days, 16 commits over 365 days) indicating it's primarily a static portfolio rather than an active development project. The project is well-documented with comprehensive guides for local development setup across multiple operating systems (macOS, Windows, Linux), post creation workflows, and both direct-push and feature-branch deployment options, making it accessible for content updates and contributions. This architecture is ideal for developers seeking a low-maintenance, Git-based publishing platform with GitHub Pages integration and automated CI/CD pipelines without requiring traditional web hosting or backend infrastructure.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 3 total (3 current, 0 outdated)

**Created**: 2021-04-18
**Last Modified**: 2026-01-12

---

### #27. [InquirySpark](https://github.com/markhazleton/InquirySpark)

Stars: 0 | Forks: 0 | Language: C# | 18 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 9371 KB | 🚀 6.0 commits/month

**Quality**: ❌ License | ✅ Docs

InquirySpark is a .NET 10-based survey and inquiry management system designed for read-only data interaction, utilizing an MVC architecture with a focus on immutable SQLite databases and strict data access patterns. The solution provides a comprehensive admin interface built with Bootstrap 5 and DataTables, enabling users to interact with survey data through a robust, warning-free implementation that emphasizes type safety, dependency injection, and centralized configuration. Key technologies include Entity Framework Core 10, Microsoft.Data.Sqlite provider, ASP.NET Core Identity, and a modular project structure spanning admin, repository, and common libraries with integrated unit testing via MSTest. The project's unique approach lies in its enforcement of read-only database interactions, elimination of SQL Server dependencies, and a carefully designed persistence layer that prevents schema or data mutations while providing a flexible, scalable framework for survey management. Target users include administrators and organizations seeking a lightweight, secure, and easily deployable survey management solution with minimal infrastructure requirements and strong architectural constraints.

**Created**: 2023-10-24
**Last Modified**: 2025-12-07

---

### #28. [TaskListProcessor](https://github.com/markhazleton/TaskListProcessor)

Stars: 0 | Forks: 0 | Language: C# | 12 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 1070 KB | 🚀 4.0 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary of the TaskListProcessor repository:

TaskListProcessor is an advanced .NET 10.0 library designed to solve complex asynchronous task orchestration challenges in enterprise-level applications, providing a robust framework for managing and executing concurrent operations with high reliability and performance. The library implements sophisticated enterprise-grade patterns including circuit breakers, dependency injection, advanced scheduling, and comprehensive telemetry, enabling developers to build resilient, observable, and highly scalable distributed systems with type-safe and configurable task processing capabilities. Key architectural features include parallel task execution with configurable concurrency limits, OpenTelemetry integration for rich observability, native .NET dependency injection support, and intelligent task dependency resolution using topological sorting and priority-based scheduling strategies. The project stands out by offering a holistic approach to async processing, addressing common challenges like fault isolation, performance monitoring, and complex workflow coordination through a clean, strongly-typed interface that follows SOLID design principles. Targeting enterprise developers, microservice architects, and high-throughput system designers, TaskListProcessor provides a comprehensive solution for managing complex asynchronous workloads across various domains such as distributed computing, API orchestration, data processing, and event-driven architectures. The library's design emphasizes developer experience, offering extensive documentation, learning paths, and practical examples to facilitate quick adoption and effective implementation of advanced task processing patterns.

**Created**: 2023-11-09
**Last Modified**: 2026-01-12

---

### #29. [TeachSpark](https://github.com/markhazleton/TeachSpark)

Stars: 0 | Forks: 0 | Language: C# | 2 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 30771 KB | 🚀 0.7 commits/month

**Quality**: ❌ License | ✅ Docs

Technical Summary:

TeachSpark is an advanced, AI-powered educational platform designed to deliver personalized learning experiences through Large Language Model (LLM) technology, built using a modern .NET 10 MVC architecture with a sophisticated frontend ecosystem. The platform provides intelligent, adaptive learning pathways by dynamically generating and customizing educational content based on individual student learning patterns, utilizing cutting-edge technologies like webpack for build optimization, Bootstrap for responsive design, and comprehensive frontend tooling including ESLint, Prettier, and Husky for code quality management. Its architectural approach emphasizes clean architecture principles, separating concerns between backend (.NET) and frontend (JavaScript/SCSS) while implementing a robust, scalable web application with advanced features like real-time content adaptation, comprehensive learning analytics, and a performance-optimized development workflow. The project stands out through its integration of AI-driven personalization, modern web technologies, and a meticulously structured development environment that prioritizes code quality, developer experience, and scalable design. Targeted primarily at educational institutions, e-learning platforms, and technology-forward learning environments, TeachSpark represents an innovative approach to creating intelligent, data-driven educational experiences that can dynamically adjust to individual learner needs and preferences.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 3 total (3 current, 0 outdated)

**Created**: 2025-06-19
**Last Modified**: 2026-01-12

---

### #30. [DecisionSpark](https://github.com/markhazleton/DecisionSpark)

Stars: 0 | Forks: 0 | Language: C# | 18 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 519 KB | 🚀 6.0 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary of the DecisionSpark repository:

DecisionSpark is an innovative .NET 10 web application that implements a dynamic, conversation-driven decision routing engine designed to guide users through intelligent decision-making processes using minimal, contextually-aware questioning. The system leverages a flexible, config-driven architecture that combines RESTful APIs, Razor Pages web interface, and OpenAI integration to generate intelligent recommendations across various domains by evaluating user responses against configurable rule sets.

The application's core architecture is modular and service-oriented, featuring key components like a Session Store, Routing Evaluator, Trait Parser, and OpenAI-powered Question Generator that work together to create adaptive, context-sensitive decision workflows. It supports multiple question types (text input, single-select, multi-select) and uses JSON-based configuration files to define decision specifications, allowing users to create complex decision trees without modifying code. The system's unique approach involves dynamically generating questions, parsing user responses, and applying intelligent routing logic to recommend optimal outcomes.

Technically, the project is built on .NET 10 with a comprehensive technology stack including Razor Pages for the web interface, Swagger/OpenAPI for API documentation, Serilog for structured logging, and optional OpenAI integration for natural language processing. The architecture supports session management, file-based conversation persistence, and a pluggable design that allows easy extension and configuration of decision scenarios.

Key distinguishing features include its conversation-driven API, intelligent question generation, rule-based evaluation with derived traits, and the ability to create complex decision workflows through simple JSON configuration. The system is particularly well-suited for scenarios requiring guided decision-making, such as recommendation engines, interactive planning tools, or adaptive questionnaires across various domains.

While currently demonstrated with example use cases like a "Family Saturday Planner" and "Tech Stack Advisor", the framework is designed to be highly generic and adaptable, enabling developers and domain experts to quickly create sophisticated, intelligent decision support systems with minimal technical overhead.

**Created**: 2025-10-29
**Last Modified**: 2025-12-27

---

### #31. [HttpClientDecoratorPattern](https://github.com/markhazleton/HttpClientDecoratorPattern)

Stars: 0 | Forks: 0 | Language: HTML | 1 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 2675 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary:

This repository demonstrates a production-ready implementation of the Decorator Pattern for HttpClient in .NET, providing a sophisticated approach to managing HTTP communication with enhanced resilience, telemetry, and caching capabilities. The project introduces a flexible, composable service architecture that allows dynamically adding cross-cutting concerns like performance monitoring, circuit breaking, and caching without modifying core service implementations. Leveraging .NET 10, dependency injection, and libraries like Polly, the implementation offers a robust solution for enterprise-grade HTTP client management, with strong emphasis on separation of concerns, testability, and observability. The WebSpark.HttpClientUtility package serves as the core implementation, featuring a comprehensive decorator chain that systematically wraps HTTP requests with additional behaviors such as retry policies, correlation tracking, and intelligent caching strategies. By providing a clean, extensible pattern for HTTP communication, the project addresses common challenges in distributed system design, making it particularly valuable for developers building microservices, API-driven applications, or systems requiring sophisticated HTTP interaction management.

**Created**: 2023-02-09
**Last Modified**: 2026-01-12

---

### #32. [Yelp.Api](https://github.com/markhazleton/Yelp.Api)

Stars: 0 | Forks: 0 | Language: C# | 1 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 462 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ❌ Docs

Here's a comprehensive technical summary for the Yelp.Api repository:

The Yelp.Api is a C# class library that provides a robust, developer-friendly wrapper for Yelp's v3 Fusion API, enabling .NET developers to easily integrate local business search and review functionality into their applications. Leveraging .NET 6 and designed with a clean, intuitive interface, the library simplifies complex API interactions by offering methods like `SearchBusinessesAllAsync()` that abstract away the underlying HTTP communication and authentication complexities. The library supports comprehensive search capabilities, including geolocation-based queries, filtering by business attributes (such as open now status), and retrieving detailed business information across 32 countries with minimal configuration required. Its design follows a client-centric architectural pattern, where developers can instantiate a `Yelp.Api.Client` with an API key and immediately perform sophisticated local business searches using either simple method signatures or more granular `SearchParameters` objects. Unique strengths include its strong typing, async support, and straightforward usage that reduces the typical boilerplate code associated with external API integrations. The primary target users are .NET developers building location-aware applications such as travel guides, restaurant recommendation systems, local service aggregators, or any software requiring rich, up-to-date local business data.

**Created**: 2022-08-10
**Last Modified**: 2026-01-12

---

### #33. [react-native-web-start](https://github.com/markhazleton/react-native-web-start)

Stars: 0 | Forks: 0 | Language: TypeScript | 1 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3184 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary for the react-native-web-start repository:

React Native Web Starter is a sophisticated, enterprise-grade cross-platform application development template designed to enable developers to build high-performance, type-safe applications that seamlessly deploy across web, iOS, and Android platforms using a unified codebase. Leveraging modern web technologies like React Native Web, Vite, and TypeScript, the project provides a comprehensive development ecosystem with robust features including responsive design, API integration, comprehensive testing infrastructure, and optimized build processes. The monorepo architecture supports modular development with dedicated packages for shared components, web, and mobile configurations, while integrating advanced tooling like Tailwind CSS, Sass preprocessing, and automated CI/CD workflows through GitHub Actions. Key differentiators include its strict TypeScript configuration, built-in documentation browser, performance optimization techniques like tree-shaking and code splitting, and comprehensive platform compatibility with responsive design principles. This starter template is particularly valuable for developers and organizations seeking to streamline cross-platform mobile and web application development with a focus on developer experience, code reusability, and scalable architectural patterns.

Would you like me to elaborate on any specific aspect of this technical summary?

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 49 total (49 current, 0 outdated)

**Created**: 2025-07-26
**Last Modified**: 2026-01-14

---

### #34. [TriviaSpark](https://github.com/markhazleton/TriviaSpark)

Stars: 0 | Forks: 0 | Language: C# | 4 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 27238 KB | 🚀 1.3 commits/month

**Quality**: ❌ License | ✅ Docs

Technical Summary for TriviaSpark:

TriviaSpark is an experimental multiplayer web and mobile trivia game application developed with AI assistance, designed to provide an interactive and competitive trivia experience for tech-savvy users aged 18-95. The project is primarily built using C# with a web-based architecture, leveraging public Trivia APIs to dynamically generate question sets and enable real-time multiplayer interactions. Key planned features include user registration, a comprehensive leaderboard system, admin-level question database management, and a customizable user interface that supports both web and mobile platforms. The application appears to follow a modern, component-based development approach with potential use of .NET technologies for backend infrastructure and web frameworks for frontend rendering. What makes TriviaSpark unique is its explicit integration of AI in the development process, as highlighted by its README noting collaborative development with ChatGPT, which suggests an innovative approach to software design and potentially leveraging AI for dynamic content generation and user experience optimization. The project aims to create an engaging, knowledge-testing platform that combines competitive gameplay with accessible, technology-driven design.

**Created**: 2023-02-22
**Last Modified**: 2025-12-02

---

### #35. [DataAnalysisDemo](https://github.com/markhazleton/DataAnalysisDemo)

Stars: 0 | Forks: 0 | Language: Visual Basic .NET | 1 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 12926 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

Technical Summary:

DataAnalysisDemo is a sophisticated web-based data analytics platform built using ASP.NET WebForms (VB.NET) that transforms raw CSV data into interactive, visually compelling analytics experiences through advanced processing and visualization techniques. The application offers comprehensive data exploration capabilities, including dynamic charting with D3.js and C3.js, advanced pivot table functionality with drag-and-drop interfaces, and robust data processing using a custom GenericParser library that supports real-time statistical analysis and memory-efficient dataset handling. Leveraging a modern client-side architecture with Webpack, Bootstrap 5, and jQuery, the platform provides a responsive, feature-rich interface that enables users to parse, analyze, visualize, and export complex datasets with intuitive tools like SearchPanes, multiple chart types, and extensible data renderers. The project demonstrates a sophisticated approach to web-based data analysis by integrating server-side .NET processing with cutting-edge client-side technologies, making it particularly valuable for data analysts, researchers, and business intelligence professionals seeking a flexible, user-friendly data exploration tool. Key architectural strengths include its modular design, extensive client-side build pipeline, multiple visualization modes, and comprehensive error handling, which collectively create a robust platform for transforming raw data into meaningful insights across various domains.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 24 total (24 current, 0 outdated)

**Created**: 2023-04-20
**Last Modified**: 2025-12-03

---

### #36. [PHPDocSpark](https://github.com/markhazleton/PHPDocSpark)

Stars: 0 | Forks: 0 | Language: PHP | 0 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 2727 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

Based on the comprehensive README and repository details, here's a technical summary:

PHPDocSpark is an innovative, open-source PHP documentation and data exploration platform that demonstrates modern web application development practices by creating a hybrid server-side and client-side architecture. The project showcases a sophisticated technology stack combining PHP 8.2+, Vite, Bootstrap 5, and modern JavaScript libraries to build a flexible documentation management and data visualization system with robust features like Markdown parsing, full-text search, interactive data tables, and external API integrations. Its unique architectural approach leverages a front controller pattern with a modular design, enabling seamless routing, asset management through a Vite-powered build pipeline, and responsive, dynamic content rendering across different devices and screen sizes.

Key technical highlights include:
- Hybrid PHP/JavaScript architecture with clean separation of concerns
- Vite-powered asset bundling with hot module replacement
- Markdown-based documentation system with automatic navigation generation
- Interactive data visualization using Chart.js and DataTables
- SQLite database integration for lightweight data management
- GitHub API and external service integrations with intelligent caching
- Responsive, mobile-first design using Bootstrap 5

The project serves as an educational reference implementation for developers seeking to understand contemporary PHP web development techniques, showcasing best practices in routing, asset management, content parsing, and API integration. It's particularly valuable for full-stack developers, technical writers, and teams looking to modernize their PHP application architecture.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2023-09-08
**Last Modified**: 2025-08-18

---


---

## Report Metadata

- **Generation Time**: 1.4 seconds
- **SVGs Generated**: 6/6
- **Total API Calls**: 0
- **Total AI Tokens**: 87,083
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
*Last updated: 2026-03-07*