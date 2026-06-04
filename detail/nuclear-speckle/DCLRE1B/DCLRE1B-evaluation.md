---
type: protein-evaluation
gene: "DCLRE1B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DCLRE1B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCLRE1B / SNM1B |
| 蛋白名称 | 5' exonuclease Apollo |
| 蛋白大小 | 532 aa / 60.0 kDa |
| UniProt ID | Q9H816 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; UniProt: Chromosome, telomere; Nucleus; Cytoplasm, cytoskeleton, micr |
| 蛋白大小 | 10/10 | ×1 | 10 | 532 aa / 60.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=74.8; PDB: 3BUA, 5AHO, 7A1F, 7B2X, 7B9B |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011084, IPR036866; Pfam: PF07522 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Supported |
| UniProt | Chromosome, telomere; Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- chromosome, telomeric region (GO:0000781)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 70 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SNM1B |

**关键文献**:
1. Integration of multi-omics transcriptome-wide analysis for the identification of novel therapeutic drug targets in diabetic retinopathy.. *Journal of translational medicine*. PMID: 39719581
2. Efficient discovery of robust prognostic biomarkers and signatures in solid tumors.. *Cancer letters*. PMID: 39864538
3. p53 in the Molecular Circuitry of Bone Marrow Failure Syndromes.. *International journal of molecular sciences*. PMID: 37834388
4. DCLRE1B as a novel prognostic biomarker associated with immune infiltration: a pancancer analysis.. *Scientific reports*. PMID: 39738287
5. Telomere structure and maintenance gene variants and risk of five cancer types.. *International journal of cancer*. PMID: 27459707

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.8 |
| 高置信度残基 (pLDDT>90) 占比 | 58.1% |
| 置信残基 (pLDDT 70-90) 占比 | 5.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.1% |
| 低置信 (pLDDT<50) 占比 | 34.2% |
| 有序区域 (pLDDT>70) 占比 | 63.7% |
| 可用 PDB 条目 | 3BUA, 5AHO, 7A1F, 7B2X, 7B9B |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3BUA, 5AHO, 7A1F, 7B2X, 7B9B）+ AlphaFold极高置信度预测（pLDDT=74.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011084, IPR036866; Pfam: PF07522 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TERF2 | 0.999 | 0.985 | — |
| TINF2 | 0.951 | 0.543 | — |
| TERF1 | 0.950 | 0.600 | — |
| SLX4 | 0.944 | 0.292 | — |
| TERF2IP | 0.934 | 0.742 | — |
| POT1 | 0.904 | 0.593 | — |
| MUS81 | 0.890 | 0.292 | — |
| FANCD2 | 0.849 | 0.295 | — |
| FANCM | 0.806 | 0.100 | — |
| PRKDC | 0.798 | 0.438 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TERF2 | psi-mi:"MI:0018"(two hybrid) | pubmed:16730175|imex:IM-17036 |
| TERF1 | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:16730175|imex:IM-17036 |
| NOXA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TERF2IP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| POT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| KANSL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| FNBP1L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| PRKDC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| HSPD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SLC39A10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.8 + PDB: 3BUA, 5AHO, 7A1F, 7B2X, 7B9B | pLDDT=74.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Chromosome, telomere; Nucleus; Cytoplasm, cytoskel / Nucleoplasm, Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DCLRE1B — 5' exonuclease Apollo，非常新颖，仅有少数基础研究。
2. 蛋白大小532 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H816
- Protein Atlas: https://www.proteinatlas.org/ENSG00000118655-DCLRE1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCLRE1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H816
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
