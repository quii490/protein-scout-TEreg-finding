---
type: protein-evaluation
gene: "UCK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UCK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UCK1 / URK1 |
| 蛋白名称 | Uridine-cytidine kinase 1 |
| 蛋白大小 | 277 aa / 31.4 kDa |
| UniProt ID | Q9HA47 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 277 aa / 31.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=83.5; PDB: 2JEO, 2UVQ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027417, IPR006083, IPR000764; Pfam: PF00485 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: URK1 |

**关键文献**:
1. The Cytidine Analog Fluorocyclopentenylcytosine (RX-3117) Is Activated by Uridine-Cytidine Kinase 2.. *PloS one*. PMID: 27612203
2. Resistance of Leukemia Cells to 5-Azacytidine: Different Responses to the Same Induction Protocol.. *Cancers*. PMID: 37297025
3. Expression of nucleoside-metabolizing enzymes in myelodysplastic syndromes and modulation of response to azacitidine.. *Leukemia*. PMID: 24192812
4. Target genes of the developmental regulator PRIB of the mushroom Lentinula edodes.. *Bioscience, biotechnology, and biochemistry*. PMID: 15388965
5. Cloning, sequence analysis and expression of the basidiomycete Lentinus edodes gene uck1, encoding UMP-CMP kinase, the homologue of Saccharomyces cerevisae URA6 gene.. *Gene*. PMID: 9602145

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.5 |
| 高置信度残基 (pLDDT>90) 占比 | 72.9% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.4% |
| 低置信 (pLDDT<50) 占比 | 21.3% |
| 有序区域 (pLDDT>70) 占比 | 77.2% |
| 可用 PDB 条目 | 2JEO, 2UVQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2JEO, 2UVQ）+ AlphaFold高质量预测（pLDDT=83.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR006083, IPR000764; Pfam: PF00485 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UPRT | 0.999 | 0.860 | — |
| UPP2 | 0.982 | 0.000 | — |
| UMPS | 0.981 | 0.067 | — |
| UCK2 | 0.980 | 0.805 | — |
| UPP1 | 0.979 | 0.000 | — |
| CDA | 0.977 | 0.000 | — |
| UCKL1 | 0.928 | 0.113 | — |
| CANT1 | 0.920 | 0.000 | — |
| ENTPD8 | 0.919 | 0.000 | — |
| CMPK2 | 0.918 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000361289.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EBI-16434671 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:26871637|imex:IM-25013| |
| Plcg2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| PLA2G12A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ezrA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| UCK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| KLHL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MPPED1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UPRT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.5 + PDB: 2JEO, 2UVQ | pLDDT=83.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. UCK1 — Uridine-cytidine kinase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小277 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HA47
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130717-UCK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UCK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HA47
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000130717-UCK1/subcellular

![](https://images.proteinatlas.org/50969/700_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/50969/700_E11_2_red_green.jpg)
![](https://images.proteinatlas.org/50969/722_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/50969/722_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/50969/726_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/50969/726_E10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HA47-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HA47 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027417;IPR006083;IPR000764; |
| Pfam | PF00485; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000130717-UCK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| UCK2 | Biogrid, Bioplex | true |
| KLHL2 | Biogrid | false |
| PLA2G12A | Biogrid | false |
| UPRT | Bioplex | false |
| USP28 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
