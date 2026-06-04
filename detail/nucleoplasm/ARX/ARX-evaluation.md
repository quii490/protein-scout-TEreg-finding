---
type: protein-evaluation
gene: "ARX"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ARX — REJECTED (研究热度过高 (PubMed strict=398，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARX |
| 蛋白名称 | Homeobox protein ARX |
| 蛋白大小 | 562 aa / 58.2 kDa |
| UniProt ID | Q96QS3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 562 aa / 58.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=398 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR003654, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 398 |
| PubMed broad count | 1121 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic Advancements in Infantile Epileptic Spasms Syndrome and Opportunities for Precision Medicine.. *Genes*. PMID: 38540325
2. Genetic determinants of global developmental delay and intellectual disability in Ukrainian children.. *Journal of neurodevelopmental disorders*. PMID: 38539105
3. Further characterisation of ARX-related disorders in females due to inherited or de novo variants.. *Journal of medical genetics*. PMID: 37879892
4. Expanding the genotypes and phenotypes for 19 rare diseases by exome sequencing performed in pediatric intensive care unit.. *Human mutation*. PMID: 34298581
5. The Rhox genes.. *Reproduction (Cambridge, England)*. PMID: 20430877

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.0 |
| 高置信度残基 (pLDDT>90) 占比 | 9.3% |
| 置信残基 (pLDDT 70-90) 占比 | 7.5% |
| 中等置信 (pLDDT 50-70) 占比 | 26.5% |
| 低置信 (pLDDT<50) 占比 | 56.8% |
| 有序区域 (pLDDT>70) 占比 | 16.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=55.0），有序残基占 16.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR003654, IPR050649; Pfam: PF00046, PF03826 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCDH19 | 0.824 | 0.000 | — |
| CDKL5 | 0.813 | 0.000 | — |
| STXBP1 | 0.800 | 0.049 | — |
| SLC25A22 | 0.781 | 0.000 | — |
| SCN1A | 0.764 | 0.078 | — |
| PNKP | 0.751 | 0.000 | — |
| IPO13 | 0.746 | 0.100 | — |
| SPTAN1 | 0.734 | 0.084 | — |
| ARHGEF9 | 0.695 | 0.000 | — |
| POLA1 | 0.687 | 0.052 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.0 + PDB: 无 | pLDDT=55.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ARX — Homeobox protein ARX，研究基础较多，新颖性有限。
2. 蛋白大小562 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 398 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 398 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96QS3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000004848-ARX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96QS3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
