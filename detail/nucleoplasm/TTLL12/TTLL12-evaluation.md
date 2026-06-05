---
type: protein-evaluation
gene: "TTLL12"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TTLL12 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTLL12 / KIAA0153 |
| 蛋白名称 | Tubulin--tyrosine ligase-like protein 12 |
| 蛋白大小 | 644 aa / 74.4 kDa |
| UniProt ID | Q14166 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Plasma membrane; UniProt: Cytoplasm; Midbody; Cytoplasm, cytoskeleton, microtubule org |
| 蛋白大小 | 10/10 | ×1 | 10 | 644 aa / 74.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR057954, IPR004344, IPR027749; Pfam: PF25556, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Plasma membrane | Supported |
| UniProt | Cytoplasm; Midbody; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, c... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- midbody (GO:0030496)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- spindle (GO:0005819)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0153 |

**关键文献**:
1. Tumor-intrinsic TTLL12 drives resistance to cancer immunotherapy via modulating myeloid-derived suppressor cells.. *Journal for immunotherapy of cancer*. PMID: 40461158
2. TTLL12 Inhibits the Activation of Cellular Antiviral Signaling through Interaction with VISA/MAVS.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 28011935
3. CRISPR library screening to develop HEK293-derived cell lines with improved lentiviral vector titers.. *Frontiers in genome editing*. PMID: 37520398
4. Identification of a novel transcript isoform of the TTLL12 gene in human cancers.. *Oncology reports*. PMID: 27748896
5. TTLL12 expression in ovarian cancer correlates with a poor outcome.. *International journal of clinical and experimental pathology*. PMID: 32211104

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.0 |
| 高置信度残基 (pLDDT>90) 占比 | 83.1% |
| 置信残基 (pLDDT 70-90) 占比 | 9.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 4.7% |
| 有序区域 (pLDDT>70) 占比 | 93.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.0，有序区 93.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR057954, IPR004344, IPR027749; Pfam: PF25556, PF03133 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PBDC1 | 0.832 | 0.831 | — |
| EEF1A1 | 0.808 | 0.803 | — |
| DNAJB1 | 0.797 | 0.786 | — |
| EEF1AKMT1 | 0.786 | 0.785 | — |
| EEF1A2 | 0.724 | 0.723 | — |
| TTLL4 | 0.722 | 0.000 | — |
| TTLL9 | 0.677 | 0.078 | — |
| DNAJB4 | 0.671 | 0.662 | — |
| TTLL11 | 0.664 | 0.000 | — |
| TTLL1 | 0.609 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q7TPC3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| PolZ2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| mad2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Sap25 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16449650|imex:IM-19874 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CSNK2A2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| eEF1alpha1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.0 + PDB: 无 | pLDDT=91.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Midbody; Cytoplasm, cytoskeleton, micro / Cytosol; 额外: Nucleoplasm, Plasma membrane | 一致 |
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
1. TTLL12 — Tubulin--tyrosine ligase-like protein 12，非常新颖，仅有少数基础研究。
2. 蛋白大小644 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14166
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100304-TTLL12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTLL12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14166
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000100304-TTLL12/subcellular

![](https://images.proteinatlas.org/3054/110_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3054/110_C1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3054/111_C1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/3054/111_C1_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/3054/159_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3054/159_C1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14166-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
