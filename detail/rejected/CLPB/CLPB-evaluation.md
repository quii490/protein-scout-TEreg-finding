---
type: protein-evaluation
gene: "CLPB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLPB — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=594，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLPB / SKD3 |
| 蛋白名称 | Mitochondrial disaggregase |
| 蛋白大小 | 707 aa / 78.7 kDa |
| UniProt ID | Q9H078 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Mitochondrion intermembrane space |
| 蛋白大小 | 10/10 | ×1 | 10 | 707 aa / 78.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=594 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=71.8; PDB: 7TTR, 7TTS, 7US2, 7XBK, 7XC5, 8DEH, 8FDS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003593, IPR002110, IPR036770, IPR003959, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **74.0/180** | |
| **归一化总分** | | | **41.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Mitochondrion intermembrane space | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- mitochondrial intermembrane space (GO:0005758)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 594 |
| PubMed broad count | 768 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SKD3 |

**关键文献**:
1. Targeting Mitochondrial Structure Sensitizes Acute Myeloid Leukemia to Venetoclax Treatment.. *Cancer discovery*. PMID: 31048321
2. ATP-Dependent Dynamic Protein Aggregation Regulates Bacterial Dormancy Depth Critical for Antibiotic Tolerance.. *Molecular cell*. PMID: 30472191
3. New perspective in diagnostics of mitochondrial disorders: two years' experience with whole-exome sequencing at a national paediatric centre.. *Journal of translational medicine*. PMID: 27290639
4. CLPB disaggregase dysfunction impacts the functional integrity of the proteolytic SPY complex.. *The Journal of cell biology*. PMID: 38270563
5. Mitochondrial Protein Homeostasis and Cardiomyopathy.. *International journal of molecular sciences*. PMID: 35328774

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.8 |
| 高置信度残基 (pLDDT>90) 占比 | 25.6% |
| 置信残基 (pLDDT 70-90) 占比 | 39.6% |
| 中等置信 (pLDDT 50-70) 占比 | 9.2% |
| 低置信 (pLDDT<50) 占比 | 25.6% |
| 有序区域 (pLDDT>70) 占比 | 65.2% |
| 可用 PDB 条目 | 7TTR, 7TTS, 7US2, 7XBK, 7XC5, 8DEH, 8FDS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7TTR, 7TTS, 7US2, 7XBK, 7XC5, 8DEH, 8FDS）+ AlphaFold极高置信度预测（pLDDT=71.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003593, IPR002110, IPR036770, IPR003959, IPR019489; Pfam: PF07724, PF12796, PF10431 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLPP | 0.999 | 0.943 | — |
| GRPEL1 | 0.993 | 0.102 | — |
| CLPX | 0.971 | 0.094 | — |
| HSPE1 | 0.967 | 0.074 | — |
| HSPA4 | 0.941 | 0.402 | — |
| HSPD1 | 0.931 | 0.095 | — |
| DNAJB1 | 0.927 | 0.155 | — |
| GRPEL2 | 0.910 | 0.102 | — |
| HSP90AA1 | 0.874 | 0.100 | — |
| HSP90AB1 | 0.873 | 0.100 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A0A7H2C767 | psi-mi:"MI:0276"(blue native page) | pubmed:16858726|imex:IM-18898 |
| mreB | psi-mi:"MI:0096"(pull down) | pubmed:15690043|mint:MINT-5217 |
| hscB | psi-mi:"MI:0096"(pull down) | pubmed:15690043|mint:MINT-5217 |
| lysU | psi-mi:"MI:0096"(pull down) | pubmed:15690043|mint:MINT-5217 |
| rlmN | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15690043|mint:MINT-5217 |
| ydeP | psi-mi:"MI:0096"(pull down) | pubmed:15690043|mint:MINT-5217 |
| ccmB | psi-mi:"MI:0096"(pull down) | pubmed:15690043|mint:MINT-5217 |
| rbn | psi-mi:"MI:0096"(pull down) | pubmed:15690043|mint:MINT-5217 |
| glcB | psi-mi:"MI:0096"(pull down) | pubmed:15690043|mint:MINT-5217 |
| lasT | psi-mi:"MI:0096"(pull down) | pubmed:15690043|mint:MINT-5217 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.8 + PDB: 7TTR, 7TTS, 7US2, 7XBK, 7XC5,  | pLDDT=71.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion intermembrane space / 暂无HPA定位数据 | 一致 |
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
1. CLPB — Mitochondrial disaggregase，研究基础较多，新颖性有限。
2. 蛋白大小707 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 594 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H078
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162129-CLPB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLPB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H078
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H078-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
