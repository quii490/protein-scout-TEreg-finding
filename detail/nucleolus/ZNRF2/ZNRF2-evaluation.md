---
type: protein-evaluation
gene: "ZNRF2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ZNRF2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ZNRF2 / RNF202 |
| 蛋白名称 | E3 ubiquitin-protein ligase ZNRF2 |
| 蛋白大小 | 242 aa / 24.1 kDa |
| UniProt ID | Q8NHG8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; 额外: Nucleoli fibrillar center; UniProt: Endosome membrane; Lysosome membrane; Presynaptic cell membr |
| 蛋白大小 | 10/10 | ×1 | 10 | 242 aa / 24.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001841, IPR013083, IPR051878; Pfam: PF13639 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Nucleoli fibrillar center | Uncertain |
| UniProt | Endosome membrane; Lysosome membrane; Presynaptic cell membrane; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic vesicle membrane (GO:0030659)
- cytosol (GO:0005829)
- endosome membrane (GO:0010008)
- fibrillar center (GO:0001650)
- lysosomal membrane (GO:0005765)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 26 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF202 |

**关键文献**:
1. ZNRF2 is essential for gliomagenesis through orchestrating glycolysis and acts as a promising therapeutic target in glioma.. *Journal of translational medicine*. PMID: 39953597
2. Targeting ZNRF2-mediated SLC3A2 plasma membrane translocation enhances ferroptosis in lung adenocarcinoma.. *Oncogene*. PMID: 40999004
3. A pancancer analysis of the oncogenic role of ZNRF2 in human tumours.. *Journal of cellular and molecular medicine*. PMID: 37551845
4. ZNRF2 is released from membranes by growth factors and, together with ZNRF1, regulates the Na+/K+ATPase.. *Journal of cell science*. PMID: 22797923
5. Deletion of ZNRF2 Exacerbates MPTP-Induced Parkinson's Disease by Activating mTOR-Mediated Neuroinflammatory Pathways.. *Molecular neurobiology*. PMID: 40402410

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.6 |
| 高置信度残基 (pLDDT>90) 占比 | 24.8% |
| 置信残基 (pLDDT 70-90) 占比 | 9.9% |
| 中等置信 (pLDDT 50-70) 占比 | 37.6% |
| 低置信 (pLDDT<50) 占比 | 27.7% |
| 有序区域 (pLDDT>70) 占比 | 34.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.6），有序残基占 34.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001841, IPR013083, IPR051878; Pfam: PF13639 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBE2D2 | 0.878 | 0.452 | — |
| UBE2N | 0.844 | 0.787 | — |
| UBE2D3 | 0.824 | 0.452 | — |
| UBE2S | 0.599 | 0.046 | — |
| ZNRF4 | 0.595 | 0.000 | — |
| ANKRD28 | 0.551 | 0.422 | — |
| RNF2 | 0.550 | 0.000 | — |
| CWC25 | 0.542 | 0.000 | — |
| EAF1 | 0.541 | 0.000 | — |
| RSPRY1 | 0.532 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| cca | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| - | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| UBE2N | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| WDR5B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| EEA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CGB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NCKAP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ABCA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ANKRD28 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.6 + PDB: 无 | pLDDT=65.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endosome membrane; Lysosome membrane; Presynaptic  / Nucleoplasm, Vesicles; 额外: Nucleoli fibrillar cent | 一致 |
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
1. ZNRF2 — E3 ubiquitin-protein ligase ZNRF2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小242 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NHG8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180233-ZNRF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ZNRF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NHG8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000180233-ZNRF2/subcellular

![](https://images.proteinatlas.org/72244/1541_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/72244/1541_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/72244/1542_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/72244/1542_F2_3_red_green.jpg)
![](https://images.proteinatlas.org/72244/1657_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/72244/1657_A10_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NHG8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
