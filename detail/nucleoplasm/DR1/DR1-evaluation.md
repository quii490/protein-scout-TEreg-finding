---
type: protein-evaluation
gene: "DR1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DR1 — REJECTED (研究热度过高 (PubMed strict=2365，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DR1 |
| 蛋白名称 | DR1 |
| 蛋白大小 | 722 aa / 78.7 kDa |
| UniProt ID | A0A126LB39 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | ×4 | 20 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 722 aa / 78.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2365 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=29.4; PDB: 无 |
| 调控结构域 | 4/10 | ×2 | 8 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **59.5/180** | |
| **归一化总分** | | | **33.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2365 |
| PubMed broad count | 2560 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Immunogenicity of neoantigens from hepatocellular carcinoma patients treated with a combined radioimmunotherapy.. *Oncoimmunology*. PMID: 41851965
2. Leveraging machine learning to predict de novo skin malignancy following lung transplantation.. *Lung Cancer Manag*. PMID: 41553243
3. Transcriptome analysis of cacao reveals differentially expressed genes associated with resistance to Phytophthora palmivora.. *3 Biotech*. PMID: 42205904
4. Differential intrahepatic integrated HBV DNA patterns between HBeAg-positive and HBeAg-negative chronic hepatitis B.. *Gut*. PMID: 42031533
5. Synthesis and pyroelectric response of disperse red 1 functionalized silicones: cyclic monomer, homopolymer, and block copolymer derivatives.. *Mater Horiz*. PMID: 42132516

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 29.4 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 100.0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 预测质量有限（pLDDT=29.4），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释稀疏，属新颖蛋白正常现象。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DRAP1 | 0.000 | 0.000 | — |
| TBP | 0.000 | 0.000 | — |
| MBIP | 0.000 | 0.000 | — |
| YEATS2 | 0.000 | 0.000 | — |
| WDR5 | 0.000 | 0.000 | — |
| TADA2A | 0.000 | 0.000 | — |
| TADA3 | 0.000 | 0.000 | — |
| POLE3 | 0.000 | 0.000 | — |
| SGF29 | 0.000 | 0.000 | — |
| KAT14 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9NRF9 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9VJQ5 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P49906 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q8SX89 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9VDK2 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9VXC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q01658 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9W256 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q14919 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:- |
| uniprotkb:P20226 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=29.4 + PDB: 无 | pLDDT=29.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DR1 — DR1，研究基础较多，新颖性有限。
2. 蛋白大小722 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2365 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=29.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2365 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A126LB39
- Protein Atlas: https://www.proteinatlas.org/ENSG00000117505-DR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A126LB39
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
