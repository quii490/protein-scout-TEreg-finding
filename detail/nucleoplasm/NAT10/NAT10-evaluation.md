---
type: protein-evaluation
gene: "NAT10"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NAT10 — REJECTED (研究热度过高 (PubMed strict=234，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAT10 / ALP, KIAA1709 |
| 蛋白名称 | RNA cytidine acetyltransferase |
| 蛋白大小 | 1025 aa / 115.7 kDa |
| UniProt ID | Q9H0A0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Midbody; UniProt: Nucleus, nucleolus; Midbody |
| 蛋白大小 | 8/10 | ×1 | 8 | 1025 aa / 115.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=234 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=78.4; PDB: 6VLA, 7MQ8, 7MQ9, 9J3C |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016181, IPR000182, IPR033688, IPR027417, IPR007 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Midbody | Enhanced |
| UniProt | Nucleus, nucleolus; Midbody | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- membrane (GO:0016020)
- midbody (GO:0030496)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- small-subunit processome (GO:0032040)
- telomerase holoenzyme complex (GO:0005697)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 234 |
| PubMed broad count | 459 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ALP, KIAA1709 |

**关键文献**:
1. Lysine 2-hydroxyisobutyrylation of NAT10 promotes cancer metastasis in an ac4C-dependent manner.. *Cell research*. PMID: 36882514
2. NAT10 Drives Cisplatin Chemoresistance by Enhancing ac4C-Associated DNA Repair in Bladder Cancer.. *Cancer research*. PMID: 36939377
3. NAT10 Is Involved in Cardiac Remodeling Through ac4C-Mediated Transcriptomic Regulation.. *Circulation research*. PMID: 37955115
4. NAT10 promotes vascular remodelling via mRNA ac4C acetylation.. *European heart journal*. PMID: 39453784
5. Mechanisms of NAT10 as ac4C writer in diseases.. *Molecular therapy. Nucleic acids*. PMID: 37128278

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.4 |
| 高置信度残基 (pLDDT>90) 占比 | 20.2% |
| 置信残基 (pLDDT 70-90) 占比 | 57.6% |
| 中等置信 (pLDDT 50-70) 占比 | 14.4% |
| 低置信 (pLDDT<50) 占比 | 7.8% |
| 有序区域 (pLDDT>70) 占比 | 77.8% |
| 可用 PDB 条目 | 6VLA, 7MQ8, 7MQ9, 9J3C |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6VLA, 7MQ8, 7MQ9, 9J3C）+ AlphaFold高质量预测（pLDDT=78.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016181, IPR000182, IPR033688, IPR027417, IPR007807; Pfam: PF13718, PF05127, PF08351 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WDR46 | 0.999 | 0.991 | — |
| BYSL | 0.999 | 0.991 | — |
| NOP58 | 0.999 | 0.992 | — |
| HEATR1 | 0.999 | 0.981 | — |
| UTP4 | 0.999 | 0.989 | — |
| NOP56 | 0.999 | 0.987 | — |
| AATF | 0.999 | 0.993 | — |
| NOP14 | 0.999 | 0.966 | — |
| NOL10 | 0.999 | 0.995 | — |
| NOL6 | 0.999 | 0.991 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KRE33 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29054886|imex:IM-25795| |
| UTP7 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SBP1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| KRR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| NOC4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| BMS1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| CDC55 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| BFR2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| KRI1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| PWP2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.4 + PDB: 6VLA, 7MQ8, 7MQ9, 9J3C | pLDDT=78.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Midbody / Nucleoli; 额外: Midbody | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NAT10 — RNA cytidine acetyltransferase，研究基础较多，新颖性有限。
2. 蛋白大小1025 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 234 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 234 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0A0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135372-NAT10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAT10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0A0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (enhanced)。来源: https://www.proteinatlas.org/ENSG00000135372-NAT10/subcellular

![](https://images.proteinatlas.org/57576/1208_F10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/57576/1208_F10_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/57576/983_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57576/983_F8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/57576/991_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57576/991_F8_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H0A0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H0A0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 558..753; /note="N-acetyltransferase"; /evidence="ECO:0000255\|HAMAP-Rule:MF_03211" |
| InterPro | IPR016181;IPR000182;IPR033688;IPR027417;IPR007807;IPR032672;IPR013562;IPR027992; |
| Pfam | PF13718;PF05127;PF08351;PF13725; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000135372-NAT10/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AATF | Biogrid, Bioplex | true |
| KRR1 | Biogrid, Bioplex | true |
| RPL10 | Biogrid, Bioplex | true |
| RPL31 | Biogrid, Bioplex | true |
| RPS2 | Intact, Biogrid, Bioplex | true |
| RPS6 | Biogrid, Bioplex | true |
| THUMPD1 | Intact, Biogrid, Bioplex | true |
| VIM | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
