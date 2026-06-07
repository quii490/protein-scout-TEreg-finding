---
type: protein-evaluation
gene: "EYA1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EYA1 — REJECTED (研究热度过高 (PubMed strict=326，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EYA1 |
| 蛋白名称 | Protein phosphatase EYA1 |
| 蛋白大小 | 592 aa / 64.6 kDa |
| UniProt ID | Q99502 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; 额外: Vesicles, Primary cilium; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 592 aa / 64.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=326 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028472, IPR006545, IPR042577, IPR038102; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Vesicles, Primary cilium | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-DNA complex (GO:0032993)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 326 |
| PubMed broad count | 507 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Branchio-oto-renal syndrome.. *American journal of medical genetics. Part A*. PMID: 17238186
2. Branchiootorenal Spectrum Disorder.. **. PMID: 20301554
3. Branchio-oto-renal syndrome.. *Journal of nephrology*. PMID: 14696767
4. Branchio-oto-renal syndrome.. *Journal of communication disorders*. PMID: 9777487
5. The transcriptional coactivator Eya1 exerts transcriptional repressive activity by interacting with REST corepressors and REST-binding sequences to maintain nephron progenitor identity.. *Nucleic acids research*. PMID: 36130284

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.7 |
| 高置信度残基 (pLDDT>90) 占比 | 42.6% |
| 置信残基 (pLDDT 70-90) 占比 | 2.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 50.7% |
| 有序区域 (pLDDT>70) 占比 | 45.0% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.7），有序残基占 45.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028472, IPR006545, IPR042577, IPR038102; Pfam: PF00702 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SIX1 | 0.997 | 0.835 | — |
| SIX2 | 0.972 | 0.670 | — |
| TLX1 | 0.948 | 0.059 | — |
| SIX5 | 0.942 | 0.474 | — |
| DACH1 | 0.942 | 0.300 | — |
| SIX4 | 0.882 | 0.483 | — |
| PAX2 | 0.872 | 0.000 | — |
| PAX3 | 0.860 | 0.071 | — |
| SALL1 | 0.839 | 0.000 | — |
| H2AX | 0.805 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Sharpin | psi-mi:"MI:0018"(two hybrid) | imex:IM-17347|pubmed:20956555 |
| Rbck1 | psi-mi:"MI:0096"(pull down) | imex:IM-17347|pubmed:20956555 |
| Six2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-17347|pubmed:20956555 |
| HSP90B1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SIX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PTPN9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CERT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SIX5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CACNB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.7 + PDB: 无 | pLDDT=65.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Nuclear bodies; 额外: Vesicles, Primary | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

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
1. EYA1 — Protein phosphatase EYA1，研究基础较多，新颖性有限。
2. 蛋白大小592 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 326 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 326 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99502
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104313-EYA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EYA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99502
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99502-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99502 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028472;IPR006545;IPR042577;IPR038102; |
| Pfam | PF00702; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000104313-EYA1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SIX1 | Intact, Biogrid | true |
| FBXW7 | Biogrid | false |
| GSK3B | Biogrid | false |
| H2AX | Biogrid | false |
| MYC | Biogrid | false |
| PLK1 | Biogrid | false |
| SIX2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
