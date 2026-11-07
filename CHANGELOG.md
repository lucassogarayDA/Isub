# Changelog

## 1.0.2

- Sanitize remote service banners before displaying them, preventing terminal control characters from being passed through.
- Reject empty or whitespace-containing host arguments before DNS resolution.
- Resolve the target hostname once and use the resolved IPv4 address for the run.
- Measure elapsed time with a monotonic clock.
- Add tests for banner sanitization and TCP port boundary values.
- Clarify IPv4-only target support in the CLI help and documentation.

## 1.0.1

- Validate port specifications, thread counts, and timeout values.
- Improve rotating log handler management.
- Add unit tests and GitHub Actions coverage.
