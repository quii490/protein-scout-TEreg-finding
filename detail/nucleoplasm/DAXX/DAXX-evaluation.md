---
type: protein-evaluation
gene: "DAXX"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DAXX — REJECTED (研究热度过高 (PubMed strict=733，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DAXX / BING2, DAP6 |
| 蛋白名称 | Death domain-associated protein 6 |
| 蛋白大小 | 740 aa / 81.4 kDa |
| UniProt ID | Q9UER7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; UniProt: Cytoplasm; Nucleus, nucleoplasm; Nucleus, PML body; Nucleus, |
| 蛋白大小 | 10/10 | ×1 | 10 | 740 aa / 81.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=733 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.6; PDB: 2KQS, 2KZS, 2KZU, 4H9N, 4H9O, 4H9P, 4H9Q |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR046378, IPR046426, IPR031333, IPR038298; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Enhanced |
| UniProt | Cytoplasm; Nucleus, nucleoplasm; Nucleus, PML body; Nucleus, nucleolus; Chromosome, centromere; Nucl... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome, centromeric region (GO:0000775)
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 733 |
| PubMed broad count | 1078 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BING2, DAP6 |

**关键文献**:
1. Driver mutations in histone H3.3 and chromatin remodelling genes in paediatric glioblastoma.. *Nature*. PMID: 22286061
2. Non-functional pancreatic neuroendocrine tumours: ATRX/DAXX and alternative lengthening of telomeres (ALT) are prognostically independent from ARX/PDX1 expression and tumour size.. *Gut*. PMID: 33849943
3. HIRA protects telomeres against R-loop-induced instability in ALT cancer cells.. *Cell reports*. PMID: 39509271
4. Daxx: death or survival protein?. *Trends in cell biology*. PMID: 16406523
5. Loss of DAXX/ATRX Protein Expression Results in Ischemia Resistance and Radiation Sensitivity in Pancreatic Neuroendocrine Tumor Cells and Is Associated with Improved Response to Trans-Arterial Radioembolization.. *Neuroendocrinology*. PMID: 40706576

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.6 |
| 高置信度残基 (pLDDT>90) 占比 | 37.2% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 56.6% |
| 有序区域 (pLDDT>70) 占比 | 40.6% |
| 可用 PDB 条目 | 2KQS, 2KZS, 2KZU, 4H9N, 4H9O, 4H9P, 4H9Q, 4H9R, 4H9S, 4HGA |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.6），有序残基占 40.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR046378, IPR046426, IPR031333, IPR038298; Pfam: PF03344, PF20920 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATRX | 0.999 | 0.991 | — |
| TP53 | 0.999 | 0.895 | — |
| H3-3B | 0.999 | 0.991 | — |
| FAS | 0.999 | 0.859 | — |
| PML | 0.999 | 0.925 | — |
| USP7 | 0.999 | 0.833 | — |
| MAP3K5 | 0.999 | 0.858 | — |
| SUMO1 | 0.999 | 0.991 | — |
| SP100 | 0.996 | 0.071 | — |
| MDM2 | 0.995 | 0.842 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000410772.2 | psi-mi:"MI:0096"(pull down) | pubmed:10698492|imex:IM-19433| |
| DEK | psi-mi:"MI:0071"(molecular sieving) | pubmed:12140263 |
| H4C16 | psi-mi:"MI:0071"(molecular sieving) | pubmed:12140263 |
| HDAC2 | psi-mi:"MI:0071"(molecular sieving) | pubmed:12140263 |
| CENPC | psi-mi:"MI:0018"(two hybrid) | pubmed:9645950 |
| PML | psi-mi:"MI:0018"(two hybrid) | pubmed:10669754 |
| Pax5 | psi-mi:"MI:0018"(two hybrid) | pubmed:11799127 |
| CREBBP | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11799127 |
| SUMO1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11948183 |
| MCRS1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11948183 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.6 + PDB: 2KQS, 2KZS, 2KZU, 4H9N, 4H9O,  | pLDDT=62.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleoplasm; Nucleus, PML body / Nucleoplasm, Nuclear bodies | 一致 |
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
1. DAXX — Death domain-associated protein 6，研究基础较多，新颖性有限。
2. 蛋白大小740 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 733 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 733 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UER7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204209-DAXX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DAXX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UER7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
