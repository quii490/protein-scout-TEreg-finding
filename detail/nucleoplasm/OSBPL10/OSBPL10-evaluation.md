---
type: protein-evaluation
gene: "OSBPL10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OSBPL10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OSBPL10 / ORP10, OSBP9 |
| 蛋白名称 | Oxysterol-binding protein-related protein 10 |
| 蛋白大小 | 764 aa / 84.0 kDa |
| UniProt ID | Q9BXB5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus, Plasma membrane; 额外: Nucleoplasm; UniProt: Cytoplasm, cytoskeleton |
| 蛋白大小 | 10/10 | ×1 | 10 | 764 aa / 84.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037239, IPR000648, IPR018494, IPR011993, IPR041 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Plasma membrane; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- transporter complex (GO:1990351)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ORP10, OSBP9 |

**关键文献**:
1. Evolutionary history of sickle-cell mutation: implications for global genetic medicine.. *Human molecular genetics*. PMID: 33461216
2. Single-Cell Analysis Combined with Mendelian Randomization Identifies Genes Associated with Prostate Cancer Cells.. *The world journal of men's health*. PMID: 40583027
3. The immune cells have complex causal regulation effects on cancers.. *International immunopharmacology*. PMID: 38710118
4. Comparison of the Mutational Profile between BCL2- and BCL6-Rearrangement Positive Follicular Lymphoma.. *The Journal of molecular diagnostics : JMD*. PMID: 40482882
5. OSBPL10, RXRA and lipid metabolism confer African-ancestry protection against dengue haemorrhagic fever in admixed Cubans.. *PLoS pathogens*. PMID: 28241052

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.3 |
| 高置信度残基 (pLDDT>90) 占比 | 44.9% |
| 置信残基 (pLDDT 70-90) 占比 | 21.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.8% |
| 低置信 (pLDDT<50) 占比 | 27.9% |
| 有序区域 (pLDDT>70) 占比 | 66.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.3，有序区 66.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037239, IPR000648, IPR018494, IPR011993, IPR041680; Pfam: PF01237, PF15409 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| IKBKG | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| USP11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| MMP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| NIPSNAP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SAP18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CLINT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| PGAM5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| ALDOA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SRRM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.3 + PDB: 无 | pLDDT=73.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton / Golgi apparatus, Plasma membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. OSBPL10 — Oxysterol-binding protein-related protein 10，非常新颖，仅有少数基础研究。
2. 蛋白大小764 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXB5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144645-OSBPL10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OSBPL10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BXB5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000144645-OSBPL10/subcellular

![](https://images.proteinatlas.org/3636/77_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3636/77_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3636/78_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3636/78_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3636/92_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3636/92_H2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BXB5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
