---
type: protein-evaluation
gene: "SPRR4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPRR4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPRR4 |
| 蛋白名称 | Small proline-rich protein 4 |
| 蛋白大小 | 79 aa / 8.8 kDa |
| UniProt ID | Q96PI1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Nuclear membrane; UniProt: Cytoplasm; Cytoplasm, cell cortex |
| 蛋白大小 | 5/10 | ×1 | 5 | 79 aa / 8.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.4; PDB: 无 |
| 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nuclear membrane | Approved |
| UniProt | Cytoplasm; Cytoplasm, cell cortex | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell cortex (GO:0005938)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of mitophagy-related biomarkers with immune cell infiltration in psoriasis.. *BMC medical genomics*. PMID: 40598168
2. Integration of Transcriptomics and Antibody-Based Proteomics for Exploration of Proteins Expressed in Specialized Tissues.. *Journal of proteome research*. PMID: 30272454
3. Isosorbide Di-(Linoleate/Oleate) Stimulates Prodifferentiation Gene Expression to Restore the Epidermal Barrier and Improve Skin Hydration.. *The Journal of investigative dermatology*. PMID: 33181142
4. SPRR4, a novel cornified envelope precursor: UV-dependent epidermal expression and selective incorporation into fragile envelopes.. *Journal of cell science*. PMID: 11719550
5. The effect of pimecrolimus on expression of genes associated with skin barrier dysfunction in atopic dermatitis skin lesions.. *Experimental dermatology*. PMID: 22142393

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.4 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 26.6% |
| 中等置信 (pLDDT 50-70) 占比 | 73.4% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 26.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.4），有序残基占 26.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LCE2A | 0.703 | 0.000 | — |
| KPRP | 0.694 | 0.000 | — |
| LOR | 0.691 | 0.000 | — |
| SPRR3 | 0.683 | 0.000 | — |
| IVL | 0.658 | 0.000 | — |
| LELP1 | 0.639 | 0.000 | — |
| TCHHL1 | 0.634 | 0.000 | — |
| LCE3E | 0.584 | 0.000 | — |
| LCE6A | 0.581 | 0.000 | — |
| LCE1A | 0.576 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.4 + PDB: 无 | pLDDT=67.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cell cortex / Nucleoplasm, Cytosol; 额外: Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SPRR4 — Small proline-rich protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小79 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96PI1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184148-SPRR4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPRR4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96PI1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000184148-SPRR4/subcellular

![](https://images.proteinatlas.org/55963/1941_C2_4_red_green.jpg)
![](https://images.proteinatlas.org/55963/1941_C2_6_red_green.jpg)
![](https://images.proteinatlas.org/55963/1972_E2_10_cr5e15aa286c338_red_green.jpg)
![](https://images.proteinatlas.org/55963/1972_E2_30_cr5e15aa286c92f_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96PI1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96PI1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | 未检出 |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000184148-SPRR4/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
