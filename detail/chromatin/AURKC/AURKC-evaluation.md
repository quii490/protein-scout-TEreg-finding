---
type: protein-evaluation
gene: "AURKC"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AURKC 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AURKC / AIE2, AIK3, AIRK3, ARK3, STK13 |
| 蛋白名称 | Aurora kinase C |
| 蛋白大小 | 309 aa / 35.6 kDa |
| UniProt ID | Q9UQB9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Chromosome; Chromosome, centromere; Cytoplasm, cyto |
| 蛋白大小 | 10/10 | ×1 | 10 | 309 aa / 35.6 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=90 篇 (≤100→2) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=84.0; PDB: 6GR8, 6GR9, 9ESA |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR030616, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.0/180** | |
| **归一化总分** | | | **57.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Chromosome; Chromosome, centromere; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- chromosome passenger complex (GO:0032133)
- condensed chromosome (GO:0000793)
- kinetochore (GO:0000776)
- midbody (GO:0030496)
- nucleus (GO:0005634)
- spindle (GO:0005819)
- spindle microtubule (GO:0005876)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 90 |
| PubMed broad count | 187 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AIE2, AIK3, AIRK3, ARK3, STK13 |

**关键文献**:
1. Genetic etiological spectrum of sperm morphological abnormalities.. *Journal of assisted reproduction and genetics*. PMID: 39417902
2. The oncogenic role of meiosis-specific Aurora kinase C in mitotic cells.. *Experimental cell research*. PMID: 34461108
3. Computational study of the potential impact of AURKC missense SNPs on AURKC-INCENP interaction and their correlation to macrozoospermia.. *Journal of biomolecular structure & dynamics*. PMID: 36326488
4. Characterization of macrozoospermia-associated AURKC mutations in a mammalian meiotic system.. *Human molecular genetics*. PMID: 27106102
5. Macrozoospermia associated with mutations of AURKC gene: First case report in Latin America and literature review.. *Revista internacional de andrologia*. PMID: 31455599

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.0 |
| 高置信度残基 (pLDDT>90) 占比 | 68.9% |
| 置信残基 (pLDDT 70-90) 占比 | 12.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 13.6% |
| 有序区域 (pLDDT>70) 占比 | 81.2% |
| 可用 PDB 条目 | 6GR8, 6GR9, 9ESA |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6GR8, 6GR9, 9ESA）+ AlphaFold高质量预测（pLDDT=84.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR030616, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| INCENP | 0.999 | 0.991 | — |
| BIRC5 | 0.972 | 0.543 | — |
| CDCA8 | 0.963 | 0.086 | — |
| AURKB | 0.926 | 0.625 | — |
| CENPA | 0.918 | 0.371 | — |
| CCNA2 | 0.880 | 0.000 | — |
| CDK1 | 0.858 | 0.095 | — |
| NDC80 | 0.838 | 0.288 | — |
| H3-5 | 0.834 | 0.149 | — |
| H3-4 | 0.834 | 0.149 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BIRC5 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| OTX2 | psi-mi:"MI:0231"(mammalian protein protein interac | pubmed:32296183|imex:IM-25472 |
| USP19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSP90AA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MYH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MYH8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDK5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FKBP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.0 + PDB: 6GR8, 6GR9, 9ESA | pLDDT=84.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Chromosome, centromere; Cytop / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. AURKC — Aurora kinase C，研究基础较多，新颖性有限。
2. 蛋白大小309 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 90 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UQB9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105146-AURKC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AURKC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UQB9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/AURKC/AURKC-PAE.png]]
