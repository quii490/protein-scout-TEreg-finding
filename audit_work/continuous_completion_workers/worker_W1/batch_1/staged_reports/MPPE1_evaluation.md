---
type: protein-evaluation
gene: "MPPE1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MPPE1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MPPE1 / PGAP5 |
| 蛋白名称 | Metallophosphoesterase 1 |
| 蛋白大小 | 396 aa / 45.1 kDa |
| UniProt ID | Q53F39 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Golgi apparatus; UniProt: Endoplasmic reticulum-Golgi intermediate compartment membran |
| 蛋白大小 | 10/10 | ×1 | 10 | 396 aa / 45.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004843, IPR029052, IPR039541, IPR033308; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Approved |
| UniProt | Endoplasmic reticulum-Golgi intermediate compartment membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum exit site (GO:0070971)
- endoplasmic reticulum-Golgi intermediate compartment membrane (GO:0033116)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PGAP5 |

**关键文献**:
1. MED27, SLC6A7, and MPPE1 Variants in a Complex Neurodevelopmental Disorder with Severe Dystonia.. *Movement disorders : official journal of the Movement Disorder Society*. PMID: 35876425
2. Association between polymorphisms in the metallophosphoesterase (MPPE1) gene and bipolar disorder.. *American journal of medical genetics. Part B, Neuropsychiatric genetics : the official publication of the International Society of Psychiatric Genetics*. PMID: 19859903
3. Metallophosphoesterase 1, a novel candidate gene in hepatocellular carcinoma malignancy and recurrence.. *Cancer biology & therapy*. PMID: 33054568
4. Identification of candidate genes associated with bacterial and viral infections in wild boars hunted in Tuscany (Italy).. *Scientific reports*. PMID: 35581286
5. cDNA cloning, genomic organization and expression of the novel human metallophosphoesterase gene MPPE1 on chromosome 18p11.2.. *Cytogenetics and cell genetics*. PMID: 11978971

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.7 |
| 高置信度残基 (pLDDT>90) 占比 | 79.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 8.1% |
| 有序区域 (pLDDT>70) 占比 | 87.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.7，有序区 87.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004843, IPR029052, IPR039541, IPR033308; Pfam: PF00149 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC27 | 0.962 | 0.000 | — |
| BATF3 | 0.866 | 0.053 | — |
| XCR1 | 0.864 | 0.000 | — |
| CLEC9A | 0.852 | 0.000 | — |
| GNAL | 0.834 | 0.000 | — |
| CD8A | 0.783 | 0.000 | — |
| PSMB5 | 0.727 | 0.000 | — |
| ITGAE | 0.725 | 0.000 | — |
| THBD | 0.718 | 0.045 | — |
| XCL1 | 0.713 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ADAM10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLXNB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EXTL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLXNA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GPC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SUN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ECEL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HLA-DRB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CANX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.7 + PDB: 无 | pLDDT=89.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum-Golgi intermediate compartme / Nucleoplasm, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MPPE1 — Metallophosphoesterase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小396 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q53F39
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154889-MPPE1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MPPE1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q53F39
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
