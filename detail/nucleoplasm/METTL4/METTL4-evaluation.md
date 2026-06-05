---
type: protein-evaluation
gene: "METTL4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## METTL4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | METTL4 |
| 蛋白名称 | N(6)-adenine-specific methyltransferase METTL4 |
| 蛋白大小 | 472 aa / 54.0 kDa |
| UniProt ID | Q8N3J2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; UniProt: Nucleus; Cytoplasm, cytosol; Mitochondrion matrix |
| 蛋白大小 | 10/10 | ×1 | 10 | 472 aa / 54.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002052, IPR007757, IPR029063; Pfam: PF05063 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Approved |
| UniProt | Nucleus; Cytoplasm, cytosol; Mitochondrion matrix | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- mitochondrial matrix (GO:0005759)
- nucleus (GO:0005634)
- RNA N6-methyladenosine methyltransferase complex (GO:0036396)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 88 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. METTL4-Mediated Mitochondrial DNA N6-Methyldeoxyadenosine Promoting Macrophage Inflammation and Atherosclerosis.. *Circulation*. PMID: 39687989
2. RNA m6A methylation across the transcriptome.. *Molecular cell*. PMID: 36736310
3. Rectifying METTL4-Mediated N(6)-Methyladenine Excess in Mitochondrial DNA Alleviates Heart Failure.. *Circulation*. PMID: 38686562
4. Methyltransferase-like proteins in cancer biology and potential therapeutic targeting.. *Journal of hematology & oncology*. PMID: 37533128
5. Targeting N(6)-Methyladenine of Tubular Mitochondrial DNA Against Hypertensive CKD.. *Hypertension (Dallas, Tex. : 1979)*. PMID: 40677234

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.2 |
| 高置信度残基 (pLDDT>90) 占比 | 51.7% |
| 置信残基 (pLDDT 70-90) 占比 | 17.8% |
| 中等置信 (pLDDT 50-70) 占比 | 9.7% |
| 低置信 (pLDDT<50) 占比 | 20.8% |
| 有序区域 (pLDDT>70) 占比 | 69.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.2，有序区 69.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002052, IPR007757, IPR029063; Pfam: PF05063 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| METTL3 | 0.999 | 0.000 | — |
| WTAP | 0.993 | 0.000 | — |
| METTL14 | 0.992 | 0.000 | — |
| VIRMA | 0.942 | 0.000 | — |
| RBM15 | 0.860 | 0.000 | — |
| ALKBH1 | 0.761 | 0.000 | — |
| N6AMT1 | 0.749 | 0.000 | — |
| METTL16 | 0.726 | 0.000 | — |
| ALKBH5 | 0.702 | 0.000 | — |
| ALKBH4 | 0.669 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| loqs | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| cold | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| drd | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| BNIP3 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| ENST00000319888 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.2 + PDB: 无 | pLDDT=77.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol; Mitochondrion matrix / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. METTL4 — N(6)-adenine-specific methyltransferase METTL4，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小472 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N3J2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101574-METTL4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=METTL4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N3J2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/METTL4/IF_images/U-2_OS_2.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/METTL4/IF_images/U-2_OS_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000101574-METTL4/subcellular

![](https://images.proteinatlas.org/40061/461_H8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40061/461_H8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40061/462_H8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/40061/462_H8_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/40061/464_H8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40061/464_H8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N3J2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
