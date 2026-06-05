---
type: protein-evaluation
gene: "DOCK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DOCK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOCK1 |
| 蛋白名称 | DOCK1 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | DOCK1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Nucleoli, Plasma membrane, Actin f; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=82 篇 (≤100→2) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **66/180** | |
| **归一化总分** | | | **36.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nucleoli, Plasma membrane, Actin filaments, Focal adhesion sites | Approved |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 82 |
| PubMed broad count | 246 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Construction of an acute myeloid leukemia prognostic model based on m6A-related efferocytosis-related genes.. *Frontiers in immunology*. PMID: 38077322
2. Genomic modifiers of neurological resilience in a Niemann-Pick C family.. *FEBS letters*. PMID: 40504793
3. MYLK*FLNB and DOCK1*LAMA2 gene-gene interactions associated with rheumatoid arthritis in the focal adhesion pathway.. *Frontiers in genetics*. PMID: 38803542
4. Human atherosclerotic plaque transcriptomics reveals endothelial beta-2 spectrin as a potential regulator a leaky plaque microvasculature phenotype.. *Angiogenesis*. PMID: 38780883
5. DOCK1 regulates the malignant biological behavior of endometrial cancer through c-Raf/ERK pathway.. *BMC cancer*. PMID: 38438882

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELMO1 | 0.999 | 0.938 | — |
| ELMO3 | 0.999 | 0.838 | — |
| ELMO2 | 0.999 | 0.374 | — |
| BCAR1 | 0.999 | 0.292 | — |
| RHOG | 0.999 | 0.522 | — |
| CRK | 0.999 | 0.904 | — |
| CRKL | 0.995 | 0.687 | — |
| RAC2 | 0.993 | 0.707 | — |
| WDR35 | 0.991 | 0.000 | — |
| SRC | 0.984 | 0.363 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm, Cytosol; 额外: Nucleoli, Plasma membran | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. DOCK1 — DOCK1 (UniProt未获取)，研究基础较多，新颖性有限。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 82 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/DOCK1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150760-DOCK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOCK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/DOCK1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000150760-DOCK1/subcellular

![](https://images.proteinatlas.org/70232/1896_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/70232/1896_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/70232/1929_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/70232/1929_A5_5_red_green.jpg)
![](https://images.proteinatlas.org/70232/2091_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/70232/2091_D8_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
