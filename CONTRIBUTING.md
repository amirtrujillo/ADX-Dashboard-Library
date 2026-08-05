# How to Contribute to the Project

Thank you for helping improve the ADX Dashboard Library.

## Found a bug?

- Search existing issues before opening a new one.
- Use a clear title.
- Include the dashboard name and version.
- Describe the exact steps needed to reproduce the problem.
- Remove credentials, customer data, and private hostnames from all evidence.

## Want to contribute a dashboard?

1. Clone the repository and create a new branch.
2. Add the canonical dashboard JSON under `source/adx`.
3. Add or update its entry in `mapping.json`.
4. Run:

```bash
python scripts/build_dist.py
python scripts/validate_adx_dashboard.py source/adx dist
```

5. Import the generated JSON from `dist` into a separate ADX dashboard.
6. Complete a smoke test.
7. Add sanitized screenshots when available.
8. Open a pull request with a clear description of the use case and validation.

Only files in `source/adx` are edited as dashboard source. Files under `dist` and
`queries` are generated.

## Contribution license

By submitting a contribution, you agree that it may be distributed as part of
this project under The Unlicense and dedicated to the public domain to the
greatest extent permitted by law.
