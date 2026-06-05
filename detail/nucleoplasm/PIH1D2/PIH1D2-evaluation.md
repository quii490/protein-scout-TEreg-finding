---
type: protein-evaluation
gene: "PIH1D2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PIH1D2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PIH1D2 |
| 蛋白名称 | PIH1 domain-containing protein 2 |
| 蛋白大小 | 315 aa / 36.0 kDa |
| UniProt ID | Q8WWB5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Vesicles, Basal body, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 315 aa / 36.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050734, IPR012981, IPR041442; Pfam: PF08190, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Basal body, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- protein folding chaperone complex (GO:0101031)
- R2TP complex (GO:0097255)
- ribonucleoprotein complex (GO:1990904)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Omics and Male Infertility: Highlighting the Application of Transcriptomic Data.. *Life (Basel, Switzerland)*. PMID: 35207567
2. Sialyltransferase-related genes as predictive factors for therapeutic response and prognosis in cervical cancer.. *PeerJ*. PMID: 40416607
3. Genetic Nurture Effects on Type 2 Diabetes Among Chinese Han Adults: A Family-Based Design.. *Biomedicines*. PMID: 39857704
4. Transcriptomic analysis of female and male gonads in juvenile snakeskin gourami (Trichopodus pectoralis).. *Scientific reports*. PMID: 32251302
5. The RPAP3-Cterminal domain identifies R2TP-like quaternary chaperones.. *Nature communications*. PMID: 29844425

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.0 |
| 高置信度残基 (pLDDT>90) 占比 | 36.8% |
| 置信残基 (pLDDT 70-90) 占比 | 38.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 18.4% |
| 有序区域 (pLDDT>70) 占比 | 75.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.0，有序区 75.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050734, IPR012981, IPR041442; Pfam: PF08190, PF18201 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RUVBL1 | 0.972 | 0.744 | — |
| RUVBL2 | 0.956 | 0.602 | — |
| SPAG1 | 0.938 | 0.258 | — |
| RPAP3 | 0.902 | 0.175 | — |
| PIH1D3 | 0.848 | 0.071 | — |
| HSP90AB1 | 0.812 | 0.135 | — |
| DNAAF2 | 0.803 | 0.000 | — |
| PIH1D1 | 0.779 | 0.000 | — |
| DNAAF4 | 0.751 | 0.258 | — |
| PTGES3 | 0.686 | 0.058 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| E9PD82 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| IGF2BP3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| EIF4A2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| ITGB3BP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| GFAP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| KRTAP12-4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP12-2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DPH3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| COMMD3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ANKRD11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.0 + PDB: 无 | pLDDT=78.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Vesicles, Basal body, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PIH1D2 — PIH1 domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小315 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WWB5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150773-PIH1D2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PIH1D2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WWB5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000150773-PIH1D2/subcellular

![](https://images.proteinatlas.org/39496/2242_G5_12_red_green.jpg)
![](https://images.proteinatlas.org/39496/2242_G5_34_red_green.jpg)
![](https://images.proteinatlas.org/39496/2243_F4_37_red_green.jpg)
![](https://images.proteinatlas.org/39496/2243_F4_45_red_green.jpg)
![](https://images.proteinatlas.org/39496/2244_F5_44_red_green.jpg)
![](https://images.proteinatlas.org/39496/2244_F5_55_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WWB5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
