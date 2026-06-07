---
type: protein-evaluation
gene: "MOB1A"
date: 2026-06-03
tags: [protein-scout, nucleolus, re-evaluation, recovery]
status: scored
category: nucleolus
normalized_score: 68.9
raw_score: 126.0
nuclear_score: 7
---

## MOB1A 核蛋白评估报告 (Full Re-evaluation)


### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MOB1A / C2orf6, MOB4B, MOBK1B, MOBKL1B |
| 蛋白名称 | MOB kinase activator 1A |
| 蛋白大小 | 216 aa / 25.1 kDa |
| UniProt ID | Q9H8S9 |
| PubMed (strict) | 43 |
| PubMed (broad) | 89 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; Nucleoplasm, Cytosol; UniProt: 无注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 216 aa / 25.1 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=43 篇 (41-60→6) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=88.3，PDB: 1PI1, 4J1V, 4JIZ, 5BRK, 5BRM, 5TWF, 5TWG |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR005301, IPR036703; Pfam: PF03637 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners, IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/183** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持，部分数据源提示非核定位但核信号主导。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 89 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C2orf6, MOB4B, MOBK1B, MOBKL1B |

**关键文献**:
1. MOB kinase activator 1A acts as an oncogene by targeting PI3K/AKT/mTOR in ovarian cancer.. *Discover oncology*. PMID: 37314589
2. AtMOB1 Genes Regulate Jasmonate Accumulation and Plant Development.. *Plant physiology*. PMID: 31862839
3. The Legionella kinase LegK7 exploits the Hippo pathway scaffold protein MOB1A for allostery and substrate phosphorylation.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 32513747
4. The Arabidopsis thaliana Mob1A gene is required for organ growth and correct tissue patterning of the root tip.. *Annals of botany*. PMID: 24201137
5. The Arabidopsis AGC kinases NDR2/4/5 interact with MOB1A/1B and play important roles in pollen development and germination.. *The Plant journal : for cell and molecular biology*. PMID: 33215783

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.3 |
| 高置信度残基 (pLDDT>90) 占比 | 73.1% |
| 置信残基 (pLDDT 70-90) 占比 | 15.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 6.5% |
| 有序区域 (pLDDT>70) 占比 | 88.4% |
| 可用 PDB 条目 | 1PI1, 4J1V, 4JIZ, 5BRK, 5BRM, 5TWF, 5TWG, 5TWH, 5XQZ, 6MCP |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1PI1, 4J1V, 4JIZ, 5BRK, 5BRM, 5TWF, 5TWG, 5TWH, 5XQZ, 6MCP）+ AlphaFold极高置信度预测（pLDDT=88.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005301, IPR036703; Pfam: PF03637 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STK38L | 0.999 | 0.996 | — |
| STK4 | 0.999 | 0.983 | — |
| LATS1 | 0.999 | 0.987 | — |
| STK3 | 0.998 | 0.979 | — |
| LATS2 | 0.997 | 0.898 | — |
| MOB1B | 0.982 | 0.815 | — |
| STK38 | 0.974 | 0.908 | — |
| SAV1 | 0.967 | 0.253 | — |
| PPP2R2A | 0.858 | 0.841 | — |
| PPP2R2B | 0.851 | 0.841 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KXD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CALM1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16512683|imex:IM-19867 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SGK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NUP98 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| STK38L | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1052818 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| BB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MPG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**已知复合体成员** (GO Cellular Component):
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.3 + PDB: 1PI1, 4J1V, 4JIZ, 5BRK, 5BRM,  | pLDDT=88.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MOB1A — MOB kinase activator 1A，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小216 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 43 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H8S9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114978-MOB1A
- Protein Atlas Subcellular: https://www.proteinatlas.org/ENSG00000114978-MOB1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MOB1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H8S9
- STRING: https://string-db.org/network
- IntAct: https://www.ebi.ac.uk/intact/search?query=MOB1A
- Packet data timestamp: 2026-06-03 21:48:31

---

*本报告基于最新的 harvest packet 数据（2026-06-03 21:48:31），各数据库实时抓取。评分严格遵循 /180 加权评分体系：核定位×4 + 大小×1 + 新颖性×5 + 结构×3 + 结构域×2 + PPI×3 + 互证加分（max+3）。PubMed>100 或 核定位≤3 为 REJECTED。*

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000114978-MOB1A/subcellular

![](https://images.proteinatlas.org/71690/1385_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/71690/1385_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/71690/1394_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/71690/1394_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/71690/1492_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/71690/1492_F1_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H8S9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H8S9 |
| SMART | SM01388; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR005301;IPR036703; |
| Pfam | PF03637; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000114978-MOB1A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LATS1 | Intact, Biogrid | true |
| LATS2 | Intact, Biogrid | true |
| STK3 | Intact, Biogrid | true |
| STK38 | Intact, Biogrid | true |
| STK38L | Intact, Biogrid, Opencell, Bioplex | true |
| STK4 | Intact, Biogrid | true |
| ANKRD28 | Biogrid | false |
| ANKRD44 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
