#!/usr/bin/env python3
"""Re-pin ONE replaced vendored library in an installed enclave42 0.1.2.

For users exercising their LGPL right to replace a bundled library
(see LGPL_REPLACEMENT_PROCEDURE.md). Run with the same interpreter that has
enclave42 installed, AFTER copying your ABI-compatible replacement over the
file in site-packages/enclave42.libs/ (keep the exact same file name).

    python repin_vendored_library.py libgmp-0ccdfb6d.so.10.5.0

It rewrites only that library's SHA-256 in confidential/providers/backend_01/
packaged_nvattest.py. A runtime modified this way is NOT the runtime Enclave42
validated: attestation results obtained with it are outside Enclave42's
verification guarantees.
"""
import hashlib, importlib.util, pathlib, re, sys

if len(sys.argv) != 2 or "/" in sys.argv[1]:
    sys.exit(__doc__)
name = sys.argv[1]
spec = importlib.util.find_spec("confidential")
root = pathlib.Path(list(spec.submodule_search_locations)[0]).parent
lib = root / "enclave42.libs" / name
module = root / "confidential/providers/backend_01/packaged_nvattest.py"
if not lib.is_file():
    sys.exit(f"not found: {lib}")
src = module.read_text("utf-8")
m = re.search(r"'%s': '([0-9a-f]{64})'" % re.escape(name), src)
if not m:
    sys.exit("library name is not in the pinned table (inventory must stay identical)")
new = hashlib.sha256(lib.read_bytes()).hexdigest()
module.write_text(src.replace(m.group(0), "'%s': '%s'" % (name, new)), "utf-8")
print(f"{name}: {m.group(1)[:12]}... -> {new[:12]}...")
