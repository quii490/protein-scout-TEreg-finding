---
type: protein-evaluation
gene: "PCMTD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PCMTD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PCMTD1 |
| 蛋白名称 | Protein-L-isoaspartate O-methyltransferase domain-containing protein 1 |
| 蛋白大小 | 357 aa / 40.7 kDa |
| UniProt ID | Q96MG8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nucleoplasm; UniProt: Cytoplasm; Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 357 aa / 40.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=84.2; PDB: 9OMA, 9OMF |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000682, IPR029063; Pfam: PF01135 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm; Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cul5-RING ubiquitin ligase complex (GO:0031466)
- cytoplasm (GO:0005737)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 37 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of RNF213 as a susceptibility gene for moyamoya disease and its possible role in vascular development.. *PloS one*. PMID: 21799892
2. Human Protein-l-isoaspartate O-Methyltransferase Domain-Containing Protein 1 (PCMTD1) Associates with Cullin-RING Ligase Proteins.. *Biochemistry*. PMID: 35486881
3. Advances in glaucoma genetics.. *Progress in brain research*. PMID: 26497787
4. Structural basis for L-isoaspartyl-containing protein recognition by the human PCMTD1 cullin-RING E3 ubiquitin ligase.. *The Journal of biological chemistry*. PMID: 40975169
5. Structural basis for L-isoaspartyl-containing protein recognition by the PCMTD1 cullin-RING E3 ubiquitin ligase.. *bioRxiv : the preprint server for biology*. PMID: 40475564

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.2 |
| 高置信度残基 (pLDDT>90) 占比 | 68.9% |
| 置信残基 (pLDDT 70-90) 占比 | 10.4% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 15.7% |
| 有序区域 (pLDDT>70) 占比 | 79.3% |
| 可用 PDB 条目 | 9OMA, 9OMF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（9OMA, 9OMF）+ AlphaFold高质量预测（pLDDT=84.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000682, IPR029063; Pfam: PF01135 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLEKHA7 | 0.728 | 0.000 | — |
| ST18 | 0.605 | 0.000 | — |
| FAM102A | 0.601 | 0.000 | — |
| COL11A1 | 0.596 | 0.000 | — |
| CUL5 | 0.578 | 0.521 | — |
| DPM2 | 0.573 | 0.000 | — |
| EPDR1 | 0.571 | 0.000 | — |
| C10orf53 | 0.519 | 0.000 | — |
| WDYHV1 | 0.475 | 0.000 | — |
| PUS7 | 0.455 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Invs | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Iqcb1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| SCHIP1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| Tipin | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| - | psi-mi:"MI:0096"(pull down) | pubmed:31964889|imex:IM-27520 |
| RPS14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SEPTIN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MRPS11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.2 + PDB: 9OMA, 9OMF | pLDDT=84.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Membrane / Plasma membrane; 额外: Nucleoplasm | 一致 |
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
1. PCMTD1 — Protein-L-isoaspartate O-methyltransferase domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小357 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96MG8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168300-PCMTD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCMTD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96MG8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000168300-PCMTD1/subcellular

![](https://images.proteinatlas.org/61444/1385_B7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61444/1385_B7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/61444/1394_B7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/61444/1394_B7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/61444/1591_H8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61444/1591_H8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96MG8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
