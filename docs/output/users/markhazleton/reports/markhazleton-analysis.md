# GitHub Profile: markhazleton

**Generated**: 2026-05-14 12:06:37 UTC
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

👥 0 contributors | 🌐 6 languages | 💾 31212 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: UISampleSpark

**UISampleSpark** is an educational ASP.NET Core reference application that demonstrates how to implement the same Employee/Department CRUD domain across seven distinct front-end UI patterns—MVC, Razor Pages, jQuery AJAX, React, Vue, htmx, and Blazor—within a single .NET 10 application. The project showcases modern web architecture practices including clean layering (UI/Core/Data), dependency injection, repository patterns, REST/OpenAPI APIs, dynamic Bootstrap theming via Bootswatch, and containerization with Docker. Built on Entity Framework Core with an in-memory database, the application includes comprehensive CI/CD pipelines using GitHub Actions, unit test coverage across domain and data layers, and observability features like Application Insights health checks and Swagger documentation. The architecture employs abstraction layers such as `IEmployeeService` and `IHttpRequestResultService`, allowing developers to compare UI framework tradeoffs—from server-rendered approaches (MVC, Razor Pages, Blazor) to client-side SPAs (React, Vue)—while maintaining consistent backend services and validation logic. This makes UISampleSpark particularly valuable for architects and senior developers evaluating UI technology choices, teaching modern .NET patterns, or establishing reference implementations for enterprise web applications. The project's evolution from .NET 5 through .NET 10, coupled with its active deployment pipeline and Docker Hub integration, demonstrates production-ready DevOps practices and long-term maintainability.

**Created**: 2019-04-25
**Last Modified**: 2026-05-13

---

### #2. [FastEndpointApi](https://github.com/markhazleton/FastEndpointApi)

Stars: 3 | Forks: 1 | Language: HTML | 0 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 153 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: FastEndpointApi Repository

This repository is a comprehensive educational demonstration and reference implementation of the **FastEndpoints framework** for ASP.NET Core, showcasing the REPR (Request-Endpoint-Response) architectural pattern through a fully functional Person Management API. The project implements a complete CRUD application with advanced features including HATEOAS hypermedia links, Swagger/OpenAPI documentation, in-memory data persistence, and a clean service layer architecture, all built on .NET 10 with FastEndpoints 7.1.1 as the core framework. The tech stack includes Bogus for test data generation, Bootstrap 5.3.3 for frontend UI, and GitHub Actions with Azure Web Apps for CI/CD deployment, demonstrating production-ready practices alongside clean code principles. FastEndpoints itself is positioned as a lightweight, developer-friendly alternative to traditional MVC Controllers and Minimal APIs, providing significant boilerplate reduction while maintaining high performance through its opinionated, convention-based approach to API development. The repository uniquely combines multiple layers of documentation—including an interactive live demo site, comprehensive README with detailed walkthroughs, static HTML sample pages with JavaScript interactivity, Swagger UI, and a linked article—making it an exceptional learning resource for developers seeking to understand modern ASP.NET Core API patterns and FastEndpoints best practices. This project is primarily intended for ASP.NET Core developers, architects, and technical decision-makers evaluating FastEndpoints for production applications, offering both theoretical understanding through documentation and practical implementation examples they can immediately adapt for their own projects.

**Created**: 2024-04-06
**Last Modified**: 2026-05-12

---

### #3. [RequestSpark](https://github.com/markhazleton/RequestSpark)

Stars: 2 | Forks: 1 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 966 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# RequestSpark - Technical Summary

RequestSpark is a comprehensive .NET 10 (LTS) web application and console tool designed for executing REST API tests, performance benchmarking, and regression testing against Postman collections. The solution provides a browser-based dashboard built with Razor Pages that enables users to manage API configurations, execute test runs, and analyze detailed performance metrics including response time percentiles, success rates, and load testing capabilities. The architecture leverages a modular project structure with separate Domain, PostmanImport, and Web layers (RequestSpark.Domain, RequestSpark.PostmanImport, RequestSpark.Web), supported by comprehensive test coverage (21 tests, 100% pass rate) using MSTest v4 with integrated code quality analyzers. Key technical differentiators include native Postman collection integration for seamless test migration, built-in CSV export functionality for results analysis, a sample CRUD API for demonstration purposes, and significant performance optimizations—19% faster builds (5.1s → 4.1s) and 25% faster test execution (0.8s → 0.6s) following the recent .NET 10 upgrade. The project maintains high code quality standards with 93% of NuGet packages at latest versions, zero security vulnerabilities, and elimination of deprecated framework-included packages, making it suitable for enterprises and development teams needing automated API testing, performance regression detection, and load testing capabilities without external dependencies. The solution is actively maintained by Mark Hazleton with a live demonstration instance at request.makeboldspark.com, though current activity is stale (90+ days without commits).

**Created**: 2021-09-30
**Last Modified**: 2026-05-11

---

### #4. [KeyPressCounter](https://github.com/markhazleton/KeyPressCounter)

Stars: 2 | Forks: 1 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 2 languages | 💾 46631 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: KeyPressCounter

**KeyPressCounter** is a lightweight Windows system tray utility written in C# (.NET 10.0) that monitors keyboard and mouse input activity while simultaneously tracking real-time system performance metrics. The application uses SharpHook for global input event hooking, Windows Performance Counters via System.Management for hardware telemetry, and User32 P/Invoke calls for idle-time detection—all without recording keystrokes or transmitting any data externally. The architecture employs a thread-safe `Counter` class with lock-protected increments, background timers for periodic logging, and a three-tab WinForms dashboard featuring live CPU/memory gauges, 60-second rolling graphs, top-process monitoring, and configurable activity thresholds to filter idle periods.

The application is designed for productivity tracking and system awareness, targeting users who want passive behavioral analytics and performance insights without privacy concerns. It logs statistics at configurable intervals (default 60 seconds) to JSON configuration and daily summaries, supports Windows startup registration, and provides quick-access launchers for system tools like Task Manager and Resource Monitor. However, the project shows signs of staleness with zero commits in the past 90-365 days, a moderate tech-stack currency score of 57/100, and minimal community engagement (2 stars, 1 fork, 0 contributors), suggesting it may serve primarily as a personal utility rather than an actively maintained community project.

**Technology Stack Currency**: ✅ 57/100
**Dependencies**: 4 total (3 current, 1 outdated)

**Created**: 2024-03-07
**Last Modified**: 2026-05-12

---

### #5. [WebSpark](https://github.com/markhazleton/WebSpark)

Stars: 1 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 8 languages | 💾 69582 KB | 🚀 0 commits/month

**Quality**: ❌ License | ❌ Docs

# WebSpark Technical Summary

**WebSpark** is a comprehensive .NET 9 suite of modular ASP.NET Core MVC web applications demonstrating modern architecture patterns, with a primary focus on AI-driven tools and spec-driven development practices. The platform comprises seven integrated areas (PromptSpark for LLM prompt optimization, RecipeSpark for recipe management, TriviaSpark for quiz creation, WebCMS for content management, AsyncSpark, Admin, and Identity modules), each designed as independent, reusable components. Core technologies include ASP.NET Core MVC, Bootstrap 5, Semantic Kernel/OpenAI integration for AI capabilities, SignalR for real-time communication, and a robust SEO optimization layer featuring dynamic meta tags, JSON-LD structured data, canonical URL management, and comprehensive analytics integration with Google Analytics 4 and Application Insights.

The repository is distinguished by its rigorous **SpecKit spec-driven development workflow**, which enforces structured feature development through automated commands (`/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.critic`, `/speckit.implement`, `/speckit.review`) that create comprehensive specifications, implementation plans, task breakdowns, and notably, an adversarial risk assessment process that identifies showstopper issues, security vulnerabilities, and performance killers before code execution begins. WebSpark serves as both a production application (live at web.makeboldspark.com) and a comprehensive reference architecture for building scalable, maintainable enterprise web solutions, making it ideal for technical professionals, architects, and development teams seeking to implement modern .NET practices, AI integration patterns, and disciplined software delivery methodologies.

**Created**: 2024-01-11
**Last Modified**: 2026-05-11

---

### #6. [WebProjectMechanics](https://github.com/markhazleton/WebProjectMechanics)

Stars: 3 | Forks: 0 | Language: Visual Basic .NET | 0 commits (90d)

👥 0 contributors | 🌐 10 languages | 💾 52587 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebProjectMechanics

**WebProjectMechanics** is a multi-tenant, multi-domain content management system designed to serve 36+ websites from a single ASP.NET Core 9 application instance, with a distinctive architecture that publishes all public content as pre-rendered static HTML served by Caddy. The project represents a greenfield modernization effort, migrating a 20+ year legacy ASP.NET Web Forms/MS Access system to contemporary cloud-native technologies (.NET 9, SQLite, and containerized infrastructure), while maintaining production continuity. The system employs a plugin-based domain architecture with independent SQLite databases per site (avoiding TenantId anti-patterns), enabling true data isolation and scalability on minimal infrastructure (~$10/month Azure Linux VM). Key technologies include ASP.NET Core Minimal APIs for the REST backend, Entity Framework Core 9 for ORM, Scriban for template rendering, and Caddy 2 as a reverse proxy with automatic SSL and static file serving. The unique "publish-to-static" approach significantly reduces runtime database load and improves security by pre-rendering content, making it ideal for content-heavy, multi-site operations with predictable traffic patterns. This architecture is particularly valuable for organizations managing numerous independent websites where per-domain data isolation, cost efficiency, and operational simplicity are critical requirements.

**Created**: 2017-09-19
**Last Modified**: 2026-05-14

---

### #7. [AsyncSpark](https://github.com/markhazleton/AsyncSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 1950 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# AsyncSpark Technical Summary

AsyncSpark is a production-ready reference implementation demonstrating enterprise-grade async/await patterns in .NET 10, built by Mark Hazleton as part of the Make Bold Spark portfolio. The project showcases eight core async patterns including ConfigureAwait(false) usage, CancellationToken threading, Task.WhenAll parallelization, SemaphoreSlim throttling, Polly resilience policies, decorator pattern implementation, fire-and-forget safety, and elimination of blocking calls—each with accompanying unit tests and live API demonstrations.

The repository implements **constitution-driven development**, a formalized governance approach that enforces architectural standards through automated compliance auditing, 80% code coverage requirements in CI/CD pipelines, and interactive pull request reviews. Built on modern .NET 10 features (nullable reference types, implicit usings, file-scoped namespaces, primary constructors), the codebase is organized into a modular structure spanning core async utilities, an ASP.NET Core web application with interactive Scalar-powered API documentation, weather service integrations, comprehensive test suites using MSTest and Moq, and console demonstrations.

The project is distinguished by its clean architecture principles—dependency injection, interface-based design, and decorator pattern for cross-cutting concerns—combined with resilience patterns via WebSpark.HttpClientUtility and structured logging with ILogger<T>. AsyncSpark targets intermediate-to-advanced .NET developers and architects seeking production-ready patterns and best practices, offering both conceptual learning through well-documented code examples and practical experience via a live web application deployed to Azure with real OpenWeatherMap API integration, comprehensive health checks, and an interactive API explorer supporting dark/light modes and live request testing.

**Created**: 2022-08-07
**Last Modified**: 2026-05-11

---

### #8. [DataSpark](https://github.com/markhazleton/DataSpark)

Stars: 0 | Forks: 0 | Language: HTML | 0 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 2089 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# DataSpark Technical Summary

DataSpark is a comprehensive .NET 10 toolkit designed for SQLite database analysis and code generation, offering both CLI and ASP.NET Core MVC web interfaces for database discovery, inspection, CSV export, and automated C# DTO generation. The project follows a modular architecture with separated concerns across five components—a console application, core library, web UI, test suite, and performance benchmarks—enabling flexible deployment and reusability across different consumption patterns. Built with modern .NET technologies including Entity Framework integration for database access and BenchmarkDotNet for performance validation, it provides enterprise-grade features such as schema reporting in multiple formats (text, JSON, Markdown), batch table exports, persistent file management, and intelligent code generation with customizable namespacing. The solution demonstrates best practices through comprehensive test coverage (with CI/CD via GitHub Actions), a professional web interface for non-technical users, and a powerful CLI for automation and scripting scenarios, making it suitable for database administrators, developers migrating legacy systems, and organizations requiring bulk DTO generation from SQLite schemas. Despite its stale repository status (no activity in 90 days), the live deployment at data.makeboldspark.com and MIT licensing position it as a practical reference implementation and potentially usable tool for SQLite database tooling workflows.

**Created**: 2017-11-06
**Last Modified**: 2026-05-12

---

### #9. [markhazleton](https://github.com/markhazleton/markhazleton)

Stars: 0 | Forks: 0 | Language: Unknown | 0 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 6624 KB | 🚀 0 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: markhazleton GitHub Profile

This is a personal GitHub profile repository serving as a portfolio and learning archive for Mark Hazleton, a .NET and Azure engineer specializing in modern web application development and developer tooling. The repository functions as a centralized hub showcasing featured projects including WebSpark (a comprehensive web application platform), ReactSpark (a Vite-based React application on Azure Static Web Apps), TailwindSpark (an opinionated UI framework for rapid consistent interface development), and UISampleSpark (a containerized UI demonstration available on Docker Hub). The technology stack emphasizes modern cloud-native development with .NET backends, React frontends, Tailwind CSS for styling, and Azure cloud services for deployment, complemented by DevOps tooling like Docker containerization and CLI utilities. The repository demonstrates a design philosophy centered on lifelong learning and continuous knowledge acquisition, with thoughtfully documented articles covering topics ranging from observability and analytics design patterns to AI confidence assessment and secure infrastructure deployment on Windows VMs with Cloudflare. This portfolio is particularly valuable for developers seeking mentorship on full-stack .NET/Azure architectures, cloud deployment strategies, and thoughtful engineering practices, while the curated collection of learning projects and published technical articles establishes credibility in enterprise web development, developer experience design, and infrastructure automation.

**Created**: 2021-04-17
**Last Modified**: 2026-05-12

---

### #10. [WebSpark.ArtSpark](https://github.com/markhazleton/WebSpark.ArtSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3894 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# WebSpark.ArtSpark - Technical Summary

**WebSpark.ArtSpark** is a comprehensive .NET 10.0 solution that provides complete programmatic access to the Art Institute of Chicago's public API through a full-featured client library, AI-powered chat system with multiple contextual personas, and interactive demo applications. The solution encompasses four interconnected projects: a strongly-typed API client library covering all 33 endpoints across six major categories, an AI agent system leveraging Semantic Kernel and OpenAI's GPT-4o models for conversational artwork analysis with hot-reloadable prompt templates, a responsive ASP.NET Core web application with user authentication and personal collections, and a console utility for developer testing. The architecture emphasizes modern .NET patterns including async/await patterns, System.Text.Json deserialization with custom naming policies, IIIF image URL construction for high-resolution artwork access, and Elasticsearch-integrated search capabilities, while maintaining minimal external dependencies. Notable for its innovative AI integration, the solution features multiple conversation personas (Artwork, Artist, Curator, Historian) with persistent chat history, OpenAI Vision capabilities for image analysis, and developer-friendly externalized prompt configuration without requiring code recompilation. The project targets .NET developers, museum technologists, and AI enthusiasts seeking to build applications around cultural collections, demonstrated by its live deployment at Art.makeboldspark.com, though the repository currently shows signs of inactivity (no commits in 90+ days) despite its polished documentation and comprehensive feature set.

**Created**: 2023-01-30
**Last Modified**: 2026-05-13

---

### #11. [WebSpark.Bootswatch](https://github.com/markhazleton/WebSpark.Bootswatch)

Stars: 0 | Forks: 0 | Language: HTML | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7144 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.Bootswatch

**WebSpark.Bootswatch** is a .NET 10 Razor Class Library that seamlessly integrates Bootswatch themes into ASP.NET Core applications, providing developers with a comprehensive theming solution built on Bootstrap 5. The library offers dynamic theme switching, light/dark mode support, responsive design, and built-in caching mechanisms through its `StyleCache` service, with tag helper support for easy UI integration via components like `<bootswatch-theme-switcher />`. Built primarily in HTML (63.8%), C# (28.6%), and supplemented by PowerShell, JavaScript, and CSS, the project leverages modern .NET dependencies (Microsoft.Extensions.* packages 10.0.1+) and the latest framework features, deliberately targeting .NET 10 exclusively to prioritize security patches, performance improvements, and simplified maintenance over broad legacy framework compatibility. The architecture demonstrates production-ready design patterns including dependency injection, comprehensive error handling, fallback mechanisms, and full IntelliSense support with XML documentation, making it suitable for enterprises and developers building modern ASP.NET Core applications requiring professional theme management. While the project shows zero activity over the past 90 days and has no external contributors, it serves as a well-documented technical demonstration within the Make Bold Spark portfolio, with a live reference implementation at bootswatch.makeboldspark.com and published NuGet packages for community adoption.

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

**InquirySpark** is a modern ASP.NET Core MVC survey and decision-management system built on .NET 10 that unifies inquiry operations, capability tracking, and operational readiness monitoring through a single web application. The system leverages a clean layered architecture with Entity Framework Core 10 for data access, read-only SQLite databases for immutable domain data, and ASP.NET Core Identity for authentication, backed by a rich frontend using Bootstrap 5, DataTables 2.3.5, and Razor views organized within a unified authenticated area. Key architectural strengths include strict nullable reference type enforcement, comprehensive XML documentation, structured logging via a custom audit service abstraction, and a standardized response pattern (`BaseResponse<T>`) across all service boundaries, enabling maintainable and predictable API contracts throughout the codebase. The project is notable for its focus on **immutability and read-only persistence** — the primary inquiry database operates in read-only SQLite mode while supporting a separate read-write Identity store, eliminating traditional migration complexity and providing data integrity guarantees. InquirySpark serves as a technical demonstration portfolio piece targeting architects and developers seeking reference implementations of modern .NET practices, including capability-driven feature delivery, operational health dashboards, and cutover management workflows for complex system transitions.

**Created**: 2023-10-24
**Last Modified**: 2026-05-11

---

### #14. [BootstrapSpark](https://github.com/markhazleton/BootstrapSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 0 commits (90d)

👥 0 contributors | 🌐 7 languages | 💾 38193 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# BootstrapSpark - Technical Summary

**BootstrapSpark** is an enterprise-grade portfolio web application that showcases modern React development practices, deployed as a serverless, cloud-native solution on Azure Static Web Apps. The project demonstrates a comprehensive full-stack architecture combining a React 19 + TypeScript frontend with Azure Functions backend services, featuring real-time capabilities through SignalR integration, interactive weather widgets, RSS feed aggregation, and dynamic project showcase functionality pulled from external APIs. The codebase emphasizes production-ready patterns including strict TypeScript typing, accessibility compliance (WCAG 2.1 AA), responsive design with Bootstrap 5, performance optimization through Vite's code splitting and lazy loading, and automated CI/CD pipelines via GitHub Actions. The technology stack is deliberately modern yet stable—leveraging Vite for lightning-fast builds, React Router for client-side navigation, Context API for state management, and a strategic separation of concerns between frontend presentation and backend API services. The project is notable for its dual-deployment strategy (Azure Static Web Apps + GitHub Pages), deliberate Content Security Policy (CSP) configuration to support cross-origin content loading, and comprehensive documentation covering security, deployment, and architectural decisions. **Target audience**: developers seeking a reference implementation of scalable React applications, cloud-native architecture patterns, or a sophisticated portfolio template; maintained by Mark Hazleton as part of the MakeBoldSpark technical demonstrations portfolio.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 47 total (47 current, 0 outdated)

**Created**: 2024-10-11
**Last Modified**: 2026-05-13

---

### #15. [PromptSpark.Chat](https://github.com/markhazleton/PromptSpark.Chat)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 19453 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: PromptSpark.Chat

**PromptSpark.Chat** is a real-time conversational workflow application built on ASP.NET Core that guides users through structured multi-step processes using adaptive cards and SignalR for bidirectional communication. The application enables dynamic workflow execution with branching logic, interactive UI elements powered by Microsoft Adaptive Cards, and optional AI integration (via chat completion services) to handle questions beyond predefined workflows. The architecture employs server-side conversation state persistence using thread-safe `ConcurrentDictionary` for continuity across page refreshes, minimal concurrency overhead, and flexible workflow definitions via JSON configuration files, allowing workflows to be easily customized without code changes. Built with a modern tech stack including C# (31.4%), SCSS (29.9%), HTML (28.5%), and JavaScript (9.1%), the application demonstrates responsive frontend design paired with backend real-time capabilities, making it suitable for guided customer interactions, onboarding flows, multi-step form processing, and intelligent chatbot scenarios. The project is positioned as a technical demonstration within the Make Bold Spark portfolio, authored by Mark Hazleton, and provides a practical example of integrating SignalR, Adaptive Cards, and optional AI services within an ASP.NET Core framework—though notably the repository shows no recent activity and zero stars, suggesting it may be early-stage or primarily for educational purposes.

**Created**: 2024-12-31
**Last Modified**: 2026-05-11

---

### #16. [WebSpark.HttpClientUtility](https://github.com/markhazleton/WebSpark.HttpClientUtility)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 3122 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.HttpClientUtility

**WebSpark.HttpClientUtility** is an enterprise-grade HTTP client wrapper library for .NET 8-10 LTS that abstracts away boilerplate HttpClient configuration by providing integrated resilience patterns (Polly), intelligent response caching, structured logging with correlation IDs, and OpenTelemetry observability—all configurable through a single `AddHttpClientUtility()` dependency injection call. The library is delivered as two focused NuGet packages: the core utility package (163 KB) for standard HTTP operations and a companion Crawler package (75 KB) for web scraping with robots.txt parsing and sitemap generation. Built with production-grade standards including comprehensive automated test coverage across .NET versions, Source Link debugging support, Native AOT and trimming compatibility, and strict semantic versioning guarantees, it targets microservices architects and backend developers who want to eliminate 50+ lines of manual HttpClient setup code while maintaining battle-tested reliability patterns. The project demonstrates modern .NET practices through zero-warning builds, package validation for breaking change detection, and CI/CD integration via GitHub Actions, though the repository itself shows no recent activity (stale for 90+ days) despite being MIT-licensed and backed by comprehensive documentation at a live reference site.

**Created**: 2025-05-03
**Last Modified**: 2026-05-13

---

### #17. [WebSpark.PrismSpark](https://github.com/markhazleton/WebSpark.PrismSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 2280 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: WebSpark.PrismSpark

**WebSpark.PrismSpark** is a modern C#/.NET 10.0 port of the popular PrismJS syntax highlighting library, designed to provide advanced code highlighting, theming, and extensibility capabilities for .NET web applications. The project delivers comprehensive tokenization and syntax highlighting support for 24 programming languages (including C#, JavaScript, Python, Rust, Go, and markup languages), coupled with a plugin architecture that enables features like line numbers, copy-to-clipboard functionality, and custom toolbars. Built with a layered architecture, the library leverages ASP.NET Core MVC integration, async/caching APIs, an extensible hook system, and a theming engine that supports both built-in and custom themes with CSS generation, making it suitable for enterprise web applications requiring sophisticated code display capabilities.

The implementation emphasizes performance through asynchronous processing and intelligent caching mechanisms, while the comprehensive test suite (52 MSTest tests) validates grammar, tokenization, and integration workflows across all supported languages. Key architectural patterns include dependency injection for service registration, a plugin/hook system for event-driven customization, and separation of concerns with dedicated highlighter implementations (HtmlHighlighter, EnhancedHtmlHighlighter, ThemedHtmlHighlighter). This project is particularly valuable for ASP.NET Core developers, documentation platforms, educational tools, code review systems, and any .NET-based application requiring production-grade syntax highlighting with minimal external JavaScript dependencies—offering a performant server-side alternative to client-side highlighting solutions while maintaining full feature parity with its PrismJS inspiration.

**Created**: 2025-05-27
**Last Modified**: 2026-05-12

---

### #18. [TeachSpark](https://github.com/markhazleton/TeachSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 29994 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# TeachSpark: Technical Summary

**TeachSpark** is an LLM-powered educational platform built with .NET 10 MVC and a modern JavaScript frontend, designed to deliver personalized, adaptive learning experiences through AI-driven content delivery. The project combines a C# backend leveraging Entity Framework Core with a sophisticated webpack-based frontend build system featuring hot module replacement, code splitting, and automated asset optimization, demonstrating enterprise-grade development practices. Key architectural features include Clean Architecture principles on the backend, responsive Bootstrap 5 styling through a managed SCSS pipeline, and comprehensive code quality automation via ESLint, Prettier, Stylelint, Husky, and lint-staged for maintaining high development standards. The platform targets educators and institutions seeking to implement AI-enhanced personalized learning pathways with real-time analytics and dynamic curriculum adaptation based on individual student performance patterns. TeachSpark is notable for its fully integrated development workflow that spans both .NET and Node.js ecosystems with synchronized build processes, comprehensive documentation structure, and a live production deployment at teach.makeboldspark.com demonstrating production-ready implementation. The project represents a modern full-stack educational technology solution combining contemporary web development practices with intelligent content personalization, though its current stale repository status (0 commits in 365 days) and lack of community engagement suggest it may be a demonstration project rather than an actively maintained product.

**Technology Stack Currency**: ✅ 76/100
**Dependencies**: 3 total (2 current, 1 outdated)

**Created**: 2025-06-19
**Last Modified**: 2026-05-13

---

### #19. [react-native-web-start](https://github.com/markhazleton/react-native-web-start)

Stars: 0 | Forks: 0 | Language: PowerShell | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2147 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: React Native Web Vite Starter

## Overview
React Native Web Start is a production-ready starter template for building cross-platform applications that run on Web, iOS, and Android from a single TypeScript/React codebase. The project demonstrates enterprise-grade development practices by combining React Native Web with Vite's fast build system, enabling developers to write once and deploy to multiple platforms using a unified component architecture.

## Key Features & Capabilities
The template provides comprehensive cross-platform support with modern tooling including TypeScript strict mode for type safety, Vite for lightning-fast HMR development, Tailwind CSS with Sass preprocessing for responsive design, and built-in markdown documentation browser. It includes production-ready features such as API integration with error handling, GitHub Pages automated deployment, PWA capabilities, performance monitoring, and Jest testing setup. The monorepo structure organizes shared components, web-specific, and mobile-specific code while maintaining a single source of truth.

## Technology Stack & Architecture
The project leverages React Native 0.85.0 for mobile abstraction, React Native Web 0.21.2 for web compatibility, Vite 8.0.8 as the primary build tool, TypeScript 6.0.2 for type safety, and Metro for React Native bundling. It uses a well-organized monorepo pattern with packages for shared logic, web configuration, and mobile configuration, accompanied by build automation scripts written in PowerShell, JavaScript, and TypeScript that handle asset management, documentation syncing, and build metadata generation.

## Current Status & Considerations
The repository shows **stale activity** with zero commits over both the last 90 and 365 days, zero stars, forks, and contributors, and a moderate tech stack currency score of 50/100. While the template appears well-documented and architecturally sound for enterprise use, the lack of maintenance history and community engagement suggests it's a personal reference project rather than an actively maintained open-source initiative. The large file size (2147 KB) and diverse language distribution (74.6% PowerShell, 12.5% TypeScript, 7.1% JavaScript) indicate comprehensive build scripting and automation.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 50 total (50 current, 0 outdated)

**Created**: 2025-07-26
**Last Modified**: 2026-05-11

---

### #20. [TailwindSpark](https://github.com/markhazleton/TailwindSpark)

Stars: 0 | Forks: 0 | Language: TypeScript | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 3866 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# TailwindSpark Technical Summary

**TailwindSpark** is a production-ready React TypeScript monorepo that serves as a comprehensive showcase and learning resource for modern web development patterns, specifically demonstrating Tailwind CSS 4's capabilities alongside contemporary React 19 patterns. The project functions as both a design system reference implementation and educational platform, featuring reusable UI components, semantic design tokens leveraging Tailwind's `@theme` directive, and interactive component examples deployed via a live demonstration site. Built with a Turborepo monorepo architecture, it encompasses a main demo application alongside shared packages for design tokens and reusable UI components, all maintained with strict TypeScript enforcement, formal code governance through a project constitution, WCAG AA accessibility compliance, and automated CI/CD pipelines including Dependabot dependency management and security scanning. The technology stack combines React 19.1.1, TypeScript 5.9, and Tailwind CSS 4.1.18, supplemented by development tools including Vitest for testing, ESLint for code quality, and PostCSS for CSS processing, with 27 total dependencies kept current. What distinguishes TailwindSpark is its emphasis on production-quality patterns and governance rather than a casual component showcase—it documents development metrics, architectural decisions, and constitutional compliance standards, making it ideal for developers seeking to understand scalable monorepo structure, design system implementation, and enterprise-grade React TypeScript practices. The project targets intermediate to advanced developers, technical architects, and teams building or refactoring design systems who want practical reference implementations and patterns beyond basic component libraries.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 27 total (27 current, 0 outdated)

**Created**: 2025-07-29
**Last Modified**: 2026-05-11

---

### #21. [MechanicsOfMotherhood](https://github.com/markhazleton/MechanicsOfMotherhood)

Stars: 0 | Forks: 0 | Language: TypeScript | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7598 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Mechanics of Motherhood

**Mechanics of Motherhood** is a production-ready recipe management web application specifically designed for busy working mothers, featuring 108+ curated recipes with smart categorization, search filtering, and nutritional information. The application demonstrates modern React 19 and TypeScript best practices, built with Vite for optimized performance and styled using Tailwind CSS with Shadcn/ui components for a polished, accessible interface. The architecture leverages TanStack React Query for intelligent server state management and real-time data synchronization with dual APIs (RecipeSpark and WebCMS), while maintaining graceful fallback to mock data for offline functionality. The project is deployed as a static Single Page Application on GitHub Pages with a custom domain (mechanicsofmotherhood.com), automated CI/CD pipelines via GitHub Actions, and Progressive Web App capabilities enabling offline recipe access and print-friendly functionality. Key technical distinguishing factors include 95+ Lighthouse performance scores, ~130KB gzipped bundle size, comprehensive SEO optimization with auto-generated sitemaps, and sophisticated data validation ensuring 100% data quality across all recipe content. The codebase represents a complete production demonstration combining responsive mobile-first design, WCAG accessibility compliance, and enterprise-grade deployment practices—serving as both a functional application for meal planning and a technical portfolio piece showcasing contemporary full-stack web development capabilities.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 42 total (42 current, 0 outdated)

**Created**: 2025-09-01
**Last Modified**: 2026-05-12

---

### #22. [Texecon](https://github.com/markhazleton/Texecon)

Stars: 0 | Forks: 0 | Language: TypeScript | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3811 KB | 🚀 0 commits/month

**Quality**: ❌ License | ❌ Docs

# Technical Summary: Texecon

**Texecon** is a static React application providing expert economic analysis and commentary focused on the Texas economy, hosted at texecon.com. The project implements a sophisticated build-time content management architecture that fetches fresh content from a WebSpark headless CMS API during compilation, with cached fallbacks for resilience, while generating static HTML pages optimized for SEO and performance on GitHub Pages deployment.

The application leverages a modern tech stack built on **React 19, TypeScript, and Vite 7.1** for development and build optimization, combined with **Tailwind CSS 4.1, Radix UI primitives, and shadcn/ui** for accessible, composable component architecture and styling. The project employs a multi-stage build pipeline that includes content fetching, dynamic sitemap generation, type-safe API integration, and post-build static page generation for all dynamic routes, enabling progressive enhancement through client-side routing with HTML fallbacks.

Architecturally, Texecon distinguishes itself through its **hybrid static-dynamic rendering approach**: it pre-renders pages at build time for optimal Core Web Vitals compliance and SEO while maintaining client-side routing capabilities for improved user experience. The design includes sophisticated asset optimization with build ID-based cache busting, structured data implementation, and a graceful fallback system that preserves functionality if the CMS API becomes unavailable during builds.

The repository targets technical stakeholders interested in headless CMS integration patterns, static site generation with modern tooling, and production-grade performance optimization for content-heavy applications. However, the project shows signs of being in maintenance mode, with zero recent activity over 90 days and stale commit history, suggesting it may be a stable, completed demonstration project rather than an actively developed product.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 37 total (37 current, 0 outdated)

**Created**: 2025-09-03
**Last Modified**: 2026-05-13

---

### #23. [git-spark](https://github.com/markhazleton/git-spark)

Stars: 0 | Forks: 0 | Language: PowerShell | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 2064 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: Git Spark

**Git Spark** is a comprehensive Git repository analytics and reporting tool that analyzes commit history to generate interactive HTML dashboards with visualizations of contributor activity, code change patterns, and repository health metrics. The project provides both a command-line interface and Node.js API, enabling users to extract insights from Git data in multiple formats (HTML, JSON, CSV, Markdown) with features including daily trend analysis, contributor statistics, file change tracking, and governance metrics based on conventional commit adherence and code churn patterns.

Built with a modern polyglot tech stack combining **PowerShell (45.3%), TypeScript (43.7%), and Shell scripting (10.0%)**, the tool leverages key dependencies like Commander.js for CLI orchestration, Chalk for terminal styling, Ora for progress indicators, and Boxen for formatted output presentation. The architecture emphasizes **security-first design** with strict Content Security Policy (CSP) implementation, SHA-256 hashing for inline assets, native SVG charting (avoiding external libraries), and self-contained report generation suitable for air-gapped environments—ensuring analytical integrity while maintaining full transparency about Git data limitations.

The project targets **Solutions Architects, DevOps engineers, and development teams** seeking governance visibility and risk assessment through Git metadata, with distinctive features including email redaction options, timezone-aware daily trend analysis, progressive table pagination for performance, dark mode with persistent preferences, and comprehensive metric documentation explaining what Git analysis can and cannot reveal. Despite having zero stars, forks, or recent commits (classified as "stale" activity), the codebase demonstrates high technical currency (98/100) and production-readiness with Node.js ≥20.19.0 support, active npm package distribution, and a live demonstration site at markhazleton.github.io/git-spark/.

**Technology Stack Currency**: ✅ 98/100
**Dependencies**: 22 total (21 current, 1 outdated)

**Created**: 2025-09-29
**Last Modified**: 2026-05-12

---

### #24. [github-stats-spark](https://github.com/markhazleton/github-stats-spark)

Stars: 0 | Forks: 0 | Language: Python | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 24578 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Analysis: github-stats-spark

## 📋 Executive Summary

**Stats Spark** is a comprehensive GitHub analytics platform that generates automated SVG profile statistics, AI-powered repository analysis, and an interactive mobile-first dashboard for GitHub users. The project demonstrates modern full-stack development but shows signs of abandonment with zero recent activity despite ambitious feature scope.

---

## 🏗️ Architecture Overview

### Tech Stack Breakdown

| Component | Languages | Key Technologies |
|-----------|-----------|------------------|
| **Backend/Analysis** | Python (51%) | PyGithub, PyYAML, requests, beautifulsoup4, svgwrite |
| **Frontend Dashboard** | JavaScript (20.1%) | React, Chart.js, Dexie (IndexedDB) |
| **Build/Deployment** | PowerShell (18.8%), CSS (9.1%), HTML (1%) | GitHub Actions, GitHub Pages |

### Core Modules

**1. SVG Statistics Generator**
- Automated weekly generation via GitHub Actions
- 6 visualization categories: Overview, Heatmap, Languages, Streaks, Fun Stats, Release Cadence
- Custom theme support (dark/light) with WCAG AA compliance
- Spark Score algorithm: 40% consistency + 35% volume + 25% collaboration

**2. AI-Powered Analysis Engine**
- Claude Haiku integration for repository summarization (97%+ success rate)
- Intelligent ranking: 30% popularity (stars/forks) + 45% activity (time-decayed commits) + 25% health (docs/licensing)
- Attention scoring for maintenance prioritization
- Markdown report generation with embedded visualizations

**3. Interactive Dashboard**
- Mobile-first design (320px-768px viewport optimization)
- Bottom-sheet navigation pattern
- Touch gestures (swipe-to-delete, horizontal navigation)
- Chart.js visualizations with touch-optimized tooltips
- Offline support via Dexie + IndexedDB (7-day retention)

---

## 📊 Key Features Analysis

### Strengths

✅ **Well-Designed Feature Set**
- Comprehensive GitHub metrics extraction
- Beautiful SVG generation with theme customization
- Mobile-first approach with accessibility (WCAG 2.1 AA)
- Smart API rate-limiting with exponential backoff
- Modular, extensible architecture

✅ **Enterprise Considerations**
- YAML-based configuration system
- CLI for local development/testing
- Intelligent caching mechanisms
- Performance optimization targets (Lighthouse CI, <2s FCP)

✅ **Production Infrastructure**
- GitHub Actions automation (weekly at midnight UTC)
- GitHub Pages deployment
- CSV/JSON export functionality
- IndexedDB offline caching

### Weaknesses

❌ **Critical Status Issues**
- **0 commits in 90 days** — project is stale/abandoned
- **0 commits in 365 days** — no maintenance window
- **0 GitHub stars/forks/contributors** — no community adoption
- Tech stack currency at 79/100 (dated dependencies likely)

❌ **Incomplete Implementation**
- Live site referenced but likely non-functional
- Sample report paths referenced but unverified
- No evidence of actual deployment

❌ **Undisclosed Dependencies**
- Claude AI integration mentioned but not in dependency list
- React mentioned in dashboard but not in `requirements.txt`
- Chart.js + react-chartjs-2 implied but not documented

---

## 🔧 Technical Debt Assessment

### Dependency Management

```python
# Listed Dependencies (12 total)
PyGithub        # GitHub API wrapper
PyYAML         # Configuration parsing
svgwrite       # SVG generation
requests       # HTTP client
beautifulsoup4 # HTML parsing
# + 7 undocumented/implied
```

**Issues:**
- React ecosystem dependencies missing from Python analysis
- No lock file mentioned (pip freeze, poetry.lock)
- No version pinning visible
- Potential security vulnerabilities in unmaintained repos

### Architecture Concerns

1. **Python/JavaScript Mismatch**: 51% Python + 20% JavaScript suggests poor separation of concerns or duplicate logic
2. **Missing CI/CD Details**: GitHub Actions referenced but workflow files not visible
3. **API Rate Limiting**: Claims "smart caching" but implementation details absent
4. **Error Handling**: No visible exception handling strategy for API failures
5. **Database**: No persistent storage strategy documented (likely JSON files)

---

## 🚀 Deployment & Performance

### Claimed Capabilities
- <5 minutes processing for 500 repositories
- <2 second First Contentful Paint (FCP)
- 0.9+ Lighthouse performance score
- Offline functionality with 7-day cache retention

### Red Flags
- No performance benchmarks provided
- Claims unverified due to project inactivity
- Cache invalidation strategy unclear
- Scalability to large numbers of repos untested

---

## 📈 Activity Analysis

```
Creation Date:    2025-12-28 (⚠️ Future date - likely data error)
Repository Size:  24.5 MB (unusually large for analytics tool)
Recent Activity:  STALE (0 commits/90d, 0 commits/365d)
Community:        0 stars, 0 forks, 0 contributors
Activity Pattern: Abandoned/POC stage
```

---

## 🎯 Use Case Assessment

### Ideal For
- **Individual developers** wanting GitHub portfolio visualization
- **Team leads** tracking repository health metrics
- **OSS maintainers** monitoring project momentum
- **Technical demonstrators** (per Make Bold Spark portfolio context)

### Not Suitable For
- **Production analytics** (unmaintained, unverified)
- **Enterprise adoption** (no support, no active development)
- **Real-time monitoring** (weekly batch processing only)
- **Mission-critical systems** (single-developer passion project)

---

## 🔐 Security Considerations

⚠️ **Concerns:**
1. **GitHub Token Storage**: No visible documentation on secure token handling
2. **AI API Keys**: Claude integration credentials management unclear
3. **User Data**: No privacy policy or data retention documentation
4. **Dependency Vulnerabilities**: No security scanning mentioned
5. **Input Validation**: SVG generation could be injection vector

---

## 💡 Recommendations

### If

**Technology Stack Currency**: ✅ 79/100
**Dependencies**: 12 total (5 current, 7 outdated)

**Created**: 2025-12-28
**Last Modified**: 2026-05-14

---

### #25. [MuseumSpark](https://github.com/markhazleton/MuseumSpark)

Stars: 0 | Forks: 0 | Language: Python | 0 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 24264 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# MuseumSpark: Technical Summary

**MuseumSpark** is an intelligent travel planning platform that transforms the Walker Art Center's reciprocal membership directory into a curated, data-enriched resource for art enthusiasts exploring North American museums. The project combines a React/Vite-based static frontend with a sophisticated Python data enrichment pipeline that aggregates and validates information from multiple sources (Wikidata, Wikipedia, museum websites) to build priority-scored museum recommendations tailored to users' interests and travel constraints.

The system implements a multi-phase enrichment architecture (Phases 0–4) currently in Phase 1, with 1,269 museums tracked but only 0.08% fully enriched, demonstrating a methodical approach to data quality. Key features include a comprehensive museum browser with search/filter capabilities, a real-time data quality dashboard tracking enrichment progress, JSON Schema validation for all records, and a "never replace known with null" data governance principle that prioritizes data integrity. The frontend uses modern React 19 with TypeScript, Tailwind CSS, and client-side routing for responsive browsing, while the backend infrastructure leverages Pydantic for validation, BeautifulSoup for web scraping, and a layered pipeline supporting identity verification, metadata extraction, and heuristic fallbacks.

The architecture is uniquely designed for iterative enrichment and expert curation, with planned Phase 2 featuring human-driven scoring of collections and Phase 2.5 introducing AI-assisted content analysis via LLM agents to identify signature artists and exhibition patterns. The project targets art-focused travelers and collectors seeking strategic museum itineraries and represents a portfolio piece demonstrating technical solutions in data engineering, full-stack development, and AI integration within a domain-specific application context.

**Created**: 2026-01-15
**Last Modified**: 2026-05-14

---

### #26. [SupportSpark](https://github.com/markhazleton/SupportSpark)

Stars: 0 | Forks: 0 | Language: PowerShell | 0 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 1756 KB | 🚀 0 commits/month

**Quality**: ❌ License | ❌ Docs

# SupportSpark: Technical Summary

**SupportSpark is a full-stack support network platform that enables members to share life journey updates with a curated group of supporters through a calm, role-based web application.** The platform addresses the emotional burden of keeping loved ones informed during challenging times by centralizing updates and organizing supporter responses in threaded conversations, with invitation-only network controls ensuring privacy and security. Built with modern web technologies—React 19 with TypeScript for the frontend, Express 5 for the backend, and Tailwind CSS 4 for a purposeful teal/sage UI design—the application demonstrates enterprise-grade patterns including role-based access control (RBAC), Passport.js authentication with session management, and Zod runtime validation for end-to-end type safety. The architecture employs a shared schema layer across client and server to maintain a single source of truth, integrates TanStack React Query for efficient server state management, and provides both cloud hosting and Windows IIS deployment options via automated PowerShell scripts, showcasing production-ready deployment flexibility. Unique features include a browser-only demo mode using localStorage for zero-backend exploration, responsive accessibility built on Radix UI primitives, and comprehensive documentation including an IIS deployment guide and constitutional governance framework for maintainability. The platform targets individuals navigating health challenges, life transitions, or personal journeys who need a distraction-free, compassionate digital space for connection, making it particularly valuable for support networks during medical treatments, major life changes, or grief management.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 97 total (97 current, 0 outdated)

**Created**: 2026-02-01
**Last Modified**: 2026-05-14

---

### #27. [DocSpecSpark](https://github.com/markhazleton/DocSpecSpark)

Stars: 0 | Forks: 0 | Language: Python | 0 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 223 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# DocSpecSpark - Technical Summary

**DocSpecSpark** is an AI-assisted documentation automation framework that provides a structured, repeatable workflow for creating, reviewing, and publishing documentation systems through markdown-based prompts and lightweight CLI tooling. The project emphasizes a separation-of-concerns architecture, dividing framework-managed assets (`.docspark/`) from user-owned artifacts (`.documentation/`), with intelligent prompt and script resolution ordering that allows customization at multiple levels. Built in Python with dependencies on `rich` (terminal formatting) and `typer` (CLI framework), it offers 21+ slash commands covering the full documentation lifecycle—from constitution creation and specification through implementation and publication—with specialized workflows for PR reviews, site audits, and repository storytelling. The framework is designed to work seamlessly with popular AI coding assistants (GitHub Copilot, Claude, Cursor) through agent-specific bootstrap prompts, eliminating the need for manual setup while remaining optional via a CLI interface for programmatic installation. What distinguishes DocSpecSpark is its focus on **prompts as the primary product** rather than code, treating AI assistants as the execution engine for structured documentation governance, making it particularly valuable for teams seeking to establish consistent documentation practices without heavy framework overhead. The target audience includes documentation-centric teams, technical architects, and AI assistant users seeking governance mechanisms for large-scale documentation projects, with examples and templates provided to demonstrate post-installation workflows.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 2 total (0 current, 2 outdated)

**Created**: 2026-03-07
**Last Modified**: 2026-05-11

---

### #28. [devspark](https://github.com/markhazleton/devspark)

Stars: 0 | Forks: 0 | Language: Python | 0 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 6710 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# DevSpark Technical Summary

DevSpark is a structured workflow framework designed to standardize AI-assisted software development through a collection of 28 markdown-based slash commands and supporting scripts, enabling repeatable processes from requirements specification through release without requiring installation or subscriptions. The system is primarily composed of Python (50.2%), PowerShell (26.3%), and Shell (23.4%) code, leveraging declarative configuration management via Pydantic, JSON Schema, and YAML to define reusable workflows, with an optional CLI built on Click for automation and validation tasks. The architecture follows a prompt-first, no-install philosophy where core functionality ships as markdown templates that AI agents (Claude, Copilot, Cursor, Gemini, and 13+ others) can directly consume, supplemented by context-gathering scripts and a harness runtime system that orchestrates multi-step engineering workflows with structured artifact preservation and execution tracing. Key capabilities include constitution-based code reviews, specification-to-implementation pipeline orchestration, pull request automation, knowledge archival through the canonical "harvest" workflow, and optional multi-app monorepo support with application registry management. The tech stack maintains a 76/100 currency score with modern dependencies, though the project shows stale activity (zero commits in 90 and 365 days), indicating it may be in maintenance mode despite solid foundational design. DevSpark targets development teams seeking to reduce cognitive load when working with AI coding assistants by providing a battle-tested, agent-agnostic workflow abstraction that bridges the gap between natural language requirements and production-ready implementations.

**Technology Stack Currency**: ✅ 76/100
**Dependencies**: 5 total (1 current, 4 outdated)

**Created**: 2026-04-02
**Last Modified**: 2026-05-11

---

### #29. [ApiSpark](https://github.com/markhazleton/ApiSpark)

Stars: 0 | Forks: 0 | Language: C# | 0 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 1636 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# ApiSpark Technical Summary

**ApiSpark** (also branded as MakeBoldSpark) is a modular ASP.NET Core backend API platform designed to consolidate multiple low-volume personal and portfolio APIs into a single, cost-effective Azure-hosted application. The platform serves as the centralized API layer for static websites and Single Page Applications, enabling a static-first architecture where public-facing sites remain lightweight while all business logic and data operations are delegated to this unified backend. Built on .NET (targeting .NET 10 LTS), Entity Framework Core, and SQLite for relational data with optional Azure Cosmos DB for document-oriented scenarios, the architecture implements role-based access control through distinct API route areas (`/api/public/`, `/api/admin/`, `/api/publish/`, `/api/integrations/`) that enforce authentication and authorization at the endpoint level. The project is optimized for Azure infrastructure—specifically Azure App Service (Linux B1 tier) with persistent SQLite storage and Azure Static Web Apps integration—making it particularly suited for developers and technical architects seeking to demonstrate scalable, maintainable multi-tenant API hosting patterns without enterprise-level complexity or cost. Its standout features include browser-based CMS/admin capabilities, static JSON generation for content websites, shallow and deep health check endpoints, and comprehensive Architecture Decision Records (ADRs) documenting design rationale. Though currently inactive (zero recent commits and no community engagement), ApiSpark functions as both a functional backend system for the MakeBoldSpark portfolio and an educational reference implementation for hosting multiple ASP.NET Core microservices cost-effectively on Azure.

**Created**: 2026-05-07
**Last Modified**: 2026-05-13

---

### #30. [markhazleton.github.io](https://github.com/markhazleton/markhazleton.github.io)

Stars: 0 | Forks: 0 | Language: SCSS | 0 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 161 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

# Technical Summary: markhazleton.github.io

This repository is a personal portfolio and blog website built with **Jekyll**, a static site generator, and hosted on GitHub Pages at markhazleton.com. The site features a customized Minima theme with a modern tech stack comprising SCSS (39.4%), HTML (30.1%), and CSS (29.8%), delivering a responsive, theme-aware experience with dark/light mode toggle functionality and emoji support without relying on external CSS frameworks. The project uses **Ruby 3.2.2**, **Jekyll 3.10.0**, and automated CI/CD via GitHub Actions for seamless deployment—changes pushed to the `sources` branch trigger automatic builds and deployment to GitHub Pages. The architecture follows Jekyll conventions with well-organized directories for posts (`_posts`), reusable components (`_includes`), customized layouts (`_layouts`), and modular Sass styling (`_sass`), making it maintainable and extensible for content creation and design updates. The repository includes comprehensive documentation for local development setup across multiple OS platforms (macOS, Windows, Linux) and detailed publishing workflows for creating blog posts using Markdown front matter, with support for categories, tags, SEO optimization, and featured images. However, the project shows signs of staleness with zero commits over 90+ days and a tech stack currency score of 56/100, indicating that dependencies and Jekyll versions may benefit from updates to align with current best practices and security standards.

**Technology Stack Currency**: ✅ 56/100
**Dependencies**: 3 total (2 current, 1 outdated)

**Created**: 2021-04-18
**Last Modified**: 2026-04-01

---


---

## Report Metadata

- **Generation Time**: 5.8 seconds
- **SVGs Generated**: 6/6
- **Total API Calls**: 0
- **Total AI Tokens**: 72,591
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
*Last updated: 2026-05-14*

## Screenshot Audit

- Repositories with websites: 22
- Screenshots present: 21
- Flagged repositories: 1

### Missing Screenshots

- PHPDocSpark: https://phpdocspark.azurewebsites.net
