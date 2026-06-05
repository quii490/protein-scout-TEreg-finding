---
type: protein-evaluation
gene: "UVRAG"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## UVRAG — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=252，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UVRAG |
| 蛋白名称 | UV radiation resistance-associated gene protein |
| 蛋白大小 | 699 aa / 78.2 kDa |
| UniProt ID | Q9P2Y5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Late endosome; Lysosome; Cytoplasmic vesicle, autophagosome; |
| 蛋白大小 | 10/10 | ×1 | 10 | 699 aa / 78.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=252 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.6; PDB: 7BL1 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000008, IPR035892, IPR018791; Pfam: PF10186, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **60.5/180** | |
| **归一化总分** | | | **33.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Late endosome; Lysosome; Cytoplasmic vesicle, autophagosome; Early endosome; Endoplasmic reticulum; ... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- autophagosome membrane (GO:0000421)
- centrosome (GO:0005813)
- chromosome, centromeric region (GO:0000775)
- cytoplasm (GO:0005737)
- early endosome (GO:0005769)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum-Golgi intermediate compartment membrane (GO:0033116)
- endosome (GO:0005768)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 252 |
| PubMed broad count | 328 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. How autophagy controls the intestinal epithelial barrier.. *Autophagy*. PMID: 33906557
2. VCP/p97 UFMylation stabilizes BECN1 and facilitates the initiation of autophagy.. *Autophagy*. PMID: 38762759
3. Emerging dimensions of autophagy in melanoma.. *Autophagy*. PMID: 38497492
4. Autophagy and apoptosis dysfunction in neurodegenerative disorders.. *Progress in neurobiology*. PMID: 24211851
5. Identification of novel lipid droplet factors that regulate lipophagy and cholesterol efflux in macrophage foam cells.. *Autophagy*. PMID: 33590792

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.6 |
| 高置信度残基 (pLDDT>90) 占比 | 31.9% |
| 置信残基 (pLDDT 70-90) 占比 | 24.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 35.8% |
| 有序区域 (pLDDT>70) 占比 | 56.2% |
| 可用 PDB 条目 | 7BL1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.6），有序残基占 56.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR018791; Pfam: PF10186, PF00168 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RUBCN | 0.999 | 0.881 | — |
| BECN1 | 0.999 | 0.998 | — |
| PIK3R4 | 0.999 | 0.941 | — |
| PIK3C3 | 0.999 | 0.982 | — |
| ATG14 | 0.999 | 0.088 | — |
| SH3GLB1 | 0.998 | 0.510 | — |
| AMBRA1 | 0.996 | 0.000 | — |
| BECN2 | 0.974 | 0.496 | — |
| BCL2 | 0.974 | 0.000 | — |
| VPS16 | 0.968 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000348455.3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| VPS33A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| PIK3C3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| PTPRA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| BECN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| RUBCN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| PIK3R4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| TGFBRAP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| VPS18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| TOP2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.6 + PDB: 7BL1 | pLDDT=67.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Late endosome; Lysosome; Cytoplasmic vesicle, auto / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. UVRAG — UV radiation resistance-associated gene protein，研究基础较多，新颖性有限。
2. 蛋白大小699 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 252 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2Y5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198382-UVRAG/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UVRAG
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2Y5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P2Y5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
