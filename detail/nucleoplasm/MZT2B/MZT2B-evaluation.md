---
type: protein-evaluation
gene: "MZT2B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MZT2B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MZT2B / FAM128B, MOZART2B |
| 蛋白名称 | Mitotic-spindle organizing protein 2B |
| 蛋白大小 | 158 aa / 16.2 kDa |
| UniProt ID | Q6NZ67 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Centrosome; 额外: Nucleoplasm, Cytosol; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 8/10 | ×1 | 8 | 158 aa / 16.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.6; PDB: 9QVM |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024332; Pfam: PF12926 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- gamma-tubulin ring complex (GO:0000931)
- nucleoplasm (GO:0005654)
- spindle (GO:0005819)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM128B, MOZART2B |

**关键文献**:
1. Aberrant Whole Blood Gene Expression in the Lumen of Human Intracranial Aneurysms.. *Diagnostics (Basel, Switzerland)*. PMID: 34441376
2. MZT2B promotes malignant phenotypes in NSCLC cells by enhancing mitochondrial function and COX5B expression.. *Cell death & disease*. PMID: 41213905
3. m(6)A Regulator Expression Segregates Meningiomas Into Biologically Distinct Subtypes.. *Frontiers in oncology*. PMID: 35004283
4. Multi-omics analysis of NEDD1 in hepatocellular carcinoma: biological function, prognostic value, and clinical significance.. *Scientific reports*. PMID: 41775913
5. RNAseq-based meta-analyses revealed tumor suppressor-inducer fusion events in liver, oral, and ovarian cancer in the Indian population: a cancer cell surviving mechanism.. *Nucleosides, nucleotides & nucleic acids*. PMID: 41661231

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.6 |
| 高置信度残基 (pLDDT>90) 占比 | 19.6% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 38.6% |
| 低置信 (pLDDT<50) 占比 | 30.4% |
| 有序区域 (pLDDT>70) 占比 | 31.0% |
| 可用 PDB 条目 | 9QVM |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.6），有序残基占 31.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024332; Pfam: PF12926 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MZT1 | 0.999 | 0.827 | — |
| NEDD1 | 0.999 | 0.994 | — |
| TUBGCP4 | 0.996 | 0.887 | — |
| TUBGCP5 | 0.993 | 0.882 | — |
| TUBGCP6 | 0.991 | 0.846 | — |
| TUBG1 | 0.991 | 0.885 | — |
| TUBGCP2 | 0.976 | 0.918 | — |
| TUBGCP3 | 0.972 | 0.855 | — |
| NME7 | 0.963 | 0.626 | — |
| CENPJ | 0.900 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| Mzt2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TUBGCP3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TUBGCP4 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TUBGCP5 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TUBGCP6 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TUBG1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TUBGCP2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CSNK1A1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.6 + PDB: 9QVM | pLDDT=63.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Centrosome; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MZT2B — Mitotic-spindle organizing protein 2B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小158 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6NZ67
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152082-MZT2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MZT2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6NZ67
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (supported)。来源: https://www.proteinatlas.org/ENSG00000152082-MZT2B/subcellular

![](https://images.proteinatlas.org/51758/767_A9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51758/767_A9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/51758/779_A9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51758/779_A9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/51758/987_D8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51758/987_D8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6NZ67-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
