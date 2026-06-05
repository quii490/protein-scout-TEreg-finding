---
type: protein-evaluation
gene: "HCFC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HCFC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HCFC2 |
| 蛋白名称 | Host cell factor 2 |
| 蛋白大小 | 792 aa / 86.8 kDa |
| UniProt ID | Q9Y5Z7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 792 aa / 86.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003961, IPR036116, IPR011043, IPR043536, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- histone methyltransferase complex (GO:0035097)
- MLL1 complex (GO:0071339)
- MLL1/2 complex (GO:0044665)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Differential microRNA expression analyses across two brain regions in Alzheimer's disease.. *Translational psychiatry*. PMID: 36038535
2. Development and validation of a nomogram with an epigenetic signature for predicting survival in patients with lung adenocarcinoma.. *Aging*. PMID: 33221751
3. Genetic dissection of behavioral flexibility: reversal learning in mice.. *Biological psychiatry*. PMID: 21392734
4. Establishing a Macrophage Phenotypic Switch-Associated Signature-Based Risk Model for Predicting the Prognoses of Lung Adenocarcinoma.. *Frontiers in oncology*. PMID: 35284334
5. Characterization of the glycosylphosphatidylinositol-anchor signal sequence of human Cryptic with a hydrophilic extension.. *Biochimica et biophysica acta*. PMID: 18930707

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.9 |
| 高置信度残基 (pLDDT>90) 占比 | 49.5% |
| 置信残基 (pLDDT 70-90) 占比 | 16.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 29.2% |
| 有序区域 (pLDDT>70) 占比 | 65.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.9，有序区 65.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003961, IPR036116, IPR011043, IPR043536, IPR013783; Pfam: PF13854 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HCFC1 | 0.982 | 0.805 | — |
| CREBZF | 0.971 | 0.000 | — |
| WDR5 | 0.959 | 0.811 | — |
| RBBP5 | 0.955 | 0.799 | — |
| ASH2L | 0.941 | 0.866 | — |
| CREB3 | 0.924 | 0.444 | — |
| KMT2B | 0.907 | 0.790 | — |
| SETD1A | 0.887 | 0.640 | — |
| KMT2A | 0.883 | 0.736 | — |
| BOD1L1 | 0.851 | 0.688 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KMT2A | psi-mi:"MI:0071"(molecular sieving) | pubmed:15199122 |
| MEN1 | psi-mi:"MI:0071"(molecular sieving) | pubmed:15199122 |
| ASH2L | psi-mi:"MI:0071"(molecular sieving) | pubmed:15199122 |
| RBBP5 | psi-mi:"MI:0071"(molecular sieving) | pubmed:15199122 |
| UTP18 | psi-mi:"MI:0071"(molecular sieving) | pubmed:15199122 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| PPP2R2B | psi-mi:"MI:0096"(pull down) | imex:IM-9155|pubmed:19156129 |
| ESR2 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-13781|pubmed:21182203 |
| capR | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| IRF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.9 + PDB: 无 | pLDDT=72.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Plasma membrane, Cytosol | 一致 |
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
1. HCFC2 — Host cell factor 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小792 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y5Z7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111727-HCFC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HCFC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y5Z7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000111727-HCFC2/subcellular

![](https://images.proteinatlas.org/6227/1876_D5_26_cr5b719adc2e799_red_green.jpg)
![](https://images.proteinatlas.org/6227/1876_D5_2_cr5b719adc2e56b_red_green.jpg)
![](https://images.proteinatlas.org/6227/2175_E10_26_red_green.jpg)
![](https://images.proteinatlas.org/6227/2175_E10_77_red_green.jpg)
![](https://images.proteinatlas.org/6227/7_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/6227/7_G6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y5Z7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
