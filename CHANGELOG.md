# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.4] - 2025-12-14

### Changed
- Improved PyPI keywords with more security, threat detection, and supply chain security domains
- Add OG image to README.md
- Add PyPI downloads badge to README.md

## [1.0.3] - 2025-11-26

### Fixed
- Minor bugfix in git push command in RELEASE.md documentation

### Changed
- Updated links in README.md
- Add delete tag commands in RELEASE.md documentation

## [1.0.2] - 2025-11-26

### Added
- Added GitHub Actions workflow for publishing
- Added CHANGELOG.md file
- Added RELEASE.md file
- Added DEVELOPMENT.md file

## [1.0.0] - 2025-11-26

### Added
- Initial release of Shai Hulud Detector
- CLI tool to scan GitHub users and organizations for Shai Hulud compromises
- Dual detection methods:
  - Repository description pattern matching for "Sha1-Hulud: The Second Coming."
  - Suspicious file detection (e.g., `secrets.json`, `credentials.json`)
- Support for scanning individual users or all members of an organization
- Concurrent scanning with configurable worker threads
- Color-coded output (FLAG/OKAY/ERROR status)
- Verbose mode for detailed output
- GitHub Personal Access Token authentication via environment variable or command-line flag

[1.0.4]: https://github.com/ysskrishna/shai-hulud-detector/compare/v1.0.3...v1.0.4
[1.0.3]: https://github.com/ysskrishna/shai-hulud-detector/compare/v1.0.2...v1.0.3
[1.0.2]: https://github.com/ysskrishna/shai-hulud-detector/compare/v1.0.0...v1.0.2
[1.0.0]: https://github.com/ysskrishna/shai-hulud-detector/releases/tag/v1.0.0

