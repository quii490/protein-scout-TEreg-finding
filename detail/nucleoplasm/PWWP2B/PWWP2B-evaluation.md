---
type: protein-evaluation
gene: "PWWP2B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PWWP2B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PWWP2B / PWWP2 |
| 蛋白名称 | PWWP domain-containing protein 2B |
| 蛋白大小 | 590 aa / 64.0 kDa |
| UniProt ID | Q6NUJ5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 590 aa / 64.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.0; PDB: 4LD6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050390, IPR000313; Pfam: PF00855 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.5/180** | |
| **归一化总分** | | | **74.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PWWP2 |

**关键文献**:
1. PWWP2A/B: Prominent players in the proteomic landscape.. *Gene*. PMID: 39809369
2. PWWP2B Fine-Tunes Adipose Thermogenesis by Stabilizing HDACs in a NuRD Subcomplex.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 34180153
3. PWWP2B promotes DNA end resection and homologous recombination.. *EMBO reports*. PMID: 35582821
4. RNF43 and PWWP2B inhibit cancer cell proliferation and are predictive or prognostic biomarker for FDA-approved drugs in patients with advanced gastric cancer.. *Journal of Cancer*. PMID: 34149925

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.0 |
| 高置信度残基 (pLDDT>90) 占比 | 15.1% |
| 置信残基 (pLDDT 70-90) 占比 | 16.4% |
| 中等置信 (pLDDT 50-70) 占比 | 22.9% |
| 低置信 (pLDDT<50) 占比 | 45.6% |
| 有序区域 (pLDDT>70) 占比 | 31.5% |
| 可用 PDB 条目 | 4LD6 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.0），有序残基占 31.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050390, IPR000313; Pfam: PF00855 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRD4 | 0.762 | 0.606 | — |
| BRD2 | 0.672 | 0.641 | — |
| RBBP4 | 0.670 | 0.205 | — |
| BRD3 | 0.615 | 0.606 | — |
| TMEM251 | 0.606 | 0.000 | — |
| ASB12 | 0.549 | 0.000 | — |
| RBM12 | 0.512 | 0.000 | — |
| TAF5L | 0.497 | 0.000 | — |
| C2orf68 | 0.473 | 0.000 | — |
| ATP8B2 | 0.469 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PRKDC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PSMA3 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| HDAC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| P4HA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GOLGA6L9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ABI2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BRD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RBBP7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| Insr | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:30300385|imex:IM-26942| |
| PNMA8A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.0 + PDB: 4LD6 | pLDDT=60.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PWWP2B — PWWP domain-containing protein 2B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小590 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6NUJ5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171813-PWWP2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PWWP2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6NUJ5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
