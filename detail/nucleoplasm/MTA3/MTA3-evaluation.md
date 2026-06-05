---
type: protein-evaluation
gene: "MTA3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MTA3 — REJECTED (研究热度过高 (PubMed strict=101，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MTA3 / KIAA1266 |
| 蛋白名称 | Metastasis-associated protein MTA3 |
| 蛋白大小 | 594 aa / 67.5 kDa |
| UniProt ID | Q9BTC8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 594 aa / 67.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=101 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001025, IPR043151, IPR000949, IPR009057, IPR040 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- NuRD complex (GO:0016581)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 101 |
| PubMed broad count | 141 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1266 |

**关键文献**:
1. Sphingosine kinase 1 promotes tumor immune evasion by regulating the MTA3-PD-L1 axis.. *Cellular & molecular immunology*. PMID: 36050478
2. The Many Faces of MTA3 Protein in Normal Development and Cancers.. *Current protein & peptide science*. PMID: 27033852
3. The feedback loop between MTA1 and MTA3/TRIM21 modulates stemness of breast cancer in response to estrogen.. *Cell death & disease*. PMID: 39154024
4. T2DM-elicited oxidative stress represses MTA3 expression in mouse Leydig cells.. *Reproduction (Cambridge, England)*. PMID: 35239504
5. The metastasis-associated protein MTA3 promotes cardiac repair by inhibiting the fibroblast to myofibroblast transition during fibrosis.. *The Journal of biological chemistry*. PMID: 40615041

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.3 |
| 高置信度残基 (pLDDT>90) 占比 | 48.8% |
| 置信残基 (pLDDT 70-90) 占比 | 25.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 19.4% |
| 有序区域 (pLDDT>70) 占比 | 74.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.3，有序区 74.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001025, IPR043151, IPR000949, IPR009057, IPR040138; Pfam: PF01426, PF01448, PF00320 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RBBP7 | 0.999 | 0.904 | — |
| HDAC1 | 0.999 | 0.904 | — |
| RBBP4 | 0.998 | 0.898 | — |
| CHD4 | 0.998 | 0.864 | — |
| CHD3 | 0.998 | 0.818 | — |
| HDAC2 | 0.998 | 0.872 | — |
| GATAD2A | 0.995 | 0.844 | — |
| GATAD2B | 0.993 | 0.892 | — |
| MTA1 | 0.993 | 0.777 | — |
| MBD3 | 0.989 | 0.908 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ARNT | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Sall4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Esrrb | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| KDM1A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12083|pubmed:19703393 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:19505873|imex:IM-20483 |
| Pou5f1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20362542|imex:IM-16970 |
| HDAC1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21258344|imex:IM-17039 |
| HDAC2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21258344|imex:IM-17039 |
| RBBP4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21258344|imex:IM-17039 |
| CDK2AP2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21258344|imex:IM-17039 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.3 + PDB: 无 | pLDDT=78.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MTA3 — Metastasis-associated protein MTA3，研究基础较多，新颖性有限。
2. 蛋白大小594 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 101 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 101 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BTC8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000057935-MTA3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MTA3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BTC8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/MTA3/IF_images/MTA3_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000057935-MTA3/subcellular

![](https://images.proteinatlas.org/39433/422_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/39433/422_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/39433/423_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/39433/423_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/39433/426_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/39433/426_B8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BTC8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
