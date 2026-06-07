---
type: protein-evaluation
gene: "PNPLA3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PNPLA3 — REJECTED (研究热度过高 (PubMed strict=865，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PNPLA3 / ADPN, C22orf20 |
| 蛋白名称 | 1-acylglycerol-3-phosphate O-acyltransferase PNPLA3 |
| 蛋白大小 | 481 aa / 52.9 kDa |
| UniProt ID | Q9NST1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; 额外: Mitochondria, Cytosol; UniProt: Membrane; Lipid droplet |
| 蛋白大小 | 10/10 | ×1 | 10 | 481 aa / 52.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=865 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016035, IPR039185, IPR033562, IPR002641; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **71.5/180** | |
| **归一化总分** | | | **39.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Mitochondria, Cytosol | Approved |
| UniProt | Membrane; Lipid droplet | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endoplasmic reticulum membrane (GO:0005789)
- lipid droplet (GO:0005811)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 865 |
| PubMed broad count | 1626 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ADPN, C22orf20 |

**关键文献**:
1. Adipocyte lipolysis: from molecular mechanisms of regulation to disease and therapeutics.. *The Biochemical journal*. PMID: 32168372
2. PNPLA3(148M) is a gain-of-function mutation that promotes hepatic steatosis by inhibiting ATGL-mediated triglyceride hydrolysis.. *Journal of hepatology*. PMID: 39550037
3. TM6SF2 E167K variant decreases PNPLA3-mediated PUFA transfer to promote hepatic steatosis and injury in MASLD.. *Clinical and molecular hepatology*. PMID: 39054606
4. AZD2693, a PNPLA3 antisense oligonucleotide, for the treatment of MASH in 148M homozygous participants: Two randomized phase I trials.. *Journal of hepatology*. PMID: 39798707
5. The fatty liver disease-causing protein PNPLA3-I148M alters lipid droplet-Golgi dynamics.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38657050

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.4 |
| 高置信度残基 (pLDDT>90) 占比 | 30.6% |
| 置信残基 (pLDDT 70-90) 占比 | 32.2% |
| 中等置信 (pLDDT 50-70) 占比 | 12.7% |
| 低置信 (pLDDT<50) 占比 | 24.5% |
| 有序区域 (pLDDT>70) 占比 | 62.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.4，有序区 62.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016035, IPR039185, IPR033562, IPR002641; Pfam: PF01734 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LIPC | 0.956 | 0.000 | — |
| PNLIP | 0.948 | 0.000 | — |
| LPL | 0.940 | 0.000 | — |
| PLPP5 | 0.940 | 0.000 | — |
| PLPP4 | 0.938 | 0.000 | — |
| MGLL | 0.938 | 0.000 | — |
| GPT | 0.929 | 0.000 | — |
| SAMM50 | 0.928 | 0.000 | — |
| LIPG | 0.924 | 0.000 | — |
| LIPF | 0.922 | 0.101 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AKT2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SNX27 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| AHNAK | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SLC27A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PEX14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.4 + PDB: 无 | pLDDT=71.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Lipid droplet / Nucleoli; 额外: Mitochondria, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

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
1. PNPLA3 — 1-acylglycerol-3-phosphate O-acyltransferase PNPLA3，研究基础较多，新颖性有限。
2. 蛋白大小481 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 865 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 865 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NST1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100344-PNPLA3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PNPLA3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NST1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NST1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NST1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 10..179; /note="PNPLA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01161" |
| InterPro | IPR016035;IPR039185;IPR033562;IPR002641; |
| Pfam | PF01734; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000100344-PNPLA3/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
