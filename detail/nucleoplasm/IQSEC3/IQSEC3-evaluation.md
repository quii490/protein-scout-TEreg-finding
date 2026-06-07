---
type: protein-evaluation
gene: "IQSEC3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IQSEC3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IQSEC3 / KIAA1110 |
| 蛋白名称 | IQ motif and SEC7 domain-containing protein 3 |
| 蛋白大小 | 1182 aa / 127.6 kDa |
| UniProt ID | Q9UPP2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Postsynaptic density |
| 蛋白大小 | 8/10 | ×1 | 8 | 1182 aa / 127.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033742, IPR011993, IPR023394, IPR000904, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Postsynaptic density | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- GABA-ergic synapse (GO:0098982)
- glycinergic synapse (GO:0098690)
- inhibitory synapse (GO:0060077)
- nucleoplasm (GO:0005654)
- postsynaptic density (GO:0014069)
- postsynaptic membrane (GO:0045211)
- postsynaptic specialization of symmetric synapse (GO:0099629)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1110 |

**关键文献**:
1. Glycine Receptor Complex Analysis Using Immunoprecipitation-Blue Native Gel Electrophoresis-Mass Spectrometry.. *Proteomics*. PMID: 31984645
2. The genomic and clinical landscape of fetal akinesia.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 31680123
3. IQ Motif and SEC7 Domain-containing Protein 3 (IQSEC3) Interacts with Gephyrin to Promote Inhibitory Synapse Formation.. *The Journal of biological chemistry*. PMID: 27002143
4. Npas4 regulates IQSEC3 expression in hippocampal somatostatin interneurons to mediate anxiety-like behavior.. *Cell reports*. PMID: 34289353
5. Extended motif recognition tunes WW domain affinity in MAGI-IQSEC complexes.. *The FEBS journal*. PMID: 41870210

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.0 |
| 高置信度残基 (pLDDT>90) 占比 | 25.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 57.1% |
| 有序区域 (pLDDT>70) 占比 | 38.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.0），有序残基占 38.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033742, IPR011993, IPR023394, IPR000904, IPR035999; Pfam: PF16453, PF01369 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RBFOX3 | 0.848 | 0.000 | — |
| GPHN | 0.826 | 0.000 | — |
| ARF6 | 0.748 | 0.091 | — |
| INSYN1 | 0.662 | 0.000 | — |
| ARF1 | 0.646 | 0.062 | — |
| ARHGEF9 | 0.593 | 0.000 | — |
| NPAS4 | 0.554 | 0.000 | — |
| ARNT2 | 0.528 | 0.000 | — |
| ARNTL | 0.528 | 0.000 | — |
| EVL | 0.525 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Mycbp2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| Tnik | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| Dlgap1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| Agap2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28706196|doi:10.1038/s4 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.0 + PDB: 无 | pLDDT=57.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Postsynaptic density / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

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
1. IQSEC3 — IQ motif and SEC7 domain-containing protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1182 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=57.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UPP2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120645-IQSEC3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IQSEC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UPP2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000120645-IQSEC3/subcellular

![](https://images.proteinatlas.org/39025/1848_F7_31_red_green.jpg)
![](https://images.proteinatlas.org/39025/1848_F7_32_red_green.jpg)
![](https://images.proteinatlas.org/39025/411_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/39025/411_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/39025/416_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/39025/416_B8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UPP2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UPP2 |
| SMART | SM00222; |
| UniProt Domain [FT] | DOMAIN 315..344; /note="IQ"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00116"; DOMAIN 644..837; /note="SEC7"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00189"; DOMAIN 850..983; /note="PH" |
| InterPro | IPR033742;IPR011993;IPR023394;IPR000904;IPR035999; |
| Pfam | PF16453;PF01369; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000120645-IQSEC3/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
