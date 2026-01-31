# GitHub Profile: markhazleton

**Generated**: 2026-01-31 16:05:57 UTC
**Report Version**: 1.0.0
**Repositories Analyzed**: 35
**AI Summary Rate**: 100.0%

> 💡 **Navigation**: [Profile Overview](#profile-overview) | [Top Repositories](#top-35-repositories) | [Metadata](#report-metadata)

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

## Top 35 Repositories

### #1. [github-stats-spark](https://github.com/markhazleton/github-stats-spark)

Stars: 0 | Forks: 0 | Language: Python | 139 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7510 KB | 🚀 46.3 commits/month

**Quality**: ❌ License | ✅ Docs

Based on the comprehensive README, here's a detailed technical summary of the GitHub Stats Spark repository:

Stats Spark is an advanced GitHub analytics platform designed to automatically generate comprehensive visualizations and insights about a developer's GitHub activity and repository ecosystem. The project leverages Python as its primary language, integrating multiple technologies including PyGithub for GitHub data retrieval, AI models like Claude Haiku for intelligent analysis, and web technologies (JavaScript, CSS) for interactive dashboards and visualizations.

The core functionality revolves around automated, multi-dimensional GitHub profile analysis, producing SVG-based statistics across five key categories: overview dashboard, commit heatmap, language statistics, contribution streaks, and "fun stats". The system employs a sophisticated "Spark Score" algorithm that evaluates developer activity through weighted metrics of consistency (40%), volume (35%), and collaboration (25%), providing a holistic performance assessment.

A standout feature is the AI-powered repository analysis, which generates comprehensive markdown reports using an intelligent ranking algorithm. This approach combines community engagement (30%), activity metrics (45%), and project health signals (25%) to create nuanced, context-aware repository evaluations. The system supports extensive customization through YAML configurations and features enterprise-grade capabilities like smart API caching, rate limit handling, and modular architectural design.

The project is engineered with strong emphasis on performance, accessibility, and user experience. It includes features like mobile-first interactive dashboards, offline support, WCAG 2.1 AA compliance, and the ability to analyze 50+ repositories in under 3 minutes. The automated GitHub Actions workflow ensures daily updates, making it a low-maintenance solution for developers seeking comprehensive GitHub insights.

Technically remarkable aspects include its use of multiple fallback strategies (e.g., AI summary generation), intelligent caching mechanisms reducing API calls by 80-95%, and a flexible, extensible architecture that supports future enhancements. The project targets developers, technical leaders, and open-source maintainers looking for sophisticated, automated GitHub activity tracking and visualization.

Recommended technical audience: Python developers, DevOps engineers, technical project managers, and open-source maintainers interested in advanced GitHub analytics and visualization tools.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 9 total (9 current, 0 outdated)

**Created**: 2025-12-28
**Last Modified**: 2026-01-31

---

### #2. [mark-hazleton-s-notes](https://github.com/markhazleton/mark-hazleton-s-notes)

Stars: 0 | Forks: 0 | Language: TypeScript | 78 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 165884 KB | 🚀 26.0 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary for the mark-hazleton-s-notes repository:

This is a sophisticated personal portfolio and technical blog site built as a static site using modern web technologies, designed to showcase Mark Hazleton's professional work and insights as a Technical Solutions Architect. The site leverages a robust React 19 and Vite 7 framework with server-side rendering (SSR) and static prerendering, enabling high-performance content delivery and excellent SEO capabilities. The architecture is meticulously structured, with a comprehensive build pipeline that automatically generates optimized assets, including static HTML routes, responsive image thumbnails, RSS feeds, sitemaps, and metadata, all managed through sophisticated build scripts written in TypeScript. Key technical innovations include dynamic GitHub repository metrics integration, automatic content optimization, and a modular component system using Tailwind CSS, Radix UI, and shadcn/ui for a consistent, responsive design. The project stands out for its advanced static site generation approach, which seamlessly combines content management, performance optimization, and developer experience through automated build processes and carefully designed scripts. Targeted primarily at technical professionals, developers, and potential collaborators, the site serves as both a personal showcase and a technical demonstration of modern web development practices.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 58 total (58 current, 0 outdated)

**Created**: 2026-01-10
**Last Modified**: 2026-01-31

---

### #3. [git-spark](https://github.com/markhazleton/git-spark)

Stars: 0 | Forks: 0 | Language: TypeScript | 47 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 1326 KB | 🚀 15.7 commits/month

**Quality**: ❌ License | ✅ Docs

Based on the repository details, here's a comprehensive technical summary:

Git Spark is a sophisticated TypeScript-based Git repository analytics tool designed to provide deep insights into software development workflows through comprehensive commit history analysis. The project enables developers and engineering managers to generate interactive HTML reports that visualize repository metrics, including contributor activity, code change patterns, daily trends, and file evolution across multiple dimensions. Leveraging modern web technologies and a modular Node.js architecture, Git Spark offers both CLI and programmatic interfaces, supporting advanced features like multi-format export, configurable analysis periods, and enterprise-grade reporting with strong emphasis on data privacy and accessibility. The tool's unique value proposition lies in its ability to transform raw Git commit data into actionable intelligence, featuring security-first design principles, dark mode support, and extensive customization options that make it suitable for teams seeking granular repository insights without external service dependencies.

Key technical highlights include:
- TypeScript-based implementation
- Node.js CLI and library architecture
- Interactive HTML reporting with dynamic charts
- Comprehensive Git commit data analysis
- Multiple export formats (HTML, JSON, CSV, Markdown)
- Configurable analysis parameters
- Strong focus on privacy and security

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 19 total (19 current, 0 outdated)

**Created**: 2025-09-29
**Last Modified**: 2026-01-25

---

### #4. [WebSpark.HttpClientUtility](https://github.com/markhazleton/WebSpark.HttpClientUtility)

Stars: 0 | Forks: 0 | Language: C# | 71 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 2157 KB | 🚀 23.7 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a technical summary of the WebSpark.HttpClientUtility repository:

WebSpark.HttpClientUtility is a sophisticated .NET HTTP client utility library designed to simplify and enhance HTTP communication in modern .NET applications (versions 8-10). The library provides a comprehensive, drop-in solution for HTTP interactions, offering enterprise-grade features like Polly-based resilience (retry and circuit breaker patterns), intelligent response caching, structured logging with correlation IDs, and built-in OpenTelemetry tracing—all configurable with a single method call. Leveraging dependency injection and modern .NET patterns, the library abstracts away complex HttpClient setup, reducing boilerplate code from 50+ lines to a single configuration method while providing robust observability, error handling, and performance optimization features.

Key technical highlights include:
- Integrated Polly resilience policies
- Configurable in-memory response caching
- Automatic correlation and tracing
- Support for .NET 8 LTS, 9, and 10 (Preview)
- Native AOT and IL trimming compatibility
- Extensive test coverage (237+ unit tests)
- Semantic versioning and long-term support

The library is particularly well-suited for microservices, distributed systems, background workers, and web scraping scenarios where reliable, observable HTTP communication is critical. Its design philosophy emphasizes simplicity, performance, and production-readiness, making it an attractive alternative to manually configured HttpClient setups or more rigid HTTP client libraries.

**Created**: 2025-05-03
**Last Modified**: 2026-01-05

---

### #5. [MuseumSpark](https://github.com/markhazleton/MuseumSpark)

Stars: 0 | Forks: 0 | Language: Python | 61 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 21061 KB | 🚀 20.3 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary of the MuseumSpark repository:

MuseumSpark is an innovative data-driven travel planning platform specifically designed for art enthusiasts, focusing on transforming the Walker Art Center Reciprocal Program museum list into a sophisticated, enriched museum discovery and travel optimization system. The project leverages a multi-phase data enrichment pipeline that systematically aggregates and validates museum metadata from diverse sources like Wikidata, Wikipedia, and official museum websites, with the ultimate goal of creating a comprehensive, intelligent museum browsing and travel planning experience. Built using a modern Python-based data pipeline and React frontend, the platform employs advanced techniques like JSON Schema validation, web scraping, and planned AI-assisted content generation to create a rich, dynamically updated museum database with sophisticated features such as priority scoring, collection strength assessment, and potential future personalized travel recommendations. The architecture is modular and extensible, with a clear roadmap progressing through distinct data enrichment and feature expansion phases, ultimately aiming to provide art lovers with a strategic tool for discovering and prioritizing museum visits across North America. Unique aspects include its rigorous data quality approach, multi-source data integration, and the vision to transform a simple museum directory into an intelligent, context-aware travel companion powered by structured data and machine learning techniques. The target users are art enthusiasts, travelers, museum researchers, and cultural tourists seeking a data-driven approach to museum exploration and travel planning.

**Created**: 2026-01-15
**Last Modified**: 2026-01-31

---

### #6. [SampleMvcCRUD](https://github.com/markhazleton/SampleMvcCRUD)

Stars: 8 | Forks: 4 | Language: HTML | 42 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 30497 KB | 🚀 14.0 commits/month

**Quality**: ❌ License | ✅ Docs

Technical Summary:

SampleMvcCRUD is a comprehensive .NET 10 web application demonstrating multiple CRUD (Create, Read, Update, Delete) implementation strategies for employee and department management, serving as both a reference implementation and educational resource for modern web development techniques. The project showcases diverse architectural approaches including traditional MVC, Razor Pages, and Single Page Application (SPA) styles, with a robust technology stack featuring ASP.NET Core, Entity Framework Core, Swagger/OpenAPI, and Bootswatch theming. Key capabilities include dynamic theme switching, REST API endpoints, in-memory database integration, modal-based CRUD forms, and comprehensive DevOps workflows with GitHub Actions, Docker containerization, and multi-platform deployment strategies. The repository emphasizes clean architecture principles, dependency injection, unit testing, and observability, making it an excellent learning tool for developers seeking to understand contemporary .NET web application design and implementation patterns. Targeted primarily at .NET developers, software architects, and technical learners, the project provides a rich, evolving template for building maintainable, scalable web applications with modern tooling and best practices.

**Created**: 2019-04-25
**Last Modified**: 2026-01-31

---

### #7. [WebSpark](https://github.com/markhazleton/WebSpark)

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

### #8. [JsBootSpark](https://github.com/markhazleton/JsBootSpark)

Stars: 0 | Forks: 0 | Language: JavaScript | 39 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 3348 KB | 🚀 13.0 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary of the JsBootSpark repository:

JsBootSpark is a sophisticated full-stack web application starter kit designed to provide developers with a robust, production-ready framework for building modern, responsive web applications using JavaScript ecosystem technologies. The project leverages a comprehensive tech stack including Express.js, Bootstrap 5, EJS templating, and Node.js 18+, offering a complete development environment with advanced features like hot reloading, SASS compilation, security middleware, and progressive web app capabilities.

Key technical highlights include:
- A modular, feature-rich architecture supporting rapid web application development
- Integrated development workflows with automated build, testing, and deployment processes
- Comprehensive security implementations including Helmet.js, rate limiting, and content security policies
- Advanced frontend capabilities with Bootstrap 5, responsive design, and dark/light mode support
- Containerization support via Docker and CI/CD integration with GitHub Actions

The project distinguishes itself through its holistic approach to web development, providing not just a starter template, but a complete ecosystem with extensive documentation, performance optimization, and scalable design patterns. It targets full-stack JavaScript developers seeking a batteries-included, enterprise-grade starting point for web applications, with particular emphasis on developer experience, security, and modern web standards.

Architecturally, JsBootSpark demonstrates a microservice-friendly, modular design that supports easy customization, extension, and deployment across various environments. Its comprehensive toolchain and opinionated yet flexible structure make it an excellent foundation for both small projects and complex web applications.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 30 total (30 current, 0 outdated)

**Created**: 2022-06-06
**Last Modified**: 2026-01-31

---

### #9. [RESTRunner](https://github.com/markhazleton/RESTRunner)

Stars: 2 | Forks: 1 | Language: C# | 16 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 426 KB | 🚀 5.3 commits/month

**Quality**: ❌ License | ✅ Docs

RESTRunner is a comprehensive .NET 10 solution designed for automated REST API testing, performance benchmarking, and regression testing, with a primary focus on integrating Postman collections into a robust testing framework. The project offers a multi-faceted approach to API validation, featuring capabilities such as automated test execution, performance analysis, load testing, and detailed reporting through both console and web interfaces. Built using C# and leveraging .NET 10's latest performance improvements, the framework supports cross-platform testing, provides interactive web-based testing via Razor Pages, and includes a sample CRUD API for demonstration purposes. Its architecture emphasizes modularity, performance optimization, and comprehensive test coverage, with notable features like CSV result exports, response time percentile tracking, and built-in performance metrics. RESTRunner is particularly valuable for developers, QA engineers, and API developers seeking a modern, high-performance testing solution that can seamlessly integrate existing Postman collections and provide in-depth insights into API behavior and performance characteristics.

**Created**: 2021-09-30
**Last Modified**: 2026-01-12

---

### #10. [tailwind-demo](https://github.com/markhazleton/tailwind-demo)

Stars: 0 | Forks: 0 | Language: HTML | 12 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 1591 KB | 🚀 4.0 commits/month

**Quality**: ❌ License | ✅ Docs

TailwindSpark is a comprehensive React-based design system and component showcase built as a modern monorepo, demonstrating advanced frontend development practices with Tailwind CSS v4, React 19, and TypeScript 5.9. The project serves as a robust template and reference implementation for building scalable, performant web applications with a focus on design system consistency, developer experience, and production-grade architectural patterns. It features a complete UI component library, responsive design, accessibility compliance, and extensive tooling including Vite, Vitest, ESLint, and GitHub Actions for CI/CD, with particular emphasis on type safety, performance optimization, and modular code organization. The repository goes beyond a typical demo by providing a production-ready framework with advanced features like lazy loading, error boundaries, dark mode support, keyboard navigation, and comprehensive testing strategies. Its unique value proposition lies in its holistic approach to frontend development, offering developers a sophisticated starter template that bridges design systems, performance optimization, and modern web technology best practices. The project is particularly valuable for frontend engineers, design system architects, and teams seeking a reference implementation of a contemporary, scalable React application with best-in-class developer tooling and UI/UX considerations.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 25 total (25 current, 0 outdated)

**Created**: 2025-07-29
**Last Modified**: 2026-01-05

---

### #11. [WebSpark.ArtSpark](https://github.com/markhazleton/WebSpark.ArtSpark)

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

### #12. [MechanicsOfMotherhood](https://github.com/markhazleton/MechanicsOfMotherhood)

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

### #13. [FastEndpointApi](https://github.com/markhazleton/FastEndpointApi)

Stars: 2 | Forks: 1 | Language: HTML | 7 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 137 KB | 🚀 2.3 commits/month

**Quality**: ❌ License | ✅ Docs

Technical Summary of FastEndpointApi Repository:

FastEndpointApi is a demonstration project showcasing the FastEndpoints framework for building high-performance, minimalistic REST APIs in ASP.NET Core, focusing on a Person Management system that implements CRUD operations with a clean, lightweight architectural approach. The project leverages the REPR (Request-Endpoint-Response) pattern to create streamlined API endpoints with minimal boilerplate code, utilizing technologies like .NET 10.0, Bogus for data generation, and integrated Swagger documentation. By implementing a complete API with features such as in-memory data storage, dependency injection, and HATEOAS-style link generation, the repository serves as both a practical tutorial and a reference implementation for developers looking to adopt a more modern, efficient approach to API development. The project stands out by emphasizing code simplicity, maintainability, and performance, providing a comprehensive example of how FastEndpoints can significantly reduce complexity in ASP.NET Core API design while maintaining robust functionality. It is particularly valuable for .NET developers seeking to modernize their API development practices, offering a real-world template for building clean, efficient web services with minimal overhead.

**Created**: 2024-04-06
**Last Modified**: 2026-01-12

---

### #14. [ReactSparkPortfolio](https://github.com/markhazleton/ReactSparkPortfolio)

Stars: 0 | Forks: 0 | Language: CSS | 8 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 45058 KB | 🚀 2.7 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary of the ReactSparkPortfolio repository:

ReactSparkPortfolio is an advanced, enterprise-grade personal portfolio application built using React 19, TypeScript, and Vite, designed to showcase modern web development practices through a feature-rich, performant, and scalable single-page application. The project demonstrates sophisticated frontend engineering by implementing cutting-edge technologies like SignalR for real-time interactions, comprehensive type safety with TypeScript, responsive design with Bootstrap 5, and a modular architecture that supports lazy loading, code splitting, and dynamic content rendering. Key technical highlights include a multi-platform deployment strategy (Azure Static Web Apps and GitHub Pages), integrated real-time features such as live chat and weather widgets, and a robust CI/CD pipeline configured through GitHub Actions, which enables automated builds, testing, and deployments. The application goes beyond a typical portfolio by incorporating advanced features like accessibility compliance, dark/light theme switching, SEO optimization, and an admin panel for dynamic content management, making it both a personal showcase and a reference implementation for modern web application development. Targeted primarily at developers, technical professionals, and potential employers, this project serves as both a personal branding tool and a comprehensive demonstration of full-stack development expertise, emphasizing performance, security, and user experience through its carefully crafted architectural choices and technology integrations.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 36 total (36 current, 0 outdated)

**Created**: 2024-10-11
**Last Modified**: 2026-01-31

---

### #15. [Texecon](https://github.com/markhazleton/Texecon)

Stars: 0 | Forks: 0 | Language: HTML | 3 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 3304 KB | 🚀 1.0 commits/month

**Quality**: ❌ License | ❌ Docs

Here's a comprehensive technical summary:

TexEcon is a sophisticated static React application designed for advanced economic analysis and reporting focused specifically on the Texas economic landscape. The project leverages modern web development technologies including React 19, TypeScript, and Vite to create a high-performance, SEO-optimized static site with dynamic content retrieval from a headless CMS (WebSpark). Its architecture emphasizes build-time content management, progressive enhancement, and comprehensive static site generation, enabling efficient content delivery with robust fallback mechanisms and automated deployment to GitHub Pages. The application implements advanced features like dynamic sitemap generation, structured data optimization, and client-side routing with static HTML fallbacks, making it a technically sophisticated platform for economic research and publication. By integrating type-safe development practices, accessibility-focused UI components from Radix UI, and a modular build pipeline, TexEcon represents a cutting-edge approach to creating performant, content-driven web applications with a focus on technical excellence and user experience.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 50 total (50 current, 0 outdated)

**Created**: 2025-09-03
**Last Modified**: 2026-01-04

---

### #16. [markhazleton](https://github.com/markhazleton/markhazleton)

Stars: 0 | Forks: 0 | Language: Unknown | 4 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 6583 KB | 🚀 1.3 commits/month

**Quality**: ❌ License | ❌ Docs

Based on the repository's README and metadata, here's a comprehensive technical summary:

Mark Hazleton's GitHub repository serves as a personal technology portfolio and learning platform, showcasing a collection of web development projects and experimental applications that demonstrate his ongoing technical exploration and skill development. The repository features multiple web-based projects like WebSpark (a comprehensive web application hosting demo projects) and ReactSpark (a React application built with Vite and deployed on Azure Static Web Applications), indicating a focus on modern web technologies and cloud deployment strategies. The projects appear to leverage contemporary web frameworks, with a strong emphasis on React, Azure cloud services, and static site generation, reflecting a cloud-native and JavaScript-centric development approach. The repository is not just a code collection but a dynamic learning archive, with blog posts and detailed documentation that provide insights into the author's technical thought processes, software development methodologies, and exploration of emerging technologies like AI and serverless architectures. What makes this repository unique is its transparent documentation of the learning journey, comprehensive GitHub stats visualization, and the author's commitment to showcasing not just code, but the context and reasoning behind technological choices. The target audience seems to be developers, technology enthusiasts, and professionals interested in web development, cloud technologies, and continuous learning in the software engineering ecosystem.

**Created**: 2021-04-17
**Last Modified**: 2026-01-29

---

### #17. [WebSpark.Bootswatch](https://github.com/markhazleton/WebSpark.Bootswatch)

Stars: 0 | Forks: 0 | Language: HTML | 19 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 7124 KB | 🚀 6.3 commits/month

**Quality**: ❌ License | ✅ Docs

WebSpark.Bootswatch is a .NET Razor Class Library designed to seamlessly integrate Bootswatch themes into ASP.NET Core applications, providing a robust theming solution built on Bootstrap 5 with advanced capabilities like dynamic theme switching, light/dark mode support, and comprehensive caching mechanisms. The library targets .NET 10.0 exclusively, offering high-performance theme management through features like `StyleCache` service, tag helper support, and responsive design with automatic theme detection and switching. Architecturally, it leverages modern .NET framework features, dependency injection, and extension methods to simplify theme integration, with a focus on providing a production-ready, easily configurable theming system that supports all official Bootswatch themes and custom theme implementations. Its unique value proposition lies in its comprehensive approach to theme management, offering developers a turnkey solution for creating visually dynamic and responsive web applications with minimal configuration overhead. The library is primarily targeted at ASP.NET Core developers seeking a sophisticated, performance-oriented theming solution with extensive customization options and built-in best practices for UI styling and responsiveness.

**Created**: 2022-08-24
**Last Modified**: 2026-01-12

---

### #18. [KeyPressCounter](https://github.com/markhazleton/KeyPressCounter)

Stars: 1 | Forks: 1 | Language: C# | 13 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 46573 KB | 🚀 4.3 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary of the KeyPressCounter repository:

KeyPressCounter is a sophisticated Windows utility designed for comprehensive system and user activity monitoring, leveraging .NET 10.0 and low-level system APIs to track keyboard/mouse interactions, system performance metrics, and resource utilization in real-time. The application employs a multi-layered monitoring approach using technologies like SharpHook for global input event tracking, Windows Performance Counters for system metrics, and WMI (Windows Management Instrumentation) for hardware information retrieval, creating a robust system tray application that provides granular insights into user behavior and computational resource consumption. Its architecture emphasizes privacy-conscious tracking, with features like idle time filtering, local data storage, and detailed logging, making it a powerful tool for productivity analysis, system diagnostics, and performance optimization. The project demonstrates advanced Windows system integration techniques, including registry management, single-instance protection, and seamless system tray interaction, with a modular design that allows for extensive customization of monitoring parameters and logging behaviors. Unique strengths include its comprehensive metrics collection, minimal system overhead, and user-friendly graphical interface that transforms complex system data into digestible visualizations and statistics. Ideal for system administrators, developers, researchers, and power users seeking deep insights into computer usage patterns and system performance characteristics.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 4 total (4 current, 0 outdated)

**Created**: 2024-03-07
**Last Modified**: 2026-01-15

---

### #19. [sql2csv](https://github.com/markhazleton/sql2csv)

Stars: 0 | Forks: 0 | Language: C# | 6 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 1891 KB | 🚀 2.0 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary of the sql2csv repository:

Sql2Csv is a comprehensive .NET 10 toolkit designed for SQLite database manipulation and analysis, offering robust capabilities for database file discovery, table export, schema introspection, and code generation across both CLI and web interfaces. The project provides multi-modal functionality including command-line and web-based interactions for tasks like exporting database tables to CSV, generating detailed schema reports, and automatically creating C# data transfer objects (DTOs) from database schemas. Built using modern .NET technologies with a modular architecture featuring separate projects for core services, console application, web interface, and testing, the toolkit leverages dependency injection, ASP.NET Core MVC, and supports flexible configuration through appsettings. Its unique value proposition lies in its comprehensive approach to SQLite database exploration, offering developers and data analysts a versatile tool for database metadata extraction, transformation, and code generation with support for various output formats and programmatic interactions. The project is particularly useful for scenarios involving database migration, data analysis, code generation, and rapid prototyping across different development and data engineering workflows.

**Created**: 2017-11-06
**Last Modified**: 2026-01-12

---

### #20. [ConcurrentProcessing](https://github.com/markhazleton/ConcurrentProcessing)

Stars: 0 | Forks: 0 | Language: C# | 19 commits (90d)

👥 0 contributors | 🌐 1 languages | 💾 139 KB | 🚀 6.3 commits/month

**Quality**: ❌ License | ✅ Docs

ConcurrentProcessing is a sophisticated .NET 10 framework for managing high-performance parallel task execution, providing developers with a robust, generic abstract base class (`ConcurrentProcessor<T>`) for implementing complex concurrent processing scenarios with fine-grained control over task parallelism. The library leverages semaphore-based throttling to precisely manage concurrent task limits, offering built-in performance metrics tracking that automatically calculates statistical insights like minimum, maximum, and average task durations, wait times, and throughput. Architecturally, the project implements several design patterns including Template Method, Factory, and Strategy patterns, enabling extensible and type-safe task processing with minimal runtime overhead and excellent scalability across various workloads. Designed as both a production-ready framework and an educational resource, ConcurrentProcessing demonstrates advanced concurrent programming techniques in C#, showcasing best practices for managing parallel execution with comprehensive performance monitoring and analysis capabilities. The framework is particularly valuable for developers working on systems requiring controlled concurrent processing, such as data pipelines, batch job processors, or distributed computing scenarios that demand precise resource management and performance optimization. Its generic, strongly-typed design, combined with built-in metrics and configuration flexibility, makes it a powerful tool for creating efficient, observable concurrent processing solutions across different domains.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 2 total (2 current, 0 outdated)

**Created**: 2023-09-18
**Last Modified**: 2026-01-22

---

### #21. [react-native-web-start](https://github.com/markhazleton/react-native-web-start)

Stars: 0 | Forks: 0 | Language: TypeScript | 1 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 3183 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

Based on the detailed README and repository analysis, here's a comprehensive technical summary:

The react-native-web-start repository is an advanced cross-platform application development starter template designed to enable developers to build production-ready mobile and web applications using a unified TypeScript codebase. Leveraging React Native Web, Vite, and a modern web stack, this template provides a comprehensive solution for creating responsive, high-performance applications that can be deployed seamlessly across web, iOS, and Android platforms. The project implements a sophisticated monorepo architecture with shared components, dedicated web and mobile packages, and a robust development environment featuring type-safe TypeScript, Tailwind CSS for styling, automated build processes, and comprehensive developer tooling including hot module replacement, code splitting, and integrated testing configurations. Key differentiators include its emphasis on enterprise-grade features like performance optimization, security integrations (Dependabot), PWA readiness, and a flexible, scalable project structure that supports true cross-platform development with minimal platform-specific code. The template is particularly valuable for developers and teams seeking a standardized, modern approach to multi-platform application development that prioritizes code reusability, developer experience, and production-ready configurations.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 49 total (49 current, 0 outdated)

**Created**: 2025-07-26
**Last Modified**: 2026-01-14

---

### #22. [TaskListProcessor](https://github.com/markhazleton/TaskListProcessor)

Stars: 0 | Forks: 0 | Language: C# | 12 commits (90d)

👥 0 contributors | 🌐 3 languages | 💾 1070 KB | 🚀 4.0 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary of the TaskListProcessor repository:

TaskListProcessor is an advanced .NET 10.0 library designed to solve complex asynchronous task orchestration challenges in enterprise-level applications, providing a robust framework for managing and executing concurrent operations with high reliability and performance. The library implements sophisticated enterprise-grade patterns including circuit breakers, dependency injection, advanced scheduling, and comprehensive telemetry, enabling developers to build resilient, observable, and highly scalable distributed systems with type-safe and configurable task processing capabilities. Key architectural features include parallel task execution with configurable concurrency limits, OpenTelemetry integration for rich observability, native .NET dependency injection support, and intelligent task dependency resolution using topological sorting and priority-based scheduling strategies. The project stands out by offering a holistic approach to async processing, addressing common challenges like fault isolation, performance monitoring, and complex workflow coordination through a clean, strongly-typed interface that follows SOLID design principles. Targeting enterprise developers, microservice architects, and high-throughput system designers, TaskListProcessor provides a comprehensive solution for managing complex asynchronous workloads across various domains such as distributed computing, API orchestration, data processing, and event-driven architectures. The library's design emphasizes developer experience, offering extensive documentation, learning paths, and practical examples to facilitate quick adoption and effective implementation of advanced task processing patterns.

**Created**: 2023-11-09
**Last Modified**: 2026-01-12

---

### #23. [WebProjectMechanics](https://github.com/markhazleton/WebProjectMechanics)

Stars: 3 | Forks: 0 | Language: Visual Basic .NET | 0 commits (90d)

👥 0 contributors | 🌐 9 languages | 💾 53211 KB | 🚀 0 commits/month

**Quality**: ❌ License | ✅ Docs

Web Project Mechanics is a custom web content management system (CMS) designed to manage multiple websites using a single MS-Access database, developed primarily in Visual Basic .NET and ASP.NET. The system provides a flexible, standalone platform for website management without external dependencies, leveraging caching mechanisms to improve performance and supporting migrations across different web technologies (from ASP to JSP to .NET Framework 4.8). Architecturally, it appears to use a centralized database approach with multi-site support, allowing administrators to manage content across different websites from a unified backend interface. The project's unique characteristics include its long-term development history (spanning over 20 years), minimal external dependencies, and a lightweight approach to web content management that prioritizes simplicity and portability. Targeted primarily at small to medium-sized website owners, developers, and organizations seeking a straightforward, self-contained CMS solution, Web Project Mechanics represents a personal project that has evolved to serve practical web management needs while serving as a technology learning platform for its creator.

**Created**: 2017-09-19
**Last Modified**: 2025-02-26

---

### #24. [markhazleton.github.io](https://github.com/markhazleton/markhazleton.github.io)

Stars: 0 | Forks: 0 | Language: SCSS | 5 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 136 KB | 🚀 1.7 commits/month

**Quality**: ❌ License | ✅ Docs

Technical Repository Summary:

This is a personal Jekyll-powered static website repository designed for Mark Hazleton's professional and blogging needs, hosted on GitHub Pages. The site leverages a customized Minima theme with modern web development practices, featuring a responsive design, dark/light mode toggle, and comprehensive content management workflow for technical blogging. Built using Ruby 3.2.2, Jekyll 3.10.0, and SCSS, the repository demonstrates a well-structured static site generator approach with robust development and deployment automation via GitHub Actions. The project emphasizes developer experience through detailed documentation, local development setup instructions, and best practices for content creation, including SEO optimization, post structuring guidelines, and flexible publishing workflows. Its unique strengths include a clean, framework-agnostic implementation, extensive post creation guidelines, and a focus on maintainability and extensibility for personal/professional technical communication.

Key Technical Highlights:
- Static site generation with Jekyll
- Custom Minima theme implementation
- GitHub Pages hosting
- Automated CI/CD via GitHub Actions
- Comprehensive development and publishing documentation
- Dark/light mode support
- Responsive design
- SEO-friendly content management

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 3 total (3 current, 0 outdated)

**Created**: 2021-04-18
**Last Modified**: 2026-01-12

---

### #25. [AsyncDemo](https://github.com/markhazleton/AsyncDemo)

Stars: 0 | Forks: 0 | Language: C# | 15 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 1555 KB | 🚀 5.0 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary of the AsyncDemo repository:

AsyncDemo is an educational C# project demonstrating advanced asynchronous programming techniques and best practices in .NET, focusing on solving common async/await challenges through practical, real-world code examples. The repository provides a comprehensive learning platform for developers, featuring interactive API documentation powered by Scalar, and showcasing critical async patterns such as cancellation token management, concurrency control, resilience with Polly, and cross-cutting concern implementation using the decorator pattern. Built on .NET 10 and integrating with external APIs like OpenWeather, the project offers structured learning modules that explore scenarios like avoiding deadlocks, implementing timeouts, throttling concurrent operations, and handling complex asynchronous workflows through meticulously organized API endpoints. The unique value proposition lies in its combination of hands-on code demonstrations, extensive documentation, and a systematic approach to teaching advanced async programming concepts, making it an invaluable resource for .NET developers seeking to master asynchronous programming techniques. By providing real-world implementations and clear learning objectives, AsyncDemo serves as both a reference implementation and an educational tool for developers looking to improve their understanding of asynchronous programming patterns and best practices.

**Created**: 2022-08-07
**Last Modified**: 2025-12-04

---

### #26. [InquirySpark](https://github.com/markhazleton/InquirySpark)

Stars: 0 | Forks: 0 | Language: C# | 18 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 9371 KB | 🚀 6.0 commits/month

**Quality**: ❌ License | ✅ Docs

InquirySpark is a .NET 10-based survey and inquiry management system designed for read-only data interaction, utilizing an MVC architecture with a focus on immutable SQLite databases and strict data access patterns. The solution provides a comprehensive admin interface built with Bootstrap 5 and DataTables, enabling users to interact with survey data through a robust, warning-free implementation that emphasizes type safety, dependency injection, and centralized configuration. Key technologies include Entity Framework Core 10, Microsoft.Data.Sqlite provider, ASP.NET Core Identity, and a modular project structure spanning admin, repository, and common libraries with integrated unit testing via MSTest. The project's unique approach lies in its enforcement of read-only database interactions, elimination of SQL Server dependencies, and a carefully designed persistence layer that prevents schema or data mutations while providing a flexible, scalable framework for survey management. Target users include administrators and organizations seeking a lightweight, secure, and easily deployable survey management solution with minimal infrastructure requirements and strong architectural constraints.

**Created**: 2023-10-24
**Last Modified**: 2025-12-07

---

### #27. [HttpClientDecoratorPattern](https://github.com/markhazleton/HttpClientDecoratorPattern)

Stars: 0 | Forks: 0 | Language: HTML | 1 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 2675 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary:

This repository demonstrates a production-ready implementation of the Decorator Pattern for HttpClient in .NET, providing a sophisticated approach to managing HTTP communication with enhanced resilience, telemetry, and caching capabilities. The project introduces a flexible, composable service architecture that allows dynamically adding cross-cutting concerns like performance monitoring, circuit breaking, and caching without modifying core service implementations. Leveraging .NET 10, dependency injection, and libraries like Polly, the implementation offers a robust solution for enterprise-grade HTTP client management, with strong emphasis on separation of concerns, testability, and observability. The WebSpark.HttpClientUtility package serves as the core implementation, featuring a comprehensive decorator chain that systematically wraps HTTP requests with additional behaviors such as retry policies, correlation tracking, and intelligent caching strategies. By providing a clean, extensible pattern for HTTP communication, the project addresses common challenges in distributed system design, making it particularly valuable for developers building microservices, API-driven applications, or systems requiring sophisticated HTTP interaction management.

**Created**: 2023-02-09
**Last Modified**: 2026-01-12

---

### #28. [Yelp.Api](https://github.com/markhazleton/Yelp.Api)

Stars: 0 | Forks: 0 | Language: C# | 1 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 462 KB | 🚀 0.3 commits/month

**Quality**: ❌ License | ❌ Docs

Here's a comprehensive technical summary for the Yelp.Api repository:

The Yelp.Api is a C# class library that provides a robust, developer-friendly wrapper for Yelp's v3 Fusion API, enabling .NET developers to easily integrate local business search and review functionality into their applications. Leveraging .NET 6 and designed with a clean, intuitive interface, the library simplifies complex API interactions by offering methods like `SearchBusinessesAllAsync()` that abstract away the underlying HTTP communication and authentication complexities. The library supports comprehensive search capabilities, including geolocation-based queries, filtering by business attributes (such as open now status), and retrieving detailed business information across 32 countries with minimal configuration required. Its design follows a client-centric architectural pattern, where developers can instantiate a `Yelp.Api.Client` with an API key and immediately perform sophisticated local business searches using either simple method signatures or more granular `SearchParameters` objects. Unique strengths include its strong typing, async support, and straightforward usage that reduces the typical boilerplate code associated with external API integrations. The primary target users are .NET developers building location-aware applications such as travel guides, restaurant recommendation systems, local service aggregators, or any software requiring rich, up-to-date local business data.

**Created**: 2022-08-10
**Last Modified**: 2026-01-12

---

### #29. [PromptSpark.Chat](https://github.com/markhazleton/PromptSpark.Chat)

Stars: 0 | Forks: 0 | Language: C# | 7 commits (90d)

👥 0 contributors | 🌐 5 languages | 💾 19281 KB | 🚀 2.3 commits/month

**Quality**: ❌ License | ✅ Docs

Here's a comprehensive technical summary for the PromptSpark.Chat repository:

PromptSpark.Chat is an innovative ASP.NET Core web application that enables dynamic, interactive conversational workflows through a real-time chat interface powered by SignalR and Adaptive Cards. The platform allows users to engage in multi-step, guided conversations with flexible branching logic, supporting complex interaction scenarios by dynamically rendering interactive UI elements and managing conversation state using thread-safe server-side storage. Leveraging modern web technologies like C#, SignalR, and optional AI integration, the application provides a robust framework for creating structured, context-aware conversational experiences with built-in persistence and extensibility. The architecture emphasizes modularity, with a clear separation of concerns between workflow management, real-time communication, and user interaction, making it particularly suitable for scenarios requiring guided user experiences such as surveys, onboarding processes, or interactive decision trees. What distinguishes PromptSpark.Chat is its elegant approach to managing conversational complexity through adaptive cards, server-side state management, and a flexible workflow definition mechanism that allows developers to easily configure and extend conversation flows without extensive custom coding.

**Created**: 2024-12-31
**Last Modified**: 2026-01-12

---

### #30. [WebSpark.PrismSpark](https://github.com/markhazleton/WebSpark.PrismSpark)

Stars: 0 | Forks: 0 | Language: HTML | 6 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 2090 KB | 🚀 2.0 commits/month

**Quality**: ❌ License | ✅ Docs

WebSpark.PrismSpark is a sophisticated .NET-based syntax highlighting library inspired by PrismJS, designed to provide advanced code rendering and tokenization capabilities for multiple programming languages. The library offers a comprehensive suite of features including support for 20+ programming languages, a plugin system, theme generation, async processing, and extensible highlighting mechanisms with robust .NET 10.0 LTS compatibility. Architecturally, it implements a modular design with interfaces like `IHighlighter`, `IPlugin`, and `ITheme`, enabling developers to easily customize and extend syntax highlighting through dependency injection, hooks, and context-aware processing. The project distinguishes itself through its performance-oriented approach, supporting advanced options like line number rendering, context-based metadata, and dynamic theme generation, making it particularly valuable for web developers, documentation platforms, and code presentation frameworks targeting .NET ecosystems. By providing a type-safe, performant alternative to traditional syntax highlighting libraries, WebSpark.PrismSpark offers developers a powerful tool for rendering and styling code snippets across various .NET web frameworks like MVC, Razor, and potentially Blazor.

**Created**: 2025-05-27
**Last Modified**: 2026-01-05

---

### #31. [TeachSpark](https://github.com/markhazleton/TeachSpark)

Stars: 0 | Forks: 0 | Language: C# | 2 commits (90d)

👥 0 contributors | 🌐 6 languages | 💾 30635 KB | 🚀 0.7 commits/month

**Quality**: ❌ License | ✅ Docs

Technical Summary:

TeachSpark is an advanced, AI-powered educational web platform built using .NET 10 MVC and modern web technologies, designed to create personalized learning experiences through Large Language Model (LLM) integration. The project leverages a clean architecture approach, combining a robust C# backend with a sophisticated frontend built using Webpack, Bootstrap, and modern JavaScript, enabling dynamic, adaptive curriculum delivery with real-time personalization and comprehensive learning analytics. Key technological highlights include intelligent content adaptation, responsive design, comprehensive build tooling with automated quality checks, and a modular architecture that supports scalable, performance-optimized educational experiences. The platform distinguishes itself through its AI-driven personalization, offering customized learning pathways that dynamically adjust content based on individual student interactions and learning patterns. Targeting educators, students, and educational technology professionals, TeachSpark represents a cutting-edge approach to digital learning platforms that emphasizes technological innovation, user experience, and data-driven educational methodology.

**Technology Stack Currency**: ✅ 50/100
**Dependencies**: 3 total (3 current, 0 outdated)

**Created**: 2025-06-19
**Last Modified**: 2026-01-12

---

### #32. [DecisionSpark](https://github.com/markhazleton/DecisionSpark)

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

### #33. [TriviaSpark](https://github.com/markhazleton/TriviaSpark)

Stars: 0 | Forks: 0 | Language: C# | 4 commits (90d)

👥 0 contributors | 🌐 4 languages | 💾 27238 KB | 🚀 1.3 commits/month

**Quality**: ❌ License | ✅ Docs

Technical Summary for TriviaSpark:

TriviaSpark is an experimental multiplayer web and mobile trivia game application developed with AI assistance, designed to provide an interactive and competitive trivia experience for tech-savvy users aged 18-95. The project is primarily built using C# with a web-based architecture, leveraging public Trivia APIs to dynamically generate question sets and enable real-time multiplayer interactions. Key planned features include user registration, a comprehensive leaderboard system, admin-level question database management, and a customizable user interface that supports both web and mobile platforms. The application appears to follow a modern, component-based development approach with potential use of .NET technologies for backend infrastructure and web frameworks for frontend rendering. What makes TriviaSpark unique is its explicit integration of AI in the development process, as highlighted by its README noting collaborative development with ChatGPT, which suggests an innovative approach to software design and potentially leveraging AI for dynamic content generation and user experience optimization. The project aims to create an engaging, knowledge-testing platform that combines competitive gameplay with accessible, technology-driven design.

**Created**: 2023-02-22
**Last Modified**: 2025-12-02

---

### #34. [DataAnalysisDemo](https://github.com/markhazleton/DataAnalysisDemo)

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

### #35. [PHPDocSpark](https://github.com/markhazleton/PHPDocSpark)

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

- **Generation Time**: 1.6 seconds
- **SVGs Generated**: 6/6
- **Total API Calls**: 0
- **Total AI Tokens**: 81,217
- **Success Rate**: 100.0%

### Data Sources

- GitHub API (public repositories only)
- Anthropic Claude API (repository summaries)
- Dependency package registries (npm, PyPI, RubyGems, Go, Maven, NuGet)

### Report Details

- **Composite Score Weights**: Popularity 30% • Activity 45% • Health 25%
- **Technology Currency**: Calculated from latest versions in package registries
- **AI Model**: claude-3-5-haiku-20241022

---

*Generated by [Stats Spark](https://github.com/markhazleton/github-stats-spark)*
*Last updated: 2026-01-31*