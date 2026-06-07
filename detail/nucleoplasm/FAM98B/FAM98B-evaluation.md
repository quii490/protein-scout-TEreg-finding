---
type: protein-evaluation
gene: "FAM98B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM98B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM98B |
| 蛋白名称 | tRNA-splicing ligase complex subunit FAM98B |
| 蛋白大小 | 433 aa / 45.5 kDa |
| UniProt ID | Q52LJ0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 433 aa / 45.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018797; Pfam: PF10239 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- tRNA-splicing ligase complex (GO:0072669)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Polyglycine-mediated aggregation of FAM98B disrupts tRNA processing in GGC repeat disorders.. *Science (New York, N.Y.)*. PMID: 40674500
2. Structural and biochemical characterization of the 3'-5' tRNA splicing ligases.. *The Journal of biological chemistry*. PMID: 40220997
3. Molecular architecture of the human tRNA ligase complex.. *eLife*. PMID: 34854379
4. hCLE/C14orf166 associates with DDX1-HSPC117-FAM98B in a novel transcription-dependent shuttling RNA-transporting complex.. *PloS one*. PMID: 24608264
5. FAM98A associates with DDX1-C14orf166-FAM98B in a novel complex involved in colorectal cancer progression.. *The international journal of biochemistry & cell biology*. PMID: 28040436

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.6 |
| 高置信度残基 (pLDDT>90) 占比 | 36.0% |
| 置信残基 (pLDDT 70-90) 占比 | 27.3% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 25.9% |
| 有序区域 (pLDDT>70) 占比 | 63.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.6，有序区 63.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018797; Pfam: PF10239 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DDX1 | 0.999 | 0.843 | — |
| RTRAF | 0.999 | 0.831 | — |
| RTCB | 0.999 | 0.835 | — |
| C2orf49 | 0.998 | 0.833 | — |
| ZBTB8OS | 0.972 | 0.292 | — |
| FAM98A | 0.687 | 0.292 | — |
| HNRNPDL | 0.624 | 0.079 | — |
| PRMT1 | 0.615 | 0.297 | — |
| KHSRP | 0.585 | 0.000 | — |
| C15orf41 | 0.584 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SGK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| BCKDK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PRKAB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| N | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| Kcnma1 | psi-mi:"MI:0096"(pull down) | imex:IM-11875|pubmed:17610306 |
| eef1a1o.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.6 + PDB: 无 | pLDDT=72.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM98B — tRNA-splicing ligase complex subunit FAM98B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小433 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q52LJ0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171262-FAM98B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM98B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q52LJ0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000171262-FAM98B/subcellular

![](https://images.proteinatlas.org/8502/100_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/8502/100_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/8502/101_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/8502/101_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/8502/82_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/8502/82_C2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q52LJ0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q52LJ0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR018797; |
| Pfam | PF10239; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000171262-FAM98B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C2orf49 | Biogrid, Bioplex | true |
| DDX1 | Intact, Biogrid, Bioplex | true |
| RTCB | Biogrid, Opencell | true |
| RTRAF | Intact, Biogrid | true |
| ACE2 | Biogrid | false |
| FAM98A | Biogrid | false |
| MYC | Biogrid | false |
| PRKN | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
