RICH_ROADMAPS = {
    "Frontend / UI Engineer": [
        {
            "title": "Foundation",
            "duration": "Month 1–2",
            "description": "Get solid on the fundamentals — HTML, CSS, and vanilla JavaScript. Everything you build later depends on this.",
            "learn": ["HTML5 semantics & accessibility", "CSS Flexbox & Grid", "JavaScript ES6+ basics", "DOM manipulation & events"],
            "resources": [
                {"icon": "📺", "name": "The Odin Project (free)"},
                {"icon": "📘", "name": "javascript.info"},
                {"icon": "🎯", "name": "CSS-Tricks guides"},
            ],
            "project": {"name": "Personal Portfolio", "desc": "Build and deploy your portfolio site with HTML/CSS/JS only. No frameworks.", "tag": "Beginner"}
        },
        {
            "title": "React & Ecosystem",
            "duration": "Month 3–5",
            "description": "Learn React deeply — components, hooks, state management, and how to structure real apps.",
            "learn": ["React components & JSX", "useState, useEffect, useContext", "React Router v6", "Tailwind CSS", "Vite & build tools"],
            "resources": [
                {"icon": "📺", "name": "React docs (react.dev)"},
                {"icon": "📘", "name": "Jack Herrington on YouTube"},
                {"icon": "🎯", "name": "Scrimba React course"},
            ],
            "project": {"name": "Full CRUD App", "desc": "Task manager or note-taking app with React. State, routing, and localStorage.", "tag": "Intermediate"}
        },
        {
            "title": "Performance & Advanced",
            "duration": "Month 6–8",
            "description": "Make your apps fast and production-ready. Learn what separates junior from senior frontend devs.",
            "learn": ["Web Vitals & performance audit", "Code splitting & lazy loading", "Accessibility (ARIA, keyboard nav)", "TypeScript basics", "Testing with Vitest/RTL"],
            "resources": [
                {"icon": "📺", "name": "web.dev/learn"},
                {"icon": "📘", "name": "TypeScript Handbook"},
                {"icon": "🎯", "name": "Kent C. Dodds blog"},
            ],
            "project": {"name": "UI Component Library", "desc": "Build a small design system with 5–8 reusable components, Storybook docs, and TypeScript.", "tag": "Advanced"}
        },
        {
            "title": "Job Prep",
            "duration": "Month 9–12",
            "description": "Polish your portfolio, practice interviews, and ship open source contributions.",
            "learn": ["DSA for frontend interviews", "System design basics (frontend)", "Open source contributions", "Resume & LinkedIn optimization"],
            "resources": [
                {"icon": "📺", "name": "Frontend Interview Handbook"},
                {"icon": "📘", "name": "greatfrontend.com"},
                {"icon": "🎯", "name": "Pramp for mock interviews"},
            ],
            "project": {"name": "Clone a Real Product", "desc": "Clone a complex UI (Notion, Linear, Figma) with React + TypeScript. Focus on detail.", "tag": "Portfolio"}
        },
    ],
    "Backend / Systems Engineer": [
        {
            "title": "Foundation",
            "duration": "Month 1–2",
            "description": "Get strong on programming fundamentals, data structures, and how the internet actually works.",
            "learn": ["Python or Node.js deeply", "HTTP, REST basics", "Linux command line", "Git workflows"],
            "resources": [
                {"icon": "📘", "name": "Python Docs / Node.js Docs"},
                {"icon": "📺", "name": "Hussein Nasser (YouTube)"},
                {"icon": "🎯", "name": "roadmap.sh/backend"},
            ],
            "project": {"name": "CLI Tool", "desc": "Build a command-line tool that does something useful — file organizer, URL shortener, etc.", "tag": "Beginner"}
        },
        {
            "title": "APIs & Databases",
            "duration": "Month 3–5",
            "description": "Build real REST APIs, connect them to databases, and handle auth properly.",
            "learn": ["REST API design", "PostgreSQL + SQL", "ORMs (SQLAlchemy / Prisma)", "JWT authentication", "Redis caching"],
            "resources": [
                {"icon": "📺", "name": "FastAPI / Express.js docs"},
                {"icon": "📘", "name": "Use The Index, Luke (SQL)"},
                {"icon": "🎯", "name": "SQLBolt for SQL practice"},
            ],
            "project": {"name": "REST API", "desc": "Build a production-quality API with auth, CRUD, pagination, and rate limiting.", "tag": "Intermediate"}
        },
        {
            "title": "System Design",
            "duration": "Month 6–9",
            "description": "Learn to design systems at scale. This is what separates junior from senior backend devs.",
            "learn": ["System design fundamentals", "Microservices & event-driven arch", "Message queues (Kafka/RabbitMQ)", "Docker & containerization", "Distributed systems basics"],
            "resources": [
                {"icon": "📘", "name": "Designing Data-Intensive Apps"},
                {"icon": "📺", "name": "ByteByteGo (YouTube)"},
                {"icon": "🎯", "name": "System Design Primer (GitHub)"},
            ],
            "project": {"name": "URL Shortener", "desc": "Build a bit.ly clone with Redis, rate limiting, analytics, and horizontal scaling design.", "tag": "Advanced"}
        },
        {
            "title": "Job Prep",
            "duration": "Month 10–12",
            "description": "Practice DSA, system design interviews, and contribute to open source.",
            "learn": ["DSA — arrays, graphs, DP", "System design mock interviews", "Open source contributions", "Behavioural interview prep"],
            "resources": [
                {"icon": "📺", "name": "NeetCode.io"},
                {"icon": "📘", "name": "Grokking System Design"},
                {"icon": "🎯", "name": "Pramp for mock interviews"},
            ],
            "project": {"name": "Open Source PR", "desc": "Contribute a meaningful feature or bug fix to a popular backend framework or tool.", "tag": "Portfolio"}
        },
    ],
    "Full Stack Developer": [
        {
            "title": "Foundation",
            "duration": "Month 1–2",
            "description": "Get comfortable with both ends — HTML/CSS/JS for frontend and Python/Node for backend.",
            "learn": ["HTML, CSS, JavaScript basics", "Node.js or Python basics", "Git & GitHub", "VS Code setup"],
            "resources": [
                {"icon": "📺", "name": "The Odin Project (free)"},
                {"icon": "📘", "name": "MDN Web Docs"},
                {"icon": "🎯", "name": "freeCodeCamp"},
            ],
            "project": {"name": "Static Website", "desc": "Build a multi-page static website about any topic you care about.", "tag": "Beginner"}
        },
        {
            "title": "React + Node Stack",
            "duration": "Month 3–6",
            "description": "Learn the most common fullstack combo — React on frontend, Express/Node + PostgreSQL on backend.",
            "learn": ["React components & hooks", "Express.js REST APIs", "PostgreSQL & SQL", "JWT auth end-to-end", "Fetch/Axios & async JS"],
            "resources": [
                {"icon": "📺", "name": "Traversy Media (YouTube)"},
                {"icon": "📘", "name": "fullstackopen.com (free)"},
                {"icon": "🎯", "name": "Fireship.io"},
            ],
            "project": {"name": "Full Stack App", "desc": "Build a complete app with login, dashboard, CRUD features, and a real database.", "tag": "Intermediate"}
        },
        {
            "title": "DevOps & Deployment",
            "duration": "Month 7–9",
            "description": "Learn to ship and scale. Deployment, CI/CD, Docker, and cloud basics.",
            "learn": ["Docker basics", "CI/CD with GitHub Actions", "Deploy to Railway/Render/AWS", "Environment variables & secrets", "Basic monitoring"],
            "resources": [
                {"icon": "📺", "name": "TechWorld with Nana (Docker)"},
                {"icon": "📘", "name": "GitHub Actions docs"},
                {"icon": "🎯", "name": "Railway.app for hosting"},
            ],
            "project": {"name": "Deployed SaaS MVP", "desc": "Take your fullstack app and fully deploy it — custom domain, CI/CD pipeline, live database.", "tag": "Advanced"}
        },
        {
            "title": "Job Prep",
            "duration": "Month 10–12",
            "description": "Build a strong portfolio, practice interviews, and ship side projects that get noticed.",
            "learn": ["DSA for interviews", "Portfolio polish", "Technical blog writing", "Open source contributions"],
            "resources": [
                {"icon": "📺", "name": "NeetCode for DSA"},
                {"icon": "📘", "name": "Portfolio inspiration: brittanychiang.com"},
                {"icon": "🎯", "name": "Dev.to for blogging"},
            ],
            "project": {"name": "2 Portfolio Projects", "desc": "Ship 2 polished fullstack projects with good README, live demo, and clean code.", "tag": "Portfolio"}
        },
    ],
    "Data Scientist / ML Engineer": [
        {
            "title": "Foundation",
            "duration": "Month 1–3",
            "description": "Get solid on Python, statistics, and the core data manipulation tools every data scientist needs.",
            "learn": ["Python for data (pandas, numpy)", "Statistics & probability", "Data visualization (matplotlib, seaborn)", "SQL for data analysis"],
            "resources": [
                {"icon": "📘", "name": "Python for Data Analysis (book)"},
                {"icon": "📺", "name": "StatQuest (YouTube)"},
                {"icon": "🎯", "name": "Kaggle Learn (free)"},
            ],
            "project": {"name": "EDA Project", "desc": "Pick a Kaggle dataset and do a full exploratory data analysis with charts and a write-up.", "tag": "Beginner"}
        },
        {
            "title": "Machine Learning",
            "duration": "Month 4–7",
            "description": "Learn classical ML algorithms, feature engineering, and how to evaluate models properly.",
            "learn": ["Scikit-learn ML algorithms", "Feature engineering & selection", "Model evaluation (CV, metrics)", "Overfitting & regularization", "Ensemble methods (XGBoost, RF)"],
            "resources": [
                {"icon": "📺", "name": "fast.ai Practical ML"},
                {"icon": "📘", "name": "Hands-On ML (Géron)"},
                {"icon": "🎯", "name": "Kaggle competitions"},
            ],
            "project": {"name": "ML Pipeline", "desc": "Build a full ML pipeline — data cleaning, feature engineering, training, evaluation, and a prediction API.", "tag": "Intermediate"}
        },
        {
            "title": "Deep Learning & NLP",
            "duration": "Month 8–10",
            "description": "Go beyond classical ML into neural networks, PyTorch, and modern NLP/LLM techniques.",
            "learn": ["Neural networks & backprop", "PyTorch fundamentals", "CNNs for vision tasks", "Transformers & HuggingFace", "RAG & LLM fine-tuning basics"],
            "resources": [
                {"icon": "📺", "name": "Andrej Karpathy (YouTube)"},
                {"icon": "📘", "name": "Deep Learning (Goodfellow)"},
                {"icon": "🎯", "name": "HuggingFace courses"},
            ],
            "project": {"name": "NLP App", "desc": "Build a text classification or summarization app using a HuggingFace model with a simple web UI.", "tag": "Advanced"}
        },
        {
            "title": "Job Prep & MLOps",
            "duration": "Month 11–12",
            "description": "Learn to deploy models, build your portfolio on Kaggle, and prep for data science interviews.",
            "learn": ["Model deployment (FastAPI + Docker)", "MLflow for experiment tracking", "Statistics interview prep", "Case study practice"],
            "resources": [
                {"icon": "📺", "name": "Made With ML (mlops)"},
                {"icon": "📘", "name": "Ace the Data Science Interview (book)"},
                {"icon": "🎯", "name": "StrataScratch for SQL/stats prep"},
            ],
            "project": {"name": "Deployed ML API", "desc": "Deploy a trained model as a REST API with FastAPI + Docker. Include a simple frontend to demo it.", "tag": "Portfolio"}
        },
    ],
    "DevOps / Cloud Engineer": [
        {
            "title": "Foundation",
            "duration": "Month 1–2",
            "description": "Get comfortable with Linux, networking, and scripting — the bedrock of all DevOps work.",
            "learn": ["Linux CLI & shell scripting", "Networking basics (TCP/IP, DNS, HTTP)", "Git & version control", "Bash scripting"],
            "resources": [
                {"icon": "📘", "name": "Linux Command Line (book)"},
                {"icon": "📺", "name": "NetworkChuck (YouTube)"},
                {"icon": "🎯", "name": "OverTheWire for Linux practice"},
            ],
            "project": {"name": "Bash Automation", "desc": "Write a bash script that automates a real task — backups, log rotation, server health checks.", "tag": "Beginner"}
        },
        {
            "title": "Docker & Kubernetes",
            "duration": "Month 3–5",
            "description": "Containers are the core of modern DevOps. Master Docker first, then Kubernetes.",
            "learn": ["Docker — images, containers, Dockerfile", "docker-compose for local dev", "Kubernetes fundamentals", "Helm charts", "Container security basics"],
            "resources": [
                {"icon": "📺", "name": "TechWorld with Nana (YouTube)"},
                {"icon": "📘", "name": "Kubernetes docs (k8s.io)"},
                {"icon": "🎯", "name": "Play with Kubernetes (free lab)"},
            ],
            "project": {"name": "Dockerized App", "desc": "Take any app and containerize it with Docker. Add docker-compose with a database and reverse proxy.", "tag": "Intermediate"}
        },
        {
            "title": "Cloud & CI/CD",
            "duration": "Month 6–9",
            "description": "Get certified in AWS or GCP and build automated CI/CD pipelines.",
            "learn": ["AWS core services (EC2, S3, RDS, Lambda)", "Terraform for IaC", "GitHub Actions & Jenkins", "Monitoring (Prometheus, Grafana)", "CloudWatch & alerting"],
            "resources": [
                {"icon": "📺", "name": "Adrian Cantrill AWS course"},
                {"icon": "📘", "name": "Terraform Up & Running (book)"},
                {"icon": "🎯", "name": "AWS Free Tier for practice"},
            ],
            "project": {"name": "Full CI/CD Pipeline", "desc": "Set up a pipeline that auto-builds, tests, and deploys a containerized app to AWS on every push.", "tag": "Advanced"}
        },
        {
            "title": "Job Prep",
            "duration": "Month 10–12",
            "description": "Get your AWS/GCP certification, polish your GitHub, and practice SRE interview questions.",
            "learn": ["AWS Solutions Architect exam prep", "SRE interview questions", "On-call incident management", "Cost optimization strategies"],
            "resources": [
                {"icon": "📺", "name": "Stephane Maarek (Udemy)"},
                {"icon": "📘", "name": "Google SRE Book (free online)"},
                {"icon": "🎯", "name": "killer.sh for exam practice"},
            ],
            "project": {"name": "Infrastructure as Code", "desc": "Provision a full 3-tier architecture on AWS using only Terraform. Document it thoroughly.", "tag": "Portfolio"}
        },
    ],
    "Cybersecurity / DevSecOps Engineer": [
        {
            "title": "Foundation",
            "duration": "Month 1–2",
            "description": "Build a strong foundation in networking, Linux, and basic security concepts before specializing.",
            "learn": ["Networking — TCP/IP, DNS, HTTP, TLS", "Linux fundamentals", "Basic cryptography concepts", "OWASP Top 10 awareness"],
            "resources": [
                {"icon": "📺", "name": "Professor Messer (free)"},
                {"icon": "📘", "name": "CompTIA Security+ study guide"},
                {"icon": "🎯", "name": "TryHackMe beginner paths"},
            ],
            "project": {"name": "Home Lab", "desc": "Set up a virtual home lab with VirtualBox — run Kali Linux and practice basic enumeration.", "tag": "Beginner"}
        },
        {
            "title": "Offensive Security",
            "duration": "Month 3–6",
            "description": "Learn to think like an attacker. Understanding how to break systems is how you learn to defend them.",
            "learn": ["Penetration testing methodology", "Web app vulnerabilities (SQLi, XSS, IDOR)", "Burp Suite", "Metasploit basics", "CTF challenges"],
            "resources": [
                {"icon": "📺", "name": "IppSec (HackTheBox writeups)"},
                {"icon": "📘", "name": "Web Application Hackers Handbook"},
                {"icon": "🎯", "name": "HackTheBox / PicoCTF"},
            ],
            "project": {"name": "CTF Writeup", "desc": "Complete 5 HackTheBox/TryHackMe machines and write detailed walkthroughs for your portfolio.", "tag": "Intermediate"}
        },
        {
            "title": "Defensive & DevSecOps",
            "duration": "Month 7–10",
            "description": "Learn how to build security into the SDLC — SAST, DAST, secrets management, and incident response.",
            "learn": ["SAST/DAST tools (SonarQube, OWASP ZAP)", "Secrets management (Vault, AWS Secrets Manager)", "SIEM basics (Splunk, ELK)", "Cloud security (AWS IAM, GuardDuty)", "Threat modelling"],
            "resources": [
                {"icon": "📺", "name": "John Hammond (YouTube)"},
                {"icon": "📘", "name": "Hacking APIs (Corey Ball)"},
                {"icon": "🎯", "name": "OWASP resources"},
            ],
            "project": {"name": "Security Pipeline", "desc": "Add SAST, dependency scanning, and secrets detection to a CI/CD pipeline. Write a security report.", "tag": "Advanced"}
        },
        {
            "title": "Certification & Job Prep",
            "duration": "Month 11–12",
            "description": "Get certified and build a portfolio that shows hands-on skills, not just knowledge.",
            "learn": ["CEH or eJPT exam prep", "Bug bounty basics", "Security report writing", "Interview prep — scenario questions"],
            "resources": [
                {"icon": "📺", "name": "TCM Security courses"},
                {"icon": "📘", "name": "Bug Bounty Bootcamp (book)"},
                {"icon": "🎯", "name": "HackerOne for bug bounties"},
            ],
            "project": {"name": "Bug Bounty Report", "desc": "Submit a valid bug bounty report on HackerOne or BugCrowd. Even a low severity one counts.", "tag": "Portfolio"}
        },
    ],
    "AI / ML Research Engineer": [
        {
            "title": "Foundation",
            "duration": "Month 1–3",
            "description": "Build a rock solid math and Python foundation. AI research requires depth, not shortcuts.",
            "learn": ["Linear algebra & calculus (3Blue1Brown)", "Probability & statistics", "Python + NumPy deeply", "Reading research papers (arxiv.org)"],
            "resources": [
                {"icon": "📺", "name": "3Blue1Brown (YouTube)"},
                {"icon": "📘", "name": "Mathematics for ML (book, free)"},
                {"icon": "🎯", "name": "Papers With Code"},
            ],
            "project": {"name": "Implement from Scratch", "desc": "Implement a neural network from scratch with only NumPy — no PyTorch. Understand backprop.", "tag": "Beginner"}
        },
        {
            "title": "PyTorch & Deep Learning",
            "duration": "Month 4–7",
            "description": "Get deep into PyTorch, CNNs, RNNs, and attention mechanisms — the core tools of modern AI.",
            "learn": ["PyTorch tensors & autograd", "CNNs for vision", "RNNs & LSTMs", "Transformer architecture", "Training tricks (LR scheduling, regularization)"],
            "resources": [
                {"icon": "📺", "name": "Andrej Karpathy lectures"},
                {"icon": "📘", "name": "Deep Learning (Goodfellow) — free PDF"},
                {"icon": "🎯", "name": "fast.ai course (free)"},
            ],
            "project": {"name": "Implement a Paper", "desc": "Reproduce a classic paper from scratch — ResNet, Attention Is All You Need, or GPT-2 at mini scale.", "tag": "Intermediate"}
        },
        {
            "title": "LLMs & Advanced Topics",
            "duration": "Month 8–10",
            "description": "Go deep on language models, fine-tuning, and the frontier research happening right now.",
            "learn": ["Transformers & HuggingFace", "LoRA & PEFT fine-tuning", "RLHF basics", "RAG architecture", "Multimodal models"],
            "resources": [
                {"icon": "📺", "name": "Yannic Kilcher (paper reviews)"},
                {"icon": "📘", "name": "HuggingFace NLP course (free)"},
                {"icon": "🎯", "name": "LeetCode + ML interview prep"},
            ],
            "project": {"name": "Fine-tuned LLM", "desc": "Fine-tune an open-source LLM (Mistral, LLaMA) on a domain-specific dataset using LoRA.", "tag": "Advanced"}
        },
        {
            "title": "Research & Job Prep",
            "duration": "Month 11–12",
            "description": "Write your own paper, build your GitHub research portfolio, and prep for ML engineering interviews.",
            "learn": ["Research methodology & writing", "MLOps (experiment tracking, model serving)", "ML system design interviews", "Open source contributions to ML frameworks"],
            "resources": [
                {"icon": "📺", "name": "AI research blogs (OpenAI, DeepMind, Anthropic)"},
                {"icon": "📘", "name": "arxiv.org daily reading habit"},
                {"icon": "🎯", "name": "Weights & Biases for experiment tracking"},
            ],
            "project": {"name": "Research Blog / Paper", "desc": "Write a technical blog post or mini paper on something you implemented. Publish on arxiv or Towards Data Science.", "tag": "Portfolio"}
        },
    ],
    "Product Manager / Tech Lead": [
        {
            "title": "Foundation",
            "duration": "Month 1–2",
            "description": "Understand users, products, and how tech products actually get built. Read widely.",
            "learn": ["Product thinking fundamentals", "User research methods", "Agile & Scrum basics", "Basic SQL for data queries"],
            "resources": [
                {"icon": "📘", "name": "Inspired — Marty Cagan"},
                {"icon": "📺", "name": "Lenny's Podcast"},
                {"icon": "🎯", "name": "Product School free resources"},
            ],
            "project": {"name": "Product Teardown", "desc": "Pick an app you use daily and write a 1000-word teardown — what works, what doesn't, and what you'd change.", "tag": "Beginner"}
        },
        {
            "title": "Core PM Skills",
            "duration": "Month 3–5",
            "description": "Get hands-on with PRDs, roadmapping, metrics, and talking to real users.",
            "learn": ["Writing PRDs & user stories", "OKRs & metrics definition", "Roadmap prioritization (RICE, MoSCoW)", "User interview techniques", "A/B testing basics"],
            "resources": [
                {"icon": "📘", "name": "Continuous Discovery Habits"},
                {"icon": "📺", "name": "GoPractice Simulator"},
                {"icon": "🎯", "name": "Mixpanel / Amplitude for analytics"},
            ],
            "project": {"name": "Real PRD", "desc": "Write a full PRD for a feature of a real product. Include user research, metrics, and success criteria.", "tag": "Intermediate"}
        },
        {
            "title": "Technical Depth",
            "duration": "Month 6–9",
            "description": "Technical PMs and tech leads stand out. Get comfortable with APIs, system design, and talking to engineers as peers.",
            "learn": ["APIs — how REST & GraphQL work", "System design basics (as a non-engineer)", "Reading & writing basic SQL", "Data analysis with Python/Excel", "Security & privacy fundamentals"],
            "resources": [
                {"icon": "📺", "name": "ByteByteGo system design"},
                {"icon": "📘", "name": "Swipe to Unlock (book)"},
                {"icon": "🎯", "name": "Mode Analytics for SQL practice"},
            ],
            "project": {"name": "Data-Driven Case Study", "desc": "Analyze a real dataset, identify a product problem, and write a recommendation backed by data.", "tag": "Advanced"}
        },
        {
            "title": "Portfolio & Job Prep",
            "duration": "Month 10–12",
            "description": "Build your PM portfolio, practice case interviews, and network intentionally.",
            "learn": ["PM case interview frameworks", "Portfolio building (Notion PM portfolio)", "Stakeholder management stories (STAR)", "Negotiation basics"],
            "resources": [
                {"icon": "📺", "name": "Exponent PM interview prep"},
                {"icon": "📘", "name": "Cracking the PM Interview"},
                {"icon": "🎯", "name": "PM Exercises for practice"},
            ],
            "project": {"name": "PM Portfolio", "desc": "Build a Notion PM portfolio with 3 case studies — a teardown, a PRD, and a metrics deep dive.", "tag": "Portfolio"}
        },
    ],
    "Mobile App Developer": [
        {
            "title": "Foundation",
            "duration": "Month 1–2",
            "description": "Decide your path — React Native (if you know JS) or Flutter (Dart). Get the basics solid.",
            "learn": ["JavaScript/Dart fundamentals", "React Native OR Flutter setup", "Expo for quick prototyping", "Mobile UX principles"],
            "resources": [
                {"icon": "📺", "name": "Expo docs (React Native)"},
                {"icon": "📘", "name": "Flutter docs (flutter.dev)"},
                {"icon": "🎯", "name": "React Native Express (free)"},
            ],
            "project": {"name": "To-Do App", "desc": "Build a simple to-do app with local state, navigation, and a clean mobile UI.", "tag": "Beginner"}
        },
        {
            "title": "Core Mobile Skills",
            "duration": "Month 3–6",
            "description": "Go deep on navigation, state management, device APIs, and connecting to backend services.",
            "learn": ["Navigation (React Navigation / Go Router)", "State management (Zustand / Riverpod)", "REST API integration", "Camera, location, push notifications", "AsyncStorage / SQLite"],
            "resources": [
                {"icon": "📺", "name": "William Candillon (React Native)"},
                {"icon": "📘", "name": "Flutter cookbook (official)"},
                {"icon": "🎯", "name": "Snack.expo.dev for quick testing"},
            ],
            "project": {"name": "Full Mobile App", "desc": "Build a complete app with login, API integration, and at least 4 screens. Deploy to Expo Go.", "tag": "Intermediate"}
        },
        {
            "title": "Performance & Native",
            "duration": "Month 7–9",
            "description": "Understand native performance, animations, and how to write native modules when needed.",
            "learn": ["Reanimated 2 / Flutter animations", "Performance profiling (Flipper)", "Native modules basics", "App Store / Play Store submission", "Offline-first architecture"],
            "resources": [
                {"icon": "📺", "name": "Software Mansion (YouTube)"},
                {"icon": "📘", "name": "High Performance React Native (blog)"},
                {"icon": "🎯", "name": "Apple Developer / Android Developer docs"},
            ],
            "project": {"name": "Animated UI", "desc": "Rebuild a complex UI with smooth animations — carousel, parallax scroll, gesture-based interactions.", "tag": "Advanced"}
        },
        {
            "title": "Ship & Job Prep",
            "duration": "Month 10–12",
            "description": "Ship your app to both stores, gather real users, and build a portfolio that stands out.",
            "learn": ["App Store Optimization (ASO)", "Crash reporting (Sentry)", "Analytics (Mixpanel / Firebase)", "Mobile interview prep"],
            "resources": [
                {"icon": "📺", "name": "Indie Hackers (mobile stories)"},
                {"icon": "📘", "name": "App Store Review Guidelines"},
                {"icon": "🎯", "name": "Mobile dev interview handbook"},
            ],
            "project": {"name": "Published App", "desc": "Ship a real app to the App Store and/or Play Store. Even 10 downloads proves you can ship.", "tag": "Portfolio"}
        },
    ],
    "Data Analyst / Business Intelligence": [
        {
            "title": "Foundation",
            "duration": "Month 1–2",
            "description": "SQL and Excel are the bread and butter of data analysis. Get genuinely good at both.",
            "learn": ["SQL — SELECT, JOINs, GROUP BY, window functions", "Excel / Google Sheets deeply", "Statistics basics", "Data cleaning principles"],
            "resources": [
                {"icon": "📘", "name": "Mode SQL Tutorial (free)"},
                {"icon": "📺", "name": "Alex The Analyst (YouTube)"},
                {"icon": "🎯", "name": "SQLZoo for practice"},
            ],
            "project": {"name": "SQL Analysis", "desc": "Find a public dataset (Kaggle, data.gov) and answer 5 business questions using only SQL.", "tag": "Beginner"}
        },
        {
            "title": "Python & Visualization",
            "duration": "Month 3–5",
            "description": "Python with pandas makes you 10x faster than Excel. Add visualization and you can tell real data stories.",
            "learn": ["pandas & numpy", "matplotlib & seaborn", "Tableau or Power BI", "Jupyter notebooks", "Data storytelling"],
            "resources": [
                {"icon": "📺", "name": "Kaggle Python & Pandas courses"},
                {"icon": "📘", "name": "Storytelling with Data (book)"},
                {"icon": "🎯", "name": "Tableau Public for free dashboards"},
            ],
            "project": {"name": "Interactive Dashboard", "desc": "Build a Tableau or Power BI dashboard on a real dataset. Make it interactive and publicly shareable.", "tag": "Intermediate"}
        },
        {
            "title": "Business & Advanced Analytics",
            "duration": "Month 6–9",
            "description": "Go beyond charts — learn A/B testing, funnel analysis, cohort analysis, and how to drive decisions.",
            "learn": ["A/B testing & statistical significance", "Cohort & funnel analysis", "Google Analytics / Mixpanel", "dbt for data transformation", "Basic ML for analysts (regression, clustering)"],
            "resources": [
                {"icon": "📺", "name": "Towards Data Science blog"},
                {"icon": "📘", "name": "Lean Analytics (book)"},
                {"icon": "🎯", "name": "dbt Learn (free)"},
            ],
            "project": {"name": "Growth Analysis", "desc": "Analyze a product's growth metrics — retention, churn, LTV. Write a recommendation memo.", "tag": "Advanced"}
        },
        {
            "title": "Job Prep",
            "duration": "Month 10–12",
            "description": "Build your portfolio of dashboards, practice SQL/stats interviews, and get your first case study ready.",
            "learn": ["SQL interview questions (window functions)", "Case study practice", "Portfolio: 3 projects on Tableau Public", "Excel advanced (pivot tables, VBA basics)"],
            "resources": [
                {"icon": "📺", "name": "Data Interview Pro (YouTube)"},
                {"icon": "📘", "name": "Ace the Data Science Interview"},
                {"icon": "🎯", "name": "StrataScratch for interview SQL"},
            ],
            "project": {"name": "Portfolio Dashboard", "desc": "Publish 3 dashboards on Tableau Public covering different industries. Link them from your LinkedIn.", "tag": "Portfolio"}
        },
    ],
    "Game Developer": [
        {
            "title": "Foundation",
            "duration": "Month 1–3",
            "description": "Learn C# or C++ and understand the math behind game development.",
            "learn": ["C# or C++ fundamentals", "Linear algebra & 3D math basics", "Object-Oriented Programming", "Design patterns for games"],
            "resources": [
                {"icon": "📺", "name": "Brackeys (YouTube)"},
                {"icon": "📘", "name": "Game Programming Patterns (book)"},
                {"icon": "🎯", "name": "Learn C# (Codecademy)"},
            ],
            "project": {"name": "Console Game", "desc": "Build a text-based RPG or Tic-Tac-Toe in terminal using pure C++ or C#.", "tag": "Beginner"}
        },
        {
            "title": "Game Engines",
            "duration": "Month 4–7",
            "description": "Pick an engine (Unity for C#, Unreal for C++) and learn to build 2D/3D worlds.",
            "learn": ["Unity or Unreal Engine UI", "Physics & Collisions", "Animation & Audio", "Lighting & Materials", "UI/Canvas design"],
            "resources": [
                {"icon": "📺", "name": "Unity Learn / Unreal Online Learning"},
                {"icon": "📘", "name": "GameDev.tv courses"},
                {"icon": "🎯", "name": "Kenney.nl for free assets"},
            ],
            "project": {"name": "2D Platformer", "desc": "Build a 2D Mario-style platformer with 3 levels, enemies, and a score system.", "tag": "Intermediate"}
        },
        {
            "title": "Advanced Mechanics",
            "duration": "Month 8–10",
            "description": "Dive into AI, multiplayer networking, and performance optimization.",
            "learn": ["Pathfinding (A* algorithm)", "State machines for enemy AI", "Multiplayer basics (Photon/Mirror)", "Memory management & pooling", "Shaders & VFX basics"],
            "resources": [
                {"icon": "📺", "name": "Sebastian Lague (YouTube)"},
                {"icon": "📘", "name": "Multiplayer Game Dev documentation"},
                {"icon": "🎯", "name": "Shader Graph tutorials"},
            ],
            "project": {"name": "3D FPS/RPG Slice", "desc": "Build a vertical slice of a 3D game featuring AI enemies, inventory, and combat.", "tag": "Advanced"}
        },
        {
            "title": "Publishing & Portfolio",
            "duration": "Month 11–12",
            "description": "Join game jams, polish your code, and publish your game.",
            "learn": ["Game Jam participation", "Steam/Itch.io publishing", "Version control (Git LFS)", "Game dev interview prep"],
            "resources": [
                {"icon": "📺", "name": "Game Maker's Toolkit (GMTK)"},
                {"icon": "📘", "name": "Itch.io creator guides"},
                {"icon": "🎯", "name": "LeetCode for logic prep"},
            ],
            "project": {"name": "Published Indie Game", "desc": "Complete a polished game and publish it on Itch.io. Get feedback from real players.", "tag": "Portfolio"}
        },
    ],
    "QA / Test Automation Engineer": [
        {
            "title": "Foundation",
            "duration": "Month 1–2",
            "description": "Understand the software testing lifecycle, bug reporting, and manual testing basics.",
            "learn": ["Software Testing Life Cycle (STLC)", "Test case writing & execution", "Jira & Bug reporting", "Agile methodologies", "Postman for manual API testing"],
            "resources": [
                {"icon": "📺", "name": "Guru99 Testing tutorials"},
                {"icon": "📘", "name": "ISTQB Foundation syllabus"},
                {"icon": "🎯", "name": "Test a public website and log bugs"},
            ],
            "project": {"name": "Test Plan", "desc": "Write a comprehensive test plan and 50 test cases for a popular app like Spotify.", "tag": "Beginner"}
        },
        {
            "title": "Programming & Web Testing",
            "duration": "Month 3–6",
            "description": "Learn to code (Python or Java) and automate web interactions.",
            "learn": ["Java or Python fundamentals", "Selenium WebDriver", "Locators (XPath, CSS)", "TestNG or PyTest", "Page Object Model (POM)"],
            "resources": [
                {"icon": "📺", "name": "Naveen AutomationLabs"},
                {"icon": "📘", "name": "Selenium official documentation"},
                {"icon": "🎯", "name": "Practice on automationpractice.com"},
            ],
            "project": {"name": "UI Automation Framework", "desc": "Build an automation framework using Selenium + POM to test an e-commerce site.", "tag": "Intermediate"}
        },
        {
            "title": "API & Advanced Testing",
            "duration": "Month 7–9",
            "description": "Move beyond UI. Learn to automate backend APIs and mobile applications.",
            "learn": ["API Automation (RestAssured / Python Requests)", "Appium for mobile testing", "Performance testing (JMeter)", "SQL for database validation"],
            "resources": [
                {"icon": "📺", "name": "Rahul Shetty API courses"},
                {"icon": "📘", "name": "JMeter documentation"},
                {"icon": "🎯", "name": "Postman API challenges"},
            ],
            "project": {"name": "API Test Suite", "desc": "Create a fully automated API testing suite validating status codes, JSON responses, and DB records.", "tag": "Advanced"}
        },
        {
            "title": "CI/CD & Job Prep",
            "duration": "Month 10–12",
            "description": "Integrate tests into the pipeline so they run automatically, and prep for SDET interviews.",
            "learn": ["Jenkins / GitHub Actions integration", "Docker for testing", "Allure Reporting", "Coding interview prep (DSA basics)"],
            "resources": [
                {"icon": "📺", "name": "TechWorld with Nana"},
                {"icon": "📘", "name": "GitHub Actions for QA"},
                {"icon": "🎯", "name": "LeetCode (Easy problems)"},
            ],
            "project": {"name": "Continuous Testing Pipeline", "desc": "Set up a GitHub Action that runs your Selenium tests automatically on every code push and generates a report.", "tag": "Portfolio"}
        },
    ],
    "Blockchain / Web3 Developer": [
        {
            "title": "Foundation",
            "duration": "Month 1–3",
            "description": "Understand cryptography, distributed ledgers, and how blockchains actually work under the hood.",
            "learn": ["Cryptography basics (Hashes, Public Key)", "Blockchain architecture (Blocks, Consensus)", "Ethereum Virtual Machine (EVM)", "Wallets & MetaMask setup"],
            "resources": [
                {"icon": "📺", "name": "MIT Blockchain course (YouTube)"},
                {"icon": "📘", "name": "Mastering Bitcoin (book)"},
                {"icon": "🎯", "name": "Read the Bitcoin Whitepaper"},
            ],
            "project": {"name": "Simple Blockchain", "desc": "Build a basic blockchain data structure in Python or JavaScript using SHA-256 hashing.", "tag": "Beginner"}
        },
        {
            "title": "Smart Contracts",
            "duration": "Month 4–7",
            "description": "Learn Solidity and build the decentralized logic that powers Web3 apps.",
            "learn": ["Solidity programming", "Remix IDE & Hardhat/Foundry", "ERC-20 & ERC-721 token standards", "Smart contract testing", "IPFS for decentralized storage"],
            "resources": [
                {"icon": "📺", "name": "Patrick Collins Web3 courses"},
                {"icon": "📘", "name": "CryptoZombies (interactive)"},
                {"icon": "🎯", "name": "Solidity documentation"},
            ],
            "project": {"name": "Custom Token & NFT", "desc": "Write, test, and deploy your own ERC-20 token and ERC-721 NFT collection to a testnet.", "tag": "Intermediate"}
        },
        {
            "title": "DApp Development",
            "duration": "Month 8–10",
            "description": "Connect your smart contracts to a frontend website using modern libraries.",
            "learn": ["React.js & Next.js", "Web3.js or Ethers.js / viem", "Wallet connection (RainbowKit)", "The Graph for indexing", "Smart contract security (Reentrancy)"],
            "resources": [
                {"icon": "📺", "name": "Buildspace projects"},
                {"icon": "📘", "name": "Ethers.js documentation"},
                {"icon": "🎯", "name": "Smart Contract Weakness Registry (SWC)"},
            ],
            "project": {"name": "Full DApp", "desc": "Build a decentralized crowdfunding platform (like Kickstarter) where users fund projects with crypto.", "tag": "Advanced"}
        },
        {
            "title": "Advanced Web3 & Job Prep",
            "duration": "Month 11–12",
            "description": "Learn L2 scaling, audit contracts, and build your Web3 portfolio.",
            "learn": ["Layer 2 scaling (Polygon, Arbitrum)", "DeFi protocols (Uniswap architecture)", "Smart contract auditing tools", "Web3 hackathons"],
            "resources": [
                {"icon": "📺", "name": "EatTheBlocks (YouTube)"},
                {"icon": "📘", "name": "OpenZeppelin documentation"},
                {"icon": "🎯", "name": "Join ETHGlobal hackathons"},
            ],
            "project": {"name": "DeFi Exchange Clone", "desc": "Build a simplified decentralized exchange (DEX) with liquidity pools and swapping functionality.", "tag": "Portfolio"}
        },
    ],
    "Embedded Systems Engineer": [
        {
            "title": "Foundation",
            "duration": "Month 1–3",
            "description": "Master the hardware-software boundary. You need strong C programming and electronics basics.",
            "learn": ["C programming (Pointers, memory deeply)", "Basic electronics (Ohm's law, circuits)", "Digital logic design", "Reading datasheets", "Git for version control"],
            "resources": [
                {"icon": "📺", "name": "Ben Eater (YouTube)"},
                {"icon": "📘", "name": "The C Programming Language (K&R)"},
                {"icon": "🎯", "name": "TinkerCAD circuits simulator"},
            ],
            "project": {"name": "Logic Gate Simulator", "desc": "Write a C program that simulates AND, OR, XOR logic gates and basic flip-flops.", "tag": "Beginner"}
        },
        {
            "title": "Microcontrollers",
            "duration": "Month 4–7",
            "description": "Start writing code that runs on actual silicon without an operating system.",
            "learn": ["Arduino & AVR microcontrollers", "GPIO, Interrupts, Timers", "Communication protocols (I2C, SPI, UART)", "Debugging via JTAG/SWD", "Oscilloscope basics"],
            "resources": [
                {"icon": "📺", "name": "Fastbit Embedded Brain Academy"},
                {"icon": "📘", "name": "Making Embedded Systems (book)"},
                {"icon": "🎯", "name": "Buy an STM32 Nucleo board"},
            ],
            "project": {"name": "Weather Station", "desc": "Interface a microcontroller with temperature/humidity sensors via I2C and display data on an LCD using UART.", "tag": "Intermediate"}
        },
        {
            "title": "RTOS & IoT",
            "duration": "Month 8–10",
            "description": "Learn how to handle multiple tasks concurrently using Real-Time Operating Systems.",
            "learn": ["FreeRTOS fundamentals", "Task scheduling, Mutexes, Semaphores", "IoT protocols (MQTT, CoAP)", "Wireless comms (Bluetooth/Wi-Fi modules)", "Power optimization"],
            "resources": [
                {"icon": "📺", "name": "Digi-Key RTOS series"},
                {"icon": "📘", "name": "FreeRTOS Reference Manual"},
                {"icon": "🎯", "name": "ESP32 programming"},
            ],
            "project": {"name": "IoT Home Monitor", "desc": "Build a multi-tasking ESP32 device using FreeRTOS that reads sensor data and publishes it to a cloud MQTT broker.", "tag": "Advanced"}
        },
        {
            "title": "Embedded Linux & Job Prep",
            "duration": "Month 11–12",
            "description": "Scale up to processors that run Linux, and prep for embedded interviews.",
            "learn": ["Embedded Linux basics", "Yocto or Buildroot", "Writing simple device drivers", "Embedded C interview questions (Bit manipulation)"],
            "resources": [
                {"icon": "📺", "name": "Bootlin training materials"},
                {"icon": "📘", "name": "Linux Device Drivers (book)"},
                {"icon": "🎯", "name": "LeetCode (Bitwise tag)"},
            ],
            "project": {"name": "Custom Linux Image", "desc": "Use Yocto to build a minimal custom Linux image for a Raspberry Pi and run a custom startup script.", "tag": "Portfolio"}
        },
    ],
    "Data Engineer / Architect": [
        {
            "title": "Foundation",
            "duration": "Month 1–2",
            "description": "Get incredible at SQL and Python. Data Engineering is all about moving and transforming data.",
            "learn": ["Advanced SQL (Window functions, CTEs)", "Python for scripting", "Linux command line", "Database normalization vs denormalization"],
            "resources": [
                {"icon": "📺", "name": "Seattle Data Guy (YouTube)"},
                {"icon": "📘", "name": "Designing Data-Intensive Apps"},
                {"icon": "🎯", "name": "LeetCode SQL problems"},
            ],
            "project": {"name": "Web Scraper to DB", "desc": "Write a Python script that scrapes a website daily, cleans the data, and inserts it into a PostgreSQL database.", "tag": "Beginner"}
        },
        {
            "title": "Data Warehousing",
            "duration": "Month 3–5",
            "description": "Learn how to store massive amounts of analytical data and build ETL pipelines.",
            "learn": ["Cloud Data Warehouses (Snowflake or BigQuery)", "ETL / ELT concepts", "Dimensional modeling (Star schema)", "dbt (Data Build Tool)", "Airflow for orchestration"],
            "resources": [
                {"icon": "📺", "name": "Data Engineering Zoomcamp"},
                {"icon": "📘", "name": "The Data Warehouse Toolkit"},
                {"icon": "🎯", "name": "dbt learn courses"},
            ],
            "project": {"name": "Automated ELT Pipeline", "desc": "Extract data from a public API, load it into Snowflake, transform it with dbt, and schedule it with Airflow.", "tag": "Intermediate"}
        },
        {
            "title": "Big Data & Streaming",
            "duration": "Month 6–9",
            "description": "Move beyond databases into distributed processing and real-time streaming.",
            "learn": ["Apache Spark / PySpark", "Data Lakes (AWS S3, Databricks)", "Streaming (Apache Kafka)", "NoSQL databases (Cassandra/MongoDB)", "Parquet / Avro file formats"],
            "resources": [
                {"icon": "📺", "name": "Zach Wilson (Data Engineer)"},
                {"icon": "📘", "name": "Spark: The Definitive Guide"},
                {"icon": "🎯", "name": "Confluent Kafka tutorials"},
            ],
            "project": {"name": "Real-time Streaming Pipeline", "desc": "Stream fake user click-data into Kafka, process it with PySpark, and output real-time analytics to a dashboard.", "tag": "Advanced"}
        },
        {
            "title": "Cloud Ops & Job Prep",
            "duration": "Month 10–12",
            "description": "Learn to deploy pipelines using IaC and prep for system design interviews.",
            "learn": ["AWS/GCP data services", "Terraform for infrastructure", "Docker & Kubernetes basics", "Data engineering system design"],
            "resources": [
                {"icon": "📺", "name": "ByteByteGo System Design"},
                {"icon": "📘", "name": "Data Engineering Interview questions"},
                {"icon": "🎯", "name": "Cloud certifications (AWS/GCP)"},
            ],
            "project": {"name": "End-to-End Cloud Platform", "desc": "Deploy your entire data pipeline using Terraform on AWS, fully containerized with CI/CD.", "tag": "Portfolio"}
        },
    ]
}

CAREER_MILESTONES = {
    "Frontend / UI Engineer": [
        {"title": "First Deploy", "desc": "Ship a live website"},
        {"title": "React App", "desc": "Build a real React project"},
        {"title": "TypeScript", "desc": "Type your first codebase"},
        {"title": "Accessibility", "desc": "Pass an a11y audit"},
        {"title": "First Job", "desc": "Land your first frontend role"},
    ],
    "Backend / Systems Engineer": [
        {"title": "REST API", "desc": "Ship a working API"},
        {"title": "Database", "desc": "Design & query a real DB"},
        {"title": "Auth System", "desc": "JWT auth end-to-end"},
        {"title": "System Design", "desc": "Design a scalable system"},
        {"title": "First Job", "desc": "Land your first backend role"},
    ],
    "Full Stack Developer": [
        {"title": "Frontend Basic", "desc": "Ship a static UI"},
        {"title": "Backend API", "desc": "Build an Express/Node server"},
        {"title": "Full CRUD", "desc": "Connect frontend to DB"},
        {"title": "Cloud Deploy", "desc": "Host app on AWS/Render"},
        {"title": "First Job", "desc": "Land a fullstack role"},
    ],
    "Data Scientist / ML Engineer": [
        {"title": "First EDA", "desc": "Publish a Kaggle notebook"},
        {"title": "First Model", "desc": "Train & evaluate an ML model"},
        {"title": "Top 30%", "desc": "Kaggle competition rank"},
        {"title": "Deployed Model", "desc": "Serve predictions via API"},
        {"title": "First Job", "desc": "Land your first DS role"},
    ],
    "DevOps / Cloud Engineer": [
        {"title": "Dockerized App", "desc": "Container your first app"},
        {"title": "CI/CD Pipeline", "desc": "Auto-deploy on push"},
        {"title": "Kubernetes", "desc": "Deploy to a K8s cluster"},
        {"title": "AWS Certified", "desc": "Pass Solutions Architect"},
        {"title": "First Job", "desc": "Land your first DevOps role"},
    ],
    "Cybersecurity / DevSecOps Engineer": [
        {"title": "Linux Mastery", "desc": "Comfortable with CLI"},
        {"title": "First Exploit", "desc": "Complete HTB machine"},
        {"title": "Security Script", "desc": "Automate an audit task"},
        {"title": "Certification", "desc": "Pass Sec+ or CEH"},
        {"title": "First Job", "desc": "Land a security role"},
    ],
    "AI / ML Research Engineer": [
        {"title": "Math Foundation", "desc": "Linear Algebra & Stats"},
        {"title": "PyTorch Basic", "desc": "Build a CNN"},
        {"title": "Implement Paper", "desc": "Code an architecture from scratch"},
        {"title": "Fine-Tuning", "desc": "Fine-tune an LLM"},
        {"title": "First Job", "desc": "Land a research role"},
    ],
    "Product Manager / Tech Lead": [
        {"title": "User Research", "desc": "Conduct 5 interviews"},
        {"title": "First PRD", "desc": "Write product requirements"},
        {"title": "Data Analysis", "desc": "SQL/Analytics project"},
        {"title": "Agile Lead", "desc": "Run a sprint"},
        {"title": "First Job", "desc": "Land a PM role"},
    ],
    "Mobile App Developer": [
        {"title": "First App", "desc": "Build a local to-do app"},
        {"title": "API Integration", "desc": "Fetch external data"},
        {"title": "State Management", "desc": "Implement Redux/Provider"},
        {"title": "Store Publish", "desc": "Live on App/Play Store"},
        {"title": "First Job", "desc": "Land a mobile role"},
    ],
    "Data Analyst / Business Intelligence": [
        {"title": "SQL Mastery", "desc": "Complex joins & windows"},
        {"title": "First Dashboard", "desc": "Publish on Tableau Public"},
        {"title": "Python Script", "desc": "Automate data cleaning"},
        {"title": "Business Case", "desc": "Present findings"},
        {"title": "First Job", "desc": "Land a data analyst role"},
    ],
    "Game Developer": [
        {"title": "First Prototype", "desc": "Build a moving character"},
        {"title": "Physics Engine", "desc": "Implement collision/gravity"},
        {"title": "Enemy AI", "desc": "Create smart opponents"},
        {"title": "Publish Game", "desc": "Release on Itch.io"},
        {"title": "First Job", "desc": "Land a game dev role"},
    ],
    "QA / Test Automation Engineer": [
        {"title": "Manual Suite", "desc": "Write complete test cases"},
        {"title": "First Script", "desc": "Automate a UI login"},
        {"title": "API Testing", "desc": "Automate Postman suite"},
        {"title": "CI Integration", "desc": "Run tests on Jenkins"},
        {"title": "First Job", "desc": "Land an SDET role"},
    ],
    "Blockchain / Web3 Developer": [
        {"title": "Crypto Basics", "desc": "Understand hashing"},
        {"title": "Smart Contract", "desc": "Deploy an ERC-20"},
        {"title": "DApp Connect", "desc": "Connect wallet to frontend"},
        {"title": "Security Audit", "desc": "Find Reentrancy bug"},
        {"title": "First Job", "desc": "Land a Web3 role"},
    ],
    "Embedded Systems Engineer": [
        {"title": "Blink LED", "desc": "Hardware \"Hello World\""},
        {"title": "Sensor Comm", "desc": "Read I2C/SPI data"},
        {"title": "RTOS Task", "desc": "Run a FreeRTOS system"},
        {"title": "Custom PCB", "desc": "Design simple board"},
        {"title": "First Job", "desc": "Land an embedded role"},
    ],
    "Data Engineer / Architect": [
        {"title": "SQL Pipeline", "desc": "Automate a DB query"},
        {"title": "Data Warehouse", "desc": "Setup Snowflake/BigQuery"},
        {"title": "Spark Job", "desc": "Process Big Data"},
        {"title": "Airflow DAG", "desc": "Orchestrate pipeline"},
        {"title": "First Job", "desc": "Land a Data Engineer role"},
    ],
    "default": [
        {"title": "Foundation", "desc": "Complete Phase 1"},
        {"title": "First Project", "desc": "Ship something real"},
        {"title": "Intermediate", "desc": "Complete Phase 3"},
        {"title": "Portfolio", "desc": "3+ projects live"},
        {"title": "First Job", "desc": "Land your first role"},
    ]
}