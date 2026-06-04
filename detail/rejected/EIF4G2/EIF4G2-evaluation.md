---
type: protein-evaluation
gene: "EIF4G2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF4G2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=110，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF4G2 / DAP5 |
| 蛋白名称 | Eukaryotic translation initiation factor 4 gamma 2 |
| 蛋白大小 | 907 aa / 102.4 kDa |
| UniProt ID | P78344 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 907 aa / 102.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=110 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=71.9; PDB: 3D3M, 3L6A, 4IUL, 9JJ7 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR003891, IPR003890, IPR003307; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **69.0/180** | |
| **归一化总分** | | | **38.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- adherens junction (GO:0005912)
- cytosol (GO:0005829)
- eukaryotic translation initiation factor 4F complex (GO:0016281)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 110 |
| PubMed broad count | 209 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DAP5 |

**关键文献**:
1. Extensive translation of circular RNAs driven by N(6)-methyladenosine.. *Cell research*. PMID: 28281539
2. ERα is an RNA-binding protein sustaining tumor cell survival and drug resistance.. *Cell*. PMID: 34559986
3. Neuronal activity rapidly reprograms dendritic translation via eIF4G2:uORF binding.. *Nature neuroscience*. PMID: 38589584
4. Specific mechanisms of translation initiation in higher eukaryotes: the eIF4G2 story.. *RNA (New York, N.Y.)*. PMID: 36517212
5. Eukaryotic translation initiation factor eIF4G2 opens novel paths for protein synthesis in development, apoptosis and cell differentiation.. *Cell proliferation*. PMID: 36547008

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.9 |
| 高置信度残基 (pLDDT>90) 占比 | 41.3% |
| 置信残基 (pLDDT 70-90) 占比 | 22.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.1% |
| 低置信 (pLDDT<50) 占比 | 30.4% |
| 有序区域 (pLDDT>70) 占比 | 63.5% |
| 可用 PDB 条目 | 3D3M, 3L6A, 4IUL, 9JJ7 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3D3M, 3L6A, 4IUL, 9JJ7）+ AlphaFold高质量预测（pLDDT=71.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR003891, IPR003890, IPR003307; Pfam: PF02847, PF02854, PF02020 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF4E | 0.999 | 0.515 | — |
| EIF4A2 | 0.999 | 0.718 | — |
| EIF4A1 | 0.999 | 0.923 | — |
| YTHDF3 | 0.996 | 0.191 | — |
| EIF4G1 | 0.984 | 0.604 | — |
| EIF4B | 0.976 | 0.579 | — |
| EIF4E1B | 0.970 | 0.515 | — |
| EIF4G3 | 0.968 | 0.595 | — |
| EIF4E2 | 0.949 | 0.091 | — |
| EIF4H | 0.932 | 0.284 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Pik3r1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| SBP1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| AAR2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| CBC2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| BOI1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| STO1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SGN1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| AIR2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| PUB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| NAM8 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 5 / 15 = 33%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 33%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.9 + PDB: 3D3M, 3L6A, 4IUL, 9JJ7 | pLDDT=71.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EIF4G2 — Eukaryotic translation initiation factor 4 gamma 2，研究基础较多，新颖性有限。
2. 蛋白大小907 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 110 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P78344
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110321-EIF4G2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF4G2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P78344
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
