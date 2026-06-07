---
type: protein-evaluation
gene: "DDB2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DDB2 — REJECTED (研究热度过高 (PubMed strict=405，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDB2 |
| 蛋白名称 | DNA damage-binding protein 2 |
| 蛋白大小 | 427 aa / 47.9 kDa |
| UniProt ID | Q92466 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Cell Junctions; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 427 aa / 47.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=405 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.6; PDB: 3EI4, 3I7L, 4E54, 4E5Z, 6R8Y, 6R8Z, 6R90 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR033312, IPR015943, IPR019775, IPR036322, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cell Junctions | Supported |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell junction (GO:0030054)
- chromatin (GO:0000785)
- Cul4-RING E3 ubiquitin ligase complex (GO:0080008)
- Cul4A-RING E3 ubiquitin ligase complex (GO:0031464)
- Cul4B-RING E3 ubiquitin ligase complex (GO:0031465)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 405 |
| PubMed broad count | 542 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Gentiopicroside targets PAQR3 to activate the PI3K/AKT signaling pathway and ameliorate disordered glucose and lipid metabolism.. *Acta pharmaceutica Sinica. B*. PMID: 35755276
2. DDB complexities.. *DNA repair*. PMID: 12967661
3. Xeroderma Pigmentosum.. **. PMID: 20301571
4. KRAS mutants confer platinum resistance by regulating ALKBH5 posttranslational modifications in lung cancer.. *The Journal of clinical investigation*. PMID: 39960727
5. Alzheimer's Disease and Aging Association: Identification and Validation of Related Genes.. *The journal of prevention of Alzheimer's disease*. PMID: 38230733

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.6 |
| 高置信度残基 (pLDDT>90) 占比 | 69.8% |
| 置信残基 (pLDDT 70-90) 占比 | 13.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 15.9% |
| 有序区域 (pLDDT>70) 占比 | 82.9% |
| 可用 PDB 条目 | 3EI4, 3I7L, 4E54, 4E5Z, 6R8Y, 6R8Z, 6R90, 6R91, 6R92 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3EI4, 3I7L, 4E54, 4E5Z, 6R8Y, 6R8Z, 6R90, 6R91, 6R92）+ AlphaFold极高置信度预测（pLDDT=83.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033312, IPR015943, IPR019775, IPR036322, IPR001680; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL4A | 0.999 | 0.974 | — |
| DDB1 | 0.999 | 0.999 | — |
| RBX1 | 0.999 | 0.856 | — |
| CUL4B | 0.998 | 0.880 | — |
| XPA | 0.989 | 0.292 | — |
| USP24 | 0.986 | 0.292 | — |
| XPC | 0.982 | 0.824 | — |
| DET1 | 0.982 | 0.000 | — |
| DTL | 0.980 | 0.292 | — |
| TP53 | 0.979 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL4B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| DDB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| CUL4A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18850735|imex:IM-20477 |
| DDB1A | psi-mi:"MI:0018"(two hybrid) | pubmed:16792691|imex:IM-20162 |
| CUL4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:18551167|imex:IM-20345 |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SUMO3 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:17000644|imex:IM-19940 |
| E2F1 | psi-mi:"MI:0096"(pull down) | pubmed:9418871 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.6 + PDB: 3EI4, 3I7L, 4E54, 4E5Z, 6R8Y,  | pLDDT=83.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm, Cell Junctions | 一致 |
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
1. DDB2 — DNA damage-binding protein 2，研究基础较多，新颖性有限。
2. 蛋白大小427 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 405 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 405 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92466
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134574-DDB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92466
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/DDB2/IF_images/DDB2_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000134574-DDB2/subcellular

![](https://images.proteinatlas.org/58406/1043_A7_3_red_green.jpg)
![](https://images.proteinatlas.org/58406/1043_A7_6_red_green.jpg)
![](https://images.proteinatlas.org/58406/983_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/58406/983_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/58406/991_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/58406/991_E10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92466-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92466 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR033312;IPR015943;IPR019775;IPR036322;IPR001680; |
| Pfam | PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000134574-DDB2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCT2 | Biogrid, Bioplex | true |
| CCT3 | Biogrid, Bioplex | true |
| CCT5 | Biogrid, Bioplex | true |
| CCT7 | Biogrid, Bioplex | true |
| COPS3 | Biogrid, Bioplex | true |
| COPS4 | Biogrid, Bioplex | true |
| COPS5 | Biogrid, Bioplex | true |
| COPS6 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
