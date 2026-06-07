---
type: protein-evaluation
gene: "DVL2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DVL2 — REJECTED (研究热度过高 (PubMed strict=340，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DVL2 |
| 蛋白名称 | Segment polarity protein dishevelled homolog DVL-2 |
| 蛋白大小 | 736 aa / 78.9 kDa |
| UniProt ID | O14641 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; 额外: Aggresome; UniProt: Cell membrane; Cytoplasm, cytosol; Cytoplasmic vesicle; Nucl |
| 蛋白大小 | 10/10 | ×1 | 10 | 736 aa / 78.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=340 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.7; PDB: 2REY, 3CBX, 3CBY, 3CBZ, 3CC0, 4WIP, 5LNP |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000591, IPR024580, IPR008339, IPR003351, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Aggresome | Approved |
| UniProt | Cell membrane; Cytoplasm, cytosol; Cytoplasmic vesicle; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- aggresome (GO:0016235)
- apical part of cell (GO:0045177)
- clathrin-coated endocytic vesicle (GO:0045334)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- lateral plasma membrane (GO:0016328)
- nuclear body (GO:0016604)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 340 |
| PubMed broad count | 534 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Targeted knockdown of PGAM5 in synovial macrophages efficiently alleviates osteoarthritis.. *Bone research*. PMID: 38433252
2. Targeting E3 Ubiquitin Ligase WWP1 Prevents Cardiac Hypertrophy Through Destabilizing DVL2 via Inhibition of K27-Linked Ubiquitination.. *Circulation*. PMID: 34139860
3. Macrophage Dvl2 deficiency promotes NOD1-Driven pyroptosis and exacerbates inflammatory liver injury.. *Redox biology*. PMID: 39644526
4. PCID2 is essential for spermatogonial differentiation by regulating alternative splicing.. *Cellular and molecular life sciences : CMLS*. PMID: 41526677
5. Association of DVL2 and AXIN2 gene polymorphisms with cleft lip with or without cleft palate in a Polish population.. *Birth defects research. Part A, Clinical and molecular teratology*. PMID: 22887353

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.7 |
| 高置信度残基 (pLDDT>90) 占比 | 16.6% |
| 置信残基 (pLDDT 70-90) 占比 | 18.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 56.9% |
| 有序区域 (pLDDT>70) 占比 | 35.5% |
| 可用 PDB 条目 | 2REY, 3CBX, 3CBY, 3CBZ, 3CC0, 4WIP, 5LNP, 5SUY, 5SUZ, 6IW3 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.7），有序残基占 35.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000591, IPR024580, IPR008339, IPR003351, IPR001158; Pfam: PF00610, PF02377, PF00778 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AXIN1 | 0.999 | 0.982 | — |
| VANGL1 | 0.994 | 0.522 | — |
| VANGL2 | 0.994 | 0.471 | — |
| LRP6 | 0.993 | 0.108 | — |
| DACT1 | 0.992 | 0.647 | — |
| DVL1 | 0.991 | 0.811 | — |
| DVL3 | 0.990 | 0.775 | — |
| FZD4 | 0.985 | 0.169 | — |
| ARRB2 | 0.981 | 0.071 | — |
| PRICKLE1 | 0.979 | 0.437 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000005340.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Plcg2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| ZNF263 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RBPMS | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ENKD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| OTULIN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| AP1M1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SORBS3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RHOXF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZNF250 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.7 + PDB: 2REY, 3CBX, 3CBY, 3CBZ, 3CC0,  | pLDDT=58.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cytoplasm, cytosol; Cytoplasmic ves / Nucleoplasm, Nuclear bodies; 额外: Aggresome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DVL2 — Segment polarity protein dishevelled homolog DVL-2，研究基础较多，新颖性有限。
2. 蛋白大小736 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 340 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 340 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14641
- Protein Atlas: https://www.proteinatlas.org/ENSG00000004975-DVL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DVL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14641
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000004975-DVL2/subcellular

![](https://images.proteinatlas.org/21611/1132_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/21611/1132_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/21611/1139_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/21611/1139_H3_3_red_green.jpg)
![](https://images.proteinatlas.org/21611/1220_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/21611/1220_G5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O14641-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O14641 |
| SMART | SM00021;SM00049;SM00228; |
| UniProt Domain [FT] | DOMAIN 11..93; /note="DIX"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00069"; DOMAIN 267..339; /note="PDZ"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143"; DOMAIN 433..507; /note="DEP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00066" |
| InterPro | IPR000591;IPR024580;IPR008339;IPR003351;IPR001158;IPR038207;IPR015506;IPR008341;IPR001478;IPR036034;IPR029071;IPR036388;IPR036390; |
| Pfam | PF00610;PF02377;PF00778;PF12316;PF00595; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000004975-DVL2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AP2M1 | Intact, Biogrid | true |
| ARR3 | Intact, Biogrid | true |
| AXIN1 | Intact, Biogrid | true |
| BAG3 | Intact, Biogrid | true |
| CSNK1E | Intact, Biogrid | true |
| DACT1 | Intact, Biogrid | true |
| DVL1 | Intact, Biogrid | true |
| DVL3 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
