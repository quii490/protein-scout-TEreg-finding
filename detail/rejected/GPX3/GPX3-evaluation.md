---
type: protein-evaluation
gene: "GPX3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPX3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=675，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPX3 / GPXP |
| 蛋白名称 | Glutathione peroxidase 3 |
| 蛋白大小 | 226 aa / 25.6 kDa |
| UniProt ID | P22352 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Secreted |
| 蛋白大小 | 10/10 | ×1 | 10 | 226 aa / 25.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=675 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 2R37 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000889, IPR029759, IPR029760, IPR036249; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **54.0/180** | |
| **归一化总分** | | | **30.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Secreted | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- extracellular space (GO:0005615)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 675 |
| PubMed broad count | 1152 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GPXP |

**关键文献**:
1. Glutathione peroxidases.. *Biochimica et biophysica acta*. PMID: 23201771
2. Proteomic landscape of the extracellular matrix in the fibrotic kidney.. *Kidney international*. PMID: 36805449
3. Oxidatively stressed extracellular microenvironment drives fibroblast activation and kidney fibrosis.. *Redox biology*. PMID: 37690165
4. GPX3 supports ovarian cancer tumor progression in vivo and promotes expression of GDF15.. *Gynecologic oncology*. PMID: 38342006
5. GPX3 promotes cisplatin resistance in TNBC by manipulating ROS-TGFB1-ZEB2.. *Cell communication and signaling : CCS*. PMID: 40713734

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 2R37 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000889, IPR029759, IPR029760, IPR036249; Pfam: PF00255 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GSR | 0.996 | 0.056 | — |
| PRDX6 | 0.967 | 0.113 | — |
| PPARGC1A | 0.958 | 0.000 | — |
| GSS | 0.945 | 0.000 | — |
| ALOX5 | 0.940 | 0.093 | — |
| GPX4 | 0.936 | 0.000 | — |
| ALOX15 | 0.933 | 0.045 | — |
| GPX8 | 0.929 | 0.000 | — |
| GPX7 | 0.927 | 0.000 | — |
| TXN | 0.925 | 0.126 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| THG1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| HYR1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| ftsY | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| livM2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| fadH | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0H2W7Y4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| trmFO | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000373477.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| UBQLN1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| LDAF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:27107014|imex:IM-24995 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 2R37 | pLDDT=0, v? | 预测+实验 |
| 定位 | UniProt + HPA | Secreted / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

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
1. GPX3 — Glutathione peroxidase 3，研究基础较多，新颖性有限。
2. 蛋白大小226 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 675 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P22352
- Protein Atlas: https://www.proteinatlas.org/ENSG00000211445-GPX3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPX3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P22352
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
