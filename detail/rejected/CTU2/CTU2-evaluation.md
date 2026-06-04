---
type: protein-evaluation
gene: "CTU2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CTU2 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTU2 / C16orf84, NCS2 |
| 蛋白名称 | Cytoplasmic tRNA 2-thiolation protein 2 |
| 蛋白大小 | 515 aa / 56.1 kDa |
| UniProt ID | Q2VPK5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Mitochondria, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 515 aa / 56.1 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=79.4; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR019407, IPR014729; Pfam: PF10288 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria, Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- cytosol (GO:0005829)
- protein-containing complex (GO:0032991)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf84, NCS2 |

**关键文献**:
1. Codon-specific translation reprogramming promotes resistance to targeted therapy.. *Nature*. PMID: 29925953
2. Activation of CTU2 expression by LXR promotes the development of hepatocellular carcinoma.. *Cell biology and toxicology*. PMID: 38630355
3. The tRNA thiolation-mediated translational control is essential for plant immunity.. *eLife*. PMID: 38284752
4. Biallelic variants in CTU2 cause DREAM-PL syndrome and impair thiolation of tRNA wobble U34.. *Human mutation*. PMID: 31301155
5. The conserved wobble uridine tRNA thiolase Ctu1 is required for angiogenesis and embryonic development.. *PloS one*. PMID: 39705244

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.4 |
| 高置信度残基 (pLDDT>90) 占比 | 57.3% |
| 置信残基 (pLDDT 70-90) 占比 | 17.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 17.7% |
| 有序区域 (pLDDT>70) 占比 | 75.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=79.4，有序区 75.2%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019407, IPR014729; Pfam: PF10288 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.4 + PDB: 无 | pLDDT=79.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Mitochondria, Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CTU2 -- Cytoplasmic tRNA 2-thiolation protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小515 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2VPK5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174177-CTU2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTU2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2VPK5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
