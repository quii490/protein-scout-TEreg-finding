---
type: protein-evaluation
gene: "LEO1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LEO1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LEO1 / RDL |
| 蛋白名称 | RNA polymerase-associated protein LEO1 |
| 蛋白大小 | 666 aa / 75.4 kDa |
| UniProt ID | Q8WVC0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli fibrillar center; 额外: Centrosome; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 666 aa / 75.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=61 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.3; PDB: 4M6T, 6GMH, 6TED, 7OOP, 7OPC, 7OPD, 7UNC |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007149; Pfam: PF04004 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli fibrillar center; 额外: Centrosome | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cdc73/Paf1 complex (GO:0016593)
- centrosome (GO:0005813)
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 61 |
| PubMed broad count | 93 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RDL |

**关键文献**:
1. Large-scale targeted sequencing identifies risk genes for neurodevelopmental disorders.. *Nature communications*. PMID: 33004838
2. Toward clinical exomes in diagnostics and management of male infertility.. *American journal of human genetics*. PMID: 38614076
3. Novel FMRP interaction networks linked to cellular stress.. *The FEBS journal*. PMID: 32525608
4. Burden re-analysis of neurodevelopmental disorder cohorts for prioritization of candidate genes.. *European journal of human genetics : EJHG*. PMID: 38965372
5. Leo1 is essential for the dynamic regulation of heterochromatin and gene expression during cellular quiescence.. *Epigenetics & chromatin*. PMID: 31315658

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.3 |
| 高置信度残基 (pLDDT>90) 占比 | 5.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.4% |
| 中等置信 (pLDDT 50-70) 占比 | 20.4% |
| 低置信 (pLDDT<50) 占比 | 58.0% |
| 有序区域 (pLDDT>70) 占比 | 21.7% |
| 可用 PDB 条目 | 4M6T, 6GMH, 6TED, 7OOP, 7OPC, 7OPD, 7UNC, 7UND, 8A3Y, 9EGX |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.3），有序残基占 21.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007149; Pfam: PF04004 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RTF1 | 0.999 | 0.997 | — |
| CTR9 | 0.999 | 0.995 | — |
| SUPT5H | 0.999 | 0.966 | — |
| CDC73 | 0.999 | 0.997 | — |
| WDR61 | 0.999 | 0.970 | — |
| PAF1 | 0.999 | 0.998 | — |
| SUPT16H | 0.997 | 0.981 | — |
| SUPT4H1 | 0.997 | 0.913 | — |
| SSRP1 | 0.991 | 0.962 | — |
| POLR2A | 0.987 | 0.926 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CAB3 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| RTF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| CDC73 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| CTR9 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| CTNNB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16630820|imex:IM-11820 |
| ATG12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22113938|imex:IM-16640 |
| SPT16 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:12242279|imex:IM-19705 |
| ARRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| SPT5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:11927560|imex:IM-19478 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.3 + PDB: 4M6T, 6GMH, 6TED, 7OOP, 7OPC,  | pLDDT=54.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli fibrillar center; 额外: Centro | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LEO1 — RNA polymerase-associated protein LEO1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小666 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 61 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=54.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WVC0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166477-LEO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LEO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WVC0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000166477-LEO1/subcellular

![](https://images.proteinatlas.org/40741/418_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/40741/418_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/40741/424_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/40741/424_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/40741/429_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/40741/429_G11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WVC0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
