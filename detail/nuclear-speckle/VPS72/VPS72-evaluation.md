---
type: protein-evaluation
gene: "VPS72"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VPS72 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VPS72 / TCFL1, YL1 |
| 蛋白名称 | Vacuolar protein sorting-associated protein 72 homolog |
| 蛋白大小 | 364 aa / 40.6 kDa |
| UniProt ID | Q15906 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 364 aa / 40.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.0; PDB: 5FUG, 8QR1, 8X15, 8X19, 8X1C, 8XVG, 8XVT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013272, IPR046757; Pfam: PF05764, PF08265 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **152.0/180** | |
| **归一化总分** | | | **84.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- NuA4 histone acetyltransferase complex (GO:0035267)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleosome (GO:0000786)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TCFL1, YL1 |

**关键文献**:
1. Targeting VPS72 inhibits ACTL6A/MYC axis activity in HCC progression.. *Hepatology (Baltimore, Md.)*. PMID: 36631007
2. Expression Analysis of VPS72 and Associated Biological Behaviors in Colon Cancer.. *International journal of general medicine*. PMID: 39135633
3. Bioinformatics Analysis and RNA-Sequencing of SCAMP3 Expression and Correlated Gene Regulation in Hepatocellular Carcinoma.. *OncoTargets and therapy*. PMID: 32099407
4. Prognostic marker VPS72 could promote the malignant progression of prostate cancer.. *BMC cancer*. PMID: 38858662
5. Cooperative and Opposing Functions of ANP32E and VPS72 Govern Gene Promoter Chromatin Status.. *Research square*. PMID: 41646306

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.0 |
| 高置信度残基 (pLDDT>90) 占比 | 28.3% |
| 置信残基 (pLDDT 70-90) 占比 | 29.7% |
| 中等置信 (pLDDT 50-70) 占比 | 22.0% |
| 低置信 (pLDDT<50) 占比 | 20.1% |
| 有序区域 (pLDDT>70) 占比 | 58.0% |
| 可用 PDB 条目 | 5FUG, 8QR1, 8X15, 8X19, 8X1C, 8XVG, 8XVT, 9C57, 9C62, 9CA7 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5FUG, 8QR1, 8X15, 8X19, 8X1C, 8XVG, 8XVT, 9C57, 9C62, 9CA7）+ AlphaFold极高置信度预测（pLDDT=73.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013272, IPR046757; Pfam: PF05764, PF08265 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DMAP1 | 0.999 | 0.940 | — |
| RUVBL1 | 0.999 | 0.965 | — |
| YEATS4 | 0.998 | 0.879 | — |
| RUVBL2 | 0.998 | 0.921 | — |
| H2AZ1 | 0.998 | 0.989 | — |
| SRCAP | 0.997 | 0.932 | — |
| TRRAP | 0.996 | 0.794 | — |
| KAT5 | 0.996 | 0.865 | — |
| ZNHIT1 | 0.993 | 0.955 | — |
| MORF4L1 | 0.991 | 0.870 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| D6VTA8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-14085|pubmed:21179020 |
| CALCOCO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MRGBP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12963728 |
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MDFI | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SWC4 | psi-mi:"MI:0096"(pull down) | pubmed:14690591 |
| UBC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| ZNHIT1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| RUVBL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15647280 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.0 + PDB: 5FUG, 8QR1, 8X15, 8X19, 8X1C,  | pLDDT=73.0, v6 | 预测+实验 |
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
1. VPS72 — Vacuolar protein sorting-associated protein 72 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小364 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15906
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163159-VPS72/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VPS72
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15906
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
