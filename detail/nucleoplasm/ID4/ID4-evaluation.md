---
type: protein-evaluation
gene: "ID4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ID4 — REJECTED (研究热度过高 (PubMed strict=337，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ID4 / BHLHB27 |
| 蛋白名称 | DNA-binding protein inhibitor ID-4 |
| 蛋白大小 | 161 aa / 16.6 kDa |
| UniProt ID | P47928 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 161 aa / 16.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=337 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR026052, IPR036638; Pfam: PF00010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.0/180** | |
| **归一化总分** | | | **43.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 337 |
| PubMed broad count | 568 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHB27 |

**关键文献**:
1. Menke-Hennekam syndrome; delineation of domain-specific subtypes with distinct clinical and DNA methylation profiles.. *HGG advances*. PMID: 38553851
2. Single-cell multiomic comparison of mouse and rat spermatogenesis reveals gene regulatory networks conserved for over 20 million years.. *Stem cell reports*. PMID: 40086448
3. Inhibitor of differentiation 4 (ID4): From development to cancer.. *Biochimica et biophysica acta*. PMID: 25512197
4. Inactivation of ID4 promotes a CRPC phenotype with constitutive AR activation through FKBP52.. *Molecular oncology*. PMID: 28252832
5. Exploring ID4 as a driver of aggression and a therapeutic target in triple-negative breast cancer.. *NPJ breast cancer*. PMID: 40640173

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.3 |
| 高置信度残基 (pLDDT>90) 占比 | 27.3% |
| 置信残基 (pLDDT 70-90) 占比 | 6.2% |
| 中等置信 (pLDDT 50-70) 占比 | 40.4% |
| 低置信 (pLDDT<50) 占比 | 26.1% |
| 有序区域 (pLDDT>70) 占比 | 33.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.3），有序残基占 33.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR026052, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OLIG1 | 0.959 | 0.311 | — |
| OLIG2 | 0.952 | 0.311 | — |
| TCF4 | 0.932 | 0.887 | — |
| ID2 | 0.919 | 0.628 | — |
| ASCL1 | 0.911 | 0.125 | — |
| TCF3 | 0.895 | 0.610 | — |
| MYOG | 0.809 | 0.785 | — |
| TCF12 | 0.769 | 0.473 | — |
| ID1 | 0.747 | 0.000 | — |
| EGR2 | 0.717 | 0.058 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| SRC | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| PIK3R1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| PLCG1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| Olig1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15280210 |
| Olig2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15280210 |
| NEUROG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| METTL2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.3 + PDB: 无 | pLDDT=66.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ID4 — DNA-binding protein inhibitor ID-4，研究基础较多，新颖性有限。
2. 蛋白大小161 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 337 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 337 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P47928
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172201-ID4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ID4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P47928
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000172201-ID4/subcellular

![](https://images.proteinatlas.org/75639/1829_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/75639/1829_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/75639/1901_L18_1_red_green.jpg)
![](https://images.proteinatlas.org/75639/1901_L18_5_red_green.jpg)
![](https://images.proteinatlas.org/75639/1909_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/75639/1909_A9_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P47928-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
