# Shai Hulud Detector

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg)

A CLI tool to scan GitHub users and organizations for shai-hulud compromise detection.

## Description

Shai Hulud Detector is a security scanning tool that checks GitHub users and organization members for signs of compromise by scanning repository descriptions for the string "Sha1-Hulud: The Second Coming.". Shai Hulud is a self-replicating npm worm that spreads through compromised developer environments. It has been responsible for significant supply-chain attacks targeting major npm packages. 


## Features

- Scan individual GitHub users
- Scan all members of a GitHub organization
- Concurrent scanning with configurable workers
- Color-coded output for easy identification
- Support for GitHub Personal Access Tokens

## Requirements

- Python 3.11+
- uv package manager (https://docs.astral.sh/uv/)

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

### Help
```bash
uv run python main.py scan --help 
``` 

### Parallelism

Set concurrency (default 5):
```bash
uv run python main.py scan --workers 10 username1 username2
```

### Verbose Output

Use the `--verbose` flag to see detailed scanning information including repository counts and progress:
```bash
uv run python main.py scan username1 --verbose
```


### Recommended Actions

If you detect a compromise:
- Rotate **all** GitHub, npm, cloud, and CI/CD secrets
- Check GitHub for repositories with the description "Sha1-Hulud: The Second Coming."
- Disable npm `postinstall` scripts in CI where possible
- Pin package versions and enforce MFA on GitHub and npm accounts
- Audit all npm dependencies and versions

### References

For more detailed information about Shai Hulud attacks, see:
- [HelixGuard: Malicious Sha1Hulud Analysis](https://helixguard.ai/blog/malicious-sha1hulud-2025-11-24)
- [Aikido Security: Shai Hulud Strikes Again](https://www.aikido.dev/blog/shai-hulud-strikes-again-hitting-zapier-ensdomains)
- [Wiz: Shai Hulud 2.0 Ongoing Supply Chain Attack](https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack)

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