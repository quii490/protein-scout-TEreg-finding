---
type: protein-evaluation
gene: "PKIB"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PKIB — REJECTED (核定位证据不足 (核定位得分 2/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | PKIB |
| 蛋白名称 | cAMP-dependent protein kinase inhibitor beta |
| 蛋白大小 | 78 aa / ~9 kDa |
| UniProt ID | Q9C010 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | GO-CC: predominantly cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 78 aa (very small) |
| 研究新颖性 | 3/10 | ×5 | 15 | PubMed=20 |
| 三维结构 | 5/10 | ×3 | 15 | Small IDR-rich, limited structure |
| 调控结构域 | 2/10 | ×2 | 4 | Single PKI domain |
| PPI 网络 | 1/10 | ×3 | 3 | PPI degree=0 |
| **加权总分** | | | **53/180** | |
| **归一化总分** | | | **29/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634) - weak/transient annotation

**结论**: 该蛋白定位于细胞质，作为PKA的竞争性抑制剂发挥作用。虽有核内瞬时出现的微弱证据，但主要功能在胞质中实现对PKA的抑制。无明确核定位信号。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI

蛋白极小（78 aa），为天然无序蛋白。研究较少（PubMed约20篇），主要涉及PKA信号调控。结构简单，含单一PKI抑制结构域。PPI网络极弱（degree=0），仅作为其他蛋白的靶标出现。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: PKIB — cAMP依赖性蛋白激酶抑制剂beta，在细胞质中通过与PKA催化亚基结合发挥抑制作用。该蛋白定位于胞质，无可靠核定位证据。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9C010
- Protein Atlas: https://www.proteinatlas.org/search/PKIB
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PKIB
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/PKIB
