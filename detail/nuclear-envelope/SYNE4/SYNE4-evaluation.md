---
type: protein-evaluation
gene: "SYNE4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SYNE4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SYNE4 / C19orf46 |
| 蛋白名称 | Nesprin-4 |
| 蛋白大小 | 404 aa / 43.5 kDa |
| UniProt ID | Q8N205 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus outer membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 404 aa / 43.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.2; PDB: 6R16, 6WMD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012315, IPR030268; Pfam: PF10541 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus outer membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- meiotic nuclear membrane microtubule tethering complex (GO:0034993)
- nuclear outer membrane (GO:0005640)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C19orf46 |

**关键文献**:
1. Genetic Hearing Loss Overview.. **. PMID: 20301607
2. Nucleocytoplasmic connections and deafness.. *The Journal of clinical investigation*. PMID: 23348730
3. A Nesprin-4/kinesin-1 cargo model for nuclear positioning in cochlear outer hair cells.. *Frontiers in cell and developmental biology*. PMID: 36211453
4. YEATS domain-containing protein GAS41 regulates nuclear shape by working in concert with BRD2 and the mediator complex in colorectal cancer.. *Pharmacological research*. PMID: 38964523
5. The LINC complex is essential for hearing.. *The Journal of clinical investigation*. PMID: 23348741

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.2 |
| 高置信度残基 (pLDDT>90) 占比 | 13.4% |
| 置信残基 (pLDDT 70-90) 占比 | 16.1% |
| 中等置信 (pLDDT 50-70) 占比 | 16.8% |
| 低置信 (pLDDT<50) 占比 | 53.7% |
| 有序区域 (pLDDT>70) 占比 | 29.5% |
| 可用 PDB 条目 | 6R16, 6WMD |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.2），有序残基占 29.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012315, IPR030268; Pfam: PF10541 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUN1 | 0.989 | 0.900 | — |
| SUN2 | 0.989 | 0.900 | — |
| SYNE3 | 0.943 | 0.000 | — |
| KIF5B | 0.925 | 0.329 | — |
| CCDC155 | 0.919 | 0.000 | — |
| SYNE1 | 0.912 | 0.000 | — |
| PLEC | 0.837 | 0.000 | — |
| KLC3 | 0.822 | 0.593 | — |
| KLC1 | 0.802 | 0.621 | — |
| SYNE2 | 0.778 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VTI1B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TCEA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CEP19 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MALL | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KTN1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| MARCHF2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| FATE1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| SFTPC | psi-mi:"MI:0397"(two hybrid array) | imex:IM-25511|pubmed:25910212 |
| ADIPOQ | psi-mi:"MI:0397"(two hybrid array) | imex:IM-25511|pubmed:25910212 |
| GOLIM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.2 + PDB: 6R16, 6WMD | pLDDT=57.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus outer membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. SYNE4 — Nesprin-4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小404 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=57.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N205
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181392-SYNE4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYNE4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N205
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
