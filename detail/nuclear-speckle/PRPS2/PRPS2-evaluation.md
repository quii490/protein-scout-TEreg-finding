---
type: protein-evaluation
gene: "PRPS2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRPS2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRPS2 |
| 蛋白名称 | Ribose-phosphate pyrophosphokinase 2 |
| 蛋白大小 | 318 aa / 34.8 kDa |
| UniProt ID | P11908 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nuclear speckles, Basal body; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 318 aa / 34.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=38 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=95.3; PDB: 7YK1, 8YI9, 8YPY |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000842, IPR029099, IPR029057, IPR000836, IPR005 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nuclear speckles, Basal body | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 38 |
| PubMed broad count | 68 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Therapy-induced mutations drive the genomic landscape of relapsed acute lymphoblastic leukemia.. *Blood*. PMID: 31697823
2. Protein and nucleotide biosynthesis are coupled by a single rate-limiting enzyme, PRPS2, to drive cancer.. *Cell*. PMID: 24855946
3. Phosphoribosyl-pyrophosphate synthetase 2 (PRPS2) depletion regulates spermatogenic cell apoptosis and is correlated with hypospermatogenesis.. *Asian journal of andrology*. PMID: 31736475
4. Role of PRPS2 as a prognostic and therapeutic target in osteosarcoma.. *Journal of clinical pathology*. PMID: 33589531
5. Host protein PRPS2 interact with the non-structural protein p17 of Avian Reovirus and promote viral replication.. *Poultry science*. PMID: 39631276

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.3 |
| 高置信度残基 (pLDDT>90) 占比 | 91.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.7% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 97.2% |
| 可用 PDB 条目 | 7YK1, 8YI9, 8YPY |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7YK1, 8YI9, 8YPY）+ AlphaFold高质量预测（pLDDT=95.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000842, IPR029099, IPR029057, IPR000836, IPR005946; Pfam: PF14572, PF13793 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRPS1 | 0.985 | 0.847 | — |
| PRPSAP1 | 0.985 | 0.907 | — |
| PRPSAP2 | 0.981 | 0.881 | — |
| PPAT | 0.975 | 0.191 | — |
| TKT | 0.958 | 0.000 | — |
| RBKS | 0.957 | 0.114 | — |
| RPIA | 0.957 | 0.000 | — |
| TKTL2 | 0.956 | 0.000 | — |
| TKTL1 | 0.956 | 0.000 | — |
| PGM2 | 0.944 | 0.094 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000370043.5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| PRS5 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| PRS2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSZ1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| EBI-1257123 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-20587 |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |
| PRPSAP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NMT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRIM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.3 + PDB: 7YK1, 8YI9, 8YPY | pLDDT=95.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Vesicles; 额外: Nuclear speckles, Basal body | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PRPS2 — Ribose-phosphate pyrophosphokinase 2，非常新颖，仅有少数基础研究。
2. 蛋白大小318 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 38 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P11908
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101911-PRPS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRPS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P11908
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
