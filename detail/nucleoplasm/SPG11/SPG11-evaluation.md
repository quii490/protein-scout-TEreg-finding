---
type: protein-evaluation
gene: "SPG11"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SPG11 — REJECTED (研究热度过高 (PubMed strict=178，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPG11 / KIAA1840 |
| 蛋白名称 | Spatacsin |
| 蛋白大小 | 2443 aa / 278.9 kDa |
| UniProt ID | Q96JI7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; 额外: Nucleoli; UniProt: Cytoplasm, cytosol; Nucleus; Cell projection, axon; Cell pro |
| 蛋白大小 | 2/10 | ×1 | 2 | 2443 aa / 278.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=178 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.7; PDB: 8YAB, 8YAD, 8YAH |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028103, IPR028107; Pfam: PF14649 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.5/180** | |
| **归一化总分** | | | **40.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoli | Supported |
| UniProt | Cytoplasm, cytosol; Nucleus; Cell projection, axon; Cell projection, dendrite | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- endoplasmic reticulum (GO:0005783)
- lysosomal membrane (GO:0005765)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 178 |
| PubMed broad count | 324 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1840 |

**关键文献**:
1. Clinical and genetic spectra of 1550 index patients with hereditary spastic paraplegia.. *Brain : a journal of neurology*. PMID: 34983064
2. The spectrum of neurodevelopmental, neuromuscular and neurodegenerative disorders due to defective autophagy.. *Autophagy*. PMID: 34130600
3. Amyotrophic Lateral Sclerosis Overview.. **. PMID: 20301623
4. Decreasing ganglioside synthesis delays motor and cognitive symptom onset in Spg11 knockout mice.. *Neurobiology of disease*. PMID: 38876323
5. SPG11: clinical and genetic features of seven Czech patients and literature review.. *Neurological research*. PMID: 35254204

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.7 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 55.3% |
| 中等置信 (pLDDT 50-70) 占比 | 28.8% |
| 低置信 (pLDDT<50) 占比 | 15.9% |
| 有序区域 (pLDDT>70) 占比 | 55.3% |
| 可用 PDB 条目 | 8YAB, 8YAD, 8YAH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.7），有序残基占 55.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028103, IPR028107; Pfam: PF14649 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AP5Z1 | 0.996 | 0.435 | — |
| ZFYVE26 | 0.990 | 0.087 | — |
| AP5B1 | 0.980 | 0.435 | — |
| AP5S1 | 0.961 | 0.232 | — |
| SPG7 | 0.957 | 0.000 | — |
| SPG21 | 0.949 | 0.000 | — |
| SPAST | 0.936 | 0.000 | — |
| PNPLA6 | 0.856 | 0.000 | — |
| SPART | 0.852 | 0.000 | — |
| AP5M1 | 0.838 | 0.628 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000261866.7 | psi-mi:"MI:0030"(cross-linking study) | pubmed:40175557|imex:IM-30310 |
| hmsS | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| tcaA1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| AP5M1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VIPR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CRYL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SERTAD3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| Rab10 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26885862|imex:IM-24977 |
| Elavl1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| GPR45 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.7 + PDB: 8YAB, 8YAD, 8YAH | pLDDT=66.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus; Cell projection, axon / Plasma membrane, Cytosol; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SPG11 — Spatacsin，研究基础较多，新颖性有限。
2. 蛋白大小2443 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 178 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 178 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96JI7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104133-SPG11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPG11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96JI7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96JI7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96JI7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028103;IPR028107; |
| Pfam | PF14649; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000104133-SPG11/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AP5B1 | Bioplex | false |
| AP5S1 | Bioplex | false |
| BAG2 | Bioplex | false |
| D2HGDH | Bioplex | false |
| DHFR | Bioplex | false |
| DNM1 | Intact | false |
| EEF1AKMT3 | Bioplex | false |
| GPR182 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
