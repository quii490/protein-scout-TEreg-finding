---
type: protein-evaluation
gene: "CLK1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLK1 — REJECTED (研究热度过高 (PubMed strict=275，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLK1 / CLK |
| 蛋白名称 | Dual specificity protein kinase CLK1 |
| 蛋白大小 | 484 aa / 57.3 kDa |
| UniProt ID | P49759 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear membrane; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 484 aa / 57.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=275 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.1; PDB: 1Z57, 2VAG, 5J1V, 5J1W, 5X8I, 6FT8, 6FT9 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051175, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 275 |
| PubMed broad count | 432 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CLK |

**关键文献**:
1. CLK1 Activates YAP to Promote Intrahepatic Cholangiocarcinogenesis.. *Cancer research*. PMID: 39693605
2. CLK1/SRSF5 pathway induces aberrant exon skipping of METTL14 and Cyclin L2 and promotes growth and metastasis of pancreatic cancer.. *Journal of hematology & oncology*. PMID: 33849617
3. Urinary Complement proteome strongly linked to diabetic kidney disease progression.. *Nature communications*. PMID: 40775226
4. Knockdown of mitochondrial heat shock protein 70 promotes progeria-like phenotypes in caenorhabditis elegans.. *The Journal of biological chemistry*. PMID: 17189267
5. Targeting CLK1/SRSF7 axis-dependent alternative splicing sensitizes pancreatic ductal adenocarcinoma to chemotherapy and immunotherapy.. *Drug resistance updates : reviews and commentaries in antimicrobial and anticancer chemotherapy*. PMID: 40840404

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.1 |
| 高置信度残基 (pLDDT>90) 占比 | 65.9% |
| 置信残基 (pLDDT 70-90) 占比 | 4.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 26.9% |
| 有序区域 (pLDDT>70) 占比 | 70.7% |
| 可用 PDB 条目 | 1Z57, 2VAG, 5J1V, 5J1W, 5X8I, 6FT8, 6FT9, 6FYO, 6G33, 6I5H |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1Z57, 2VAG, 5J1V, 5J1W, 5X8I, 6FT8, 6FT9, 6FYO, 6G33, 6I5H）+ AlphaFold极高置信度预测（pLDDT=79.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051175, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLK4 | 0.959 | 0.000 | — |
| SRSF1 | 0.930 | 0.831 | — |
| DDX23 | 0.859 | 0.206 | — |
| SRSF2 | 0.826 | 0.000 | — |
| CYCS | 0.809 | 0.000 | — |
| TRA2A | 0.799 | 0.712 | — |
| CLK2 | 0.792 | 0.779 | — |
| NKTR | 0.788 | 0.000 | — |
| SRSF3 | 0.758 | 0.540 | — |
| SRPK2 | 0.749 | 0.579 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RCK2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| UBC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SNA3 | psi-mi:"MI:0111"(dihydrofolate reductase reconstru | pubmed:28183979|imex:IM-26166| |
| PIAS4 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| GOLM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| DOCK9 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| 38918" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.1 + PDB: 1Z57, 2VAG, 5J1V, 5J1W, 5X8I,  | pLDDT=79.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. CLK1 — Dual specificity protein kinase CLK1，研究基础较多，新颖性有限。
2. 蛋白大小484 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 275 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 275 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49759
- Protein Atlas: https://www.proteinatlas.org/ENSG00000013441-CLK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49759
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CLK1/IF_images/CLK1_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000013441-CLK1/subcellular

![](https://images.proteinatlas.org/62405/1191_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/62405/1191_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/62405/1194_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/62405/1194_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/62405/1282_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/62405/1282_D9_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P49759-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P49759 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 161..477; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR051175;IPR011009;IPR000719;IPR017441;IPR008271; |
| Pfam | PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000013441-CLK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| YWHAG | Intact, Biogrid | true |
| CLASRP | Biogrid | false |
| CLK2 | Biogrid | false |
| KRTAP10-7 | Intact | false |
| PDE9A | Intact | false |
| PRPF38A | Biogrid | false |
| RBM39 | Biogrid | false |
| SRPK2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
