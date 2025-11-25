# Shai Hulud Detector

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg)

A CLI tool to scan GitHub users and organizations for shai-hulud compromise detection.

## Description

Shai Hulud Detector is a security scanning tool that checks GitHub users and organization members for signs of compromise by scanning repository descriptions for specific patterns. The tool can scan individual users or entire organizations concurrently.

## Features

- Scan individual GitHub users
- Scan all members of a GitHub organization
- Concurrent scanning with configurable workers
- Color-coded output for easy identification
- Support for GitHub Personal Access Tokens

## Installation

### Clone the repository

```bash
git clone https://github.com/ysskrishna/shai-hulud-detector.git
cd shai-hulud-detector
```

### Install dependencies

```bash
uv sync
```

## Usage

### Scan one or more users

```bash
uv run python main.py scan username1
uv run python main.py scan username1 username2 username3
```

### Scan all members of an organization

```bash
uv run python main.py scan --org organizationname
```

### Authentication

- **Command-line**: `--token GITHUB_TOKEN_HERE`
- **Environment**:
    ```bash
    export GITHUB_TOKEN=your_token_here
    uv run python main.py scan alice
    ```

**Note:** Without a token, the tool uses anonymous access which has lower rate limits.

**Note:** Without a token, GitHub rate limits are much lower.

### Parallelism

Set concurrency (default 5):
```bash
uv run python main.py scan --workers 10 username1 username2
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Author

**Y. Siva Sai Krishna**

- GitHub: [@ysskrishna](https://github.com/ysskrishna)
- LinkedIn: [ysskrishna](https://linkedin.com/in/ysskrishna)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Issues

If you encounter any issues or have feature requests, please open an issue on [GitHub](https://github.com/ysskrishna/shai-hulud-detector/issues).