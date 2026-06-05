---
type: protein-evaluation
gene: "PKP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PKP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PKP3 |
| 蛋白名称 | Plakophilin-3 |
| 蛋白大小 | 797 aa / 87.1 kDa |
| UniProt ID | Q9Y446 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cell Junctions; 额外: Nucleoplasm; UniProt: Nucleus; Cell junction, desmosome; Cytoplasm; Cell membrane; |
| 蛋白大小 | 10/10 | ×1 | 10 | 797 aa / 87.1 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=73 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR000225, IPR028435; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cell Junctions; 额外: Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cell junction, desmosome; Cytoplasm; Cell membrane; Cell junction, adherens junction; Cell ... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- cell junction (GO:0030054)
- cell-cell junction (GO:0005911)
- cornified envelope (GO:0001533)
- cytoplasm (GO:0005737)
- desmosome (GO:0030057)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 73 |
| PubMed broad count | 113 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. N(6)-methyladenosine-modified circIGF2BP3 inhibits CD8(+) T-cell responses to facilitate tumor immune evasion by promoting the deubiquitination of PD-L1 in non-small cell lung cancer.. *Molecular cancer*. PMID: 34416901
2. Defining desmosomal plakophilin-3 interactions.. *The Journal of cell biology*. PMID: 12707304
3. Plakophilin 3 drives acinar cell transformation and promotes cancer initiation and progression in pancreas.. *Cell reports*. PMID: 41166312
4. Identification of Hypoxia and Mitochondrial-related Gene Signature and Prediction of Prognostic Model in Lung Adenocarcinoma.. *Journal of Cancer*. PMID: 39006078
5. Comprehensive Analysis Identifies PKP3 Overexpression in Pancreatic Cancer Related to Unfavorable Prognosis.. *Biomedicines*. PMID: 37760912

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.3 |
| 高置信度残基 (pLDDT>90) 占比 | 48.7% |
| 置信残基 (pLDDT 70-90) 占比 | 6.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 40.0% |
| 有序区域 (pLDDT>70) 占比 | 55.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.3），有序残基占 55.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR000225, IPR028435; Pfam: PF00514 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DSG3 | 0.965 | 0.360 | — |
| FXR1 | 0.940 | 0.292 | — |
| DSG1 | 0.935 | 0.360 | — |
| DSP | 0.930 | 0.259 | — |
| DSC3 | 0.929 | 0.360 | — |
| DSG2 | 0.926 | 0.360 | — |
| PKP1 | 0.916 | 0.000 | — |
| DSC2 | 0.910 | 0.304 | — |
| JUP | 0.851 | 0.275 | — |
| PABPC1 | 0.804 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| ESR2 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13781|pubmed:21182203 |
| MCM7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23764002|imex:IM-20916 |
| MAPK14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| PRKD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| CFTR | psi-mi:"MI:0096"(pull down) | pubmed:29924966|imex:IM-27204 |
| IQUB | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CDK15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KIF3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GDF5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.3 + PDB: 无 | pLDDT=68.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cell junction, desmosome; Cytoplasm; Cell / Cell Junctions; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PKP3 — Plakophilin-3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小797 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 73 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y446
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184363-PKP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PKP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y446
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cell Junctions (enhanced)。来源: https://www.proteinatlas.org/ENSG00000184363-PKP3/subcellular

![](https://images.proteinatlas.org/12993/653_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/12993/653_E1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/12993/658_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/12993/658_E1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/12993/659_E1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/12993/659_E1_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y446-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
