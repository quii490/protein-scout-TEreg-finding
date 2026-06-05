---
type: protein-evaluation
gene: "APLF"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## APLF 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | APLF / C2orf13, PALF, XIP1 |
| 蛋白名称 | Aprataxin and PNK-like factor |
| 蛋白大小 | 511 aa / 57.0 kDa |
| UniProt ID | Q8IW19 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome; Cytoplasm, cytosol |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 511 aa / 57.0 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=41 篇 (≤60→6) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.5; PDB: 2KQB, 2KQC, 2KQD, 2KQE, 2KUO, 5E50, 5W7W |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039253, IPR019406, IPR041388, IPR008984; Pfam:  |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分 (÷1.83)** | | | **59.6/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Chromosome; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- site of DNA damage (GO:0090734)
- site of double-strand break (GO:0035861)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 41 |
| PubMed broad count | 79 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C2orf13, PALF, XIP1 |

**关键文献**:
1. APLF and long non-coding RNA NIHCOLE promote stable DNA synapsis in non-homologous end joining.. *Cell reports*. PMID: 36640344
2. APLF promotes the assembly and activity of non-homologous end joining protein complexes.. *The EMBO journal*. PMID: 23178593
3. XRCC1 mediates PARP1- and PAR-dependent recruitment of PARP2 to DNA damage sites.. *Nucleic acids research*. PMID: 39970298
4. The PARP3- and ATM-dependent phosphorylation of APLF facilitates DNA double-strand break repair.. *Nucleic acids research*. PMID: 23449221
5. APLF facilitates interstrand DNA crosslink repair and replication fork protection to confer cisplatin resistance.. *Nucleic acids research*. PMID: 38520407

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.5 |
| 高置信度残基 (pLDDT>90) 占比 | 22.5% |
| 置信残基 (pLDDT 70-90) 占比 | 13.7% |
| 中等置信 (pLDDT 50-70) 占比 | 14.9% |
| 低置信 (pLDDT<50) 占比 | 48.9% |
| 有序区域 (pLDDT>70) 占比 | 36.2% |
| 可用 PDB 条目 | 2KQB, 2KQC, 2KQD, 2KQE, 2KUO, 5E50, 5W7W, 5W7X, 5W7Y, 6ERF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.5），有序残基占 36.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039253, IPR019406, IPR041388, IPR008984; Pfam: PF17913, PF10283 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| XRCC4 | 0.999 | 0.741 | — |
| XRCC1 | 0.999 | 0.854 | — |
| XRCC5 | 0.999 | 0.982 | — |
| APTX | 0.992 | 0.000 | — |
| XRCC6 | 0.992 | 0.967 | — |
| CHFR | 0.979 | 0.000 | — |
| LIG3 | 0.969 | 0.782 | — |
| LIG4 | 0.935 | 0.834 | — |
| PARP1 | 0.919 | 0.847 | — |
| MACROH2A1 | 0.908 | 0.757 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| XRCC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17353262|imex:IM-19723 |
| XRCC4 | psi-mi:"MI:0018"(two hybrid) | pubmed:17353262|imex:IM-19723 |
| H2BC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MACROH2A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CST4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CST1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PARP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H2AC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| XRCC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| XRCC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.5 + PDB: 2KQB, 2KQC, 2KQD, 2KQE, 2KUO,  | pLDDT=61.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Cytoplasm, cytosol / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. APLF — Aprataxin and PNK-like factor，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小511 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 41 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IW19
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169621-APLF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=APLF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IW19
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:59:25

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000169621-APLF/subcellular

![](https://images.proteinatlas.org/34642/640_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/34642/640_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/34642/641_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/34642/641_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/34642/642_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/34642/642_D11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IW19-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
