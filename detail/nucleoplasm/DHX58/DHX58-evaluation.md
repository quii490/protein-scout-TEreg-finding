---
type: protein-evaluation
gene: "DHX58"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DHX58 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DHX58 |
| 蛋白名称 | ATP-dependent RNA helicase DHX58 |
| 蛋白大小 | 678 aa / 76.6 kDa |
| UniProt ID | Q96C10 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Golgi apparatus, Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 678 aa / 76.6 kDa |
| 研究新颖性 | 2/10 | x5 | 10 | PubMed strict=94 篇 (<=100->2) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=91.0; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 21 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.5/180** | |
| **归一化总分** | | | **45.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 94 |
| PubMed broad count | 171 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Bacillus velezensis-fermented postbiotics as feed additives for viral infection control in largemouth bass (Micropterus salmoides).. *Fish Shellfish Immunol*. PMID: 42044706
2. Genome-wide identification, expression analysis and antiviral function of RIG-I-like receptors (RLRs) in basal chordate Branchiostoma japonicum.. *Fish Shellfish Immunol*. PMID: 41887303
3. The Effects of Tibetan Medicine Renqing Changjue Extracts on Cyclophosphamide-Induced Immunosuppression in a Mouse Model.. *Dose Response*. PMID: 42182618
4. SIRT3 deSUMOylation sustains hematopoietic stem cell activities under stressful conditions via the DHX58-IRF7 axis.. *Haematologica*. PMID: 42059296
5. Identification of DHX58 as a potential therapeutic target for ovarian cancer through multi-omics Mendelian randomization and transcriptomic data analysis.. *J Ovarian Res*. PMID: 41913250

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.0 |
| 高置信度残基 (pLDDT>90) 占比 | 71.7% |
| 置信残基 (pLDDT 70-90) 占比 | 24.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 95.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.0，有序区 95.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IFIH1 | 0.000 | 0.000 | — |
| MAVS | 0.000 | 0.000 | — |
| DDX58 | 0.000 | 0.000 | — |
| USP18 | 0.000 | 0.000 | — |
| ISG15 | 0.000 | 0.000 | — |
| IRF7 | 0.000 | 0.000 | — |
| IRF3 | 0.000 | 0.000 | — |
| DDX60 | 0.000 | 0.000 | — |
| TRIM25 | 0.000 | 0.000 | — |
| RSAD2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q96C10 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:O15226 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q7L2E3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:P56537 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:P19525 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q9UPY3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q9UKV8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:O95793 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9NUL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9H0D6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 21
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 21 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.0 + PDB: 无 | pLDDT=91.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Golgi apparatus, Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 25 + 21 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: **

**核心优势**:
1. DHX58 -- ATP-dependent RNA helicase DHX58，研究基础较多，新颖性有限。
2. 蛋白大小678 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 94 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96C10
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108771-DHX58/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DHX58
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96C10
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
