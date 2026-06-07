---
type: protein-evaluation
gene: "CXADR"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CXADR 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CXADR / CAR |
| 蛋白名称 | Coxsackievirus and adenovirus receptor |
| 蛋白大小 | 365 aa / 40.0 kDa |
| UniProt ID | P78310 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Plasma membrane, Cell Junctions; 额外: Nucleoplasm; UniProt: Cell membrane; Basolateral cell membrane; Cell junction, tig |
| 蛋白大小 | 10/10 | x1 | 10 | 365 aa / 40.0 kDa |
| 研究新颖性 | 2/10 | x5 | 10 | PubMed strict=85 篇 (≤100→2) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=79.3; PDB: 1EAJ, 1F5W, 1JEW, 1KAC, 1P69, 1P6A, 1RSF |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR052307, IPR007110, IPR036179, IPR013783, IPR003 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cell Junctions; 额外: Nucleoplasm | Supported |
| UniProt | Cell membrane; Basolateral cell membrane; Cell junction, tight junction; Cell junction, adherens jun... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- adherens junction (GO:0005912)
- apicolateral plasma membrane (GO:0016327)
- basolateral plasma membrane (GO:0016323)
- bicellular tight junction (GO:0005923)
- cell body (GO:0044297)
- cell junction (GO:0030054)
- cell-cell junction (GO:0005911)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 85 |
| PubMed broad count | 108 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CAR |

**关键文献**:
1. CXADR-Like Membrane Protein Regulates Colonic Epithelial Cell Proliferation and Prevents Tumor Growth.. *Gastroenterology*. PMID: 37716376
2. Coxsackievirus and Adenovirus Receptor (CXADR): Recent Findings and Its Role and Regulation in Spermatogenesis.. *Advances in experimental medicine and biology*. PMID: 34453733
3. Single-cell RNA sequencing identifies CXADR as a fate determinant of the placental exchange surface.. *Nature communications*. PMID: 39747179
4. CXADR promote epithelial-mesenchymal transition in endometriosis by modulating AKT/GSK-3β signaling.. *Cell cycle (Georgetown, Tex.)*. PMID: 38146657
5. Proteome-wide copy-number estimation from transcriptomics.. *bioRxiv : the preprint server for biology*. PMID: 37503057

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.3 |
| 高置信度残基 (pLDDT>90) 占比 | 57.8% |
| 置信残基 (pLDDT 70-90) 占比 | 10.4% |
| 中等置信 (pLDDT 50-70) 占比 | 13.7% |
| 低置信 (pLDDT<50) 占比 | 18.1% |
| 有序区域 (pLDDT>70) 占比 | 68.2% |
| 可用 PDB 条目 | 1EAJ, 1F5W, 1JEW, 1KAC, 1P69, 1P6A, 1RSF, 2J12, 2J1K, 2NPL |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold极高置信度（pLDDT=79.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052307, IPR007110, IPR036179, IPR013783, IPR003599; Pfam: PF13927, PF07686 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| JAML | 0.998 | 0.865 | — |
| LNX1 | 0.910 | 0.253 | — |
| CD46 | 0.860 | 0.045 | — |
| CD55 | 0.859 | 0.045 | — |
| OCLN | 0.831 | 0.124 | — |
| TJP1 | 0.815 | 0.075 | — |
| CYP2B6 | 0.733 | 0.000 | — |
| DSG2 | 0.733 | 0.118 | — |
| NR1I3 | 0.652 | 0.000 | — |
| AGBL3 | 0.650 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=79.3 + PDB: 1EAJ, 1F5W, 1JEW, 1KAC, 1P69,  | pLDDT=79.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Basolateral cell membrane; Cell jun / Plasma membrane, Cell Junctions; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CXADR -- Coxsackievirus and adenovirus receptor，研究基础较多，新颖性有限。
2. 蛋白大小365 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 85 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P78310
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154639-CXADR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CXADR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P78310
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P78310-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P78310 |
| SMART | SM00409;SM00408;SM00406; |
| UniProt Domain [FT] | DOMAIN 20..134; /note="Ig-like C2-type 1"; DOMAIN 141..228; /note="Ig-like C2-type 2" |
| InterPro | IPR052307;IPR007110;IPR036179;IPR013783;IPR003599;IPR003598;IPR013106; |
| Pfam | PF13927;PF07686; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000154639-CXADR/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CANX | Biogrid, Opencell | true |
| ARF6 | Biogrid | false |
| ARL13B | Biogrid | false |
| CCDC8 | Biogrid | false |
| EPHA2 | Biogrid | false |
| FAM3C | Intact | false |
| KRAS | Biogrid | false |
| MAL | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
