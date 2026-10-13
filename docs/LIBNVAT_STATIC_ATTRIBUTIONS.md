# Static components inside libnvat and nvattest — attribution register

**Status: NOT exhaustive and NOT a lockfile.** The original `Cargo.lock` of the `libnvat.so.1.2.2` build does not exist in any recoverable form, so no complete dependency list is claimed. Components are listed at the level of proof actually obtained. Machine-readable: [`inventory/libnvat-static-attributions.json`](../inventory/libnvat-static-attributions.json). Licence texts: [`notices/libnvat-static/`](../notices/libnvat-static/).

libnvat sha256 `14f5ec4a074f0549dd112a82f8e0d39545472c170f87f9fa8f1a11c1e9241542`; built with rustc `1.99.0 (b940084d7 2026-09-28)`; NVIDIA attestation-sdk commit `9d12801cea8a198ea0f29640dfaf8a4017c841c5`. Contact: support@enclave42.com.

| Level | Meaning | Count |
|---|---|---|
| `VERSION_PROVEN` | version read from the binary (or source-pinned) and crates.io checksum verified | 58 |
| `VERSION_NOT_PROVEN` (symbol) | crate/std name seen as a symbol only | 39 |
| `VERSION_NOT_PROVEN` (precautionary) | declared non-optional dependency of a proven crate, not seen in the binary | 12 |
| `VERSION_PINNED_BY_SOURCE` | C++ / git-tag pins in the NVIDIA CMake files | 6 |

22 of the 58 proven versions have no attribution in the notices shipped inside the published wheels 0.1.1/0.1.2 (the wheels are immutable; this register and the licence texts are published externally).

## A. Proven versions (Rust crates, checksum-verified)

| Crate | Version | Licence (crates.io) | SHA-256 of .crate | Licence files | In wheel notices |
|---|---|---|---|---|---|
| [ahash](https://crates.io/crates/ahash/0.8.12) | 0.8.12 | MIT OR Apache-2.0 | `5a15f179cd60c4584b8a8c596927aadc462e27f2ca70c04e0071964a73ba7a75` | LICENSE-APACHE, LICENSE-MIT | NO_ATTRIBUTION_FOUND |
| [aho-corasick](https://crates.io/crates/aho-corasick/1.1.5) | 1.1.5 | Unlicense OR MIT | `c982642fa9e8606056828ee9a8505737230110bb1099153c79efe865c59d12ba` | COPYING, LICENSE-MIT, UNLICENSE | NO_ATTRIBUTION_FOUND |
| [anyhow](https://crates.io/crates/anyhow/1.0.104) | 1.0.104 | MIT OR Apache-2.0 | `330a5ed07fa54e4702c9d6c4174f74427fc0ef6e214bbd677ae50a5099946470` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [base64](https://crates.io/crates/base64/0.22.1) | 0.22.1 | MIT OR Apache-2.0 | `72b3254f16251a8381aa12e40e3c4d2f0199f8c6508fbecb9d91f575e0fbb8c6` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [bit-set](https://crates.io/crates/bit-set/0.8.0) | 0.8.0 | Apache-2.0 OR MIT | `08807e080ed7f9d5433fa9b275196cfc35414f66a0c79d864dc51a0d825231a3` | LICENSE-APACHE, LICENSE-MIT | NO_ATTRIBUTION_FOUND |
| [bit-vec](https://crates.io/crates/bit-vec/0.8.0) | 0.8.0 | Apache-2.0 OR MIT | `5e764a1d40d510daf35e07be9eb06e75770908c27d411ee6c92109c9840eaaf7` | LICENSE-APACHE, LICENSE-MIT | NO_ATTRIBUTION_FOUND |
| [chrono](https://crates.io/crates/chrono/0.4.45) | 0.4.45 | MIT OR Apache-2.0 | `1aa79e62e7697b8e29b513a68abacf485adcd1fe8284a4316c5ae868e6633327` | LICENSE.txt | ATTRIBUTED_BY_NAME_MATCH |
| [chrono-tz](https://crates.io/crates/chrono-tz/0.10.4) | 0.10.4 | MIT OR Apache-2.0 | `a6139a8597ed92cf816dfb33f5dd6cf0bb93a6adc938f11039f371bc5bcd26c3` | LICENSE | NO_ATTRIBUTION_FOUND |
| [data-encoding](https://crates.io/crates/data-encoding/2.11.1) | 2.11.1 | MIT | `4583a4551df46e2792f82ceeac45e850d2e2d5debba0b91f102385cda5b11f06` | LICENSE | ATTRIBUTED_BY_NAME_MATCH |
| [email_address](https://crates.io/crates/email_address/0.2.9) | 0.2.9 | MIT | `e079f19b08ca6239f47f8ba8509c11cf3ea30095831f7fed61441475edd8c449` | LICENSE | NO_ATTRIBUTION_FOUND |
| [fancy-regex](https://crates.io/crates/fancy-regex/0.14.0) | 0.14.0 | MIT | `6e24cb5a94bcae1e5408b0effca5cd7172ea3c5755049c5f3af4cd283a165298` | LICENSE | NO_ATTRIBUTION_FOUND |
| [fluent-uri](https://crates.io/crates/fluent-uri/0.3.2) | 0.3.2 | MIT | `1918b65d96df47d3591bed19c5cca17e3fa5d0707318e4b5ef2eae01764df7e5` | LICENSE | NO_ATTRIBUTION_FOUND |
| [form_urlencoded](https://crates.io/crates/form_urlencoded/1.2.2) | 1.2.2 | MIT OR Apache-2.0 | `cb4cb245038516f5f85277875cdaa4f7d2c9a0fa0468de06ed190163b1581fcf` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [fraction](https://crates.io/crates/fraction/0.15.4) | 0.15.4 | MIT OR Apache-2.0 | `e076045bb43dac435333ed5f04caf35c7463631d0dae2deb2638d94dd0a5b872` | LICENSE-APACHE, LICENSE-MIT | NO_ATTRIBUTION_FOUND |
| [hashbrown](https://crates.io/crates/hashbrown/0.17.1) | 0.17.1 | MIT OR Apache-2.0 | `ed5909b6e89a2db4456e54cd5f673791d7eca6732202bbf2a9cc504fe2f9b84a` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [iana-time-zone](https://crates.io/crates/iana-time-zone/0.1.65) | 0.1.65 | MIT OR Apache-2.0 | `e31bc9ad994ba00e440a8aa5c9ef0ec67d5cb5e5cb0cc7f8b744a35b389cc470` | LICENSE-APACHE, LICENSE-MIT | NO_ATTRIBUTION_FOUND |
| [icu_collections](https://crates.io/crates/icu_collections/2.3.0) | 2.3.0 | Unicode-3.0 | `fa68d21081c4a05d5a901a1c62add574c77048b6a1c67be3b50ce0b60d4ca513` | LICENSE | ATTRIBUTED_BY_NAME_MATCH |
| [icu_locale_core](https://crates.io/crates/icu_locale_core/2.3.0) | 2.3.0 | Unicode-3.0 | `d56e28588da92eee5c3201a6eff33fabdd49b62269c8938d4ff050ce4d900deb` | LICENSE | ATTRIBUTED_BY_NAME_MATCH |
| [icu_normalizer](https://crates.io/crates/icu_normalizer/2.3.0) | 2.3.0 | Unicode-3.0 | `12f9cf5f235641ed274641dd81c3f28d870e276763d0797aeeab72317b1c646f` | LICENSE | ATTRIBUTED_BY_NAME_MATCH |
| [icu_provider](https://crates.io/crates/icu_provider/2.3.1) | 2.3.1 | Unicode-3.0 | `d27bbb9d3abbefac45d55f647c9de1d44aafcd1186eb91879afef17c396c3e73` | LICENSE | ATTRIBUTED_BY_NAME_MATCH |
| [idna](https://crates.io/crates/idna/1.1.0) | 1.1.0 | MIT OR Apache-2.0 | `3b0875f23caa03898994f6ddc501886a45c7d3d62d04d2d90788d47be1b1e4de` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [indexmap](https://crates.io/crates/indexmap/2.14.2) | 2.14.2 | Apache-2.0 OR MIT | `cc4e190f5d26ca7051642629da2c52fc03bde85a03197c99408dcd291734c855` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [itertools](https://crates.io/crates/itertools/0.11.0) | 0.11.0 | MIT OR Apache-2.0 | `b1c173a5686ce8bfa551b3563d0c2170bf24ca44da99c7ca4bfdab5418c3fe57` | LICENSE-APACHE, LICENSE-MIT | NO_ATTRIBUTION_FOUND |
| [itoa](https://crates.io/crates/itoa/1.0.18) | 1.0.18 | MIT OR Apache-2.0 | `8f42a60cbdf9a97f5d2305f08a87dc4e09308d1276d28c869c684d7777685682` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [jsonschema](https://crates.io/crates/jsonschema/0.29.1) | 0.29.1 | MIT | `161c33c3ec738cfea3288c5c53dfcdb32fd4fc2954de86ea06f71b5a1a40bfcd` | LICENSE | NO_ATTRIBUTION_FOUND |
| [lazy_static](https://crates.io/crates/lazy_static/1.5.1) | 1.5.1 | MIT OR Apache-2.0 | `20870f649af7073d53e38067b2a84312175d56ea15217e1b15bc83506ec50afb` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [memchr](https://crates.io/crates/memchr/2.8.3) | 2.8.3 | Unlicense OR MIT | `cf8baf1c55e62ffcace7a9f06f4bd9cd3f0c4beb022d3b367256b91b87513d98` | COPYING, LICENSE-MIT, UNLICENSE | ATTRIBUTED_BY_NAME_MATCH |
| [nom](https://crates.io/crates/nom/7.1.3) | 7.1.3 | MIT | `d273983c5a657a70a3e8f2a01329822f3b8c8172b73826411a55751e404a0a4a` | LICENSE | NO_ATTRIBUTION_FOUND |
| [num-bigint](https://crates.io/crates/num-bigint/0.4.8) | 0.4.8 | MIT OR Apache-2.0 | `c89e69e7e0f03bea5ef08013795c25018e101932225a656383bd384495ecc367` | LICENSE-APACHE, LICENSE-MIT | NO_ATTRIBUTION_FOUND |
| [num-integer](https://crates.io/crates/num-integer/0.1.47) | 0.1.47 | MIT OR Apache-2.0 | `7ce2d95d4b3734dc35aa2f45e1aa22cd416814592a4f9d9205e11affd5b8e10b` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [num-rational](https://crates.io/crates/num-rational/0.4.2) | 0.4.2 | MIT OR Apache-2.0 | `f83d14da390562dca69fc84082e73e548e1ad308d24accdedd2720017cb37824` | LICENSE-APACHE, LICENSE-MIT | NO_ATTRIBUTION_FOUND |
| [once_cell](https://crates.io/crates/once_cell/1.21.4) | 1.21.4 | MIT OR Apache-2.0 | `9f7c3e4beb33f85d45ae3e3a1792185706c8e16d043238c593331cc7cd313b50` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [parking_lot](https://crates.io/crates/parking_lot/0.12.5) | 0.12.5 | MIT OR Apache-2.0 | `93857453250e3077bd71ff98b6a65ea6621a19bb0f559a85248955ac12c45a1a` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [parking_lot_core](https://crates.io/crates/parking_lot_core/0.9.12) | 0.9.12 | MIT OR Apache-2.0 | `2621685985a2ebf1c516881c026032ac7deafcda1a2c9b7850dc81e3dfcb64c1` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [percent-encoding](https://crates.io/crates/percent-encoding/2.3.2) | 2.3.2 | MIT OR Apache-2.0 | `9b4f627cb1b25917193a259e49bdad08f671f8d9708acfd5fe0a8c1455d87220` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [ppv-lite86](https://crates.io/crates/ppv-lite86/0.2.21) | 0.2.21 | MIT OR Apache-2.0 | `85eae3c4ed2f50dcfe72643da4befc30deadb458a9b590d720cde2f2b1e97da9` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [rand](https://crates.io/crates/rand/0.10.3) | 0.10.3 | MIT OR Apache-2.0 | `65c9fb96cbc91e3478eaae79a69fcd3f1ae4ad052e471fe6732fff548984b4af` | COPYRIGHT, LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [rand](https://crates.io/crates/rand/0.9.5) | 0.9.5 | MIT OR Apache-2.0 | `b9ef1d0d795eb7d84685bca4f72f3649f064e6641543d3a8c415898726a57b41` | COPYRIGHT, LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [rand_chacha](https://crates.io/crates/rand_chacha/0.9.0) | 0.9.0 | MIT OR Apache-2.0 | `d3022b5f1df60f26e1ffddd6c66e8aa15de382ae63b3a0c1bfc0e4d3e3f325cb` | COPYRIGHT, LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [referencing](https://crates.io/crates/referencing/0.29.1) | 0.29.1 | MIT | `40a64b3a635fad9000648b4d8a59c8710c523ab61a23d392a7d91d47683f5adc` | LICENSE | ATTRIBUTED_BY_NAME_MATCH |
| [regex](https://crates.io/crates/regex/1.13.1) | 1.13.1 | MIT OR Apache-2.0 | `f020237b6c8eed93db2e2cb53c00c60a8e1bc73da7d073199a1180401450218d` | LICENSE-APACHE, LICENSE-MIT | NO_ATTRIBUTION_FOUND |
| [regex-automata](https://crates.io/crates/regex-automata/0.4.18) | 0.4.18 | MIT OR Apache-2.0 | `ad8553b9b26413251cbf30e620595c7a41b3887f03da04579c0e6b0d6a06b4b2` | LICENSE-APACHE, LICENSE-MIT | NO_ATTRIBUTION_FOUND |
| [regex-syntax](https://crates.io/crates/regex-syntax/0.8.11) | 0.8.11 | MIT OR Apache-2.0 | `d6f6ff9a378485b298a5286656da665ba74413d36db0979633275d2e708145d4` | LICENSE-APACHE, LICENSE-MIT | NO_ATTRIBUTION_FOUND |
| [regorus](https://crates.io/crates/regorus/0.4.0) | 0.4.0 | non-standard | `bf70615014ce5c89fe427197fd9b52e6506916838b449e80ee141adc43adec6b` | LICENSE | NO_ATTRIBUTION_FOUND |
| [scientific](https://crates.io/crates/scientific/0.5.3) | 0.5.3 | MIT | `38a4b339a8de779ecb098a772ecbba2ace74e23ed959a5b4f30631d8bf1799a8` | LICENSE | ATTRIBUTED_BY_NAME_MATCH |
| [semver](https://crates.io/crates/semver/1.0.28) | 1.0.28 | MIT OR Apache-2.0 | `8a7852d02fc848982e0c167ef163aaff9cd91dc640ba85e263cb1ce46fae51cd` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [serde](https://crates.io/crates/serde/1.0.229) | 1.0.229 | MIT OR Apache-2.0 | `4148590afebada386688f18773da617792bf2ef03ffc1e4cbd2b1d45b023e0ba` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [serde_core](https://crates.io/crates/serde_core/1.0.229) | 1.0.229 | MIT OR Apache-2.0 | `67dca2c9c51e58a4791a4b1ed58308b39c64224d349a935ab5039aa360942a48` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [serde_json](https://crates.io/crates/serde_json/1.0.151) | 1.0.151 | MIT OR Apache-2.0 | `c841b55ecdae098c80dcae9cf767f6f8a0c2cdb3416bbef72181df4d0fe73f14` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [serde_yaml](https://crates.io/crates/serde_yaml/0.9.34+deprecated) | 0.9.34+deprecated | MIT OR Apache-2.0 | `6a8b1a1a2ebf674015cc02edccce75287f1a0130d394307b36743c2f5d504b47` | LICENSE-APACHE, LICENSE-MIT | NO_ATTRIBUTION_FOUND |
| [sha2](https://crates.io/crates/sha2/0.10.9) | 0.10.9 | MIT OR Apache-2.0 | `a7507d819769d01a365ab707794a4084392c824f54a7a6a7862f8c3d0892b283` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [smallvec](https://crates.io/crates/smallvec/1.16.2) | 1.16.2 | MIT OR Apache-2.0 | `f9395f0f0eee849a9b707b2f06bb92a6a422090e2123bb2ef8e87a0e61892a8e` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [unsafe-libyaml](https://crates.io/crates/unsafe-libyaml/0.2.11) | 0.2.11 | MIT | `673aac59facbab8a9007c7f6108d11f63b603f7cabff99fabf650fea5c32b861` | LICENSE-MIT | NO_ATTRIBUTION_FOUND |
| [url](https://crates.io/crates/url/2.5.8) | 2.5.8 | MIT OR Apache-2.0 | `ff67a8a4397373c3ef660812acab3268222035010ab8680ec4215f38ba3d0eed` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [uuid](https://crates.io/crates/uuid/1.27.0) | 1.27.0 | Apache-2.0 OR MIT | `97277d36b9c3ace13e58fa6e753f8b0bbbf302a18dd193240d70f9e29681059a` | LICENSE-APACHE, LICENSE-MIT | ATTRIBUTED_BY_NAME_MATCH |
| [wax](https://crates.io/crates/wax/0.6.0) | 0.6.0 | MIT | `8d12a78aa0bab22d2f26ed1a96df7ab58e8a93506a3e20adb47c51a93b4e1357` | LICENSE | NO_ATTRIBUTION_FOUND |
| [zerotrie](https://crates.io/crates/zerotrie/0.2.5) | 0.2.5 | Unicode-3.0 | `4ea269c3bd32f0a32c321907a2ae912ba6f4649bb0fc764a15627e99a7095a3f` | LICENSE | ATTRIBUTED_BY_NAME_MATCH |
| [zerovec](https://crates.io/crates/zerovec/0.11.8) | 0.11.8 | Unicode-3.0 | `bb0464e17806c1d976d5cba29399c7f08e516e279e2ba493f63123b5fca67dd8` | LICENSE | ATTRIBUTED_BY_NAME_MATCH |

## B. Name seen in the binary, version `VERSION_NOT_PROVEN`

Licence column: licences over all crate versions compatible with the declared dependency constraints and published before the build (an envelope, not a proof of the linked version).

| Component | Declared by (constraint check) | Licence envelope | In wheel notices |
|---|---|---|---|
| addr2line | — | MIT OR Apache-2.0 (Rust standard library; per rust-lang COPYRIGHT at the toolchain commit) | NO_ATTRIBUTION_FOUND |
| adler2 | — | MIT OR Apache-2.0 (Rust standard library; per rust-lang COPYRIGHT at the toolchain commit) | NO_ATTRIBUTION_FOUND |
| alloc | — | MIT OR Apache-2.0 (Rust standard library; per rust-lang COPYRIGHT at the toolchain commit) | NO_ATTRIBUTION_FOUND |
| block-buffer | digest@0.10.7 ^0.10 (optional) | MIT OR Apache-2.0 | NAME_PRESENT |
| bytecount | jsonschema@0.29.1 ^0.6 | Apache-2.0/MIT | ABSENT |
| chacha20 | rand@0.10.3 ^0.10.0 (optional) | MIT OR Apache-2.0 | NAME_PRESENT |
| compiler_builtins | — | MIT OR Apache-2.0 (Rust standard library; per rust-lang COPYRIGHT at the toolchain commit) | NO_ATTRIBUTION_FOUND |
| constant_time_eq | regorus@0.4.0 0.4.0 (optional) | CC0-1.0 OR MIT-0 OR Apache-2.0 | ABSENT |
| core | — | MIT OR Apache-2.0 (Rust standard library; per rust-lang COPYRIGHT at the toolchain commit) | NO_ATTRIBUTION_FOUND |
| digest | sha2@0.10.9 ^0.10.7; hmac@0.12.1 ^0.10.3 | MIT OR Apache-2.0 | NAME_PRESENT |
| generic-array | — | MIT | NAME_PRESENT |
| getrandom | ahash@0.8.12 ^0.3.1 (optional); rand@0.10.3 ^0.4.0 (optional) | MIT OR Apache-2.0 | NAME_PRESENT |
| gimli | — | MIT OR Apache-2.0 (Rust standard library; per rust-lang COPYRIGHT at the toolchain commit) | NO_ATTRIBUTION_FOUND |
| hex | regorus@0.4.0 0.4.3 (optional) | MIT OR Apache-2.0 | NAME_PRESENT |
| hmac | regorus@0.4.0 0.12.1 (optional) | MIT OR Apache-2.0 | NAME_PRESENT |
| icu_properties | icu_normalizer@2.3.0 ~2.3.0 (optional) | Unicode-3.0 | NAME_PRESENT |
| libc | parking_lot_core@0.9.12 ^0.2.95 | MIT OR Apache-2.0 | NAME_PRESENT |
| litemap | icu_locale_core@2.3.0 ^0.8.0; zerotrie@0.2.5 ^0.8.0 (optional) | Unicode-3.0 | NAME_PRESENT |
| lock_api | parking_lot@0.12.5 ^0.4.14 | MIT OR Apache-2.0 | NAME_PRESENT |
| md-5 (symbol root "md5") | uuid@1.27.0 ^0.10 (optional); regorus@0.4.0 0.10.6 (optional) | MIT OR Apache-2.0 | NAME_PRESENT |
| miniz_oxide | — | MIT OR Apache-2.0 (Rust standard library; per rust-lang COPYRIGHT at the toolchain commit) | NO_ATTRIBUTION_FOUND |
| num-traits | chrono@0.4.45 ^0.2; num-bigint@0.4.8 ^0.2.18 | MIT OR Apache-2.0, MIT/Apache-2.0 | NAME_PRESENT |
| object | — | MIT OR Apache-2.0 (Rust standard library; per rust-lang COPYRIGHT at the toolchain commit) | NO_ATTRIBUTION_FOUND |
| panic_unwind | — | MIT OR Apache-2.0 (Rust standard library; per rust-lang COPYRIGHT at the toolchain commit) | NO_ATTRIBUTION_FOUND |
| potential_utf | icu_collections@2.3.0 ^0.1.3 | Unicode-3.0 | NAME_PRESENT |
| rand_core | rand@0.10.3 ^0.10.0; rand@0.9.5 ^0.9.0 | MIT OR Apache-2.0 | NAME_PRESENT |
| rustc-demangle | — | MIT OR Apache-2.0 (Rust standard library; per rust-lang COPYRIGHT at the toolchain commit) | NO_ATTRIBUTION_FOUND |
| ryu | serde_yaml@0.9.34+deprecated ^1.0 | Apache-2.0 OR BSL-1.0 | NAME_PRESENT |
| std | — | MIT OR Apache-2.0 (Rust standard library; per rust-lang COPYRIGHT at the toolchain commit) | NO_ATTRIBUTION_FOUND |
| std_detect | — | MIT OR Apache-2.0 (Rust standard library; per rust-lang COPYRIGHT at the toolchain commit) | NO_ATTRIBUTION_FOUND |
| tinystr | icu_locale_core@2.3.0 ^0.8.4 | Unicode-3.0 | NAME_PRESENT |
| typenum | — | MIT OR Apache-2.0, MIT/Apache-2.0 | NAME_PRESENT |
| utf8_iter | icu_collections@2.3.0 ^1.0.2; icu_normalizer@2.3.0 ^1.0.2 (optional) | Apache-2.0 OR MIT | NAME_PRESENT |
| uuid-simd | jsonschema@0.29.1 ^0.8 | MIT | ABSENT |
| writeable | icu_locale_core@2.3.0 ^0.6.4; icu_provider@2.3.1 ^0.6.4 (optional) | Unicode-3.0 | NAME_PRESENT |
| yoke | icu_collections@2.3.0 ^0.8.3; icu_provider@2.3.1 ^0.8.3 | Unicode-3.0 | NAME_PRESENT |
| zerofrom | icu_collections@2.3.0 ^0.1.6; icu_provider@2.3.1 ^0.1.6 | Unicode-3.0 | NAME_PRESENT |
| zmij | serde_json@1.0.151 ^1.0 | MIT | NAME_PRESENT |
| pori | wax@0.6.0 =0.0.0 | MIT (crates.io, candidate versions) | NO_ATTRIBUTION_FOUND |

## C. Precautionary: declared dependencies not observed in the binary (`VERSION_NOT_PROVEN`)

They may be inlined or absent; second-level dependencies were not explored.

| Component | Declared by | Licence envelope |
|---|---|---|
| borrow-or-share | fluent-uri@0.3.2 ^0.2 | CC0-1.0, CC0-1.0 OR MIT, MIT-0 |
| cfg-if | ahash@0.8.12 ^1.0; parking_lot_core@0.9.12 ^1.0.0 | MIT OR Apache-2.0, MIT/Apache-2.0 |
| cpufeatures | sha2@0.10.9 ^0.2 | MIT OR Apache-2.0 |
| either | itertools@0.11.0 ^1.0 | MIT OR Apache-2.0, MIT/Apache-2.0 |
| equivalent | indexmap@2.14.2 ^1.0 | Apache-2.0 OR MIT |
| idna-adapter | idna@1.1.0 ^1 | Apache-2.0 OR MIT |
| log | iana-time-zone@0.1.65 ^0.4.14 | MIT OR Apache-2.0 |
| minimal-lexical | nom@7.1.3 ^0.2.0 | MIT/Apache-2.0 |
| num | fraction@0.15.4 ^0.4.3 | MIT OR Apache-2.0 |
| num-cmp | jsonschema@0.29.1 ^0.1 | MIT/Apache-2.0 |
| phf | chrono-tz@0.10.4 ^0.12 | MIT |
| zerocopy | ahash@0.8.12 ^0.8.24; ppv-lite86@0.2.21 ^0.8.23 | BSD-2-Clause OR Apache-2.0 OR MIT |

## D. C++ components and git-tag pins

| Component | Version | Licence | Source | Licence file (sha256) | Evidence |
|---|---|---|---|---|---|
| jwt-cpp | v0.7.1 | MIT | https://github.com/Thalhammer/jwt-cpp/tree/v0.7.1 | `notices/libnvat-static/cxx/jwt-cpp-v0.7.1-LICENSE` (`35c2d7d6824a1e1e…`) | libnvat (CMake FetchContent GIT_TAG v0.7.1, pinned in NVIDIA source commit 9d12801c) |
| picojson | bundled in jwt-cpp v0.7.1 | BSD-2-Clause (Cybozu Labs, Kazuho Oku) | https://github.com/Thalhammer/jwt-cpp/blob/v0.7.1/include/picojson/picojson.h | `notices/libnvat-static/cxx/jwt-cpp-v0.7.1-picojson.h.head` (`eecfb89d1a72ab38…`) | libnvat symbol "picojson"; license = file header only |
| nlohmann/json | 3.12.0 | MIT | https://github.com/nlohmann/json/releases/tag/v3.12.0 | `notices/libnvat-static/cxx/nlohmann-json-3.12.0-LICENSE.MIT` (`46a65cffd1ea9551…`) | libnvat and nvattest (CMake pin) |
| fmt | 10.2.1 | MIT (+ optional binary exception) | https://github.com/fmtlib/fmt/tree/10.2.1 | `notices/libnvat-static/cxx/fmt-10.2.1-LICENSE` (`07580f2a3b35709c…`) | libnvat and nvattest (CMake pin) |
| spdlog | v1.14.1 | MIT | https://github.com/gabime/spdlog/tree/v1.14.1 | `notices/libnvat-static/cxx/spdlog-1.14.1-LICENSE` (`4ccecab18d1ff0b6…`) | libnvat and nvattest (CMake pin) |
| regorus (git tag regorus-v0.4.0) | 0.4.0 | MIT (LICENSE file; crates.io metadata says "non-standard") | https://github.com/microsoft/regorus/tree/regorus-v0.4.0 | `notices/libnvat-static/cxx/regorus-v0.4.0-git-tag-LICENSE` (`c2cfccb812fe4821…`) | libnvat (CMake FetchContent GIT_TAG regorus-v0.4.0); src/ identical to crates.io package 0.4.0 |

## E. Not claimed
- No complete list of the Rust dependencies of libnvat; no `Cargo.lock`.
- Second-level dependencies of the precautionary crates; platform-specific and proc-macro crates not linked on Linux x86-64.
- The `pori` crate was first classified as C++ by mistake and is listed in section B.
- The register is technical documentation, not legal advice.
