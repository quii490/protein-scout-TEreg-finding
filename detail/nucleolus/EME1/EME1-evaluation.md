---
type: protein-evaluation
gene: "EME1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EME1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EME1 / MMS4 |
| 蛋白名称 | Structure-specific endonuclease subunit EME1 |
| 蛋白大小 | 570 aa / 63.3 kDa |
| UniProt ID | Q96AY2 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EME1/IF_images/HAP1_1.jpg|HAP1]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EME1/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 570 aa / 63.3 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=87 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.5; PDB: 2ZIU, 2ZIV, 2ZIW, 2ZIX, 4P0P, 4P0Q, 4P0R |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042530, IPR043086, IPR043087, IPR006166, IPR033 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.5/180** | |
| **归一化总分** | | | **55.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- endodeoxyribonuclease complex (GO:1905347)
- heterochromatin (GO:0000792)
- Holliday junction resolvase complex (GO:0048476)
- nuclear chromosome (GO:0000228)
- nuclear replication fork (GO:0043596)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 87 |
| PubMed broad count | 208 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MMS4 |

**关键文献**:
1. CRISPR/Cas9 screens identify LIG1 as a sensitizer of PARP inhibitors in castration-resistant prostate cancer.. *The Journal of clinical investigation*. PMID: 39718835
2. Investigation of the immunogenicity of Zika glycan loop.. *Virology journal*. PMID: 32234060
3. SLX4-SLX1 Protein-independent Down-regulation of MUS81-EME1 Protein by HIV-1 Viral Protein R (Vpr).. *The Journal of biological chemistry*. PMID: 27354282
4. A protocol to determine the activities of human MUS81-EME1&2 endonucleases.. *STAR protocols*. PMID: 35819885
5. Essential meiotic structure-specific endonuclease1 (EME1) promotes malignant features in gastric cancer cells via the Akt/GSK3B/CCND1 pathway.. *Bioengineered*. PMID: 34719326

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.5 |
| 高置信度残基 (pLDDT>90) 占比 | 38.2% |
| 置信残基 (pLDDT 70-90) 占比 | 13.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 40.0% |
| 有序区域 (pLDDT>70) 占比 | 51.7% |
| 可用 PDB 条目 | 2ZIU, 2ZIV, 2ZIW, 2ZIX, 4P0P, 4P0Q, 4P0R, 4P0S, 9F98, 9F99 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EME1/EME1-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=67.5），有序残基占 51.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042530, IPR043086, IPR043087, IPR006166, IPR033310; Pfam: PF21292, PF02732 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MUS81 | 0.999 | 0.991 | — |
| SLX4 | 0.999 | 0.783 | — |
| SLX1A | 0.997 | 0.420 | — |
| EME2 | 0.985 | 0.000 | — |
| ERCC4 | 0.960 | 0.334 | — |
| ERCC1 | 0.931 | 0.000 | — |
| GEN1 | 0.931 | 0.140 | — |
| EXO1 | 0.915 | 0.140 | — |
| RAD51 | 0.881 | 0.051 | — |
| BRCA1 | 0.880 | 0.439 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| SLX1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| MUS81 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12201|pubmed:19596236 |
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ERCC4 | psi-mi:"MI:0096"(pull down) | pubmed:17289582|imex:IM-25488 |
| FANCM | psi-mi:"MI:0096"(pull down) | pubmed:17289582|imex:IM-25488 |
| ENSP00000339897.4 | psi-mi:"MI:1034"(nuclease assay) | pubmed:17289582|imex:IM-25488 |
| DCAF1 | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:24412650|imex:IM-22043 |
| vpr | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:24412650|imex:IM-22043 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.5 + PDB: 2ZIU, 2ZIV, 2ZIW, 2ZIX, 4P0P,  | pLDDT=67.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EME1 — Structure-specific endonuclease subunit EME1，研究基础较多，新颖性有限。
2. 蛋白大小570 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 87 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96AY2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154920-EME1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EME1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96AY2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/EME1/EME1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96AY2 |
| SMART | SM00891; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR042530;IPR043086;IPR043087;IPR006166;IPR033310;IPR047522; |
| Pfam | PF21292;PF02732; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000154920-EME1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MUS81 | Intact, Biogrid | true |
| SLX4 | Intact, Biogrid | true |
| APP | Biogrid | false |
| HERC2 | Biogrid | false |
| SUMO2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
