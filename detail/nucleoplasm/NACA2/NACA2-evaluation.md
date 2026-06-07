---
type: protein-evaluation
gene: "NACA2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NACA2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NACA2 / NACAL |
| 蛋白名称 | Nascent polypeptide-associated complex subunit alpha-2 |
| 蛋白大小 | 215 aa / 23.2 kDa |
| UniProt ID | Q9H009 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 215 aa / 23.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016641, IPR044034, IPR038187, IPR002715; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nascent polypeptide-associated complex (GO:0005854)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NACAL |

**关键文献**:
1. NCX1 Na/Ca exchanger inhibition by antisense oligonucleotides in mouse distal convoluted tubule cells.. *Kidney international*. PMID: 9734614
2. Studies of TBX4 and chromosome 17q23.1q23.2: an uncommon cause of nonsyndromic clubfoot.. *American journal of medical genetics. Part A*. PMID: 22678995
3. Structural and functional analysis of Na+/Ca2+ exchange in distal convoluted tubule cells.. *The American journal of physiology*. PMID: 8853417
4. Na/Ca exchanger isoforms expressed in kidney.. *The American journal of physiology*. PMID: 7694482
5. Role of calcium-sensing receptor in regulating activation susceptibility of postovulatory aging mouse oocytes.. *The Journal of reproduction and development*. PMID: 37245986

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.4 |
| 高置信度残基 (pLDDT>90) 占比 | 41.4% |
| 置信残基 (pLDDT 70-90) 占比 | 13.5% |
| 中等置信 (pLDDT 50-70) 占比 | 17.7% |
| 低置信 (pLDDT<50) 占比 | 27.4% |
| 有序区域 (pLDDT>70) 占比 | 54.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.4，有序区 54.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016641, IPR044034, IPR038187, IPR002715; Pfam: PF01849, PF19026 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BTF3 | 0.992 | 0.964 | — |
| RPL7A | 0.963 | 0.829 | — |
| RPL13 | 0.957 | 0.852 | — |
| RPL23A | 0.953 | 0.842 | — |
| RPL23 | 0.949 | 0.849 | — |
| RPL18 | 0.947 | 0.820 | — |
| RPL5 | 0.946 | 0.828 | — |
| RPL18A | 0.943 | 0.829 | — |
| RPL9 | 0.942 | 0.821 | — |
| RPL8 | 0.941 | 0.820 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BTF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KCNJ2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:32541000|imex:IM-29166 |
| BTF3L4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.4 + PDB: 无 | pLDDT=72.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NACA2 — Nascent polypeptide-associated complex subunit alpha-2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小215 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H009
- Protein Atlas: https://www.proteinatlas.org/ENSG00000253506-NACA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NACA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H009
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000253506-NACA2/subcellular

![](https://images.proteinatlas.org/73152/1437_A6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/73152/1437_A6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/73152/1564_G4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/73152/1564_G4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/73152/1668_A6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/73152/1668_A6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H009-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H009 |
| SMART | SM01407; |
| UniProt Domain [FT] | DOMAIN 70..135; /note="NAC-A/B"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00507"; DOMAIN 176..213; /note="UBA" |
| InterPro | IPR016641;IPR044034;IPR038187;IPR002715; |
| Pfam | PF01849;PF19026; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000253506-NACA2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BTF3 | Biogrid, Opencell | true |
| BTF3L4 | Biogrid, Bioplex | true |
| VCP | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
