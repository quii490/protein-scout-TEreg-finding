---
type: protein-evaluation
gene: "PHOX2B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PHOX2B — REJECTED (研究热度过高 (PubMed strict=482，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PHOX2B / PMX2B |
| 蛋白名称 | Paired mesoderm homeobox protein 2B |
| 蛋白大小 | 314 aa / 31.6 kDa |
| UniProt ID | Q99453 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 314 aa / 31.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=482 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.8; PDB: 7MJA, 8EK5, 8P7G, 8PTL, 8PUI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR050649; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 482 |
| PubMed broad count | 893 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PMX2B |

**关键文献**:
1. Engineered human pluripotent-stem-cell-derived intestinal tissues with a functional enteric nervous system.. *Nature medicine*. PMID: 27869805
2. Heterogeneity of neuroblastoma cell identity defined by transcriptional circuitries.. *Nature genetics*. PMID: 28740262
3. Targeting of intracellular oncoproteins with peptide-centric CARs.. *Nature*. PMID: 37938771
4. A medullary centre for lapping in mice.. *Nature communications*. PMID: 34728601
5. Molecular ontology of the parabrachial nucleus.. *The Journal of comparative neurology*. PMID: 35134251

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.8 |
| 高置信度残基 (pLDDT>90) 占比 | 17.2% |
| 置信残基 (pLDDT 70-90) 占比 | 5.4% |
| 中等置信 (pLDDT 50-70) 占比 | 35.4% |
| 低置信 (pLDDT<50) 占比 | 42.0% |
| 有序区域 (pLDDT>70) 占比 | 22.6% |
| 可用 PDB 条目 | 7MJA, 8EK5, 8P7G, 8PTL, 8PUI |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=59.8），有序残基占 22.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR050649; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ASCL1 | 0.894 | 0.000 | — |
| DBH | 0.834 | 0.000 | — |
| HAND2 | 0.833 | 0.000 | — |
| EDN3 | 0.785 | 0.000 | — |
| RET | 0.782 | 0.000 | — |
| ISL1 | 0.773 | 0.000 | — |
| TH | 0.763 | 0.000 | — |
| GDNF | 0.749 | 0.000 | — |
| GATA3 | 0.738 | 0.000 | — |
| EDNRB | 0.730 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=59.8 + PDB: 7MJA, 8EK5, 8P7G, 8PTL, 8PUI | pLDDT=59.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PHOX2B — Paired mesoderm homeobox protein 2B，研究基础较多，新颖性有限。
2. 蛋白大小314 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 482 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 482 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99453
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109132-PHOX2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHOX2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99453
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
