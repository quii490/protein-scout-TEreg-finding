---
type: protein-evaluation
gene: "NFATC4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NFATC4 — REJECTED (研究热度过高 (PubMed strict=178，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NFATC4 / NFAT3 |
| 蛋白名称 | Nuclear factor of activated T-cells, cytoplasmic 4 |
| 蛋白大小 | 902 aa / 95.4 kDa |
| UniProt ID | Q14934 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 902 aa / 95.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=178 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.6; PDB: 2YRP |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013783, IPR014756, IPR002909, IPR008366, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.5/180** | |
| **归一化总分** | | | **43.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 178 |
| PubMed broad count | 317 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NFAT3 |

**关键文献**:
1. The genomic landscape of pediatric acute lymphoblastic leukemia.. *Nature genetics*. PMID: 36050548
2. Novel cell lines derived from adult human ventricular cardiomyocytes.. *Journal of molecular and cellular cardiology*. PMID: 15913645
3. Therapeutic Inhibition of LincRNA-p21 Protects Against Cardiac Hypertrophy.. *Circulation research*. PMID: 38864216
4. Correlation of inflammatory markers and NFATC4 gene expression among subjects with prediabetes.. *Journal of cardiovascular and thoracic research*. PMID: 40027364
5. TRIM24 regulates chromatin remodeling and calcium dynamics in cardiomyocytes.. *Cell communication and signaling : CCS*. PMID: 40598158

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.6 |
| 高置信度残基 (pLDDT>90) 占比 | 25.2% |
| 置信残基 (pLDDT 70-90) 占比 | 7.1% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 57.9% |
| 有序区域 (pLDDT>70) 占比 | 32.3% |
| 可用 PDB 条目 | 2YRP |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.6），有序残基占 32.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013783, IPR014756, IPR002909, IPR008366, IPR008967; Pfam: PF16179, PF00554 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPP3R1 | 0.985 | 0.000 | — |
| GATA4 | 0.984 | 0.000 | — |
| PPP3CA | 0.969 | 0.480 | — |
| PPP3CC | 0.953 | 0.422 | — |
| PPP3CB | 0.941 | 0.000 | — |
| MEF2A | 0.933 | 0.000 | — |
| NFATC2 | 0.926 | 0.068 | — |
| SRF | 0.924 | 0.000 | — |
| MEF2D | 0.921 | 0.000 | — |
| SOX10 | 0.921 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GPR22 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| JUP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NR1I2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CCNG1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| MAPK14 | psi-mi:"MI:0813"(proximity ligation assay) | pubmed:25241761|imex:IM-18707 |
| NLGN3 | psi-mi:"MI:0018"(two hybrid) | pubmed:25464930|imex:IM-26157 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| PPP3CA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP3CC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ANKRD28 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:24255178|imex:IM-21541 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.6 + PDB: 2YRP | pLDDT=58.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear speckles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NFATC4 — Nuclear factor of activated T-cells, cytoplasmic 4，研究基础较多，新颖性有限。
2. 蛋白大小902 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 178 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 178 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14934
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100968-NFATC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NFATC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14934
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000100968-NFATC4/subcellular

![](https://images.proteinatlas.org/76526/1709_G5_12_cr5809b81b09cf5_blue_red_green.jpg)
![](https://images.proteinatlas.org/76526/1709_G5_4_cr5809b8128e580_blue_red_green.jpg)
![](https://images.proteinatlas.org/76526/1749_F11_13_cr58049cb964aa2_blue_red_green.jpg)
![](https://images.proteinatlas.org/76526/1749_F11_18_cr58049cc2dfa47_blue_red_green.jpg)
![](https://images.proteinatlas.org/76526/1751_G7_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/76526/1751_G7_34_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14934-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
