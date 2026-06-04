# Git Status — Final IF/PAE Acceptance
**Date**: 2026-06-04 19:37:12

## Suggested commit message
```
protein-scout: complete IF/PAE mismatch repair and CRITICAL false-rejection recovery

- Repair 520 HPA IF false-absence: embed images, fix text
- Repair 23 PAE false-absence: embed images
- Reopen 10 CRITICAL nuclear<=3 false rejections
- Rescue 5 to scored: ALKBH2, ALKBH6, AKIRIN1, AIRIM, AKIP1
- Confirm 5 rejected: AFMID, DNM3, MKLN1, ANAPC13, NAF1
- All true data mismatches resolved
- Accept current state for delivery
```

## git status
```
 M ../../../.claudian/sessions/conv-1780213051054-6cms7w3g1.meta.json
 M detail/chromatin/ALKBH3/ALKBH3-evaluation.md
 M detail/chromatin/ARID3A/ARID3A-evaluation.md
 M detail/chromatin/BAHD1/BAHD1-evaluation.md
 M detail/chromatin/CFDP1/CFDP1-evaluation.md
 M detail/chromatin/CRAMP1/CRAMP1-evaluation.md
 M detail/chromatin/CREB3L4/CREB3L4-evaluation.md
 M detail/chromatin/CSNK1A1/CSNK1A1-evaluation.md
 M detail/chromatin/DSN1/DSN1-evaluation.md
 M detail/chromatin/ELOF1/ELOF1-evaluation.md
 M detail/chromatin/EXD2/EXD2-evaluation.md
 M detail/chromatin/FAM131A/FAM131A-evaluation.md
 M detail/chromatin/IHO1/IHO1-evaluation.md
 M detail/chromatin/JADE1/JADE1-evaluation.md
 M detail/chromatin/LRWD1/LRWD1-evaluation.md

```

## git diff --stat
```
 .../detail/rejected/OASL/OASL-evaluation.md                  |  4 ++++
 .../detail/rejected/XRN2/XRN2-evaluation.md                  |  4 ++++
 790 files changed, 3143 insertions(+), 31 deletions(-)

```
