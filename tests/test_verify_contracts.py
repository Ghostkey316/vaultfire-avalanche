#!/usr/bin/env python3
"""
Unit tests for verify_contracts.py — Vaultfire Avalanche contract verification.

Tests cover:
  - Contract map integrity (addresses, uniqueness, completeness)
  - RPC configuration
  - Description map coverage
  - Helper functions
  - CLI parser

Run:
    python -m pytest tests/test_verify_contracts.py -v
    # or
    python tests/test_verify_contracts.py
"""

import os
import sys
import unittest

# Ensure project root is on sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "scripts"))

from verify_contracts import (
    CONTRACTS,
    DESCRIPTIONS,
    USDC_ADDRESS,
    CHAIN_ID,
    SNOWTRACE_BASE,
    _RPC_FALLBACKS,
    _short_address,
    build_parser,
)


# ---------------------------------------------------------------------------
# Contract map integrity
# ---------------------------------------------------------------------------

class TestContractMap(unittest.TestCase):
    """Tests for the CONTRACTS dictionary."""

    def test_all_addresses_valid_hex(self):
        """Every address must be a valid 42-char hex string with 0x prefix."""
        for name, addr in CONTRACTS.items():
            with self.subTest(contract=name):
                self.assertTrue(addr.startswith("0x"), f"{name}: missing 0x prefix")
                self.assertEqual(len(addr), 42, f"{name}: wrong length {len(addr)}")
                int(addr, 16)  # Should not raise ValueError

    def test_no_duplicate_addresses(self):
        """No two contracts should share the same address."""
        addrs = [a.lower() for a in CONTRACTS.values()]
        self.assertEqual(len(addrs), len(set(addrs)), "Duplicate contract addresses found")

    def test_contract_count(self):
        """We should have exactly 15 contracts on Avalanche."""
        self.assertEqual(len(CONTRACTS), 15)

    def test_core_contracts_present(self):
        """Essential protocol contracts must exist in the map."""
        required = [
            "ERC8004IdentityRegistry",
            "ERC8004ReputationRegistry",
            "AIPartnershipBondsV2",
            "AIAccountabilityBondsV2",
            "MissionEnforcement",
            "AntiSurveillance",
            "PrivacyGuarantees",
            "DilithiumAttestor",
            "VaultfireTeleporterBridge",
        ]
        for name in required:
            self.assertIn(name, CONTRACTS, f"Missing required contract: {name}")

    def test_erc8004_suite_present(self):
        """All four ERC-8004 registries/adapters must be present."""
        erc8004 = [
            "ERC8004IdentityRegistry",
            "ERC8004ReputationRegistry",
            "ERC8004ValidationRegistry",
            "VaultfireERC8004Adapter",
        ]
        for name in erc8004:
            self.assertIn(name, CONTRACTS, f"Missing ERC-8004 contract: {name}")

    def test_bond_contracts_present(self):
        """Both bond contracts (the stars) must be present."""
        self.assertIn("AIPartnershipBondsV2", CONTRACTS)
        self.assertIn("AIAccountabilityBondsV2", CONTRACTS)

    def test_security_layer_present(self):
        """Security/governance contracts must be present."""
        security = [
            "DilithiumAttestor",
            "MultisigGovernance",
            "ProductionBeliefAttestationVerifier",
            "BeliefAttestationVerifier",
            "MissionEnforcement",
            "AntiSurveillance",
            "PrivacyGuarantees",
        ]
        for name in security:
            self.assertIn(name, CONTRACTS, f"Missing security contract: {name}")

    def test_addresses_match_main_repo(self):
        """Spot-check key addresses against the main Vaultfire repo README values."""
        expected = {
            "ERC8004IdentityRegistry": "0x57741F4116925341d8f7Eb3F381d98e07C73B4a3",
            "AIPartnershipBondsV2":    "0xDC8447c66fE9D9c7D54607A98346A15324b7985D",
            "AIAccountabilityBondsV2":  "0x376831fB2457E34559891c32bEb61c442053C066",
            "MissionEnforcement":       "0xcf64D815F5424B7937aB226bC733Ed35ab6CaDcB",
            "DilithiumAttestor":        "0x211554bd46e3D4e064b51a31F61927ae9c7bCF1f",
            "VaultfireTeleporterBridge": "0x0dF0523aF5aF2Aef180dB052b669Bea97fee3d31",
        }
        for name, addr in expected.items():
            with self.subTest(contract=name):
                self.assertEqual(
                    CONTRACTS[name].lower(),
                    addr.lower(),
                    f"Address mismatch for {name}",
                )


# ---------------------------------------------------------------------------
# Description map
# ---------------------------------------------------------------------------

class TestDescriptions(unittest.TestCase):
    """Tests for the DESCRIPTIONS dictionary."""

    def test_every_contract_has_description(self):
        """Every contract in CONTRACTS should have a matching description."""
        for name in CONTRACTS:
            self.assertIn(name, DESCRIPTIONS, f"Missing description for {name}")

    def test_descriptions_not_empty(self):
        """No description should be an empty string."""
        for name, desc in DESCRIPTIONS.items():
            with self.subTest(contract=name):
                self.assertTrue(len(desc.strip()) > 0, f"Empty description for {name}")


# ---------------------------------------------------------------------------
# USDC
# ---------------------------------------------------------------------------

class TestUSDC(unittest.TestCase):
    """Tests for the USDC address constant."""

    def test_usdc_address_valid(self):
        """USDC address must be valid hex."""
        self.assertTrue(USDC_ADDRESS.startswith("0x"))
        self.assertEqual(len(USDC_ADDRESS), 42)
        int(USDC_ADDRESS, 16)

    def test_usdc_is_native_circle(self):
        """Verify this is the native Circle USDC on Avalanche, not bridged USDC.e."""
        self.assertEqual(
            USDC_ADDRESS.lower(),
            "0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e",
        )


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

class TestConfig(unittest.TestCase):
    """Tests for configuration constants."""

    def test_chain_id(self):
        """Avalanche C-Chain ID must be 43114."""
        self.assertEqual(CHAIN_ID, 43114)

    def test_rpc_fallbacks_not_empty(self):
        self.assertGreater(len(_RPC_FALLBACKS), 0)

    def test_rpc_fallbacks_are_https(self):
        for url in _RPC_FALLBACKS:
            self.assertTrue(url.startswith("https://"), f"Non-HTTPS RPC: {url}")

    def test_snowtrace_base_url(self):
        self.assertEqual(SNOWTRACE_BASE, "https://snowtrace.io/address/")


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

class TestShortAddress(unittest.TestCase):
    """Tests for _short_address formatting."""

    def test_with_prefix(self):
        result = _short_address("0x57741F4116925341d8f7Eb3F381d98e07C73B4a3")
        self.assertEqual(result, "0x5774...B4a3")

    def test_without_prefix(self):
        result = _short_address("57741F4116925341d8f7Eb3F381d98e07C73B4a3")
        self.assertEqual(result, "0x5774...B4a3")


# ---------------------------------------------------------------------------
# CLI parser
# ---------------------------------------------------------------------------

class TestCLIParser(unittest.TestCase):
    """Tests for argparse CLI structure."""

    def setUp(self):
        self.parser = build_parser()

    def test_default_flags(self):
        args = self.parser.parse_args([])
        self.assertFalse(args.as_json)
        self.assertFalse(args.verbose)

    def test_json_flag(self):
        args = self.parser.parse_args(["--json"])
        self.assertTrue(args.as_json)

    def test_verbose_flag(self):
        args = self.parser.parse_args(["--verbose"])
        self.assertTrue(args.verbose)

    def test_verbose_short(self):
        args = self.parser.parse_args(["-v"])
        self.assertTrue(args.verbose)

    def test_both_flags(self):
        args = self.parser.parse_args(["--json", "--verbose"])
        self.assertTrue(args.as_json)
        self.assertTrue(args.verbose)


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()
