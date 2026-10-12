# Replacing a bundled LGPL library (enclave42 0.1.2)

Ten bundled libraries are LGPL: libgmp, libnettle, libhogweed, libgnutls, libidn2, libunistring, libtasn1, libkeyutils, librtmp, libssh (files in `site-packages/enclave42.libs/`, loaded dynamically). Their exact sources and Debian patches are in `enclave42-0.1.2-lgpl-corresponding-sources.tar`; licence texts in `enclave42-0.1.2-oss-compliance-g2-0.1.2-v1.tar.gz`.

The SDK verifies the SHA-256 of every file in `enclave42.libs/` before use and refuses to run on any difference (fail-closed). To use your own modified or newer build:

1. Build a replacement that is ABI/SONAME-compatible with the original.
2. Copy it over the file in `enclave42.libs/`, **keeping the exact same file name** (for example `libgmp-0ccdfb6d.so.10.5.0`). Adding or renaming files is rejected.
3. Re-pin it: `python repin_vendored_library.py libgmp-0ccdfb6d.so.10.5.0` (same interpreter as the install). This edits one hash in `confidential/providers/backend_01/packaged_nvattest.py`.

**Important:** a runtime modified this way is not the runtime Enclave42 validated. Attestation outcomes produced with it are outside Enclave42's verification guarantees, and Enclave42 cannot support it. Reinstalling the wheel restores the original.
