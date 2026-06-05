---
type: protein-evaluation
gene: "DUSP8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DUSP8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP8 / C11orf81, VH5 |
| 蛋白名称 | Dual specificity protein phosphatase 8 |
| 蛋白大小 | 625 aa / 65.8 kDa |
| UniProt ID | Q13202 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 625 aa / 65.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=60 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.8; PDB: 4JMK |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000340, IPR048035, IPR008343, IPR029021, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 60 |
| PubMed broad count | 81 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C11orf81, VH5 |

**关键文献**:
1. Identifying disease progression biomarkers in metabolic associated steatotic liver disease (MASLD) through weighted gene co-expression network analysis and machine learning.. *Journal of translational medicine*. PMID: 40275274
2. DUSP8 phosphatase: structure, functions, expression regulation and the role in human diseases.. *Cell & bioscience*. PMID: 31467668
3. DUSP8 as a regulator of glioblastoma stem-like cell contribution to tumor vascularization.. *Journal of experimental & clinical cancer research : CR*. PMID: 41029387
4. Type 2 diabetes risk gene Dusp8 regulates hypothalamic Jnk signaling and insulin sensitivity.. *The Journal of clinical investigation*. PMID: 32780722
5. DUSP8-attenuated ERK1/2 signaling mediates lipogenesis and steroidogenesis in chicken granulosa cells.. *Theriogenology*. PMID: 38820772

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.8 |
| 高置信度残基 (pLDDT>90) 占比 | 30.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 51.2% |
| 有序区域 (pLDDT>70) 占比 | 42.3% |
| 可用 PDB 条目 | 4JMK |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.8），有序残基占 42.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000340, IPR048035, IPR008343, IPR029021, IPR001763; Pfam: PF00782, PF00581 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAPK8 | 0.982 | 0.747 | — |
| MAPK9 | 0.968 | 0.558 | — |
| MAPK11 | 0.866 | 0.300 | — |
| MAPK12 | 0.861 | 0.300 | — |
| MAPK13 | 0.859 | 0.300 | — |
| MAPK14 | 0.812 | 0.300 | — |
| MAPK1 | 0.808 | 0.272 | — |
| MAPK3 | 0.793 | 0.272 | — |
| LOC102723407 | 0.580 | 0.000 | — |
| DUSP7 | 0.562 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=62.8 + PDB: 4JMK | pLDDT=62.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DUSP8 — Dual specificity protein phosphatase 8，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小625 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 60 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13202
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184545-DUSP8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13202
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000184545-DUSP8/subcellular

![](https://images.proteinatlas.org/20071/183_H6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20071/183_H6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/20071/185_H6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20071/185_H6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/20071/242_H6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20071/242_H6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13202-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
