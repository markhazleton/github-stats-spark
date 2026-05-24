# GitHub Profile: markhazleton

**Generated**: 2026-05-24 00:45:48 UTC
**Report Version**: 1.0.0
**Repositories Analyzed**: 30
**AI Summary Rate**: 96.7%

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

### #1. [UISampleSpark](https://github.com/markhazleton/UISampleSpark)

Stars: 8 | Forks: 4 | Language: HTML | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 31228 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# UISampleSpark - Technical Summary

**UISampleSpark** is an educational reference application built on .NET 10 (ASP.NET Core) that demonstrates how to implement identical Employee/Department CRUD functionality across seven distinct front-end UI patterns—MVC, Razor Pages, jQuery AJAX, React, Vue, htmx, and Blazor Server—within a single cohesive application. The project showcases modern web architecture practices including REST APIs with Swagger/OpenAPI documentation, dependency injection, repository/service patterns, Entity Framework Core with in-memory databases, and comprehensive unit testing across domain and data layers. The technology stack leverages Bootstrap 5 with dynamic Bootswatch theming, React 18 via CDN with Babel transpilation, Vue 3 Composition API, and includes advanced features such as PivotTable.js reporting, real-time SignalR communication via Blazor, and health check endpoints with Application Insights telemetry integration. Its architecture emphasizes clean separation of concerns through layered projects (UI, Core/Domain, Data/EF, and Tests), API key-based security, and full DevOps/CI-CD integration via GitHub Actions and Docker containerization for seamless Azure deployment. The project's primary value lies in its comparative analysis capability—developers can study how different frameworks solve the same domain problem, making it an invaluable learning resource for teams evaluating UI technology choices or modernizing legacy applications. Target audiences include ASP.NET Core developers, enterprise architects, and teams planning digital transformation initiatives who need practical examples of scalable, multi-pattern UI implementations in production-ready code.

**Created**: 2019-04-25
**Last Modified**: 2026-05-16

---

### #2. [WebProjectMechanics](https://github.com/markhazleton/WebProjectMechanics)

Stars: 3 | Forks: 0 | Language: Visual Basic .NET | 11 commits (90d)

👥 0 contributors | 🌐 11 languages | 💾 52587 KB | 🚀 3.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebProjectMechanics

**WebProjectMechanics** is a greenfield rebuild of a legacy multi-tenant content management system designed to serve 36+ independent websites from a single application instance while maintaining physical data isolation and minimal infrastructure costs (~$10/month). The system architecture employs a plugin-based domain model with domain-specific content types (CMS pages, mineral collections, recipes), per-site SQLite databases for tenant isolation, and a publish-to-static workflow that pre-renders all public content as HTML served by Caddy, eliminating database queries in the critical path. Built on ASP.NET Core 9 with EF Core 9, the project leverages modern .NET patterns including Minimal APIs, dependency injection, and xUnit testing while using Scriban for templating and GitHub Actions for CI/CD on Ubuntu 24.04. The codebase is structured around separation of concerns with shared contracts (WPM.Core), infrastructure services, a minimal API host, and isolated domain projects, complemented by comprehensive documentation of both the legacy system it's replacing and the phased implementation plan. This approach is particularly noteworthy for its cost-efficiency, data isolation without tenant IDs, and the pragmatic decision to maintain a read-only archive of the 20+ year legacy system, making it an excellent case study in migrating complex enterprise applications to modern cloud-native architectures while preserving operational continuity.

**Created**: 2017-09-19
**Last Modified**: 2026-05-14

---

### #3. [FastEndpointApi](https://github.com/markhazleton/FastEndpointApi)

Stars: 3 | Forks: 1 | Language: HTML | 0 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 156 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: FastEndpointApi Repository

**FastEndpointsSpark** is a comprehensive demonstration project showcasing the FastEndpoints framework for ASP.NET Core, implementing a fully functional Person Management API that exemplifies the REPR (Request-Endpoint-Response) pattern and modern API best practices. The project leverages .NET 10.0, FastEndpoints 7.1.1, and FastEndpoints.Swagger to provide a production-ready example of building clean, maintainable REST APIs with minimal boilerplate code, featuring complete CRUD operations, HATEOAS hypermedia links, dependency injection, smart request/response mapping, and interactive Swagger/OpenAPI documentation. The architecture demonstrates proper separation of concerns through a service layer abstraction, in-memory data persistence, and reusable endpoint base classes, while utilizing auxiliary technologies including Bogus for test data generation, Bootstrap for frontend UI, and GitHub Actions with Azure Web Apps for CI/CD deployment. The codebase is organized across HTML (60.4%), C# (38.4%), and JavaScript (1.2%), providing both backend API implementation and static HTML sample pages (index.html, docs.html, test.html) that serve as an educational platform for developers. This project is particularly valuable for developers looking to understand modern ASP.NET Core API patterns, migrate from MVC Controllers or Minimal APIs, and implement enterprise-level architectural practices in a learning-friendly environment, with accompanying documentation, live deployment at fastendpoints.makeboldspark.com, and an associated detailed article explaining the implementation methodology. Though currently in a stale state (no commits in 365+ days), it remains a well-documented, production-quality reference implementation suitable for educational purposes and architectural guidance.

**Created**: 2024-04-06
**Last Modified**: 2026-05-15

---

### #4. [RequestSpark](https://github.com/markhazleton/RequestSpark)

Stars: 2 | Forks: 1 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 966 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# RequestSpark - Technical Summary

RequestSpark is a comprehensive .NET 10 (LTS) web application and console tool designed for REST API testing, performance benchmarking, and regression testing using Postman collections as the primary input format. The project provides both a Razor Pages-based web interface and a console application that enable users to import Postman collection definitions, execute automated API test suites, perform load testing, analyze response time metrics, and export detailed results to CSV with statistical analysis including percentiles and success rates. The architecture comprises multiple layers including a core Domain project (RequestSpark.Domain) handling business logic, a PostmanImport project for collection parsing, a Web project built on ASP.NET Core, and comprehensive test coverage through MSTest v4, demonstrating solid separation of concerns and testability patterns. The technology stack includes modern .NET 10 components with optimized dependencies (93% at latest versions), security-hardened with zero vulnerabilities, and delivers measurable performance improvements—19% faster builds and 25% faster test execution compared to its .NET 9 predecessor. RequestSpark is positioned as a technical demonstration within the Make Bold Spark portfolio and serves developers, QA engineers, and solutions architects who need to validate API reliability and performance without licensing commercial tools like Postman Cloud. The project's stale status (no commits in 90+ days) and minimal community engagement (2 stars, 1 fork) suggest it remains a proof-of-concept or internal tool rather than an actively maintained open-source project, though the live instance at request.makeboldspark.com indicates ongoing deployment and demonstration purposes.

**Created**: 2021-09-30
**Last Modified**: 2026-05-11

---

### #5. [KeyPressCounter](https://github.com/markhazleton/KeyPressCounter)

Stars: 2 | Forks: 1 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 2 languages | 💾 46631 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# KeyPressCounter - Technical Summary

## Overview
KeyPressCounter is a lightweight Windows system tray utility designed to monitor keyboard and mouse input activity alongside real-time system performance metrics, providing users with comprehensive statistics about their computer usage patterns without recording sensitive data or transmitting information externally. The application runs silently in the background as a single-instance Windows Forms application with a rich dashboard interface for viewing aggregated statistics.

## Key Features & Capabilities
The application combines input monitoring (keystroke and mouse click tracking with peak activity metrics and idle period detection) with comprehensive system performance monitoring, including real-time CPU/memory gauges, disk I/O metrics, network speeds, and a top-10 process monitor. Users benefit from a three-tab statistics dashboard featuring input statistics, system performance graphs (60-second rolling line charts with GDI+ rendering), hardware information via WMI, persistent configuration management, automatic daily summary logging, and quick-launch access to Windows system utilities—all exposed through an intuitive system tray context menu with single-click access to activity logs.

## Technology Stack & Architecture
Built on **.NET 10.0** with **C# 13**, the project leverages **SharpHook** (7.1.1) for global keyboard/mouse event hooking on background threads, **System.Management** for WMI-based hardware enumeration, native Windows Performance Counters for CPU/memory/disk/network metrics, and **User32 P/Invoke** (`GetLastInputInfo`) for idle detection. The architecture follows a modular design pattern with clear separation of concerns: `CustomApplicationContext` manages the tray icon and event lifecycle, `Counter` provides thread-safe increment operations with peak tracking, `SystemPerformanceMonitor` abstracts performance counter management, and `StatsForm` implements the UI dashboard with 1-second refresh intervals.

## Notable Design Patterns & Implementation
The codebase demonstrates strong Windows desktop development practices including thread-safe counter operations with lock-based synchronization, persistent JSON-based configuration stored in `%APPDATA%`, automatic Windows startup registry integration, and comprehensive logging with timestamped activity logs and daily summaries written to the Documents folder. The application enforces single-instance behavior at startup and implements graceful exception handling with global exception handlers to prevent silent failures.

## Unique Aspects & Target Users
KeyPressCounter distinguishes itself through privacy-first design—it counts input events without capturing key identities or recording what users type, making it suitable for productivity tracking, workstation monitoring, or activity analytics in professional environments where privacy compliance is critical. The project targets productivity-conscious users, system administrators tracking workstation utilization, and organizations needing lightweight activity baselines without intrusive keystroke logging.

## Current Project Status
The repository shows signs of maturity but inactivity: zero commits in 365 days, no recent activity, and a tech stack currency score of 57/100, indicating the project may require updates to remain compatible with current .NET versions and security best practices, though the core functionality remains sound for Windows 10+ environments.

**Technology Stack Currency**: ✅ 57/100
**Dependencies**: 4 total (3 current, 1 outdated)

**Created**: 2024-03-07
**Last Modified**: 2026-05-12

---

### #6. [WebSpark](https://github.com/markhazleton/WebSpark)

Stars: 1 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 8 languages | 💾 69609 KB | 🚀 0 commits/month

**Quality**: ❌ License | ❌ Docs

# WebSpark Technical Summary

WebSpark is a comprehensive .NET 9 ASP.NET Core MVC suite consisting of seven modular applications (PromptSpark, RecipeSpark, TriviaSpark, WebCMS, AsyncSpark, Admin, and Identity) designed to demonstrate modern enterprise web architecture with AI integration via Semantic Kernel and OpenAI APIs. The project emphasizes scalability, maintainability, and real-time communication through SignalR, Bootstrap 5 UI framework, and advanced SEO optimization features including dynamic metadata, JSON-LD structured data, XML sitemaps, Google Analytics 4 integration, and Core Web Vitals monitoring. A standout feature is its **spec-driven development workflow** powered by SpecKit commands (`/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.critic`, `/speckit.implement`, `/speckit.review`) that enforce rigorous feature specifications, implementation planning, adversarial risk assessment, and automated showstopper detection before code execution—catching ASP.NET Core anti-patterns, security vulnerabilities, performance issues, and operational readiness gaps before they reach production. The repository serves as a reference architecture for enterprise developers and is maintained by Mark Hazleton as part of the MakeBoldSpark technical portfolio, though the project is currently inactive (no commits in 90+ days) with minimal community engagement. Target users are .NET developers seeking best-practice examples of prompt engineering tools, recipe management systems, content management platforms, and developers wanting to implement spec-driven, risk-aware development workflows in their own projects.

**Created**: 2024-01-11
**Last Modified**: 2026-05-15

---

### #7. [AsyncSpark](https://github.com/markhazleton/AsyncSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2146 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# AsyncSpark - Technical Summary

AsyncSpark is a production-ready reference implementation demonstrating enterprise-grade asynchronous programming patterns in .NET 10, built by Mark Hazleton as part of the Make Bold Spark portfolio. The project serves as an educational and architectural showcase for proper async/await practices, featuring comprehensive implementations of critical patterns including ConfigureAwait(false) in library code, CancellationToken threading, Task.WhenAll parallelization, SemaphoreSlim throttling, Polly resilience policies, and fire-and-forget safety mechanisms—each with accompanying unit tests and live API demonstrations.

The architecture employs clean design principles including dependency injection, decorator pattern for cross-cutting concerns (telemetry, caching, logging), and interface-based abstractions, with an ASP.NET Core web application exposing interactive Scalar-powered API documentation and multiple controller endpoints demonstrating real-world async scenarios such as weather service integration, bulk API calls, and concurrency pattern comparisons. Built with modern .NET conventions (nullable reference types, implicit usings, file-scoped namespaces, primary constructors), the codebase enforces 80% code coverage in CI/CD pipelines and implements "Constitution-Driven Development"—a formalized governance model with automated audits, compliance validation against documented standards, and structured code quality enforcement through GitHub Actions workflows.

The project uniquely combines technical demonstration with governance and learning, featuring a comprehensive constitution document, audit reports, SpecKit development workflows, interactive API documentation with live testing capabilities, and explicit learning objectives linking patterns to specific code implementations, making it valuable for architects, senior developers, and teams seeking to establish async/await best practices and architectural governance frameworks in enterprise .NET applications.

**Created**: 2022-08-07
**Last Modified**: 2026-05-17

---

### #8. [markhazleton](https://github.com/markhazleton/markhazleton)

Stars: 0 | Forks: 0 | Language: Unknown | 0 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 6626 KB | 🚀 0 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary

This repository serves as Mark Hazleton's personal portfolio and learning archive—a curated collection showcasing his expertise as a .NET and Azure engineer specializing in modern web application development and developer tooling. The project functions as a dynamic documentation of his professional journey, featuring multiple interconnected demo applications including WebSpark (comprehensive web application platform), ReactSpark (Vite-based React site hosted on Azure Static Web Applications), TailwindSpark (opinionated UI component library), and UISampleSpark (containerized UI sample application available on Docker Hub).

The technology stack centers on modern full-stack development practices, emphasizing .NET/C# backend capabilities combined with contemporary frontend frameworks (React with Vite), cloud-native deployment on Azure infrastructure, containerization via Docker, and design systems built with Tailwind CSS. The architecture reflects a polished, production-oriented approach with emphasis on developer experience, including CLI tooling (DevSpark) for AI-assisted workflows, comprehensive blogging capabilities, and well-documented learning resources that bridge AI capabilities with practical software engineering.

What distinguishes this portfolio is its dual nature as both a professional showcase and an intentional learning documentation system—each repository represents milestones in continuous skill development rather than disconnected projects. The accompanying blog content demonstrates thought leadership on emerging topics like AI confidence traps, analytics-driven design patterns, and agent-based tooling, making this particularly valuable for engineers seeking to understand modern development practices, cloud deployment patterns, and the intersection of AI with developer productivity tools. The project targets experienced developers and architects interested in .NET ecosystem maturity, Azure best practices, and evolving approaches to developer experience optimization.

**Created**: 2021-04-17
**Last Modified**: 2026-05-20

---

### #9. [WebSpark.Bootswatch](https://github.com/markhazleton/WebSpark.Bootswatch)

Stars: 0 | Forks: 0 | Language: HTML | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7172 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.Bootswatch

**WebSpark.Bootswatch** is a .NET 10.0-targeted Razor Class Library that provides seamless integration of Bootswatch themes (Bootstrap 5-based styling) into ASP.NET Core applications, enabling dynamic theme switching, light/dark mode support, and responsive UI theming without manual CSS management. The library leverages modern .NET extensions, dependency injection, caching mechanisms via the `StyleCache` service, and Tag Helper components (e.g., `<bootswatch-theme-switcher />`) to deliver production-ready theming with minimal configuration—typically requiring only single-line setup through extension methods. Built with a polyglot tech stack (HTML 63.9%, C# 28.5%, PowerShell 4.4%, JavaScript 2.6%), the project demonstrates a deliberate architectural decision to prioritize latest-generation framework support (exclusively .NET 10) over broad backward compatibility, sacrificing support for .NET 8/9 to ensure access to cutting-edge security patches, performance optimizations, and current NuGet package versions. The library targets ASP.NET Core developers who need enterprise-grade theme management with comprehensive error handling, IntelliSense documentation, and a live demonstration site, positioning itself as a reusable, maintainable alternative to manual Bootswatch integration. However, the repository shows signs of stagnation with zero commits in the past 365 days and zero community engagement (0 stars, forks, contributors), suggesting either abandoned development or very limited adoption despite its polished README and versioning strategy.

**Created**: 2022-08-24
**Last Modified**: 2026-05-18

---

### #10. [devspark](https://github.com/markhazleton/devspark)

Stars: 0 | Forks: 1 | Language: Python | 0 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 7145 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# DevSpark Technical Summary

DevSpark is a structured workflow framework designed to augment AI coding assistants (Claude, Copilot, Cursor, Gemini, and 13+ others) with a repeatable development lifecycle—spanning requirements definition through release—entirely through markdown-based slash commands and reusable prompt templates. The core product consists of 28 contextualized command prompts organized into orchestrated workflows (create-spec, execute-plan, suggest-improvement) that guide AI agents through specification, planning, implementation, code review, and release phases without requiring installation or external dependencies.

The architecture employs a dual-surface model separating lifecycle governance (slash-commands that manage branching, artifact routing, and gates) from portable skill definitions (reusable capability instructions compatible with any skills-enabled AI client). DevSpark ships with optional CLI tooling (written in Python with dependencies on Click, Pydantic, PyYAML, and JSON Schema) that enables advanced features like harness runtime execution (declarative workflow specs with structured artifact output), environment validation, and adapter management for multi-agent environments.

The framework is distinguished by its zero-installation quickstart model—users copy markdown files directly into projects and point their AI agent at platform-specific onboarding prompts—while offering optional CLI depth for teams requiring repeatable engineering workflows, constitution-based governance, and structured artifact management. Its design philosophy emphasizes being "not a program, not a subscription," positioning itself as portable prompt and template infrastructure rather than a SaaS platform, making it particularly valuable for teams standardizing AI-assisted development processes across heterogeneous agent toolchains.

**Technology Stack Currency**: ✅ 76/100
**Dependencies**: 5 total (1 current, 4 outdated)

**Created**: 2026-04-02
**Last Modified**: 2026-05-22

---

### #11. [WebSpark.HttpClientUtility](https://github.com/markhazleton/WebSpark.HttpClientUtility)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2796 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# WebSpark.HttpClientUtility - Technical Summary

**WebSpark.HttpClientUtility** is an enterprise-grade HTTP client wrapper library for .NET 8-10 that simplifies distributed HTTP communication by encapsulating complex resilience, caching, and observability patterns into a single-line dependency injection setup (`AddHttpClientUtility()`). The library abstracts away boilerplate configuration for Polly resilience policies (retries, circuit breakers), intelligent in-memory response caching, structured logging with automatic correlation IDs, and OpenTelemetry distributed tracing—eliminating 50+ lines of manual setup code that developers typically write when building production microservices. Core technical features include configurable HTTP request/response handling via the `IHttpRequestResultService` interface, generic response typing support, automatic retry mechanisms with exponential backoff, rate-limit-aware caching strategies, and Source Link debugging support with trimming/AOT compatibility. The architecture leverages the decorator pattern to wrap standard .NET HttpClient functionality while maintaining seamless integration with ASP.NET Core's dependency injection and middleware ecosystems, making it particularly well-suited for microservices, background workers, and web crawling scenarios. The project is delivered as two focused NuGet packages (core utility plus optional Crawler extension for robots.txt parsing and sitemap generation), backed by comprehensive automated testing across .NET versions, zero-warning builds, and strict semantic versioning guarantees ensuring production stability. The accompanying live demo site and extensive documentation position this as both a practical utility library and an educational reference for implementing cloud-native HTTP patterns in modern .NET applications.

**Created**: 2025-05-03
**Last Modified**: 2026-05-18

---

### #12. [TeachSpark](https://github.com/markhazleton/TeachSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 30030 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: TeachSpark

TeachSpark is an AI-powered educational platform built with .NET 10 MVC and C# that demonstrates how Large Language Models can be integrated into modern web applications to deliver personalized, adaptive learning experiences. The project combines a sophisticated backend architecture leveraging Entity Framework Core and Clean Architecture principles with a modern frontend ecosystem featuring Webpack 5, SCSS styling, and ES6+ JavaScript, all unified through automated development tooling including Husky pre-commit hooks and comprehensive linting/formatting standards (ESLint, Prettier, Stylelint). Key features include intelligent content adaptation via LLM technology, interactive curriculum delivery with real-time feedback, personalized learning pathways, comprehensive progress analytics, and a responsive user interface optimized for performance through code splitting and asset optimization. The architecture demonstrates contemporary full-stack development practices with a clear separation of concerns—backend business logic and data management in C#, frontend presentation and interactivity through a webpack-managed build pipeline—along with robust development infrastructure supporting hot module replacement, bundle analysis, and automated code quality enforcement. As a technical demonstration project from the MakeBoldSpark portfolio created by Mark Hazleton, TeachSpark serves as both a functional educational platform and a reference implementation for integrating LLM capabilities into enterprise .NET applications, making it particularly valuable for architects and developers evaluating modern AI integration patterns in web applications.

**Technology Stack Currency**: ✅ 90/100
**Dependencies**: 3 total (2 current, 1 outdated)

**Created**: 2025-06-19
**Last Modified**: 2026-05-15

---

### #13. [react-native-web-start](https://github.com/markhazleton/react-native-web-start)

Stars: 0 | Forks: 0 | Language: PowerShell | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2477 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: React Native Web Start

## Overview
React Native Web Start is a production-ready, enterprise-grade starter template for building cross-platform applications that run seamlessly on Web, iOS, and Android from a single TypeScript codebase. It combines React Native Web with Vite's lightning-fast build tooling to enable true "write once, deploy everywhere" development, eliminating the need to maintain separate codebases for different platforms while maintaining native-like performance and user experience.

## Key Features & Capabilities
The template provides comprehensive cross-platform development infrastructure including type-safe TypeScript configuration, Vite-powered HMR for instant feedback during development, responsive adaptive UI with Tailwind CSS and Sass preprocessing, production-ready HTTP client with error handling, and an innovative in-app markdown documentation browser. It features a monorepo structure organizing shared components, web-specific, and mobile-specific code with clear separation of concerns, alongside build automation scripts for asset management, documentation synchronization, and GitHub Pages deployment.

## Technology Stack & Architecture
Built on modern tooling (React 19.2.5, React Native 0.85.0, Vite 8.0.8, TypeScript 6.0.2), the project employs Metro bundler for mobile and Vite for web builds, with Tailwind CSS 4.2.2 for styling and Marked 17.0.6 for markdown rendering. The architecture uses a carefully organized packages structure separating shared UI components and business logic from platform-specific implementations, enabling code reuse while allowing platform-specific customizations when necessary.

## Development & Production Readiness
The repository demonstrates enterprise-grade practices including Jest testing setup, comprehensive ESLint and Prettier code quality tools, Dependabot security integration, automated CI/CD pipelines with GitHub Actions, SEO optimization, and PWA capabilities. Build automation scripts handle complex tasks like asset copying, documentation synchronization, and dynamic build metadata generation, reducing manual configuration overhead.

## Current Status & Target Audience
Despite zero stars and commits in the last 90 days (indicating a stale project), the template represents a mature, well-architected solution targeting React Native developers, full-stack engineers, and startups seeking to reduce development costs by maintaining single codebases. The 50-dependency stack with 50/100 tech currency score suggests the foundational technologies are stable, though some dependencies may benefit from updates; the project serves as an excellent reference implementation for teams evaluating React Native Web adoption or establishing cross-platform development standards.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 50 total (50 current, 0 outdated)

**Created**: 2025-07-26
**Last Modified**: 2026-05-11

---

### #14. [TailwindSpark](https://github.com/markhazleton/TailwindSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 4357 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# TailwindSpark Technical Summary

**TailwindSpark** is a production-ready React TypeScript monorepo that serves as a comprehensive showcase and learning platform for modern web development patterns, specifically emphasizing Tailwind CSS 4's advanced features like the `@theme` directive and semantic design tokens. Built with React 19.1.1, TypeScript 5.9, and Tailwind CSS 4.1.18, the project demonstrates scalable architecture through a Turborepo monorepo structure with shared design token packages, reusable UI component libraries, and a fully-featured demo application deployed at Tailwind.makeboldspark.com. The codebase emphasizes production quality through strict TypeScript enforcement, minimum 40% test coverage, WCAG AA accessibility compliance, and automated CI/CD pipelines, supplemented by formal project governance via a documented constitution and active maintenance including Dependabot dependency updates and security scanning. Its unique value proposition lies in combining educational content (interactive component examples and design system documentation) with enterprise-grade practices—making it equally valuable as a learning resource for developers studying modern React patterns and as a reference implementation for teams building scalable design systems. The project targets intermediate-to-advanced developers, technical architects, and organizations seeking to understand how to structure large-scale React applications with design-system-first approaches, though the stale activity status (0 commits in 90+ days) suggests it may currently be in maintenance mode rather than active development.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2025-07-29
**Last Modified**: 2026-05-15

---

### #15. [Texecon](https://github.com/markhazleton/Texecon)

Stars: 0 | Forks: 0 | Language: TypeScript | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3915 KB | 🚀 0 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: Texecon Repository

**Texecon** is a static React application delivering expert analysis and commentary on the Texas economy, hosted at texecon.com and built with React 19, TypeScript, Vite, and Tailwind CSS. The project implements a sophisticated build-time content management system that fetches fresh economic data from a headless WebSpark CMS API, generates SEO-optimized static HTML pages, and deploys to GitHub Pages with custom domain support. Its architecture emphasizes performance and search visibility through static site generation, pre-rendered routes, dynamic XML sitemaps, structured data implementation, and automatic cache busting—representing a modern approach to content-heavy web applications that require both real-time data integration and static hosting constraints. The tech stack includes accessible UI primitives from Radix UI, component library patterns via shadcn/ui, lightweight client-side routing through Wouter, and a comprehensive build pipeline orchestrating content fetching, type generation, Vite compilation, and post-build static page generation. Notably, the project demonstrates professional-grade engineering practices such as TypeScript strict typing, fallback content systems for API failures, build reporting mechanisms, and environment-based configuration—making it a technical demonstration portfolio piece by solutions architect Mark Hazleton that balances developer experience with production-grade reliability and SEO optimization.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 37 total (37 current, 0 outdated)

**Created**: 2025-09-03
**Last Modified**: 2026-05-13

---

### #16. [git-spark](https://github.com/markhazleton/git-spark)

Stars: 0 | Forks: 0 | Language: PowerShell | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 1608 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Git Spark - Technical Summary

**Git Spark** is a comprehensive Git repository analytics and reporting tool that analyzes commit history to generate interactive, enterprise-focused HTML dashboards with visualizations, contributor statistics, and file analysis patterns. The project provides both a command-line interface and Node.js API, enabling users to extract actionable insights from Git data through multiple export formats (HTML, JSON, CSV, Markdown) with configurable analysis periods and filtering options.

The application features advanced analytics capabilities including multi-series timeline visualizations, daily activity trends, contribution heatmaps, risk factor assessments, governance radar charts, and progressive data pagination—all delivered as self-contained, security-hardened reports with strict Content Security Policy implementation, email redaction options, and transparent metric documentation that explicitly acknowledges Git data limitations. The tech stack leverages TypeScript (43.7%) for core logic, PowerShell (45.3%) and Shell scripting (10.0%) for automation, with key dependencies including Commander for CLI parsing, Chalk for terminal styling, Ora for progress indicators, Semver for version management, and Boxen for formatted output.

Architecturally, the project emphasizes analytical integrity through offline-capable, air-gapped-friendly reports with embedded data (no external API calls), strict accessibility compliance (ARIA regions, keyboard navigation, reduced-motion support), and progressive enhancement patterns for handling large datasets. The platform targets development teams, solutions architects, and governance stakeholders seeking Git-based repository health assessments, knowledge concentration analysis, and conventional commit adherence tracking—positioning itself as part of the broader Make Bold Spark portfolio of technical demonstrations by Mark Hazleton. Despite strong tech stack currency (95/100) and polished documentation, the repository shows no recent activity over 90 days and zero community engagement, suggesting it may be in maintenance mode or a dormant personal project.

**Technology Stack Currency**: ✅ 95/100
**Dependencies**: 22 total (19 current, 3 outdated)

**Created**: 2025-09-29
**Last Modified**: 2026-05-19

---

### #17. [github-stats-spark](https://github.com/markhazleton/github-stats-spark)

Stars: 0 | Forks: 0 | Language: Python | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 26626 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Analysis: github-stats-spark

## Executive Summary

**Stats Spark** is a sophisticated GitHub analytics platform that combines automated SVG profile visualization generation with AI-powered repository analysis and an interactive mobile-first dashboard. Despite zero stars/forks and stale activity, the codebase demonstrates enterprise-grade architecture with 26.6MB of well-organized Python, JavaScript, and PowerShell components.

---

## 🏗️ Architecture Overview

### Technology Stack

| Layer | Technologies | Purpose |
|-------|--------------|---------|
| **Backend** | Python 3.11+, PyGithub, Claude AI API | Data aggregation, analysis, SVG generation |
| **Frontend** | JavaScript, React, Chart.js, Dexie | Interactive dashboard, visualizations |
| **Scripting** | PowerShell (18.8%) | CI/CD automation, GitHub Actions |
| **Styling** | CSS (9.1%), HTML (1.0%) | UI/UX responsive design |
| **Infrastructure** | GitHub Pages, GitHub Actions | Deployment & automation |

**Tech Currency Score: 76/100** — Modern stack with some aging dependencies (see risks below)

---

## 📦 Core Components

### 1. **SVG Profile Statistics Generator** (Python Backend)
**Dependencies**: PyGithub, svgwrite, requests

**Functionality:**
- Generates 6 categories of embeddable SVG visualizations
- **Spark Score Algorithm**: Weighted composite metric (40% consistency, 35% volume, 25% collaboration)
- **Dynamic Heatmap**: GitHub-style contribution calendars with intensity mapping
- **Activity Pattern Detection**: Identifies "Night Owl," "Early Bird," "Daytime Coder" personalities
- **Language Analysis**: Polyglot tracking with diversity metrics
- **Streak Tracking**: Current/longest streaks with visual indicators
- **Fun Stats**: 8 emoji-driven personality achievements
- **Release Cadence**: Sparklines for weekly/monthly activity breadth

**Technical Approach:**
- Automated weekly updates via GitHub Actions (Sunday midnight UTC)
- WCAG AA accessibility compliance
- Theme customization (dark/light/custom)
- Zero maintenance after initial setup

### 2. **AI-Powered Analysis Engine** (Python + Claude API)
**Dependencies**: PyYAML, beautifulsoup4, requests

**Capabilities:**
- **Intelligent Repository Ranking**: 3-weighted composite algorithm
  - 30% Popularity (stars/forks)
  - 45% Activity (time-decay: 90d/180d/365d windows)
  - 25% Health (documentation, licensing, maintenance signals)

- **Dependency Coverage Tracking**: Schema 2.3.0 with:
  - Known version tracking
  - Registry resolution coverage
  - Unknown-version gap identification
  - Enriched tech stack metadata

- **Attention Scoring**: Blends:
  - PR backlog pressure
  - Security findings
  - Staleness metrics
  - Dependency health indicators

- **AI Summaries**: Claude Haiku generates 4-6 sentence technical descriptions:
  - Purpose & scope
  - Key features & capabilities
  - Technology stack
  - Architectural patterns
  - Unique value proposition
  - Target use cases
  - **97%+ success rate** with sub-5-minute processing for 500+ repos

- **Performance**: Smart caching, rate-limit handling with exponential backoff

### 3. **Interactive Mobile-First Dashboard** (JavaScript/React)
**Dependencies**: React, Chart.js, react-chartjs-2, Dexie, IndexedDB

**UX Features:**
- **Mobile-Optimized**:
  - 44x44px minimum touch targets
  - Responsive layouts (320px-768px viewports)
  - Bottom sheet navigation pattern
  - Swipe gestures (swipe-to-delete, horizontal nav)

- **Data Visualization**:
  - Interactive Chart.js analytics
  - Touch-optimized tooltips
  - Real-time filtering & sorting
  - Drill-down detail views

- **Attention Dashboard**:
  - Ranks repositories by combined risk metrics
  - Security alerts integration
  - PR backlog visualization
  - Dependency drift tracking
  - Staleness indicators

- **Advanced Features**:
  - Offline support (Dexie/IndexedDB, 7-day retention)
  - CSV/JSON export functionality
  - GitHub-flavored markdown rendering
  - WCAG 2.1 AA compliance
  - Keyboard navigation support

- **Performance**:
  - Lighthouse CI configured
  - Target <2s First Contentful Paint
  - 0.9+ performance score goal

- **Deployment**: Automatic GitHub Pages publishing with weekly updates

---

## 🔧 Configuration & Deployment

**Configuration**: YAML-based (12 total dependencies)
**Local Development**: Full CLI support for testing
**Automation**: GitHub Actions workflow for:
- Weekly SVG regeneration
- Repository analysis updates
- Dashboard deployment
- Cache management

**Extensibility**: Modular architecture for custom implementations

---

## 📊 Data Pipeline

```
GitHub API (PyGithub) 
    ↓
[Data Aggregation & Caching]
    ↓
[Analysis Engine]
├── Repository Ranking
├── Dependency Analysis
├── AI Summarization (Claude API)
└── Spark Score Calculation
    ↓
[SVG Generation] + [Report Markdown]
    ↓
[Dashboard Indexing] (IndexedDB)
    ↓
[GitHub Pages + Deployment]
```

---

## ⚠️ Risk Assessment

### Critical Issues

| Issue | Severity | Details |
|-------|----------|---------|
| **No Recent Activity** | 🔴 HIGH | 0 commits in 90d/365d — codebase appears abandoned |
| **Zero Community Engagement** | 🔴 HIGH | No stars, forks, or contributors indicates lack of adoption |
| **Stale Dependencies** | 🟡 MEDIUM | Tech score 76/100 suggests outdated libraries; no lock files visible |
| **API Rate Limiting** | 🟡 MEDIUM | Unauthenticated GitHub API calls have strict limits; backoff strategy mentioned but not validated |
| **AI API Costs** |

**Technology Stack Currency**: ✅ 76/100
**Dependencies**: 12 total (4 current, 8 outdated)

**Created**: 2025-12-28
**Last Modified**: 2026-05-17

---

### #18. [MuseumSpark](https://github.com/markhazleton/MuseumSpark)

Stars: 0 | Forks: 0 | Language: Python | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 26794 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# MuseumSpark - Technical Summary

**MuseumSpark** is an intelligent travel planning platform that transforms the Walker Art Center's reciprocal membership program into a curated, data-enriched resource for art enthusiasts across North America. The project intelligently catalogs and prioritizes 1,269+ museums through a multi-phase data enrichment pipeline that combines structured data from Wikidata, Wikipedia, and official museum websites with expert scoring based on collection strength, historical significance, and reputation. The architecture employs a React 19 + Vite frontend with Tailwind CSS for a responsive museum browser interface, while Python 3.11+ scripts handle the complex backend data pipeline using Pydantic for schema validation, BeautifulSoup4 for web scraping, and JSON Schema for quality assurance across the dataset.

The project demonstrates a sophisticated approach to data quality and incremental development, featuring a transparent multi-phase roadmap (currently at Phase 1 with 0.08% enrichment completion) that progresses from foundational data gathering through expert scoring and AI-assisted validation, with planned Phase 4 enhancements including FastAPI backend, user authentication, and AI-powered itinerary generation. Currently deployed as a static GitHub Pages site with an automated data synchronization workflow, the platform uniquely combines the practical utility of museum discovery with rigorous data engineering practices—including evidence tracking, schema validation, and a "never replace known with null" data quality principle—while planning future evolution into a full-featured travel companion with personalization and AI recommendations. The codebase reflects best practices in both frontend development (React Router, component architecture) and data engineering (pipeline orchestration, multi-source validation), targeting art-loving travelers who need strategic guidance for museum visits across multiple cities and time constraints.

**Created**: 2026-01-15
**Last Modified**: 2026-05-14

---

### #19. [markhazleton.github.io](https://github.com/markhazleton/markhazleton.github.io)

Stars: 0 | Forks: 0 | Language: SCSS | 7 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 161 KB | 🚀 2.3 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: markhazleton.github.io

This repository is Mark Hazleton's personal portfolio website built with **Jekyll**, a static site generator, and hosted on GitHub Pages with automated CI/CD via GitHub Actions. The site implements a customized Minima theme using **SCSS**, HTML, and CSS (39.4%, 30.1%, and 29.8% respectively) to create a modern, responsive design with dark/light mode toggle functionality and emoji support, all without external UI frameworks. The tech stack leverages Ruby 3.2.2 and Jekyll 4.3+ dependencies (github-pages, faraday-retry, wdm) with a well-documented development workflow supporting local testing via `bundle exec jekyll serve --livereload` and streamlined post creation through standardized Markdown front matter conventions. The architecture follows Jekyll's conventional structure with modular layouts, reusable includes, and asset management, enabling efficient content management and SEO optimization through excerpt fields and proper heading hierarchies. The repository demonstrates maintained consistency with 7 commits over 90 days and includes comprehensive documentation covering setup instructions for macOS, Windows, and Linux environments, making it accessible for both local development and collaborative contributions. This project serves as both a functional personal brand platform and a well-documented template for Jekyll-based static site implementations, ideal for developers seeking to establish professional web presence with minimal infrastructure overhead.

**Technology Stack Currency**: ✅ 56/100
**Dependencies**: 3 total (2 current, 1 outdated)

**Created**: 2021-04-18
**Last Modified**: 2026-04-01

---

### #20. [SupportSpark](https://github.com/markhazleton/SupportSpark)

Stars: 0 | Forks: 0 | Language: PowerShell | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 1842 KB | 🚀 0 commits/month

**Quality**: ❌ License | ❌ Docs

# SupportSpark: Technical Summary

SupportSpark is a compassionate support network platform designed to help individuals share journey updates with trusted circles during challenging life moments (health issues, transitions, personal journeys). The application implements a role-based architecture where members create and manage private updates while invited supporters view posts and engage through threaded conversations, eliminating the burden of individually notifying loved ones during difficult periods.

The platform features a modern full-stack TypeScript architecture built on React 19 with Vite for the frontend, Express 5 for the backend, and Tailwind CSS 4 with shadcn/ui components for a calming, accessible interface optimized for sensitive contexts. Key capabilities include invitation-only networks with email-based supporter management, role-based access control, real-time threaded conversations, image support in updates, a demo mode with localStorage-backed data, and end-to-end type safety using Zod for runtime validation. The codebase demonstrates production-grade patterns including TanStack React Query for server state management, Passport.js authentication with session management, and comprehensive documentation spanning architectural decisions, deployment procedures, and API contracts.

The project is uniquely positioned as a portfolio demonstration piece by Solutions Architect Mark Hazleton, featuring Windows IIS deployment automation via PowerShell scripts and supporting both static GitHub Pages builds and traditional backend deployment. While the repository shows no recent activity (stale status since 90 days) and moderate tech stack currency (50/100), it exemplifies thoughtful application design for emotionally sensitive use cases, combining functional requirements (state management, authentication, data persistence) with UX principles emphasizing calm, distraction-free interaction patterns. The live deployment at support.makeboldspark.com provides a functional reference implementation targeting individuals navigating health challenges or life transitions who need a centralized platform for keeping supporters informed without constant individual communication.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 97 total (97 current, 0 outdated)

**Created**: 2026-02-01
**Last Modified**: 2026-05-14

---

### #21. [DocSpecSpark](https://github.com/markhazleton/DocSpecSpark)

Stars: 0 | Forks: 0 | Language: Python | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 575 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: DocSpecSpark

**DocSpecSpark** is an AI-assisted documentation framework that provides structured workflows for creating, reviewing, and publishing documentation systems through markdown-based prompts and lightweight tooling. The project implements a separation-of-concerns architecture with two distinct directories: `.docspark/` for framework-managed stock assets and `.documentation/` for user-owned artifacts, enabling safe upgrades while preserving customizations. Core functionality revolves around 21+ slash commands organized into workflows (constitution, specification, planning, implementation, publishing) plus specialized utilities for PR reviews, site audits, quality assurance, and documentation evolution—all designed to augment AI coding assistants (Copilot, Claude, Cursor) with repeatable processes. The tech stack leverages Python (77.7%) for the optional CLI tooling built with `typer` and `rich` libraries, complemented by JavaScript, PowerShell, and Shell scripts for cross-platform context-gathering and automation. The architecture emphasizes prompt resolution hierarchies and configurable script resolution, allowing users to personalize workflows while maintaining framework consistency, with MkDocs and GitHub Pages templates providing publication scaffolding. This makes DocSpecSpark particularly valuable for teams seeking AI-native documentation practices that maintain governance through constitutional guidelines while reducing manual setup friction through CLI automation and reference examples.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 2 total (0 current, 2 outdated)

**Created**: 2026-03-07
**Last Modified**: 2026-05-17

---

### #22. [DataSpark](https://github.com/markhazleton/DataSpark)

Stars: 0 | Forks: 0 | Language: HTML | 0 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 2089 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# DataSpark Technical Summary

DataSpark is a comprehensive .NET 10 toolkit designed for SQLite database discovery, analysis, and code generation, offering both CLI and ASP.NET Core MVC web interfaces for database operations. The solution provides core functionality including SQLite file discovery within directories, table export to CSV format, schema inspection with multiple output formats (text, JSON, Markdown), and automated C# Data Transfer Object (DTO) generation from database schemas. Built with a modular architecture comprising a shared Core library, specialized Console CLI application, web UI with file persistence capabilities, comprehensive MSTest unit/integration tests, and BenchmarkDotNet performance benchmarks, the project demonstrates enterprise-grade software engineering practices. The technology stack leverages .NET 10, ASP.NET Core MVC, SQLite, with optional Node.js for frontend asset building, supporting both PowerShell and HTML components for broader compatibility. DataSpark targets software developers and data engineers who need rapid database schema exploration and C# model generation, particularly in scenarios requiring bulk SQLite analysis across multiple files or one-time database migrations. The project is actively maintained with CI/CD pipelines, code coverage tracking, and a live deployment at data.makeboldspark.com, making it both a practical tool and a reference implementation for modern .NET database tooling best practices.

**Created**: 2017-11-06
**Last Modified**: 2026-05-12

---

### #23. [WebSpark.ArtSpark](https://github.com/markhazleton/WebSpark.ArtSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3894 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.ArtSpark

WebSpark.ArtSpark is a comprehensive .NET 10.0 solution that provides a complete client library and AI-powered chatbot system for the Art Institute of Chicago's public REST API, covering all 33 endpoints across 6 major categories. The solution demonstrates modern .NET development practices through four interconnected projects: a strongly-typed API client library with async/await support and IIIF image handling, a revolutionary AI agent system leveraging Semantic Kernel and OpenAI Vision for multi-persona conversational analysis (Artwork, Artist, Curator, Historian personas), an ASP.NET Core web application with user authentication and personal collection management, and a command-line interface for developers. Key architectural highlights include externalized prompt management with hot-reload capability for development, comprehensive error handling with System.Text.Json deserialization, and a responsive Bootstrap 5 UI with dynamic theme switching and mobile-first navigation. The project uniquely combines traditional REST API client patterns with cutting-edge generative AI, featuring visual analysis capabilities, conversation memory management, and cultural sensitivity guardrails for educational contexts. Built by Mark Hazleton as part of the MakeBoldSpark portfolio, it serves as both a production-ready library for Art Institute integration and a technical demonstration of enterprise-grade .NET patterns, though the repository shows signs of staleness with zero recent commits over 90 days despite being publicly available at Art.makeboldspark.com.

**Created**: 2023-01-30
**Last Modified**: 2026-05-13

---

### #24. [PHPDocSpark](https://github.com/markhazleton/PHPDocSpark)

Stars: 0 | Forks: 0 | Language: PHP | 0 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 3049 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

An open-source PHP documentation & data exploration platform by Mark Hazleton (WebSpark suite) showcasing hybrid server-side + modern asset pipeline techniques. Written in PHP.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2023-09-08
**Last Modified**: 2026-05-12

---

### #25. [InquirySpark](https://github.com/markhazleton/InquirySpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 9 languages | 💾 13989 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# InquirySpark - Technical Summary

InquirySpark is a modern .NET 10 web application that serves as a unified survey, inquiry, and decision-management platform, consolidating multiple legacy applications into a single ASP.NET Core MVC workspace. Built by Mark Hazleton as a technical demonstration within the Make Bold Spark portfolio, it showcases contemporary enterprise web development patterns by combining Bootstrap 5 frontend components with Entity Framework Core 10, ASP.NET Core Identity for authentication, and immutable SQLite databases for persistence—eliminating the need for SQL Server infrastructure. The architecture emphasizes clean separation of concerns through a multi-project structure (Web, Repository, Common libraries) with comprehensive dependency injection, structured audit logging, and standardized response wrappers, while the unified operations area consolidates capabilities like the Capability Completion Matrix and Operational Readiness dashboards under a single authenticated session and navigation model. Key technical distinguishing factors include warning-as-error enforcement across all projects (ensuring nullable reference type safety and XML documentation), automated npm asset pipeline integration, read-only database modes for inquiry data with selective read-write access for Identity operations, and an extensive test suite (MSTest) covering shared libraries and capability services. This solution is particularly valuable for organizations seeking reference implementations of modern ASP.NET Core practices, those migrating from legacy multi-application ecosystems to unified platforms, and teams evaluating enterprise web architecture patterns for survey and decision-management workloads—though the project is currently in a stale state with no recent commits, indicating it functions as a completed demonstration rather than an actively evolving product.

**Created**: 2023-10-24
**Last Modified**: 2026-05-11

---

### #26. [BootstrapSpark](https://github.com/markhazleton/BootstrapSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 0 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 38317 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# BootstrapSpark - Technical Summary

**BootstrapSpark** is an enterprise-grade developer portfolio and technical demonstration website built with React 19, TypeScript, and Vite, deployed on Azure Static Web Apps and showcasing modern full-stack web development practices. The application serves as both a personal portfolio for Mark Hazleton and a comprehensive reference implementation, featuring a responsive Bootstrap 5-based UI with dark/light theme switching, real-time chat via SignalR integration, live weather widgets powered by OpenWeather API, dynamic RSS feed aggregation, and interactive mapping capabilities using Leaflet. The technology stack emphasizes type safety and performance optimization through strict TypeScript configuration, code splitting, lazy loading, and Vite's optimized build process, complemented by a clean separation of concerns using React Context API for state management and a modular component architecture. The project implements production-ready patterns including CI/CD automation via GitHub Actions, content security policy configuration for multi-source asset loading, WCAG 2.1 AA accessibility compliance, and comprehensive documentation for both users and developers. BootstrapSpark is particularly noteworthy for its intentionally permissive but well-documented frontend-only architecture that aggregates content from external sources (markhazleton.com), demonstrating how to build sophisticated web applications without traditional backend infrastructure while maintaining security awareness. The repository targets full-stack developers and architects seeking reference implementations of enterprise-grade React development, modern deployment patterns, and scalable web application architecture—though it currently shows signs of being maintenance-stale with zero recent commits over 90 and 365-day periods.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 47 total (47 current, 0 outdated)

**Created**: 2024-10-11
**Last Modified**: 2026-05-15

---

### #27. [PromptSpark.Chat](https://github.com/markhazleton/PromptSpark.Chat)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 19666 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# PromptSpark.Chat - Technical Summary

PromptSpark.Chat is a real-time conversational workflow application built with ASP.NET Core and SignalR that guides users through multi-step processes using Adaptive Cards for interactive UI elements, with optional AI integration to handle open-ended questions beyond structured workflows. The application leverages modern web technologies including C#, SCSS, HTML, and JavaScript to deliver a responsive chat interface that maintains conversation state server-side through thread-safe ConcurrentDictionary storage, enabling persistent user sessions that survive page refreshes. Key features include workflow persistence, real-time bidirectional communication via SignalR, branching logic driven by JSON-configured workflow nodes, and optional chat completion service integration for AI-driven responses to questions outside the predefined workflow scope. The architecture demonstrates clean separation of concerns with dedicated Controllers, Services, and Views layers, supports flexible JSON-based workflow configuration for easy customization without code changes, and implements simple concurrency management suitable for moderate user loads. The project is designed as both a production-ready demonstration and a learning resource for developers building conversational interfaces, with comprehensive documentation covering setup, configuration, deployment strategies, and scaling considerations. Target users include enterprises needing guided user interactions, customer support teams automating common workflows, and developers seeking examples of real-time web applications with structured conversation management.

**Created**: 2024-12-31
**Last Modified**: 2026-05-14

---

### #28. [WebSpark.PrismSpark](https://github.com/markhazleton/WebSpark.PrismSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 2280 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.PrismSpark

**WebSpark.PrismSpark** is a modern C#/.NET 10 port of the popular PrismJS syntax highlighting library, providing advanced code highlighting, theming, and extensibility capabilities for .NET web applications. The project delivers tokenization and syntax highlighting for 24 programming languages (C#, JavaScript, Python, Markdown, Pug, etc.) with a robust plugin system supporting line numbers, copy-to-clipboard, toolbars, and custom extensions, alongside a comprehensive theme system with built-in themes and CSS generation capabilities.

The architecture employs a modular design pattern with clear separation of concerns—featuring core tokenization engines, language-specific grammars, plugin and hook systems for extensibility, and specialized highlighter implementations (HtmlHighlighter, EnhancedHtmlHighlighter, ThemedHtmlHighlighter) that support advanced options like line highlighting, custom CSS classes, async processing, and caching. The codebase is primarily C# (72.9%) with supporting HTML, PowerShell, JavaScript, and CSS components, and includes a comprehensive test suite of 52 MSTest tests covering grammar validation, tokenization, highlighting workflows, and integration scenarios.

The project stands out through its tight ASP.NET Core MVC integration via dependency injection, live interactive demo pages (including a real-time code editor and markdown processor), and production-ready performance considerations with async/caching APIs—making it particularly valuable for developers building documentation sites, code review platforms, learning management systems, and technical blogging platforms within the .NET ecosystem. However, the repository shows signs of being inactive (zero commits in 90-365 days, no contributors or stars recorded), suggesting it may be a completed demonstration project or archived reference implementation rather than an actively maintained production library.

**Created**: 2025-05-27
**Last Modified**: 2026-05-12

---

### #29. [MechanicsOfMotherhood](https://github.com/markhazleton/MechanicsOfMotherhood)

Stars: 0 | Forks: 0 | Language: TypeScript | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7598 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Mechanics of Motherhood

**Mechanics of Motherhood** is a production-ready recipe management web application built with React 19 and TypeScript, designed specifically for busy working mothers seeking organized meal planning solutions. The platform features 108+ curated recipes sourced from live APIs (RecipeSpark and WebCMS), organized across 14 categories with smart search, filtering, ratings, and nutritional information capabilities. The architecture leverages modern frontend technologies including Vite for fast builds, TanStack React Query for server state management, Tailwind CSS with Shadcn/ui components for industrial-themed styling, and Wouter for lightweight client-side routing. The application is deployed as a static Single Page Application (SPA) on GitHub Pages with a custom domain (mechanicsofmotherhood.com), automated CI/CD pipelines via GitHub Actions, and PWA-ready offline support with cached recipe data. Key technical achievements include mobile-first responsive design optimized for 3G networks, Lighthouse performance scores exceeding 95, SEO optimization with structured data and auto-generated sitemaps, and automated data quality validation. While the repository shows no recent activity and a stale status (0 commits in 90+ days), it demonstrates a complete production deployment pattern combining real API integration, custom domain hosting with SSL, and modern TypeScript/React best practices—making it an excellent portfolio piece for showcasing full-stack modern web development capabilities.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 42 total (42 current, 0 outdated)

**Created**: 2025-09-01
**Last Modified**: 2026-05-12

---

### #30. [ApiSpark](https://github.com/markhazleton/ApiSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 1659 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: ApiSpark

**ApiSpark** is a modular ASP.NET Core backend platform designed to consolidate multiple low-volume APIs into a single, cost-effective Azure-hosted service that serves as the centralized API layer for static sites and single-page applications. The project demonstrates enterprise-grade API architecture by combining EF Core with SQLite as the default data store while supporting Azure Cosmos DB for document-oriented workloads, all hosted on Azure App Service with Azure Static Web Apps clients. The platform implements a sophisticated route segmentation strategy with `/api/public/*` for anonymous read-only access, `/api/admin/*` for authenticated CMS operations, `/api/publish/*` for content export, and `/api/integrations/*` for third-party connectivity, along with health check endpoints for monitoring. Built on .NET 10 LTS and leveraging browser-based CMS/admin capabilities, ApiSpark prioritizes simplicity, portability, and cost-efficiency by eliminating the need for expensive database services while maintaining relational data integrity and multi-tenant API governance. The architecture is governed by documented Architecture Decision Records and a project constitution, making it a reference implementation for developers seeking to host multiple small APIs sustainably while keeping client-side applications static-first. This project is particularly valuable for portfolio demonstrations, multi-project API consolidation, and organizations looking to minimize hosting costs without sacrificing ASP.NET Core's capabilities or architectural rigor.

**Created**: 2026-05-07
**Last Modified**: 2026-05-15

---


---

## Report Metadata

- **Generation Time**: 3.9 seconds
- **SVGs Generated**: 6/6
- **Total API Calls**: 0
- **Total AI Tokens**: 73,278
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
*Last updated: 2026-05-24*

## Screenshot Audit

- Repositories with websites: 22
- Screenshots present: 5
- Flagged repositories: 17

### Likely 404 Pages

- UISampleSpark: https://ui.makeboldspark.com (status: 403, title: Just a moment...)
- WebProjectMechanics: https://wpm.makeboldspark.com (status: 403, title: Just a moment...)
- WebSpark.Bootswatch: https://bootswatch.makeboldspark.com/ (status: 403, title: Just a moment...)
- TeachSpark: https://teach.makeboldspark.com (status: 403, title: Just a moment...)
- WebSpark.ArtSpark: https://art.makeboldspark.com (status: 403, title: Just a moment...)
- BootstrapSpark: https://bootstrap.makeboldspark.com/ (status: 403, title: Just a moment...)
- WebSpark.PrismSpark: https://prism.makeboldspark.com (status: 403, title: Just a moment...)
- ApiSpark: https://makeboldspark.com (status: 403, title: Just a moment...)

### Missing Screenshots

- UISampleSpark: https://ui.makeboldspark.com
- WebProjectMechanics: https://wpm.makeboldspark.com
- KeyPressCounter: http://keypresscounter.makeboldspark.com/
- WebSpark.Bootswatch: https://bootswatch.makeboldspark.com/
- WebSpark.HttpClientUtility: http://httpclientutility.makeboldspark.com/
- TeachSpark: https://teach.makeboldspark.com
- TailwindSpark: http://tailwind.makeboldspark.com/
- Texecon: https://texecon.com
- MuseumSpark: https://markhazleton.github.io/MuseumSpark/
- SupportSpark: http://support.makeboldspark.com/
- DocSpecSpark: https://markhazleton.github.io/DocSpecSpark/
- WebSpark.ArtSpark: https://art.makeboldspark.com
- BootstrapSpark: https://bootstrap.makeboldspark.com/
- WebSpark.PrismSpark: https://prism.makeboldspark.com
- MechanicsOfMotherhood: http://mechanicsofmotherhood.com/
- ApiSpark: https://makeboldspark.com
- PHPDocSpark: https://phpdocspark.azurewebsites.net
