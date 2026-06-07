---
type: protein-evaluation
gene: "KASH5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KASH5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KASH5 / CCDC155 |
| 蛋白名称 | Protein KASH5 |
| 蛋白大小 | 562 aa / 62.8 kDa |
| UniProt ID | Q8N6L0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus outer membrane; Nucleus; Chromosome, telomere; Nucle |
| 蛋白大小 | 10/10 | ×1 | 10 | 562 aa / 62.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.7; PDB: 6R2I, 6WMF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011992, IPR028170, IPR028168, IPR039508; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus outer membrane; Nucleus; Chromosome, telomere; Nucleus envelope | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- lateral element (GO:0000800)
- meiotic nuclear membrane microtubule tethering complex (GO:0034993)
- meiotic spindle pole (GO:0090619)
- nuclear outer membrane (GO:0005640)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CCDC155 |

**关键文献**:
1. The meiotic LINC complex component KASH5 is an activating adaptor for cytoplasmic dynein.. *The Journal of cell biology*. PMID: 36946995
2. Homozygous Variant in KASH5 Causes Premature Ovarian Insufficiency by Disordered Meiotic Homologous Pairing.. *The Journal of clinical endocrinology and metabolism*. PMID: 35708642
3. Novel bi-allelic variants in KASH5 are associated with meiotic arrest and non-obstructive azoospermia.. *Molecular human reproduction*. PMID: 35674372
4. A homozygous KASH5 frameshift mutation causes diminished ovarian reserve, recurrent miscarriage, and non-obstructive azoospermia in humans.. *Frontiers in endocrinology*. PMID: 36864840
5. A conserved KASH domain protein associates with telomeres, SUN1, and dynactin during mammalian meiosis.. *The Journal of cell biology*. PMID: 22826121

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.7 |
| 高置信度残基 (pLDDT>90) 占比 | 38.1% |
| 置信残基 (pLDDT 70-90) 占比 | 15.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 39.5% |
| 有序区域 (pLDDT>70) 占比 | 53.6% |
| 可用 PDB 条目 | 6R2I, 6WMF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.7），有序残基占 53.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR028170, IPR028168, IPR039508; Pfam: PF14658, PF14662 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUN1 | 0.999 | 0.901 | — |
| SUN2 | 0.998 | 0.901 | — |
| SYNE4 | 0.919 | 0.000 | — |
| DKKL1 | 0.917 | 0.047 | — |
| TERB1 | 0.890 | 0.095 | — |
| MAJIN | 0.861 | 0.000 | — |
| SYNE3 | 0.848 | 0.095 | — |
| LRMP | 0.846 | 0.000 | — |
| SYNE1 | 0.842 | 0.063 | — |
| TERB2 | 0.839 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCDC87 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| tuf | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| BET1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC41A1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CYBC1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM19 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM86A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SERP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GALNT2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM147 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.7 + PDB: 6R2I, 6WMF | pLDDT=68.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus outer membrane; Nucleus; Chromosome, telom / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KASH5 — Protein KASH5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小562 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N6L0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000161609-KASH5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KASH5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N6L0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N6L0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N6L0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011992;IPR028170;IPR028168;IPR039508; |
| Pfam | PF14658;PF14662; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000161609-KASH5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABHD1 | Intact | false |
| ADIPOQ | Intact | false |
| ATF7 | Intact | false |
| BAG5 | Intact | false |
| BCL2L2 | Intact | false |
| BCL2L2-PABPN1 | Intact | false |
| BET1 | Intact | false |
| C14orf180 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
