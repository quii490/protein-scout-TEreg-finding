---
type: protein-evaluation
gene: "ARL2BP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARL2BP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARL2BP / BART, BART1 |
| 蛋白名称 | ADP-ribosylation factor-like protein 2-binding protein |
| 蛋白大小 | 163 aa / 18.8 kDa |
| UniProt ID | Q9Y2Y0 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 02:31:43 |

**IF 图像**:
![](https://images.proteinatlas.org/43066/2185_C1_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/43066/2185_C1_20_blue_red_green.jpg)

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 6/10 | x4 | 24 | HPA: Nucleoplasm, Cytosol; UniProt: C... |
| 蛋白大小 | 7/10 | x1 | 7 | 163 aa / 18.8 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=15 篇 (<=20->10) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=80.8; PDB: 2K9A, 3DOE, ... |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: 3; Pfam: 1; IPR038849, IPR023379... |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.5 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5; PDB 多条目覆盖: +0.5 |
| **原始总分** | | | **154.5/180** | |
| **归一化总分 (/1.83)** | | | **84.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm, Centrosome, Basal body, Cytosol | Supported |
| UniProt | Cytoplasm, Mitochondrion intermembrane space, Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: 原图已通过HPA检索获取，见上方嵌入图像。

**GO Cellular Component**:
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)
- midbody (GO:0030496)
- mitochondrial intermembrane space (GO:0005758)
- mitochondrial matrix (GO:0005759)
- nucleoplasm (GO:0005654)
- spindle (GO:0005819)

**结论**: 核定位证据较好，主要数据源支持核定位，但存在一定程度的其它亚细胞定位信号。

#### 3.2 蛋白大小评估

**评价**: 163 aa，蛋白较小，但仍在可操作范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BART, BART1 |

**关键文献**:
1. Nonsyndromic Retinitis Pigmentosa Overview.. **. PMID: 20301590
2. Construction of the model for predicting prognosis by key genes regulating EGFR-TKI resistance.. *Frontiers in genetics*. PMID: 36506325
3. Syndromic forms of inherited retinal dystrophies: a comprehensive molecular diagnosis of consanguineous Pakistani families using capture panel sequencing.. *Molecular vision*. PMID: 40384762
4. Mutations in ARL2BP, encoding ADP-ribosylation-factor-like 2 binding protein, cause autosomal-recessive retinitis pigmentosa.. *American journal of human genetics*. PMID: 23849777
5. Novel homozygous splicing mutations in ARL2BP cause autosomal recessive retinitis pigmentosa.. *Molecular vision*. PMID: 30210231

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.8 |
| 高置信度残基 (pLDDT>90) 占比 | 46.6% |
| 置信残基 (pLDDT 70-90) 占比 | 25.8% |
| 中等置信 (pLDDT 50-70) 占比 | 21.5% |
| 低置信 (pLDDT<50) 占比 | 6.1% |
| 有序区域 (pLDDT>70) 占比 | 72.4% |
| 可用 PDB 条目 | 2K9A, 3DOE, 3DOF |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: PDB实验结构 + AlphaFold高质量预测（pLDDT=80.8），结构可信度高。三维结构评分 9/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038849, IPR023379, IPR042541; Pfam: PF11527 |

**染色质调控潜力分析**: 存在 4 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RPGR | 0.505 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ARL2 | two hybrid array | imex:IM-15364|pubmed:21988832 |
| CAMK2D | two hybrid array | imex:IM-15364|pubmed:21988832 |
| MPP3 | two hybrid array | imex:IM-15364|pubmed:21988832 |
| RAC1 | two hybrid pooling approach | pubmed:20936779|imex:IM-17049 |
| CFAP20 | two hybrid array | pubmed:32296183|imex:IM-25472 |
| ARL3 | inference by socio-affinity scoring | pubmed:unassigned1312 |
| FSD1 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| PNKD | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| GNPAT | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| ATE1 | anti tag coimmunoprecipitation | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.8 + PDB: 2K9A, 3DOE, 3DOF | pLDDT=80.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleoplasm / Nucleus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0.5
**总分**: +2.5 / max +3

### 4. 总体评价

**归一化总分**: 84.4/100

**核心优势**:
1. ARL2BP -- ADP-ribosylation factor-like protein 2-binding protein，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. AlphaFold高质量预测（pLDDT=80.8），结构可信度高。
3. 已有PDB实验结构：2K9A, 3DOE, 3DOF。
4. 存在 4 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 暂无明显风险因素。

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2Y0
- Protein Atlas: https://www.proteinatlas.org/search/ARL2BP
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARL2BP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2Y0
- STRING: https://string-db.org/network/9606.ARL2BP
- Packet data timestamp: 2026-06-03 02:31:43
