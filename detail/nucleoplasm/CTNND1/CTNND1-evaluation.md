---
type: protein-evaluation
gene: "CTNND1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CTNND1 — REJECTED (研究热度过高 (PubMed strict=128，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTNND1 / KIAA0384 |
| 蛋白名称 | Catenin delta-1 |
| 蛋白大小 | 968 aa / 108.2 kDa |
| UniProt ID | O60716 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Plasma membrane; 额外: Basal body; UniProt: Cell junction, adherens junction; Cytoplasm; Nucleus; Cell m |
| 蛋白大小 | 8/10 | x1 | 8 | 968 aa / 108.2 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=128 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=65.1; PDB: 3L6X, 3L6Y |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR011989, IPR016024, IPR000225, IPR028435; Pfam:  |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.0/180** | |
| **归一化总分** | | | **43.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Basal body | Enhanced |
| UniProt | Cell junction, adherens junction; Cytoplasm; Nucleus; Cell membrane; Cell junction; Nucleus; Nucleus... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- catenin complex (GO:0016342)
- cell-cell junction (GO:0005911)
- ciliary basal body (GO:0036064)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- midbody (GO:0030496)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 128 |
| PubMed broad count | 497 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0384 |

**关键文献**:
1. Genome-wide analyses identify 30 loci associated with obsessive-compulsive disorder.. *Nature genetics*. PMID: 40360802
2. Genome-wide analyses identify 30 loci associated with obsessive-compulsive disorder.. *medRxiv : the preprint server for health sciences*. PMID: 38712091
3. Functional analysis of ESRP1/2 gene variants and CTNND1 isoforms in orofacial cleft pathogenesis.. *Communications biology*. PMID: 39179789
4. CTNND1 is involved in germline predisposition to early-onset gastric cancer by affecting cell-to-cell interactions.. *Gastric cancer : official journal of the International Gastric Cancer Association and the Japanese Gastric Cancer Association*. PMID: 38796558
5. Cross-ancestry genome-wide association study and systems-level integrative analyses implicate new risk genes and therapeutic targets for depression.. *Nature human behaviour*. PMID: 39994458

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.1 |
| 高置信度残基 (pLDDT>90) 占比 | 40.3% |
| 置信残基 (pLDDT 70-90) 占比 | 9.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 46.9% |
| 有序区域 (pLDDT>70) 占比 | 49.6% |
| 可用 PDB 条目 | 3L6X, 3L6Y |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.1），有序残基占 49.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR000225, IPR028435; Pfam: PF00514 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDH1 | 0.999 | 0.930 | — |
| CDH17 | 0.999 | 0.134 | — |
| ZBTB33 | 0.999 | 0.878 | — |
| CDH2 | 0.999 | 0.877 | — |
| CTNNB1 | 0.999 | 0.834 | — |
| CDH5 | 0.999 | 0.690 | — |
| AFDN | 0.998 | 0.082 | — |
| CTNNA1 | 0.998 | 0.454 | — |
| EGFR | 0.994 | 0.835 | — |
| RHOA | 0.986 | 0.243 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.1 + PDB: 3L6X, 3L6Y | pLDDT=65.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell junction, adherens junction; Cytoplasm; Nucle / Plasma membrane; 额外: Basal body | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CTNND1 -- Catenin delta-1，研究基础较多，新颖性有限。
2. 蛋白大小968 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 128 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 128 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60716
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198561-CTNND1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTNND1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60716
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60716-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60716 |
| SMART | SM00185; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011989;IPR016024;IPR000225;IPR028435; |
| Pfam | PF00514; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198561-CTNND1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDH2 | Intact, Biogrid | true |
| CTNNB1 | Biogrid, Opencell | true |
| EGFR | Intact, Biogrid | true |
| PLPP3 | Intact, Biogrid | true |
| PTPRJ | Intact, Biogrid | true |
| ZBTB33 | Intact, Biogrid | true |
| ANLN | Biogrid | false |
| CCNF | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
