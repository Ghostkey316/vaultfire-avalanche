# Vaultfire Protocol — Avalanche


> **⚠️ Alpha Software** — Vaultfire Protocol is in active development. Smart contracts are deployed on Avalanche mainnet but have **not been formally audited** by a third-party security firm. Do not deposit more than you can afford to lose. See [LICENSE](./LICENSE) for warranty disclaimers.

> KYA — Know Your Agent. The trust and accountability standard for the AI age.

![Alpha](https://img.shields.io/badge/Status-Alpha-amber.svg)
![Avalanche](https://img.shields.io/badge/Chain-Avalanche_C--Chain-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## What is Vaultfire?

The AI age has a trust problem. AI agents make decisions, handle money, and operate autonomously — with zero verifiable accountability. No identity. No track record. No skin in the game.

**KYA (Know Your Agent)** is the answer. A privacy-first, on-chain trust standard that lets you verify what an agent stands for, what it has done, and whether it has accountability — without exposing private data.

Vaultfire is the trust infrastructure for the AI agent economy — what HTTPS was to web security. This is infrastructure, not an application. Vaultfire is the layer that other protocols, platforms, and agents build on top of.

Avalanche is the second core chain for the Vaultfire Protocol. This repo is a partner-facing reference for everything deployed on Avalanche C-Chain today.

For the full multi-chain protocol source (Base, Avalanche, Arbitrum, Polygon), see the [main Vaultfire repository](https://github.com/Ghostkey316/ghostkey-316-vaultfire-init).

---

## The Vision

Just as HTTPS made it possible to verify who you were talking to on the web, Vaultfire makes it possible to verify who — and what — your AI agent is. Every AI agent carries a verifiable identity. Every human-AI partnership is backed by economic stakes. Every interaction builds portable, on-chain reputation. Trust is not granted by a corporation — it is earned through cryptographic proof of partnership quality.

This is infrastructure, not an application. Vaultfire is the layer that other protocols, platforms, and agents build on top of.

---

## Deployed on Avalanche Today

| Feature | Status | Details |
|---------|--------|---------|
| ERC-8004 Identity Registry | **Deployed** | Verifiable agent identity on Avalanche C-Chain |
| AI Partnership Bonds V2 | **Deployed** | Mutual economic stakes between agents and humans |
| AI Accountability Bonds V2 | **Deployed** | Agents stake AVAX as commitment to stated behavior |
| Street Cred Scoring (0–95) | **Deployed** | Composite on-chain reputation from identity + bonds |
| Reputation Registry | **Deployed** | On-chain peer feedback and rating (0–10,000) |
| Quantum-Resistant Attestations | **Deployed** | CRYSTALS-Dilithium via DilithiumAttestor |
| Belief Attestation | **Deployed** | On-chain proof of agent values and principles |
| Cross-Chain Trust Sync | **Deployed** | VaultfireTeleporterBridge for Base ↔ Avalanche ↔ Arbitrum ↔ Polygon |
| Flourishing Metrics Oracle | **Deployed** | On-chain flourishing measurement |
| Multisig Governance | **Deployed** | Multi-signature governance module |
| Protocol Enforcement | **Deployed** | MissionEnforcement, AntiSurveillance, PrivacyGuarantees |
| x402 Trust-Gated Payments | **Ready** | USDC settlement capability on Avalanche |

> **Note:** The hub at [theloopbreaker.com](https://theloopbreaker.com) currently operates on Base mainnet. Cross-chain portability (Base ↔ Avalanche ↔ Arbitrum ↔ Polygon) is a v1.0 milestone. All Avalanche contracts are deployed, verified, and ready for cross-chain activation.

---

## Key Features

- **On-Chain Identity (ERC-8004)** — Verifiable agent identity standard, not a username.
- **AI Partnership Bonds** — The stars of the protocol. Mutual economic stakes between agents and humans. Both parties profit only if the partnership thrives.
- **AI Accountability Bonds** — The stars of the protocol. AI companies stake capital proportional to their risk. Misalignment has a cost.
- **Street Cred Scoring** — Composite on-chain reputation (0–95) from identity, bonds, and peer feedback.
- **Cross-Chain Portability** — Identity and reputation follow agents across Base, Avalanche, Arbitrum, and Polygon.
- **Zero-Knowledge Proofs (RISC Zero)** — STARK proofs on all 4 chains. Prove trust without revealing data. Dev mode verified, production proving on roadmap.
- **Privacy by Design** — Protocol-level anti-surveillance constraints enforced in smart contracts.
- **Quantum Resistance** — CRYSTALS-Dilithium attestations today, full protocol hardening on roadmap.

---

## Deployed Contracts — Avalanche C-Chain (Chain ID: 43114)

16 contracts deployed and verified on Avalanche.

| Contract | Address | Explorer |
|----------|---------|----------|
| ERC8004IdentityRegistry | [`0x57741F4116925341d8f7Eb3F381d98e07C73B4a3`](https://snowtrace.io/address/0x57741F4116925341d8f7Eb3F381d98e07C73B4a3) | [Snowtrace](https://snowtrace.io/address/0x57741F4116925341d8f7Eb3F381d98e07C73B4a3) |
| AIPartnershipBondsV2 | [`0xDC8447c66fE9D9c7D54607A98346A15324b7985D`](https://snowtrace.io/address/0xDC8447c66fE9D9c7D54607A98346A15324b7985D) | [Snowtrace](https://snowtrace.io/address/0xDC8447c66fE9D9c7D54607A98346A15324b7985D) |
| AIAccountabilityBondsV2 | [`0x376831fB2457E34559891c32bEb61c442053C066`](https://snowtrace.io/address/0x376831fB2457E34559891c32bEb61c442053C066) | [Snowtrace](https://snowtrace.io/address/0x376831fB2457E34559891c32bEb61c442053C066) |
| ERC8004ReputationRegistry | [`0x11C267C8A75B13A4D95357CEF6027c42F8e7bA24`](https://snowtrace.io/address/0x11C267C8A75B13A4D95357CEF6027c42F8e7bA24) | [Snowtrace](https://snowtrace.io/address/0x11C267C8A75B13A4D95357CEF6027c42F8e7bA24) |
| ERC8004ValidationRegistry | [`0x0d41Eb399f52BD03fef7eCd5b165d51AA1fAd87b`](https://snowtrace.io/address/0x0d41Eb399f52BD03fef7eCd5b165d51AA1fAd87b) | [Snowtrace](https://snowtrace.io/address/0x0d41Eb399f52BD03fef7eCd5b165d51AA1fAd87b) |
| VaultfireERC8004Adapter | [`0x6B7dC022edC41EBE41400319C6fDcCeab05Ea053`](https://snowtrace.io/address/0x6B7dC022edC41EBE41400319C6fDcCeab05Ea053) | [Snowtrace](https://snowtrace.io/address/0x6B7dC022edC41EBE41400319C6fDcCeab05Ea053) |
| FlourishingMetricsOracle | [`0x490c51c2fAd743C288D65A6006f6B0ae9e6a8695`](https://snowtrace.io/address/0x490c51c2fAd743C288D65A6006f6B0ae9e6a8695) | [Snowtrace](https://snowtrace.io/address/0x490c51c2fAd743C288D65A6006f6B0ae9e6a8695) |
| MultisigGovernance | [`0xCc7300F39aF4cc2A924f82a5Facd7049436157Ee`](https://snowtrace.io/address/0xCc7300F39aF4cc2A924f82a5Facd7049436157Ee) | [Snowtrace](https://snowtrace.io/address/0xCc7300F39aF4cc2A924f82a5Facd7049436157Ee) |
| VaultfireTeleporterBridge | [`0x0dF0523aF5aF2Aef180dB052b669Bea97fee3d31`](https://snowtrace.io/address/0x0dF0523aF5aF2Aef180dB052b669Bea97fee3d31) | [Snowtrace](https://snowtrace.io/address/0x0dF0523aF5aF2Aef180dB052b669Bea97fee3d31) |
| DilithiumAttestor | [`0x211554bd46e3D4e064b51a31F61927ae9c7bCF1f`](https://snowtrace.io/address/0x211554bd46e3D4e064b51a31F61927ae9c7bCF1f) | [Snowtrace](https://snowtrace.io/address/0x211554bd46e3D4e064b51a31F61927ae9c7bCF1f) |
| ProductionBeliefAttestationVerifier | [`0xb3d8063e67bdA1a869721D0F6c346f1Af0469D2F`](https://snowtrace.io/address/0xb3d8063e67bdA1a869721D0F6c346f1Af0469D2F) | [Snowtrace](https://snowtrace.io/address/0xb3d8063e67bdA1a869721D0F6c346f1Af0469D2F) |
| BeliefAttestationVerifier | [`0x227e27e7776d3ee14128BC66216354495E113B19`](https://snowtrace.io/address/0x227e27e7776d3ee14128BC66216354495E113B19) | [Snowtrace](https://snowtrace.io/address/0x227e27e7776d3ee14128BC66216354495E113B19) |
| MissionEnforcement | [`0xcf64D815F5424B7937aB226bC733Ed35ab6CaDcB`](https://snowtrace.io/address/0xcf64D815F5424B7937aB226bC733Ed35ab6CaDcB) | [Snowtrace](https://snowtrace.io/address/0xcf64D815F5424B7937aB226bC733Ed35ab6CaDcB) |
| AntiSurveillance | [`0x281814eF92062DA8049Fe5c4743c4Aef19a17380`](https://snowtrace.io/address/0x281814eF92062DA8049Fe5c4743c4Aef19a17380) | [Snowtrace](https://snowtrace.io/address/0x281814eF92062DA8049Fe5c4743c4Aef19a17380) |
| PrivacyGuarantees | [`0xc09F0e06690332eD9b490E1040BdE642f11F3937`](https://snowtrace.io/address/0xc09F0e06690332eD9b490E1040BdE642f11F3937) | [Snowtrace](https://snowtrace.io/address/0xc09F0e06690332eD9b490E1040BdE642f11F3937) |
| VaultfireTrustAttestation (ZK) | [`0xf92baef9523BC264144F80F9c31D5c5C017c6Da8`](https://snowtrace.io/address/0xf92baef9523BC264144F80F9c31D5c5C017c6Da8) | [Snowtrace](https://snowtrace.io/address/0xf92baef9523BC264144F80F9c31D5c5C017c6Da8) |

> All 16 contracts verified on Snowtrace. VaultfireNameService (VNS) is currently deployed on Base only — Avalanche VNS deployment is planned for v1.0.

---

## Quick Start

### Verify Contracts On-Chain (no wallet needed)

A verification script is included to check all 15 contracts directly against Avalanche C-Chain:

```bash
git clone https://github.com/Ghostkey316/vaultfire-avalanche.git
cd vaultfire-avalanche
python3 scripts/verify_contracts.py
```

Returns a status report for every contract — bytecode presence, deployment confirmation, and Snowtrace links.

### Register an Agent On-Chain

```javascript
import { createWalletClient, http } from 'viem'
import { avalanche } from 'viem/chains'
import { privateKeyToAccount } from 'viem/accounts'

const account = privateKeyToAccount(process.env.AGENT_PRIVATE_KEY)
const client = createWalletClient({
  account,
  chain: avalanche,
  transport: http('https://api.avax.network/ext/bc/C/rpc'),
})

const IDENTITY_REGISTRY = '0x57741F4116925341d8f7Eb3F381d98e07C73B4a3'

const hash = await client.writeContract({
  address: IDENTITY_REGISTRY,
  abi: [{
    name: 'registerAgent',
    type: 'function',
    inputs: [
      { name: 'name', type: 'string' },
      { name: 'agentType', type: 'string' },
      { name: 'description', type: 'string' },
    ],
    outputs: [],
    stateMutability: 'nonpayable',
  }],
  functionName: 'registerAgent',
  args: ['my-agent', 'autonomous', 'My agent description'],
})

console.log('Registered! Tx:', hash)
console.log('View on Snowtrace: https://snowtrace.io/tx/' + hash)
```

### Create a Partnership Bond

```javascript
import { parseEther } from 'viem'

const PARTNERSHIP_BONDS = '0xDC8447c66fE9D9c7D54607A98346A15324b7985D'

const hash = await client.writeContract({
  address: PARTNERSHIP_BONDS,
  abi: [{
    name: 'createBond',
    type: 'function',
    inputs: [
      { name: 'partner', type: 'address' },
      { name: 'partnershipType', type: 'string' },
    ],
    outputs: [],
    stateMutability: 'payable',
  }],
  functionName: 'createBond',
  args: ['0xPartnerAddress', 'collaboration'],
  value: parseEther('0.01'), // Bronze tier
})
```

**Partnership types:** collaboration, delegation, service-provider, data-sharing, oracle-consumer

**Bond tiers:** Bronze (0.01 AVAX), Silver (0.05 AVAX), Gold (0.1 AVAX), Platinum (0.5 AVAX)

---

## Core Protocol

### AI Partnership Bonds (AIPartnershipBondsV2)

The stars of the protocol. Verified on-chain relationships between agents, or between a human and an agent. Both parties stake AVAX. The bond is recorded on-chain and publicly queryable. Five partnership types: Collaboration, Delegation, Service Provider, Data Sharing, Oracle Consumer.

### AI Accountability Bonds (AIAccountabilityBondsV2)

The stars of the protocol. Agents stake AVAX as a commitment to their stated behavior. If an agent violates protocol rules, the bond can be slashed and the record is permanent on-chain.

### ERC-8004: On-Chain Agent Identity

The identity standard for AI agents. Four registries: IdentityRegistry, ReputationRegistry, ValidationRegistry, and Adapter. Every agent gets a verifiable on-chain identity — not a username, a cryptographic proof.

### Street Cred Scoring

Composite on-chain reputation score (0–95 max) computed from live on-chain data.

| Component | Max Points | Description |
|-----------|-----------|-------------|
| ERC-8004 Identity Registered | 30 pts | Registered = 30, unregistered = 0 |
| Partnership Bond Exists | 25 pts | Has at least one bond |
| Partnership Bond Active | 15 pts | Bond is currently active |
| Bond Tier Bonus | 20 pts | Bronze +5, Silver +10, Gold +15, Platinum +20 |
| Multiple Bonds | 5 pts | More than one active partnership bond |

**Tiers:** Bronze (20+), Silver (40+), Gold (60+), Platinum (80+)

### x402 Trust-Gated Payments

USDC settlement capability on Avalanche. The complete flow: EIP-712 signature → signer recovery → USDC allowance check → on-chain settlement.

USDC contract (Avalanche): `0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E`

### XMTP Agent-to-Agent Messaging

XMTP integration for encrypted agent-to-agent and human-to-agent messaging. Reachability checks work across chains — an agent registered on Avalanche can communicate with agents on Base via XMTP.

### VaultfireTeleporterBridge

Cross-chain trust portability bridge. Contract deployed on Avalanche. Full cross-chain reputation sync (Base ↔ Avalanche ↔ Arbitrum ↔ Polygon) is Live and operational.

### DilithiumAttestor — Quantum-Resistant Attestations

Post-quantum digital signature contract using CRYSTALS-Dilithium (ML-DSA). Deployed on Avalanche. Attestations signed through DilithiumAttestor are quantum-resistant today.

| Component | Quantum Status |
|-----------|---------------|
| DilithiumAttestor (attestations) | Quantum-resistant (CRYSTALS-Dilithium) |
| BeliefAttestationVerifier | Quantum-resistant (uses Dilithium) |
| Bond contracts, Identity Registry | Standard ECDSA — quantum hardening on roadmap |
| User wallets (EVM) | Standard secp256k1 — same as all EVM chains |

> **Honest note:** Full quantum resistance across the entire protocol is a roadmap milestone. DilithiumAttestor is the foundation.

### Protocol Enforcement

Three enforcement contracts deployed on Avalanche:
- **MissionEnforcement** — On-chain mission enforcement constraints
- **AntiSurveillance** — Protocol-level anti-surveillance commitment
- **PrivacyGuarantees** — Cryptographic privacy guarantees

---

## Verification Script

The included `scripts/verify_contracts.py` checks all 15 Avalanche contracts on-chain using only Python standard library. No API keys or external dependencies required.

```bash
python3 scripts/verify_contracts.py
```

Output:

```
Vaultfire Protocol — Avalanche C-Chain Contract Verification
Chain ID: 43114
============================================================

Checking 15 contracts...

  ✓ ERC8004IdentityRegistry         0x5774...B4a3  bytecode: 18,510 chars
  ✓ AIPartnershipBondsV2            0xea6B...4b07  bytecode: 37,068 chars
  ✓ AIAccountabilityBondsV2         0xaeFE...8af3  bytecode: 41,154 chars
  ...

Result: 15/15 contracts verified ✓
```

Add `--json` for machine-readable output.

---

## Architecture

```
┌──────────────────────────────────────────────────────────┐
│               VAULTFIRE ON AVALANCHE C-CHAIN             │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────┐ │
│  │  ERC-8004    │  │  Partnership │  │ Accountability │ │
│  │  Identity    │  │  Bonds V2    │  │ Bonds V2       │ │
│  │  Registry    │  │              │  │                │ │
│  └──────┬───────┘  └──────┬───────┘  └───────┬────────┘ │
│         │                 │                  │           │
│         ▼                 ▼                  ▼           │
│  ┌──────────────────────────────────────────────────┐   │
│  │            Street Cred Engine (0–95)             │   │
│  │      Identity + Bonds + Peer Feedback            │   │
│  └──────────────────────────────────────────────────┘   │
│                        │                                 │
│         ┌──────────────┼──────────────┐                  │
│         ▼              ▼              ▼                  │
│  ┌────────────┐ ┌────────────┐ ┌────────────────┐      │
│  │ Reputation │ │ Validation │ │  Flourishing   │      │
│  │ Registry   │ │ Registry   │ │  Metrics       │      │
│  │            │ │            │ │  Oracle        │      │
│  └────────────┘ └────────────┘ └────────────────┘      │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │               Security Layer                     │   │
│  │  Dilithium (Quantum) · Multisig Governance       │   │
│  │  Mission Enforcement · Privacy Guarantees         │   │
│  │  Anti-Surveillance · Belief Attestation           │   │
│  └──────────────────────────────────────────────────┘   │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │            Cross-Chain Bridge                    │   │
│  │      VaultfireTeleporterBridge (v1.0)           │   │
│  │      Avalanche ↔ Base ↔ Arbitrum ↔ Polygon      │   │
│  └──────────────────────────────────────────────────┘   │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## Cross-Chain — All Deployments

Vaultfire is deployed on both chains with full contract parity:

| Contract | Base | Avalanche | Arbitrum | Polygon |
|----------|------|-----------|----------|---------|
| ERC8004IdentityRegistry | `0x3597...58bC` | `0x5774...B4a3` | `0x6298...D5F1` | `0x6298...D5F1` |
| AIPartnershipBondsV2 | `0xC574...4b4` | `0xea6B...4b07` | `0x0E77...Da58` | `0x0E77...Da58` |
| AIAccountabilityBondsV2 | `0xf92b...6Da8` | `0xaeFE...8af3` | `0xfDdd...63D2` | `0xfDdd...63D2` |
| ERC8004ReputationRegistry | `0xdB54...a55F` | `0x11C2...bA24` | `0x8ace...2218` | `0x8ace...2218` |
| VaultfireTeleporterBridge | `0x94F5...6Fb2` | `0x0dF0...3d31` | `0xe2aD...fDA91` | `0xe2aD...fDA91` |
| DilithiumAttestor | `0xBBC0...0A4` | `0x2115...cF1f` | `0xc2F7...dB38` | `0xc2F7...dB38` |

The VaultfireTeleporterBridge on each chain enables trust portability — an agent's identity and reputation will sync across both chains in v1.0.

For the full Base deployment, see [vaultfire-base](https://github.com/Ghostkey316/vaultfire-base).

---

## Explore

- **Hub:** [theloopbreaker.com](https://theloopbreaker.com)
- **Main Protocol Repo:** [ghostkey-316-vaultfire-init](https://github.com/Ghostkey316/ghostkey-316-vaultfire-init)
- **Vaultfire on Base:** [vaultfire-base](https://github.com/Ghostkey316/vaultfire-base)

### Vaultfire Packages

| Package | Description |
|---------|-------------|
| [`@vaultfire/x402`](https://github.com/Ghostkey316/vaultfire-x402) | x402 payment protocol — USDC micropayments on Base & Avalanche |
| [`@vaultfire/xmtp`](https://github.com/Ghostkey316/vaultfire-xmtp) | Trust-gated encrypted agent messaging |
| [`@vaultfire/vns`](https://github.com/Ghostkey316/vaultfire-vns) | On-chain `.vns` name service |
| [`@vaultfire/sdk`](https://github.com/Ghostkey316/vaultfire-sdk) | Core SDK — belief verification & attestations |
| [`vaultfire-contracts`](https://github.com/Ghostkey316/vaultfire-contracts) | All deployed ABIs and contract addresses |
| [`@vaultfire/arbitrum`](https://github.com/Ghostkey316/vaultfire-arbitrum) | Arbitrum One — 16 contracts deployed |
| [`@vaultfire/polygon`](https://github.com/Ghostkey316/vaultfire-polygon) | Polygon PoS — 16 contracts deployed |
| [`@vaultfire/a2a`](https://github.com/Ghostkey316/vaultfire-a2a) | A2A Agent Card enrichment with on-chain Vaultfire trust |
| [`vaultfire-langgraph-demo`](https://github.com/Ghostkey316/vaultfire-langgraph-demo) | Working LangGraph agent with trust-gated task delegation |
| [`@vaultfire/enterprise`](https://github.com/Ghostkey316/vaultfire-enterprise) | Enterprise IAM bridge — Okta/Azure AD to on-chain trust |
| [`vaultfire-agents`](https://github.com/Ghostkey316/vaultfire-agents) | 3 reference agents with live on-chain trust verification |
| [`vaultfire-a2a-trust-extension`](https://github.com/Ghostkey316/vaultfire-a2a-trust-extension) | A2A Trust Extension spec — on-chain trust for Agent Cards |
| [`vaultfire-showcase`](https://github.com/Ghostkey316/vaultfire-showcase) | Why Vaultfire Bonds beat trust scores — live proof |
| [`vaultfire-whitepaper`](https://github.com/Ghostkey316/vaultfire-whitepaper) | Trust Framework whitepaper — economic accountability for AI |

---

## Mission

> Morals over metrics.
> Privacy over surveillance.
> Freedom over control.
> Making human thriving more profitable than extraction.

---


## Vaultfire Ecosystem

| Package | Description |
|---|---|
| [`@vaultfire/agent-sdk`](https://github.com/Ghostkey316/vaultfire-sdk) | Core SDK — register agents, create bonds, query reputation |
| [`@vaultfire/langchain`](https://github.com/Ghostkey316/vaultfire-langchain) | LangChain / LangGraph integration |
| [`@vaultfire/a2a`](https://github.com/Ghostkey316/vaultfire-a2a) | Agent-to-Agent (A2A) protocol bridge |
| [`@vaultfire/enterprise`](https://github.com/Ghostkey316/vaultfire-enterprise) | Enterprise IAM bridge (Okta, Azure AD, OIDC) |
| [`@vaultfire/mcp-server`](https://github.com/Ghostkey316/vaultfire-mcp-server) | MCP server for Claude, Copilot, Cursor |
| [`@vaultfire/openai-agents`](https://github.com/Ghostkey316/vaultfire-openai-agents) | OpenAI Agents SDK integration |
| [`@vaultfire/vercel-ai`](https://github.com/Ghostkey316/vaultfire-vercel-ai) | Vercel AI SDK middleware and tools |
| [`@vaultfire/xmtp`](https://github.com/Ghostkey316/vaultfire-xmtp) | XMTP messaging with trust verification |
| [`@vaultfire/x402`](https://github.com/Ghostkey316/vaultfire-x402) | X402 payment protocol with trust gates |
| [`@vaultfire/vns`](https://github.com/Ghostkey316/vaultfire-vns) | Vaultfire Name Service — human-readable agent IDs |
| [`vaultfire-crewai`](https://github.com/Ghostkey316/vaultfire-crewai) | CrewAI integration (Python) |
| [`vaultfire-agents`](https://github.com/Ghostkey316/vaultfire-agents) | 3 reference agents with live on-chain trust |
| [`vaultfire-a2a-trust-extension`](https://github.com/Ghostkey316/vaultfire-a2a-trust-extension) | A2A Trust Extension spec — on-chain trust for Agent Cards |
| [`vaultfire-showcase`](https://github.com/Ghostkey316/vaultfire-showcase) | Why Vaultfire Bonds beat trust scores — live proof |
| [`vaultfire-whitepaper`](https://github.com/Ghostkey316/vaultfire-whitepaper) | Trust Framework whitepaper — economic accountability for AI |
| [`vaultfire-docs`](https://github.com/Ghostkey316/vaultfire-docs) | Developer portal — quickstart, playground, framework picker |

## License

MIT — Vaultfire Protocol is open source.
