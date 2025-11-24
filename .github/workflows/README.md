# GitHub Actions Workflows

This directory contains GitHub Actions workflows for CI/CD.

## CI/CD Pipeline (ci-cd.yml)

The main workflow includes:

### Jobs

1. **Test and Lint**
   - Runs on: `ubuntu-latest`
   - Steps:
     - Sets up Python 3.10
     - Installs dependencies
     - Runs flake8 linting
     - Checks code formatting with black
     - Runs pytest with coverage
     - Uploads coverage to Codecov

2. **Build Docker Image**
   - Runs on: `ubuntu-latest`
   - Depends on: Test job
   - Steps:
     - Sets up Docker Buildx
     - Logs in to GitHub Container Registry
     - Builds and pushes Docker image
     - Uses GitHub Actions cache for faster builds

3. **Test Docker Image**
   - Runs on: `ubuntu-latest`
   - Depends on: Build job
   - Only runs on push (not PRs)
   - Steps:
     - Builds Docker image
     - Tests that container starts
     - Tests health endpoint

4. **Security Scan**
   - Runs on: `ubuntu-latest`
   - Depends on: Build job
   - Only runs on push (not PRs)
   - Steps:
     - Scans Docker image with Trivy
     - Uploads results to GitHub Security

### Triggers

- Push to `main`, `master`, or `develop` branches
- Pull requests to these branches

### Container Registry

Images are pushed to GitHub Container Registry:
- Format: `ghcr.io/<username>/<repository>:<tag>`
- Tags include: branch name, commit SHA, semantic version, and `latest` for default branch

### Permissions

The workflow requires:
- `contents: read` - to checkout code
- `packages: write` - to push Docker images
- `security-events: write` - to upload security scan results

### Secrets

No additional secrets required! The workflow uses `GITHUB_TOKEN` which is automatically provided by GitHub Actions.

