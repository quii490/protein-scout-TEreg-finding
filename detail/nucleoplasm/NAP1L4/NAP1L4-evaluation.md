---
type: protein-evaluation
gene: "NAP1L4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NAP1L4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAP1L4 / NAP2 |
| 蛋白名称 | Nucleosome assembly protein 1-like 4 |
| 蛋白大小 | 375 aa / 42.8 kDa |
| UniProt ID | Q99733 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 375 aa / 42.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR037231, IPR002164; Pfam: PF00956 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Chromosome; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- dendrite (GO:0030425)
- neuronal cell body (GO:0043025)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 49 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NAP2 |

**关键文献**:
1. NAP1L4 in hepatocellular carcinoma progression and treatment from gene expression to clinical impact.. *Discover oncology*. PMID: 41258556
2. Nucleosome assembly proteins NAP1L1 and NAP1L4 modulate p53 acetylation to regulate cell fate.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 31634504
3. NAP1L1 and NAP1L4 Binding to Hypervariable Domain of Chikungunya Virus nsP3 Protein Is Bivalent and Requires Phosphorylation.. *Journal of virology*. PMID: 34076483
4. NAP1L4 inhibits porcine circovirus type 2 replication via IFN-β signaling pathway.. *Veterinary microbiology*. PMID: 32605741
5. Telomeric NAP1L4 and OSBPL5 of the KCNQ1 cluster, and the DECORIN gene are not imprinted in human trophoblast stem cells.. *PloS one*. PMID: 20644730

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.3 |
| 高置信度残基 (pLDDT>90) 占比 | 55.2% |
| 置信残基 (pLDDT 70-90) 占比 | 14.4% |
| 中等置信 (pLDDT 50-70) 占比 | 16.5% |
| 低置信 (pLDDT<50) 占比 | 13.9% |
| 有序区域 (pLDDT>70) 占比 | 69.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.3，有序区 69.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037231, IPR002164; Pfam: PF00956 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NAP1L1 | 0.927 | 0.867 | — |
| H2AZ1 | 0.844 | 0.802 | — |
| PHLDA2 | 0.813 | 0.000 | — |
| MAGED2 | 0.801 | 0.612 | — |
| H2BC21 | 0.799 | 0.547 | — |
| NPM1 | 0.751 | 0.467 | — |
| NAP1L5 | 0.746 | 0.508 | — |
| PES1 | 0.730 | 0.678 | — |
| DGKZ | 0.727 | 0.213 | — |
| H2AC8 | 0.706 | 0.691 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Iqcb1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| tat | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| MAPK13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12163|pubmed:19135240 |
| Kcnma1 | psi-mi:"MI:0096"(pull down) | imex:IM-11875|pubmed:17610306 |
| Cep78 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23075850|imex:IM-18674 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| EBI-1257123 | psi-mi:"MI:0400"(affinity technology) | pubmed:19367725|imex:IM-20587 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.3 + PDB: 无 | pLDDT=80.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NAP1L4 — Nucleosome assembly protein 1-like 4，非常新颖，仅有少数基础研究。
2. 蛋白大小375 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99733
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205531-NAP1L4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAP1L4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99733
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000205531-NAP1L4/subcellular

![](https://images.proteinatlas.org/11567/610_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/11567/610_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/11567/613_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/11567/613_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/11567/617_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/11567/617_D3_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99733-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
