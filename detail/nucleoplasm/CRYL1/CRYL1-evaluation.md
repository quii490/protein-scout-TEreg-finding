---
type: protein-evaluation
gene: "CRYL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CRYL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRYL1 / CRY |
| 蛋白名称 | Lambda-crystallin homolog |
| 蛋白大小 | 319 aa / 35.4 kDa |
| UniProt ID | Q9Y2S2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm, Nucleoli; 额外: Golgi apparatus, Plasma membrane; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 319 aa / 35.4 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=25 篇 (<=40->8) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=96.4; PDB: 3F3S |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR022694, IPR006180, IPR006176, IPR006108, IPR008 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Golgi apparatus, Plasma membrane | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CRY |

**关键文献**:
1. GJB2-Related Autosomal Recessive Nonsyndromic Hearing Loss.. **. PMID: 20301449
2. Genome-wide meta-analysis identifies new candidate genes for sickle cell disease nephropathy.. *Blood advances*. PMID: 36399516
3. Downregulation of Crystallin Lambda 1 is a New Independent Prognostic Marker in Clear Cell Renal Cell Carcinoma.. *Pharmacogenomics and personalized medicine*. PMID: 36246497
4. Human CRYL1, a novel enzyme-crystallin overexpressed in liver and kidney and downregulated in 58% of liver cancer tissues from 60 Chinese patients, and four new homologs from other mammalians.. *Gene*. PMID: 12527201
5. A Novel Recurrent 200 kb CRYL1 Deletion Underlies DFNB1A Hearing Loss in Patients from Northwestern Spain.. *Genes*. PMID: 40565562

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.4 |
| 高置信度残基 (pLDDT>90) 占比 | 96.2% |
| 置信残基 (pLDDT 70-90) 占比 | 1.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 1.3% |
| 有序区域 (pLDDT>70) 占比 | 97.8% |
| 可用 PDB 条目 | 3F3S |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=96.4，有序区 97.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022694, IPR006180, IPR006176, IPR006108, IPR008927; Pfam: PF00725, PF02737 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACAA1 | 0.933 | 0.546 | — |
| AKR1A1 | 0.927 | 0.000 | — |
| HSDL2 | 0.901 | 0.092 | — |
| ACAA2 | 0.882 | 0.481 | — |
| ACAT2 | 0.879 | 0.481 | — |
| SCP2 | 0.878 | 0.066 | — |
| ACAT1 | 0.875 | 0.481 | — |
| HADHB | 0.872 | 0.481 | — |
| CARTPT | 0.867 | 0.481 | — |
| ACOT8 | 0.866 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ci | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| aru | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Neos | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ABCC6 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| Cpr97Eb | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| MYO9A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PIK3C2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HAUS5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| USP19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.4 + PDB: 3F3S | pLDDT=96.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Nucleoli; 额外: Golgi apparatus, Plasma | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. CRYL1 -- Lambda-crystallin homolog，非常新颖，仅有少数基础研究。
2. 蛋白大小319 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2S2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165475-CRYL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRYL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2S2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
