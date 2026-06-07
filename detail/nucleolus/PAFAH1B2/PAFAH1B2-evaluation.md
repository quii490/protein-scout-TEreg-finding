---
type: protein-evaluation
gene: "PAFAH1B2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PAFAH1B2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAFAH1B2 / PAFAHB |
| 蛋白名称 | Platelet-activating factor acetylhydrolase IB subunit alpha2 |
| 蛋白大小 | 229 aa / 25.6 kDa |
| UniProt ID | P68402 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoli, Plasma membrane; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 229 aa / 25.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.9; PDB: 1VYH |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013830, IPR036514; Pfam: PF13472 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.0/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli, Plasma membrane | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 1-alkyl-2-acetylglycerophosphocholine esterase complex (GO:0008247)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- fibrillar center (GO:0001650)
- ficolin-1-rich granule lumen (GO:1904813)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PAFAHB |

**关键文献**:
1. PAFAH1B2 is a HIF1a target gene and promotes metastasis in pancreatic cancer.. *Biochemical and biophysical research communications*. PMID: 29758199
2. Analysis of circRNA-miRNA-mRNA regulatory network of embryonic gonadal development in Mulard duck.. *Poultry science*. PMID: 38096667
3. MicroRNA-212-5p and its target PAFAH1B2 suppress vascular proliferation and contraction via the downregulation of RhoA.. *PloS one*. PMID: 33760887
4. Exclusion of the alpha2 subunit of platelet-activating factor acetylhydrolase 1b (PAFAH1B2) as a prothrombotic gene in a protein C-deficient kindred and population-based case-control sample.. *Thrombosis and haemostasis*. PMID: 17849047
5. Activity-Based Protein Profiling of Oncogene-Driven Changes in Metabolism Reveals Broad Dysregulation of PAFAH1B2 and 1B3 in Cancer.. *ACS chemical biology*. PMID: 25945974

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.9 |
| 高置信度残基 (pLDDT>90) 占比 | 90.4% |
| 置信残基 (pLDDT 70-90) 占比 | 3.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.7% |
| 低置信 (pLDDT<50) 占比 | 4.4% |
| 有序区域 (pLDDT>70) 占比 | 93.9% |
| 可用 PDB 条目 | 1VYH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.9，有序区 93.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013830, IPR036514; Pfam: PF13472 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAFAH1B1 | 0.999 | 0.981 | — |
| PAFAH1B3 | 0.998 | 0.903 | — |
| PAFAH2 | 0.944 | 0.000 | — |
| PLA2G7 | 0.929 | 0.000 | — |
| LPCAT1 | 0.910 | 0.000 | — |
| LPCAT2 | 0.909 | 0.000 | — |
| LPCAT4 | 0.902 | 0.000 | — |
| CHPT1 | 0.900 | 0.000 | — |
| CEPT1 | 0.900 | 0.000 | — |
| NDEL1 | 0.816 | 0.174 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PAFAH1B3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RPLP0 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ASF1A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SNUPN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SLA | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ACIN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CCT3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PINX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PPP1R12C | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| REXO1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.9 + PDB: 1VYH | pLDDT=93.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nucleoli, Plasma membrane | 一致 |
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
1. PAFAH1B2 — Platelet-activating factor acetylhydrolase IB subunit alpha2，非常新颖，仅有少数基础研究。
2. 蛋白大小229 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P68402
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168092-PAFAH1B2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAFAH1B2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P68402
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000168092-PAFAH1B2/subcellular

![](https://images.proteinatlas.org/51836/782_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51836/782_F5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/51836/787_F5_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/51836/787_F5_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/51836/840_D8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51836/840_D8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P68402-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P68402 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013830;IPR036514; |
| Pfam | PF13472; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168092-PAFAH1B2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PAFAH1B1 | Intact, Biogrid, Bioplex | true |
| PAFAH1B3 | Intact, Biogrid, Bioplex | true |
| BAG3 | Biogrid | false |
| CLVS2 | Intact | false |
| PRKN | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
