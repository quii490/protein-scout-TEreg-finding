---
type: protein-evaluation
gene: "WDR83"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR83 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDR83 / MORG1 |
| 蛋白名称 | WD repeat domain-containing protein 83 |
| 蛋白大小 | 315 aa / 34.3 kDa |
| UniProt ID | Q9BRX9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; 额外: Centriolar satellite, Basal body,; UniProt: Cytoplasm; Lysosome; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 315 aa / 34.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015943, IPR020472, IPR019775, IPR036322, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Centriolar satellite, Basal body, Cytosol | Approved |
| UniProt | Cytoplasm; Lysosome; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- catalytic step 2 spliceosome (GO:0071013)
- endosome membrane (GO:0010008)
- lysosome (GO:0005764)
- spliceosomal complex (GO:0005681)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MORG1 |

**关键文献**:
1. Splicing-dependent restriction of the HBZ gene by Tax underlies biphasic HTLV-1 infection.. *PLoS pathogens*. PMID: 40720552
2. WDR83/MORG1 inhibits RRAG GTPase-MTORC1 signaling to facilitate basal autophagy.. *Autophagy*. PMID: 38450633
3. Bidirectional regulation between WDR83 and its natural antisense transcript DHPS in gastric cancer.. *Cell research*. PMID: 22491477
4. Defining the Functional Interactome of Spliceosome-Associated G-Patch Protein Gpl1 in the Fission Yeast Schizosaccharomyces pombe.. *International journal of molecular sciences*. PMID: 36361590
5. SNPs detection in DHPS-WDR83 overlapping genes mapping on porcine chromosome 2 in a QTL region for meat pH.. *BMC genetics*. PMID: 24103193

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.3 |
| 高置信度残基 (pLDDT>90) 占比 | 90.5% |
| 置信残基 (pLDDT 70-90) 占比 | 4.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 1.3% |
| 有序区域 (pLDDT>70) 占比 | 94.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.3，有序区 94.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015943, IPR020472, IPR019775, IPR036322, IPR001680; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SF3B4 | 0.995 | 0.994 | — |
| PRPF8 | 0.994 | 0.994 | — |
| LAMTOR3 | 0.956 | 0.292 | — |
| EGLN3 | 0.948 | 0.094 | — |
| GPATCH1 | 0.913 | 0.860 | — |
| PPIL1 | 0.815 | 0.783 | — |
| MAP2K1 | 0.813 | 0.292 | — |
| LAMTOR2 | 0.804 | 0.000 | — |
| AQR | 0.796 | 0.786 | — |
| MAPK3 | 0.795 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| WDR83OS | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:22645275|imex:IM-17891 |
| CENATAC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| WBP4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:28838205|imex:IM-26387 |
| KEAP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PIKFYVE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SH2B2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIPA1L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIPA1L3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AQR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDC40 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.3 + PDB: 无 | pLDDT=93.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Lysosome; Nucleus / Nucleoplasm, Vesicles; 额外: Centriolar satellite, B | 一致 |
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
1. WDR83 — WD repeat domain-containing protein 83，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小315 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BRX9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123154-WDR83/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDR83
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BRX9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000123154-WDR83/subcellular

![](https://images.proteinatlas.org/42629/2121_B8_21_blue_red_green.jpg)
![](https://images.proteinatlas.org/42629/2121_B8_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/42629/2129_D7_34_blue_red_green.jpg)
![](https://images.proteinatlas.org/42629/2129_D7_58_blue_red_green.jpg)
![](https://images.proteinatlas.org/42629/2210_C11_39_blue_red_green.jpg)
![](https://images.proteinatlas.org/42629/2210_C11_51_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BRX9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
