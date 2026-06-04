---
type: protein-evaluation
gene: "HASPIN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HASPIN — REJECTED (研究热度过高 (PubMed strict=107，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HASPIN / GSG2 |
| 蛋白名称 | Serine/threonine-protein kinase haspin |
| 蛋白大小 | 798 aa / 88.5 kDa |
| UniProt ID | Q8TF76 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome; Cytoplasm, cytoskeleton, spindle |
| 蛋白大小 | 10/10 | ×1 | 10 | 798 aa / 88.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=107 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.9; PDB: 2VUW, 2WB8, 3DLZ, 3E7V, 3F2N, 3FMD, 3IQ7 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024604, IPR011009, IPR000719, IPR017441; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Chromosome; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spindle (GO:0005819)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 107 |
| PubMed broad count | 218 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GSG2 |

**关键文献**:
1. Structure, Roles and Inhibitors of a Mitotic Protein Kinase Haspin.. *Current medicinal chemistry*. PMID: 28413956
2. Roles and regulation of Haspin kinase and its impact on carcinogenesis.. *Cellular signalling*. PMID: 35278668
3. Function and inhibition of Haspin kinase: targeting multiple cancer therapies by antimitosis.. *The Journal of pharmacy and pharmacology*. PMID: 36334086
4. Cloning and characterization of human haspin gene encoding haploid germ cell-specific nuclear protein kinase.. *Molecular human reproduction*. PMID: 11228240
5. Haspin: a newly discovered regulator of mitotic chromosome behavior.. *Chromosoma*. PMID: 19997740

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.9 |
| 高置信度残基 (pLDDT>90) 占比 | 39.5% |
| 置信残基 (pLDDT 70-90) 占比 | 4.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 52.9% |
| 有序区域 (pLDDT>70) 占比 | 44.1% |
| 可用 PDB 条目 | 2VUW, 2WB8, 3DLZ, 3E7V, 3F2N, 3FMD, 3IQ7, 4OUC, 4QTC, 5HTB |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.9），有序残基占 44.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024604, IPR011009, IPR000719, IPR017441; Pfam: PF12330 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AURKB | 0.956 | 0.292 | — |
| BUB1 | 0.938 | 0.073 | — |
| PDS5A | 0.937 | 0.330 | — |
| KIF2C | 0.886 | 0.000 | — |
| SGO1 | 0.877 | 0.046 | — |
| PLK1 | 0.873 | 0.292 | — |
| H3-4 | 0.818 | 0.096 | — |
| H3C12 | 0.810 | 0.096 | — |
| H3C13 | 0.808 | 0.096 | — |
| H3-5 | 0.803 | 0.096 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17314511 |
| HSP90AB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17906|pubmed:22939624| |
| NCBP3 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| HSF2BP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MDFI | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TNFRSF19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IL17RA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIRT6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EEF1D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.9 + PDB: 2VUW, 2WB8, 3DLZ, 3E7V, 3F2N,  | pLDDT=62.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Cytoplasm, cytoskeleton, spin / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HASPIN — Serine/threonine-protein kinase haspin，研究基础较多，新颖性有限。
2. 蛋白大小798 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 107 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 107 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TF76
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177602-HASPIN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HASPIN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TF76
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/HASPIN/HASPIN-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HASPIN/HASPIN-PAE.png]]
