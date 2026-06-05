---
type: protein-evaluation
gene: "EZHIP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EZHIP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EZHIP / CXorf67 |
| 蛋白名称 | EZH inhibitory protein |
| 蛋白大小 | 503 aa / 51.9 kDa |
| UniProt ID | Q86X51 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 503 aa / 51.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052882 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 63 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CXorf67 |

**关键文献**:
1. Targeting integrated epigenetic and metabolic pathways in lethal childhood PFA ependymomas.. *Science translational medicine*. PMID: 34613815
2. EZHIP restricts noncanonical PRC2 binding and regulates H3K27me3 intergenerational inheritance and reprogramming.. *Cell stem cell*. PMID: 41118764
3. cIMPACT-NOW update 11: Proposal on adaptation of diagnostic criteria for IDH- and H3-wildtype diffuse high-grade gliomas and for posterior fossa ependymal tumors.. *Brain pathology (Zurich, Switzerland)*. PMID: 40887057
4. Common molecular features of H3K27M DMGs and PFA ependymomas map to hindbrain developmental pathways.. *Acta neuropathologica communications*. PMID: 36759899
5. EZHIP boosts neuronal-like synaptic gene programs and depresses polyamine metabolism.. *Acta neuropathologica communications*. PMID: 41204377

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.8 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 5.8% |
| 中等置信 (pLDDT 50-70) 占比 | 22.9% |
| 低置信 (pLDDT<50) 占比 | 71.4% |
| 有序区域 (pLDDT>70) 占比 | 5.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=48.8），有序残基占 5.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052882 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EZH2 | 0.825 | 0.358 | — |
| MBTD1 | 0.775 | 0.000 | — |
| SUZ12 | 0.757 | 0.301 | — |
| MEAF6 | 0.694 | 0.000 | — |
| ZC3H7B | 0.649 | 0.136 | — |
| PHF1 | 0.642 | 0.000 | — |
| JAZF1 | 0.621 | 0.051 | — |
| EPOP | 0.583 | 0.000 | — |
| POLR2G | 0.567 | 0.486 | — |
| NUTM2A | 0.564 | 0.074 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TRAF4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZNF417 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENKD1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TRIM41 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SCNM1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.8 + PDB: 无 | pLDDT=48.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

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
1. EZHIP — EZH inhibitory protein，非常新颖，仅有少数基础研究。
2. 蛋白大小503 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=48.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86X51
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187690-EZHIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EZHIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86X51
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000187690-EZHIP/subcellular

![](https://images.proteinatlas.org/4003/111_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/4003/111_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/4003/159_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/4003/159_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/6128/111_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/6128/111_G1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86X51-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
