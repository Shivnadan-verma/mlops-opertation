# Setting Up GitHub Actions CI/CD

This guide will help you set up GitHub Actions for your MLflow learning project.

## Prerequisites

1. A GitHub repository (create one if you haven't already)
2. Your code pushed to GitHub

## Step-by-Step Setup

### 1. Push Your Code to GitHub

If you haven't already, initialize git and push your code:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit with CI/CD setup"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push to GitHub
git push -u origin main
```

### 2. Verify Workflow Files

The CI/CD workflow is already configured in `.github/workflows/ci-cd.yml`. 

**Key features:**
- ✅ Automatic testing on every push/PR
- ✅ Docker image building
- ✅ Code linting and formatting checks
- ✅ Security scanning
- ✅ Coverage reporting

### 3. Enable GitHub Actions

1. Go to your GitHub repository
2. Click on the **Actions** tab
3. You should see the workflow listed
4. GitHub Actions are enabled by default - no additional setup needed!

### 4. View Workflow Runs

After pushing code or creating a PR:

1. Go to the **Actions** tab in your repository
2. Click on a workflow run to see details
3. View logs for each job and step

### 5. Access Docker Images

Docker images are automatically pushed to GitHub Container Registry:

1. Go to your repository
2. Click on **Packages** (on the right side)
3. You'll see your Docker images there

**Pull the image:**
```bash
# Login to GitHub Container Registry
echo $GITHUB_TOKEN | docker login ghcr.io -u YOUR_USERNAME --password-stdin

# Pull the image
docker pull ghcr.io/YOUR_USERNAME/YOUR_REPO:latest
```

### 6. Customize the Workflow (Optional)

You can customize the workflow by editing `.github/workflows/ci-cd.yml`:

#### Change Python Version
```yaml
python-version: '3.11'  # Change from '3.10'
```

#### Add More Test Commands
```yaml
- name: Run custom tests
  run: |
    python -m pytest tests/ -v
```

#### Change Docker Registry
Edit the `REGISTRY` and `IMAGE_NAME` environment variables at the top of the workflow file.

#### Disable Security Scanning
Remove or comment out the `security-scan` job if you don't need it.

### 7. Branch Protection (Recommended)

Set up branch protection rules:

1. Go to **Settings** → **Branches**
2. Add a rule for `main` branch
3. Enable:
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging
   - Select the "Test and Lint" check

This ensures code quality before merging.

### 8. Secrets (If Needed)

If you need to push to external registries (Docker Hub, etc.):

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Add secrets like:
   - `DOCKER_USERNAME`
   - `DOCKER_PASSWORD`

Then update the workflow to use these secrets.

## Workflow Triggers

The workflow runs automatically on:

- ✅ Push to `main`, `master`, or `develop` branches
- ✅ Pull requests to these branches
- ✅ Manual trigger (workflow_dispatch) - can be added

## Troubleshooting

### Workflow Not Running?

1. Check that `.github/workflows/ci-cd.yml` exists
2. Verify the file has correct YAML syntax
3. Check the **Actions** tab for error messages

### Docker Build Fails?

1. Check Dockerfile syntax
2. Verify all dependencies in `requirements.txt`
3. Check the build logs in GitHub Actions

### Tests Failing?

1. Run tests locally first: `pytest tests/ -v`
2. Check test files are in the `tests/` directory
3. Verify all dependencies are installed

### Permission Errors?

1. Go to **Settings** → **Actions** → **General**
2. Under "Workflow permissions", select:
   - ✅ Read and write permissions
   - ✅ Allow GitHub Actions to create and approve pull requests

## Next Steps

1. ✅ Push your code to trigger the first workflow run
2. ✅ Check the Actions tab to see it in action
3. ✅ Create a PR to test the full pipeline
4. ✅ Pull your Docker image from GitHub Container Registry

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
- [Docker Buildx](https://docs.docker.com/build/buildx/)

## Support

If you encounter issues:
1. Check the workflow logs in the Actions tab
2. Verify all files are committed and pushed
3. Ensure your GitHub repository has Actions enabled

