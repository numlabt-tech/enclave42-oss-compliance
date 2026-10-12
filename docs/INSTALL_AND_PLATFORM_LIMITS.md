# enclave42 0.1.2 — installation and platform limits

**Validated platform:** Linux x86_64, Ubuntu 24.04 (glibc 2.39), Python 3.12. This is the only platform on which 0.1.2 has been validated end-to-end.

```
python3.12 -m venv .venv && . .venv/bin/activate
pip install "enclave42>=0.1.2"   # once 0.1.2 is available on PyPI (see the repository README for status)
python -c "import enclave42, importlib.metadata as m; print(m.version('enclave42'))"   # 0.1.2
```

## Limits you should know
- The 0.1.2 wheel is `manylinux_2_39_x86_64`: it needs glibc >= 2.39 (Ubuntu 24.04 or newer). There is no wheel for macOS, Windows, ARM, or older glibc, and no source distribution.
- On such systems `pip install enclave42` does **not** fail: pip silently picks the older 0.1.0 (different packaging, no bundled NVIDIA attestation runtime). Use `enclave42>=0.1.2` so the install fails instead of falling back.
- Python versions other than 3.12 are not validated for this release (the package metadata says >=3.9; its pinned dependency `pqcrypto==0.3.4` has no installable distribution on Python 3.14 in our check).
- GPU attestation uses the bundled NVIDIA `nvattest` runtime and needs outbound network access to NVIDIA's RIM/OCSP services; if it cannot verify, the dimension is reported as not verified — never as verified.
- In the validated confidential run, five dimensions were VERIFIED (freshness, hardware TEE, debug disabled, GPU attestation, public-key binding); `workload_binding` and `model_revision_binding` are reported UNSUPPORTED.
- The wheel bundles third-party open-source libraries (some LGPL). Notices: `enclave42-0.1.2.dist-info/licenses/`. Corresponding sources and replacement procedure: see the files next to this one.
