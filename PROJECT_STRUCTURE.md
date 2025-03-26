# Tento Project Structure

This document provides an overview of the Tento project structure and explains the organization of the codebase.

## Overview

Tento is organized as a monorepo containing multiple components:

- `backend/`: Django API server
- `frontend/`: React web application
- `mobile/`: Flutter mobile application
- `infrastructure/`: Kubernetes and deployment configurations

## Backend Structure

The backend is a Django application organized as follows:

```
backend/
├── apps/                  # Django applications
│   ├── core/              # Core functionality shared across apps
│   ├── users/             # User management
│   ├── properties/        # Property listings and management
│   ├── leases/            # Lease agreements and management
│   ├── payments/          # Rent payments and financial transactions
│   ├── maintenance/       # Maintenance requests and tracking
│   └── communications/    # Messaging and notifications
├── config/                # Configuration files
├── tento/                 # Main Django project
│   ├── settings.py        # Django settings
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── tests/                 # Test files
├── scripts/               # Utility scripts
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

Each app in the `apps/` directory follows a similar structure:

```
app_name/
├── models/                # Database models
├── views/                 # API views
├── serializers/           # DRF serializers
└── tests/                 # Tests for this app
```

## Frontend Structure

The frontend is a React application with TypeScript and Vite, organized as follows:

```
frontend/
├── public/                # Static files
│   └── index.html         # HTML entry point
├── src/                   # Source code
│   ├── components/        # React components
│   │   ├── common/        # Shared components
│   │   ├── property/      # Property-related components
│   │   ├── user/          # User-related components
│   │   ├── lease/         # Lease-related components
│   │   ├── payment/       # Payment-related components
│   │   ├── maintenance/   # Maintenance-related components
│   │   └── communication/ # Communication-related components
│   ├── pages/             # Page components
│   │   ├── home/          # Home page
│   │   ├── auth/          # Authentication pages
│   │   ├── dashboard/     # Dashboard pages
│   │   ├── property/      # Property pages
│   │   ├── lease/         # Lease pages
│   │   ├── payment/       # Payment pages
│   │   ├── maintenance/   # Maintenance pages
│   │   ├── profile/       # Profile pages
│   │   └── admin/         # Admin pages
│   ├── services/          # API services
│   ├── assets/            # Images, fonts, etc.
│   ├── utils/             # Utility functions
│   ├── hooks/             # Custom React hooks
│   ├── context/           # React context providers
│   ├── App.tsx            # Main App component
│   ├── App.css            # App component styles
│   ├── main.tsx           # Entry point
│   ├── index.css          # Global styles
│   └── routes.tsx         # Route definitions
├── package.json           # NPM dependencies
├── tsconfig.json          # TypeScript configuration
├── tsconfig.node.json     # Node.js TypeScript configuration
├── vite.config.ts         # Vite configuration
└── .env                   # Environment variables
```

## Mobile Structure

The mobile app is a Flutter application organized as follows:

```
mobile/
├── android/               # Android-specific files
├── ios/                   # iOS-specific files
├── lib/                   # Dart source code
│   ├── screens/           # App screens
│   │   ├── auth/          # Authentication screens
│   │   ├── home/          # Home screen
│   │   ├── property/      # Property screens
│   │   ├── lease/         # Lease screens
│   │   ├── payment/       # Payment screens
│   │   ├── maintenance/   # Maintenance screens
│   │   └── profile/       # Profile screens
│   ├── widgets/           # UI widgets
│   │   ├── common/        # Shared widgets
│   │   ├── property/      # Property-related widgets
│   │   ├── user/          # User-related widgets
│   │   ├── lease/         # Lease-related widgets
│   │   ├── payment/       # Payment-related widgets
│   │   └── maintenance/   # Maintenance-related widgets
│   ├── models/            # Data models
│   ├── services/          # API services
│   ├── utils/             # Utility functions
│   ├── providers/         # State management
│   └── main.dart          # Entry point
└── pubspec.yaml           # Flutter dependencies
```

## Infrastructure Structure

The infrastructure configuration is organized as follows:

```
infrastructure/
├── kubernetes/            # Kubernetes configuration
│   ├── dev/               # Development environment
│   │   ├── backend/       # Backend services
│   │   ├── frontend/      # Frontend services
│   │   └── database/      # Database services
│   ├── staging/           # Staging environment
│   │   ├── backend/       # Backend services
│   │   ├── frontend/      # Frontend services
│   │   └── database/      # Database services
│   └── prod/              # Production environment
│       ├── backend/       # Backend services
│       ├── frontend/      # Frontend services
│       └── database/      # Database services
├── docker/                # Docker configuration
│   ├── Dockerfile.backend # Backend Dockerfile
│   ├── Dockerfile.frontend # Frontend Dockerfile
│   └── docker-compose.yml # Docker Compose for local development
└── terraform/             # Terraform configuration
```

## CI/CD Configuration

CI/CD is configured using GitHub Actions:

```
.github/
└── workflows/
    ├── backend-ci.yml     # Backend CI workflow
    ├── frontend-ci.yml    # Frontend CI workflow
    ├── mobile-ci.yml      # Mobile CI workflow
    └── deploy.yml         # Deployment workflow
```

## Documentation

- `README.md`: Project overview and getting started guide
- `CONTRIBUTING.md`: Guidelines for contributing to the project
- `CODE_OF_CONDUCT.md`: Code of conduct for contributors
- `LICENSE`: Project license
- `PROJECT_STRUCTURE.md`: This file, explaining the project structure
