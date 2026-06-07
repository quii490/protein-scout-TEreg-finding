---
type: protein-evaluation
gene: "FAM188A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM188A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM188A / C10orf97, CARP, DERP5, FAM188A |
| 蛋白名称 | Ubiquitin carboxyl-terminal hydrolase MINDY-3 |
| 蛋白大小 | 445 aa / 49.7 kDa |
| UniProt ID | Q9H8M7 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/FAM188A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/FAM188A/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear membrane; 额外: Microtubules, Primary cil; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 445 aa / 49.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.8; PDB: 8Q06 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011992, IPR025257, IPR039785; Pfam: PF13898 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane; 额外: Microtubules, Primary cilium, Primary cilium tip, Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf97, CARP, DERP5, FAM188A |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.8 |
| 高置信度残基 (pLDDT>90) 占比 | 73.0% |
| 置信残基 (pLDDT 70-90) 占比 | 16.4% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 6.7% |
| 有序区域 (pLDDT>70) 占比 | 89.4% |
| 可用 PDB 条目 | 8Q06 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/FAM188A/FAM188A-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=87.8，有序区 89.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR025257, IPR039785; Pfam: PF13898 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMEM45A | 0.868 | 0.000 | — |
| CARD6 | 0.805 | 0.000 | — |
| GHITM | 0.804 | 0.000 | — |
| TMEM9 | 0.775 | 0.000 | — |
| COPS7A | 0.772 | 0.000 | — |
| CRADD | 0.728 | 0.000 | — |
| CARD8 | 0.713 | 0.000 | — |
| CASP1 | 0.713 | 0.000 | — |
| NLRP1 | 0.665 | 0.000 | — |
| APAF1 | 0.653 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MINDY3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RFX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KIF9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRAF2 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| RBCK1 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| TRADD | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| RAD23A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TRIM49 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DAZAP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRIM49C | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.8 + PDB: 8Q06 | pLDDT=87.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear membrane; 额外: Microtubules, P | 一致 |
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
1. FAM188A — Ubiquitin carboxyl-terminal hydrolase MINDY-3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小445 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H8M7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148481-MINDY3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM188A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H8M7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/FAM188A/FAM188A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H8M7 |
| SMART | SM01174; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011992;IPR025257;IPR039785; |
| Pfam | PF13898; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000148481-MINDY3/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
