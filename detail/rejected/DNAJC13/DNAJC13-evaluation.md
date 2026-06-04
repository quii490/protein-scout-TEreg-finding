---
type: protein-evaluation
gene: "DNAJC13"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJC13 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC13 / KIAA0678, RME8 |
| 蛋白名称 | DnaJ homolog subfamily C member 13 |
| 蛋白大小 | 2243 aa / 254.4 kDa |
| UniProt ID | O75165 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles; 额外: Cytosol; UniProt: Early endosome; Early endosome membrane; Endosome membrane |
| 📏 蛋白大小 | 2/10 | ×1 | 2 | 2243 aa / 254.4 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.6; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR001623, IPR044978, IPR045 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **97.0/180** | |
| **归一化总分** | | | **53.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Cytosol | Supported |
| UniProt | Early endosome; Early endosome membrane; Endosome membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: Protein Atlas 中未找到该基因条目（无ENSG匹配），无法获取IF原图。

**GO Cellular Component**:
- azurophil granule membrane (GO:0035577)
- cytosol (GO:0005829)
- early endosome membrane (GO:0031901)
- endosome membrane (GO:0010008)
- extracellular exosome (GO:0070062)
- lysosomal membrane (GO:0005765)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0678, RME8 |

**关键文献**:
1. A conserved requirement for RME-8/DNAJC13 in neuronal autophagic lysosome reformation.. *Autophagy*. PMID: 37942902
2. Dysregulation of SNX1-retromer axis in pharmacogenetic models of Parkinson's disease.. *Cell death discovery*. PMID: 38886344
3. The Parkinson Disease-Associated Mutant DNAJC13(N855S) Leads to Its Accelerated Degradation and Negatively Affects Macroautophagy and Retromer Complex-Mediated Dynamics.. *Journal of cellular physiology*. PMID: 40717240
4. The genetic landscape of Parkinson's disease.. *Revue neurologique*. PMID: 30245141
5. VPS35 and DNAJC13 disease-causing variants in essential tremor.. *European journal of human genetics : EJHG*. PMID: 25118025

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.6 |
| 高置信度残基 (pLDDT>90) 占比 | 33.9% |
| 置信残基 (pLDDT 70-90) 占比 | 52.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 6.3% |
| 有序区域 (pLDDT>70) 占比 | 86.7% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=82.6，有序区 86.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR001623, IPR044978, IPR045802; Pfam: PF00226, PF14237, PF19432 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SNX1 | 0.942 | 0.330 | — |
| VPS35 | 0.937 | 0.292 | — |
| HSPA8 | 0.838 | 0.453 | — |
| DNAJC6 | 0.824 | 0.000 | — |
| SYNJ1 | 0.742 | 0.000 | — |
| ATP13A2 | 0.734 | 0.000 | — |
| TMEM230 | 0.731 | 0.000 | — |
| VPS13C | 0.718 | 0.000 | — |
| VPS29 | 0.692 | 0.000 | — |
| CHCHD2 | 0.690 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.6 + PDB: 无 | pLDDT=82.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Early endosome; Early endosome membrane; Endosome  / Vesicles; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DNAJC13 — DnaJ homolog subfamily C member 13，非常新颖，仅有少数基础研究。
2. 蛋白大小2243 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75165
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138246-DNAJC13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75165
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:17:00
