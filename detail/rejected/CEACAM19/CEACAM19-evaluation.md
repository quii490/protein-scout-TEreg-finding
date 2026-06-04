---
type: protein-evaluation
gene: "CEACAM19"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CEACAM19 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEACAM19 / CEAL1 |
| 蛋白名称 | Cell adhesion molecule CEACAM19 |
| 蛋白大小 | 300 aa / 32.6 kDa |
| UniProt ID | Q7Z692 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 300 aa / 32.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050831, IPR036179, IPR013783, IPR013106; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CEAL1 |

**关键文献**:
1. Aberrant CEACAM19 expression is associated with metastatic phenotype in penile cancer.. *Cancer management and research*. PMID: 30679925
2. The expression of the CEACAM19 gene, a novel member of the CEA family, is associated with breast cancer progression.. *International journal of oncology*. PMID: 23525470
3. Identification and expression analysis of novel splice variants of the human carcinoembryonic antigen-related cell adhesion molecule 19 (CEACAM19) gene using a high-throughput sequencing approach.. *Genomics*. PMID: 32659328
4. Integrated Multi-Omics Signature Predicts Survival in Head and Neck Cancer.. *Cells*. PMID: 36010616
5. Lnc-PSMA8-1 activated by GEFT promotes rhabdomyosarcoma progression via upregulation of mTOR expression by sponging miR-144-3p.. *BMC cancer*. PMID: 38225540

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.1 |
| 高置信度残基 (pLDDT>90) 占比 | 35.7% |
| 置信残基 (pLDDT 70-90) 占比 | 11.7% |
| 中等置信 (pLDDT 50-70) 占比 | 24.0% |
| 低置信 (pLDDT<50) 占比 | 28.7% |
| 有序区域 (pLDDT>70) 占比 | 47.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.1），有序残基占 47.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050831, IPR036179, IPR013783, IPR013106; Pfam: PF07686 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CEACAM18 | 0.822 | 0.000 | — |
| CEACAM20 | 0.741 | 0.000 | — |
| CEACAM21 | 0.652 | 0.000 | — |
| PRSS36 | 0.581 | 0.000 | — |
| CLPTM1 | 0.510 | 0.000 | — |
| PVR | 0.505 | 0.000 | — |
| BCL3 | 0.489 | 0.000 | — |
| CEACAM4 | 0.457 | 0.000 | — |
| IGSF23 | 0.450 | 0.000 | — |
| LIPE | 0.445 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 11，IntAct interactions: 0
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.1 + PDB: 无 | pLDDT=69.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 11 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CEACAM19 — Cell adhesion molecule CEACAM19，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小300 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z692
- Protein Atlas: https://www.proteinatlas.org/search/CEACAM19
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEACAM19
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z692
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CEACAM19/CEACAM19-PAE.png]]
