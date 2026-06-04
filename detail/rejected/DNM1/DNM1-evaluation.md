---
type: protein-evaluation
gene: "DNM1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNM1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=307，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNM1 |
| 蛋白名称 | Dynamin-1 |
| 蛋白大小 | 867 aa / 97.6 kDa |
| UniProt ID | A0A994J7J4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Cytoplasmic vesicle, secretory vesicle, chrom |
| 蛋白大小 | 8/10 | ×1 | 8 | 867 aa / 97.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=307 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.6; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **59.0/180** | |
| **归一化总分** | | | **32.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cell membrane; Cytoplasmic vesicle, secretory vesicle, chromaffin granule; Membrane, clathrin-coated... | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 307 |
| PubMed broad count | 329 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Proteomic Study on the Amelioration of Cognitive Impairments in 3×Tg-AD Mice by Treadmill Exercise.. *J Proteome Res*. PMID: 42200610
2. Modulation of oxidative stress mediates kaempferol induced enhancement of bovine oocyte In Vitro maturation developmental efficiency.. *Anim Reprod Sci*. PMID: 42202568
3. Dapagliflozin Protects Cardiomyocytes against Doxorubicin-Induced Toxicity by Modulating Sirtuin 1/Sirtuin 3 and Ferroptosis Pathway.. *ACS Pharmacol Transl Sci*. PMID: 42130718
4. Modeling Synaptic Maturation From Growth Cone to Synapse in Human Organoids.. *J Neurochem*. PMID: 42108706
5. Bosentan confers cardioprotection against cisplatin toxicity: Involvement of β-arrestin-linked ET(A) receptor signaling.. *Biochem Pharmacol*. PMID: 42069228

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.6 |
| 高置信度残基 (pLDDT>90) 占比 | 27.2% |
| 置信残基 (pLDDT 70-90) 占比 | 44.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.4% |
| 低置信 (pLDDT<50) 占比 | 17.6% |
| 有序区域 (pLDDT>70) 占比 | 72.0% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=75.6，有序区 72.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNM3 | 0.000 | 0.000 | — |
| FIS1 | 0.000 | 0.000 | — |
| AMPH | 0.000 | 0.000 | — |
| BIN1 | 0.000 | 0.000 | — |
| DNM2 | 0.000 | 0.000 | — |
| ITSN1 | 0.000 | 0.000 | — |
| HCLS1 | 0.000 | 0.000 | — |
| GRB2 | 0.000 | 0.000 | — |
| SNX9 | 0.000 | 0.000 | — |
| SH3GL2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P39053 | psi-mi:"MI:0028"(cosedimentation in solution) | pubmed:- |
| uniprotkb:Q05193 | psi-mi:"MI:0040"(electron microscopy) | pubmed:- |
| uniprotkb:P54861 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P04147 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P10664 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P49626 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P38262 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P10592 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P11484 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P02994 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.6 + PDB: 无 | pLDDT=75.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cytoplasmic vesicle, secretory vesi / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DNM1 — Dynamin-1，研究基础较多，新颖性有限。
2. 蛋白大小867 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 307 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A994J7J4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106976-DNM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A994J7J4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
