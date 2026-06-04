---
type: protein-evaluation
gene: "ATF6B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ATF6B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATF6B / CREBL1, G13 |
| 蛋白名称 | Cyclic AMP-dependent transcription factor ATF-6 beta |
| 蛋白大小 | 703 aa / 76.7 kDa |
| UniProt ID | Q99941 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: Endoplasmic reticulum membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 703 aa / 76.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051882, IPR004827, IPR046347; Pfam: PF00170 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Supported |
| UniProt | Endoplasmic reticulum membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 58 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CREBL1, G13 |

**关键文献**:
1. CRISPR-Cas9-Mediated ATF6B Gene Editing Enhances Membrane Protein Production in HEK293T Cells.. *Bioengineering (Basel, Switzerland)*. PMID: 40281769
2. Impact of ATF6 deletion on the embryonic brain development.. *iScience*. PMID: 40487428
3. ATF6β Deficiency Elicits Anxiety-like Behavior and Hyperactivity Under Stress Conditions.. *Neurochemical research*. PMID: 36853481
4. Overlapping and differential functions of ATF6α versus ATF6β in the mouse heart.. *Scientific reports*. PMID: 30765833
5. Evaluation of genetic risk, its clinical manifestation and disease management based on 18 susceptibility gene markers among West-Slavonic patients with sarcoidosis.. *Gene*. PMID: 37336276

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.3 |
| 高置信度残基 (pLDDT>90) 占比 | 12.8% |
| 置信残基 (pLDDT 70-90) 占比 | 13.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.9% |
| 低置信 (pLDDT<50) 占比 | 62.2% |
| 有序区域 (pLDDT>70) 占比 | 25.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=54.3），有序残基占 25.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051882, IPR004827, IPR046347; Pfam: PF00170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATF4 | 0.962 | 0.000 | — |
| ATF6 | 0.961 | 0.535 | — |
| CREB1 | 0.953 | 0.000 | — |
| DDIT3 | 0.950 | 0.000 | — |
| WFS1 | 0.934 | 0.045 | — |
| CREB3L2 | 0.932 | 0.071 | — |
| CREB3L3 | 0.931 | 0.071 | — |
| CREB3L1 | 0.931 | 0.071 | — |
| CREB3L4 | 0.929 | 0.071 | — |
| CREB3 | 0.926 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| proP16 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A1U8QTN6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A384KT94 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| OS9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CLEC2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCDHB11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMED6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HLA-E | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TBC1D15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.3 + PDB: 无 | pLDDT=54.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus / Nucleoplasm; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ATF6B — Cyclic AMP-dependent transcription factor ATF-6 beta，非常新颖，仅有少数基础研究。
2. 蛋白大小703 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=54.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99941
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213676-ATF6B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATF6B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99941
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
