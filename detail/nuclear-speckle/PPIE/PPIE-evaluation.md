---
type: protein-evaluation
gene: "PPIE"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PPIE 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PPIE / CYP33 |
| 蛋白名称 | Peptidyl-prolyl cis-trans isomerase E |
| 蛋白大小 | 301 aa / 33.4 kDa |
| UniProt ID | Q9UNP9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 301 aa / 33.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.2; PDB: 1ZMF, 2CQB, 2KU7, 2KYX, 2R99, 3LPY, 3MDF |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029000, IPR020892, IPR002130, IPR012677, IPR016 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- catalytic step 2 spliceosome (GO:0071013)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 389 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CYP33 |

**关键文献**:
1. Identification of RNA binding proteins that mediate a quality control mechanism of splicing.. *bioRxiv : the preprint server for biology*. PMID: 40777298
2. Structural and Functional Insights into Human Nuclear Cyclophilins.. *Biomolecules*. PMID: 30518120
3. Comprehensive Analysis of Gene Expression Profiles and DNA Methylome reveals Oas1, Ppie, Polr2g as Pathogenic Target Genes of Gestational Diabetes Mellitus.. *Scientific reports*. PMID: 30389953
4. Implications of polyadenylation in health and disease.. *Nucleus (Austin, Tex.)*. PMID: 25484187
5. Systematic druggable genome-wide Mendelian randomization identifies therapeutic targets for calcium pyrophosphate deposition disease.. *Clinical rheumatology*. PMID: 40768106

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.2 |
| 高置信度残基 (pLDDT>90) 占比 | 54.8% |
| 置信残基 (pLDDT 70-90) 占比 | 24.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 13.6% |
| 有序区域 (pLDDT>70) 占比 | 79.7% |
| 可用 PDB 条目 | 1ZMF, 2CQB, 2KU7, 2KYX, 2R99, 3LPY, 3MDF, 3UCH, 5MQF, 5YZG |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1ZMF, 2CQB, 2KU7, 2KYX, 2R99, 3LPY, 3MDF, 3UCH, 5MQF, 5YZG）+ AlphaFold极高置信度预测（pLDDT=83.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029000, IPR020892, IPR002130, IPR012677, IPR016304; Pfam: PF00160, PF00076 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AQR | 0.999 | 0.979 | — |
| XAB2 | 0.999 | 0.997 | — |
| PRPF19 | 0.999 | 0.997 | — |
| CRNKL1 | 0.998 | 0.975 | — |
| SNW1 | 0.997 | 0.968 | — |
| BUD31 | 0.997 | 0.966 | — |
| SYF2 | 0.997 | 0.960 | — |
| CDC5L | 0.997 | 0.954 | — |
| BCAS2 | 0.996 | 0.954 | — |
| RBM22 | 0.996 | 0.960 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| XAB2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KMT2A | psi-mi:"MI:0018"(two hybrid) | pubmed:11313484 |
| PHYHIP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| trx | psi-mi:"MI:0096"(pull down) | pubmed:11976948|imex:IM-19924 |
| H3C1 | psi-mi:"MI:0065"(isothermal titration calorimetry) | imex:IM-14957|pubmed:20541251 |
| EBI-1801917 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-14957|pubmed:20541251 |
| EBI-2891648 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-14957|pubmed:20541251 |
| Prpf8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Snw1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| MAGOH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23084401|imex:IM-18688 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.2 + PDB: 1ZMF, 2CQB, 2KU7, 2KYX, 2R99,  | pLDDT=83.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nuclear speckles | 一致 |
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
1. PPIE — Peptidyl-prolyl cis-trans isomerase E，非常新颖，仅有少数基础研究。
2. 蛋白大小301 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UNP9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000084072-PPIE/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PPIE
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UNP9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
