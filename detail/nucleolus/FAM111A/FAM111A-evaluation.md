---
type: protein-evaluation
gene: "FAM111A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM111A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM111A / KIAA1895 |
| 蛋白名称 | Serine protease FAM111A |
| 蛋白大小 | 611 aa / 70.2 kDa |
| UniProt ID | Q96PZ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli fibrillar center; UniProt: Nucleus; Chromosome; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 611 aa / 70.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=76.7; PDB: 8S9K, 8S9L |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009003, IPR043504; Pfam: PF13365 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli fibrillar center | Approved |
| UniProt | Nucleus; Chromosome; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 85 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1895 |

**关键文献**:
1. Human FAM111A inhibits vaccinia virus replication by degrading viral protein I3 and is antagonized by poxvirus host range factor SPI-1.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37607234
2. Functions and evolution of FAM111 serine proteases.. *Frontiers in molecular biosciences*. PMID: 36589246
3. FAM111A regulates replication origin activation and cell fitness.. *Life science alliance*. PMID: 37793778
4. FAM111A protects replication forks from protein obstacles via its trypsin-like domain.. *Nature communications*. PMID: 32165630
5. From the TOP: Formation, recognition and resolution of topoisomerase DNA protein crosslinks.. *DNA repair*. PMID: 39180935

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.7 |
| 高置信度残基 (pLDDT>90) 占比 | 38.5% |
| 置信残基 (pLDDT 70-90) 占比 | 34.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.7% |
| 低置信 (pLDDT<50) 占比 | 18.8% |
| 有序区域 (pLDDT>70) 占比 | 72.5% |
| 可用 PDB 条目 | 8S9K, 8S9L |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8S9K, 8S9L）+ AlphaFold高质量预测（pLDDT=76.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009003, IPR043504; Pfam: PF13365 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TBCE-2 | 0.950 | 0.000 | — |
| TBCE | 0.950 | 0.000 | — |
| BRCA1 | 0.590 | 0.439 | — |
| SPRTN | 0.528 | 0.000 | — |
| PTH | 0.527 | 0.000 | — |
| GCNA | 0.507 | 0.000 | — |
| TMEM260 | 0.503 | 0.000 | — |
| AMZ1 | 0.472 | 0.000 | — |
| CUL7 | 0.468 | 0.000 | — |
| CUL9 | 0.464 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| rph | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SF3A1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TP53 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NCSTN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CDC23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| URS00000A07C1_10090 | psi-mi:"MI:0096"(pull down) | pubmed:29867223|imex:IM-24989 |
| NOP56 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RPL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RBM4B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RPLP0 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.7 + PDB: 8S9K, 8S9L | pLDDT=76.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Cytoplasm / Nucleoplasm, Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM111A — Serine protease FAM111A，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小611 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96PZ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166801-FAM111A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM111A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96PZ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000166801-FAM111A/subcellular

![](https://images.proteinatlas.org/40176/412_G8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40176/412_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40176/419_G8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40176/419_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40176/471_G8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40176/471_G8_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96PZ2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
