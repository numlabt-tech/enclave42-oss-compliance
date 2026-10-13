# Source availability for the LGPL libraries in Enclave42 SDK 0.1.2

This document describes what is actually available and how to obtain it. It states **no period** for which any hosting is maintained and gives no guarantee about third-party hosting.

## Files available now
- **`enclave42-0.1.2-lgpl-corresponding-sources.tar`** (sha256 `a51365007a8b689639120457ae67b8b518dcb0e4c552f5ef19b06b701229309d`), attached to the releases `oss-g2-0.1.2-v1` and `oss-g2-0.1.2-v2` of this repository (identical bytes). It contains, for the nine Ubuntu source packages behind the ten LGPL libraries (libgmp, libnettle, libhogweed, libgnutls, libidn2, libunistring, libtasn1, libkeyutils, librtmp, libssh): the upstream source tarballs, the Ubuntu `.dsc` files, the Debian packaging tarballs (including the security patches applied), and the upstream signature files where Ubuntu ships them. Every file's SHA-256 matches the value in its `.dsc`.
- **`enclave42-0.1.2-lgpl-ubuntu-debs.tar`** (release `oss-g2-0.1.2-v2`): the ten exact Ubuntu 24.04 binary packages from which the bundled libraries were derived, with their SHA-256 values. The bundled files are those binaries plus one `patchelf` invocation each ([LGPL_PROVENANCE.md](LGPL_PROVENANCE.md)).
- **`enclave42-0.1.2-oss-compliance-g2-0.1.2-v2.tar.gz`** (release `oss-g2-0.1.2-v2`): licence texts, verbatim upstream licence files, `debian/copyright`, the Debian patch series, the attribution register and the inventories, with its own `MANIFEST.sha256`.
- The same upstream/Ubuntu files are published by Ubuntu at archive.ubuntu.com; exact URLs are in [`inventory/LGPL-LIBRARIES.json`](../inventory/LGPL-LIBRARIES.json). On 2026-10-13 all 43 URLs listed there (sources, `.dsc` files and the ten `.deb`) answered HTTP 200 ([`inventory/verification/`](../inventory/verification/)). Ubuntu may remove superseded versions from its pool; the release files above are copies.

## Replacement of a bundled library
See [LGPL_REPLACEMENT_PROCEDURE.md](LGPL_REPLACEMENT_PROCEDURE.md).

## Contact
Questions and requests about these materials: **support@enclave42.com**.
