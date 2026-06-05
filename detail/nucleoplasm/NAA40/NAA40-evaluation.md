---
type: protein-evaluation
gene: "NAA40"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NAA40 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAA40 / NAT11, PATT1 |
| 蛋白名称 | N-alpha-acetyltransferase 40 |
| 蛋白大小 | 237 aa / 27.2 kDa |
| UniProt ID | Q86UY6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Centriolar satellite, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 237 aa / 27.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=92.1; PDB: 4U9V, 4U9W, 7KD7, 7KPU |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016181, IPR000182, IPR039949; Pfam: PF00583 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centriolar satellite, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriolar satellite (GO:0034451)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NAT11, PATT1 |

**关键文献**:
1. N-Terminal Acetyltransferase Naa40p Whereabouts Put into N-Terminal Proteoform Perspective.. *International journal of molecular sciences*. PMID: 33916271
2. N-terminal histone acetyltransferase NAA40 modulates osteosarcoma progression by controlling AGR2 expression.. *Biochemical and biophysical research communications*. PMID: 40020320
3. N(alpha)-acetyltransferase 40-mediated histone acetylation plays an important role in ecdysone regulation of metamorphosis in the red flour beetle, Tribolium castaneum.. *Communications biology*. PMID: 38702540
4. NAA40 and NAC cooperate in co-translational histone acetylation in humans.. *Nature communications*. PMID: 41820326
5. NAA40 contributes to colorectal cancer growth by controlling PRMT5 expression.. *Cell death & disease*. PMID: 30858358

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.1 |
| 高置信度残基 (pLDDT>90) 占比 | 86.5% |
| 置信残基 (pLDDT 70-90) 占比 | 4.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 5.9% |
| 有序区域 (pLDDT>70) 占比 | 91.1% |
| 可用 PDB 条目 | 4U9V, 4U9W, 7KD7, 7KPU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4U9V, 4U9W, 7KD7, 7KPU）+ AlphaFold高质量预测（pLDDT=92.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016181, IPR000182, IPR039949; Pfam: PF00583 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NAA50 | 0.906 | 0.000 | — |
| NAA60 | 0.875 | 0.000 | — |
| NAA20 | 0.846 | 0.000 | — |
| WDR11 | 0.840 | 0.835 | — |
| H4C6 | 0.833 | 0.710 | — |
| NAA15 | 0.823 | 0.166 | — |
| NAA30 | 0.822 | 0.000 | — |
| NAA10 | 0.811 | 0.000 | — |
| NAA80 | 0.793 | 0.000 | — |
| XPOT | 0.791 | 0.790 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BTF3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MACROH2A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GLRX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATG7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TPP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MCM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| METAP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBA52 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| XPC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SSRP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.1 + PDB: 4U9V, 4U9W, 7KD7, 7KPU | pLDDT=92.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Centriolar satellite, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NAA40 — N-alpha-acetyltransferase 40，非常新颖，仅有少数基础研究。
2. 蛋白大小237 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86UY6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110583-NAA40/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAA40
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86UY6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000110583-NAA40/subcellular

![](https://images.proteinatlas.org/56142/2269_B8_39_red_green.jpg)
![](https://images.proteinatlas.org/56142/2269_B8_66_red_green.jpg)
![](https://images.proteinatlas.org/56142/975_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/56142/975_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/56142/976_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/56142/976_E6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86UY6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
