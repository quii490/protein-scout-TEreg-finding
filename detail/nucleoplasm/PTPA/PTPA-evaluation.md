---
type: protein-evaluation
gene: "PTPA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PTPA — REJECTED (研究热度过高 (PubMed strict=145，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PTPA / PPP2R4 |
| 蛋白名称 | Serine/threonine-protein phosphatase 2A activator |
| 蛋白大小 | 358 aa / 40.7 kDa |
| UniProt ID | Q15257 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 358 aa / 40.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=145 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.2; PDB: 2G62, 2HV6, 2HV7, 2IXM, 4LAC, 4NY3 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004327, IPR043170, IPR037218; Pfam: PF03095 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ATPase complex (GO:1904949)
- calcium channel complex (GO:0034704)
- cytoplasm (GO:0005737)
- extracellular exosome (GO:0070062)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein phosphatase type 2A complex (GO:0000159)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 145 |
| PubMed broad count | 276 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PPP2R4 |

**关键文献**:
1. A mycobacterial effector promotes ferroptosis-dependent pathogenicity and dissemination.. *Nature communications*. PMID: 36932056
2. Gut microbial bile and amino acid metabolism associate with peanut oral immunotherapy failure.. *Nature communications*. PMID: 40634275
3. Cross-Ethnic Variant Screening and Burden Analysis of PTPA in Parkinson's Disease.. *Movement disorders : official journal of the Movement Disorder Society*. PMID: 37046398
4. UBE3A-mediated PTPA ubiquitination and degradation regulate PP2A activity and dendritic spine morphology.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 31160454
5. PTPA variants and impaired PP2A activity in early-onset parkinsonism with intellectual disability.. *Brain : a journal of neurology*. PMID: 36073231

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.2 |
| 高置信度残基 (pLDDT>90) 占比 | 77.1% |
| 置信残基 (pLDDT 70-90) 占比 | 5.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 15.1% |
| 有序区域 (pLDDT>70) 占比 | 83.0% |
| 可用 PDB 条目 | 2G62, 2HV6, 2HV7, 2IXM, 4LAC, 4NY3 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2G62, 2HV6, 2HV7, 2IXM, 4LAC, 4NY3）+ AlphaFold极高置信度预测（pLDDT=87.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004327, IPR043170, IPR037218; Pfam: PF03095 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPP2CA | 0.999 | 0.978 | — |
| PPP2R1A | 0.998 | 0.941 | — |
| PPP4C | 0.974 | 0.896 | — |
| PPP4R2 | 0.972 | 0.833 | — |
| PPP4R3A | 0.941 | 0.842 | — |
| PPP2R5C | 0.922 | 0.133 | — |
| PPP2R3A | 0.919 | 0.292 | — |
| PPP2CB | 0.917 | 0.404 | — |
| PPP2R1B | 0.889 | 0.540 | — |
| PPP4R1 | 0.880 | 0.416 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RRD1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-14085|pubmed:21179020 |
| RRD2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-14085|pubmed:21179020 |
| RpS27 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| TPD3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| WWM1 | psi-mi:"MI:0089"(protein array) | pubmed:16606443|imex:IM-19627| |
| EBI-829527 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16267556|imex:IM-16518| |
| - | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16267556|imex:IM-16518| |
| MSP9 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16267556|imex:IM-16518| |
| MPE1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| DAL82 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.2 + PDB: 2G62, 2HV6, 2HV7, 2IXM, 4LAC,  | pLDDT=87.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. PTPA — Serine/threonine-protein phosphatase 2A activator，研究基础较多，新颖性有限。
2. 蛋白大小358 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 145 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 145 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15257
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119383-PTPA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PTPA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15257
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/PTPA/IF_images/PTPA_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000119383-PTPA/subcellular

![](https://images.proteinatlas.org/5695/79_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/5695/79_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/5695/80_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/5695/80_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/5695/81_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/5695/81_A6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15257-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P18433 |
| SMART | SM00194;SM00404; |
| UniProt Domain [FT] | DOMAIN 241..501; /note="Tyrosine-protein phosphatase 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00160"; DOMAIN 533..791; /note="Tyrosine-protein phosphatase 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00160" |
| InterPro | IPR029021;IPR050348;IPR000242;IPR016130;IPR003595;IPR000387;IPR016336;IPR027262; |
| Pfam | PF00102; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000119383-PTPA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PPP4C | Intact, Biogrid | true |
| AKT1 | Biogrid | false |
| ATM | Biogrid | false |
| CCNG1 | Biogrid | false |
| CYLD | Biogrid | false |
| FOXO3 | Biogrid | false |
| GPRASP3 | Biogrid | false |
| GRIN3A | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
