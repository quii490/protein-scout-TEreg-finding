---
type: protein-evaluation
gene: "LBR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LBR — REJECTED (研究热度过高 (PubMed strict=270，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LBR |
| 蛋白名称 | Delta(14)-sterol reductase LBR |
| 蛋白大小 | 615 aa / 70.7 kDa |
| UniProt ID | Q14739 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; 额外: Nucleoli fibrillar center; UniProt: Nucleus inner membrane; Endoplasmic reticulum membrane; Cyto |
| 蛋白大小 | 10/10 | ×1 | 10 | 615 aa / 70.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=270 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=76.6; PDB: 2DIG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001171, IPR019023, IPR018083, IPR002999; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.0/180** | |
| **归一化总分** | | | **48.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane; 额外: Nucleoli fibrillar center | Supported |
| UniProt | Nucleus inner membrane; Endoplasmic reticulum membrane; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endoplasmic reticulum membrane (GO:0005789)
- fibrillar center (GO:0001650)
- membrane (GO:0016020)
- nuclear envelope (GO:0005635)
- nuclear inner membrane (GO:0005637)
- nuclear lamina (GO:0005652)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 270 |
| PubMed broad count | 1966 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Expanding the genetic architecture and phenotypic spectrum in the skeletal ciliopathies.. *Human mutation*. PMID: 29068549
2. Fremanezumab.. **. PMID: 30371997
3. Human Genetics of Ventricular Septal Defect.. *Advances in experimental medicine and biology*. PMID: 38884729
4. Nuclear assembly.. *Annual review of cell and developmental biology*. PMID: 9442884
5. Evenly Distributed Protein Intake over 3 Meals Augments Resistance Exercise-Induced Muscle Hypertrophy in Healthy Young Men.. *The Journal of nutrition*. PMID: 32321161

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.6 |
| 高置信度残基 (pLDDT>90) 占比 | 44.9% |
| 置信残基 (pLDDT 70-90) 占比 | 30.7% |
| 中等置信 (pLDDT 50-70) 占比 | 1.6% |
| 低置信 (pLDDT<50) 占比 | 22.8% |
| 有序区域 (pLDDT>70) 占比 | 75.6% |
| 可用 PDB 条目 | 2DIG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=76.6，有序区 75.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001171, IPR019023, IPR018083, IPR002999; Pfam: PF01222, PF09465 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LMNB1 | 0.999 | 0.335 | — |
| LMNB2 | 0.998 | 0.086 | — |
| CYP51A1 | 0.993 | 0.782 | — |
| MSMO1 | 0.976 | 0.400 | — |
| MECP2 | 0.975 | 0.292 | — |
| EMD | 0.967 | 0.125 | — |
| CBX3 | 0.955 | 0.295 | — |
| DHCR24 | 0.950 | 0.000 | — |
| SC5D | 0.941 | 0.782 | — |
| LEMD3 | 0.941 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Atpalpha | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PHLDA3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| 7242199 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| CBX3 | psi-mi:"MI:0018"(two hybrid) | pubmed:8663349 |
| CBX5 | psi-mi:"MI:0018"(two hybrid) | pubmed:8663349 |
| ARRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| CLK3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.6 + PDB: 2DIG | pLDDT=76.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus inner membrane; Endoplasmic reticulum memb / Nuclear membrane; 额外: Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. LBR — Delta(14)-sterol reductase LBR，研究基础较多，新颖性有限。
2. 蛋白大小615 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 270 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 270 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14739
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143815-LBR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LBR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14739
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000143815-LBR/subcellular

![](https://images.proteinatlas.org/62236/1104_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/62236/1104_A5_3_red_green.jpg)
![](https://images.proteinatlas.org/62236/1127_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/62236/1127_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/62236/1171_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/62236/1171_H7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14739-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14739 |
| SMART | SM00333; |
| UniProt Domain [FT] | DOMAIN 1..62; /note="Tudor" |
| InterPro | IPR001171;IPR019023;IPR018083;IPR002999; |
| Pfam | PF01222;PF09465; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000143815-LBR/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C1QBP | Intact, Biogrid, Opencell | true |
| CANX | Biogrid, Opencell | true |
| CBX3 | Intact, Biogrid | true |
| CBX5 | Intact, Biogrid | true |
| LMNB1 | Biogrid, Opencell | true |
| YWHAG | Intact, Biogrid, Opencell | true |
| YWHAH | Biogrid, Opencell | true |
| ARF6 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
