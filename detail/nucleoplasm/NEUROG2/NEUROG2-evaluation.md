---
type: protein-evaluation
gene: "NEUROG2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NEUROG2 — REJECTED (研究热度过高 (PubMed strict=121，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NEUROG2 / ATOH4, BHLHA8, NGN2 |
| 蛋白名称 | Neurogenin-2 |
| 蛋白大小 | 272 aa / 28.6 kDa |
| UniProt ID | Q9H2A3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 272 aa / 28.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=121 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050359, IPR036638, IPR032655; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 121 |
| PubMed broad count | 457 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ATOH4, BHLHA8, NGN2 |

**关键文献**:
1. Examining the NEUROG2 lineage and associated gene expression in human cortical organoids.. *Development (Cambridge, England)*. PMID: 39680368
2. Therapeutic potential of astrocyte transdifferentiated neurons.. *Neural regeneration research*. PMID: 41467429
3. Essential transcription factors for induced neuron differentiation.. *Nature communications*. PMID: 38102126
4. The Neurog2-Tbr2 axis forms a continuous transition to the neurogenic gene expression state in neural stem cells.. *Developmental cell*. PMID: 38772376
5. A novel role for Neurog2 in MYCN driven neuroendocrine plasticity of prostate cancer.. *Oncogene*. PMID: 40301542

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.9 |
| 高置信度残基 (pLDDT>90) 占比 | 23.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 33.1% |
| 低置信 (pLDDT<50) 占比 | 38.2% |
| 有序区域 (pLDDT>70) 占比 | 28.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.9），有序残基占 28.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050359, IPR036638, IPR032655; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ASCL1 | 0.976 | 0.113 | — |
| PAX6 | 0.908 | 0.045 | — |
| ISL1 | 0.897 | 0.048 | — |
| LHX3 | 0.897 | 0.000 | — |
| SOX1 | 0.875 | 0.051 | — |
| LMX1A | 0.872 | 0.048 | — |
| SOX2 | 0.850 | 0.051 | — |
| POU4F1 | 0.834 | 0.000 | — |
| OLIG2 | 0.825 | 0.091 | — |
| LHX1 | 0.812 | 0.048 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PFDN5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TCF4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.9 + PDB: 无 | pLDDT=62.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NEUROG2 — Neurogenin-2，研究基础较多，新颖性有限。
2. 蛋白大小272 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 121 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 121 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H2A3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178403-NEUROG2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NEUROG2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H2A3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
