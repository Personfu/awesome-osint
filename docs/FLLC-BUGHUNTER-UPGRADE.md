# FLLC Bug Hunter Upgrade — awesome-osint

## Portfolio role

awesome-osint should become the **offensive OSINT source map** for PersonFu/FLLC: a curated, categorized, scored reference for bug bounty recon, exploit intelligence, infrastructure mapping, and exposure reduction.

## Offensive OSINT lanes

| Lane | Purpose | Output |
| --- | --- | --- |
| Domain / DNS | subdomains, DNS history, takeover candidates | asset graph, scope notes |
| Certificate Transparency | newly issued certs, staging/admin names | CT timeline, candidate targets |
| ASN / BGP | netblocks, hosting, routing context | infrastructure map |
| Code / Repo Exposure | leaked keys, endpoints, configs | redacted report |
| People / Org OSINT | public org context and contacts | escalation map, no doxxing |
| Cloud Exposure | buckets, apps, public endpoints | owned-scope checklist |
| CVE Mapping | products to vulnerabilities | exploit maturity note |
| Dark/Leak Mentions | public leak references | source-confidence brief |

## Data model target

```json
{
  "name": "Example Source",
  "category": "ct | dns | asn | code | cloud | cve | leak | people | geospatial",
  "access": "free | freemium | paid",
  "best_for": ["bug-bounty", "asset-discovery", "exploit-triage"],
  "risk": "low | medium | high",
  "requires_authorization": false,
  "notes": "short usage guidance"
}
```

## FLLC visual upgrade

Feed the `/mission-systems` page and future member dashboards with:

- source tiles;
- category filters;
- confidence badges;
- live/synthetic/source labels;
- graph connections from source → workflow → report.

## Content outputs

- Blog: “Offensive OSINT is an attack-surface map, not a link dump.”
- Short video: “Bug bounty recon starts with scope, CT logs, DNS, ASN, and code exposure.”
- Member lesson: “Build an offensive OSINT workflow without crossing scope.”
- Product card: `FLLC Offensive OSINT Atlas`.

## Professional rules

- Respect bug bounty scope.
- Do not publish personal data.
- Redact secrets immediately.
- Do not automate harassment, doxxing, stalking, or credential abuse.
- Keep third-party findings in reports, not public screenshots.
