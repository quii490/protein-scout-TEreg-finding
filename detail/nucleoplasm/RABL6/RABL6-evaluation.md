---
type: protein-evaluation
gene: "RABL6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RABL6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RABL6 / C9orf86, PARF |
| 蛋白名称 | Rab-like protein 6 |
| 蛋白大小 | 729 aa / 79.5 kDa |
| UniProt ID | Q3YEC7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Centrosome, Cytosol; 额外: Centriolar satellite, Basal body; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 729 aa / 79.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027417, IPR040385; Pfam: PF08477 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome, Cytosol; 额外: Centriolar satellite, Basal body | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriolar satellite (GO:0034451)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 26 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf86, PARF |

**关键文献**:
1. Oncogenic RABL6A promotes NF1-associated MPNST progression in vivo.. *Neuro-oncology advances*. PMID: 35571990
2. Dissecting novel mechanisms of hepatitis B virus related hepatocellular carcinoma using meta-analysis of public data.. *World journal of gastrointestinal oncology*. PMID: 36187396
3. Etoposide-induced DNA damage affects multiple cellular pathways in addition to DNA damage response.. *Oncotarget*. PMID: 29844877
4. Androgen Receptors Act as a Tumor Suppressor Gene to Suppress Hepatocellular Carcinoma Cells Progression via miR-122-5p/RABL6 Signaling.. *Frontiers in oncology*. PMID: 34745992
5. RABL6A Regulates Schwann Cell Senescence in an RB1-Dependent Manner.. *International journal of molecular sciences*. PMID: 34065204

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.5 |
| 高置信度残基 (pLDDT>90) 占比 | 22.6% |
| 置信残基 (pLDDT 70-90) 占比 | 8.8% |
| 中等置信 (pLDDT 50-70) 占比 | 16.5% |
| 低置信 (pLDDT<50) 占比 | 52.1% |
| 有序区域 (pLDDT>70) 占比 | 31.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.5），有序残基占 31.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR040385; Pfam: PF08477 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TBRG1 | 0.774 | 0.000 | — |
| MBD3 | 0.769 | 0.000 | — |
| CCDC183 | 0.658 | 0.000 | — |
| CDKN2A | 0.654 | 0.135 | — |
| CDKN2AIP | 0.629 | 0.000 | — |
| VPS33B | 0.606 | 0.442 | — |
| VPS33A | 0.579 | 0.426 | — |
| SPINK7 | 0.579 | 0.450 | — |
| RABL3 | 0.571 | 0.000 | — |
| TRAPPC1 | 0.559 | 0.467 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MDFI | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| CALCOCO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RBPMS | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| BRME1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SPINK7 | psi-mi:"MI:0018"(two hybrid) | pubmed:12646258|imex:IM-19228 |
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| EBI-1257121 | psi-mi:"MI:0400"(affinity technology) | pubmed:19367725|imex:IM-20587 |
| NF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DLST | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.5 + PDB: 无 | pLDDT=59.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Centrosome, Cytosol; 额外: Centriolar satellite, Bas | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. RABL6 — Rab-like protein 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小729 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3YEC7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196642-RABL6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RABL6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3YEC7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (approved)。来源: https://www.proteinatlas.org/ENSG00000196642-RABL6/subcellular

![](https://images.proteinatlas.org/44037/2134_G8_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/44037/2134_G8_76_blue_red_green.jpg)
![](https://images.proteinatlas.org/44037/2165_E5_42_blue_red_green.jpg)
![](https://images.proteinatlas.org/44037/2165_E5_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/44037/2241_D10_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/44037/2241_D10_26_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3YEC7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
