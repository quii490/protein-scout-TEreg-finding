---
type: protein-evaluation
gene: "GNAZ"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GNAZ 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNAZ |
| 蛋白名称 | Guanine nucleotide-binding protein G(z) subunit alpha |
| 蛋白大小 | 355 aa / 40.9 kDa |
| UniProt ID | P19086 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 355 aa / 40.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=37 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=93.5; PDB: 8DZS, 9MD1 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001408, IPR001019, IPR011025, IPR027417; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell body (GO:0044297)
- cytoplasm (GO:0005737)
- dendrite (GO:0030425)
- endoplasmic reticulum (GO:0005783)
- heterotrimeric G-protein complex (GO:0005834)
- nuclear envelope (GO:0005635)
- plasma membrane (GO:0005886)
- synapse (GO:0045202)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 91 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Gnaz couples the circadian and dopaminergic system to G protein-mediated signaling in mouse photoreceptors.. *PloS one*. PMID: 29088301
2. Overexpressed GNAZ predicts poor outcome and promotes G0/G1 cell cycle progression in hepatocellular carcinoma.. *Gene*. PMID: 34530087
3. Analysis of GNAZ gene polymorphism in bipolar affective disorder.. *American journal of medical genetics*. PMID: 10402497
4. Expression of GNAZ, encoding the Gα(z) protein, predicts survival in mantle cell lymphoma.. *British journal of haematology*. PMID: 30788840
5. Free fatty acid receptor 4 agonists stimulate insulin secretion via different mechanisms in mouse versus human islets.. *bioRxiv : the preprint server for biology*. PMID: 40894772

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.5 |
| 高置信度残基 (pLDDT>90) 占比 | 83.9% |
| 置信残基 (pLDDT 70-90) 占比 | 13.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 0.8% |
| 有序区域 (pLDDT>70) 占比 | 96.9% |
| 可用 PDB 条目 | 8DZS, 9MD1 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（8DZS, 9MD1）+ AlphaFold高质量预测（pLDDT=93.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001408, IPR001019, IPR011025, IPR027417; Pfam: PF00503 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RGS20 | 0.952 | 0.695 | — |
| CRHR1 | 0.935 | 0.289 | — |
| IGF1R | 0.910 | 0.088 | — |
| GRM1 | 0.905 | 0.000 | — |
| RGS19 | 0.901 | 0.558 | — |
| GNB2 | 0.884 | 0.307 | — |
| GNB5 | 0.847 | 0.307 | — |
| GNB1 | 0.830 | 0.307 | — |
| GNG3 | 0.828 | 0.459 | — |
| GNB4 | 0.826 | 0.307 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000478892.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| BIRC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MED21 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FYTTD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NUFIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GJB7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HOXB5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM171A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MTHFR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EPHA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.5 + PDB: 8DZS, 9MD1 | pLDDT=93.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GNAZ — Guanine nucleotide-binding protein G(z) subunit alpha，非常新颖，仅有少数基础研究。
2. 蛋白大小355 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P19086
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128266-GNAZ/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNAZ
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P19086
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
