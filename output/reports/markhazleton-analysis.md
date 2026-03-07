# GitHub Profile: markhazleton

**Generated**: 2026-03-07 21:30:39 UTC
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

Stars: 0 | Forks: 0 | Language: Python | 171 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 9768 KB | 🚀 57.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: github-stats-spark

Stats Spark is a comprehensive GitHub analytics and visualization platform that automatically generates beautiful SVG profile statistics and AI-powered repository analysis reports. The project combines multiple data processing pipelines—leveraging PyGithub for API interactions, svgwrite for dynamic SVG generation, and Claude AI for intelligent repository summaries—to transform raw GitHub activity into actionable insights and professional visualizations. The architecture supports both backend Python services (handling data aggregation, caching, and AI integration) and a modern frontend dashboard built with JavaScript and CSS, featuring mobile-first responsive design with interactive Chart.js visualizations and offline IndexedDB caching capabilities. Key technical innovations include a sophisticated ranking algorithm that weighs repository popularity (30%), activity recency with time-decay windows (45%), and health metrics (25%), plus an intelligent 97%+ success-rate fallback system for AI-generated summaries that gracefully degrades from Claude Haiku to README extraction to basic metadata. The project demonstrates enterprise-grade engineering practices including rate-limit handling with exponential backoff, smart API caching reducing requests by 80-95%, YAML-based configuration management, and WCAG AA accessibility compliance across both visualizations and interactive components. This tool targets developers seeking professional GitHub portfolio enhancement, technical leaders analyzing productivity metrics, and open-source maintainers tracking project momentum, with automated daily GitHub Actions workflows enabling zero-maintenance continuous updates and real-time dashboard synchronization.

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

This repository is a personal technical blog and portfolio site built for Mark Hazleton, a Technical Solutions Architect, showcasing long-form articles on cloud architecture and engineering practices alongside a curated project portfolio and live GitHub activity metrics. The site is constructed with a modern React 19 + TypeScript stack, leveraging Vite 7 for both client-side and server-side rendering with static prerendering capabilities, styled with Tailwind CSS and Radix UI components. The architecture implements a sophisticated content pipeline that combines Markdown-based blog posts with JSON metadata, automatically optimizes images and generates SEO assets (sitemaps, RSS feeds with Media RSS namespace), and inlines live repository statistics from a separate GitHub stats aggregator to ensure rich first-paint content without client-side delays. Static prerendering via `prerender.mjs` transforms all routes—including dynamic blog posts and repository detail pages—into static HTML for optimal performance and SEO, with the entire build output deployed to Azure Static Web Apps via GitHub Actions automation. The project demonstrates strong DevOps practices through comprehensive build scripting, TypeScript type safety, a well-documented repository structure, and a governance-driven development approach documented in `.documentation/`, making it an exemplary reference implementation for technical portfolios and static site generation at scale. This solution is particularly valuable for technical professionals seeking to establish credible online presence with minimal hosting overhead while maintaining full control over content, presentation, and deployment pipelines.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 59 total (59 current, 0 outdated)

**Created**: 2026-01-10
**Last Modified**: 2026-03-07

---

### #3. [MuseumSpark](https://github.com/markhazleton/MuseumSpark)

Stars: 0 | Forks: 0 | Language: Python | 62 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 21243 KB | 🚀 20.7 commits/month

**Quality**: ❌ License | ✅ Docs

# MuseumSpark – Technical Summary

**MuseumSpark** is an intelligent museum discovery and travel planning platform that transforms the Walker Art Center Reciprocal Program membership list (1,269 museums across North America) into a data-rich, searchable resource for art enthusiasts. The project leverages a sophisticated multi-phase data enrichment pipeline combining Wikidata, Wikipedia, museum websites, and structured metadata extraction to progressively build a comprehensive museum database with priority scoring based on artistic collection strength, historical significance, and visitor relevance.

The platform is built as a **React 19 + Vite static web application** with Tailwind CSS styling, offering core features including a museum browser with state/province filtering and search, detailed museum profiles with contact information and enrichment metadata, and a real-time data quality dashboard tracking enrichment progress (currently 0.08% complete on Phase 1). The backend employs a **Python 3.11+ data pipeline architecture** with Pydantic 2 for strict schema validation, BeautifulSoup4 for web scraping, and JSON Schema enforcement to ensure data integrity across multiple enrichment phases—a disciplined approach that demonstrates mature data engineering practices with explicit quality assurance rules ("Never Replace Known With Null").

The project's roadmap is ambitious and clearly staged: Phase 0-1 (current, 80% complete) establishes the data foundation; Phase 2 introduces expert scoring for collection quality assessment; Phase 2.5-3 integrates Claude/OpenAI agents for AI-assisted content validation; and Phase 4 (Q4 2026) expands into a full-featured FastAPI backend with user authentication, favorites management, and AI-powered travel recommendations. What distinguishes MuseumSpark is its **intentional separation of concerns**—decoupling the static frontend deployment (GitHub Pages) from heavyweight data processing, enabling scalable enrichment work without deployment friction—and its transparent methodology, publishing data quality metrics and enrichment progress publicly to build user trust.

The project is actively maintained with 62 commits in the last 90 days showing accelerating momentum, targets art lovers and cultural travelers seeking optimized museum itineraries, and represents a sophisticated blend of data science, web development, and domain-specific expertise that could ultimately serve as a model for cultural tourism intelligence platforms beyond museums.

**Created**: 2026-01-15
**Last Modified**: 2026-02-20

---

### #4. [UISampleSpark](https://github.com/markhazleton/UISampleSpark)

Stars: 8 | Forks: 4 | Language: HTML | 54 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 30713 KB | 🚀 18.0 commits/month

**Quality**: ❌ License | ✅ Docs

# UISampleSpark – Technical Summary

**UISampleSpark** is a comprehensive educational reference application built on .NET 10 and ASP.NET Core that demonstrates how to implement the same Employee/Department CRUD domain using seven different front-end UI technologies: MVC, Razor Pages, React 18, Vue 3, htmx, Blazor Server, and vanilla JavaScript SPA. The project showcases modern web development patterns through a consistently architected backend that exposes REST/OpenAPI endpoints, leveraging clean architecture principles with dependency injection, repository patterns, and in-memory Entity Framework Core, complemented by responsive Bootstrap 5 theming with dynamic Bootswatch theme switching and comprehensive CI/CD automation via GitHub Actions and Docker containerization.

The repository is particularly valuable for developers and architects evaluating front-end framework trade-offs, as it provides side-by-side implementations of identical business logic across multiple paradigms—from server-rendered approaches (MVC/Razor Pages) to interactive hypermedia systems (htmx) to client-side SPAs (React/Vue)—while maintaining shared validation, paging, and service layers. Beyond its educational merit, the project demonstrates enterprise-grade practices including unit testing across domain and data layers, Application Insights observability, health checks, Swagger/OpenAPI documentation, and production-ready deployment patterns on both Windows IIS and Docker/Azure Linux environments, making it an ideal reference for teams modernizing legacy applications or comparing architectural decisions before committing to a specific UI technology stack.

**Created**: 2019-04-25
**Last Modified**: 2026-02-08

---

### #5. [git-spark](https://github.com/markhazleton/git-spark)

Stars: 0 | Forks: 0 | Language: TypeScript | 15 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 1582 KB | 🚀 5.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Git Spark

**Git Spark** is a TypeScript-based command-line analytics tool and Node.js library that analyzes Git repository commit history to generate comprehensive insights into development patterns, contributor activity, and code change metrics. The project provides multi-format reporting (HTML, JSON, CSV, Markdown) with an emphasis on interactive, security-hardened dashboards featuring time-series visualizations, contributor statistics, file analysis, and governance metrics—all derived exclusively from Git commit data without external API dependencies. The architecture employs a dual-interface design supporting both CLI operations (via Commander.js) and programmatic usage, leveraging dependencies like Chalk for styled terminal output, Ora for progress indicators, and Boxen for formatted console displays, with the core tech stack heavily weighted toward TypeScript (88.3%) for type safety. Notable architectural strengths include security-first HTML report generation with Content Security Policy (CSP) hashing, client-side data export capabilities, dark mode support with localStorage persistence, and optional email redaction for privacy-sensitive audits—making it suitable for enterprise governance workflows and air-gapped environments. The project targets DevOps engineers, engineering managers, and development teams seeking transparent, Git-native visibility into repository health and contributor patterns, with emerging Azure DevOps integration capabilities expanding its enterprise applicability. Despite strong feature completeness and recent activity (90-day commit frequency), the tech stack currency score of 50/100 and lack of adoption metrics (0 stars, 0 forks) suggest the tool is either newly published or in early community adoption phases.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 19 total (19 current, 0 outdated)

**Created**: 2025-09-29
**Last Modified**: 2026-02-20

---

### #6. [JsBootSpark](https://github.com/markhazleton/JsBootSpark)

Stars: 0 | Forks: 0 | Language: JavaScript | 22 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 3448 KB | 🚀 7.3 commits/month

**Quality**: ❌ License | ✅ Docs

# JsBootSpark - Technical Summary

**JsBootSpark** is a production-ready, full-stack starter kit designed to accelerate development of modern, responsive web applications by combining Express.js backend with Bootstrap 5.3+ frontend frameworks. The project provides a comprehensive, pre-configured development environment featuring Express 5.1.0 with EJS templating, SASS preprocessing, and a curated component library with 2,000+ Bootstrap Icons, enabling developers to bootstrap projects with battle-tested security configurations (Helmet.js, rate limiting, CSP), performance optimizations (compression middleware, responsive images), and PWA capabilities (service workers, web manifests) out of the box.

The architecture leverages a modular, convention-based structure that supports both static site generation and dynamic page rendering, with automated build pipelines (CSV-to-JSON conversion, path conversion for subdirectory deployment) and CI/CD integration via GitHub Actions for seamless deployment to GitHub Pages, Docker containers, or traditional hosting. Key technical differentiation includes hot-reload development with synchronized SASS compilation, comprehensive testing infrastructure (Jest with coverage), linting/formatting standards (ESLint + Prettier), and extensive documentation spanning quick-start guides, architectural decisions, security policies, and AI-assisted development sessions—all while maintaining a relatively lightweight 3.4 MB codebase composed primarily of JavaScript (66.8%) and EJS templates (21.1%).

Ideal for developers, startups, and organizations seeking to rapidly prototype responsive web applications, build content-heavy sites with dynamic generation, or establish standardized web development practices, the project demonstrates **active maintenance** (22 commits in 90 days, 81 in the past year) though it remains early-stage with zero stars, forks, or external contributors. The 50/100 tech stack currency score reflects intentional stability choices (Node.js 18+, Bootstrap 5.3.x) rather than bleeding-edge dependencies, making it a pragmatic foundation for production applications requiring reliability over novelty.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 30 total (30 current, 0 outdated)

**Created**: 2022-06-06
**Last Modified**: 2026-01-31

---

### #7. [TailwindSpark](https://github.com/markhazleton/TailwindSpark)

Stars: 0 | Forks: 0 | Language: HTML | 28 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 3632 KB | 🚀 9.3 commits/month

**Quality**: ❌ License | ✅ Docs

# TailwindSpark - Technical Summary

**TailwindSpark** is a comprehensive, production-ready Tailwind CSS design system and component showcase built as a modern React TypeScript monorepo. The project demonstrates modern web development best practices through a complete design system featuring interactive components, animations, dashboards, e-commerce flows, and marketing pages—all powered by React 19.1, TypeScript 5.9, Tailwind CSS 4.1, and Vite 7.1 within a Turborepo 2.7 architecture.

The repository excels in developer experience and code quality, implementing 100% TypeScript with strict type checking, comprehensive ESLint and Prettier linting, automated testing via Vitest with coverage reporting, and full WCAG 2.1 AA accessibility compliance with keyboard navigation and screen reader support. Its production-ready infrastructure includes GitHub Actions CI/CD pipelines, Dependabot security scanning, real-time performance monitoring via Web Vitals, service worker offline support, and automated deployments to GitHub Pages, while also providing extensive documentation covering architecture, testing strategies, deployment procedures, and brand guidelines.

The project is uniquely positioned as both a practical design system reference implementation and an educational resource for developers seeking to understand modern React patterns, TypeScript best practices, and Tailwind CSS v4 capabilities including the new @theme directive and CSS custom properties. Target users include frontend developers, design system teams, and organizations looking to establish scalable component libraries, with particular value for those implementing accessibility-first approaches and seeking battle-tested architectural patterns for monorepo-based projects.

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

**WebSpark.HttpClientUtility** is a production-ready, open-source .NET library that provides a streamlined wrapper around HttpClient, eliminating boilerplate configuration for enterprise microservices. It packages Polly resilience policies (retries, circuit breakers), intelligent in-memory response caching, automatic correlation ID propagation, structured logging, and OpenTelemetry tracing into a single `AddHttpClientUtility()` dependency injection call—reducing typical 50+ line HttpClient setup to one line. The library is architected around the `IHttpRequestResultService` interface and supports .NET 8, 9, and 10 LTS with Native AOT and IL trimming compatibility, backed by 237+ unit tests with 100% pass rate and zero breaking changes within major versions.

The project comprises two modular NuGet packages: the core **WebSpark.HttpClientUtility** (163 KB) handles HTTP client utilities with authentication, caching, resilience, and observability, while the optional **WebSpark.HttpClientUtility.Crawler** (75 KB) extension adds web crawling capabilities including robots.txt parsing and sitemap generation. Key features include configurable request/response caching strategies, automatic retry logic with exponential backoff via Polly, built-in ActivitySource for distributed tracing, rich contextual logging with request correlation IDs, and error handling with detailed diagnostics—all configured through fluent options builders without requiring manual middleware composition or ActivitySource registration.

The codebase (73.2% C#, 16.8% HTML documentation, 6.1% PowerShell build scripts) demonstrates strong engineering practices: Source Link symbol packages enable step-through debugging, GitHub Actions CI/CD pipelines validate every commit, semantic versioning prevents accidental breaking changes, and comprehensive GitHub Pages documentation provides getting-started guides, API references, and best-practice examples. The library targets microservice architectures, background workers, and web scrapers where developers need enterprise-grade resilience, observability, and rate-limit compliance without building custom Polly orchestration or telemetry instrumentation, positioning it as a productivity-focused alternative to raw HttpClient, RestSharp, or Refit when rapid setup with integrated observability is prioritized over declarative, type-safe API contracts.

**Created**: 2025-05-03
**Last Modified**: 2026-02-27

---

### #9. [ReactSparkPortfolio](https://github.com/markhazleton/ReactSparkPortfolio)

Stars: 0 | Forks: 0 | Language: CSS | 24 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 43361 KB | 🚀 8.0 commits/month

**Quality**: ❌ License | ✅ Docs

# ReactSparkPortfolio - Technical Summary

**ReactSparkPortfolio** is a production-ready, enterprise-grade developer portfolio application built with React 19, TypeScript, and Vite that serves as both a personal showcase and comprehensive reference implementation for modern web development practices. The project demonstrates sophisticated frontend architecture with real-time capabilities, including SignalR-powered chat functionality, live weather integration with interactive mapping (Leaflet), RSS feed aggregation, and a searchable portfolio system—all pulling dynamically from external APIs and content sources. The tech stack is contemporary and well-curated, leveraging Bootstrap 5 for responsive UI components, SCSS for advanced styling with theme switching (dark/light modes), Axios for HTTP communication, and date-fns for date utilities, while maintaining strict TypeScript type safety across the entire codebase.

The architecture employs a frontend-first, serverless approach with dual-platform deployment capabilities (Azure Static Web Apps and GitHub Pages), Azure Functions for API proxying, and GitHub Actions for CI/CD automation, demonstrating cloud-native design patterns suitable for scalable applications. Notably, the project prioritizes accessibility (WCAG 2.1 AA compliance), performance optimization through lazy loading and code splitting via Vite, and developer experience with comprehensive TypeScript support, ESLint configuration, and detailed documentation covering security considerations (particularly regarding intentionally permissive CSP headers required for external content integration). This repository is particularly valuable for developers seeking a reference implementation of enterprise-grade React patterns, serverless architecture with Azure, real-time web features, and best practices for responsive, accessible web applications—making it suitable for professionals building scalable portfolio platforms, SPA applications, or learning modern frontend development methodologies.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 46 total (46 current, 0 outdated)

**Created**: 2024-10-11
**Last Modified**: 2026-03-07

---

### #10. [WebProjectMechanics](https://github.com/markhazleton/WebProjectMechanics)

Stars: 3 | Forks: 0 | Language: Visual Basic .NET | 9 commits (90d)

👥 0 contributors | 🌐 10 languages | 💾 52405 KB | 🚀 3.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebProjectMechanics

**WebProjectMechanics** is a greenfield rebuild of a legacy multi-tenant, multi-domain content management system designed to serve 36+ websites from a single application instance while maintaining physical data isolation and cost efficiency (~$10/month on Azure Linux). The system architecture employs a plugin-based domain model (CMS pages, Mineral Collection, Recipes) with per-site SQLite databases, eliminating the need for tenant ID columns, and implements a publish-to-static workflow that pre-renders all public content as HTML served by Caddy 2 for optimal performance and security. Built on modern .NET 9 with ASP.NET Core Minimal APIs, Entity Framework Core 9, and Scriban templating, the project represents a strategic migration away from a 20+ year legacy ASP.NET Web Forms/MS Access system while maintaining backward compatibility through documented migration tooling and an archived reference implementation. The codebase demonstrates sophisticated multi-tenancy patterns through physical isolation rather than logical separation, enabling simplified security boundaries and database management while the static HTML publishing approach eliminates runtime rendering overhead. This architecture is particularly noteworthy for cost-conscious organizations operating multiple domain properties, as it consolidates infrastructure while maintaining the simplicity and performance characteristics of static site serving, making it ideal for content-driven websites with predictable traffic patterns and infrequent updates. The project's active maintenance status (accelerating commit activity) and comprehensive documentation infrastructure suggest a well-planned long-term initiative currently in Phase 1 (Foundation) development.

**Created**: 2017-09-19
**Last Modified**: 2026-02-19

---

### #11. [RESTRunner](https://github.com/markhazleton/RESTRunner)

Stars: 2 | Forks: 1 | Language: C# | 16 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 426 KB | 🚀 5.3 commits/month

**Quality**: ❌ License | ✅ Docs

# RESTRunner - Technical Summary

RESTRunner is a comprehensive .NET 10 (LTS) solution designed for REST API testing, performance benchmarking, and regression testing with native Postman collection integration. The project provides dual interfaces—a console application for batch processing and a Razor Pages web application for interactive testing—enabling developers to automate API validation, conduct load testing, and analyze performance metrics across multiple environments with detailed statistical reporting exported to CSV format.

The solution demonstrates modern .NET architecture with a multi-project structure including a Domain layer for business logic, a Data layer for persistence, and a Web layer for UI, complemented by comprehensive MSTest v4 unit test coverage (21/21 tests passing). Key capabilities include automated regression testing suites, configurable load testing parameters, response time percentile analysis, success rate metrics, a sample CRUD API for demonstration purposes, and sophisticated performance comparison features—all optimized through the recent .NET 10 upgrade which achieved 19% faster builds and 25% faster test execution while maintaining zero security vulnerabilities.

The project targets QA engineers, API developers, and DevOps teams who need enterprise-grade testing automation without the overhead of commercial solutions, distinguishing itself through seamless Postman collection portability, lightweight containerization (evidenced by Dockerfile inclusion), and modern dependency management with 93% packages at latest versions. The active development trajectory (16 commits in 90 days, accelerating pattern) and comprehensive upgrade documentation in `.github/upgrades/` indicate mature maintenance practices and a commitment to staying current with the .NET ecosystem's LTS releases.

**Created**: 2021-09-30
**Last Modified**: 2026-01-12

---

### #12. [ConcurrentProcessing](https://github.com/markhazleton/ConcurrentProcessing)

Stars: 0 | Forks: 0 | Language: C# | 19 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 145 KB | 🚀 6.3 commits/month

**Quality**: ❌ License | ✅ Docs

# ConcurrentProcessing - Technical Summary

**ConcurrentProcessing** is a production-ready, educational framework for .NET 10 that provides sophisticated concurrent task execution with fine-grained parallelism control through semaphore-based throttling. The project implements a generic abstract base class (`ConcurrentProcessor<T>`) that enables developers to create type-safe, custom task processors while automatically tracking comprehensive performance metrics including task duration, semaphore wait times, and throughput statistics. Built with modern C# 12+ features and optimized for .NET 10, the framework employs established design patterns—including Template Method, Factory, Strategy, and Resource Pool patterns—to deliver both flexibility and high performance with minimal overhead, demonstrating linear scalability across configurable concurrency limits. The repository excels as both a production component for applications requiring bounded parallel processing (such as API rate limiting, batch job scheduling, or database bulk operations) and as an exemplary educational resource for learning advanced concurrent programming, performance profiling, and generic type system design in C#. Its comprehensive documentation, CI/CD automation (with .NET Build/Test and Release workflows), and well-instrumented codebase make it valuable for developers ranging from intermediate practitioners seeking to understand concurrent patterns to architects designing scalable .NET systems that require deterministic resource management.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 2 total (2 current, 0 outdated)

**Created**: 2023-09-18
**Last Modified**: 2026-01-22

---

### #13. [markhazleton](https://github.com/markhazleton/markhazleton)

Stars: 0 | Forks: 0 | Language: Unknown | 11 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 6595 KB | 🚀 3.7 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: markhazleton Repository

This repository serves as Mark Hazleton's personal portfolio and learning archive, functioning as a central hub that showcases his development journey and hosts documentation for multiple project demonstrations. The primary purpose is to aggregate and curate a collection of learning projects, technical articles, and featured applications—particularly **WebSpark** (a comprehensive web application demo hosting platform) and **ReactSpark** (a modern React application built with Vite and deployed on Azure Static Web Applications)—reflecting a commitment to continuous skill development across diverse technology stacks. The architecture emphasizes modern cloud-native deployment patterns, leveraging **Azure** services for hosting, **Git**-based workflow automation (including fork synchronization and upstream integration), and **AI-assisted development methodologies** as documented in the article series on spec-driven development. Key technical differentiators include integration of automated GitHub statistics generation, dynamic blog post aggregation, and demonstrated expertise in full-stack development spanning Oracle databases, .NET/MVC frameworks, React/Vite frontend stacks, and DevOps practices through Azure DevOps. The repository targets software engineers and architects seeking to understand practical implementations of feature-to-outcome-driven development, governance patterns for sprint hotfixes, and evolving approaches to AI-augmented software engineering. This multifaceted project exemplifies pragmatic engineering philosophy, balancing evolutionary improvements over revolutionary rewrites while maintaining strong emphasis on accountability, authority structures, and sustainable team practices.

**Created**: 2021-04-17
**Last Modified**: 2026-03-01

---

### #14. [WebSpark](https://github.com/markhazleton/WebSpark)

Stars: 1 | Forks: 0 | Language: C# | 14 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 69006 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ❌ Docs

# WebSpark - Technical Summary

**WebSpark** is a comprehensive .NET 9-based web application suite comprising three specialized tools (PromptSpark for LLM prompt optimization, RecipeSpark for recipe management, and TriviaSpark for quiz creation) built on ASP.NET Core MVC with Bootstrap 5 frontend. The project features a modular seven-area architecture (PromptSpark, RecipeSpark, TriviaSpark, WebCMS, AsyncSpark, Admin, Identity) enabling scalable, domain-driven development across multiple functional domains. A standout feature is its extensive SEO optimization system with dynamic meta tags, JSON-LD structured data (Schema.org), automated sitemap generation, multi-engine webmaster verification, Google Analytics 4 integration with custom dimensions, Core Web Vitals monitoring, and Application Insights-based SEO audit logging—backed by 47 passing tests ensuring production-ready search engine visibility.

The repository implements a sophisticated **spec-driven development workflow** via SpecKit commands that enforce quality gates before implementation: `/speckit.specify` creates feature specifications, `/speckit.plan` generates implementation architectures, `/speckit.tasks` breaks work into actionable items, and critically, `/speckit.critic` performs automated adversarial risk assessment identifying showstoppers, security vulnerabilities, performance killers, and operational gaps before code is written. This workflow enforces strict branch protection rules (NNN-short-name convention) and maintains architectural constitution principles to reduce production risk and technical debt. The codebase shows active development (14 commits in 90 days, 83 in 365 days) with a 47% C#/40% HTML/7% SCSS composition, making it ideal for organizations seeking a well-architected, SEO-optimized content management and engagement platform with formalized quality assurance processes.

**Created**: 2024-01-11
**Last Modified**: 2026-01-29

---

### #15. [SupportSpark](https://github.com/markhazleton/SupportSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 23 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 1856 KB | 🚀 7.7 commits/month

**Quality**: ❌ License | ❌ Docs

# SupportSpark - Technical Summary

**SupportSpark** is a compassionate support network platform built with TypeScript and React that enables individuals facing life challenges to share journey updates with a trusted circle of supporters through a calm, invitation-only interface. The application implements a dual-role system where members (update creators) post updates with text and images while supporters engage through threaded conversations, eliminating the burden of individual notifications during difficult periods. The tech stack leverages modern frontend technologies including React 19, Vite, Tailwind CSS 4, shadcn/ui components built on Radix primitives, and TanStack React Query for state management, paired with an Express 5 backend using Passport.js for authentication and Zod for runtime type validation across a fully TypeScript codebase (strict mode). The architecture follows a clear separation between client, server, and shared layers with JSON-based storage for development and production deployment targeting Windows 11 + IIS via iisnode, supported by automated PowerShell deployment scripts and comprehensive documentation. Notably distinctive is its emphasis on accessible, distraction-free design specifically tailored for sensitive moments, combined with a fully functional client-side demo mode using localStorage that allows users to explore the platform on GitHub Pages without a backend server. The project demonstrates thoughtful UX decisions—such as role-based access control, threaded replies for organized dialogue, and a calming teal/sage aesthetic—making it particularly valuable for healthcare, mental health, and personal crisis support scenarios where reducing friction in communication significantly improves outcomes.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 97 total (97 current, 0 outdated)

**Created**: 2026-02-01
**Last Modified**: 2026-02-25

---

### #16. [KeyPressCounter](https://github.com/markhazleton/KeyPressCounter)

Stars: 2 | Forks: 1 | Language: C# | 13 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 46573 KB | 🚀 4.3 commits/month

**Quality**: ❌ License | ✅ Docs

# KeyPressCounter - Technical Summary

**KeyPressCounter** is a Windows-based system monitoring utility written in C# (.NET 10.0) that provides comprehensive tracking of user input activity and real-time system performance metrics through a non-intrusive system tray application. The tool combines global keyboard/mouse event hooking via the SharpHook library with Windows Management Instrumentation (WMI) and Performance Counter APIs to simultaneously monitor keystroke/click patterns, CPU/memory usage, disk I/O, network throughput, and running processes, all while maintaining privacy by counting interactions without logging keystroke content.

The application features a sophisticated architecture that includes native Windows API integration for idle detection, configurable activity logging with automatic daily summaries, registry-based startup management, and a tabbed statistics dashboard with real-time graphical visualization of performance trends. Its design emphasizes local data storage (privacy-first approach), single-instance protection, and user-friendly system integration through rich context menus that provide quick access to detailed logs and Windows system tools. The 46MB codebase shows active development (13 commits in 90 days) with a 50/100 tech stack currency score, indicating well-established dependencies, though the minimal community engagement (2 stars, no contributors) and Windows-only deployment suggest this is a specialized utility rather than a mainstream project. KeyPressCounter is primarily targeted at productivity analysts, system administrators, and individual users seeking detailed insights into their computing behavior and system performance without relying on cloud-based monitoring solutions.

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

**sql2csv** is a comprehensive .NET 10 toolkit designed for SQLite database introspection, data export, and code generation, offering both command-line and web-based interfaces for database analysis workflows. The project provides multiple complementary tools: a CLI application for batch operations, an ASP.NET Core MVC web UI for interactive database exploration, a core library (`Sql2Csv.Core`) containing shared business logic, and an experimental data visualization module (`DataSpark.Web`), all supported by unit tests and performance benchmarks using BenchmarkDotNet. Key capabilities include automatic SQLite file discovery within directories, bulk table export to CSV format with optional filtering, schema inspection with multiple output formats (text, JSON, Markdown), and automated C# Data Transfer Object (DTO) generation from database schemas, enabling developers to quickly integrate legacy SQLite databases into modern applications.

The architecture demonstrates a clean separation of concerns with a layered design: the core library abstracts database operations, allowing both the console and web applications to share business logic without duplication, while the web UI adds file persistence, upload management, and interactive analysis capabilities beyond CLI functionality. Built on modern .NET technologies including .NET 10, ASP.NET Core, MSTest, and Node.js for frontend asset management, the project emphasizes maintainability through comprehensive test coverage (with coverage badges) and performance monitoring through dedicated benchmarks. The repository is particularly valuable for database administrators, legacy system modernizers, and developers needing to quickly extract and transform SQLite data into portable CSV formats or strongly-typed C# models, with the dual interface approach accommodating both batch automation (CLI) and interactive exploration (web UI) use cases.

**Created**: 2017-11-06
**Last Modified**: 2026-01-12

---

### #18. [PromptSpark.Chat](https://github.com/markhazleton/PromptSpark.Chat)

Stars: 0 | Forks: 0 | Language: C# | 10 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 19796 KB | 🚀 3.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: PromptSpark.Chat

**PromptSpark.Chat** is an ASP.NET Core-based real-time conversational workflow application designed to guide users through multi-step interactive processes using a dynamic chat interface. The application leverages **SignalR** for real-time bidirectional communication, **Adaptive Cards** for rendering structured, interactive UI elements, and a **ConcurrentDictionary**-based in-memory store for thread-safe conversation state persistence, enabling users to maintain progress across page refreshes without data loss. The architecture employs a node-based workflow pattern where users progress through branching logic defined in JSON configuration files, with optional AI integration via a chat completion service for handling out-of-scope queries, while the multi-language codebase (31.5% C#, 30% SCSS, 28.4% HTML, 8.9% JavaScript) reflects a full-stack MVC implementation with emphasis on responsive front-end styling. The project demonstrates clean separation of concerns through dedicated Controllers, Services, and Views layers, employing simple concurrency management without heavy frameworks, making it lightweight yet production-ready for deployment on cloud platforms like Azure. This solution is particularly well-suited for enterprises and organizations requiring flexible, user-friendly workflow orchestration systems—such as customer onboarding, survey platforms, decision trees, or support ticketing processes—where real-time interaction and conversation continuity are essential, while its minimal overhead and extensible JSON-based workflow definition enable rapid customization and scaling without substantial architectural changes.

**Created**: 2024-12-31
**Last Modified**: 2026-02-10

---

### #19. [AsyncSpark](https://github.com/markhazleton/AsyncSpark)

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

### #20. [FastEndpointApi](https://github.com/markhazleton/FastEndpointApi)

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

### #21. [Texecon](https://github.com/markhazleton/Texecon)

Stars: 0 | Forks: 0 | Language: HTML | 3 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 2957 KB | 🚀 1.0 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: TexEcon

**TexEcon** is a static-generated React application designed to deliver expert analysis and commentary on the Texas economy, leveraging modern web technologies to achieve optimal performance and SEO on GitHub Pages. The project implements a sophisticated build pipeline that fetches dynamic content from a WebSpark headless CMS API during build time, then pre-renders all pages into static HTML files, combining the benefits of static site generation with content freshness and progressive enhancement through client-side routing. The technology stack centers on React 19 with TypeScript for type safety, Vite 7.1 for fast builds, Tailwind CSS 4.1 for styling, and Radix UI/shadcn/ui for accessible, composable components, while employing lightweight routing via Wouter and icons from Lucide React.

The architecture demonstrates a thoughtful approach to content management and deployment: it includes build-time content fetching with graceful fallback mechanisms, automated sitemap generation for SEO optimization, cache busting via build IDs, and structured data implementation for enhanced search visibility. The codebase is well-organized with clear separation between static assets, React components, cached content, utilities, and page routes, supported by comprehensive build automation scripts that orchestrate the full pipeline from cleanup through content retrieval to final static page generation. What distinguishes this project is its pragmatic hybrid approach—combining the SEO and performance benefits of static site generation with the flexibility of a CMS-driven content model and client-side interactivity—making it particularly suitable for content-heavy sites that require both excellent performance metrics and dynamic content updates without rebuilding, while also targeting a specific economic analysis audience in the Texas region.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 50 total (50 current, 0 outdated)

**Created**: 2025-09-03
**Last Modified**: 2026-01-04

---

### #22. [WebSpark.PrismSpark](https://github.com/markhazleton/WebSpark.PrismSpark)

Stars: 0 | Forks: 0 | Language: C# | 14 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 2272 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ✅ Docs

# WebSpark.PrismSpark - Technical Summary

**WebSpark.PrismSpark** is a high-performance C#/.NET port of the popular PrismJS syntax highlighting library, designed to provide server-side code tokenization, syntax highlighting, and theming for .NET applications with support for 24 programming languages (C#, Python, JavaScript, Rust, Go, and more). The project leverages a modular architecture featuring a comprehensive plugin system (line numbers, copy-to-clipboard, toolbars), event-driven hooks for customization, and a flexible theme engine with built-in CSS generation, all optimized for async processing and caching to handle large-scale code highlighting efficiently. Built for .NET 10.0 LTS with backward compatibility to .NET 9.0, it integrates seamlessly into ASP.NET MVC/Razor applications through dependency injection and includes advanced features such as line-specific highlighting, custom CSS classes, and context metadata preservation. The codebase demonstrates strong software engineering practices with a comprehensive 52-test MSTest suite covering grammars, tokenization, and integration scenarios, while the interactive demo web application provides real-time syntax highlighting, a live code editor with validation and formatting, and language-specific showcases. PrismSpark differentiates itself by bringing Prism's powerful, extensible JavaScript highlighting capabilities to server-side .NET environments, eliminating the need for client-side JavaScript execution and enabling better performance, security, and integration with enterprise .NET applications—making it ideal for documentation generators, code review platforms, blog engines, and any .NET application requiring sophisticated syntax highlighting.

**Created**: 2025-05-27
**Last Modified**: 2026-02-11

---

### #23. [WebSpark.ArtSpark](https://github.com/markhazleton/WebSpark.ArtSpark)

Stars: 0 | Forks: 0 | Language: C# | 7 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3658 KB | 🚀 2.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.ArtSpark

**WebSpark.ArtSpark** is a comprehensive .NET 10.0 solution that provides complete client library coverage for the Art Institute of Chicago's public REST API, encompassing all 33 endpoints across 6 major resource categories (Collections, Shop, Mobile, Publications, etc.). The solution consists of four interconnected projects: a strongly-typed async API client library with IIIF image support and Elasticsearch integration, an innovative AI agent system featuring multiple personas (Artwork, Artist, Curator, Historian) powered by OpenAI's GPT-4o with vision capabilities and hot-reloadable prompt configuration, an interactive ASP.NET Core web demo application with user authentication and personal collection management, and a command-line utility for developer access. The architecture emphasizes modern .NET practices including System.Text.Json deserialization with proper naming policies, async/await patterns throughout, minimal external dependencies, and separation of concerns across projects, while the AI components add conversational intelligence with persistent chat history, visual analysis, and content filtering guardrails. The primary use cases are developers integrating Art Institute data into applications, museum enthusiasts exploring artworks through AI-powered conversations, and organizations seeking a reference implementation of clean .NET architecture with AI integration. While currently unmaintained (declining activity with only 7 commits in the last 90 days), the project demonstrates sophisticated integration of REST APIs, machine learning services, and enterprise web application patterns, making it valuable both as a practical tool and educational reference for advanced .NET development.

**Created**: 2023-01-30
**Last Modified**: 2026-01-12

---

### #24. [markhazleton.github.io](https://github.com/markhazleton/markhazleton.github.io)

Stars: 0 | Forks: 0 | Language: SCSS | 1 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 144 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Mark Hazleton's Personal Jekyll Site

This repository is a personal portfolio and blog website built with **Jekyll 3.10.0** and hosted on GitHub Pages, implementing a customized version of the Minima theme with a modern styling approach that eschews external frameworks. The site features responsive design with dark/light mode toggle functionality, markdown-based content management, and comprehensive emoji support, all served through automated GitHub Actions CI/CD pipelines that trigger on commits to the `sources` branch. The tech stack primarily consists of **SCSS (36.8%), HTML (34.6%), and CSS (27.9%)** with minimal Ruby dependencies (`github-pages`, `faraday-retry`, `wdm`), indicating a lean, static-site approach optimized for performance and maintainability.

Key architectural elements include a modular component system with reusable Liquid template includes, a `_drafts` folder workflow for content staging, and Jekyll's standard post structure with YAML front matter for metadata management—enabling SEO optimization through excerpt fields, category/tag taxonomies, and configurable featured images. The project demonstrates solid development practices through dual publishing workflows (direct-to-main and feature-branch approaches), local development support across Windows/macOS/Linux platforms with livereload capabilities, and comprehensive documentation covering setup, post creation, and deployment procedures. With declining activity (1 commit in 90 days, 16 in the past year) and a tech currency score of 50/100, the site appears well-established and stable, serving as a professional portfolio and technical blog suitable for showcasing expertise while maintaining a lightweight, fast-loading presence without third-party frameworks or complex dependencies.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 3 total (3 current, 0 outdated)

**Created**: 2021-04-18
**Last Modified**: 2026-01-12

---

### #25. [DocSpecSpark](https://github.com/markhazleton/DocSpecSpark)

Stars: 0 | Forks: 0 | Language: Unknown | 1 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 0 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# DocSpecSpark - Technical Summary

**DocSpecSpark** is a document specification toolkit designed to facilitate the creation, management, and generation of structured documentation artifacts, particularly for technical specifications and compliance documentation. The project appears to be a utility framework that leverages Apache Spark's distributed computing capabilities (as suggested by the "Spark" naming convention) to handle large-scale document processing, specification generation, or batch documentation tasks at scale. While the repository is newly established (created March 2026) with minimal public activity and no external contributors yet, the recent commit history and maintenance status indicate active development, suggesting the project is in early-stage maturity. The toolkit likely targets technical teams, documentation engineers, and software architects who need to automate specification document generation, maintain version-controlled documentation standards, or process large volumes of technical documentation efficiently. Without access to detailed source code or comprehensive documentation, the project's full scope and specific feature set remain somewhat opaque, but the naming and structure suggest it combines document templating, specification validation, and distributed processing capabilities. This tool would be particularly valuable in enterprise environments requiring standardized, automated documentation pipelines or in organizations managing complex technical specifications across multiple systems.

**Created**: 2026-03-07
**Last Modified**: 2026-03-07

---

### #26. [WebSpark.Bootswatch](https://github.com/markhazleton/WebSpark.Bootswatch)

Stars: 0 | Forks: 0 | Language: HTML | 5 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7124 KB | 🚀 1.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.Bootswatch

**WebSpark.Bootswatch** is a .NET 10-exclusive Razor Class Library that provides seamless integration of Bootswatch themes into ASP.NET Core applications, enabling dynamic theme switching and light/dark mode support with built-in caching mechanisms. The library abstracts Bootstrap 5's theming complexity through extension methods and tag helpers (e.g., `<bootswatch-theme-switcher />`), allowing developers to implement responsive, modern UI themes with minimal configuration while maintaining comprehensive error handling and fallback strategies. Built primarily with HTML (63.8%), C# (28.6%), and supporting PowerShell/JavaScript utilities, the project follows a modern dependency-focused architecture that prioritizes latest-generation packages and security patches over broad framework compatibility—a deliberate design choice reflected in version 2.0's exclusive .NET 10 targeting and deprecation of .NET 8/9 support. The library leverages the `StyleCache` service for high-performance CSS delivery and integrates with `WebSpark.HttpClientUtility` as a core dependency, demonstrating a modular ecosystem approach to shared utilities. Key architectural patterns include service injection through extension methods, caching abstractions, and tag helper encapsulation, making it production-ready for enterprise ASP.NET Core applications requiring flexible, performant theming without heavy manual configuration. This project is particularly valuable for development teams needing rapid theme deployment across multiple ASP.NET Core applications while maintaining performance standards and staying aligned with current .NET framework evolution.

**Created**: 2022-08-24
**Last Modified**: 2026-01-12

---

### #27. [TeachSpark](https://github.com/markhazleton/TeachSpark)

Stars: 0 | Forks: 0 | Language: C# | 1 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 30771 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# TeachSpark - Technical Summary

**TeachSpark** is a modern, LLM-powered educational platform built on .NET 10 MVC that delivers personalized, adaptive learning experiences through AI-driven content delivery. The application features intelligent course personalization, real-time feedback mechanisms, comprehensive progress analytics, and a responsive web interface powered by Webpack 5, Bootstrap 5, and modern ES6+ JavaScript, enabling dynamic curriculum adaptation based on individual student learning patterns and preferences.

The architecture follows Clean Architecture principles with a C# backend utilizing Entity Framework Core for data persistence and a sophisticated frontend build system incorporating hot module replacement, code splitting, and automated asset optimization. The project demonstrates strong engineering practices through comprehensive tooling integration including Husky pre-commit hooks, ESLint/Prettier/Stylelint quality enforcement, and lint-staged automation that maintains code quality standards across both backend and frontend codebases.

TeachSpark targets educational institutions and online learning platforms seeking to implement intelligent tutoring systems that leverage Large Language Models for enhanced pedagogical outcomes. While currently in early-stage development (0 stars, 32 commits over 365 days), the project represents a well-architected foundation for building scalable, AI-enhanced educational technology with clear separation of concerns, modern development workflows, and infrastructure prepared for production deployment. The tech stack is contemporary (.NET 10, Node.js 18+) with a tech currency score of 50/100, indicating moderate adoption of current industry standards while maintaining stability over cutting-edge experimentation.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 3 total (3 current, 0 outdated)

**Created**: 2025-06-19
**Last Modified**: 2026-01-12

---

### #28. [DecisionSpark](https://github.com/markhazleton/DecisionSpark)

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

### #29. [MechanicsOfMotherhood](https://github.com/markhazleton/MechanicsOfMotherhood)

Stars: 0 | Forks: 0 | Language: TypeScript | 7 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 5888 KB | 🚀 2.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Mechanics of Motherhood

**Mechanics of Motherhood** is a production-ready recipe management web application specifically designed for busy working mothers, featuring 108+ curated recipes with intelligent categorization, search, and filtering capabilities. Built with modern React 19 and TypeScript, the application implements a client-side SPA architecture powered by Vite for rapid builds, TanStack Query for efficient server state management, and Tailwind CSS with Shadcn/ui components for a cohesive industrial-themed UI. The project demonstrates strong architectural practices including real-time API integration (RecipeSpark and WebCMS APIs) with graceful fallback to mock data, automated data quality validation pipelines, and comprehensive CI/CD automation through GitHub Actions that deploys to GitHub Pages with a custom domain setup. Key differentiators include mobile-first responsive design optimized for 3G networks, PWA capabilities with offline support, WCAG accessibility compliance, and impressive performance metrics (95+ Lighthouse scores, ~130KB gzipped bundle). This is a fully maintained, professionally-deployed application targeting home cooks and meal planners who need efficient recipe organization and meal planning tools with a focus on usability for time-constrained working mothers.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 46 total (46 current, 0 outdated)

**Created**: 2025-09-01
**Last Modified**: 2026-01-31

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

### #31. [HttpClientDecoratorPattern](https://github.com/markhazleton/HttpClientDecoratorPattern)

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

### #32. [Yelp.Api](https://github.com/markhazleton/Yelp.Api)

Stars: 0 | Forks: 0 | Language: C# | 1 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 462 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: Yelp.API

**Yelp.API** is a C# class library that provides a managed wrapper around Yelp's v3 Fusion API, enabling .NET developers to seamlessly integrate local business search and review functionality into their applications targeting .NET 6 and later frameworks. The library abstracts the complexity of REST API calls to Yelp's backend, offering both simplified convenience methods (e.g., `SearchBusinessesAllAsync()`) and advanced query capabilities through structured `SearchRequest` objects, allowing developers to search millions of businesses across 32 countries with support for filtering by location, search terms, result limits, and operational status. Built primarily in C# (53.1%) with supplementary web assets (CSS, HTML, JavaScript), the project demonstrates a clean separation of concerns with a client-based architecture that handles authentication via API key injection and asynchronous operations for non-blocking I/O. The codebase employs modern async/await patterns and appears to follow standard .NET library conventions with organized model classes for request/response handling, making it accessible for both simple and complex business discovery scenarios. While currently unmaintained (zero recent activity over 90+ days), the library targets developers building .NET applications requiring Yelp business intelligence, review data, and location-based search functionality—useful for applications in travel, food delivery, local commerce, and business intelligence domains. The straightforward integration API and credential management approach via .NET secrets management make it a practical choice for teams already invested in the Microsoft development ecosystem.

**Created**: 2022-08-10
**Last Modified**: 2026-01-12

---

### #33. [react-native-web-start](https://github.com/markhazleton/react-native-web-start)

Stars: 0 | Forks: 0 | Language: TypeScript | 1 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3184 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary

**react-native-web-start** is a production-ready, enterprise-grade starter template designed to enable true cross-platform application development using React Native Web, Vite, and TypeScript. The project allows developers to write a single codebase and deploy across web (via Vite), iOS (via Xcode), and Android (via Metro bundler) platforms, significantly reducing development time and maintenance overhead for organizations building multi-platform applications.

The template features a sophisticated monorepo structure with shared components, platform-specific configurations, and a comprehensive build automation pipeline that includes asset management, documentation synchronization, and dynamic build metadata generation. Key capabilities include full TypeScript type safety, modern styling with Tailwind CSS and Sass preprocessing, an integrated markdown documentation browser, responsive design patterns, production-ready HTTP client integration, and GitHub Pages deployment automation with CI/CD pipelines.

Built on a modern technology stack featuring React 19.2.3, React Native 0.83.1, Vite 7.3.1, and TypeScript 5.9.3, the architecture implements organized separation of concerns through dedicated packages for shared logic, web-specific, and mobile-specific code. The project includes developer-focused features such as hot module replacement for instant feedback, ESLint and Prettier configuration, Jest testing setup, and comprehensive in-app documentation with markdown support.

While the repository shows declining activity (54 commits over 365 days with only 1 recent commit), it maintains a moderate tech stack currency score of 50/100 and demonstrates enterprise-grade practices through security integrations (Dependabot), performance monitoring capabilities, PWA readiness, and SEO optimization. This template is ideal for startups and enterprises seeking to maximize code reuse across platforms while maintaining strict type safety and leveraging modern development tooling, with a particular focus on reducing the complexity traditionally associated with cross-platform mobile and web development.

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

**InquirySpark** is a modern .NET 10-based survey and inquiry management system designed as a read-only data exploration platform, featuring a responsive MVC admin interface built with Bootstrap 5 and DataTables for intuitive data visualization and management. The architecture leverages Entity Framework Core 10 with SQLite as the persistence layer, operated strictly in read-only mode to ensure data immutability, making it ideal for audit-safe analytics and reporting scenarios where schema integrity is paramount. The solution is composed of modular components—including an admin UI layer (InquirySpark.Admin), a data access abstraction layer (InquirySpark.Repository), and shared domain models (InquirySpark.Common)—all enforced with nullable reference types, comprehensive XML documentation, and automated npm asset pipeline integration for a zero-CDN-dependency deployment model. Its key distinguishing feature is the elimination of SQL Server dependency in favor of lightweight, file-based SQLite databases with immutable connection strings, reducing infrastructure overhead while maintaining full EF Core capabilities and testability through MSTest integration tests. The project targets developers and organizations requiring self-contained survey platforms with strict data governance, read-only reporting requirements, or proof-of-concept implementations where minimal external dependencies are desirable, supported by comprehensive documentation covering Bootstrap templates, DataTables configuration, and SQLite asset management.

**Created**: 2023-10-24
**Last Modified**: 2025-12-07

---

### #35. [TriviaSpark](https://github.com/markhazleton/TriviaSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 27238 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# TriviaSpark - Technical Summary

**TriviaSpark** is a multiplayer trivia game application developed as an experimental project using ChatGPT assistance, designed to integrate with public Trivia APIs to deliver competitive gaming experiences across web and mobile platforms. The application is built primarily with **C# (.NET)** for backend logic (61.1%), complemented by **HTML, CSS, and JavaScript** (26.5%, 12.3%, and 0.1% respectively) for frontend presentation, suggesting an ASP.NET or Blazor-based architecture with traditional web technologies. Core features include user registration and authentication systems, a leaderboard ranking system for competitive gameplay, admin-level question database management, and a customizable UI designed to support both web and mobile clients while maintaining a modern, interactive interface. The application follows a standard multi-tier web application pattern, consuming external Trivia APIs to populate dynamic question sets and managing user sessions, scores, and rankings through backend persistence. The project is notable as a case study in AI-assisted development, demonstrating ChatGPT's capability to scaffold functional applications while targeting a broad demographic (ages 18-95) of tech-savvy trivia enthusiasts seeking competitive gaming experiences. However, the repository shows minimal recent activity (zero commits in 90 days, declining engagement), suggesting the project may be in maintenance mode or has stalled in active development despite its ambitious scope covering both web and mobile deployment targets.

**Created**: 2023-02-22
**Last Modified**: 2025-12-02

---

### #36. [DataAnalysisDemo](https://github.com/markhazleton/DataAnalysisDemo)

Stars: 0 | Forks: 0 | Language: Visual Basic .NET | 0 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 12926 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: DataAnalysisDemo (DAWPM)

**DataAnalysisDemo** is a comprehensive web-based data analytics platform built on ASP.NET WebForms 4.8 that enables users to upload and analyze CSV files through interactive visualizations, pivot tables, and detailed statistical analysis. The application features a modern client-side architecture powered by Bootstrap 5.3.8, jQuery 3.7.1, and a Webpack-based build system, providing responsive UI components alongside advanced data processing capabilities including dynamic charting (D3.js, C3.js, Microsoft Chart Controls), pivot table operations, and DataTables v2 integration with search panes and export functionality. The backend uses a custom GenericParser library for efficient CSV processing with support for large datasets, while the frontend leverages a sophisticated asset bundling pipeline with npm package management to handle 24 key dependencies including Bootstrap, DataTables, Chosen.js, and visualization libraries. The codebase demonstrates hybrid legacy-modern architecture patterns, combining older ASP.NET WebForms infrastructure with contemporary ES6+ JavaScript, responsive design principles, and client-side build optimization techniques. With 69.8% Visual Basic .NET code alongside 16.5% ASP.NET and supporting JavaScript/CSS, the project targets business analysts and data professionals seeking a user-friendly platform for exploratory data analysis without requiring specialized statistical software. The project's moderate tech stack currency score (50/100) and minimal recent activity (zero commits in 90 days, declining to 6 commits annually) suggest it functions as a stable demonstration or educational reference implementation rather than an actively maintained production system.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 24 total (24 current, 0 outdated)

**Created**: 2023-04-20
**Last Modified**: 2025-12-03

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

- **Generation Time**: 2.0 seconds
- **SVGs Generated**: 6/6
- **Total API Calls**: 0
- **Total AI Tokens**: 88,517
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