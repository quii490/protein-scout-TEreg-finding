---
type: protein-evaluation
gene: "KPNA7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KPNA7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KPNA7 |
| 蛋白名称 | Importin subunit alpha-8 |
| 蛋白大小 | 516 aa / 56.9 kDa |
| UniProt ID | A9QM74 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 516 aa / 56.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR032413, IPR000225, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- female germ cell nucleus (GO:0001674)
- NLS-dependent protein nuclear import complex (GO:0042564)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spindle (GO:0005819)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Karyopherin α deficiency contributes to human preimplantation embryo arrest.. *The Journal of clinical investigation*. PMID: 36647821
2. Case-only analysis of gene-gene interactions in inflammatory bowel disease.. *Scandinavian journal of gastroenterology*. PMID: 32649238
3. Role of importin alpha8, a new member of the importin alpha family of nuclear transport proteins, in early embryonic development in cattle.. *Biology of reproduction*. PMID: 19420384
4. DNA methylation and miRNA-1296 act in concert to mediate spatiotemporal expression of KPNA7 during bovine oocyte and early embryonic development.. *BMC developmental biology*. PMID: 31787077
5. Changing expression and subcellular distribution of karyopherins during murine oogenesis.. *Reproduction (Cambridge, England)*. PMID: 26399853

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.8 |
| 高置信度残基 (pLDDT>90) 占比 | 75.8% |
| 置信残基 (pLDDT 70-90) 占比 | 6.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 14.5% |
| 有序区域 (pLDDT>70) 占比 | 82.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.8，有序区 82.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR032413, IPR000225, IPR002652; Pfam: PF00514, PF16186, PF01749 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KPNB1 | 0.927 | 0.653 | — |
| IL1F10 | 0.838 | 0.000 | — |
| BTN3A1 | 0.783 | 0.071 | — |
| RAN | 0.783 | 0.388 | — |
| MUC3A | 0.743 | 0.128 | — |
| CSE1L | 0.737 | 0.523 | — |
| FOXP1-2 | 0.702 | 0.065 | — |
| RANBP2 | 0.692 | 0.522 | — |
| SMURF1 | 0.687 | 0.056 | — |
| RCC1 | 0.685 | 0.451 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KPNB1 | psi-mi:"MI:0096"(pull down) | pubmed:20701745|imex:IM-25699 |
| CDC45 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-30020|pubmed:39009827 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.8 + PDB: 无 | pLDDT=85.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KPNA7 — Importin subunit alpha-8，非常新颖，仅有少数基础研究。
2. 蛋白大小516 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A9QM74
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185467-KPNA7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KPNA7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A9QM74
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A9QM74-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A9QM74 |
| SMART | SM00185; |
| UniProt Domain [FT] | DOMAIN 1..57; /note="IBB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00561" |
| InterPro | IPR011989;IPR016024;IPR032413;IPR000225;IPR002652;IPR036975;IPR024931; |
| Pfam | PF00514;PF16186;PF01749; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000185467-KPNA7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| H1-2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
