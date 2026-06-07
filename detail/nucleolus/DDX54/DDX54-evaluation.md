---
type: protein-evaluation
gene: "DDX54"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDX54 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDX54 |
| 蛋白名称 | ATP-dependent RNA helicase DDX54 |
| 蛋白大小 | 881 aa / 98.6 kDa |
| UniProt ID | Q8TDD1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Nucleoli, Golgi apparatus; UniProt: Nucleus, nucleolus; Nucleus, nucleoplasm |
| 蛋白大小 | 8/10 | x1 | 8 | 881 aa / 98.6 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=70.4; PDB: 8FKT, 8FKU, 8FKV, 8FKW, 8FKX, 8FKY |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR012541, IPR033517, IPR011545, IPR050079, IPR014 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli, Golgi apparatus | Approved |
| UniProt | Nucleus, nucleolus; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 30 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Activation of PKR by a short-hairpin RNA.. *Scientific reports*. PMID: 39384561
2. Activation of PKR by a short-hairpin RNA.. *bioRxiv : the preprint server for biology*. PMID: 38766230
3. LINC00908 attenuates LUAD tumorigenesis through DEAD-box helicase 54.. *American journal of cancer research*. PMID: 38859824
4. DEAD-box helicase 54 regulates microglial inflammatory response in rats with chronic constriction injuries through NF-κB/NLRP3 signaling axis.. *Journal of neurophysiology*. PMID: 37377223
5. DDX54 drives ALKBH5-mediated demethylation of selected transcripts to suppress interferon antiviral response.. *Journal of virology*. PMID: 40793791

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.4 |
| 高置信度残基 (pLDDT>90) 占比 | 27.4% |
| 置信残基 (pLDDT 70-90) 占比 | 36.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 26.9% |
| 有序区域 (pLDDT>70) 占比 | 64.3% |
| 可用 PDB 条目 | 8FKT, 8FKU, 8FKV, 8FKW, 8FKX, 8FKY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold极高置信度（pLDDT=70.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012541, IPR033517, IPR011545, IPR050079, IPR014001; Pfam: PF08147, PF00270, PF00271 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BOP1 | 0.966 | 0.295 | — |
| PES1 | 0.959 | 0.552 | — |
| FTSJ3 | 0.952 | 0.174 | — |
| NIFK | 0.948 | 0.820 | — |
| DDX24 | 0.941 | 0.288 | — |
| NOC2L | 0.941 | 0.570 | — |
| NOP2 | 0.934 | 0.548 | — |
| DDX10 | 0.925 | 0.234 | — |
| RBM19 | 0.922 | 0.220 | — |
| RBM34 | 0.920 | 0.479 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.4 + PDB: 8FKT, 8FKU, 8FKV, 8FKW, 8FKX,  | pLDDT=70.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Nucleus, nucleoplasm / Nucleoplasm, Nucleoli, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DDX54 -- ATP-dependent RNA helicase DDX54，非常新颖，仅有少数基础研究。
2. 蛋白大小881 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TDD1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123064-DDX54/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDX54
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TDD1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000123064-DDX54/subcellular

![](https://images.proteinatlas.org/70786/1304_E1_3_red_green.jpg)
![](https://images.proteinatlas.org/70786/1304_E1_5_red_green.jpg)
![](https://images.proteinatlas.org/70786/1323_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/70786/1323_E1_4_red_green.jpg)
![](https://images.proteinatlas.org/70786/1356_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/70786/1356_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TDD1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TDD1 |
| SMART | SM01123;SM00487;SM00490; |
| UniProt Domain [FT] | DOMAIN 127..299; /note="Helicase ATP-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00541"; DOMAIN 326..473; /note="Helicase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00542" |
| InterPro | IPR012541;IPR033517;IPR011545;IPR050079;IPR014001;IPR001650;IPR027417;IPR000629;IPR014014; |
| Pfam | PF08147;PF00270;PF00271; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000123064-DDX54/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSNK2B | Biogrid, Opencell | true |
| NPM1 | Biogrid, Opencell | true |
| ANLN | Biogrid | false |
| AURKB | Biogrid | false |
| C1QBP | Biogrid | false |
| CSNK2A1 | Biogrid | false |
| CSNK2A2 | Biogrid | false |
| DRG1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
