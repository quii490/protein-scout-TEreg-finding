---
type: protein-evaluation
gene: "CKAP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CKAP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CKAP2 / LB1, TMAP |
| 蛋白名称 | Cytoskeleton-associated protein 2 |
| 蛋白大小 | 683 aa / 77.0 kDa |
| UniProt ID | Q8WWK9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Microtubules, Mitotic spindle, Primary cilium; 额外: Centrosom; UniProt: Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, spindle; C |
| 蛋白大小 | 10/10 | ×1 | 10 | 683 aa / 77.0 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=65 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029197, IPR026165; Pfam: PF15297 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules, Mitotic spindle, Primary cilium; 额外: Centrosome, Basal body | Supported |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, spindle; Cytoplasm, cytoskeleton, spindle pole | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cilium (GO:0005929)
- microtubule (GO:0005874)
- microtubule cytoskeleton (GO:0015630)
- mitotic spindle (GO:0072686)
- nucleolus (GO:0005730)
- spindle pole (GO:0000922)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 65 |
| PubMed broad count | 94 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LB1, TMAP |

**关键文献**:
1. A multidimensional systems biology analysis of cellular senescence in aging and disease.. *Genome biology*. PMID: 32264951
2. Identification and validation of CKAP2 as a novel biomarker in the development and progression of rheumatoid arthritis.. *Frontiers in immunology*. PMID: 40636121
3. Structurally divergent and recurrently mutated regions of primate genomes.. *Cell*. PMID: 38428424
4. The mitotic spindle protein CKAP2 potently increases formation and stability of microtubules.. *eLife*. PMID: 35029146
5. The spindle protein CKAP2 regulates microtubule dynamics and ensures faithful chromosome segregation.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38381793

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.8 |
| 高置信度残基 (pLDDT>90) 占比 | 9.8% |
| 置信残基 (pLDDT 70-90) 占比 | 26.4% |
| 中等置信 (pLDDT 50-70) 占比 | 12.7% |
| 低置信 (pLDDT<50) 占比 | 51.1% |
| 有序区域 (pLDDT>70) 占比 | 36.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.8），有序残基占 36.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029197, IPR026165; Pfam: PF15297 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CENPF | 0.934 | 0.000 | — |
| TOP2A | 0.898 | 0.000 | — |
| BUB1B | 0.886 | 0.000 | — |
| BUB1 | 0.879 | 0.000 | — |
| ASPM | 0.869 | 0.000 | — |
| TTK | 0.868 | 0.000 | — |
| KIF20A | 0.861 | 0.000 | — |
| CEP55 | 0.857 | 0.196 | — |
| CDK1 | 0.842 | 0.045 | — |
| DLGAP5 | 0.838 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IGHA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15174051|imex:IM-19123 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| TANK | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| TMEM171 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRAK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP1R15A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-23248|pubmed:29109149 |
| Wdr5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MIS12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| OTUB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-23897|pubmed:26752685 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.8 + PDB: 无 | pLDDT=58.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton,  / Microtubules, Mitotic spindle, Primary cilium; 额外: | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. CKAP2 — Cytoskeleton-associated protein 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小683 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 65 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=58.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WWK9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136108-CKAP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CKAP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WWK9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Microtubules (supported)。来源: https://www.proteinatlas.org/ENSG00000136108-CKAP2/subcellular

![](https://images.proteinatlas.org/8410/100_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8410/100_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/8410/101_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8410/101_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/8410/2069_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8410/2069_B2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WWK9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WWK9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029197;IPR026165; |
| Pfam | PF15297; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000136108-CKAP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KIF22 | Biogrid, Opencell | true |
| KIF2A | Biogrid, Opencell | true |
| MAPRE1 | Biogrid, Opencell | true |
| ACTG1 | Opencell | false |
| CEP55 | Opencell | false |
| DCTN1 | Biogrid | false |
| DDOST | Opencell | false |
| DYNLT1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
