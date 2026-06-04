---
type: protein-evaluation
gene: "CIDEC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CIDEC — REJECTED (研究热度过高 (PubMed strict=209，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CIDEC / FSP27 |
| 蛋白名称 | Lipid transferase CIDEC |
| 蛋白大小 | 238 aa / 26.8 kDa |
| UniProt ID | Q96AQ7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Lipid droplet; Endoplasmic reticulum; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 238 aa / 26.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=209 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003508; Pfam: PF02017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Lipid droplet; Endoplasmic reticulum; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- lipid droplet (GO:0005811)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 209 |
| PubMed broad count | 296 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FSP27 |

**关键文献**:
1. Adipose Triglyceride Lipase Regulation: An Overview.. *Current protein & peptide science*. PMID: 28925902
2. Genetic and Epigenetic Regulation of the Innate Immune Response to Gout.. *Immunological investigations*. PMID: 36745138
3. Functional analysis of FSP27 protein regions for lipid droplet localization, caspase-dependent apoptosis, and dimerization with CIDEA.. *American journal of physiology. Endocrinology and metabolism*. PMID: 19843876
4. Mutational scanning pinpoints distinct binding sites of key ATGL regulators in lipolysis.. *Nature communications*. PMID: 38514628
5. Alcohol and fat promote steatohepatitis: a critical role for fat-specific protein 27/CIDEC.. *Journal of investigative medicine : the official publication of the American Federation for Clinical Research*. PMID: 27342423

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.8 |
| 高置信度残基 (pLDDT>90) 占比 | 26.5% |
| 置信残基 (pLDDT 70-90) 占比 | 35.3% |
| 中等置信 (pLDDT 50-70) 占比 | 21.4% |
| 低置信 (pLDDT<50) 占比 | 16.8% |
| 有序区域 (pLDDT>70) 占比 | 61.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=73.8，有序区 61.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003508; Pfam: PF02017 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLIN1 | 0.990 | 0.000 | — |
| CIDEA | 0.958 | 0.301 | — |
| DFFA | 0.916 | 0.000 | — |
| PPARG | 0.850 | 0.000 | — |
| LIPE | 0.812 | 0.000 | — |
| PLIN4 | 0.778 | 0.000 | — |
| LEP | 0.773 | 0.000 | — |
| CD36 | 0.759 | 0.000 | — |
| ADIPOQ | 0.743 | 0.000 | — |
| CREB3L3 | 0.740 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UFSP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| METTL15 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KLHL20 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NR0B2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SPATA12 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PRSS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TOP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZBTB42 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GSTT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.8 + PDB: 无 | pLDDT=73.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Lipid droplet; Endoplasmic reticulum; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CIDEC — Lipid transferase CIDEC，研究基础较多，新颖性有限。
2. 蛋白大小238 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 209 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 209 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96AQ7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187288-CIDEC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CIDEC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96AQ7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
