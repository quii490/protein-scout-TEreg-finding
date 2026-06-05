---
type: protein-evaluation
gene: "LIMD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LIMD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LIMD2 |
| 蛋白名称 | LIM domain-containing protein 2 |
| 蛋白大小 | 127 aa / 14.1 kDa |
| UniProt ID | Q9BT23 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 127 aa / 14.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=72.2; PDB: 2LZU |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR044115, IPR001781; Pfam: PF00412 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.0/180** | |
| **归一化总分** | | | **75.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Atrazine exposure induces skeletal muscle atrophy: Multi-omics insights into mechanisms and therapeutic targets.. *Ecotoxicology and environmental safety*. PMID: 40945087
2. LIMD2 is a small LIM-only protein overexpressed in metastatic lesions that regulates cell motility and tumor progression by directly binding to and activating the integrin-linked kinase.. *Cancer research*. PMID: 24590809
3. LIMD2 is the Signature of Cell Aging-immune/Inflammation in Acute Myocardial Infarction.. *Current medicinal chemistry*. PMID: 37936458
4. Overexpression of LIMD2 promotes the progression of non-small cell lung cancer.. *Oncology letters*. PMID: 31423280
5. LIMD2 targeted by miR‑34a promotes the proliferation and invasion of non‑small cell lung cancer cells.. *Molecular medicine reports*. PMID: 30221696

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.2 |
| 高置信度残基 (pLDDT>90) 占比 | 24.4% |
| 置信残基 (pLDDT 70-90) 占比 | 27.6% |
| 中等置信 (pLDDT 50-70) 占比 | 33.9% |
| 低置信 (pLDDT<50) 占比 | 14.2% |
| 有序区域 (pLDDT>70) 占比 | 52.0% |
| 可用 PDB 条目 | 2LZU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=72.2，有序区 52.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR044115, IPR001781; Pfam: PF00412 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PDLIM2 | 0.691 | 0.000 | — |
| GRAP | 0.638 | 0.000 | — |
| MED14 | 0.483 | 0.000 | — |
| EYA3 | 0.483 | 0.000 | — |
| ZNF771 | 0.460 | 0.000 | — |
| MARK2 | 0.456 | 0.046 | — |
| MPP7 | 0.435 | 0.045 | — |
| SPATS2 | 0.433 | 0.000 | — |
| TMA7 | 0.430 | 0.000 | — |
| FHL2 | 0.426 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| carB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PSMA6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.2 + PDB: 2LZU | pLDDT=72.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LIMD2 — LIM domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小127 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BT23
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136490-LIMD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LIMD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BT23
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000136490-LIMD2/subcellular

![](https://images.proteinatlas.org/62432/1141_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/62432/1141_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/62432/1170_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/62432/1170_A4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BT23-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
