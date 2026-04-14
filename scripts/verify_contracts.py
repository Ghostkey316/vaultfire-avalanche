#!/usr/bin/env python3
"""
Vaultfire Protocol — Avalanche C-Chain Contract Verification

Checks all 15 deployed Vaultfire contracts on Avalanche C-Chain (chain ID 43114)
by querying bytecode directly via JSON-RPC. No API keys. No external dependencies.
Python standard library only.

Usage:
    python3 verify_contracts.py            # Human-readable output
    python3 verify_contracts.py --json     # Machine-readable JSON
    python3 verify_contracts.py --verbose  # Include bytecode sizes
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CHAIN_ID = 43114  # Avalanche C-Chain

# RPC endpoint fallback chain — first one that responds wins
_RPC_FALLBACKS: list[str] = [
    "https://api.avax.network/ext/bc/C/rpc",
    "https://avalanche-c-chain-rpc.publicnode.com",
    "https://1rpc.io/avax/c",
    "https://avax.meowrpc.com",
]

RPC_TIMEOUT = 15  # seconds per request

# All 15 Vaultfire contracts on Avalanche C-Chain
# Source: https://github.com/Ghostkey316/ghostkey-316-vaultfire-init (main repo README)
CONTRACTS: dict[str, str] = {
    "ERC8004IdentityRegistry":           "0x57741F4116925341d8f7Eb3F381d98e07C73B4a3",
    "AIPartnershipBondsV2":              "0xea6B504827a746d781f867441364C7A732AA4b07",
    "AIAccountabilityBondsV2":           "0xaeFEa985E0C52f92F73606657B9dA60db2798af3",
    "ERC8004ReputationRegistry":         "0x11C267C8A75B13A4D95357CEF6027c42F8e7bA24",
    "ERC8004ValidationRegistry":         "0x0d41Eb399f52BD03fef7eCd5b165d51AA1fAd87b",
    "VaultfireERC8004Adapter":           "0x6B7dC022edC41EBE41400319C6fDcCeab05Ea053",
    "FlourishingMetricsOracle":          "0x490c51c2fAd743C288D65A6006f6B0ae9e6a8695",
    "MultisigGovernance":                "0xCc7300F39aF4cc2A924f82a5Facd7049436157Ee",
    "VaultfireTeleporterBridge":         "0x0dF0523aF5aF2Aef180dB052b669Bea97fee3d31",
    "DilithiumAttestor":                 "0x211554bd46e3D4e064b51a31F61927ae9c7bCF1f",
    "ProductionBeliefAttestationVerifier": "0xb3d8063e67bdA1a869721D0F6c346f1Af0469D2F",
    "BeliefAttestationVerifier":         "0x227e27e7776d3ee14128BC66216354495E113B19",
    "MissionEnforcement":                "0xcf64D815F5424B7937aB226bC733Ed35ab6CaDcB",
    "AntiSurveillance":                  "0x281814eF92062DA8049Fe5c4743c4Aef19a17380",
    "PrivacyGuarantees":                 "0xc09F0e06690332eD9b490E1040BdE642f11F3937",
}

# USDC on Avalanche C-Chain (native Circle USDC)
USDC_ADDRESS = "0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E"

SNOWTRACE_BASE = "https://snowtrace.io/address/"

# Contract descriptions for display
DESCRIPTIONS: dict[str, str] = {
    "ERC8004IdentityRegistry":           "ERC-8004 agent identity registry",
    "AIPartnershipBondsV2":              "AI partnership bonds (v2) — the stars of the protocol",
    "AIAccountabilityBondsV2":           "AI accountability bonds (v2) — the stars of the protocol",
    "ERC8004ReputationRegistry":         "On-chain agent reputation scores (0–10,000)",
    "ERC8004ValidationRegistry":         "ERC-8004 identity validation registry",
    "VaultfireERC8004Adapter":           "ERC-8004 protocol adapter",
    "FlourishingMetricsOracle":          "Flourishing metrics oracle",
    "MultisigGovernance":                "Multi-signature governance module",
    "VaultfireTeleporterBridge":         "Cross-chain trust portability bridge",
    "DilithiumAttestor":                 "Post-quantum attestor (CRYSTALS-Dilithium)",
    "ProductionBeliefAttestationVerifier": "Production belief attestation verifier",
    "BeliefAttestationVerifier":         "Belief attestation verifier",
    "MissionEnforcement":                "On-chain mission enforcement",
    "AntiSurveillance":                  "Anti-surveillance commitment",
    "PrivacyGuarantees":                 "Privacy guarantees contract",
}


# ---------------------------------------------------------------------------
# RPC helpers
# ---------------------------------------------------------------------------

_active_rpc: str | None = None


def _get_rpc() -> str:
    """
    Find a working Avalanche C-Chain RPC endpoint.

    Tries each endpoint in the fallback list with a lightweight eth_chainId call.
    Caches the first endpoint that responds successfully.
    """
    global _active_rpc
    if _active_rpc is not None:
        return _active_rpc

    for url in _RPC_FALLBACKS:
        try:
            payload = json.dumps({
                "jsonrpc": "2.0",
                "method": "eth_chainId",
                "params": [],
                "id": 1,
            }).encode("utf-8")
            req = urllib.request.Request(
                url,
                data=payload,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read())
            chain = int(data.get("result", "0x0"), 16)
            if chain == CHAIN_ID:
                _active_rpc = url
                return url
        except Exception:
            continue

    # Default fallback
    _active_rpc = _RPC_FALLBACKS[0]
    return _active_rpc


def rpc_request(payload: dict, timeout: int = RPC_TIMEOUT) -> dict:
    """
    Send a JSON-RPC request with automatic fallback.

    Uses _get_rpc() to resolve a working endpoint. If the primary fails,
    tries remaining fallbacks.
    """
    url = _get_rpc()
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read())
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError):
        global _active_rpc
        _active_rpc = None
        for fallback_url in _RPC_FALLBACKS:
            if fallback_url == url:
                continue
            try:
                req2 = urllib.request.Request(
                    fallback_url,
                    data=body,
                    headers={"Content-Type": "application/json", "Accept": "application/json"},
                    method="POST",
                )
                with urllib.request.urlopen(req2, timeout=timeout) as resp2:
                    result = json.loads(resp2.read())
                _active_rpc = fallback_url
                return result
            except Exception:
                continue
        raise


def eth_get_code(address: str) -> str | None:
    """Get the bytecode at an address. Returns hex string or None."""
    try:
        resp = rpc_request({
            "jsonrpc": "2.0",
            "method": "eth_getCode",
            "params": [address, "latest"],
            "id": 1,
        })
        result = resp.get("result")
        if result and result != "0x" and result != "0x0":
            return result
        return None
    except Exception:
        return None


def eth_call(to: str, data: str) -> str | None:
    """Make a read-only eth_call. Returns hex result or None."""
    try:
        resp = rpc_request({
            "jsonrpc": "2.0",
            "method": "eth_call",
            "params": [{"to": to, "data": data}, "latest"],
            "id": 1,
        })
        result = resp.get("result")
        if result and result != "0x":
            return result
        return None
    except Exception:
        return None


def _short_address(address: str) -> str:
    """Format address as 0xABCD...EF12."""
    addr = address if address.startswith("0x") else "0x" + address
    return f"{addr[:6]}...{addr[-4:]}"


# ---------------------------------------------------------------------------
# Verification logic
# ---------------------------------------------------------------------------

def verify_all_contracts(verbose: bool = False) -> list[dict]:
    """
    Verify all 15 Vaultfire contracts on Avalanche.

    Returns a list of result dicts, one per contract.
    """
    results = []
    for name, address in CONTRACTS.items():
        code = eth_get_code(address)
        has_code = code is not None and len(code) > 4
        bytecode_len = len(code) if code else 0

        result = {
            "name": name,
            "address": address,
            "deployed": has_code,
            "bytecode_chars": bytecode_len,
            "description": DESCRIPTIONS.get(name, ""),
            "snowtrace": SNOWTRACE_BASE + address,
        }
        results.append(result)

    return results


def verify_usdc() -> dict:
    """Verify USDC contract on Avalanche."""
    code = eth_get_code(USDC_ADDRESS)
    has_code = code is not None and len(code) > 4
    return {
        "name": "USDC (Native Circle)",
        "address": USDC_ADDRESS,
        "deployed": has_code,
        "bytecode_chars": len(code) if code else 0,
        "description": "Circle USDC on Avalanche C-Chain",
        "snowtrace": SNOWTRACE_BASE + USDC_ADDRESS,
    }


def verify_chain_id() -> bool:
    """Verify we're actually connected to Avalanche C-Chain."""
    try:
        resp = rpc_request({
            "jsonrpc": "2.0",
            "method": "eth_chainId",
            "params": [],
            "id": 1,
        })
        chain_id = int(resp.get("result", "0x0"), 16)
        return chain_id == CHAIN_ID
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def print_results(results: list[dict], usdc: dict, verbose: bool = False) -> int:
    """Print verification results in human-readable format. Returns exit code."""
    print()
    print("Vaultfire Protocol — Avalanche C-Chain Contract Verification")
    print(f"Chain ID: {CHAIN_ID}")
    print(f"RPC: {_active_rpc}")
    print("=" * 60)
    print()

    passed = 0
    failed = 0

    print(f"Checking {len(results)} Vaultfire contracts...")
    print()

    for r in results:
        status = "✓" if r["deployed"] else "✗"
        short = _short_address(r["address"])

        if verbose:
            bytecode_info = f"  bytecode: {r['bytecode_chars']:,} chars"
        else:
            bytecode_info = ""

        if r["deployed"]:
            print(f"  {status} {r['name']:<40s} {short}{bytecode_info}")
            passed += 1
        else:
            print(f"  {status} {r['name']:<40s} {short}  NOT FOUND")
            failed += 1

    # USDC check
    print()
    print("Additional:")
    usdc_status = "✓" if usdc["deployed"] else "✗"
    usdc_short = _short_address(usdc["address"])
    print(f"  {usdc_status} {usdc['name']:<40s} {usdc_short}")

    print()
    print("-" * 60)

    total = len(results)
    if failed == 0:
        print(f"Result: {passed}/{total} contracts verified ✓")
        if usdc["deployed"]:
            print("USDC (Native Circle) verified ✓")
        print()
        print("All Vaultfire contracts are deployed on Avalanche C-Chain.")
        print(f"Explorer: https://snowtrace.io")
        return 0
    else:
        print(f"Result: {passed}/{total} verified, {failed} MISSING")
        return 1


def print_json(results: list[dict], usdc: dict) -> int:
    """Print verification results as JSON. Returns exit code."""
    failed = sum(1 for r in results if not r["deployed"])
    output = {
        "chain": "avalanche",
        "chain_id": CHAIN_ID,
        "rpc": _active_rpc,
        "contracts": results,
        "usdc": usdc,
        "total": len(results),
        "verified": len(results) - failed,
        "missing": failed,
        "all_verified": failed == 0,
    }
    print(json.dumps(output, indent=2))
    return 0 if failed == 0 else 1


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    parser = argparse.ArgumentParser(
        description="Verify Vaultfire Protocol contracts on Avalanche C-Chain",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Output results as JSON",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show bytecode sizes",
    )
    return parser


def main() -> int:
    """Main entry point."""
    parser = build_parser()
    args = parser.parse_args()

    # Verify chain connection
    if not verify_chain_id():
        if args.as_json:
            print(json.dumps({"error": "Could not connect to Avalanche C-Chain RPC"}, indent=2))
        else:
            print("Error: Could not connect to Avalanche C-Chain RPC")
            print(f"Tried: {', '.join(_RPC_FALLBACKS)}")
        return 1

    # Verify all contracts
    results = verify_all_contracts(verbose=args.verbose)
    usdc = verify_usdc()

    if args.as_json:
        return print_json(results, usdc)
    else:
        return print_results(results, usdc, verbose=args.verbose)


if __name__ == "__main__":
    sys.exit(main())
