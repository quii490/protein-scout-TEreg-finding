---
type: protein-evaluation
gene: "WDR19"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR19 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDR19 / IFT144, KIAA1638 |
| 蛋白名称 | WD repeat-containing protein 19 |
| 蛋白大小 | 1342 aa / 151.6 kDa |
| UniProt ID | Q8NEZ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Mid piece; 额外: Centrosome, Basal body, Cytosol,; UniProt: Cell projection, cilium; Cytoplasm, cytoskeleton, cilium bas |
| 蛋白大小 | 5/10 | ×1 | 5 | 1342 aa / 151.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=86.3; PDB: 8BBF, 8BBG, 8FGW, 8FH3 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR057855, IPR011990, IPR056168, IPR015943, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.0/180** | |
| **归一化总分** | | | **58.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mid piece; 额外: Centrosome, Basal body, Cytosol, Principal piece | Uncertain |
| UniProt | Cell projection, cilium; Cytoplasm, cytoskeleton, cilium basal body; Cell projection, cilium, photor... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- ciliary tip (GO:0097542)
- cilium (GO:0005929)
- intraciliary transport particle A (GO:0030991)
- motile cilium (GO:0031514)
- non-motile cilium (GO:0097730)
- photoreceptor connecting cilium (GO:0032391)
- photoreceptor outer segment (GO:0001750)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IFT144, KIAA1638 |

**关键文献**:
1. Nephronophthisis-Related Ciliopathies.. **. PMID: 27336129
2. Cranioectodermal Dysplasia.. **. PMID: 24027799
3. Stargardt-like Clinical Characteristics and Disease Course Associated with Variants in the WDR19 Gene.. *Genes*. PMID: 36833218
4. Elucidating Mechanisms of Hypomorphic WDR19-Related Kidney Failure.. *Kidney international reports*. PMID: 41141533
5. Phenotypic spectrum and theoretical prime editing analysis of WDR19-mediated retinal degeneration.. *Documenta ophthalmologica. Advances in ophthalmology*. PMID: 40183892

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.3 |
| 高置信度残基 (pLDDT>90) 占比 | 38.7% |
| 置信残基 (pLDDT 70-90) 占比 | 56.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 95.4% |
| 可用 PDB 条目 | 8BBF, 8BBG, 8FGW, 8FH3 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（8BBF, 8BBG, 8FGW, 8FH3）+ AlphaFold高质量预测（pLDDT=86.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR057855, IPR011990, IPR056168, IPR015943, IPR001680; Pfam: PF23389, PF15911, PF24762 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WDR35 | 0.999 | 0.986 | — |
| IFT43 | 0.999 | 0.959 | — |
| TTC21B | 0.999 | 0.941 | — |
| IFT140 | 0.999 | 0.997 | — |
| IFT122 | 0.999 | 0.997 | — |
| IFT27 | 0.961 | 0.000 | — |
| IFT80 | 0.955 | 0.310 | — |
| TULP3 | 0.952 | 0.784 | — |
| IFT172 | 0.935 | 0.000 | — |
| IFT52 | 0.933 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PAPLA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| Ten-m | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| Spn | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Caper | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| Tsp | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| IFT122 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PFKP | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| WDR35 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| NEK7 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| ACSL3 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.3 + PDB: 8BBF, 8BBG, 8FGW, 8FH3 | pLDDT=86.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell projection, cilium; Cytoplasm, cytoskeleton,  / Nucleoplasm, Mid piece; 额外: Centrosome, Basal body | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. WDR19 — WD repeat-containing protein 19，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1342 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEZ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157796-WDR19/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDR19
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEZ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
