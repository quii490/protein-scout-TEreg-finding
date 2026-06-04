---
type: protein-evaluation
gene: "CHEK2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CHEK2 — REJECTED (研究热度过高 (PubMed strict=1182，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHEK2 / CDS1, CHK2, RAD53 |
| 蛋白名称 | Serine/threonine-protein kinase Chk2 |
| 蛋白大小 | 543 aa / 60.9 kDa |
| UniProt ID | O96017 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus; UniProt: Nucleus; Nucleus; Nucleus; Nucleus; Nucleus; Nucleus, PML bo |
| 蛋白大小 | 10/10 | ×1 | 10 | 543 aa / 60.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1182 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.2; PDB: 1GXC, 2CN5, 2CN8, 2W0J, 2W7X, 2WTC, 2WTD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000253, IPR011009, IPR000719, IPR008271, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus | Supported |
| UniProt | Nucleus; Nucleus; Nucleus; Nucleus; Nucleus; Nucleus, PML body; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1182 |
| PubMed broad count | 3049 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CDS1, CHK2, RAD53 |

**关键文献**:
1. Breast Cancer Risk Genes - Association Analysis in More than 113,000 Women.. *The New England journal of medicine*. PMID: 33471991
2. Rare, protein-truncating variants in ATM, CHEK2 and PALB2, but not XRCC2, are associated with increased breast cancer risks.. *Journal of medical genetics*. PMID: 28779002
3. Cancer Susceptibility Gene Mutations in Individuals With Colorectal Cancer.. *Journal of clinical oncology : official journal of the American Society of Clinical Oncology*. PMID: 28135145
4. CHEK2 variants: linking functional impact to cancer risk.. *Trends in cancer*. PMID: 35643632
5. Contralateral Breast Cancer Risk Among Carriers of Germline Pathogenic Variants in ATM, BRCA1, BRCA2, CHEK2, and PALB2.. *Journal of clinical oncology : official journal of the American Society of Clinical Oncology*. PMID: 36623243

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.2 |
| 高置信度残基 (pLDDT>90) 占比 | 47.0% |
| 置信残基 (pLDDT 70-90) 占比 | 20.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.5% |
| 低置信 (pLDDT<50) 占比 | 23.9% |
| 有序区域 (pLDDT>70) 占比 | 67.6% |
| 可用 PDB 条目 | 1GXC, 2CN5, 2CN8, 2W0J, 2W7X, 2WTC, 2WTD, 2WTI, 2WTJ, 2XBJ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1GXC, 2CN5, 2CN8, 2W0J, 2W7X, 2WTC, 2WTD, 2WTI, 2WTJ, 2XBJ）+ AlphaFold极高置信度预测（pLDDT=76.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000253, IPR011009, IPR000719, IPR008271, IPR008984; Pfam: PF00498, PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRCA1 | 0.999 | 0.842 | — |
| ATM | 0.999 | 0.836 | — |
| TP53 | 0.999 | 0.833 | — |
| CDC25A | 0.998 | 0.849 | — |
| CDC25C | 0.998 | 0.907 | — |
| ATR | 0.998 | 0.970 | — |
| TP53BP1 | 0.996 | 0.883 | — |
| MDC1 | 0.990 | 0.469 | — |
| CDC7 | 0.988 | 0.940 | — |
| BRCA2 | 0.985 | 0.532 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RAD53 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-14085|pubmed:21179020 |
| ENSMUSP00000066679.2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ACT1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| ASF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| MCM5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| AATF | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-11842|pubmed:17157788 |
| Tp53 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-11842|pubmed:17157788 |
| NR4A1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| POLR2L | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ARHGAP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.2 + PDB: 1GXC, 2CN5, 2CN8, 2W0J, 2W7X,  | pLDDT=76.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus; Nucleus; Nucleus; Nucleus; Nucle / Nucleoplasm; 额外: Golgi apparatus | 一致 |
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
1. CHEK2 — Serine/threonine-protein kinase Chk2，研究基础较多，新颖性有限。
2. 蛋白大小543 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1182 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1182 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O96017
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183765-CHEK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHEK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O96017
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
