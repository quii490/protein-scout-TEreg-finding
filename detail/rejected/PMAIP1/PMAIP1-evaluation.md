---
type: protein-evaluation
gene: "PMAIP1"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PMAIP1 — REJECTED (核定位证据不足 (核定位得分 1/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | PMAIP1 |
| 蛋白名称 | Phorbol-12-myristate-13-acetate-induced protein 1 (NOXA) |
| 蛋白大小 | 103 aa / ~11 kDa |
| UniProt ID | Q13794 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | GO-CC: mitochondrial outer membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 103 aa (BH3-only) |
| 研究新颖性 | 7/10 | ×5 | 35 | PubMed=500 |
| 三维结构 | 4/10 | ×3 | 12 | Mostly disordered with BH3 helix |
| 调控结构域 | 2/10 | ×2 | 4 | Single BH3 motif |
| PPI 网络 | 6/10 | ×3 | 18 | PPI degree=24 |
| **加权总分** | | | **81/180** | |
| **归一化总分** | | | **45/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- mitochondrial outer membrane (GO:0005741)
- cytoplasm (GO:0005737)

**结论**: 该蛋白定位于线粒体外膜，作为关键的促凋亡BH3-only蛋白发挥作用。虽然研究热度高、PPI网络丰富，但其功能完全在线粒体外膜上实现（结合MCL1、促进MOMP）。无核定位信号或核内功能报道。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI

蛋白较小（103 aa），为典型的BH3-only蛋白。研究极多（PubMed约500篇），是凋亡领域的核心分子。结构以无序为主，含单一BH3螺旋基序。PPI网络丰富（degree=24），与Bcl-2家族成员广泛互作。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: PMAIP1/NOXA — 线粒体外膜促凋亡BH3-only蛋白，通过中和MCL1促进线粒体途径凋亡。该蛋白定位于线粒体外膜，无核定位证据。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13794
- Protein Atlas: https://www.proteinatlas.org/search/PMAIP1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PMAIP1
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/PMAIP1
