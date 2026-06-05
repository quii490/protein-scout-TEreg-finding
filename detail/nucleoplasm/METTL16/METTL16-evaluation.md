---
type: protein-evaluation
gene: "METTL16"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## METTL16 — REJECTED (研究热度过高 (PubMed strict=156，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | METTL16 / METT10D |
| 蛋白名称 | RNA N(6)-adenosine-methyltransferase METTL16 |
| 蛋白大小 | 562 aa / 63.6 kDa |
| UniProt ID | Q86W50 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 562 aa / 63.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=156 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=78.5; PDB: 2H00, 6B91, 6B92, 6DU4, 6DU5, 6GFK, 6GFN |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017182, IPR010286, IPR029063; Pfam: PF05971 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 156 |
| PubMed broad count | 249 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: METT10D |

**关键文献**:
1. Lactylation of METTL16 promotes cuproptosis via m(6)A-modification on FDX1 mRNA in gastric cancer.. *Nature communications*. PMID: 37863889
2. RNA m6A methylation across the transcriptome.. *Molecular cell*. PMID: 36736310
3. Methyltransferase-like proteins in cancer biology and potential therapeutic targeting.. *Journal of hematology & oncology*. PMID: 37533128
4. METTL16 drives leukemogenesis and leukemia stem cell self-renewal by reprogramming BCAA metabolism.. *Cell stem cell*. PMID: 36608679
5. METTL16 promotes glycolytic metabolism reprogramming and colorectal cancer progression.. *Journal of experimental & clinical cancer research : CR*. PMID: 37340443

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.5 |
| 高置信度残基 (pLDDT>90) 占比 | 52.3% |
| 置信残基 (pLDDT 70-90) 占比 | 21.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 20.1% |
| 有序区域 (pLDDT>70) 占比 | 73.5% |
| 可用 PDB 条目 | 2H00, 6B91, 6B92, 6DU4, 6DU5, 6GFK, 6GFN, 6GT5, 6M1U |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2H00, 6B91, 6B92, 6DU4, 6DU5, 6GFK, 6GFN, 6GT5, 6M1U）+ AlphaFold极高置信度预测（pLDDT=78.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017182, IPR010286, IPR029063; Pfam: PF05971 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WTAP | 0.997 | 0.000 | — |
| ZC3H13 | 0.997 | 0.000 | — |
| VIRMA | 0.997 | 0.292 | — |
| RBM15 | 0.996 | 0.000 | — |
| METTL14 | 0.996 | 0.000 | — |
| METTL3 | 0.990 | 0.000 | — |
| RBM15B | 0.966 | 0.000 | — |
| ZCCHC4 | 0.954 | 0.000 | — |
| METTL5 | 0.951 | 0.000 | — |
| CBLL1 | 0.926 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLC39A9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HCCS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| H2AP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| Q7TLC9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |
| EBI-25475914 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |
| ORF4a | psi-mi:"MI:0096"(pull down) | imex:IM-28441|pubmed:33060197 |
| GYPA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GPRC5D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KCNK3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-29540|pubmed:36012204 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.5 + PDB: 2H00, 6B91, 6B92, 6DU4, 6DU5,  | pLDDT=78.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. METTL16 — RNA N(6)-adenosine-methyltransferase METTL16，研究基础较多，新颖性有限。
2. 蛋白大小562 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 156 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 156 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86W50
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127804-METTL16/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=METTL16
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86W50
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000127804-METTL16/subcellular

![](https://images.proteinatlas.org/20352/218_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/20352/218_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/20352/219_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/20352/219_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/20352/220_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/20352/220_E1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86W50-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
