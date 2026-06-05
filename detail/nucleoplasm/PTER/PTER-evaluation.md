---
type: protein-evaluation
gene: "PTER"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PTER — REJECTED (研究热度过高 (PubMed strict=478，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PTER |
| 蛋白名称 | N-acetyltaurine hydrolase |
| 蛋白大小 | 349 aa / 39.0 kDa |
| UniProt ID | Q96BW5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 349 aa / 39.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=478 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=97.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017947, IPR032466, IPR001559; Pfam: PF02126 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 478 |
| PubMed broad count | 1516 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. PTER is a N-acetyltaurine hydrolase that regulates feeding and obesity.. *Nature*. PMID: 39112712
2. Genetic Creutzfeldt-Jakob disease.. *Handbook of clinical neurology*. PMID: 29887139
3. The taurine transporter gene and its role in renal development.. *Amino acids*. PMID: 11140355
4. Phosphotriesterase-related protein as a novel prognostic predictor for hepatocellular carcinoma patients.. *Chinese clinical oncology*. PMID: 37699602
5. Clinical and molecular genetic characterization of two siblings with trisomy 2p24.3-pter and monosomy 5p14.3-pter.. *American journal of medical genetics. Part A*. PMID: 28599099

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.6 |
| 高置信度残基 (pLDDT>90) 占比 | 98.6% |
| 置信残基 (pLDDT 70-90) 占比 | 1.1% |
| 中等置信 (pLDDT 50-70) 占比 | 0.3% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=97.6，有序区 99.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017947, IPR032466, IPR001559; Pfam: PF02126 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POP5 | 0.657 | 0.000 | — |
| TMEM18 | 0.618 | 0.000 | — |
| KCTD15 | 0.613 | 0.000 | — |
| GNPDA2 | 0.609 | 0.000 | — |
| SEC16B | 0.603 | 0.000 | — |
| FAIM2 | 0.580 | 0.000 | — |
| SH2B1 | 0.580 | 0.000 | — |
| MTCH2 | 0.577 | 0.000 | — |
| POP7 | 0.558 | 0.000 | — |
| NEGR1 | 0.545 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257123 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-20587 |
| TMEM51 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GSC2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KHDRBS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| S1PR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NPDC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MRM3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HYAL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TEKT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LIPH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.6 + PDB: 无 | pLDDT=97.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PTER — N-acetyltaurine hydrolase，研究基础较多，新颖性有限。
2. 蛋白大小349 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 478 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 478 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96BW5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165983-PTER/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PTER
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96BW5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000165983-PTER/subcellular

![](https://images.proteinatlas.org/38045/437_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/38045/437_B7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96BW5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
