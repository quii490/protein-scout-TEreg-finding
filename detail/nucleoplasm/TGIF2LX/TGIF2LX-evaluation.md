---
type: protein-evaluation
gene: "TGIF2LX"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TGIF2LX 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TGIF2LX / TGIFLX |
| 蛋白名称 | Homeobox protein TGIF2LX |
| 蛋白大小 | 241 aa / 26.7 kDa |
| UniProt ID | Q8IUE1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 241 aa / 26.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.5; PDB: 2DMN |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR009057, IPR008422, IPR050224; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TGIFLX |

**关键文献**:
1. Homeodomain Protein Transforming Growth Factor Beta-Induced Factor 2 Like, X-Linked Function in Colon Adenocarcinoma Cells.. *Asian Pacific journal of cancer prevention : APJCP*. PMID: 28843229
2. Regulation of long non-coding RNAs XIST and ROR induced by homeodomain protein TGIF2LX in colorectal cancer.. *Journal of cancer research and therapeutics*. PMID: 36510989
3. A comprehensive survey for human transcription factors on expression, regulation, interaction, phenotype and cancer survival.. *Briefings in bioinformatics*. PMID: 33517372
4. Profiling cancer testis antigens in non-small-cell lung cancer.. *JCI insight*. PMID: 27699219
5. In vivo identification of novel TGIF2LX target genes in colorectal adenocarcinoma using the cDNA-AFLP method.. *Arab journal of gastroenterology : the official publication of the Pan-Arab Association of Gastroenterology*. PMID: 29960902

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.5 |
| 高置信度残基 (pLDDT>90) 占比 | 27.8% |
| 置信残基 (pLDDT 70-90) 占比 | 8.3% |
| 中等置信 (pLDDT 50-70) 占比 | 43.2% |
| 低置信 (pLDDT<50) 占比 | 20.7% |
| 有序区域 (pLDDT>70) 占比 | 36.1% |
| 可用 PDB 条目 | 2DMN |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.5），有序残基占 36.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR009057, IPR008422, IPR050224; Pfam: PF05920 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PABPC5 | 0.944 | 0.000 | — |
| TGIF2LY | 0.871 | 0.866 | — |
| PCDH11X | 0.853 | 0.000 | — |
| TGFBI | 0.849 | 0.000 | — |
| ARID4A | 0.661 | 0.586 | — |
| ING2 | 0.641 | 0.622 | — |
| ING1 | 0.625 | 0.605 | — |
| RHOXF2 | 0.611 | 0.071 | — |
| BAHCC1 | 0.599 | 0.589 | — |
| ARID4B | 0.594 | 0.477 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| TGIF2LY | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCGF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DKK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LRRK2 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| EBI-26476040 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| IFNA14 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| PPBP | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| XCL1 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| PUSL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.5 + PDB: 2DMN | pLDDT=67.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TGIF2LX — Homeobox protein TGIF2LX，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小241 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IUE1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153779-TGIF2LX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TGIF2LX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IUE1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
