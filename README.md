# Enclave42 SDK 0.1.2 — open-source compliance materials

Public compliance materials for **Enclave42 SDK 0.1.2** (Python package `enclave42`, wheel `enclave42-0.1.2-py3-none-manylinux_2_39_x86_64.whl`, sha256 `d7fb0e7cb7aa607f7a634d6c0824616f1953447161a49bad158c474153833555`).
This repository does **not** contain the wheel. Version of this material set: `oss-g2-0.1.2-v1`.

**Contact:** support@enclave42.com

## Downloads (release `oss-g2-0.1.2-v1`)
Release page: https://github.com/numlabt-tech/enclave42-oss-compliance/releases/tag/oss-g2-0.1.2-v1

| File | SHA-256 |
|---|---|
| [enclave42-0.1.2-lgpl-corresponding-sources.tar](https://github.com/numlabt-tech/enclave42-oss-compliance/releases/download/oss-g2-0.1.2-v1/enclave42-0.1.2-lgpl-corresponding-sources.tar) — upstream sources, Ubuntu .dsc and Debian patches of the LGPL libraries | `a51365007a8b689639120457ae67b8b518dcb0e4c552f5ef19b06b701229309d` |
| [enclave42-0.1.2-oss-compliance-g2-0.1.2-v1.tar.gz](https://github.com/numlabt-tech/enclave42-oss-compliance/releases/download/oss-g2-0.1.2-v1/enclave42-0.1.2-oss-compliance-g2-0.1.2-v1.tar.gz) — licence texts, upstream licence files, debian/copyright, patch series, component evidence (own `MANIFEST.sha256`) | `acdeba0a38f683df8b4cf6fe4b210d433534fbf51192ed687506c2134ee0873b` |
| [SHA256SUMS](https://github.com/numlabt-tech/enclave42-oss-compliance/releases/download/oss-g2-0.1.2-v1/SHA256SUMS) — all release files | |

Verify: download all release files into one directory, then `sha256sum -c SHA256SUMS`.

## What is redistributed in the wheel
Full table: [docs/COMPONENTS.md](docs/COMPONENTS.md); machine-readable [inventory/](inventory/).
- **36 shared libraries** in `enclave42.libs/` (35 from Ubuntu 24.04 packages + NVIDIA libnvat), loaded dynamically. **Ten are LGPL**: libgmp, libnettle, libhogweed, libgnutls, libidn2, libunistring, libtasn1, libkeyutils, librtmp, libssh. The others are permissive (MIT/BSD/Apache/curl/ICU/OpenLDAP style).
- **nvattest 1.2.2** (NVIDIA attestation-sdk, Apache-2.0, commit `9d12801c…`), modified by Enclave42 — the change is the patch in the SDK source repository; modified files are named in [notices/NATIVE_LIBRARY_NOTICES.txt](notices/NATIVE_LIBRARY_NOTICES.txt). **libnvat 1.2.2** unmodified.
- Statically included code: CLI11, nlohmann/json, spdlog, {fmt}, jwt-cpp/picojson, regorus and Rust crates inside libnvat; Rust crates of `dcap_runtime` (see [notices/THIRD_PARTY_NOTICES.txt](notices/THIRD_PARTY_NOTICES.txt)).
- Licence texts: [licenses/](licenses/) (LGPL-2.1, LGPL-3.0, GPL-2.0, GPL-3.0) and [notices/](notices/).

## Platform limits
Validated only on **Linux x86-64, Ubuntu 24.04 (glibc 2.39), Python 3.12**. The wheel is `manylinux_2_39_x86_64`; there is no wheel for macOS, Windows, ARM or older glibc, and on those systems `pip install enclave42` silently falls back to the older 0.1.0 unless you require `enclave42>=0.1.2`. Details: [docs/INSTALL_AND_PLATFORM_LIMITS.md](docs/INSTALL_AND_PLATFORM_LIMITS.md). Security Receipt offline check: [docs/SECURITY_RECEIPT_VERIFICATION.md](docs/SECURITY_RECEIPT_VERIFICATION.md).

## Replacing a bundled LGPL library
The SDK checks the SHA-256 of every bundled library and refuses to run on a difference. The documented two-step procedure and helper are in [docs/LGPL_REPLACEMENT_PROCEDURE.md](docs/LGPL_REPLACEMENT_PROCEDURE.md) and [tools/repin_vendored_library.py](tools/repin_vendored_library.py).

## Known limitations of this evidence
This is technical documentation, **not legal advice and not a guarantee of compliance**.
1. **Source availability is provisional**: the period of availability and final wording of any written offer are not defined yet ([docs/SOURCE_AVAILABILITY.md](docs/SOURCE_AVAILABILITY.md)).
2. **libnvat's statically linked Rust dependencies are not proven complete.** The original `Cargo.lock` of the libnvat build could not be recovered. Evidence: 58 crate versions (regorus 0.4.0 from the pinned CMake tag, the others from strings embedded in the binary; each checked against its crates.io checksum, licence files included) and 38 further crate/standard-library names found only as symbols, with versions unproven. No GPL-family licence appears in any published version of these crates, but the list may be incomplete ([inventory/crates-evidence.json](inventory/crates-evidence.json)).
3. regorus 0.4.0: crates.io licence metadata says "non-standard"; its LICENSE file is MIT. The build used the git tag; equality with the crates.io package is unverified.
4. For 27 of the 35 Ubuntu libraries (including all ten LGPL ones) the code sections were compared with the exact Ubuntu `.deb`; for 8 (libcrypto, libssl, libcurl, libgssapi_krb5, libk5crypto, libkrb5, libkrb5support, libxml2) the `.deb` is no longer in the public pool, so the match is unverified.
5. The licence of the `libcom_err` object itself (MIT-style vs. other e2fsprogs components) is unconfirmed.
6. GPG signatures (`.asc`) of upstream tarballs are included but not verified; SHA-256 values were verified against the Ubuntu `.dsc` files.
7. Component licences are those determined from Debian copyright files and upstream sources; third-party files keep their own licences.
