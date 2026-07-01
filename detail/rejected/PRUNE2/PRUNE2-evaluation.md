---
type: protein-evaluation
gene: "PRUNE2"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PRUNE2 — REJECTED (核定位证据不足 (核定位得分 1/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | PRUNE2 |
| 蛋白名称 | Protein prune homolog 2 |
| 蛋白大小 | 3088 aa / ~335 kDa |
| UniProt ID | Q8WUY3 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | GO-CC: cytoplasm |
| 蛋白大小 | 1/10 | ×1 | 1 | 3088 aa (very large) |
| 研究新颖性 | 3/10 | ×5 | 15 | PubMed=40 |
| 三维结构 | 3/10 | ×3 | 9 | Multi-domain, partially disordered |
| 调控结构域 | 6/10 | ×2 | 12 | BNIP2 + BCH + DHHA1 + CRAL-TRIO |
| PPI 网络 | 3/10 | ×3 | 9 | PPI degree=7 |
| **加权总分** | | | **50/180** | |
| **归一化总分** | | | **28/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 该蛋白为超大型胞质蛋白，通过BNIP2/BCH结构域与Rho家族GTPases互作，调控细胞骨架动力学。虽在前列腺癌中被认为是潜在抑癌基因，但无任何核定位证据。UniProt GO-CC明确指向胞质。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI

蛋白极长（3088 aa），为少见的超大胞质蛋白（~335 kDa）。研究较少（PubMed约40篇），主要关注前列腺癌。多结构域蛋白，含BNIP2、BCH、DHHA1和CRAL-TRIO结构域，但整体结构部分无序。PPI网络中等偏弱（degree=7）。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: PRUNE2 — 含BNIP2基序的超大胞质蛋白，通过Rho GTPase通路调控细胞骨架，前列腺癌相关。该蛋白定位于胞质，无核定位证据。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WUY3
- Protein Atlas: https://www.proteinatlas.org/search/PRUNE2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRUNE2
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/PRUNE2
