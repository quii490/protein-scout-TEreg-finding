---
type: protein-evaluation
gene: "GPR78"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR78 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR78 |
| 蛋白名称 | G-protein coupled receptor 78 |
| 蛋白大小 | 363 aa / 39.3 kDa |
| UniProt ID | Q96P69 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 363 aa / 39.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=58 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051880, IPR000276, IPR017452, IPR049579; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.0/180** | |
| **归一化总分** | | | **52.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 58 |
| PubMed broad count | 75 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A novel HIF-2α targeted inhibitor suppresses hypoxia-induced breast cancer stemness via SOD2-mtROS-PDI/GPR78-UPR(ER) axis.. *Cell death and differentiation*. PMID: 35301432
2. GPR78 Regulates Autophagy and Drug Resistance in Non-small Cell Lung Cancer.. *Alternative therapies in health and medicine*. PMID: 35986740
3. Association analysis of the chromosome 4p-located G protein-coupled receptor 78 (GPR78) gene in bipolar affective disorder and schizophrenia.. *Molecular psychiatry*. PMID: 16389273
4. Association of G protein-coupled receptor 78 with salivary dysfunction in male Sjögren's patients.. *Oral diseases*. PMID: 36652502
5. Constitutive Activity among Orphan Class-A G Protein Coupled Receptors.. *PloS one*. PMID: 26384023

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.6 |
| 高置信度残基 (pLDDT>90) 占比 | 61.7% |
| 置信残基 (pLDDT 70-90) 占比 | 23.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 10.5% |
| 有序区域 (pLDDT>70) 占比 | 84.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=84.6，有序区 84.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051880, IPR000276, IPR017452, IPR049579; Pfam: PF00001 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LPAR1 | 0.810 | 0.000 | — |
| ATF6 | 0.735 | 0.000 | — |
| ERN1 | 0.686 | 0.000 | — |
| HSPA5 | 0.669 | 0.000 | — |
| DNAJC1 | 0.559 | 0.000 | — |
| DDIT3 | 0.477 | 0.000 | — |
| XBP1 | 0.477 | 0.045 | — |
| TDGF1 | 0.434 | 0.049 | — |
| GPR32 | 0.423 | 0.000 | — |
| EIF2AK3 | 0.404 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 11，IntAct interactions: 0
- 调控相关比例: 1 / 11 = 9%

**评价**: STRING 11 个预测互作，IntAct 0 个实验互作。调控相关配体占比 9%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.6 + PDB: 无 | pLDDT=84.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 11 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPR78 — G-protein coupled receptor 78，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小363 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 58 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96P69
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155269-GPR78/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR78
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96P69
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
