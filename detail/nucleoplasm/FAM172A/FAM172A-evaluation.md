---
type: protein-evaluation
gene: "FAM172A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM172A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM172A / C5orf21, FAM172A |
| 蛋白名称 | Cotranscriptional regulator ARB2A |
| 蛋白大小 | 416 aa / 48.0 kDa |
| UniProt ID | Q8WUF8 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM172A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM172A/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm; Endoplasmic reticulum |
| 蛋白大小 | 10/10 | ×1 | 10 | 416 aa / 48.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029058, IPR048263, IPR053858; Pfam: PF22749 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Endoplasmic reticulum | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C5orf21, FAM172A |

**关键文献**:
1. The CHARGE syndrome-associated protein FAM172A controls AGO2 nuclear import.. *Life science alliance*. PMID: 37221016
2. FAM172A deletion aggravates high fat diet-induced MASLD via the eIF2α-ATF4-FGF21 loop.. *Life sciences*. PMID: 40425140
3. Deletion of Fam172a accelerates advanced atherosclerosis and induces plaque instability.. *Atherosclerosis*. PMID: 34425526
4. [Effect of FAM172A protein on apoptosis and proliferation in HEK293 cells].. *Zhonghua yi xue za zhi*. PMID: 21092515
5. FAM172A modulates apoptosis and proliferation of colon cancer cells via STAT1 binding to its promoter.. *Oncology reports*. PMID: 26676844

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.2 |
| 高置信度残基 (pLDDT>90) 占比 | 66.1% |
| 置信残基 (pLDDT 70-90) 占比 | 8.2% |
| 中等置信 (pLDDT 50-70) 占比 | 13.0% |
| 低置信 (pLDDT<50) 占比 | 12.7% |
| 有序区域 (pLDDT>70) 占比 | 74.3% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM172A/FAM172A-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=84.2，有序区 74.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029058, IPR048263, IPR053858; Pfam: PF22749 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLAC8L1 | 0.709 | 0.000 | — |
| POU5F2 | 0.612 | 0.000 | — |
| GRIK3 | 0.601 | 0.000 | — |
| SLF1 | 0.589 | 0.000 | — |
| NR2F1 | 0.585 | 0.000 | — |
| MCTP1 | 0.557 | 0.000 | — |
| PCYOX1 | 0.527 | 0.000 | — |
| KIAA0825 | 0.512 | 0.000 | — |
| CPPED1 | 0.486 | 0.000 | — |
| STYX | 0.451 | 0.421 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dynll1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ARB2A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MESD | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SKP1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:27705803|imex:IM-21659 |
| DNAJB9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DEFB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ATP5F1D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DHX34 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ZNF331 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TANK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.2 + PDB: 无 | pLDDT=84.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Endoplasmic reticulum / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. FAM172A — Cotranscriptional regulator ARB2A，非常新颖，仅有少数基础研究。
2. 蛋白大小416 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WUF8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113391-FAM172A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM172A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WUF8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM172A/FAM172A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WUF8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029058;IPR048263;IPR053858; |
| Pfam | PF22749; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000113391-FAM172A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DYNLL1 | Biogrid, Opencell | true |
| SKP1 | Biogrid, Bioplex | true |
| DNAJB9 | Bioplex | false |
| FBXO38 | Biogrid | false |
| MESD | Intact | false |
| STYX | Biogrid | false |
| TTC9C | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
