---
type: protein-evaluation
gene: "MPND"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MPND 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MPND |
| 蛋白名称 | MPN domain-containing protein |
| 蛋白大小 | 471 aa / 50.7 kDa |
| UniProt ID | Q8N594 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli rim; 额外: Nucleoplasm; UniProt: 无注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 471 aa / 50.7 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.2; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000555, IPR050242, IPR037518, IPR040843; Pfam:  |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli rim; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- BRCA1-A complex (GO:0070531)
- BRISC complex (GO:0070552)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 26 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Synthesis and characterization of novel protein nanodots as drug delivery carriers with an enhanced biological efficacy of melatonin in breast cancer cells.. *RSC advances*. PMID: 35423422
2. Whole genome and transcriptome sequencing of matched primary and peritoneal metastatic gastric carcinoma.. *Scientific reports*. PMID: 26330360
3. MPND Loss Epigenetically Activates TGF-β/SMAD3 Signaling to Drive Tumor Progression and Metastasis in Non-small Cell Lung Cancer.. *Cancer research*. PMID: 42202052
4. LncRNA-mRNA co-expression network in the mechanism of butylphthalide treatment for ischemic stroke.. *BMC neurology*. PMID: 40211238
5. Characterization of a single gene cluster responsible for methylpendolmycin and pendolmycin biosynthesis in the deep sea bacterium Marinactinospora thermotolerans.. *Chembiochem : a European journal of chemical biology*. PMID: 22362652

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.2 |
| 高置信度残基 (pLDDT>90) 占比 | 28.5% |
| 置信残基 (pLDDT 70-90) 占比 | 33.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.5% |
| 低置信 (pLDDT<50) 占比 | 29.5% |
| 有序区域 (pLDDT>70) 占比 | 62.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 中等质量（pLDDT=70.2，有序区 62.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000555, IPR050242, IPR037518, IPR040843; Pfam: PF01398, PF18755 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PSMD6 | 0.859 | 0.481 | — |
| PSMD4 | 0.821 | 0.486 | — |
| PSMC1 | 0.802 | 0.479 | — |
| PSMB2 | 0.801 | 0.596 | — |
| FAU | 0.785 | 0.736 | — |
| PSMA3 | 0.779 | 0.591 | — |
| PSMD13 | 0.752 | 0.486 | — |
| ADRM1 | 0.751 | 0.601 | — |
| PSMB4 | 0.737 | 0.549 | — |
| PSMA1 | 0.737 | 0.520 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| USP30 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| USP36 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| WFS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| SPRED1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| SOD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| KIF1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| RNF11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| HTRA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| JPH3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| APP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.2 + PDB: 无 | pLDDT=70.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli rim; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. MPND — MPN domain-containing protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小471 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N594
- Protein Atlas: https://www.proteinatlas.org/ENSG00000008382-MPND/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MPND
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N594
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 21:56:49
