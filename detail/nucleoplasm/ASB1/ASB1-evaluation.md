---
type: protein-evaluation
gene: "ASB1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ASB1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ASB1 / KIAA1146 |
| 蛋白名称 | Ankyrin repeat and SOCS box protein 1 |
| 蛋白大小 | 335 aa / 37.0 kDa |
| UniProt ID | Q9Y576 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 335 aa / 37.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002110, IPR036770, IPR037331, IPR001496, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- ubiquitin ligase complex (GO:0000151)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 111 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1146 |

**关键文献**:
1. ASB1 engages with ELOB to facilitate SQOR ubiquitination and H(2)S homeostasis during spermiogenesis.. *Redox biology*. PMID: 39733518
2. Helicobacter heilmannii sp. nov., isolated from feline gastric mucosa.. *International journal of systematic and evolutionary microbiology*. PMID: 21421932
3. Coordinated cytokinin signaling and auxin biosynthesis mediates arsenate-induced root growth inhibition.. *Plant physiology*. PMID: 33793921
4. An unconventional role of an ASB family protein in NF-κB activation and inflammatory response during microbial infection and colitis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 33431678
5. ASB1 differential methylation in ischaemic cardiomyopathy: relationship with left ventricular performance in end-stage heart failure patients.. *ESC heart failure*. PMID: 29667349

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.7 |
| 高置信度残基 (pLDDT>90) 占比 | 53.7% |
| 置信残基 (pLDDT 70-90) 占比 | 18.5% |
| 中等置信 (pLDDT 50-70) 占比 | 15.8% |
| 低置信 (pLDDT<50) 占比 | 11.9% |
| 有序区域 (pLDDT>70) 占比 | 72.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.7，有序区 72.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR037331, IPR001496, IPR036036; Pfam: PF12796, PF13606, PF07525 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL5 | 0.954 | 0.780 | — |
| ELOB | 0.888 | 0.610 | — |
| RNF7 | 0.868 | 0.450 | — |
| ELOC | 0.850 | 0.634 | — |
| TRAF3IP1 | 0.797 | 0.127 | — |
| CISH | 0.756 | 0.000 | — |
| ASB6 | 0.669 | 0.087 | — |
| CAND1 | 0.646 | 0.292 | — |
| UBE2F | 0.610 | 0.045 | — |
| NEDD8 | 0.563 | 0.100 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BSK5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| Eloc | psi-mi:"MI:0231"(mammalian protein protein interac | pubmed:19159283|imex:IM-20301 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| TSHB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CASQ2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SETDB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| LMO3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| YWHAG | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| KAT5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32814053|imex:IM-28217| |
| RNF7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.7 + PDB: 无 | pLDDT=80.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. ASB1 — Ankyrin repeat and SOCS box protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小335 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y576
- Protein Atlas: https://www.proteinatlas.org/ENSG00000065802-ASB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ASB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y576
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000065802-ASB1/subcellular

![](https://images.proteinatlas.org/3508/1165_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/3508/1165_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/3508/71_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/3508/71_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/3508/73_A2_1_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y576-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y576 |
| SMART | SM00248;SM00969; |
| UniProt Domain [FT] | DOMAIN 286..335; /note="SOCS box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00194" |
| InterPro | IPR002110;IPR036770;IPR037331;IPR001496;IPR036036; |
| Pfam | PF12796;PF13606;PF07525; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000065802-ASB1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CUL5 | Intact, Biogrid, Bioplex | true |
| RNF7 | Intact, Biogrid, Bioplex | true |
| ELOB | Biogrid | false |
| ELOC | Biogrid | false |
| KAT5 | Intact | false |
| YWHAG | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
