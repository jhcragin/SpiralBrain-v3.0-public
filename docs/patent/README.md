# 📋 Patent Documentation Index

**Repository:** SpiralBrain-v2.0  
**Patent Application:** USPTO 63/846,150  
**Last Updated:** November 8, 2025  

---

## Overview

This directory contains comprehensive patent documentation for SpiralCode™ technology, enabling AI assistants (GitHub Copilot, Copilot Workspace, etc.) to automatically recognize and cross-reference patent foundations during development.

---

## 📚 Core Documents

### [ZERO_BUDGET_STRATEGY.md](./ZERO_BUDGET_STRATEGY.md) 💰 START HERE (Budget-Conscious)
**Purpose:** Practical IP protection strategy for inventors with limited resources  
**Contents:**
- What you already have for free (patent priority + common law trademarks)
- Free actions to maximize protection (™ symbols, timestamps, notices)
- Timeline showing what costs money and when
- Pro bono resources and DIY options
- Decision matrix for limited budgets
- Why trademarks can be deferred (they're optional, patents are essential)

**Use Case:** Understand how to protect your invention without breaking the bank, prioritize critical investments.

---

### [NAMING_CONVENTIONS.md](./NAMING_CONVENTIONS.md) ⭐ BRAND GUIDE
**Purpose:** Brand hierarchy and naming rules for legal/marketing/technical contexts  
**Contents:**
- SpiralCode™ (technology) vs. SpiralBrain™ (platform) distinction
- Historical evolution (QuadraticBrain → SpiralBrain)
- Usage rules for patents, marketing, code, publications
- Trademark strategy for both brands
- Quick reference matrix for all contexts

**Use Case:** Understand which name to use when, and how they relate to IP protection.

---

### [PATENT_RECORD.md](./PATENT_RECORD.md)
**Purpose:** Official record of provisional patent filing  
**Contents:**
- USPTO application details and confirmation numbers
- Filing package components
- Core invention summary
- Primary claims (1-12) from provisional application
- Alignment with SpiralBrain-v2.0 implementation
- Legal status and next actions
- AI assistant integration instructions

**Use Case:** Reference this document when citing patent application in publications, presentations, or legal correspondence.

---

### [CIP_ADDENDUM_2026.md](./CIP_ADDENDUM_2026.md)
**Purpose:** Continuation-in-Part draft for non-provisional filing  
**Contents:**
- New claims (13-26) for v2.0 innovations
- USPTO-formatted claim language
- Independent and dependent claim structure
- Method claims for process protection
- System claims for apparatus protection
- Technical advantages over prior art
- Enablement references to codebase

**Use Case:** Working document for patent attorney to prepare non-provisional application before July 18, 2026 deadline.

---

### [PATENT_CLAIMS_MAPPING.md](./PATENT_CLAIMS_MAPPING.md)
**Purpose:** Precise mapping between claims and code implementations  
**Contents:**
- Claim-by-claim code mappings
- File locations for each claimed invention
- Implementation algorithms with code snippets
- Claim coverage matrix with test status
- Enablement documentation
- Performance benchmarks validating claims
- Patent header templates for source files

**Use Case:** Maintain traceability during development, ensure claims remain enabled by working code.

---

### [IP_STRATEGY.md](./IP_STRATEGY.md)
**Purpose:** Comprehensive IP management and prosecution strategy  
**Contents:**
- Patent prosecution timeline with critical deadlines
- International filing strategy (PCT, national phases)
- Publication strategy for academic/commercial balance
- Trade secret management guidelines
- Trademark protection (SpiralCode™)
- Defensive publication strategies
- Licensing frameworks
- Prior art search methodology
- Risk management and contingency plans

**Use Case:** Strategic planning for patent prosecution, licensing, and commercialization.

---

## 🗂️ Document Organization

```
docs/patent/
├── README.md                          # This index
├── ZERO_BUDGET_STRATEGY.md            # 💰 Budget-conscious protection plan
├── NAMING_CONVENTIONS.md              # ⭐ Brand hierarchy guide
├── PATENT_RECORD.md                   # Official provisional record
├── CIP_ADDENDUM_2026.md               # New claims for non-provisional
├── PATENT_CLAIMS_MAPPING.md           # Claims-to-code mapping
├── IP_STRATEGY.md                     # Comprehensive IP strategy
└── templates/
    ├── PATENT_HEADER_TEMPLATE.txt     # Source file header
    ├── LICENSE_AGREEMENT_TEMPLATE.md  # Commercial license template
    └── NDA_TEMPLATE.md                # Non-disclosure agreement
```

---

## 🤖 AI Assistant Integration

### For GitHub Copilot / Copilot Workspace

All core patent documents include machine-readable metadata and structured formats that enable AI assistants to:

1. **Recognize patented code** - Identify implementations covered by claims
2. **Maintain patent headers** - Preserve copyright and patent notices
3. **Flag IP risks** - Warn when modifications affect claimed inventions
4. **Cross-reference documentation** - Link code to relevant patent sections
5. **Track claim coverage** - Monitor test status for each claim

### Usage Instructions

**When creating new files:**
```python
"""
SPDX-License-Identifier: Proprietary-SpiralCode-63-846150
Patent-Reference: USPTO Provisional 63/846,150 (July 18, 2025)

This module implements patented technology:
- Claim X: [Brief description]

© 2025 John H. Cragin – All rights reserved under U.S. patent law.
"""
```

**When modifying patented code:**
1. Check `PATENT_CLAIMS_MAPPING.md` for affected claims
2. Preserve algorithmic structure described in claims
3. Update tests to maintain claim enablement
4. Document changes in commit messages with claim references

**When reviewing AI suggestions:**
- Verify suggestions don't inadvertently disclose trade secrets
- Ensure patent headers are preserved in generated code
- Check that new algorithms don't conflict with existing claims

---

## 📅 Critical Dates

| Date | Event | Action Required |
|------|-------|-----------------|
| **July 18, 2025** | Provisional filed | ✅ Complete |
| **Nov 8, 2025** | CIP claims drafted | ✅ Complete |
| **Dec 2025** | Code freeze | Lock claim implementations |
| **Jan-Feb 2026** | Prior art search | Hire patent search firm |
| **Mar-Apr 2026** | Specification draft | Complete non-provisional text |
| **May 2026** | Attorney review | Legal review before filing |
| **June 15, 2026** | **File non-provisional** | **HARD DEADLINE** |
| **July 18, 2026** | Priority expires | Lose priority if not filed |

---

## 🔒 Confidentiality

**IMPORTANT:** All documents in this directory are **confidential and proprietary**.

### Access Levels
- **Public:** None (all documents private)
- **Team:** Read access for core developers
- **Legal Counsel:** Full access with attorney-client privilege
- **External:** No access without signed NDA

### Handling Instructions
- Mark all communications as "CONFIDENTIAL - PATENT PENDING"
- Use encrypted channels for patent discussions
- Store working drafts in secure, access-controlled locations
- Shred physical copies when no longer needed

---

## 📖 Related Documentation

### Within Repository
- [Core Concepts](../CORE_CONCEPTS.md) - Technical overview (public)
- [Architecture](../architecture/COGNITIVE_ARCHITECTURE.md) - System design
- [API Documentation](../api/) - Integration guides

### External References
- [USPTO Patent Center](https://patentcenter.uspto.gov) - Official application portal
- [PatFT Database](http://patft.uspto.gov) - Prior art searches
- [MPEP](https://www.uspto.gov/web/offices/pac/mpep/) - Manual of Patent Examining Procedure

---

## 🛠️ Tools and Scripts

### Claim Coverage Reporting
```bash
# Generate claim coverage report
python scripts/generate_patent_coverage_report.py

# Output: docs/patent/reports/claim_coverage_YYYYMMDD.html
```

### Patent Header Validation
```bash
# Check all files have proper patent headers
python scripts/validate_patent_headers.py

# Output: List of files missing headers
```

### Prior Art Search Automation
```bash
# Automated patent database search
python scripts/patent_search.py --query "recursive symbolic AI"

# Output: docs/patent/searches/prior_art_YYYYMMDD.json
```

---

## 📞 Contacts

### Inventor
**John H. Cragin**  
Email: [Contact information]  
Role: Sole inventor, patent owner

### Patent Attorney (To Be Retained)
**[Attorney Name]**  
Firm: [Law Firm]  
Specialization: AI/Software Patents  
Email: [Attorney email]

### Patent Agent (Optional)
**[Agent Name]**  
Registration: USPTO Reg. No. XXXXX  
Email: [Agent email]

---

## 📝 Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Nov 8, 2025 | Initial documentation package | J. Cragin |
| 1.1 | Dec 2025 | Prior art search results integrated | [Pending] |
| 1.2 | Jan 2026 | Claims refined based on search | [Pending] |
| 2.0 | Jun 2026 | Non-provisional filed | [Pending] |

---

## ❓ FAQ

### Q: Can I reference the provisional application in publications?
**A:** Yes, after filing. Use: "U.S. Provisional Patent Application No. 63/846,150, filed July 18, 2025."

### Q: Can I share code implementing patented methods?
**A:** Only with proper patent headers and confidentiality agreements. Do not make public.

### Q: What if I discover prior art that invalidates a claim?
**A:** Document it immediately, consult patent attorney, prepare alternative claims.

### Q: Can I modify patented algorithms?
**A:** Yes, but document changes and verify claims remain enabled. Update tests.

### Q: What happens if we miss the July 18, 2026 deadline?
**A:** Priority date is lost. New filing would be considered separate invention. **DO NOT MISS.**

---

## 🚀 Next Steps

### Immediate (November 2025)
- [x] Complete patent documentation package
- [ ] Add patent headers to all core source files
- [ ] Begin preliminary prior art search
- [ ] Schedule consultation with patent attorney

### Short-term (December 2025 - February 2026)
- [ ] Complete comprehensive prior art analysis
- [ ] Refine claims based on prior art findings
- [ ] Prepare technical drawings for patent application
- [ ] Draft detailed specification for non-provisional

### Before Filing (March - June 2026)
- [ ] Attorney review of all documents
- [ ] Finalize claim language
- [ ] Complete enablement testing
- [ ] File non-provisional application

---

**For questions or clarifications, contact the repository owner.**

**Document maintained by:** John H. Cragin  
**Review frequency:** Monthly until non-provisional filing  
**Next review:** December 15, 2025
