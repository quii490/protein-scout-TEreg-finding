---
type: protein-evaluation
gene: "LYRM4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LYRM4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LYRM4 / C6orf149, ISD11 |
| 蛋白名称 | LYR motif-containing protein 4 |
| 蛋白大小 | 91 aa / 10.8 kDa |
| UniProt ID | Q9HD34 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; UniProt: Mitochondrion; Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 91 aa / 10.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.2; PDB: 5USR, 5WGB, 5WKP, 5WLW, 6NZU, 6ODD, 6UXE |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008011, IPR045297, IPR051522; Pfam: PF05347 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.0/180** | |
| **归一化总分** | | | **78.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Supported |
| UniProt | Mitochondrion; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- iron-sulfur cluster assembly complex (GO:1990229)
- L-cysteine desulfurase complex (GO:1990221)
- mitochondrial [2Fe-2S] assembly complex (GO:0099128)
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)
- nuclear body (GO:0016604)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf149, ISD11 |

**关键文献**:
1. Integrated functional genomics-identified LYRM4 promotes fumarate accumulation and hepatocellular carcinoma progression.. *Archives of biochemistry and biophysics*. PMID: 40320061
2. Hinokitiol preferentially suppresses metastatic lung adenocarcinoma via TMDD1-mediated ferroptosis induction and iron-sulfur cluster inhibition.. *Cancer letters*. PMID: 40975161
3. High LYRM4-AS1 predicts poor prognosis in patients with glioma and correlates with immune infiltration.. *PeerJ*. PMID: 37810780
4. Mitochondrial-related genome-wide Mendelian randomization identifies putatively causal genes in the pathogenesis of sepsis.. *Surgery*. PMID: 39933430
5. Iron-sulfur cluster ISD11 deficiency (LYRM4 gene) presenting as cardiorespiratory arrest and 3-methylglutaconic aciduria.. *JIMD reports*. PMID: 31497476

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.2 |
| 高置信度残基 (pLDDT>90) 占比 | 86.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.4% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 91.2% |
| 可用 PDB 条目 | 5USR, 5WGB, 5WKP, 5WLW, 6NZU, 6ODD, 6UXE, 6W1D, 6WI2, 6WIH |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5USR, 5WGB, 5WKP, 5WLW, 6NZU, 6ODD, 6UXE, 6W1D, 6WI2, 6WIH）+ AlphaFold极高置信度预测（pLDDT=93.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008011, IPR045297, IPR051522; Pfam: PF05347 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NFS1 | 0.999 | 0.996 | — |
| FXN | 0.999 | 0.885 | — |
| ISCU | 0.999 | 0.923 | — |
| NDUFAB1 | 0.997 | 0.969 | — |
| FDX2 | 0.953 | 0.094 | — |
| HSPA9 | 0.919 | 0.099 | — |
| ACO1 | 0.905 | 0.228 | — |
| FDX1 | 0.879 | 0.094 | — |
| HSCB | 0.866 | 0.407 | — |
| GLRX5 | 0.863 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NECTIN2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| HSPD1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| PDK1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CHCHD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| ISCU | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| FXN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| NFS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| IDE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| DDAH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| ECH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.2 + PDB: 5USR, 5WGB, 5WKP, 5WLW, 6NZU,  | pLDDT=93.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion; Nucleus / Nuclear bodies | 一致 |
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
1. LYRM4 — LYR motif-containing protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小91 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HD34
- Protein Atlas: https://www.proteinatlas.org/ENSG00000214113-LYRM4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LYRM4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HD34
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000214113-LYRM4/subcellular

![](https://images.proteinatlas.org/30362/583_A12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30362/583_A12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30362/598_A12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30362/598_A12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30362/602_A12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30362/602_A12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HD34 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008011;IPR045297;IPR051522; |
| Pfam | PF05347; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000214113-LYRM4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ISCU | Intact, Biogrid, Bioplex | true |
| NDUFAB1 | Biogrid, Bioplex | true |
| NFS1 | Intact, Biogrid | true |
| C1QBP | Biogrid | false |
| CLPP | Biogrid | false |
| CS | Biogrid | false |
| EPS8 | Bioplex | false |
| HSCB | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
