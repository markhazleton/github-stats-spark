# GitHub Profile: markhazleton

**Generated**: 2026-05-13 17:29:11 UTC
**Report Version**: 1.0.0
**Repositories Analyzed**: 30
**AI Summary Rate**: 100.0%

> 💡 **Navigation**: [Profile Overview](#profile-overview) | [Top Repositories](#top-30-repositories) | [Metadata](#report-metadata)

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

## Top 30 Repositories

### #1. [devspark](https://github.com/markhazleton/devspark)

Stars: 0 | Forks: 0 | Language: Python | 284 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 6710 KB | 🚀 94.7 commits/month

**Quality**: ❌ License | ✅ Docs

# DevSpark Technical Summary

DevSpark is a structured workflow framework designed to enhance AI coding assistants with repeatable, methodology-driven development processes through modular markdown-based prompts and optional CLI tooling. The project provides 28 slash-command templates covering the entire software development lifecycle—from requirements specification through release—that work across 15+ AI agents (Claude, Copilot, Cursor, Gemini, etc.) without requiring installation or dependencies on the agent side. The core offering is intentionally lightweight and distribution-agnostic: users can copy markdown files directly into their projects or use optional Python CLI tools (`click`, `pydantic`, `jsonschema`, `PyYAML`) for automated setup, environment validation, and a declarative harness runtime that executes reproducible engineering workflows with structured artifact generation.

The architecture combines three complementary components: (1) 28 prompt templates organized by workflow phases (specify → plan → implement → review → release) plus constitution-based commands that enforce project principles; (2) shell/PowerShell context-gathering scripts that prepare codebase metadata for AI consumption; and (3) an optional harness runtime (`devspark harness run`) that orchestrates multi-step declarative workflows with state preservation and adapter-based extensibility. DevSpark's philosophy emphasizes human-in-the-loop decision gates (specs reviewed before implementation, PRs approved before merging) and supports multi-app monorepo scenarios through optional registry-based application scoping. With 284 commits in 90 days, accelerating activity, and 76/100 tech stack currency, the project is actively evolving toward production readiness while maintaining its core promise: no mandatory tooling, just markdown files that AI assistants can copy and execute immediately within existing chat interfaces.

**Technology Stack Currency**: ✅ 76/100
**Dependencies**: 5 total (1 current, 4 outdated)

**Created**: 2026-04-02
**Last Modified**: 2026-05-11

---

### #2. [TailwindSpark](https://github.com/markhazleton/TailwindSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 105 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 3866 KB | 🚀 35.0 commits/month

**Quality**: ❌ License | ✅ Docs

# TailwindSpark - Technical Summary

**TailwindSpark** is a production-ready React TypeScript monorepo that serves as a comprehensive showcase and learning resource for modern web development patterns, specifically demonstrating Tailwind CSS 4's capabilities including the `@theme` directive and semantic design tokens. The project implements a scalable architecture using Turborepo with shared packages for design tokens and reusable UI components, coupled with a main demo application that provides interactive examples and extensive documentation covering setup, architecture, testing standards, and project governance.

The technology stack leverages React 19.1.1, TypeScript 5.9, and Tailwind CSS 4.1.18, with additional tooling including Vitest for testing, ESLint for code quality, accessibility auditing via @axe-core/react, and automated CI/CD workflows with Dependabot integration for dependency management. The project emphasizes production quality through strict TypeScript enforcement, a minimum 40% test coverage requirement, WCAG AA accessibility compliance, and formal code governance documented in a project constitution. Its monorepo structure with shared design systems and component libraries demonstrates enterprise-scale architectural patterns while remaining accessible as an educational resource.

What makes TailwindSpark particularly notable is its dual purpose: it functions simultaneously as a living educational platform showcasing cutting-edge React and Tailwind CSS patterns and as a reference implementation of production engineering best practices, including automated security scanning, performance monitoring, and regular constitutional compliance audits. The project targets both developers seeking to learn modern web development practices and technical architects looking for patterns and governance models for building scalable design systems. With highly active development (105 commits in 90 days, accelerating activity patterns), comprehensive documentation, and a live deployed instance, TailwindSpark represents an exceptionally well-maintained demonstration project that bridges the gap between educational content and production-grade code.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2025-07-29
**Last Modified**: 2026-05-11

---

### #3. [WebSpark.HttpClientUtility](https://github.com/markhazleton/WebSpark.HttpClientUtility)

Stars: 0 | Forks: 0 | Language: C# | 75 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 3127 KB | 🚀 25.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.HttpClientUtility

**WebSpark.HttpClientUtility** is a production-ready, enterprise-grade HTTP client wrapper for .NET 8-10 LTS that dramatically simplifies HttpClient configuration by bundling resilience patterns (Polly retry/circuit-breaker policies), intelligent response caching, structured logging with correlation IDs, and OpenTelemetry observability into a single-line `AddHttpClientUtility()` dependency injection call. The library eliminates boilerplate—reducing typical 50+ lines of manual HttpClient setup to one configuration statement—while maintaining strict semantic versioning, comprehensive test coverage across all supported .NET versions, source-link debugging support, and AOT/trimming readiness for modern cloud-native deployments. Delivered as two modular NuGet packages (core HTTP utilities and an optional web-crawling extension with robots.txt parsing), it targets microservice architects and backend developers who need battle-tested resilience patterns, distributed tracing, and request/response caching without manual Polly boilerplate or framework lock-in. The project demonstrates strong engineering discipline through continuous GitHub Actions CI/CD, zero-warning builds with strict compiler settings, package validation, and transparent breaking-change commitments—positioning it as a pragmatic middle ground between raw HttpClient complexity and opinionated frameworks like Refit, particularly valuable for teams building rate-limited API consumers, web scrapers, or distributed systems requiring automatic correlation tracking and telemetry instrumentation.

**Created**: 2025-05-03
**Last Modified**: 2026-05-11

---

### #4. [InquirySpark](https://github.com/markhazleton/InquirySpark)

Stars: 0 | Forks: 0 | Language: C# | 64 commits (90d)

👥 0 contributors | 🌐 9 languages | 💾 13989 KB | 🚀 21.3 commits/month

**Quality**: ❌ License | ✅ Docs

# InquirySpark - Technical Summary

**InquirySpark** is a modern .NET 10 MVC web application that serves as a unified survey, inquiry, and decision-management system, designed to consolidate multiple legacy applications into a single integrated workspace. The platform delivers comprehensive operational capabilities including survey management, capability completion matrices, operational readiness assessments, and system health monitoring through a responsive Bootstrap 5 UI with DataTables integration, all backed by read-only SQLite databases that eliminate the need for SQL Server infrastructure.

The architecture demonstrates contemporary ASP.NET Core best practices, leveraging Entity Framework Core 10 with primary constructors, ASP.NET Core Identity for authentication, structured logging via a custom `IUnifiedAuditService`, and a standardized response pattern (`BaseResponse<T>`) across all service layers. The application consolidates formerly separate applications (`DecisionSpark` and `InquirySpark.Admin`) into a single authenticated area structure under `/Unified/`, with npm-driven frontend asset pipelines for dependency-free Bootstrap and icon delivery.

The project is notable for its immutable database strategy—using read-only mode for the inquiry domain database while maintaining read-write access solely for Identity operations—enforced warning-as-error compilation with nullable reference types, comprehensive MSTest coverage (99/108 tests passing), and detailed documentation governance through a formal project constitution. Target users include operations teams, decision-makers, and system administrators requiring integrated visibility into surveys, capability readiness, and system health across multiple business domains, with deployment demonstrated at a live production site (`inquiry.makeboldspark.com`).

**Created**: 2023-10-24
**Last Modified**: 2026-05-11

---

### #5. [git-spark](https://github.com/markhazleton/git-spark)

Stars: 0 | Forks: 0 | Language: PowerShell | 52 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 2064 KB | 🚀 17.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Git Spark - Technical Summary

**Git Spark** is a sophisticated Git repository analytics and reporting tool that analyzes commit history to generate interactive, enterprise-grade HTML dashboards with comprehensive insights into contributor activity, code change patterns, and development metrics. Built with TypeScript and PowerShell, it provides both a command-line interface and Node.js API for flexible integration, supporting multiple export formats (HTML, JSON, CSV, Markdown) and featuring advanced analytical capabilities including contribution heatmaps, governance radar charts, risk factor analysis, and file-level change tracking. The tool emphasizes analytical integrity and transparency by embedding all data directly in self-contained reports with strict Content Security Policy protections, native SVG visualizations (avoiding external dependencies), and comprehensive documentation of metric limitations to prevent misinterpretation of Git data. Key differentiators include dark mode support with persistent preferences, progressive pagination for large datasets, email redaction for privacy-sensitive audits, configurable date range analysis with timezone support, and accessibility enhancements including ARIA live regions and keyboard navigation. The project demonstrates production-ready engineering practices with 100/100 tech stack currency, 22 well-curated dependencies (commander, ora, chalk, boxen for CLI excellence), consistent commit activity (52 commits in 90 days), and explicit focus on air-gapped deployment scenarios where reports serve as standalone analytical artifacts. Git Spark targets development teams, technical leaders, and auditors seeking data-driven insights into repository health, contributor patterns, and potential code quality risks, while maintaining principled honesty about what Git commit metadata can—and cannot—reveal about actual development practices.

**Technology Stack Currency**: ✅ 98/100
**Dependencies**: 22 total (21 current, 1 outdated)

**Created**: 2025-09-29
**Last Modified**: 2026-05-12

---

### #6. [BootstrapSpark](https://github.com/markhazleton/BootstrapSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 51 commits (90d)

👥 0 contributors | 🌐 8 languages | 💾 38193 KB | 🚀 17.0 commits/month

**Quality**: ❌ License | ✅ Docs

# BootstrapSpark - Technical Summary

**BootstrapSpark** is a production-ready, enterprise-grade developer portfolio and technical demonstration platform built with React 19, TypeScript, and Vite, deployed on Azure Static Web Apps. The project showcases modern frontend engineering best practices by implementing a sophisticated single-page application that integrates multiple real-time features including SignalR-powered chat with AI personalities, live weather data visualization with interactive Leaflet maps, dynamic RSS feed aggregation, and a searchable project portfolio system that pulls content from external APIs. The architecture leverages a frontend-first design pattern with TypeScript strict mode for type safety, Vite for optimized bundling and hot module reloading, Bootstrap 5 with custom SCSS for responsive UI components, and implements comprehensive accessibility standards (WCAG 2.1 AA compliance), dark/light theme switching, and SEO optimization with structured data. Notably, the project emphasizes developer experience through well-documented code organization, CI/CD automation via GitHub Actions, dual deployment strategies (Azure and GitHub Pages), and intentional architectural transparency regarding Content Security Policy trade-offs required for external API integration. The technology stack is modern and actively maintained, featuring 47 dependencies including Axios for HTTP communication, date-fns for date utilities, and xml2js for RSS parsing, with accelerating development activity (90-day and 365-day commit patterns indicate sustained engagement). This repository serves as both a professional portfolio and a comprehensive reference implementation for teams building scalable, maintainable web applications with modern JavaScript frameworks and cloud-native architectures.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 47 total (47 current, 0 outdated)

**Created**: 2024-10-11
**Last Modified**: 2026-05-13

---

### #7. [RequestSpark](https://github.com/markhazleton/RequestSpark)

Stars: 2 | Forks: 1 | Language: C# | 48 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 966 KB | 🚀 16.0 commits/month

**Quality**: ❌ License | ✅ Docs

# RequestSpark: Technical Summary

RequestSpark is a modern .NET 10 (LTS) web application and console tool designed for comprehensive REST API testing, performance benchmarking, and regression testing against Postman collections. The platform provides a browser-based dashboard built with ASP.NET Razor Pages that enables users to import Postman collections, execute automated test suites, perform load testing, and analyze API performance metrics including response time percentiles, success rates, and detailed statistics exportable to CSV. The architecture is multi-layered, comprising a console application (`RequestSpark`), domain logic library (`RequestSpark.Domain`), specialized Postman import module (`RequestSpark.PostmanImport`), and web application (`RequestSpark.Web`), with comprehensive test coverage via MSTest v4 achieving 100% pass rate across 21 tests. Key technical strengths include recent optimization to .NET 10 delivering 19% faster builds and 25% faster test execution, a lean dependency footprint (15 packages with 93% at latest versions), zero security vulnerabilities, and built-in sample CRUD API for demonstration purposes. The project targets API developers, QA engineers, and solutions architects who need programmatic testing and performance analysis capabilities beyond traditional Postman workflows, with deployment demonstrated through a live instance at request.makeboldspark.com. This actively maintained project (48 commits in 90 days) represents a production-ready solution that combines accessibility through web UI with automation capabilities for CI/CD integration and scalable API test management.

**Created**: 2021-09-30
**Last Modified**: 2026-05-11

---

### #8. [KeyPressCounter](https://github.com/markhazleton/KeyPressCounter)

Stars: 2 | Forks: 1 | Language: C# | 10 commits (90d)

👥 0 contributors | 🌐 2 languages | 💾 46631 KB | 🚀 3.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: KeyPressCounter

**KeyPressCounter** is a lightweight Windows system tray utility written in C# (.NET 10.0) that monitors keyboard and mouse input activity while simultaneously tracking real-time system performance metrics. The application runs silently in the background, using global input hooks (via SharpHook library) to count keystrokes and mouse clicks without capturing keystroke content or transmitting data, and supplements this with real-time CPU, memory, disk, and network monitoring through Windows Performance Counters and WMI. The architecture follows a single-instance, event-driven pattern centered on `CustomApplicationContext`, which manages system tray integration, background timers, global hooks, and a thread-safe counter mechanism with idle detection via P/Invoke to `GetLastInputInfo`. The feature-rich dashboard (WinForms-based, three-tab interface) displays input statistics, live performance gauges with 60-second rolling GDI+ graphs, hardware inventory, top-10 process rankings, and activity/summary logs that persist to JSON configuration and daily text logs in the user's AppData directory. This project is ideal for productivity analysts, developers, or system administrators who need unobtrusive activity tracking and performance visibility without the privacy concerns or complexity of enterprise monitoring solutions, distinguished by its zero-data-transmission model, offline-first design, and deep Windows integration with minimal resource overhead.

**Technology Stack Currency**: ✅ 57/100
**Dependencies**: 4 total (3 current, 1 outdated)

**Created**: 2024-03-07
**Last Modified**: 2026-05-12

---

### #9. [WebSpark](https://github.com/markhazleton/WebSpark)

Stars: 1 | Forks: 0 | Language: C# | 10 commits (90d)

👥 0 contributors | 🌐 8 languages | 💾 69582 KB | 🚀 3.3 commits/month

**Quality**: ❌ License | ❌ Docs

# WebSpark Technical Summary

**WebSpark** is a comprehensive .NET 9 suite of ASP.NET Core MVC web applications demonstrating modern enterprise architecture patterns, featuring three main applications (PromptSpark for LLM prompt optimization, RecipeSpark for recipe management, and TriviaSpark for quiz creation) alongside supporting modules for content management, async operations, and identity services. The platform integrates advanced AI capabilities through Semantic Kernel/OpenAI APIs and enables real-time communication via SignalR, built with a scalable 7-area modular architecture that emphasizes separation of concerns and reusability across 43.7% C# backend code, 33.7% HTML/Razor templates, and styling infrastructure.

A distinctive feature is its **spec-driven development workflow** powered by SpecKit, an innovative command-based system (`/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.critic`, `/speckit.implement`, `/speckit.review`) that enforces rigorous specification-first development with automated adversarial risk assessment—identifying showstoppers, security vulnerabilities, performance killers, and operational readiness gaps before implementation begins. The repository also demonstrates sophisticated **SEO optimization** capabilities including dynamic meta tags, JSON-LD structured data, canonical URL management, XML sitemaps, multi-engine verification, and analytics integration with Core Web Vitals monitoring, backed by 47 passing test cases.

Built by Mark Hazleton as a technical reference portfolio, WebSpark targets enterprise architects, senior developers, and technical decision-makers seeking practical examples of scalable, maintainable .NET solutions that balance modern web technologies (Bootstrap 5, responsive design) with architectural best practices, DevOps-ready health checks, and comprehensive monitoring—making it valuable for both educational reference and production-grade implementation patterns.

**Created**: 2024-01-11
**Last Modified**: 2026-05-11

---

### #10. [MuseumSpark](https://github.com/markhazleton/MuseumSpark)

Stars: 0 | Forks: 0 | Language: Python | 27 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 24264 KB | 🚀 9.0 commits/month

**Quality**: ❌ License | ✅ Docs

# MuseumSpark - Technical Summary

**MuseumSpark** is an intelligent travel planning platform that transforms the Walker Art Center Reciprocal Program membership list into a data-rich, searchable resource for art enthusiasts across North America. The project curates information on 1,269 museums and provides smart filtering, priority scoring, and trip planning capabilities to help users discover and visit museums aligned with their interests and time constraints. The platform employs a sophisticated multi-phase data enrichment pipeline that aggregates information from Wikidata, Wikipedia, museum websites, and structured data sources, applying JSON Schema validation and data quality assurance rules to progressively enrich each museum record across 10+ enrichment phases.

The frontend is built with **React 19 + Vite + Tailwind CSS**, deployed as a static site on GitHub Pages with local search/filter functionality and detailed museum pages. The backend data infrastructure leverages **Python 3.11+ with Pydantic 2** for validation, **BeautifulSoup4** for web scraping, and custom scripts for multi-source data integration and quality tracking. The project follows a well-defined roadmap progressing from foundational data enrichment (currently 0.08% complete) through expert-driven priority scoring and AI-assisted content generation, ultimately culminating in a full-featured backend with **FastAPI, SQLite persistence, and PydanticAI** for user authentication, favorite saving, and AI-powered travel recommendations. What distinguishes MuseumSpark is its transparent, phased approach to data quality—openly tracking enrichment progress through a public dashboard and enforcing strict validation rules (e.g., "never replace known with null")—combined with its focus on art-specific curation rather than generic directory functionality, making it particularly valuable for curated travel planning in the museum/cultural tourism space.

**Created**: 2026-01-15
**Last Modified**: 2026-05-10

---

### #11. [UISampleSpark](https://github.com/markhazleton/UISampleSpark)

Stars: 8 | Forks: 4 | Language: HTML | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 31198 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: UISampleSpark

**UISampleSpark** is an educational ASP.NET Core (.NET 10) reference application that demonstrates comparative implementations of the same Employee/Department CRUD domain across seven distinct front-end UI patterns—MVC, Razor Pages, jQuery AJAX, React, Vue, htmx, and Blazor Server—within a unified application. The project showcases modern web development practices including clean architecture with dependency injection, repository/service patterns, RESTful API design (with Swagger/OpenAPI), dynamic theming via Bootswatch, and containerized deployment via Docker and Azure, making it an invaluable resource for developers evaluating UI technology trade-offs.

The codebase demonstrates enterprise-grade patterns such as separation of concerns (Core/Data/UI project structure), in-memory EF Core data persistence with mock data generation, API key-based security, health checks, Application Insights telemetry, and comprehensive CI/CD automation using GitHub Actions and Azure Pipelines. Key technical implementations include React 18 with hooks and Fetch API, Vue 3 Composition API, real-time Blazor components via SignalR, server-driven htmx interactions, and a SPA variant with DataTables and advanced reporting via PivotTable.js, all unified under responsive Bootstrap 5 styling with instant light/dark theme switching capabilities.

The project is particularly notable for its pedagogical value and production-readiness: it serves as a living documentation artifact for .NET ecosystem evolution (tracking migrations from .NET 5 through .NET 10), includes unit test projects for domain and repository layers, features interactive API documentation, and maintains an extensive commit history visualization tool (`git-spark` reports) to aid learning. This makes **UISampleSpark** ideal for architects and mid-to-senior developers evaluating front-end frameworks, learning ASP.NET Core best practices, designing scalable UI architectures, or preparing for technology modernization initiatives—while the stale repository status (90+ days without commits) suggests it may serve primarily as a reference implementation rather than an actively developed product.

**Created**: 2019-04-25
**Last Modified**: 2026-05-13

---

### #12. [FastEndpointApi](https://github.com/markhazleton/FastEndpointApi)

Stars: 3 | Forks: 1 | Language: HTML | 2 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 153 KB | 🚀 0.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: FastEndpointApi

**FastEndpointsSpark** is a comprehensive demonstration and educational project showcasing the FastEndpoints framework (v7.1.1) for building high-performance REST APIs on .NET 10. The repository implements a fully functional Person Management API that illustrates the REPR (Request-Endpoint-Response) pattern, featuring complete CRUD operations, in-memory data persistence, dependency injection, smart DTO mapping, HATEOAS hypermedia links, and integrated Swagger/OpenAPI documentation. The tech stack includes FastEndpoints for the API framework, Bogus for synthetic data generation, Bootstrap for the frontend UI, and GitHub Actions with Azure Web Apps for CI/CD deployment, with the codebase composed primarily of HTML (63.1%), C# (35.7%), and JavaScript (1.3%). The project employs clean architecture principles with separation of concerns through service layers, reusable base endpoint classes, and a well-organized project structure that makes it ideal for developers learning FastEndpoints or seeking production-ready patterns for ASP.NET Core API development. The repository includes extensive documentation, a live demo site, interactive Swagger UI, and a companion article, positioning it as both an educational resource and a practical reference implementation for building maintainable, performant REST APIs with minimal boilerplate code. Though experiencing slightly declining activity (2 recent commits over 90 days), the project remains actively maintained and represents a valuable technical resource for the FastEndpoints community.

**Created**: 2024-04-06
**Last Modified**: 2026-05-12

---

### #13. [SupportSpark](https://github.com/markhazleton/SupportSpark)

Stars: 0 | Forks: 0 | Language: PowerShell | 37 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 1675 KB | 🚀 12.3 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: SupportSpark

**SupportSpark** is a compassionate support network platform that enables members to share life journey updates with invited supporters through a role-based, invitation-only system with organized threaded conversations. The application addresses the emotional and logistical burden of repeatedly updating loved ones during challenging life moments by providing a centralized, calming space where members post once and supporters engage through structured threaded replies, creating meaningful, organized dialogue rather than scattered messages.

The platform features a sophisticated full-stack TypeScript architecture combining **React 19 + Vite** for the frontend with **Express 5** for the backend, leveraging **Tailwind CSS 4** and **Radix UI/shadcn** components for an accessible, peace-focused interface designed specifically for sensitive emotional contexts. The tech stack emphasizes type safety (strict TypeScript with Zod runtime validation), modern state management (TanStack React Query), and performance (HMR during development, optimized static builds), while maintaining end-to-end type safety through shared schema definitions between client and server.

Architecturally, SupportSpark demonstrates sophisticated **role-based access control** with distinct member (update creator) and supporter (reader/responder) capabilities, localStorage-based data persistence for GitHub Pages deployment, and a dual deployment strategy supporting both serverless browser-based operation and Windows IIS production hosting via iisnode. The project exemplifies thoughtful engineering for a sensitive use case, with comprehensive documentation, automated PowerShell deployment scripts, and consideration for accessibility and usability across devices, making it both a functional support platform and a technical demonstration of full-stack modern web development patterns.

**Target Users**: Individuals navigating health challenges, life transitions, or personal journeys who need to keep support networks informed; supporters seeking structured engagement with loved ones during difficult periods.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 97 total (97 current, 0 outdated)

**Created**: 2026-02-01
**Last Modified**: 2026-05-11

---

### #14. [markhazleton](https://github.com/markhazleton/markhazleton)

Stars: 0 | Forks: 0 | Language: Unknown | 26 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 6624 KB | 🚀 8.7 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: markhazleton Repository

This repository serves as Mark Hazleton's primary portfolio and knowledge archive, functioning as a personal learning hub and central hub for showcasing .NET and Azure engineering expertise. The project encompasses a collection of full-stack web applications and developer tooling, including WebSpark (a comprehensive demo application hosting platform), ReactSpark (a Vite-based React application on Azure Static Web Apps), TailwindSpark (an opinionated UI component library), and UISampleSpark (a containerized UI reference application available on Docker Hub). The technology stack centers on .NET/C# backend services with Azure cloud infrastructure, complemented by modern frontend frameworks (React with Vite) and CSS frameworks (Tailwind), demonstrating a polyglot approach to building production-grade applications. The repository emphasizes clean architecture principles, continuous learning, and developer experience—evidenced by articles on CLI design, blogging workflows, and engineering metrics—along with DevOps practices including containerization and automated deployment pipelines. The 26 commits over the past 90 days and accelerating activity pattern indicate active maintenance and evolution, with a particular focus on developer tooling (DevSpark CLI) and content-driven education. Target audience includes enterprise developers, DevOps engineers, and technology enthusiasts interested in modern cloud-native .NET development patterns, CI/CD automation, and Azure hosting strategies.

**Created**: 2021-04-17
**Last Modified**: 2026-05-12

---

### #15. [WebProjectMechanics](https://github.com/markhazleton/WebProjectMechanics)

Stars: 3 | Forks: 0 | Language: Visual Basic .NET | 11 commits (90d)

👥 0 contributors | 🌐 10 languages | 💾 52587 KB | 🚀 3.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebProjectMechanics

**WebProjectMechanics** is a sophisticated multi-tenant content management system currently undergoing a greenfield migration from legacy ASP.NET Web Forms to modern .NET 9, designed to manage and publish static HTML websites for 36+ domains from a single application instance. The system employs a plugin-based architecture with domain-specific modules (CMS, Mineral Collection, Recipes) backed by per-site SQLite databases, eliminating the need for tenant ID columns through physical file isolation—a design pattern that significantly simplifies multi-tenancy complexity. Built on ASP.NET Core 9 Minimal APIs with EF Core 9 for data access, Scriban for templating, and Caddy 2 as a reverse proxy and static file server, the architecture follows a publish-to-static pattern where all public content is pre-rendered to HTML, enabling extremely cost-effective hosting (~$10/month on a single Ubuntu Linux VM) with automatic SSL management. The project is particularly noteworthy for its pragmatic approach to migration—maintaining a frozen archive of the 20+ year legacy codebase while developing a comprehensive implementation plan with detailed phased delivery, comprehensive documentation of both legacy and new systems, and supporting infrastructure-as-code for Caddy and systemd deployment. This makes it an excellent reference implementation for organizations managing high-availability, multi-domain web properties seeking to modernize legacy platforms while maintaining operational continuity, targeting small-to-medium web hosting scenarios where cost efficiency and simplicity are paramount.

**Created**: 2017-09-19
**Last Modified**: 2026-04-13

---

### #16. [react-native-web-start](https://github.com/markhazleton/react-native-web-start)

Stars: 0 | Forks: 0 | Language: PowerShell | 28 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2147 KB | 🚀 9.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: React Native Web Vite Starter

**React Native Web Start** is a production-ready, enterprise-grade starter template that enables cross-platform application development using React Native Web, Vite, and TypeScript. The project allows developers to write a single codebase that deploys to web (via Vite), iOS, and Android platforms simultaneously, addressing the "write once, deploy everywhere" paradigm. It combines React 19.2.5, React Native 0.85.0, and React Native Web 0.21.2 for consistent API surfaces across platforms while leveraging Vite's lightning-fast build tooling (HMR support) and TypeScript 6.0.2 for type safety, supplemented by Tailwind CSS 4.2.2 and Sass for modern styling capabilities.

The architecture employs a **monorepo structure** using `packages/` (shared, web, mobile) to separate platform-specific logic while maintaining a unified component library and business logic layer, with Metro handling React Native bundling and Vite orchestrating the web build pipeline. Notable features include production-ready HTTP client integration, in-app markdown documentation browser (using Marked 17.0.6), comprehensive build automation scripts (asset management, CI/CD integration with GitHub Pages), ESLint/Prettier code quality enforcement, and PWA-ready capabilities. The project demonstrates enterprise-level practices through organized asset management, dynamic build metadata generation, Dependabot security integration, and extensive TypeScript strict mode configuration, making it suitable for teams building serious cross-platform applications rather than proof-of-concept projects.

With **50 total dependencies** (tech stack currency: 50/100), active recent development (28 commits in 90 days, accelerating activity), comprehensive documentation, and a live demo, this starter template serves as both a functional boilerplate and a reference implementation for cross-platform development patterns using modern JavaScript tooling.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 50 total (50 current, 0 outdated)

**Created**: 2025-07-26
**Last Modified**: 2026-05-11

---

### #17. [DataSpark](https://github.com/markhazleton/DataSpark)

Stars: 0 | Forks: 0 | Language: HTML | 14 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 2089 KB | 🚀 4.7 commits/month

**Quality**: ❌ License | ✅ Docs

# DataSpark Technical Summary

**DataSpark** is a comprehensive .NET 10 toolkit designed for SQLite database analysis and transformation, offering both CLI and ASP.NET Core MVC web interfaces for discovering database files, exporting tables to CSV, inspecting database schemas, and automatically generating C# Data Transfer Objects (DTOs) from database structures. The project demonstrates a well-architected multi-project solution with clear separation of concerns—a `DataSpark.Core` library containing shared business logic, a `DataSpark.Console` CLI application, a `DataSpark.Web` ASP.NET Core frontend with optional Node.js asset pipeline, comprehensive MSTest unit and integration tests, and BenchmarkDotNet performance benchmarks, all built on .NET 10 with modern CI/CD via GitHub Actions and code coverage reporting. Key capabilities include recursive SQLite file discovery, flexible table filtering and CSV export, schema documentation in multiple formats (text, JSON, Markdown), and automated DTO generation with configurable namespaces—enabling developers to quickly reverse-engineer database structures into strongly-typed C# models. The solution emphasizes code quality through persistent coverage badges, active maintenance (14 commits in 90 days), and a live deployment at `data.makeboldspark.com` that allows users to upload SQLite files and perform analysis directly through the web UI. This toolkit is particularly valuable for developers working with SQLite databases who need rapid schema introspection, data export capabilities, and automated code generation workflows, serving both as a practical utility and a reference implementation of modern .NET architecture patterns.

**Created**: 2017-11-06
**Last Modified**: 2026-05-12

---

### #18. [PromptSpark.Chat](https://github.com/markhazleton/PromptSpark.Chat)

Stars: 0 | Forks: 0 | Language: C# | 20 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 19453 KB | 🚀 6.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: PromptSpark.Chat

**PromptSpark.Chat** is a real-time conversational workflow application that enables guided, multi-step user interactions through an intelligent chat interface, with optional AI integration for handling questions outside the defined workflow scope. The application leverages **ASP.NET Core** with **SignalR** for bidirectional real-time communication, **Adaptive Cards** for rendering interactive UI elements, and a thread-safe **ConcurrentDictionary** for in-memory conversation state management, allowing users to maintain progress across page refreshes without server-side persistence overhead.

Key features include dynamic workflow orchestration through JSON-defined node graphs with branching logic, interactive form inputs and button-driven navigation, server-side conversation storage for continuity, and seamless optional AI chat completion integration for open-ended queries. The architecture demonstrates clean separation of concerns with dedicated Controllers, Services, and Models layers, supporting both structured workflows and flexible AI-driven responses through an abstracted **IChatCompletionService** interface.

The technology stack comprises **C# (31.4%)**, **SCSS (29.9%)**, and **HTML (28.5%)** with JavaScript for client-side interactivity, representing a modern full-stack .NET web application with responsive design considerations. The project exemplifies a pragmatic approach to workflow automation, combining event-driven real-time communication patterns with state machine-like node traversal, making it suitable for customer onboarding, guided interviews, multi-step forms, and conversational process automation scenarios where both structured and flexible interactions are needed.

**Created**: 2024-12-31
**Last Modified**: 2026-05-11

---

### #19. [PHPDocSpark](https://github.com/markhazleton/PHPDocSpark)

Stars: 0 | Forks: 0 | Language: PHP | 9 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 3049 KB | 🚀 3.0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: PHPDocSpark

**PHPDocSpark** is an open-source documentation and data exploration platform that demonstrates modern PHP web development practices by combining traditional server-side PHP (8.2+) with a contemporary client-side build toolchain powered by Vite 7.1+. The platform serves as a comprehensive reference implementation featuring markdown-based documentation management with full-text search capabilities, interactive data visualization using Chart.js and DataTables, SQLite database integration for contact management, and API integration examples (GitHub, JokeAPI) with caching strategies—all presented through a responsive Bootstrap 5.3 UI with SCSS preprocessing.

The architecture employs a hybrid pattern using a PHP front controller for server-side routing and logic, paired with an optimized asset pipeline that handles CSS/JavaScript compilation, minification, and hot module replacement during development. Key technical capabilities include recursive directory scanning for dynamic navigation, CSV data analysis with automatic field statistics, CRUD operations for database management, and a performance-optimized content delivery layer. The project is deployed via Azure Pipelines to Azure Web Apps and includes comprehensive tooling with ESLint and Prettier for code quality.

PHPDocSpark is uniquely positioned as both a production-ready application and an educational reference for full-stack developers seeking to understand how to build scalable modern PHP applications with clean separation of concerns, containerized deployment workflows, and professional build system integration. It targets PHP developers exploring contemporary development workflows, full-stack engineers interested in hybrid architectures, and technical teams seeking reference implementations for internal documentation and data exploration tools—making it valuable for learning modern development practices while serving as a practical demonstration platform within the Make Bold Spark portfolio.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2023-09-08
**Last Modified**: 2026-05-12

---

### #20. [AsyncSpark](https://github.com/markhazleton/AsyncSpark)

Stars: 0 | Forks: 0 | Language: C# | 1 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 1950 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# AsyncSpark Technical Summary

AsyncSpark is a production-ready reference implementation demonstrating enterprise-grade async/await patterns in .NET 10, built by Mark Hazleton as part of the Make Bold Spark portfolio of technical demonstrations. The project showcases best practices including ConfigureAwait(false) in library code, proper CancellationToken threading, Task.WhenAll for parallel execution, SemaphoreSlim throttling, Polly resilience policies, and decorator patterns for cross-cutting concerns—with comprehensive unit tests (MSTest + Moq) enforcing 80% code coverage via CI/CD. The codebase is structured around constitution-driven development, a formalized approach that codifies coding standards and architectural principles into a living document with automated compliance auditing through GitHub Actions workflows, SpecKit agents, and compliance reports that validate against the constitution's five core principles (Modern .NET Standards, Async/Await Best Practices, Testing Standards, Dependency Injection & Architecture, and Resilience/Documentation/Logging).

Key features include an ASP.NET Core web application with interactive Scalar-powered API documentation, a weather service demonstrating external API integration patterns, console application demos, and multiple async pattern controllers exposing endpoints for cancellation patterns, concurrency patterns, remote operations, and weather integration. The technology stack leverages modern C# features (nullable reference types, implicit usings, file-scoped namespaces, primary constructors), dependency injection, clean architecture principles, and enforces async best practices through .editorconfig rules that treat async violations as build errors. AsyncSpark is particularly noteworthy for its dual purpose as both a working production application (live at web.makeboldspark.com/asyncspark) and a comprehensive educational resource with linked code examples and structured learning objectives, making it ideal for architects, senior developers, and technical teams seeking to adopt constitution-driven development practices and establish enterprise-grade async/await patterns in their .NET organizations.

**Created**: 2022-08-07
**Last Modified**: 2026-05-11

---

### #21. [WebSpark.Bootswatch](https://github.com/markhazleton/WebSpark.Bootswatch)

Stars: 0 | Forks: 0 | Language: HTML | 1 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7144 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

# WebSpark.Bootswatch - Technical Summary

**WebSpark.Bootswatch** is a .NET 10-exclusive Razor Class Library that provides seamless integration of Bootswatch themes into ASP.NET Core applications, enabling developers to implement modern, responsive Bootstrap 5-based theming with dynamic switching capabilities. The library leverages C# (28.6%), HTML (63.8%), and JavaScript (2.6%) to deliver a comprehensive feature set including light/dark mode support, built-in caching mechanisms via the `StyleCache` service, Tag Helper integration for UI components, and automatic fallback mechanisms for production resilience. Built on a clean architectural foundation with extension methods for dependency injection and optimized for .NET 10's latest framework features and security patches, it demonstrates a deliberate shift away from multi-framework support to prioritize modern dependencies and maintenance simplicity. The project targets ASP.NET Core developers who need rapid theme implementation without sacrificing performance or security, offering a live demonstration site and comprehensive NuGet distribution (with migration guidance for existing users on .NET 8/9). Key design decisions include requiring .NET 10 exclusively as of v2.0 to align with LTS/STS lifecycle considerations and avoiding legacy framework support burden, while maintaining full backward API compatibility for existing codebase migrations. The repository represents a mature, production-ready solution positioned within the Make Bold Spark portfolio, complete with CI/CD integration, detailed documentation, and strategic versioning that reflects real-world enterprise ASP.NET Core development practices.

**Created**: 2022-08-24
**Last Modified**: 2026-05-11

---

### #22. [DocSpecSpark](https://github.com/markhazleton/DocSpecSpark)

Stars: 0 | Forks: 0 | Language: Python | 12 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 223 KB | 🚀 4.0 commits/month

**Quality**: ❌ License | ✅ Docs

# DocSpecSpark Technical Summary

DocSpecSpark is an AI-assisted documentation generation and management tool that provides AI coding assistants (GitHub Copilot, Claude, Cursor, etc.) with a structured, repeatable workflow for creating, reviewing, and publishing documentation systems through markdown-based prompts and lightweight CLI automation. The project implements a separation-of-concerns architecture with two distinct directory structures: `.docspark/` containing framework-managed stock assets and `.documentation/` for user-owned artifacts, enabling clean upgrade paths and customization via a hierarchical prompt/script resolution system across 21 workflow commands (ranging from core specification and planning to constitution-powered reviews, quality assurance, and publication scaffolding). Built in Python using minimal dependencies (Rich for CLI styling and Typer for command-line interfaces), the tool offers dual access paths: direct AI agent integration through quickstart markdown prompts for immediate use, or CLI-based installation via the optional `docspark-cli` for automated bootstrapping into target repositories. The architecture uniquely bridges the gap between AI-native workflows (markdown prompts as primary artifacts) and traditional software tooling, treating the prompt set and template collection as the actual product rather than positioning the CLI as the focus, making it particularly suited for documentation-driven projects, technical specification work, and AI-augmented documentation governance. The project demonstrates active development with accelerating commit patterns and serves as a reference implementation demonstrating how modern AI coding assistants can be systematically guided through complex documentation governance and publication processes using lightweight, version-controllable configuration.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 2 total (0 current, 2 outdated)

**Created**: 2026-03-07
**Last Modified**: 2026-05-11

---

### #23. [WebSpark.PrismSpark](https://github.com/markhazleton/WebSpark.PrismSpark)

Stars: 0 | Forks: 0 | Language: C# | 2 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 2280 KB | 🚀 0.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.PrismSpark

**PrismSpark** is a modern C#/.NET 10.0 port of the popular PrismJS syntax highlighting library, providing high-performance code tokenization, highlighting, and rendering for ASP.NET Core and .NET applications. The project delivers enterprise-grade syntax highlighting for 24 programming languages (C#, JavaScript, Python, Rust, Go, SQL, Markdown, and others) with support for advanced features including customizable theming, a plugin architecture (line numbers, copy-to-clipboard, toolbars), event-driven hooks, and async/caching APIs for optimal performance. Built using C# (72.9% of codebase) with supporting HTML, PowerShell, and JavaScript components, the architecture follows plugin and theme manager patterns with extensible grammar systems, a comprehensive MSTest suite (52 tests), and integrates seamlessly into ASP.NET MVC controllers and Razor views through dependency injection. The project distinguishes itself through native .NET implementation of a JavaScript library, eliminating JavaScript runtime dependencies while providing typed, performant alternatives; it includes interactive demo pages (live code editor, Markdown/PUG previews), CSS generation capabilities, and context-aware metadata support for specialized rendering scenarios. Designed for .NET web developers, solutions architects, and teams requiring embedded syntax highlighting without external JavaScript libraries, PrismSpark is particularly valuable for documentation platforms, code review tools, educational applications, and developer-focused web applications that need production-grade highlighting with full customization control.

**Created**: 2025-05-27
**Last Modified**: 2026-05-12

---

### #24. [WebSpark.ArtSpark](https://github.com/markhazleton/WebSpark.ArtSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3894 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.ArtSpark

**WebSpark.ArtSpark** is a comprehensive .NET 10.0 solution that provides complete programmatic access to the Art Institute of Chicago's public API through a fully-typed C# client library, coupled with an innovative AI-powered chat system featuring multiple personas (Artwork, Artist, Curator, Historian) enabled by OpenAI's GPT-4 Vision and Semantic Kernel. The solution encompasses four interconnected projects: a production-grade `ArtInstituteClient` library implementing all 33 API endpoints across 6 categories with support for IIIF image construction, Elasticsearch full-text search, and flexible pagination; an `ArtSparkAgent` system leveraging externalized markdown-based prompts with hot-reload capabilities for conversational AI interactions; an ASP.NET Core MVC demo web application featuring user authentication, personal collections, and responsive Bootstrap 5 UI; and a console utility for developer testing. The architecture demonstrates modern .NET best practices including async/await patterns, `System.Text.Json` deserialization with proper naming policies, dependency injection, and minimal external dependencies, while the AI layer incorporates conversation memory, visual analysis, and content filtering for educational contexts. This project serves as both a practical tool for interacting with the Art Institute's collections and a technical portfolio demonstration showcasing enterprise-grade .NET development, though it appears inactive (no commits in 365 days) and unmaintained despite its sophisticated feature set.

**Created**: 2023-01-30
**Last Modified**: 2026-05-13

---

### #25. [TeachSpark](https://github.com/markhazleton/TeachSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 29994 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# TeachSpark - Technical Summary

**TeachSpark** is an LLM-powered educational platform built with .NET 10 MVC and a modern webpack-based frontend that delivers personalized, adaptive learning experiences through AI-driven content delivery. The project demonstrates a full-stack integration of Large Language Models into a responsive web application, featuring intelligent curriculum adaptation, real-time feedback, progress analytics, and customized learning pathways tailored to individual student patterns. The architecture follows Clean Architecture principles with a C# backend (Entity Framework Core), a frontend stack leveraging webpack 5 with ES6+/Babel, SCSS styling, and comprehensive code quality tooling (ESLint, Prettier, Stylelint, Husky pre-commit hooks). The tech stack is relatively current (76/100 currency score) with .NET 10, Node.js 18+, and modern JavaScript tooling, supported by automated build optimization including hot module replacement, code splitting, and bundle analysis for performance monitoring. This is a production-ready reference implementation created by Mark Hazleton (Technical Solutions Architect) as part of the MakeBoldSpark portfolio, designed to showcase best practices in integrating AI capabilities into educational web applications with enterprise-grade development practices. However, the repository shows signs of staleness with zero recent activity over 90 days and zero community engagement (no forks, contributors, or commits), suggesting this may be a completed demonstration project rather than an actively maintained product.

**Technology Stack Currency**: ✅ 76/100
**Dependencies**: 3 total (2 current, 1 outdated)

**Created**: 2025-06-19
**Last Modified**: 2026-05-13

---

### #26. [MechanicsOfMotherhood](https://github.com/markhazleton/MechanicsOfMotherhood)

Stars: 0 | Forks: 0 | Language: TypeScript | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7598 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Mechanics of Motherhood

**Mechanics of Motherhood** is a production-ready recipe management web application built with React 19 and TypeScript, designed specifically for busy working mothers seeking organized meal planning. The platform features 108+ curated recipes integrated from live APIs (RecipeSpark and WebCMS), with intelligent categorization across 14 recipe types, advanced search and filtering capabilities, nutritional information, and print-friendly recipe cards. The architecture leverages modern web technologies including Vite for fast builds, TanStack React Query for server state management, Tailwind CSS with Shadcn/ui components for responsive design, and Wouter for lightweight client-side routing—all deployed via GitHub Pages with GitHub Actions CI/CD automation and hosted on a custom domain with SSL certificates. The application demonstrates production-grade engineering practices including automated data quality validation, PWA-ready offline support, 95+ Lighthouse performance scores, comprehensive SEO optimization with sitemaps and structured data, and mobile-first responsive design optimized for 3G networks. The codebase is structured as a TypeScript-dominant SPA (53% TypeScript, 25.8% JavaScript) with build automation scripts, comprehensive development commands, and fallback mock data to ensure graceful degradation—serving as both a functional recipe platform and a technical portfolio piece showcasing enterprise-ready React and modern DevOps practices.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 42 total (42 current, 0 outdated)

**Created**: 2025-09-01
**Last Modified**: 2026-05-12

---

### #27. [Texecon](https://github.com/markhazleton/Texecon)

Stars: 0 | Forks: 0 | Language: TypeScript | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3811 KB | 🚀 0 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: Texecon

**Texecon** is a static React-based web application delivering expert economic analysis and commentary on the Texas economy, hosted at texecon.com and deployed via GitHub Pages. The project implements a modern JAMstack architecture with build-time content management, combining React 19, TypeScript, Vite 7.1, and Tailwind CSS to create a performance-optimized, SEO-friendly static site that fetches fresh content from a WebSpark headless CMS API during the build process with intelligent fallback caching. Key technical features include automated sitemap generation, progressive enhancement with client-side routing, structured data implementation, cache-busting strategies, and a comprehensive build pipeline that orchestrates content fetching, type generation, Vite compilation, and static HTML page generation for dynamic routes. The architecture emphasizes accessibility through Radix UI primitives and shadcn/ui components, lightweight routing via Wohor, and demonstrates advanced static site generation patterns that bridge the gap between dynamic content management and static site performance. Though currently in a stale state (no commits in 90+ days), the repository exemplifies a sophisticated approach to building content-rich, SEO-optimized web applications for domain-specific expertise delivery, making it particularly valuable as a technical demonstration and portfolio piece for architects and developers seeking to implement modern full-stack JavaScript workflows with zero-latency, pre-rendered content delivery.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 37 total (37 current, 0 outdated)

**Created**: 2025-09-03
**Last Modified**: 2026-05-13

---

### #28. [github-stats-spark](https://github.com/markhazleton/github-stats-spark)

Stars: 0 | Forks: 0 | Language: Python | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 20249 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: github-stats-spark

## Project Overview

**Stats Spark** is a comprehensive GitHub analytics platform that generates automated profile statistics, AI-powered repository analysis, and an interactive mobile-first dashboard. It transforms raw GitHub data into actionable insights through SVG visualizations, intelligent repository ranking algorithms, and Claude AI-powered technical summaries.

## Core Architecture

### Technology Stack
- **Backend**: Python 3.11+ with PyGithub for GitHub API integration
- **Data Processing**: PyYAML (configuration), beautifulsoup4 (HTML parsing), requests (HTTP)
- **Visualization**: svgwrite (SVG generation), Chart.js with react-chartjs-2 (interactive charts)
- **Frontend**: JavaScript, HTML, CSS with mobile-first responsive design
- **Build/Automation**: PowerShell scripts, GitHub Actions workflows
- **Data Persistence**: IndexedDB (via Dexie) for offline-first caching

## Key Features & Components

### 1. **SVG Profile Statistics Generator**
- **6 visualization categories**: Overview, heatmap, languages, streaks, fun stats, release cadence
- **Spark Score Algorithm**: 0-100 metric (40% consistency, 35% volume, 25% collaboration)
- **Automated Updates**: GitHub Actions triggers weekly at midnight UTC on Sundays
- **Theme Support**: Dark, light, custom themes with WCAG AA accessibility compliance
- **Activity Pattern Detection**: Identifies coding time personalities (night owl, early bird, daytime coder)

### 2. **AI-Powered Repository Analysis**
- **Intelligent Ranking Algorithm**: 
  - 30% Popularity (stars/forks)
  - 45% Activity (recent commits with time-decay across 90d/180d/365d windows)
  - 25% Health (documentation, licensing, maintenance signals)
- **Claude Haiku Integration**: 97%+ success rate for generating 4-6 sentence technical summaries
- **Attention Scoring**: Combines PR backlog, security findings, staleness, and dependency health
- **Performance**: Processes up to 500 repositories in <5 minutes with smart caching

### 3. **Interactive Mobile-First Dashboard**
- **UI/UX Design**:
  - Touch-optimized (44x44px minimum touch targets)
  - Bottom sheet navigation for filters and controls
  - Swipe gesture support for navigation and deletion
  - Responsive across 320px-768px viewports
- **Data Visualization**: Chart.js with touch-optimized tooltips
- **Features**:
  - "Needs Attention" ranking view
  - Drill-down repository details with commit history
  - Rendered markdown summaries
  - CSV/JSON export functionality
- **Performance Optimization**: 
  - Lighthouse CI targeting <2s First Contentful Paint
  - 0.9+ performance score
  - IndexedDB caching with Dexie (7-day retention)
- **Accessibility**: WCAG 2.1 AA compliant with screen reader support and keyboard navigation
- **Deployment**: GitHub Pages with automatic updates

## Data Flow Architecture

```
GitHub API → PyGithub Collector
    ↓
YAML Config & Rate Limit Handler (exponential backoff)
    ↓
Analysis Engine:
  - Repository Ranking (algorithm)
  - AI Summarization (Claude Haiku)
  - Dependency Analysis
  - Contribution Pattern Detection
    ↓
Output Generation:
  - SVG Visualizations (svgwrite)
  - Markdown Reports
  - JSON/CSV Data
    ↓
Dashboard Frontend:
  - React Components
  - Chart.js Visualizations
  - IndexedDB Cache
    ↓
GitHub Pages Deployment
```

## Configuration & Customization

- **YAML-based configuration** for all analytics parameters
- **Local CLI** for testing and development
- **Extensible modular architecture** for custom integrations
- **Smart caching system** for API optimization

## Quality Metrics

| Metric | Value |
|--------|-------|
| Tech Stack Currency | 82/100 |
| Code Size | 20.2 MB |
| Dependencies | 11 (well-managed) |
| AI Success Rate | 97%+ |
| Target Python Version | 3.11+ |
| Accessibility Standard | WCAG 2.1 AA |
| Performance Target | <2s FCP, 0.9+ Lighthouse |

## Project Status & Observations

⚠️ **Status Concerns**:
- **Stale Activity**: 0 commits in last 90-365 days
- **No Community Engagement**: 0 stars, 0 forks, 0 contributors
- **Creation Date Anomaly**: Listed as 2025-12-28 (future date - likely metadata error)

## Notable Technical Achievements

1. **Composite Ranking Algorithm**: Multi-weighted scoring balances popularity, activity, and health
2. **AI Integration**: Claude API integration with fallback error handling and 97%+ success
3. **Offline-First**: IndexedDB strategy enables progressive enhancement
4. **Accessibility Focus**: WCAG 2.1 AA compliance from ground up
5. **Touch-Optimized UX**: Mobile-first approach with native interaction patterns
6. **Smart Caching**: Reduces API calls while maintaining fresh data

## Use Cases

- 👨‍💻 Developer portfolio showcase
- 📊 Team repository health monitoring
- 🎯 Engineering leadership dashboards
- 🚀 Open-source maintainer engagement tracking

## Deployment Model

Self-hosted with GitHub Pages + GitHub Actions automation. Fully functional without external dependencies beyond GitHub API tokens.

**Technology Stack Currency**: ✅ 82/100
**Dependencies**: 11 total (6 current, 5 outdated)

**Created**: 2025-12-28
**Last Modified**: 2026-05-13

---

### #29. [markhazleton.github.io](https://github.com/markhazleton/markhazleton.github.io)

Stars: 0 | Forks: 0 | Language: SCSS | 7 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 161 KB | 🚀 2.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: markhazleton.github.io

This repository is Mark Hazleton's personal Jekyll-based static site hosted on GitHub Pages, designed to serve as a professional portfolio and blog platform. The project leverages Jekyll 3.10.0 with Ruby 3.2.2 and a customized Minima theme to deliver a responsive, feature-rich website without external frontend frameworks. Key features include dark/light mode toggle functionality, emoji support, comprehensive post management with front matter templating, and automated CI/CD deployment via GitHub Actions. The codebase employs a modern SCSS/CSS architecture (69.2% combined styling) alongside structured HTML templates, organized into reusable components through Jekyll's `_includes` and `_layouts` conventions, enabling maintainable content separation and consistent design patterns across pages. The project demonstrates a well-documented development workflow supporting both direct commits and feature branch workflows, with local development tooling optimized for Windows, macOS, and Linux environments through the Bundler dependency manager. This architecture makes it an ideal reference implementation for developers seeking to build SEO-optimized, low-maintenance personal sites on GitHub Pages with minimal external dependencies while maintaining professional content management practices.

**Technology Stack Currency**: ✅ 56/100
**Dependencies**: 3 total (2 current, 1 outdated)

**Created**: 2021-04-18
**Last Modified**: 2026-04-01

---

### #30. [ApiSpark](https://github.com/markhazleton/ApiSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 1636 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: ApiSpark

**ApiSpark** is a modular ASP.NET Core backend API platform designed to consolidate multiple low-volume APIs into a single, cost-effective Azure-hosted service. Built by Mark Hazleton as part of his MakeBoldSpark portfolio, it demonstrates how to serve static-first websites and Single Page Applications with a centralized API layer while maintaining simplicity and affordability. The platform leverages **ASP.NET Core (.NET 10 LTS)**, **Entity Framework Core**, and **SQLite** as the primary data store, with optional **Azure Cosmos DB** integration for document-oriented use cases, all deployed on Azure App Service Linux and supported by Azure Static Web Apps for client-facing applications.

The architecture employs a **route-based segmentation pattern** organizing endpoints into distinct areas (`/api/public/*`, `/api/admin/*`, `/api/publish/*`, `/api/integrations/*`) with corresponding authentication and authorization controls, enabling granular access management for anonymous read-only content, authenticated administration, publishing workflows, and external integrations. The project emphasizes **portable, low-cost hosting** using SQLite with persistent App Service storage, eschewing expensive managed databases for typical use cases while retaining flexibility for specialized workloads. ApiSpark is particularly noteworthy as a reference implementation for developers seeking to optimize hosting costs by consolidating multiple small APIs into a single application rather than deploying microservices, making it ideal for portfolios, technical demonstrations, and small-to-medium organizations with diverse but low-traffic API needs. The codebase includes comprehensive documentation including Architecture Decision Records and a project constitution, positioning it as both a functional service and an educational reference for .NET architectural patterns.

**Created**: 2026-05-07
**Last Modified**: 2026-05-13

---


---

## Report Metadata

- **Generation Time**: 6.3 seconds
- **SVGs Generated**: 6/6
- **Total API Calls**: 0
- **Total AI Tokens**: 75,846
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
*Last updated: 2026-05-13*

## Screenshot Audit

- Repositories with websites: 21
- Screenshots present: 20
- Flagged repositories: 1

### Missing Screenshots

- PHPDocSpark: https://phpdocspark.azurewebsites.net
