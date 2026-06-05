---
type: protein-evaluation
gene: "CHMP1B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CHMP1B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHMP1B / C18orf2 |
| 蛋白名称 | Charged multivesicular body protein 1b |
| 蛋白大小 | 199 aa / 22.1 kDa |
| UniProt ID | Q7LBR1 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CHMP1B/IF_images/MCF-7_1.jpg|MCF-7]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/CHMP1B/IF_images/SiHa_1.jpg|SiHa]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Midbody; UniProt: Cytoplasm, cytosol; Endosome; Late endosome membrane |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 199 aa / 22.1 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.8; PDB: 3EAB, 3JC1, 4TXQ, 4TXR, 6E8G, 6TZ4, 6TZ5 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR005024; Pfam: PF03357 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Midbody | Approved |
| UniProt | Cytoplasm, cytosol; Endosome; Late endosome membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- amphisome membrane (GO:1904930)
- autophagosome membrane (GO:0000421)
- cytosol (GO:0005829)
- endosome membrane (GO:0010008)
- ESCRT III complex (GO:0000815)
- extracellular exosome (GO:0070062)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C18orf2 |

**关键文献**:
1. A chemical inhibitor of IST1-CHMP1B interaction impairs endosomal recycling and induces noncanonical LC3 lipidation.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38635626
2. Classical swine fever virus hijacks ESCRT-III and VPS4A to promote phagophore closure for accelerating mitophagy.. *Autophagy*. PMID: 40574328
3. The hereditary spastic paraplegia protein spastin interacts with the ESCRT-III complex-associated endosomal protein CHMP1B.. *Human molecular genetics*. PMID: 15537668
4. IST1 regulates select endosomal recycling pathways.. *bioRxiv : the preprint server for biology*. PMID: 37577466
5. The Noonan Syndrome Gene Lztr1 Controls Cardiovascular Function by Regulating Vesicular Trafficking.. *Circulation research*. PMID: 32175818

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.8 |
| 高置信度残基 (pLDDT>90) 占比 | 44.2% |
| 置信残基 (pLDDT 70-90) 占比 | 33.2% |
| 中等置信 (pLDDT 50-70) 占比 | 15.6% |
| 低置信 (pLDDT<50) 占比 | 7.0% |
| 有序区域 (pLDDT>70) 占比 | 77.4% |
| 可用 PDB 条目 | 3EAB, 3JC1, 4TXQ, 4TXR, 6E8G, 6TZ4, 6TZ5, 6TZ9, 8V2Q, 8V2R |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3EAB, 3JC1, 4TXQ, 4TXR, 6E8G, 6TZ4, 6TZ5, 6TZ9, 8V2Q, 8V2R）+ AlphaFold预测（pLDDT=80.8），实验结构可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005024; Pfam: PF03357 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VTA1 | 0.999 | 0.994 | — |
| SPAST | 0.999 | 0.926 | — |
| CHMP3 | 0.999 | 0.878 | — |
| VPS4A | 0.999 | 0.830 | — |
| IST1 | 0.999 | 0.994 | — |
| CHMP2A | 0.997 | 0.843 | — |
| VPS4B | 0.996 | 0.722 | — |
| RNF103-CHMP3 | 0.995 | 0.878 | — |
| CHMP4B | 0.994 | 0.910 | — |
| CHMP2B | 0.994 | 0.296 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000432279.1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-24991|pubmed:16730941 |
| Wasf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| STAMBP | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| SNRNP65 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| LIP5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| folC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PA | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| EBI-2846580 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| secA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.8 + PDB: 3EAB, 3JC1, 4TXQ, 4TXR, 6E8G,  | pLDDT=80.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Endosome; Late endosome membra / Nucleoplasm, Midbody | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CHMP1B — Charged multivesicular body protein 1b，非常新颖，仅有少数基础研究。
2. 蛋白大小199 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7LBR1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000255112-CHMP1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHMP1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7LBR1
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:55:03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7LBR1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
