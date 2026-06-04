---
type: protein-evaluation
gene: "ITPKC"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ITPKC 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ITPKC / IP3KC |
| 蛋白名称 | Inositol-trisphosphate 3-kinase C |
| 蛋白大小 | 683 aa / 75.2 kDa |
| UniProt ID | Q96DU7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 683 aa / 75.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.9; PDB: 2A98 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR005522, IPR038286; Pfam: PF03770 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.5/180** | |
| **归一化总分** | | | **66.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 63 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IP3KC |

**关键文献**:
1. Association of ITPKC gene polymorphisms rs28493229 and rs2290692 in North Indian children with Kawasaki disease.. *Pediatric research*. PMID: 34952936
2. Inositol-Triphosphate 3-Kinase C and DNA Methylation Involvement in NLRP3 Inflammasome Activation in Kawasaki Disease.. *Indian journal of pediatrics*. PMID: 35353363
3. ITPKC and SLC11A1 Gene Polymorphisms and Gene-Gene Interactions in Korean Patients with Kawasaki Disease.. *Yonsei medical journal*. PMID: 29214786
4. The genetics of Kawasaki disease.. *International journal of rheumatic diseases*. PMID: 29152908
5. Genetic polymorphisms in the ITPKC gene and cervical squamous cell carcinoma risk.. *Cancer immunology, immunotherapy : CII*. PMID: 22610085

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.9 |
| 高置信度残基 (pLDDT>90) 占比 | 32.4% |
| 置信残基 (pLDDT 70-90) 占比 | 6.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 59.3% |
| 有序区域 (pLDDT>70) 占比 | 38.7% |
| 可用 PDB 条目 | 2A98 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.9），有序残基占 38.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005522, IPR038286; Pfam: PF03770 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IPMK | 0.949 | 0.000 | — |
| INPP5A | 0.939 | 0.000 | — |
| MINPP1 | 0.929 | 0.000 | — |
| INPP5K | 0.925 | 0.000 | — |
| ITPK1 | 0.923 | 0.000 | — |
| INPP5J | 0.919 | 0.000 | — |
| ITPKB | 0.916 | 0.000 | — |
| ITPKA | 0.910 | 0.000 | — |
| CALM1 | 0.903 | 0.062 | — |
| PLCG1 | 0.745 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP3CC | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| Il16 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| ERP44 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AURKA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SSUH2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NPAS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| STX17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| OR2A4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RAMP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCDC71 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.9 + PDB: 2A98 | pLDDT=58.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ITPKC — Inositol-trisphosphate 3-kinase C，非常新颖，仅有少数基础研究。
2. 蛋白大小683 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=58.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96DU7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000086544-ITPKC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ITPKC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96DU7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
