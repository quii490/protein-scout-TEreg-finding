---
type: protein-evaluation
gene: "CPNE3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CPNE3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPNE3 / CPN3, KIAA0636 |
| 蛋白名称 | Copine-3 |
| 蛋白大小 | 537 aa / 60.1 kDa |
| UniProt ID | O75131 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus; Cytoplasm; Cell membrane; Cell junction; Cell junct |
| 蛋白大小 | 10/10 | x1 | 10 | 537 aa / 60.1 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=92.2; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR000008, IPR035892, IPR037768, IPR045052, IPR010 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cell membrane; Cell junction; Cell junction, focal adhesion | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- azurophil granule membrane (GO:0035577)
- cell junction (GO:0030054)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- focal adhesion (GO:0005925)
- mitochondrion (GO:0005739)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CPN3, KIAA0636 |

**关键文献**:
1. YAP1-CPNE3 positive feedback pathway promotes gastric cancer cell progression.. *Cellular and molecular life sciences : CMLS*. PMID: 38493426
2. CPNE3 moderates the association between anxiety and working memory.. *Scientific reports*. PMID: 33767297
3. Upregulation of CPNE3 suppresses invasion, migration and proliferation of glioblastoma cells through FAK pathway inactivation.. *Journal of molecular histology*. PMID: 33725213
4. Copine 3 "CPNE3" is a novel regulator for insulin secretion and glucose uptake in pancreatic β-cells.. *Scientific reports*. PMID: 34667273
5. Quantitative proteomic analysis identifies CPNE3 as a novel metastasis-promoting gene in NSCLC.. *Journal of proteome research*. PMID: 23713811

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.2 |
| 高置信度残基 (pLDDT>90) 占比 | 80.1% |
| 置信残基 (pLDDT 70-90) 占比 | 16.8% |
| 中等置信 (pLDDT 50-70) 占比 | 1.7% |
| 低置信 (pLDDT<50) 占比 | 1.5% |
| 有序区域 (pLDDT>70) 占比 | 96.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度（pLDDT=92.2，有序区 96.9%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR037768, IPR045052, IPR010734; Pfam: PF00168, PF07002 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COPS5 | 0.616 | 0.292 | — |
| LMTK2 | 0.522 | 0.000 | — |
| SLC7A13 | 0.518 | 0.000 | — |
| BRD4 | 0.516 | 0.510 | — |
| MSMB | 0.503 | 0.000 | — |
| IL16 | 0.502 | 0.000 | — |
| EHBP1 | 0.496 | 0.000 | — |
| JAZF1 | 0.488 | 0.000 | — |
| CTBP2 | 0.467 | 0.000 | — |
| SRD5A2 | 0.456 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.2 + PDB: 无 | pLDDT=92.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cell membrane; Cell junction;  / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CPNE3 -- Copine-3，非常新颖，仅有少数基础研究。
2. 蛋白大小537 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75131
- Protein Atlas: https://www.proteinatlas.org/ENSG00000085719-CPNE3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPNE3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75131
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
