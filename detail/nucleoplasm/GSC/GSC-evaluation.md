---
type: protein-evaluation
gene: "GSC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GSC — REJECTED (研究热度过高 (PubMed strict=1207，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GSC |
| 蛋白名称 | Homeobox protein goosecoid |
| 蛋白大小 | 257 aa / 28.1 kDa |
| UniProt ID | P56915 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 257 aa / 28.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1207 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.8; PDB: 2DMU |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051440, IPR001356, IPR017970, IPR009057; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1207 |
| PubMed broad count | 4083 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. PTBP1 Lactylation Promotes Glioma Stem Cell Maintenance through PFKFB4-Driven Glycolysis.. *Cancer research*. PMID: 39570804
2. IGFBP5 is an ROR1 ligand promoting glioblastoma invasion via ROR1/HER2-CREB signaling axis.. *Nature communications*. PMID: 36949068
3. Suppression of mitochondrial ROS by prohibitin drives glioblastoma progression and therapeutic resistance.. *Nature communications*. PMID: 34140524
4. Histone Lactylation-Driven Upregulation of VRK1 Expression Promotes Stemness and Proliferation of Glioma Stem Cells.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40990975
5. TRIM8 regulates stemness in glioblastoma through PIAS3-STAT3.. *Molecular oncology*. PMID: 28100038

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.8 |
| 高置信度残基 (pLDDT>90) 占比 | 20.2% |
| 置信残基 (pLDDT 70-90) 占比 | 10.9% |
| 中等置信 (pLDDT 50-70) 占比 | 38.1% |
| 低置信 (pLDDT<50) 占比 | 30.7% |
| 有序区域 (pLDDT>70) 占比 | 31.1% |
| 可用 PDB 条目 | 2DMU |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=63.8），有序残基占 31.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051440, IPR001356, IPR017970, IPR009057; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FOPNL | 0.954 | 0.954 | — |
| RRP15 | 0.954 | 0.954 | — |
| SUPT6H | 0.954 | 0.954 | — |
| ZNF330 | 0.954 | 0.954 | — |
| PSME3IP1 | 0.954 | 0.954 | — |
| WDR26 | 0.954 | 0.954 | — |
| HINFP | 0.954 | 0.954 | — |
| TEKT2 | 0.954 | 0.954 | — |
| TBX20 | 0.863 | 0.859 | — |
| RAB11FIP3 | 0.841 | 0.840 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-15107479 | psi-mi:"MI:0397"(two hybrid array) | pubmed:unassigned1513|imex:IM- |
| RpS26 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| mdcds_12730 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| tth | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| bsh | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG3528 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| mol | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG3651 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG4617 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| gro | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.8 + PDB: 2DMU | pLDDT=63.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GSC — Homeobox protein goosecoid，研究基础较多，新颖性有限。
2. 蛋白大小257 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1207 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1207 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P56915
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133937-GSC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GSC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P56915
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
