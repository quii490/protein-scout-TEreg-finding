---
type: protein-evaluation
gene: "REV3L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## REV3L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | REV3L / POLZ, REV3 |
| 蛋白名称 | DNA polymerase zeta catalytic subunit |
| 蛋白大小 | 3130 aa / 352.8 kDa |
| UniProt ID | O60673 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 0/10 | ×1 | 0 | 3130 aa / 352.8 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=74 篇 (≤80→4) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 3ABD, 3ABE, 3VU7, 4EXT, 4GK0, 4GK5, 5O8K |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006172, IPR017964, IPR006133, IPR006134, IPR043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.0/180** | |
| **归一化总分** | | | **51.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- site of DNA damage (GO:0090734)
- zeta DNA polymerase complex (GO:0016035)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 74 |
| PubMed broad count | 183 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: POLZ, REV3 |

**关键文献**:
1. REV3L, a promising target in regulating the chemosensitivity of cervical cancer cells.. *PloS one*. PMID: 25781640
2. REV3L as a prognostic biomarker and therapeutic target in bladder urothelial carcinoma.. *Biochemical and biophysical research communications*. PMID: 41187431
3. The role of DNA polymerase ζ in benzo[a]pyrene-induced mutagenesis in the mouse lung.. *Mutagenesis*. PMID: 33544859
4. Precision Target Discovery for Migraine: An Integrated GWAS-eQTL-PheWAS Pipeline.. *Molecules (Basel, Switzerland)*. PMID: 41097341
5. Molecular cloning, expression and chromosomal localisation of the mouse Rev3l gene, encoding the catalytic subunit of polymerase zeta.. *Mutation research*. PMID: 10102037

**评价**: 已有一定研究基础，但仍存在niche空间。

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
| 可用 PDB 条目 | 3ABD, 3ABE, 3VU7, 4EXT, 4GK0, 4GK5, 5O8K, 6BC8, 6BCD, 6BI7 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006172, IPR017964, IPR006133, IPR006134, IPR043502; Pfam: PF00136, PF03104, PF15735 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAD2L2 | 0.999 | 0.997 | — |
| POLD2 | 0.999 | 0.964 | — |
| REV1 | 0.999 | 0.991 | — |
| POLD3 | 0.997 | 0.143 | — |
| POLE | 0.989 | 0.419 | — |
| FANCM | 0.987 | 0.962 | — |
| POLH | 0.986 | 0.838 | — |
| POLA2 | 0.985 | 0.745 | — |
| POLD1 | 0.984 | 0.635 | — |
| PRIM2 | 0.980 | 0.636 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-28974373 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SLTM | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H3-3A | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| APP | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| POLD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Mad2l2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CCND1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 3ABD, 3ABE, 3VU7, 4EXT, 4GK0,  | pLDDT=0, v? | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. REV3L — DNA polymerase zeta catalytic subunit，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小3130 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 74 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60673
- Protein Atlas: https://www.proteinatlas.org/ENSG00000009413-REV3L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=REV3L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60673
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000009413-REV3L/subcellular

![](https://images.proteinatlas.org/69382/1369_E4_2_red_green.jpg)
![](https://images.proteinatlas.org/69382/1369_E4_7_red_green.jpg)
![](https://images.proteinatlas.org/69382/1371_E4_2_red_green.jpg)
![](https://images.proteinatlas.org/69382/1371_E4_4_red_green.jpg)
![](https://images.proteinatlas.org/69382/1418_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/69382/1418_C2_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60673 |
| SMART | SM00486; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR006172;IPR017964;IPR006133;IPR006134;IPR043502;IPR042087;IPR023211;IPR056435;IPR032757;IPR030559;IPR056447;IPR012337;IPR036397;IPR025687; |
| Pfam | PF00136;PF03104;PF15735;PF24055;PF24065;PF14260; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000009413-REV3L/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MAD2L2 | Intact, Biogrid | true |
| APP | Intact | false |
| MAD2L1 | Biogrid | false |
| PKM | Biogrid | false |
| REV1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
