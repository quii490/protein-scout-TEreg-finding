---
type: protein-evaluation
gene: "DOCK4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DOCK4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOCK4 / KIAA0716 |
| 蛋白名称 | Dedicator of cytokinesis protein 4 |
| 蛋白大小 | 1966 aa / 225.2 kDa |
| UniProt ID | Q8N1I0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Plasma membrane; 额外: Golgi apparatus, Cytosol; UniProt: Cell membrane; Cell projection; Cytoplasm, cytosol |
| 蛋白大小 | 5/10 | ×1 | 5 | 1966 aa / 225.2 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=88 篇 (≤100→2) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037811, IPR027007, IPR035892, IPR037014, IPR026 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Plasma membrane; 额外: Golgi apparatus, Cytosol | Approved |
| UniProt | Cell membrane; Cell projection; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- glutamatergic synapse (GO:0098978)
- Golgi apparatus (GO:0005794)
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- plasma membrane (GO:0005886)
- postsynapse (GO:0098794)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 88 |
| PubMed broad count | 135 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0716 |

**关键文献**:
1. Transcytosis of LDL Across Arterial Endothelium: Mechanisms and Therapeutic Targets.. *Arteriosclerosis, thrombosis, and vascular biology*. PMID: 40013359
2. Histone lactylation regulates DOCK4 to control heat nociception and supports Dynein-mediated Nav1.7 trafficking.. *Nature communications*. PMID: 40759894
3. DOCK4 regulates ghrelin production in gastric X/A-like cells.. *Journal of endocrinological investigation*. PMID: 35302184
4. DOCK4 is a Novel Prognostic Biomarker and Correlated with Immune Infiltrates in Colon Adenocarcinoma.. *Combinatorial chemistry & high throughput screening*. PMID: 37702239
5. TMOD2 and DOCK4 as Novel Gut Microbiota-Associated Biomarkers for Colorectal Adenoma: Integrated Transcriptomic Analysis and Therapeutic Target Identification.. *Mediators of inflammation*. PMID: 41378121

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.3 |
| 高置信度残基 (pLDDT>90) 占比 | 35.5% |
| 置信残基 (pLDDT 70-90) 占比 | 39.3% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 20.8% |
| 有序区域 (pLDDT>70) 占比 | 74.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.3，有序区 74.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037811, IPR027007, IPR035892, IPR037014, IPR026791; Pfam: PF06920, PF20422, PF20421 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAU | 0.995 | 0.967 | — |
| RPS24 | 0.980 | 0.840 | — |
| RPS7 | 0.980 | 0.840 | — |
| RPL18 | 0.979 | 0.834 | — |
| RPL24 | 0.979 | 0.835 | — |
| RPS6 | 0.979 | 0.825 | — |
| RPS3 | 0.979 | 0.836 | — |
| RPL34 | 0.978 | 0.839 | — |
| RPL6 | 0.978 | 0.832 | — |
| RPL23A | 0.978 | 0.834 | — |

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
| 三维结构 | AlphaFold pLDDT=75.3 + PDB: 无 | pLDDT=75.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cell projection; Cytoplasm, cytosol / Nucleoli, Plasma membrane; 额外: Golgi apparatus, Cy | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. DOCK4 — Dedicator of cytokinesis protein 4，研究基础较多，新颖性有限。
2. 蛋白大小1966 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 88 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N1I0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128512-DOCK4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOCK4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N1I0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (uncertain)。来源: https://www.proteinatlas.org/ENSG00000128512-DOCK4/subcellular

![](https://images.proteinatlas.org/71516/1433_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/71516/1433_C10_3_red_green.jpg)
![](https://images.proteinatlas.org/71516/1435_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/71516/1435_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/71516/1729_E11_2_red_green.jpg)
![](https://images.proteinatlas.org/71516/1729_E11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N1I0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
