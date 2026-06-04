---
type: protein-evaluation
gene: "MECP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MECP2 — REJECTED (研究热度过高 (PubMed strict=3256，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MECP2 |
| 蛋白名称 | Methyl-CpG-binding protein 2 |
| 蛋白大小 | 486 aa / 52.4 kDa |
| UniProt ID | P51608 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 486 aa / 52.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=3256 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.6; PDB: 1QK9, 3C2I, 5BT2, 6C1Y, 6OGJ, 6OGK, 6YWW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016177, IPR017353, IPR045138, IPR001739; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- extracellular space (GO:0005615)
- heterochromatin (GO:0000792)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- postsynapse (GO:0098794)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3256 |
| PubMed broad count | 4190 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. MECP2 directly interacts with RNA polymerase II to modulate transcription in human neurons.. *Neuron*. PMID: 38697112
2. Preclinical Milestones in MECP2 Gene Transfer for Treating Rett Syndrome.. *Developmental neuroscience*. PMID: 38723617
3. Acute MeCP2 loss in adult mice reveals transcriptional and chromatin changes that precede neurological dysfunction and inform pathogenesis.. *Neuron*. PMID: 39689710
4. The Efficacy of a Human-Ready miniMECP2 Gene Therapy in a Pre-Clinical Model of Rett Syndrome.. *Genes*. PMID: 38254921
5. Rett syndrome.. *Current opinion in neurology*. PMID: 15791137

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.6 |
| 高置信度残基 (pLDDT>90) 占比 | 8.2% |
| 置信残基 (pLDDT 70-90) 占比 | 8.6% |
| 中等置信 (pLDDT 50-70) 占比 | 41.6% |
| 低置信 (pLDDT<50) 占比 | 41.6% |
| 有序区域 (pLDDT>70) 占比 | 16.8% |
| 可用 PDB 条目 | 1QK9, 3C2I, 5BT2, 6C1Y, 6OGJ, 6OGK, 6YWW, 8AJR, 8ALQ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=56.6），有序残基占 16.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016177, IPR017353, IPR045138, IPR001739; Pfam: PF01429 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HDAC1 | 0.999 | 0.757 | — |
| SIN3A | 0.999 | 0.842 | — |
| DNMT1 | 0.998 | 0.295 | — |
| NCOR1 | 0.997 | 0.516 | — |
| HDAC2 | 0.997 | 0.124 | — |
| CREB1 | 0.996 | 0.199 | — |
| RCOR1 | 0.994 | 0.292 | — |
| SUV39H1 | 0.993 | 0.292 | — |
| ATRX | 0.981 | 0.379 | — |
| YBX1 | 0.978 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SOX18 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Hdac2 | psi-mi:"MI:0028"(cosedimentation in solution) | pubmed:15696166 |
| Smarca2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15696166 |
| Smarce1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15696166 |
| ENSP00000486089.2 | psi-mi:"MI:0413"(electrophoretic mobility shift as | pubmed:23452848|imex:IM-20940 |
| Atrx | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23452848|imex:IM-20940 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| ARHGAP22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| FGD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| GTPBP10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.6 + PDB: 1QK9, 3C2I, 5BT2, 6C1Y, 6OGJ,  | pLDDT=56.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. MECP2 — Methyl-CpG-binding protein 2，研究基础较多，新颖性有限。
2. 蛋白大小486 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3256 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 3256 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51608
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169057-MECP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MECP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51608
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
