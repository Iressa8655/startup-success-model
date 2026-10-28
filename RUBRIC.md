# Deck scoring rubric

Three pillars, 16 sub-criteria, each scored 1 to 5. The criteria come from the essay [How venture capital actually works, §7](https://iressa8655.github.io/digital-garden/Ventures/How-venture-capital-actually-works#7-what-to-show-me-if-you-are-a-founder).

Every sub-score also carries a status.

- **verified** means a human checked it against an independent record.
- **claimed** means it rests only on the deck. The score is pulled halfway towards 3.
- **contradicted** means the check failed. The score becomes 1.

## Pillar 1, outlier team

| Key | Sub-criterion | 1 | 3 | 5 | Evidence |
|---|---|---|---|---|---|
| T1 | Mastery on the axis the company is hard at (scientific, distribution or infrastructure) | Wrong axis or none | Strong, not exceptional | Exceptional on exactly that axis | Matches the core risk to T2–T4 |
| T2 | Research record | No papers | Papers as a middle author | Lead author in top venues, widely cited | OpenAlex, Google Scholar, ORCID |
| T3 | Engineering record | No public work | Contributor | Maintainer of a widely used project, or patents | GitHub commit history, patent databases |
| T4 | Operator record | None | Relevant roles | A verified exit, or hard systems scaled | Company registers, acquirer announcements |
| T5 | Founder-market fit | Generic "big market" pitch | Has done customer discovery | Lived the problem, can name past failures | Founder conversation |
| T6 | Someone builds the company (hires, sells, raises) | Nobody | Partly | Clearly owned by a founder | Team slide and conversation |

Red flags cap the team pillar at 2. These include a generic AI wrapper, a product whose only edge is a better interface, deep tech with no in-house engineering, and any contradicted claim.

## Pillar 2, upside

| Key | Sub-criterion | 1 | 3 | 5 |
|---|---|---|---|---|
| U1 | Bottom-up path to $100M ARR (customers × contract value) | Only a percentage of TAM | Bottom-up, with gaps | Closes, and the customers exist |
| U2 | Budget source | Competes for tool budget | Mixed | Captures labour budget or creates new revenue |
| U3 | Market shape | Incumbents absorb it | Unclear | One company can win most of it |
| U4 | Why now | Nothing changed | Plausible | A clear recent shift |
| U5 | Market ambition | Home country only, "expand later" | Vague international plan | Names a large market and what must be true to win it |
| U6 | Margin survives a competitor | No answer | Partial | Structural reason |

## Pillar 3, a moat that survives the next model

| Key | Sub-criterion | 1 | 3 | 5 |
|---|---|---|---|---|
| M1 | Proprietary data that deepens with use | None | Data others can buy | Every customer adds to it |
| M2 | Domain expertise embedded in the product | Generic | Some | Hard to hire, and built in |
| M3 | System complexity a general API cannot match | Thin wrapper or prompt layer | Some orchestration | Compound system |
| M4 | Model-release test | Killed by the next frontier model | Partly exposed | Improves as models improve |

## From scores to a recommendation

Each pillar score is the mean of its sub-scores, after the status adjustment.

| Rule | Recommendation |
|---|---|
| Every pillar ≥ 4 | Take meeting |
| Any pillar ≤ 2 | Pass |
| Otherwise | Maybe |

The thresholds and the discount for claimed scores are judgement calls, not fitted values, and they live in `src/rubric.json`. The tool only ever recommends whether to take a meeting. The investment decision stays with a person.
