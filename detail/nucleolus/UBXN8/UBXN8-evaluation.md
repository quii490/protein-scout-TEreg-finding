---
type: protein-evaluation
gene: "UBXN8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UBXN8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UBXN8 / D8S2298E, REP8, UBXD6 |
| 蛋白名称 | UBX domain-containing protein 8 |
| 蛋白大小 | 270 aa / 30.5 kDa |
| UniProt ID | O00124 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum; 额外: Nucleoplasm, Nucleoli; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 270 aa / 30.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029071, IPR001012, IPR050730, IPR017247; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Nucleoplasm, Nucleoli | Supported |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: D8S2298E, REP8, UBXD6 |

**关键文献**:
1. Epigenetic silencing of UBXN8 contributes to leukemogenesis in t(8;21) acute myeloid leukemia.. *Experimental & molecular medicine*. PMID: 34921223
2. Recognition of DNA Methylation Molecular Features for Diagnosis and Prognosis in Gastric Cancer.. *Frontiers in genetics*. PMID: 34745226
3. The function of targeted host genes determines the oncogenicity of HBV integration in hepatocellular carcinoma.. *Journal of hepatology*. PMID: 24362074
4. Genome-Wide DNA Methylation Profiles in Community Members Exposed to the World Trade Center Disaster.. *International journal of environmental research and public health*. PMID: 32751422

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.1 |
| 高置信度残基 (pLDDT>90) 占比 | 27.4% |
| 置信残基 (pLDDT 70-90) 占比 | 38.9% |
| 中等置信 (pLDDT 50-70) 占比 | 23.0% |
| 低置信 (pLDDT<50) 占比 | 10.7% |
| 有序区域 (pLDDT>70) 占比 | 66.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.1，有序区 66.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029071, IPR001012, IPR050730, IPR017247; Pfam: PF00789 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VCP | 0.991 | 0.873 | — |
| UBXN2A | 0.965 | 0.094 | — |
| PPP2CB | 0.964 | 0.049 | — |
| UBXN1 | 0.960 | 0.051 | — |
| UBXN6 | 0.959 | 0.095 | — |
| UBXN4 | 0.956 | 0.000 | — |
| NSFL1C | 0.950 | 0.094 | — |
| SVIP | 0.912 | 0.000 | — |
| UFD1 | 0.857 | 0.781 | — |
| NPLOC4 | 0.792 | 0.727 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NPLOC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| VCPIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| UFD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| VCP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| GTF2F2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| MEOX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GJA8 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| Q7Z6F2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PGRMC2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HSD17B13 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.1 + PDB: 无 | pLDDT=77.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Endoplasmic reticulum; 额外: Nucleoplasm, Nucleoli | 一致 |
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
1. UBXN8 — UBX domain-containing protein 8，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小270 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00124
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104691-UBXN8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UBXN8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00124
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (supported)。来源: https://www.proteinatlas.org/ENSG00000104691-UBXN8/subcellular

![](https://images.proteinatlas.org/77538/1692_B11_18_cr57d27d71098d6_red_green.jpg)
![](https://images.proteinatlas.org/77538/1692_B11_28_cr57d27d7d86eda_red_green.jpg)
![](https://images.proteinatlas.org/77538/1743_F1_13_cr57fe1ad8e6ca5_red_green.jpg)
![](https://images.proteinatlas.org/77538/1743_F1_28_cr57fe1ae443ed4_red_green.jpg)
![](https://images.proteinatlas.org/77538/1757_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/77538/1757_F5_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00124-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
