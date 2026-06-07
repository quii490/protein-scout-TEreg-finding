---
type: protein-evaluation
gene: "DNMBP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNMBP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNMBP |
| 蛋白名称 | Dynamin-binding protein |
| 蛋白大小 | 1577 aa / 177.3 kDa |
| UniProt ID | Q6XZF7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli, Golgi apparatus, Cytosol; 额外: Nucleoplasm, Nuclear; UniProt: Cytoplasm; Golgi apparatus, Golgi stack; Cytoplasm, cytoskel |
| 蛋白大小 | 5/10 | ×1 | 5 | 1577 aa / 177.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.9; PDB: 无 |
| 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.0/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Golgi apparatus, Cytosol; 额外: Nucleoplasm, Nuclear bodies | Approved |
| UniProt | Cytoplasm; Golgi apparatus, Golgi stack; Cytoplasm, cytoskeleton; Synapse; Cell junction | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 50 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Decoding ulcerative colitis pathogenesis through transcriptomics: from dysregulated gene networks to targeted intervention strategies.. *J Transl Autoimmun*. PMID: 41492412
2. Integrative Transcriptomic and Perturbagen Analyses Reveal Sex-Specific Molecular Signatures Across Glioma Subtypes.. *Cancers (Basel)*. PMID: 41514565
3. Proteomic ratio reveals subtype-specific genetic mechanisms and therapeutic targets in osteoarthritis.. *Clin Proteomics*. PMID: 41345833
4. The ubiquitin ligase Nedd4-2 promotes localization of DNMBP/Tuba to P-bodies under hyperosmotic stress.. *J Biol Chem*. PMID: 40975170
5. Unveiling the impact of interferon genes on the immune microenvironment of triple-negative breast cancer: identification of therapeutic targets.. *Front Bioinform*. PMID: 41132901

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.9 |
| 高置信度残基 (pLDDT>90) 占比 | 26.7% |
| 置信残基 (pLDDT 70-90) 占比 | 26.4% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 41.0% |
| 有序区域 (pLDDT>70) 占比 | 53.1% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 预测质量有限（pLDDT=63.9），有序残基占 53.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WASL | 0.000 | 0.000 | — |
| BIN1 | 0.000 | 0.000 | — |
| BIN3 | 0.000 | 0.000 | — |
| CDC42 | 0.000 | 0.000 | — |
| AMPH | 0.000 | 0.000 | — |
| WIPF2 | 0.000 | 0.000 | — |
| DNM1 | 0.000 | 0.000 | — |
| BIN2 | 0.000 | 0.000 | — |
| VASP | 0.000 | 0.000 | — |
| ENAH | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q6XZF7 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P48023 | psi-mi:"MI:0084"(phage display) | pubmed:- |
| uniprotkb:Q9NQY0 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:O60566 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P50570 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9UQ16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q3MHD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q3KQU3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P07237 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q5EBL8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.9 + PDB: 无 | pLDDT=63.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Golgi apparatus, Golgi stack; Cytoplasm / Nucleoli, Golgi apparatus, Cytosol; 额外: Nucleoplas | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DNMBP — Dynamin-binding protein，非常新颖，仅有少数基础研究。
2. 蛋白大小1577 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6XZF7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107554-DNMBP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNMBP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6XZF7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6XZF7 |
| SMART | SM00721;SM00325;SM00326; |
| UniProt Domain [FT] | DOMAIN 2..61; /note="SH3 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192"; DOMAIN 66..126; /note="SH3 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192"; DOMAIN 145..204; /note="SH3 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192"; DOMAIN 243..302; /note="SH3 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192"; DOMAIN 784..967; /note="DH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00062"; DOMAIN 1008..1217; /note="BAR"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00361"; DOMAIN 1285..1348; /note="SH3 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192"; DOMAIN 1513..1576; /note="SH3 6"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192" |
| InterPro | IPR027267;IPR004148;IPR035899;IPR000219;IPR035820;IPR035817;IPR035818;IPR035819;IPR051492;IPR001331;IPR036028;IPR001452; |
| Pfam | PF03114;PF00621;PF00018;PF07653;PF14604; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000107554-DNMBP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BIN3 | Intact, Biogrid, Opencell, Bioplex | true |
| C10orf88 | Bioplex | false |
| CAPZB | Opencell | false |
| CDC42 | Biogrid | false |
| CIAO2A | Bioplex | false |
| CRYBB3 | Bioplex | false |
| DHFR | Bioplex | false |
| DNM1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
