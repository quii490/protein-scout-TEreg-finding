---
type: protein-evaluation
gene: "ABI1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ABI1 — REJECTED (研究热度过高 (PubMed strict=451，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ABI1 / SSH3BP1 |
| 蛋白名称 | Abl interactor 1 |
| 蛋白大小 | 508 aa / 55.1 kDa |
| UniProt ID | Q8IZP0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cell Junctions; UniProt: Cytoplasm; Nucleus; Cell projection, lamellipodium; Cell pro |
| 蛋白大小 | 10/10 | ×1 | 10 | 508 aa / 55.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=451 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.3; PDB: 7LXE |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028457, IPR035725, IPR012849, IPR036028, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cell Junctions | Approved |
| UniProt | Cytoplasm; Nucleus; Cell projection, lamellipodium; Cell projection, filopodium; Cell projection, gr... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin-based cell projection (GO:0098858)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- extracellular exosome (GO:0070062)
- filopodium tip (GO:0032433)
- growth cone (GO:0030426)
- lamellipodium (GO:0030027)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 451 |
| PubMed broad count | 642 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SSH3BP1 |

**关键文献**:
1. ABA perception and signalling.. *Trends in plant science*. PMID: 20493758
2. Regulators of PP2C phosphatase activity function as abscisic acid sensors.. *Science (New York, N.Y.)*. PMID: 19407143
3. Osmotic signaling releases PP2C-mediated inhibition of Arabidopsis SnRK2s via the receptor-like cytoplasmic kinase BIK1.. *The EMBO journal*. PMID: 39433899
4. RBFOX2 deregulation promotes pancreatic cancer progression and metastasis through alternative splicing.. *Nature communications*. PMID: 38114498
5. Phosphorylation dynamics of RAF12 and PP2C control SnRK2 activity under hyperosmotic stress in Arabidopsis.. *Developmental cell*. PMID: 40555240

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.3 |
| 高置信度残基 (pLDDT>90) 占比 | 39.2% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 10.4% |
| 低置信 (pLDDT<50) 占比 | 46.1% |
| 有序区域 (pLDDT>70) 占比 | 43.5% |
| 可用 PDB 条目 | 7LXE |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.3），有序残基占 43.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028457, IPR035725, IPR012849, IPR036028, IPR001452; Pfam: PF07815, PF00018 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WASF2 | 0.999 | 0.915 | — |
| BRK1 | 0.999 | 0.564 | — |
| NCKAP1 | 0.999 | 0.908 | — |
| NCKAP1L | 0.999 | 0.732 | — |
| EPS8 | 0.999 | 0.658 | — |
| CYFIP2 | 0.999 | 0.861 | — |
| WASF1 | 0.999 | 0.888 | — |
| CYFIP1 | 0.999 | 0.838 | — |
| ABL1 | 0.998 | 0.876 | — |
| SOS1 | 0.998 | 0.332 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PYL5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| SRK2E | psi-mi:"MI:0018"(two hybrid) | pubmed:16365038|imex:IM-16528 |
| ACS2 | psi-mi:"MI:0018"(two hybrid) | pubmed:19705149|imex:IM-20377 |
| ACS6 | psi-mi:"MI:0018"(two hybrid) | pubmed:19705149|imex:IM-20377 |
| SWI3B | psi-mi:"MI:0018"(two hybrid) | pubmed:19033529|imex:IM-19099 |
| PYL9 | psi-mi:"MI:0018"(two hybrid) | pubmed:19407143|imex:IM-20307 |
| PYR1 | psi-mi:"MI:0018"(two hybrid) | pubmed:19407142|imex:IM-20308 |
| PYL4 | psi-mi:"MI:0018"(two hybrid) | pubmed:19407142|imex:IM-20308 |
| SRK2D | psi-mi:"MI:0018"(two hybrid) | pubmed:19407142|imex:IM-20308 |
| EBI-16953145 | psi-mi:"MI:0112"(ubiquitin reconstruction) | imex:IM-26362|pubmed:24833385| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.3 + PDB: 7LXE | pLDDT=65.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell projection, lamellipodium / Plasma membrane, Cell Junctions | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ABI1 — Abl interactor 1，研究基础较多，新颖性有限。
2. 蛋白大小508 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 451 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 451 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZP0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136754-ABI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ABI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZP0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ABI1/IF_images/U2OS_2.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ABI1/IF_images/U2OS_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000136754-ABI1/subcellular

![](https://images.proteinatlas.org/68407/1250_A11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/68407/1250_A11_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/68407/1255_A11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68407/1255_A11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/68407/1279_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68407/1279_F12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IZP0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IZP0 |
| SMART | SM00326; |
| UniProt Domain [FT] | DOMAIN 45..107; /note="t-SNARE coiled-coil homology"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00202"; DOMAIN 446..505; /note="SH3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192" |
| InterPro | IPR028457;IPR035725;IPR012849;IPR036028;IPR001452;IPR000727; |
| Pfam | PF07815;PF00018; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000136754-ABI1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABL1 | Intact, Biogrid | true |
| BAIAP2 | Intact, Biogrid, Opencell | true |
| CACNA1A | Intact, Biogrid | true |
| CTTN | Biogrid, Opencell | true |
| CYFIP1 | Intact, Biogrid | true |
| CYFIP2 | Intact, Biogrid | true |
| NCK1 | Intact, Biogrid | true |
| NCKAP1 | Intact, Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
