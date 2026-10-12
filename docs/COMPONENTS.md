# Components redistributed in the Enclave42 SDK 0.1.2 wheel

Wheel: `enclave42-0.1.2-py3-none-manylinux_2_39_x86_64.whl`, sha256 `d7fb0e7cb7aa607f7a634d6c0824616f1953447161a49bad158c474153833555` (not hosted here).

## A. 36 shared libraries in `enclave42.libs/` (dynamic; file and SONAME renamed by auditwheel)

| Vendored file | Package | Version | Licence (determined, not legal advice) | SHA-256 |
|---|---|---|---|---|
| `libbrotlicommon-a91ead09.so.1.1.0` | libbrotli1 | 1.1.0-2build2 | MIT | `ab1458632b3f5508525ec3089ae4d3d19376fedec8e8aa75adcd3c5a8b1862d5` |
| `libbrotlidec-64d8a501.so.1.1.0` | libbrotli1 | 1.1.0-2build2 | MIT | `f472b061e147f8a2a31ce9c10f37ad725994700a2781d35681282d7c3b7f7aec` |
| `libcom_err-022943b3.so.2.1` | libcom-err2 | 1.47.0-2.4~exp1ubuntu4.1 | MIT-style (lib/et); package copyright also lists GPL/LGPL for other e2fsprogs libs | `ace50d22c97cb18f3b8462feeef7fdf137188eb590069ae599102366af1985ce` |
| `libcrypto-6a66c3ba.so.3` | libssl3t64 | 3.0.13-0ubuntu3.15 | Apache-2.0 | `b3403bd30617b58f8f44bdc033e18b4bfab3eeb30f58ba67e37098a636e90119` |
| `libcurl-eac8f2e9.so.4.8.0` | libcurl4t64 | 8.5.0-2ubuntu10.13 | curl (MIT-style) | `42103fefa54ff89b46a6ec836eb3411abfdd5b76eeb34438913ef1e96d8b4139` |
| `libffi-00f593fe.so.8.1.4` | libffi8 | 3.4.6-1build1 | MIT | `d3666af0d72f4c121c4d6c605bd597b820b386d75ffb5122f4b4d67ecd91d574` |
| `libgmp-0ccdfb6d.so.10.5.0` | libgmp10 | 2:6.3.0+dfsg-2ubuntu6.1 | LGPL-3.0-or-later OR GPL-2.0-or-later (choose LGPL-3+) | `1560a9d8decd4ee97e3e14eb771cea4e80d299364b4484c139158e2c68df4d7b` |
| `libgnutls-ddbae299.so.30.37.1` | libgnutls30t64 | 3.8.3-1.1ubuntu3.6 | LGPL-2.1-or-later | `2d524265c643b505465bde37dba011b07d3683dbae8244e60e573cc438412471` |
| `libgssapi_krb5-6c1b8169.so.2.2` | libgssapi-krb5-2 | 1.20.1-6ubuntu2.8 | MIT-style (MIT Kerberos) | `65d3565864b0ec947c627436ffe592454c965d4e98145c015e1558356f43b5a0` |
| `libhogweed-c3c60613.so.6.8` | libhogweed6t64 | 3.9.1-2.2build1.1 | LGPL-3.0-or-later OR GPL-2.0-or-later | `95940bb68b12c9e2b1670753d45ff1811d6444d538a0cc496098257c9c8b0ce0` |
| `libicudata-ddbb3718.so.74.2` | libicu74 | 74.2-1ubuntu3.1 | Unicode License (ICU) | `982dd9026375f4354f88c2badc71e6af5e1135777b8f43aec110d6b4d9ffe3f6` |
| `libicuuc-7560aadd.so.74.2` | libicu74 | 74.2-1ubuntu3.1 | Unicode License (ICU) | `1ff55419837f5228602dd12da425e38a1d818b00ec25d3dae9b6de2831ddcaab` |
| `libidn2-6e632fd9.so.0.4.0` | libidn2-0 | 2.3.7-2build1.1 | LGPL-3.0-or-later OR GPL-2.0-or-later (library) | `9682c25c6ea3a2081aa977ebf0b8b8ada6a20a4500e3310908c5749dd9da2f83` |
| `libk5crypto-73bc9d72.so.3.1` | libk5crypto3 | 1.20.1-6ubuntu2.8 | MIT-style (MIT Kerberos) | `1907fe52588852bf5e511efa7f8827686e15e1de0cb887e99475040b58ad9757` |
| `libkeyutils-f4821441.so.1.10` | libkeyutils1 | 1.6.3-3build1 | LGPL-2.1-or-later (Debian tag: LGPL-2+) | `0602ec3462deaa353e9d89760bd55d8d0ea9c8b5080eac0f2ffdb674a530153a` |
| `libkrb5-9615a284.so.3.3` | libkrb5-3 | 1.20.1-6ubuntu2.8 | MIT-style (MIT Kerberos) | `1e29f19f18f98ce33942679cc968d2c139c10c3acb13022f77124e041a0bfedd` |
| `libkrb5support-0aa43578.so.0.1` | libkrb5support0 | 1.20.1-6ubuntu2.8 | MIT-style (MIT Kerberos) | `a0cdc88c4a95897a2094b54e2cae74ef182f8424c98441e6ac0e9197a1e940d0` |
| `liblber-ddf14275.so.2.0.200` | libldap2 | 2.6.10+dfsg-0ubuntu0.24.04.1 | OpenLDAP Public License 2.8 | `a3678cdf5fa8a6952577c598c5ba2a1279a70883ce4fbbf0a0d57e8b33e9cc29` |
| `libldap-a9829b99.so.2.0.200` | libldap2 | 2.6.10+dfsg-0ubuntu0.24.04.1 | OpenLDAP Public License 2.8 | `4921ae7fc3890dd0ecfeb8db8c9f2bc7091970e18537819e80e117ce97da7b77` |
| `liblzma-696e868d.so.5.4.5` | liblzma5 | 5.6.1+really5.4.5-1ubuntu0.3 | 0BSD / public domain (liblzma 5.4.5) | `6e5cff05a1dda972aad37796430d523b2c75361b0e29a40322015996e305c8fb` |
| `libnettle-a245ed91.so.8.8` | libnettle8t64 | 3.9.1-2.2build1.1 | LGPL-3.0-or-later OR GPL-2.0-or-later | `2b1d650bcce0400f889eb0d2df3cdfa03eec26f6229399df49a093301ecff6f1` |
| `libnghttp2-46764ab5.so.14.26.0` | libnghttp2-14 | 1.59.0-1ubuntu0.4 | MIT | `3f768f4eef5862291c6fe4ad8477356388cdd8089223e0802b6cae9daf346c14` |
| `libnvat-14f5ec4a.so.1.2.2` | NVIDIA attestation-sdk 1.2.2 | 1.2.2 (NVIDIA) | Apache-2.0 (+ statically linked Rust crates, see below) | `7e1d3fbf95de4cf1536640529862c55d39c7af9b55e2703c4c65934c982f7f5e` |
| `libp11-kit-a59efd47.so.0.3.1` | libp11-kit0 | 0.25.3-4ubuntu2.2 | BSD-3-Clause | `76ef9662515b524daaca566dd6a5329005ea6b605b0db6efca5a89e7ace10fae` |
| `libpsl-ae6c5a9a.so.5.3.4` | libpsl5t64 | 0.21.2-1.1build1 | MIT | `053a2a8d3653ad71dd7757555f3f37cac88084f06f872526c6ffa58b7e32ab7c` |
| `librtmp-15a2a75e.so.1` | librtmp1 | 2.4+20151223.gitfa8646d.1-2build7 | LGPL-2.1 | `4b46f92297d5c906b5f1b58e58a6c520e8662d0a517f635907e628104886e104` |
| `libsasl2-a0f410ad.so.2.0.25` | libsasl2-2 | 2.1.28+dfsg1-5ubuntu3.1 | BSD-style (CMU) | `fca83c28f34f0a5d39c414461dec51d1b1efe99b62dea6b9b9199c991ee72cd3` |
| `libssh-b82bd54e.so.4.9.6` | libssh-4 | 0.10.6-2ubuntu0.5 | LGPL-2.1-or-later (Debian: LGPL-2.1+~OpenSSL) | `b00802e83c182607142c07c0411150ffb250468f0b7a3b1efbc081c721847d1a` |
| `libssl-8e49cebd.so.3` | libssl3t64 | 3.0.13-0ubuntu3.15 | Apache-2.0 | `44a23b0a8ac3b117b2e3d332601c6dde088a5281bca7f00d2e2d0189961eac48` |
| `libtasn1-59994414.so.6.6.3` | libtasn1-6 | 4.19.0-3ubuntu0.24.04.2 | LGPL-2.1-or-later | `08d928ab7aa234a2dad8daf8ab0b6e07f9d0a22cfdbdf60bccdb588a284d570a` |
| `libunistring-7bcf825c.so.5.0.0` | libunistring5 | 1.1-2build1.1 | LGPL-3.0-or-later OR GPL-2.0-or-later | `4caf0e86092940b8cf995dc47ab48f518acb8b391f57817a3881198b5acfc227` |
| `libxml2-8b6f68c2.so.2.9.14` | libxml2 | 2.9.14+dfsg-1.3ubuntu3.8 | MIT | `e91d0d33c782fafcb3e7a2c96ac22dabf65c9a18b6b5ecf0f9a54e05ad92f04e` |
| `libxmlsec1-0a0920b8.so.1.2.39` | libxmlsec1t64 | 1.2.39-5build2 | MIT | `e7cd2c8b4f328fd98e18c15181599eb361d577a43bd85c25901ad748244ec46f` |
| `libxmlsec1-openssl-0c5b28d6.so.1.2.39` | libxmlsec1t64-openssl | 1.2.39-5build2 | MIT | `41af099a325e181d0b3df72a5a619bfcafa245f3b5c11c9cb3dc3073abba4be6` |
| `libxslt-a4215f84.so.1.1.39` | libxslt1.1 | 1.1.39-0exp1ubuntu0.24.04.3 | MIT | `f7b6a1c652b96a15f961997ae23c229f8869f4caccdf111e8a9d9a25077eb2c4` |
| `libzstd-0a2128bc.so.1.5.5` | libzstd1 | 1.5.5+dfsg2-2build1.1 | BSD-3-Clause (choose BSD; dual GPL-2.0) | `1ccfe0bc51c4429a4d01e8a94a26bf4f8b5d8f4caf61760d68e3a22e09d4e542` |

Libraries whose source is provided: see `SOURCE_AVAILABILITY.md`. Binary-to-package check: for 27 of the 35 Ubuntu libraries (all 10 LGPL ones) the code sections are identical to the exact Ubuntu `.deb`; 8 could not be checked because their `.deb` files are no longer in the public Ubuntu pool (libcrypto, libssl, libcurl, libgssapi_krb5, libk5crypto, libkrb5, libkrb5support, libxml2).

## B. Executables in the wheel

- `nvattest` 1.2.2 — NVIDIA attestation-sdk (Apache-2.0), commit `9d12801cea8a198ea0f29640dfaf8a4017c841c5`, **modified by Enclave42** (patch `0001-enclave42-bounded-http-and-caches.patch`, sha256 `d472ed6d889fc11643913efb95e4ea35a79d329b41bb951abb1a33108a20a667`); statically includes CLI11 2.6.1 (BSD-3-Clause), nlohmann/json 3.12.0 (MIT), spdlog 1.14.1 (MIT), {fmt} 10.2.1 (MIT).
- `libnvat.so.1.2.2` — NVIDIA attestation-sdk (Apache-2.0), unmodified; statically includes regorus 0.4.0 and Rust crates (see `rust-libnvat/` in the compliance archive), jwt-cpp 0.7.1 (MIT) with picojson (BSD-2-Clause), nlohmann/json, fmt, spdlog.
- `dcap_runtime` — Enclave42 Rust binary; its crates are listed in `notices/THIRD_PARTY_NOTICES.txt`.

Machine-readable: `native-libraries.json`, `LGPL-LIBRARIES.json`.
