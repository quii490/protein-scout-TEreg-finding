---
type: protein-evaluation
gene: "RPTOR"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RPTOR — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | RPTOR |
| 蛋白名称 | Regulatory-associated protein of mTOR (RAPTOR) |
| 蛋白大小 | 1335 aa / ~149 kDa |
| UniProt ID | Q8N122 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | 胞质: mTORC1复合物支架蛋白, 主要胞质/溶酶体定位; 少数核内报道 |
| 蛋白大小 | 10/10 | ×1 | 10 | 1335 aa |
| 研究新颖性 | 1/10 | ×5 | 5 | PubMed≈3000+篇, mTOR信号研究极成熟 |
| 三维结构 | 7/10 | ×3 | 21 | cryo-EM多结构可用, mTORC1复合物已高分辨解析 |
| 调控结构域 | 7/10 | ×2 | 14 | HEAT重复(RAPTOR N端) + WD40重复 + TOS结合模体 |
| PPI 网络 | 10/10 | ×3 | 30 | PPI degree=58 |
| **加权总分** | | | **88/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- TORC1 complex (GO:0031931)
- lysosomal membrane (GO:0005765)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: RPTOR(RAPTOR)为mTORC1复合物核心支架亚基，主要定位于溶酶体膜表面的mTORC1复合物中，在氨基酸信号感应后招募mTOR到溶酶体。虽有零星文献描述其在应激条件下可部分入核，但主要功能空间在胞质/溶酶体。非核蛋白。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 1335 aa，极大蛋白，cryo-EM结构已解析。
- **研究现状**: PubMed超3000篇，mTOR核心组分，研究极成熟，几乎被全方位研究。
- **三维结构**: 多个cryo-EM结构可用，mTORC1全复合物结构解析到近原子分辨率。
- **结构域**: RNC(HEAT重复)结构域 + 串联WD40重复 + TOS基序识别模体。
- **PPI**: 58个互作配体(source STRING)，mTOR信号通路核心枢纽，互作网络极为密集。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: RPTOR — mTORC1关键支架蛋白RAPTOR，主要定位于胞质/溶酶体膜，作为营养信号感应和mTORC1激活的核心适配器。虽有极少数入核报道但主要功能空间非核，不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N122
- Protein Atlas: https://www.proteinatlas.org/search/RPTOR
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RPTOR
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/RPTOR
