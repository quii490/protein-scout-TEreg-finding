---
type: protein-evaluation
gene: "SOX11"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SOX11 — REJECTED (研究热度过高 (PubMed strict=471，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SOX11 |
| 蛋白名称 | Transcription factor SOX-11 |
| 蛋白大小 | 441 aa / 46.7 kDa |
| UniProt ID | P35716 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 441 aa / 46.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=471 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.4; PDB: 6T78, 6T7A, 6T7C, 6T7D |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009071, IPR036910, IPR017386, IPR050140; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.0/180** | |
| **归一化总分** | | | **43.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 471 |
| PubMed broad count | 815 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular Pathogenesis of Mantle Cell Lymphoma.. *Hematology/oncology clinics of North America*. PMID: 32861278
2. Coffin-Siris Syndrome.. **. PMID: 23556151
3. How I manage mantle cell lymphoma: indolent versus aggressive disease.. *British journal of haematology*. PMID: 36807902
4. SOX11 as a potential prognostic biomarker in hepatocellular carcinoma linked to immune infiltration and ferroptosis.. *Chinese journal of cancer research = Chung-kuo yen cheng yen chiu*. PMID: 39246708
5. Genotype-Phenotype Correlations in 208 Individuals with Coffin-Siris Syndrome.. *Genes*. PMID: 34205270

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.4 |
| 高置信度残基 (pLDDT>90) 占比 | 17.5% |
| 置信残基 (pLDDT 70-90) 占比 | 2.7% |
| 中等置信 (pLDDT 50-70) 占比 | 25.4% |
| 低置信 (pLDDT<50) 占比 | 54.4% |
| 有序区域 (pLDDT>70) 占比 | 20.2% |
| 可用 PDB 条目 | 6T78, 6T7A, 6T7C, 6T7D |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.4），有序残基占 20.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009071, IPR036910, IPR017386, IPR050140; Pfam: PF00505 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SOX5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MTNR1A | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:26514267|imex:IM-24624 |
| CCL26 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| IL23A | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| SOX13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000322002 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 6
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.4 + PDB: 6T78, 6T7A, 6T7C, 6T7D | pLDDT=56.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 0 + 6 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SOX11 — Transcription factor SOX-11，研究基础较多，新颖性有限。
2. 蛋白大小441 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 471 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 471 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P35716
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176887-SOX11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SOX11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P35716
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000176887-SOX11/subcellular

![](https://images.proteinatlas.org/448/1836_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/448/1836_H7_3_red_green.jpg)
![](https://images.proteinatlas.org/448/1956_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/448/1956_G12_3_red_green.jpg)
![](https://images.proteinatlas.org/448/2055_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/448/2055_F5_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P35716-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P35716 |
| SMART | SM00398; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009071;IPR036910;IPR017386;IPR050140; |
| Pfam | PF00505; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000176887-SOX11/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SOX13 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
