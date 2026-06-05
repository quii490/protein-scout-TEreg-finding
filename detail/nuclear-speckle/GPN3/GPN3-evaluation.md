---
type: protein-evaluation
gene: "GPN3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPN3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPN3 / ATPBD1C |
| 蛋白名称 | GPN-loop GTPase 3 |
| 蛋白大小 | 284 aa / 32.8 kDa |
| UniProt ID | Q9UHW5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 284 aa / 32.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004130, IPR030228, IPR027417; Pfam: PF03029 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ATPBD1C |

**关键文献**:
1. Gpn1 and Gpn3 associate tightly and their protein levels are mutually dependent in mammalian cells.. *FEBS letters*. PMID: 25241168
2. Npa3 interacts with Gpn3 and assembly factor Rba50 for RNA polymerase II biogenesis.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 32985767
3. Parcs/Gpn3 is required for the nuclear accumulation of RNA polymerase II.. *Biochimica et biophysica acta*. PMID: 21782856
4. FRET-based analysis and molecular modeling of the human GPN-loop GTPases 1 and 3 heterodimer unveils a dominant-negative protein complex.. *The FEBS journal*. PMID: 31298811
5. Gpn3 is polyubiquitinated on lysine 216 and degraded by the proteasome in the cell nucleus in a Gpn1-inhibitable manner.. *FEBS letters*. PMID: 29029378

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.2 |
| 高置信度残基 (pLDDT>90) 占比 | 57.7% |
| 置信残基 (pLDDT 70-90) 占比 | 26.4% |
| 中等置信 (pLDDT 50-70) 占比 | 12.0% |
| 低置信 (pLDDT<50) 占比 | 3.9% |
| 有序区域 (pLDDT>70) 占比 | 84.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.2，有序区 84.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004130, IPR030228, IPR027417; Pfam: PF03029 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPN1 | 0.987 | 0.956 | — |
| RPAP2 | 0.955 | 0.837 | — |
| POLR2C | 0.942 | 0.841 | — |
| POLR2F | 0.913 | 0.797 | — |
| POLR2L | 0.911 | 0.778 | — |
| POLR1C | 0.908 | 0.821 | — |
| POLR2D | 0.908 | 0.810 | — |
| POLR2B | 0.903 | 0.752 | — |
| POLR2A | 0.889 | 0.776 | — |
| POLR2E | 0.882 | 0.753 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MED9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED26 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| WDR48 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| HNT3 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| SIGLEC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MICU1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| ZFC3H1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.2 + PDB: 无 | pLDDT=86.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear speckles; 额外: Cytosol | 一致 |
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
1. GPN3 — GPN-loop GTPase 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小284 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UHW5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111231-GPN3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UHW5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000111231-GPN3/subcellular

![](https://images.proteinatlas.org/39764/468_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/39764/468_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/39764/470_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/39764/470_H1_3_red_green.jpg)
![](https://images.proteinatlas.org/39764/473_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/39764/473_H1_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UHW5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
