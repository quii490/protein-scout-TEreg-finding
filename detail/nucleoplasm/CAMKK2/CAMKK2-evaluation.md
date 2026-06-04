---
type: protein-evaluation
gene: "CAMKK2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CAMKK2 — REJECTED (研究热度过高 (PubMed strict=323，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CAMKK2 / CAMKKB, KIAA0787 |
| 蛋白名称 | Calcium/calmodulin-dependent protein kinase kinase 2 |
| 蛋白大小 | 588 aa / 64.7 kDa |
| UniProt ID | Q96RR4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus; Cytoplasm; Cell projection, neuron projection |
| 蛋白大小 | 10/10 | ×1 | 10 | 588 aa / 64.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=323 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.8; PDB: 2ZV2, 5UY6, 5UYJ, 5VT1, 5YV8, 5YV9, 5YVA |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR000719, IPR017441, IPR008271; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cell projection, neuron projection | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- neuron projection (GO:0043005)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 323 |
| PubMed broad count | 457 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CAMKKB, KIAA0787 |

**关键文献**:
1. Buddleoside alleviates nonalcoholic steatohepatitis by targeting the AMPK-TFEB signaling pathway.. *Autophagy*. PMID: 39936600
2. Macrophage Sprouty4 deficiency diminishes sepsis-induced acute lung injury in mice.. *Redox biology*. PMID: 36334381
3. Activation of AMPK by GLP-1R agonists mitigates Alzheimer-related phenotypes in transgenic mice.. *Nature aging*. PMID: 40394225
4. Cardiomyocyte OTUD1 drives diabetic cardiomyopathy via directly deubiquitinating AMPKα2 and inducing mitochondrial dysfunction.. *Nature communications*. PMID: 40683882
5. Cytosolic DNA sensing by cGAS/STING promotes TRPV2-mediated Ca(2+) release to protect stressed replication forks.. *Molecular cell*. PMID: 36696898

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.8 |
| 高置信度残基 (pLDDT>90) 占比 | 37.6% |
| 置信残基 (pLDDT 70-90) 占比 | 12.6% |
| 中等置信 (pLDDT 50-70) 占比 | 9.4% |
| 低置信 (pLDDT<50) 占比 | 40.5% |
| 有序区域 (pLDDT>70) 占比 | 50.2% |
| 可用 PDB 条目 | 2ZV2, 5UY6, 5UYJ, 5VT1, 5YV8, 5YV9, 5YVA, 5YVB, 5YVC, 6BKU |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.8），有序残基占 50.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CALM3 | 0.999 | 0.343 | — |
| CALML3 | 0.998 | 0.072 | — |
| CALML5 | 0.998 | 0.072 | — |
| CALML6 | 0.997 | 0.045 | — |
| CALML4 | 0.997 | 0.045 | — |
| PRKAB2 | 0.975 | 0.256 | — |
| PRKAG1 | 0.975 | 0.427 | — |
| PRKAG2 | 0.975 | 0.301 | — |
| PRKAB1 | 0.973 | 0.352 | — |
| PRKAA2 | 0.964 | 0.503 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000498824.1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| CEP63 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| EBI-1380996 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| Csf1 | psi-mi:"MI:0096"(pull down) | pubmed:16267818|imex:IM-16654 |
| 38936" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| 38943" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| FLNA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| SMC1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| FLNC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.8 + PDB: 2ZV2, 5UY6, 5UYJ, 5VT1, 5YV8,  | pLDDT=66.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cell projection, neuron projec / Cytosol | 一致 |
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
1. CAMKK2 — Calcium/calmodulin-dependent protein kinase kinase 2，研究基础较多，新颖性有限。
2. 蛋白大小588 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 323 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 323 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96RR4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110931-CAMKK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CAMKK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96RR4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
