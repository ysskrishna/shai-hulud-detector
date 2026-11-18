# Release Guide

This project uses **Git tags**, **uv**, **Trusted Publishing**, and **GitHub Actions** to publish releases to PyPI.

## 🔄 Release Pipeline Overview

1. **Create a Git tag**
   Each release is triggered by pushing a new version tag.

   ```bash
   git tag -a vX.Y.Z -m "vX.Y.Z"
   git push origin vX.Y.Z
   ```

2. **GitHub Actions Workflow Runs**
   When a new tag is pushed:

   * The release workflow is triggered.
   * `uv build` creates the source distribution and wheel.
   * GitHub performs a **trusted publishing** handshake with PyPI.
   * If successful, the artifacts are uploaded to PyPI.

3. **Publish to PyPI (via uv + trusted publishing)**
   No PyPI API tokens are required.
   PyPI trusts GitHub Actions based on your project’s configuration.

4. **Versioning**

   * Versions follow **semantic versioning** (e.g., `v1.2.3`).
   * The version in `pyproject.toml` must match the tag:

     ```
     [project]
     version = "1.2.3"
     ```

## 🚀 How to Cut a New Release

1. Update version in `pyproject.toml`.
2. Commit the change:

   ```bash
   git commit -am "chore: bump version to vX.Y.Z"
   ```
3. Create and push a tag:

   ```bash
   git tag -a vX.Y.Z -m "vX.Y.Z"
   git push origin vX.Y.Z
   ```
4. Wait for GitHub Actions to publish the release to PyPI.

## 🗑️ Deleting Tags

If you need to delete a tag (e.g., if you created it incorrectly):

### Delete Tag Locally

```bash
git tag -d vX.Y.Z
```

### Delete Tag Remotely

```bash
git push origin --delete vX.Y.Z
```

**Note:** If the tag has already triggered a GitHub Actions workflow, you may need to handle the PyPI release separately if it was already published.

## 📝 Notes

* Only pushes of tags matching `v*.*.*` trigger publishing. The GitHub Release uses `ysskrishna/changelog-release-action@v1` with the matching nonempty `CHANGELOG.md` section and title `Release <tag>`. Missing or empty notes fail; there is no fallback.
* Ensure your repository is registered for **trusted publishing** on PyPI.
* You can verify release status under **GitHub → Actions → Publish**.

## References

- https://docs.astral.sh/uv/guides/integration/github/#publishing-to-pypi
- https://github.com/astral-sh/trusted-publishing-examples