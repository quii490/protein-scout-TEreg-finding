---
type: protein-evaluation
gene: "PUS3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PUS3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PUS3 |
| 蛋白名称 | tRNA pseudouridine(38/39) synthase |
| 蛋白大小 | 481 aa / 55.6 kDa |
| UniProt ID | Q9BZE2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 481 aa / 55.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.7; PDB: 8OKD, 9ENB, 9ENC, 9ENE, 9ENF, 9F9Q |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR020103, IPR001406, IPR020097, IPR020095, IPR041 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 62 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification and validation of key biomarkers based on RNA methylation genes in sepsis.. *Frontiers in immunology*. PMID: 37701433
2. Destabilization of mutated human PUS3 protein causes intellectual disability.. *Human mutation*. PMID: 36125428
3. Clinical and molecular delineation of PUS3-associated neurodevelopmental disorders.. *Clinical genetics*. PMID: 34415064
4. DISTINCT ROLES OF VIRAL US3 AND UL13 PROTEIN KINASES IN HERPES VIRUS SIMPLEX TYPE 1 (HSV-1) NUCLEAR EGRESS.. *bioRxiv : the preprint server for biology*. PMID: 36993506
5. Differentiating the Roles of UL16, UL21, and Us3 in the Nuclear Egress of Herpes Simplex Virus Capsids.. *Journal of virology*. PMID: 32321804

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.7 |
| 高置信度残基 (pLDDT>90) 占比 | 62.8% |
| 置信残基 (pLDDT 70-90) 占比 | 16.4% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 12.5% |
| 有序区域 (pLDDT>70) 占比 | 79.2% |
| 可用 PDB 条目 | 8OKD, 9ENB, 9ENC, 9ENE, 9ENF, 9F9Q |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8OKD, 9ENB, 9ENC, 9ENE, 9ENF, 9F9Q）+ AlphaFold极高置信度预测（pLDDT=83.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020103, IPR001406, IPR020097, IPR020095, IPR041707; Pfam: PF01416 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRUB1 | 0.913 | 0.128 | — |
| PUS7 | 0.888 | 0.088 | — |
| PUS7L | 0.858 | 0.079 | — |
| TRUB2 | 0.843 | 0.128 | — |
| RPUSD4 | 0.840 | 0.000 | — |
| RPUSD2 | 0.821 | 0.000 | — |
| WDR4 | 0.810 | 0.288 | — |
| PUS10 | 0.784 | 0.000 | — |
| RPUSD1 | 0.783 | 0.000 | — |
| MRPL17 | 0.782 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DEG1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| PFD1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| CCT5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| PDZK1 | psi-mi:"MI:0900"(p8 filamentous phage display) | imex:IM-26482|pubmed:30126976 |
| PRKAB2 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| MAP2K4 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| MAD2L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PAK5 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.7 + PDB: 8OKD, 9ENB, 9ENC, 9ENE, 9ENF,  | pLDDT=83.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

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
1. PUS3 — tRNA pseudouridine(38/39) synthase，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小481 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BZE2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110060-PUS3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PUS3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BZE2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000110060-PUS3/subcellular

![](https://images.proteinatlas.org/38040/422_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/38040/422_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/38040/423_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/38040/423_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/38040/426_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/38040/426_E1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BZE2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
