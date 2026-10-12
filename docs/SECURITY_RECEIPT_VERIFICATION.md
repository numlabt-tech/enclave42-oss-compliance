# Verifying a Security Receipt offline (enclave42 0.1.2)

The wheel installs `enclave42-receipt-verify`: an offline Ed25519 verifier (no network, no API key, no database).

1. Save your receipt JSON (for example `receipt.json`).
2. Get Enclave42's public signing-key manifest (the only network step, done by you):
   `curl -fsS https://api.enclave42.com/.well-known/enclave42/security-receipt-keys.json -o keys.json`
3. Verify:
   `enclave42-receipt-verify --receipt receipt.json --manifest keys.json`
   (alternatively `--public-key <base64url key>`). Exit code 0 = PASS, 1 = FAIL; the result is also printed.

What PASS means: the receipt content (including its attestation block) has not been altered since Enclave42 signed it, and its schema is valid. It is not, by itself, a re-verification of the raw hardware evidence. Run `enclave42-receipt-verify --help` for the exact verification levels and caveats.
