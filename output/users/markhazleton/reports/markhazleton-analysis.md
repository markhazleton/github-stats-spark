# GitHub Profile: markhazleton

**Generated**: 2026-05-17 00:46:56 UTC
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

👥 0 contributors | 🌐 6 languages | 💾 31215 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# UISampleSpark – Technical Summary

**UISampleSpark** is an educational .NET 10 (ASP.NET Core) reference application that demonstrates how to implement the same Employee/Department CRUD domain across seven distinct front-end UI patterns—MVC, Razor Pages, jQuery AJAX, React, Vue, htmx, and Blazor Server—within a single application. The project serves as a comprehensive comparison framework for modern web UI technologies, allowing developers to evaluate architectural tradeoffs, component patterns, and interactivity approaches side-by-side using a consistent REST API backend built with Entity Framework Core and Swagger/OpenAPI documentation.

The application showcases production-grade practices including clean architecture with dependency injection, a service/repository abstraction layer, comprehensive unit test coverage across domain and data layers, dynamic Bootswatch theme switching for real-time UI customization, and integrated Application Insights telemetry for observability. It demonstrates multiple data handling patterns—from traditional server-side rendering and AJAX-driven modals to modern client-side SPAs with frameworks like React 18 and Vue 3, plus innovative approaches like htmx for server-driven hypermedia and Blazor for real-time C# components over SignalR.

The tech stack spans C# (18%), HTML (45.2%), JavaScript (21.4%), PowerShell (14.8%), and CSS, with heavy use of Bootstrap 5, Entity Framework Core in-memory databases, and containerization via Docker. The project is fully integrated with modern CI/CD pipelines using GitHub Actions for automated building, testing, and Docker image publishing to Docker Hub, plus historical Azure Pipelines integration, making it suitable for teams exploring cloud deployment and DevOps practices.

Designed by Mark Hazleton as part of the MakeBoldSpark portfolio, **UISampleSpark** is ideal for architects, senior developers, and engineering teams evaluating UI technology choices, learning contemporary web patterns, or establishing reference implementations for enterprise ASP.NET Core applications. Despite recent inactivity (no commits in 90+ days), the codebase remains a valuable educational resource demonstrating how to structure scalable, maintainable web applications with multiple presentation layers while maintaining a single, well-designed backend domain model.

**Created**: 2019-04-25
**Last Modified**: 2026-05-16

---

### #2. [FastEndpointApi](https://github.com/markhazleton/FastEndpointApi)

Stars: 3 | Forks: 1 | Language: HTML | 0 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 156 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: FastEndpointApi Repository

**FastEndpointsSpark** is a comprehensive demonstration project showcasing the FastEndpoints framework for ASP.NET Core, implementing a fully functional Person Management API that exemplifies the REPR (Request-Endpoint-Response) pattern and modern API best practices. The project leverages .NET 10.0, FastEndpoints 7.1.1, and FastEndpoints.Swagger to provide a production-ready example of building clean, maintainable REST APIs with minimal boilerplate code, featuring complete CRUD operations, HATEOAS hypermedia links, dependency injection, smart request/response mapping, and interactive Swagger/OpenAPI documentation. The architecture demonstrates proper separation of concerns through a service layer abstraction, in-memory data persistence, and reusable endpoint base classes, while utilizing auxiliary technologies including Bogus for test data generation, Bootstrap for frontend UI, and GitHub Actions with Azure Web Apps for CI/CD deployment. The codebase is organized across HTML (60.4%), C# (38.4%), and JavaScript (1.2%), providing both backend API implementation and static HTML sample pages (index.html, docs.html, test.html) that serve as an educational platform for developers. This project is particularly valuable for developers looking to understand modern ASP.NET Core API patterns, migrate from MVC Controllers or Minimal APIs, and implement enterprise-level architectural practices in a learning-friendly environment, with accompanying documentation, live deployment at fastendpoints.makeboldspark.com, and an associated detailed article explaining the implementation methodology. Though currently in a stale state (no commits in 365+ days), it remains a well-documented, production-quality reference implementation suitable for educational purposes and architectural guidance.

**Created**: 2024-04-06
**Last Modified**: 2026-05-15

---

### #3. [RequestSpark](https://github.com/markhazleton/RequestSpark)

Stars: 2 | Forks: 1 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 966 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# RequestSpark - Technical Summary

RequestSpark is a comprehensive .NET 10 (LTS) web application and console tool designed for REST API testing, performance benchmarking, and regression testing using Postman collections as the primary input format. The project provides both a Razor Pages-based web interface and a console application that enable users to import Postman collection definitions, execute automated API test suites, perform load testing, analyze response time metrics, and export detailed results to CSV with statistical analysis including percentiles and success rates. The architecture comprises multiple layers including a core Domain project (RequestSpark.Domain) handling business logic, a PostmanImport project for collection parsing, a Web project built on ASP.NET Core, and comprehensive test coverage through MSTest v4, demonstrating solid separation of concerns and testability patterns. The technology stack includes modern .NET 10 components with optimized dependencies (93% at latest versions), security-hardened with zero vulnerabilities, and delivers measurable performance improvements—19% faster builds and 25% faster test execution compared to its .NET 9 predecessor. RequestSpark is positioned as a technical demonstration within the Make Bold Spark portfolio and serves developers, QA engineers, and solutions architects who need to validate API reliability and performance without licensing commercial tools like Postman Cloud. The project's stale status (no commits in 90+ days) and minimal community engagement (2 stars, 1 fork) suggest it remains a proof-of-concept or internal tool rather than an actively maintained open-source project, though the live instance at request.makeboldspark.com indicates ongoing deployment and demonstration purposes.

**Created**: 2021-09-30
**Last Modified**: 2026-05-11

---

### #4. [KeyPressCounter](https://github.com/markhazleton/KeyPressCounter)

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

### #5. [WebProjectMechanics](https://github.com/markhazleton/WebProjectMechanics)

Stars: 3 | Forks: 0 | Language: Visual Basic .NET | 11 commits (90d)

👥 0 contributors | 🌐 11 languages | 💾 52587 KB | 🚀 3.7 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebProjectMechanics

**WebProjectMechanics** is a greenfield rebuild of a legacy multi-tenant content management system designed to serve 36+ independent websites from a single application instance while maintaining physical data isolation and minimal infrastructure costs (~$10/month). The system architecture employs a plugin-based domain model with domain-specific content types (CMS pages, mineral collections, recipes), per-site SQLite databases for tenant isolation, and a publish-to-static workflow that pre-renders all public content as HTML served by Caddy, eliminating database queries in the critical path. Built on ASP.NET Core 9 with EF Core 9, the project leverages modern .NET patterns including Minimal APIs, dependency injection, and xUnit testing while using Scriban for templating and GitHub Actions for CI/CD on Ubuntu 24.04. The codebase is structured around separation of concerns with shared contracts (WPM.Core), infrastructure services, a minimal API host, and isolated domain projects, complemented by comprehensive documentation of both the legacy system it's replacing and the phased implementation plan. This approach is particularly noteworthy for its cost-efficiency, data isolation without tenant IDs, and the pragmatic decision to maintain a read-only archive of the 20+ year legacy system, making it an excellent case study in migrating complex enterprise applications to modern cloud-native architectures while preserving operational continuity.

**Created**: 2017-09-19
**Last Modified**: 2026-05-14

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

👥 0 contributors | 🌐 6 languages | 💾 1950 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# AsyncSpark Technical Summary

AsyncSpark is a production-ready reference implementation demonstrating enterprise-grade asynchronous programming patterns in .NET 10, built by Solutions Architect Mark Hazleton as part of the Make Bold Spark portfolio. The project serves as both a working application and an educational resource, featuring a live ASP.NET Core web application with interactive API documentation that showcases eight core async/await patterns including ConfigureAwait(false) usage, CancellationToken threading, Task.WhenAll parallelization, SemaphoreSlim throttling, Polly resilience policies, decorator pattern implementation, and fire-and-forget safety patterns.

The repository's defining characteristic is its "Constitution-Driven Development" approach—a formalized framework that enforces coding standards and architectural principles through automated compliance auditing, strict 80% code coverage requirements in CI/CD pipelines, and principled design constraints covering modern .NET standards, testing methodologies, dependency injection patterns, and resilience implementation. Built with C# (43%), HTML (34.2%), PowerShell (18.8%), and supporting technologies including MSTest, Moq, OpenAPI/Scalar, and the Polly resilience library, the architecture emphasizes clean design with interface-based components, decorator-pattern cross-cutting concerns, and zero blocking calls throughout the codebase.

AsyncSpark is particularly noteworthy for its comprehensive developer experience, combining a live demonstration site (web.makeboldspark.com/asyncspark) with Scalar-powered interactive API documentation, detailed learning objectives linking patterns to specific code implementations, and automated SpecKit-based PR reviews and constitution audits. The project targets intermediate-to-advanced .NET developers seeking production patterns, architecture best practices, and a reusable template for enterprise async workflows, though the repository appears inactive (no commits in 90-365 days) despite being positioned as a current reference implementation for .NET 10 standards.

**Created**: 2022-08-07
**Last Modified**: 2026-05-11

---

### #8. [DataSpark](https://github.com/markhazleton/DataSpark)

Stars: 0 | Forks: 0 | Language: HTML | 0 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 2089 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# DataSpark Technical Summary

DataSpark is a comprehensive .NET 10 toolkit designed for SQLite database discovery, analysis, and code generation, offering both CLI and ASP.NET Core MVC web interfaces for database operations. The solution provides core functionality including SQLite file discovery within directories, table export to CSV format, schema inspection with multiple output formats (text, JSON, Markdown), and automated C# Data Transfer Object (DTO) generation from database schemas. Built with a modular architecture comprising a shared Core library, specialized Console CLI application, web UI with file persistence capabilities, comprehensive MSTest unit/integration tests, and BenchmarkDotNet performance benchmarks, the project demonstrates enterprise-grade software engineering practices. The technology stack leverages .NET 10, ASP.NET Core MVC, SQLite, with optional Node.js for frontend asset building, supporting both PowerShell and HTML components for broader compatibility. DataSpark targets software developers and data engineers who need rapid database schema exploration and C# model generation, particularly in scenarios requiring bulk SQLite analysis across multiple files or one-time database migrations. The project is actively maintained with CI/CD pipelines, code coverage tracking, and a live deployment at data.makeboldspark.com, making it both a practical tool and a reference implementation for modern .NET database tooling best practices.

**Created**: 2017-11-06
**Last Modified**: 2026-05-12

---

### #9. [markhazleton](https://github.com/markhazleton/markhazleton)

Stars: 0 | Forks: 0 | Language: Unknown | 0 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 6624 KB | 🚀 0 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: Mark Hazleton's Portfolio Repository

This repository serves as Mark Hazleton's personal GitHub profile and portfolio hub, functioning primarily as a curated entry point to his professional work and learning journey rather than a traditional code project. The README showcases a .NET and Azure-focused engineer's featured projects including WebSpark (a comprehensive demo application hosting platform), ReactSpark (a Vite-built React application on Azure Static Web Apps), TailwindSpark (an opinionated UI foundation framework), and UISampleSpark (a containerized UI component library available on Docker Hub). The technical stack emphasizes modern web development with React, Vite, Tailwind CSS, .NET backend services, and Azure cloud infrastructure, reflecting a focus on full-stack development and cloud-native architecture patterns. The repository is notable for its emphasis on continuous learning, developer tooling, and educational content, evidenced by an extensive blog featuring articles on DevOps practices, analytics design, AI/ML considerations, and engineering metrics—positioning the profile as both a portfolio and thought leadership platform. The project targets fellow developers and potential collaborators seeking insights into contemporary .NET/Azure practices, UI design patterns, and software engineering best practices, with active engagement across multiple platforms (LinkedIn, Stack Overflow, Postman) indicating a community-oriented approach to knowledge sharing.

**Created**: 2021-04-17
**Last Modified**: 2026-05-12

---

### #10. [WebSpark.ArtSpark](https://github.com/markhazleton/WebSpark.ArtSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3894 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.ArtSpark

WebSpark.ArtSpark is a comprehensive .NET 10.0 solution that provides a complete client library and AI-powered chatbot system for the Art Institute of Chicago's public REST API, covering all 33 endpoints across 6 major categories. The solution demonstrates modern .NET development practices through four interconnected projects: a strongly-typed API client library with async/await support and IIIF image handling, a revolutionary AI agent system leveraging Semantic Kernel and OpenAI Vision for multi-persona conversational analysis (Artwork, Artist, Curator, Historian personas), an ASP.NET Core web application with user authentication and personal collection management, and a command-line interface for developers. Key architectural highlights include externalized prompt management with hot-reload capability for development, comprehensive error handling with System.Text.Json deserialization, and a responsive Bootstrap 5 UI with dynamic theme switching and mobile-first navigation. The project uniquely combines traditional REST API client patterns with cutting-edge generative AI, featuring visual analysis capabilities, conversation memory management, and cultural sensitivity guardrails for educational contexts. Built by Mark Hazleton as part of the MakeBoldSpark portfolio, it serves as both a production-ready library for Art Institute integration and a technical demonstration of enterprise-grade .NET patterns, though the repository shows signs of staleness with zero recent commits over 90 days despite being publicly available at Art.makeboldspark.com.

**Created**: 2023-01-30
**Last Modified**: 2026-05-13

---

### #11. [WebSpark.Bootswatch](https://github.com/markhazleton/WebSpark.Bootswatch)

Stars: 0 | Forks: 0 | Language: HTML | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7144 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.Bootswatch

**WebSpark.Bootswatch** is a .NET 10-exclusive Razor Class Library that provides streamlined integration of Bootswatch themes into ASP.NET Core applications, enabling developers to implement modern, responsive Bootstrap 5-based theming with dynamic switching capabilities. The library combines HTML (63.8%), C# (28.6%), and supporting languages to deliver a comprehensive feature set including light/dark mode support, built-in caching mechanisms via the `StyleCache` service, tag helper components for easy UI integration, and production-ready error handling with fallback mechanisms. Built on contemporary .NET standards, the library leverages modern Microsoft.Extensions packages and demonstrates a deliberate architectural decision to prioritize security, performance, and maintainability by exclusively targeting .NET 10 rather than supporting legacy frameworks—a strategic choice documented through comprehensive migration guides for users upgrading from version 1.x. The project employs dependency injection patterns, extension methods for single-line setup, and comprehensive XML documentation with IntelliSense support, making it accessible for developers while maintaining enterprise-grade reliability. WebSpark.Bootswatch is positioned as a production-ready component within the broader Make Bold Spark portfolio, with a live demonstration site and NuGet distribution, making it particularly valuable for ASP.NET Core teams seeking rapid theme implementation without custom CSS development or complex styling infrastructure. Despite current inactivity (90+ days without commits and zero community engagement metrics), the project represents a mature, well-documented solution targeted at mid-to-large organizations requiring professional theming capabilities in their web applications.

**Created**: 2022-08-24
**Last Modified**: 2026-05-11

---

### #12. [PHPDocSpark](https://github.com/markhazleton/PHPDocSpark)

Stars: 0 | Forks: 0 | Language: PHP | 0 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 3049 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

An open-source PHP documentation & data exploration platform by Mark Hazleton (WebSpark suite) showcasing hybrid server-side + modern asset pipeline techniques. Written in PHP.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2023-09-08
**Last Modified**: 2026-05-12

---

### #13. [InquirySpark](https://github.com/markhazleton/InquirySpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 9 languages | 💾 13989 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# InquirySpark - Technical Summary

InquirySpark is a modern .NET 10 web application that serves as a unified survey, inquiry, and decision-management platform, consolidating multiple legacy applications into a single ASP.NET Core MVC workspace. Built by Mark Hazleton as a technical demonstration within the Make Bold Spark portfolio, it showcases contemporary enterprise web development patterns by combining Bootstrap 5 frontend components with Entity Framework Core 10, ASP.NET Core Identity for authentication, and immutable SQLite databases for persistence—eliminating the need for SQL Server infrastructure. The architecture emphasizes clean separation of concerns through a multi-project structure (Web, Repository, Common libraries) with comprehensive dependency injection, structured audit logging, and standardized response wrappers, while the unified operations area consolidates capabilities like the Capability Completion Matrix and Operational Readiness dashboards under a single authenticated session and navigation model. Key technical distinguishing factors include warning-as-error enforcement across all projects (ensuring nullable reference type safety and XML documentation), automated npm asset pipeline integration, read-only database modes for inquiry data with selective read-write access for Identity operations, and an extensive test suite (MSTest) covering shared libraries and capability services. This solution is particularly valuable for organizations seeking reference implementations of modern ASP.NET Core practices, those migrating from legacy multi-application ecosystems to unified platforms, and teams evaluating enterprise web architecture patterns for survey and decision-management workloads—though the project is currently in a stale state with no recent commits, indicating it functions as a completed demonstration rather than an actively evolving product.

**Created**: 2023-10-24
**Last Modified**: 2026-05-11

---

### #14. [BootstrapSpark](https://github.com/markhazleton/BootstrapSpark)

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

### #15. [PromptSpark.Chat](https://github.com/markhazleton/PromptSpark.Chat)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 19666 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# PromptSpark.Chat - Technical Summary

PromptSpark.Chat is a real-time conversational workflow application built with ASP.NET Core and SignalR that guides users through multi-step processes using Adaptive Cards for interactive UI elements, with optional AI integration to handle open-ended questions beyond structured workflows. The application leverages modern web technologies including C#, SCSS, HTML, and JavaScript to deliver a responsive chat interface that maintains conversation state server-side through thread-safe ConcurrentDictionary storage, enabling persistent user sessions that survive page refreshes. Key features include workflow persistence, real-time bidirectional communication via SignalR, branching logic driven by JSON-configured workflow nodes, and optional chat completion service integration for AI-driven responses to questions outside the predefined workflow scope. The architecture demonstrates clean separation of concerns with dedicated Controllers, Services, and Views layers, supports flexible JSON-based workflow configuration for easy customization without code changes, and implements simple concurrency management suitable for moderate user loads. The project is designed as both a production-ready demonstration and a learning resource for developers building conversational interfaces, with comprehensive documentation covering setup, configuration, deployment strategies, and scaling considerations. Target users include enterprises needing guided user interactions, customer support teams automating common workflows, and developers seeking examples of real-time web applications with structured conversation management.

**Created**: 2024-12-31
**Last Modified**: 2026-05-14

---

### #16. [WebSpark.HttpClientUtility](https://github.com/markhazleton/WebSpark.HttpClientUtility)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2751 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.HttpClientUtility

**WebSpark.HttpClientUtility** is an enterprise-grade HTTP client wrapper library for .NET 8-10 LTS that dramatically simplifies resilient HTTP communication by encapsulating complex patterns (Polly retry/circuit-breaker policies, intelligent response caching, correlation ID tracking, and OpenTelemetry distributed tracing) into a single `AddHttpClientUtility()` dependency injection call. Built primarily in C# with PowerShell build automation, the library is distributed as two focused NuGet packages: the core **WebSpark.HttpClientUtility** providing HTTP client utilities with authentication, caching, and resilience features, and **WebSpark.HttpClientUtility.Crawler** adding web crawling, robots.txt parsing, and sitemap generation capabilities. The project follows enterprise software practices including comprehensive automated test coverage across all three supported .NET versions, Source Link debugging support, Native AOT and IL trimming annotations, semantic versioning with strict backward compatibility guarantees, and continuous integration via GitHub Actions—positioning it as production-ready for microservices, background workers, and web scrapers that require distributed tracing and rate-limit compliance without boilerplate. The architecture leverages established libraries (Polly for resilience, IHttpClientFactory for client management, structured logging with correlation IDs) and provides an opinionated, minimal-configuration alternative to manual HttpClient setup or more heavyweight frameworks like Refit, targeting developers seeking to eliminate 50+ lines of redundant setup code while maintaining full control and customization. Though currently in a dormant state (no recent commits), the project is actively documented through a comprehensive static site and live demo application, making it suitable for organizations standardizing HTTP client patterns across distributed .NET architectures.

**Created**: 2025-05-03
**Last Modified**: 2026-05-16

---

### #17. [WebSpark.PrismSpark](https://github.com/markhazleton/WebSpark.PrismSpark)

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

### #18. [TeachSpark](https://github.com/markhazleton/TeachSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 29910 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# TeachSpark Technical Summary

**TeachSpark** is an LLM-powered educational platform built with .NET 10 MVC that delivers personalized, adaptive learning experiences through AI-driven content customization. The application combines a modern C# backend leveraging Entity Framework Core and Clean Architecture principles with a sophisticated frontend build system using Webpack 5, featuring real-time asset optimization, hot module replacement, and automated code quality enforcement through ESLint, Prettier, and Stylelint. Key capabilities include intelligent curriculum delivery with AI-powered content adaptation, personalized learning pathways based on student behavior patterns, comprehensive progress analytics, and a fully responsive web experience with Bootstrap 5 styling and ES6+ JavaScript. The project employs enterprise-grade development tooling including Husky-managed Git hooks for pre-commit automation, lint-staged for efficient code quality checks on changed files only, and a comprehensive bundle analysis system to monitor frontend performance. TeachSpark stands out as a reference implementation demonstrating production-ready integration of Large Language Models into modern educational software, designed as a technical portfolio piece by Mark Hazleton to showcase full-stack architecture best practices across both .NET and Node.js ecosystems. The platform targets educators and learning institutions seeking intelligent, scalable alternatives to traditional static learning management systems, though currently the repository shows no active maintenance (0 commits in 365 days) despite strong technical scaffolding and a deployed live instance.

**Technology Stack Currency**: ✅ 90/100
**Dependencies**: 3 total (2 current, 1 outdated)

**Created**: 2025-06-19
**Last Modified**: 2026-05-15

---

### #19. [react-native-web-start](https://github.com/markhazleton/react-native-web-start)

Stars: 0 | Forks: 0 | Language: PowerShell | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2147 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: react-native-web-start

## Overview
React Native Web Start is a production-ready starter template designed to enable true cross-platform development by leveraging React Native Web, Vite, and TypeScript to build applications that run seamlessly across web, iOS, and Android platforms from a single codebase. The project serves as both a functional boilerplate and a comprehensive demonstration of enterprise-grade architecture patterns for cross-platform development, complete with a live demo deployed on GitHub Pages.

## Key Features & Capabilities
The template provides a complete development ecosystem featuring Vite-powered hot module replacement for rapid iteration, full TypeScript strict mode for type safety, responsive adaptive UI with Tailwind CSS and Sass preprocessing, production-ready HTTP clients with error handling, and an innovative in-app markdown documentation browser. It includes comprehensive build automation with asset management, monorepo structure organization (shared/web/mobile), testing infrastructure with Jest, and GitHub Pages deployment with automated CI/CD workflows.

## Technology Stack & Architecture
The project combines React Native 0.85.0 with React Native Web 0.21.2 for cross-platform compatibility, Vite 8.0.8 as the primary build tool, TypeScript 6.0.2 for strict type safety, and Metro for React Native bundling. The architecture employs a sophisticated monorepo structure separating shared components, web-specific, and mobile-specific configurations, enabling single-source-of-truth development while maintaining platform-specific optimizations. Styling leverages Tailwind CSS 4.2.2 with Sass 1.99.0 for enhanced CSS capabilities, and the stack includes Marked 17.0.6 for markdown processing and native Fetch API for HTTP communication.

## Current State & Project Maturity
The repository exhibits stale activity patterns with zero commits over the past 365 days despite its comprehensive initial setup, zero community engagement (0 stars, forks, contributors), and a concerning tech stack currency score of 50/100 indicating moderately outdated dependencies. However, the codebase is technically sophisticated with 50 dependencies properly configured and represents a complete, production-grade template rather than an incomplete proof-of-concept.

## Unique Value Proposition
This starter template distinguishes itself through its genuine cross-platform approach (not just code sharing), sophisticated build automation via custom PowerShell/Node.js scripts, integrated documentation browser demonstrating practical use of React Native's versatility, and emphasis on developer experience through modern tooling and strict TypeScript configuration. It serves enterprise developers and architects seeking to standardize cross-platform development rather than traditional mobile developers, offering architectural patterns and best practices for monorepo organization at scale.

## Considerations & Use Cases
The project is ideal for teams building customer-facing applications requiring web and mobile parity, enterprise development shops standardizing on React Native ecosystems, or developers learning cross-platform architecture patterns. However, the lack of active maintenance and community engagement suggests it should be evaluated for dependency currency before production deployment, though its comprehensive structure and configuration provide an excellent foundation for customization in long-term projects.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 50 total (50 current, 0 outdated)

**Created**: 2025-07-26
**Last Modified**: 2026-05-11

---

### #20. [TailwindSpark](https://github.com/markhazleton/TailwindSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 4114 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# TailwindSpark - Technical Summary

**TailwindSpark** is a production-ready React TypeScript monorepo that serves as both a comprehensive showcase and learning resource for modern web development patterns, specifically demonstrating Tailwind CSS 4's advanced features like the `@theme` directive and semantic design tokens. The project implements a scalable architecture using Turborepo with shared design token packages and reusable UI component libraries, maintaining strict code quality standards including 40% minimum test coverage, WCAG AA accessibility compliance, and automated CI/CD pipelines governed by formal project documentation. Built with React 19.1.1, TypeScript 5.9, and Tailwind CSS 4.1.18, the repository includes 27 key dependencies covering accessibility testing (@axe-core/react), form utilities, and web performance monitoring (web-vitals), while utilizing PowerShell and Shell scripts for build automation and Dependabot for continuous dependency management. The project stands out for its emphasis on production-grade governance through a documented constitution, comprehensive development history metrics, and active maintenance practices rather than typical open-source community contributions, making it an ideal reference implementation for enterprise-scale design system architecture and React best practices. TailwindSpark targets developers and architects seeking to understand modern design system implementation, scalable monorepo patterns, and how to build accessible, performant component libraries with TypeScript and Tailwind CSS in a professionally-maintained codebase.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2025-07-29
**Last Modified**: 2026-05-15

---

### #21. [MechanicsOfMotherhood](https://github.com/markhazleton/MechanicsOfMotherhood)

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

### #22. [Texecon](https://github.com/markhazleton/Texecon)

Stars: 0 | Forks: 0 | Language: TypeScript | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3811 KB | 🚀 0 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: Texecon Repository

**Texecon** is a static React application delivering expert economic analysis and commentary on the Texas economy, hosted as a GitHub Pages site with a custom domain (texecon.com). The project employs a sophisticated build pipeline that integrates headless CMS content from WebSpark API, featuring build-time content management, static site generation, and progressive enhancement—all optimized for SEO performance and Core Web Vitals. The technology stack centers on modern React 19 with TypeScript, Vite 7.1 for bundling, Tailwind CSS 4.1 for styling, and Radix UI/shadcn/ui for accessible component primitives, with client-side routing handled by Wouter for seamless user navigation. Its architecture distinguishes itself through a multi-stage build process that includes content fetching, XML sitemap generation, and post-build static page generation for dynamic routes, complemented by a comprehensive fallback system that gracefully degrades to cached content when API calls fail. The project demonstrates enterprise-grade development practices with type-safe content handling, cache busting strategies, build reports, and environment-based configuration—making it a technically mature demonstration of modern static site generation combined with dynamic content management. Target users include economic analysts, Texas business stakeholders, and researchers seeking reliable, SEO-optimized economic insights, while the repository itself serves as a technical portfolio piece showcasing modern web development patterns by Solutions Architect Mark Hazleton.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 37 total (37 current, 0 outdated)

**Created**: 2025-09-03
**Last Modified**: 2026-05-13

---

### #23. [git-spark](https://github.com/markhazleton/git-spark)

Stars: 0 | Forks: 0 | Language: PowerShell | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 2064 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Git Spark - Technical Summary

**Git Spark** is a comprehensive Git repository analytics and reporting tool that analyzes commit history to generate interactive HTML dashboards with visualizations of contributor activity, code change patterns, and development trends. The project provides both a command-line interface and Node.js API for flexible integration, supporting multiple export formats (HTML, JSON, CSV, Markdown) and advanced features like file-level analysis, contributor statistics, and customizable date-range filtering. Built with a modern tech stack combining TypeScript, PowerShell, and shell scripting, the tool leverages dependencies like Commander for CLI management, Ora for progress indicators, and Chalk for terminal styling, while delivering security-first HTML reports with strict Content Security Policy headers and embedded analytics (no external calls). The interactive reports include advanced visualizations such as multi-series timelines, contribution heatmaps, risk factor analysis, governance radar charts, dark mode support, and progressive table pagination—all designed for enterprise accessibility and air-gapped security review workflows. Git Spark targets development teams, solutions architects, and organizations seeking transparent insights into repository health and development patterns while maintaining complete honesty about Git data limitations. Despite having zero stars, forks, and recent commits (indicating early-stage/stale status), the project demonstrates high technical currency (95/100) and professional polish suitable for institutional code audits and governance-focused analytics.

**Technology Stack Currency**: ✅ 95/100
**Dependencies**: 22 total (19 current, 3 outdated)

**Created**: 2025-09-29
**Last Modified**: 2026-05-12

---

### #24. [github-stats-spark](https://github.com/markhazleton/github-stats-spark)

Stars: 0 | Forks: 0 | Language: Python | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 26398 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Analysis: github-stats-spark

## 🎯 Project Overview

**Stats Spark** is a sophisticated GitHub analytics and visualization platform designed to generate automated, beautiful SVG profile statistics and AI-powered repository analysis. It's a full-stack application combining Python backend services with a JavaScript-based interactive dashboard, hosted at `github-stats.makeboldspark.com`.

---

## 📊 Repository Health Assessment

| Metric | Status | Assessment |
|--------|--------|------------|
| **Stars/Forks** | 0/0 | Early-stage/private project |
| **Recent Activity** | Stale (0 commits in 90d & 365d) | ⚠️ Inactive development |
| **Repository Size** | 26.4 MB | Moderate codebase |
| **Tech Currency** | 79/100 | Well-maintained dependencies |
| **Code Maturity** | Production-Ready | Live service operational |

**⚠️ Key Concern**: Repository shows no commit activity in the past year despite having a live service, suggesting this may be a **completed/stable product** or the actual development occurs in a private repository.

---

## 🏗️ Architecture & Technology Stack

### Backend (Python 51.0%)
**Core Dependencies:**
- **PyGithub**: GitHub API client for data collection
- **PyYAML**: Configuration management
- **svgwrite**: SVG generation for profile statistics
- **requests**: HTTP client for API calls
- **beautifulsoup4**: HTML/data parsing

**Key Capabilities:**
- GitHub API integration with intelligent rate limiting
- SVG visualization generation (6 distinct visualization categories)
- AI-powered repository analysis (Claude Haiku integration implied)
- YAML-based configuration system
- CLI interface for local development

### Frontend (JavaScript 20.1% + HTML 1.0%)
**Architecture Pattern**: Mobile-first React-based dashboard
- **Chart.js + react-chartjs-2**: Interactive visualizations
- **IndexedDB/Dexie**: Offline data persistence (7-day cache)
- **Bottom Sheet Navigation**: Native mobile UI patterns
- **Responsive Design**: 320px-768px viewport optimization

### DevOps/Automation (PowerShell 18.8%)
- GitHub Actions workflows (automated Sunday midnight UTC updates)
- GitHub Pages deployment pipeline
- Lighthouse CI performance monitoring

### Styling (CSS 9.1%)
- WCAG 2.1 AA compliance
- Theme system (dark/light/custom)
- Mobile-optimized touch targets (44x44px minimum)

---

## 🌟 Core Features Deep Dive

### 1. **SVG Profile Statistics Generation**
```
6 Visualization Categories:
├── Overview Dashboard (Spark Score, activity patterns, metrics)
├── Commit Heatmap (GitHub-style calendar, intensity)
├── Language Statistics (tech stack breakdown)
├── Streaks & Consistency (current/longest streaks)
├── Fun Stats (8 personality-driven achievements)
└── Release Cadence (weekly/monthly activity sparklines)
```

**Spark Score Algorithm:**
- 40% Consistency (regular contribution patterns)
- 35% Volume (commit/activity count)
- 25% Collaboration (stars, forks, community metrics)
- Result: 0-100 scale + 1-5 lightning rating

### 2. **AI-Powered Repository Analysis**
**Intelligent Ranking (Composite Algorithm):**
- 30% Popularity: Stars/forks (community engagement)
- 45% Activity: Recent commits with time-decay windows (90d/180d/365d)
- 25% Health: Documentation, licensing, maintenance signals

**AI Summaries:** Claude Haiku generates 4-6 sentence technical descriptions with 97%+ success rate, covering:
- Purpose and functionality
- Key technologies/frameworks
- Architectural patterns
- Unique attributes
- Target audience

**Schema 2.3.0 Enhancements:**
- Attention scoring (PR backlog, security alerts, staleness)
- Dependency coverage tracking (known versions, registry resolution)
- Diagnostics and maintenance signals
- Screenshot auditing capabilities

### 3. **Interactive Mobile-First Dashboard**
**Performance Metrics:**
- Target: <2s First Contentful Paint (Lighthouse CI)
- 0.9+ Lighthouse performance score
- Handles up to 500 repositories in <5 minutes

**Mobile UX Features:**
- Touch-optimized interactions (swipe gestures, swipe-to-delete)
- Bottom sheet navigation patterns
- Responsive layouts across 320px-768px viewports
- "Needs Attention" ranking view (security alerts + PR backlog + dependency drift)

**Data Management:**
- Offline support via IndexedDB/Dexie
- CSV/JSON export functionality
- Smart caching with intelligent API optimization

---

## 🔧 Technical Implementation Details

### Configuration Management
- **YAML-based**: Flexible, version-controlled configuration
- **Extensible Architecture**: Modular design for customization
- **Theme Customization**: Dark/light/custom with accessibility compliance

### API Integration & Resilience
- **Smart Caching**: Reduces API calls intelligently
- **Rate Limit Handling**: Automatic retry with exponential backoff
- **Graceful Degradation**: Maintains functionality under API constraints

### Deployment Strategy
- **GitHub Actions**: Automated weekly updates (Sunday, midnight UTC)
- **GitHub Pages**: Static site hosting with auto-updates
- **Zero Maintenance**: Set once, updates automatically

### Data Pipeline
```
GitHub API → Python Processing → SVG Generation + AI Analysis
                ↓
        Configuration (YAML)
                ↓
        Interactive Dashboard (React/JS)
                ↓
    GitHub Pages / Web Hosting
```

---

## 📈 Use Cases & Target Audience

1. **Individual Developers**: Showcase GitHub activity professionally
2. **Development Teams**: Repository health analysis and contribution tracking
3. **Technical Leaders**: Developer productivity metrics and technology stack analysis
4. **Open Source Maintainers**: Project momentum and community engagement tracking

---

## ⚠️ Quality & Maintenance Observations

### Strengths ✅
- **Production-Ready**: Live service operational
- **Modern Stack**: Current Python (3.11+) and JavaScript frameworks
- **Accessibility**: WCAG 2

**Technology Stack Currency**: ✅ 79/100
**Dependencies**: 12 total (5 current, 7 outdated)

**Created**: 2025-12-28
**Last Modified**: 2026-05-14

---

### #25. [markhazleton.github.io](https://github.com/markhazleton/markhazleton.github.io)

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

### #26. [MuseumSpark](https://github.com/markhazleton/MuseumSpark)

Stars: 0 | Forks: 0 | Language: Python | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 26764 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# MuseumSpark - Technical Summary

**MuseumSpark** is an intelligent museum discovery and travel planning platform designed to help art enthusiasts strategically plan museum visits across North America. Built upon the Walker Art Center Reciprocal Program membership list of 1,269 museums, the project transforms a static directory into a data-rich, intelligently-ranked resource by implementing a sophisticated multi-phase enrichment pipeline that combines structured data from Wikidata, Wikipedia, official museum websites, and expert scoring to provide priority rankings based on artistic collections, historical significance, and travel logistics.

The platform features a modern React 19 + Vite frontend with Tailwind CSS styling deployed via GitHub Pages, offering comprehensive museum browsing with search, filtering, and detailed museum profiles alongside a real-time data quality dashboard. The technical architecture emphasizes data validation and quality assurance through JSON Schema validation, Pydantic-based data models, and automated scraping infrastructure (BeautifulSoup4, html2text) that processes external data sources while enforcing a strict "never replace known with null" principle to maintain data integrity.

The project employs a phased development strategy with clear milestones: Phase 0-1 (currently 80% complete) focuses on data foundation and enrichment infrastructure; Phase 2 (Q2 2026) will implement expert-driven collection scoring; Phase 2.5-3 (Q3 2026) will leverage LLM agents for automated content analysis and validation; and Phase 4 (Q4 2026) will transform the static site into a full-stack interactive platform with FastAPI backend, user authentication, and AI-powered personalized itinerary generation. Despite showing zero recent activity and minimal enrichment progress (0.08% complete), the repository demonstrates ambitious architectural planning with clear separation of concerns between frontend (Node/React), data pipeline (Python scripts), and future backend components, making it a technically sophisticated demonstration project intended to showcase solutions architecture capabilities.

**Created**: 2026-01-15
**Last Modified**: 2026-05-14

---

### #27. [SupportSpark](https://github.com/markhazleton/SupportSpark)

Stars: 0 | Forks: 0 | Language: PowerShell | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 1756 KB | 🚀 0 commits/month

**Quality**: ❌ License | ❌ Docs

# SupportSpark - Technical Summary

**SupportSpark** is a compassionate support network platform designed to help individuals share life journey updates with trusted circles during challenging moments, built as a full-stack TypeScript application demonstrating modern web architecture patterns. The platform implements a role-based access model where members create and manage journey conversations while supporters receive invitations to read updates and provide threaded feedback, eliminating the burden of individually notifying multiple contacts. The technology stack combines React 19 with Vite for the frontend, Express 5 for the backend, and Tailwind CSS 4 for a calm, accessible UI built on Radix primitives and shadcn/ui components, with end-to-end type safety enforced through TypeScript strict mode and Zod runtime validation.

The architecture demonstrates several noteworthy patterns including invitation-only network isolation, session-based authentication via Passport.js, TanStack React Query for server state management, and a localStorage-backed static build option that enables the GitHub Pages deployment to function entirely client-side. The project is uniquely designed for Windows IIS deployment in production (via iisnode), with automated PowerShell deployment scripts, while also supporting development workflows on any Node.js 18+ environment with npm. Target users are individuals navigating health challenges, life transitions, or personal journeys who need a distraction-free, purpose-built communication platform, and supporters who want organized, threaded access to meaningful updates without scattered messaging fatigue.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 97 total (97 current, 0 outdated)

**Created**: 2026-02-01
**Last Modified**: 2026-05-14

---

### #28. [DocSpecSpark](https://github.com/markhazleton/DocSpecSpark)

Stars: 0 | Forks: 0 | Language: Python | 0 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 223 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# DocSpecSpark Technical Summary

DocSpecSpark is an AI-native documentation framework that provides a structured, repeatable workflow for creating, reviewing, and publishing documentation systems through markdown-based prompts and lightweight automation tooling. The core product consists of 21 document workflow prompts and helper templates designed to guide AI assistants (Copilot, Claude, Cursor) through a systematic documentation process, with an optional Python CLI for automated bootstrap installation into target repositories. The architecture follows a clean separation-of-concerns model with framework-managed stock assets in `.docspark/` and user-owned artifacts in `.documentation/`, implementing a configurable prompt resolution hierarchy that supports customization by git user, global overrides, and framework defaults. Key capabilities include core workflows (constitution, specification, planning, implementation, publishing), constitution-powered workflows (PR reviews, site audits, release management), quality assurance features (clarification, analysis, checklists), and publication scaffolding with mkdocs and GitHub Pages templates. Built with Python (94%), leveraging the `typer` CLI framework and `rich` for terminal output, the project targets AI-assisted documentation teams and technical writers seeking AI-driven workflows that maintain human control through markdown-first prompts rather than opaque automation. What distinguishes DocSpecSpark is its human-centric approach to AI tooling—rather than replacing developer judgment, it provides AI assistants with explicit constitutional guidelines and repeatable patterns, making it particularly valuable for documentation-heavy projects, architecture decision records, and specification-driven development where audit trails and evolution tracking are critical.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 2 total (0 current, 2 outdated)

**Created**: 2026-03-07
**Last Modified**: 2026-05-11

---

### #29. [devspark](https://github.com/markhazleton/devspark)

Stars: 0 | Forks: 0 | Language: Python | 0 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 6770 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# DevSpark Technical Summary

**DevSpark** is a structured development workflow framework designed to integrate AI coding assistants (Claude, Copilot, Cursor, Gemini, and 13+ others) into repeatable engineering processes—delivering capabilities through 28 markdown-based slash commands rather than installed software or subscriptions. The system provides three flagship workflows (`create-spec`, `execute-plan`, `suggest-improvement`) that guide users from requirements specification through PR review and release, with each command being a discrete prompt file that agents can execute to gather context, analyze code, generate documentation, or perform constitution-based quality reviews. Built on a Python CLI foundation (with PowerShell and Bash helper scripts), DevSpark includes a declarative harness runtime for workflow automation, optional schema validation via Pydantic and JSON Schema, and support for multi-app monorepo registries—enabling teams to establish project "constitutions" (principles and guidelines) that inform all downstream QA, PR reviews, and refactoring decisions. The architecture prioritizes accessibility by making core functionality available through simple markdown copy-paste (no installation required), while offering an optional advanced CLI for teams needing programmatic workflow execution, environment validation, and structured artifact logging. Key design strengths include constitutional code review automation, adversarial risk analysis (`/devspark.critic`), knowledge-preserving cleanup workflows (`/devspark.harvest`), and commit-history-based narrative generation—making it particularly valuable for teams standardizing AI-assisted development without infrastructure lock-in or dependency burden.

**Technology Stack Currency**: ✅ 76/100
**Dependencies**: 5 total (1 current, 4 outdated)

**Created**: 2026-04-02
**Last Modified**: 2026-05-16

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

- **Generation Time**: 4.4 seconds
- **SVGs Generated**: 6/6
- **Total API Calls**: 0
- **Total AI Tokens**: 73,495
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
*Last updated: 2026-05-17*

## Screenshot Audit

- Repositories with websites: 22
- Screenshots present: 5
- Flagged repositories: 17

### Likely 404 Pages

- UISampleSpark: https://ui.makeboldspark.com (status: 403, title: Just a moment...)
- WebProjectMechanics: https://wpm.makeboldspark.com (status: 403, title: Just a moment...)
- WebSpark.ArtSpark: https://art.makeboldspark.com (status: 403, title: Just a moment...)
- WebSpark.Bootswatch: https://bootswatch.makeboldspark.com/ (status: 403, title: Just a moment...)
- BootstrapSpark: https://bootstrap.makeboldspark.com/ (status: 403, title: Just a moment...)
- WebSpark.PrismSpark: https://prism.makeboldspark.com (status: 403, title: Just a moment...)
- TeachSpark: https://teach.makeboldspark.com (status: 403, title: Just a moment...)
- ApiSpark: https://makeboldspark.com (status: 403, title: Just a moment...)

### Missing Screenshots

- UISampleSpark: https://ui.makeboldspark.com
- KeyPressCounter: http://keypresscounter.makeboldspark.com/
- WebProjectMechanics: https://wpm.makeboldspark.com
- WebSpark.ArtSpark: https://art.makeboldspark.com
- WebSpark.Bootswatch: https://bootswatch.makeboldspark.com/
- BootstrapSpark: https://bootstrap.makeboldspark.com/
- WebSpark.HttpClientUtility: http://httpclientutility.makeboldspark.com/
- WebSpark.PrismSpark: https://prism.makeboldspark.com
- TeachSpark: https://teach.makeboldspark.com
- TailwindSpark: http://tailwind.makeboldspark.com/
- MechanicsOfMotherhood: http://mechanicsofmotherhood.com/
- Texecon: https://texecon.com
- MuseumSpark: https://markhazleton.github.io/MuseumSpark/
- SupportSpark: http://support.makeboldspark.com/
- DocSpecSpark: https://markhazleton.github.io/DocSpecSpark/
- ApiSpark: https://makeboldspark.com
- PHPDocSpark: https://phpdocspark.azurewebsites.net
