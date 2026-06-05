---
type: protein-evaluation
gene: "ANGEL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANGEL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANGEL2 / KIAA0759L |
| 蛋白名称 | RNA 2',3'-cyclic phosphatase ANGEL2 |
| 蛋白大小 | 544 aa / 62.3 kDa |
| UniProt ID | Q5VTE6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nuclear bodies, Mitochondria; UniProt: Mitochondrion matrix |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 544 aa / 62.3 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=74.4; PDB: 6RVZ, 6RW0 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR045816, IPR050410, IPR036691, IPR005135; Pfam:  |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分 (÷1.83)** | | | **68.9/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Mitochondria | Approved |
| UniProt | Mitochondrion matrix | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- Cajal body (GO:0015030)
- cytoplasm (GO:0005737)
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0759L |

**关键文献**:
1. ANGEL2 phosphatase activity is required for non-canonical mitochondrial RNA processing.. *Nature communications*. PMID: 36180430
2. ANGEL2 Modulates Wild-type TP53 Translation and Doxorubicin Chemosensitivity in Colon Cancer.. *Molecular cancer research : MCR*. PMID: 40052999
3. ANGEL2 is a member of the CCR4 family of deadenylases with 2',3'-cyclic phosphatase activity.. *Science (New York, N.Y.)*. PMID: 32732418
4. An epigenomic landscape of cervical intraepithelial neoplasia and cervical cancer using single-base resolution methylome and hydroxymethylome.. *Clinical and translational medicine*. PMID: 34323415

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.4 |
| 高置信度残基 (pLDDT>90) 占比 | 59.0% |
| 置信残基 (pLDDT 70-90) 占比 | 4.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 33.6% |
| 有序区域 (pLDDT>70) 占比 | 63.4% |
| 可用 PDB 条目 | 6RVZ, 6RW0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6RVZ, 6RW0）+ AlphaFold高质量预测（pLDDT=74.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045816, IPR050410, IPR036691, IPR005135; Pfam: PF19339, PF03372 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TOE1 | 0.836 | 0.000 | — |
| CNOT8 | 0.651 | 0.000 | — |
| PRMT8 | 0.633 | 0.629 | — |
| TATDN3 | 0.633 | 0.000 | — |
| CNOT7 | 0.560 | 0.000 | — |
| BEND7 | 0.558 | 0.000 | — |
| PARN | 0.550 | 0.000 | — |
| PAPOLG | 0.543 | 0.000 | — |
| ICE2 | 0.534 | 0.000 | — |
| OTOL1 | 0.533 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MGST3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TRMT61B | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ZFC3H1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PDK1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| FAM136A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EEF1D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NAA40 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RBM4B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HNRNPLL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.4 + PDB: 6RVZ, 6RW0 | pLDDT=74.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion matrix / Nucleoplasm; 额外: Nuclear bodies, Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. ANGEL2 — RNA 2',3'-cyclic phosphatase ANGEL2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小544 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VTE6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174606-ANGEL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANGEL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VTE6
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 01:51:38

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000174606-ANGEL2/subcellular

![](https://images.proteinatlas.org/30795/1792_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/30795/1792_B11_4_red_green.jpg)
![](https://images.proteinatlas.org/30795/1838_B11_31_red_green.jpg)
![](https://images.proteinatlas.org/30795/1838_B11_32_red_green.jpg)
![](https://images.proteinatlas.org/30795/1893_J21_21_cr5bbdf4b7c361a_red_green.jpg)
![](https://images.proteinatlas.org/30795/1893_J21_2_cr5bbdf4b7c30d8_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5VTE6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
