# Replacing a bundled LGPL library (enclave42 0.1.2)

Ten bundled libraries are LGPL: libgmp, libnettle, libhogweed, libgnutls, libidn2, libunistring, libtasn1, libkeyutils, librtmp, libssh (files in `site-packages/enclave42.libs/`, loaded dynamically). Exact sources, Debian patches and checksums: [LGPL_PROVENANCE.md](LGPL_PROVENANCE.md) and the release archives.

## How the shipped files relate to the Ubuntu binaries
Every shipped file is the Ubuntu 24.04 binary plus one `patchelf` 0.19.1 invocation that renames the SONAME, rewrites the NEEDED entries that point to other bundled libraries, and (where applicable) sets `DT_RPATH` to `$ORIGIN` — reproduced byte for byte:

| Library file | `patchelf` invocation applied to the Ubuntu binary to obtain the shipped file |
|---|---|
| `libgmp-0ccdfb6d.so.10.5.0` | `patchelf --set-soname libgmp-0ccdfb6d.so.10.5.0 <input>` |
| `libnettle-a245ed91.so.8.8` | `patchelf --set-soname libnettle-a245ed91.so.8.8 <input>` |
| `libhogweed-c3c60613.so.6.8` | `patchelf --set-soname libhogweed-c3c60613.so.6.8 --replace-needed libnettle.so.8 libnettle-a245ed91.so.8.8 --replace-needed libgmp.so.10 libgmp-0ccdfb6d.so.10.5.0 --force-rpath --set-rpath '$ORIGIN' <input>` |
| `libgnutls-ddbae299.so.30.37.1` | `patchelf --set-soname libgnutls-ddbae299.so.30.37.1 --replace-needed libp11-kit.so.0 libp11-kit-a59efd47.so.0.3.1 --replace-needed libidn2.so.0 libidn2-6e632fd9.so.0.4.0 --replace-needed libunistring.so.5 libunistring-7bcf825c.so.5.0.0 --replace-needed libtasn1.so.6 libtasn1-59994414.so.6.6.3 --replace-needed libnettle.so.8 libnettle-a245ed91.so.8.8 --replace-needed libhogweed.so.6 libhogweed-c3c60613.so.6.8 --replace-needed libgmp.so.10 libgmp-0ccdfb6d.so.10.5.0 --force-rpath --set-rpath '$ORIGIN' <input>` |
| `libidn2-6e632fd9.so.0.4.0` | `patchelf --set-soname libidn2-6e632fd9.so.0.4.0 --replace-needed libunistring.so.5 libunistring-7bcf825c.so.5.0.0 --force-rpath --set-rpath '$ORIGIN' <input>` |
| `libunistring-7bcf825c.so.5.0.0` | `patchelf --set-soname libunistring-7bcf825c.so.5.0.0 <input>` |
| `libtasn1-59994414.so.6.6.3` | `patchelf --set-soname libtasn1-59994414.so.6.6.3 <input>` |
| `libkeyutils-f4821441.so.1.10` | `patchelf --set-soname libkeyutils-f4821441.so.1.10 <input>` |
| `librtmp-15a2a75e.so.1` | `patchelf --set-soname librtmp-15a2a75e.so.1 --replace-needed libgnutls.so.30 libgnutls-ddbae299.so.30.37.1 --replace-needed libhogweed.so.6 libhogweed-c3c60613.so.6.8 --replace-needed libnettle.so.8 libnettle-a245ed91.so.8.8 --replace-needed libgmp.so.10 libgmp-0ccdfb6d.so.10.5.0 --force-rpath --set-rpath '$ORIGIN' <input>` |
| `libssh-b82bd54e.so.4.9.6` | `patchelf --set-soname libssh-b82bd54e.so.4.9.6 --replace-needed libcrypto.so.3 libcrypto-6a66c3ba.so.3 --replace-needed libgssapi_krb5.so.2 libgssapi_krb5-6c1b8169.so.2.2 --force-rpath --set-rpath '$ORIGIN' <input>` |

## Integrity control (VENDORED_SHA256)
Before use, the SDK checks the SHA-256 of each file of `enclave42.libs/` against the table `VENDORED_SHA256` in `confidential/providers/backend_01/packaged_nvattest.py`, requires the directory inventory to equal that table, and then runs `nvattest` from a private temporary copy. On any difference it refuses to run (fail-closed). This control is unchanged. It protects against corruption and partial substitution; it does not prevent a user who can edit the package files from changing the table.

## To use your own build of one of the ten libraries
1. Build a replacement that is ABI-compatible with the original.
2. Give it the shipped SONAME and dependency names with the recipe above, e.g. `patchelf --set-soname libgmp-0ccdfb6d.so.10.5.0 libgmp.so.10.5.0` (and the `--replace-needed` / `--force-rpath --set-rpath '$ORIGIN'` options listed for libraries that depend on other bundled ones). Check with `readelf -d`.
3. Copy it over the file in `site-packages/enclave42.libs/`, **keeping the exact file name**. Adding or renaming files is refused.
4. Re-pin it: `python repin_vendored_library.py <file name>` (same interpreter as the install). It rewrites that one SHA-256 in `packaged_nvattest.py`.

A runtime modified this way is not the runtime Enclave42 validated: attestation results obtained with it are outside Enclave42's verification guarantees and are not supported. Reinstalling the wheel restores the original.

Limits, documented rather than hidden: the procedure edits a Python module of the package; whether this satisfies each licence's requirements for modification and replacement is a legal question not answered here. The procedure was exercised on a scratch copy with a stand-in library (one appended byte), not with a rebuilt library.
