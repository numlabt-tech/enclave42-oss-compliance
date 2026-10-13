# Enclave42 SDK 0.1.2 — open-source compliance materials

Public compliance materials for **Enclave42 SDK 0.1.2** (Python package `enclave42`, published on PyPI; wheel `enclave42-0.1.2-py3-none-manylinux_2_39_x86_64.whl`, sha256 `d7fb0e7cb7aa607f7a634d6c0824616f1953447161a49bad158c474153833555`).
This repository does **not** contain the wheel. Current version of this material set: `oss-g2-0.1.2-v2` (documentation revision of `v1`; `v1` is kept unchanged).

**Contact:** support@enclave42.com

## Downloads (release `oss-g2-0.1.2-v2`)
Release page: https://github.com/numlabt-tech/enclave42-oss-compliance/releases/tag/oss-g2-0.1.2-v2

| File | SHA-256 |
|---|---|
| [enclave42-0.1.2-lgpl-corresponding-sources.tar](https://github.com/numlabt-tech/enclave42-oss-compliance/releases/download/oss-g2-0.1.2-v2/enclave42-0.1.2-lgpl-corresponding-sources.tar) — upstream sources, Ubuntu `.dsc` and Debian patch tarballs of the LGPL libraries (byte-identical to the file in `v1`) | `a51365007a8b689639120457ae67b8b518dcb0e4c552f5ef19b06b701229309d` |
| [enclave42-0.1.2-lgpl-ubuntu-debs.tar](https://github.com/numlabt-tech/enclave42-oss-compliance/releases/download/oss-g2-0.1.2-v2/enclave42-0.1.2-lgpl-ubuntu-debs.tar) — the ten exact Ubuntu binary packages the LGPL libraries derive from (`DEBS.SHA256` inside) | `7f1a8e3618c7538e1e0344281832ade489bbfeb8041e0d78149726ed3e733ba5` |
| [enclave42-0.1.2-oss-compliance-g2-0.1.2-v2.tar.gz](https://github.com/numlabt-tech/enclave42-oss-compliance/releases/download/oss-g2-0.1.2-v2/enclave42-0.1.2-oss-compliance-g2-0.1.2-v2.tar.gz) — licence texts, upstream licence files, `debian/copyright`, Debian patch series, attribution register, inventories, evidence (own `MANIFEST.sha256`) | `7464d4df1e1f1068cb1ffc947f8dedd5c0d8328bb7f4d62ef25b0c5b76714f90` |
| [SHA256SUMS](https://github.com/numlabt-tech/enclave42-oss-compliance/releases/download/oss-g2-0.1.2-v2/SHA256SUMS) — all release files (also attached: the documents under `docs/` and `tools/repin_vendored_library.py`) | |

Verify: download all release files into one directory, then `sha256sum -c SHA256SUMS`.

### What changed from `v1`
Corrected statements (35/35 Ubuntu libraries matched to exact `.deb`; `libcom_err` licence identified; regorus tag equals the crates.io package; signature results), new attribution register for components inside libnvat, LGPL provenance and replacement recipe, the ten `.deb` files, and a factual `SOURCE_AVAILABILITY.md`. The `v1` release remains at https://github.com/numlabt-tech/enclave42-oss-compliance/releases/tag/oss-g2-0.1.2-v1.

## What is redistributed in the wheel
Full table: [docs/COMPONENTS.md](docs/COMPONENTS.md); static components of libnvat: [docs/LIBNVAT_STATIC_ATTRIBUTIONS.md](docs/LIBNVAT_STATIC_ATTRIBUTIONS.md); LGPL provenance: [docs/LGPL_PROVENANCE.md](docs/LGPL_PROVENANCE.md); machine-readable [inventory/](inventory/).
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
1. **Hosting:** the sources are available from this repository's releases and from archive.ubuntu.com ([docs/SOURCE_AVAILABILITY.md](docs/SOURCE_AVAILABILITY.md)). No availability period is stated in these documents and no guarantee is given about third-party hosting.
2. **libnvat's statically linked Rust dependencies are not proven complete.** The original `Cargo.lock` of the libnvat build does not exist in any recoverable form, and none has been reconstructed. Register: [docs/LIBNVAT_STATIC_ATTRIBUTIONS.md](docs/LIBNVAT_STATIC_ATTRIBUTIONS.md) — 58 component versions proven (read from the binary or source-pinned, crates.io checksum verified, licence files included), 39 crate/standard-library names seen only as symbols and 12 precautionary declared dependencies, all marked `VERSION_NOT_PROVEN`, plus 6 C++ / git-tag pins. No GPL-family licence appears in any published version of these crates, but the list may be incomplete.
3. regorus 0.4.0: crates.io licence metadata says "non-standard"; its LICENSE file is MIT. The `src/` tree of the git tag used by the build is identical to the crates.io 0.4.0 package.
4. All 35 Ubuntu libraries (including the ten LGPL ones) have code sections identical to the exact Ubuntu `.deb` packages (27 from the Ubuntu archive, 8 — libcrypto, libssl, libcurl, libgssapi_krb5, libk5crypto, libkrb5, libkrb5support, libxml2 — from Launchpad, where those superseded versions are still hosted). Each of the ten LGPL libraries is also reproduced byte for byte from its `.deb` by one `patchelf` invocation ([docs/LGPL_PROVENANCE.md](docs/LGPL_PROVENANCE.md)).
5. `libcom_err`: the upstream e2fsprogs `NOTICE` states that `lib/et` is under an MIT-style licence; the source headers confirm it (MIT SIPB; `com_right.c` BSD-3-Clause KTH; `vfprintf.c` Berkeley BSD). The Debian package copyright file lists GPL/LGPL for other e2fsprogs components, which are not part of this library.
6. Upstream GPG signatures: 6 of 9 source packages verify ("Good signature") with the keys shipped in the Debian packaging — trust in those keys was not independently established; gmp (repackaged), keyutils and rtmpdump ship no upstream signature. SHA-256 values of all source files were verified against the Ubuntu `.dsc` files.
7. Component licences are those determined from Debian copyright files and upstream sources; third-party files keep their own licences.
