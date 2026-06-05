---
type: protein-evaluation
gene: "ABL1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ABL1 — REJECTED (研究热度过高 (PubMed strict=1942，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ABL1 / ABL, JTK7 |
| 蛋白名称 | Tyrosine-protein kinase ABL1 |
| 蛋白大小 | 1130 aa / 122.9 kDa |
| UniProt ID | P00519 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Cytoplasm, cytoskeleton; Nucleus; Mitochondrion; Nucleus mem |
| 蛋白大小 | 8/10 | ×1 | 8 | 1130 aa / 122.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1942 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.4; PDB: 1AB2, 1AWO, 1BBZ, 1JU5, 1OPL, 1ZZP, 2ABL |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035837, IPR015015, IPR011009, IPR050198, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.0/180** | |
| **归一化总分** | | | **43.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Supported |
| UniProt | Cytoplasm, cytoskeleton; Nucleus; Mitochondrion; Nucleus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- glutamatergic synapse (GO:0098978)
- growth cone (GO:0030426)
- mitochondrion (GO:0005739)
- neuronal cell body (GO:0043025)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1942 |
| PubMed broad count | 4831 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ABL, JTK7 |

**关键文献**:
1. Chronic Myeloid Leukemia: Modern therapies, current challenges and future directions.. *Blood reviews*. PMID: 33773846
2. ABLs and TMKs are co-receptors for extracellular auxin.. *Cell*. PMID: 37979582
3. Timing and trajectory of BCR::ABL1-driven chronic myeloid leukaemia.. *Nature*. PMID: 40205062
4. Significance of Measurable Residual Disease in Adult Philadelphia Chromosome-Positive ALL: A GRAAPH-2014 Study.. *Journal of clinical oncology : official journal of the American Society of Clinical Oncology*. PMID: 39028928
5. Developmental trajectories and cooperating genomic events define molecular subtypes of BCR::ABL1-positive ALL.. *Blood*. PMID: 38153913

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.4 |
| 高置信度残基 (pLDDT>90) 占比 | 36.7% |
| 置信残基 (pLDDT 70-90) 占比 | 9.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 49.2% |
| 有序区域 (pLDDT>70) 占比 | 46.3% |
| 可用 PDB 条目 | 1AB2, 1AWO, 1BBZ, 1JU5, 1OPL, 1ZZP, 2ABL, 2E2B, 2F4J, 2FO0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.4），有序残基占 46.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035837, IPR015015, IPR011009, IPR050198, IPR000719; Pfam: PF08919, PF07714, PF00017 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GRB2 | 0.999 | 0.846 | — |
| CRK | 0.999 | 0.986 | — |
| ABI1 | 0.998 | 0.876 | — |
| CRKL | 0.998 | 0.887 | — |
| RIN1 | 0.997 | 0.808 | — |
| CBL | 0.996 | 0.896 | — |
| BCR | 0.996 | 0.737 | — |
| SHC1 | 0.991 | 0.610 | — |
| ATM | 0.988 | 0.820 | — |
| HSP90AA1 | 0.983 | 0.788 | — |

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
| 三维结构 | AlphaFold pLDDT=63.4 + PDB: 1AB2, 1AWO, 1BBZ, 1JU5, 1OPL,  | pLDDT=63.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Nucleus; Mitochondrion; N / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ABL1 — Tyrosine-protein kinase ABL1，研究基础较多，新颖性有限。
2. 蛋白大小1130 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1942 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1942 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P00519
- Protein Atlas: https://www.proteinatlas.org/ENSG00000097007-ABL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ABL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P00519
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000097007-ABL1/subcellular

![](https://images.proteinatlas.org/27280/258_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/27280/258_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/27280/259_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/27280/259_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/27280/260_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/27280/260_B8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P00519-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
