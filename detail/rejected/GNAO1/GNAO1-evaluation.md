---
type: protein-evaluation
gene: "GNAO1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNAO1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=167，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNAO1 |
| 蛋白名称 | Guanine nucleotide-binding protein G(o) subunit alpha |
| 蛋白大小 | 354 aa / 40.1 kDa |
| UniProt ID | P09471 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 354 aa / 40.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=167 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.5; PDB: 6FUF, 6G79, 6K41, 6OIK, 6WWZ, 7D76, 7D77 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001408, IPR001019, IPR011025, IPR027417; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell body (GO:0044297)
- cytoplasm (GO:0005737)
- dendrite (GO:0030425)
- GABA-ergic synapse (GO:0098982)
- glutamatergic synapse (GO:0098978)
- heterotrimeric G-protein complex (GO:0005834)
- parallel fiber to Purkinje cell synapse (GO:0098688)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 167 |
| PubMed broad count | 274 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. GNAO1-Related Disorder.. **. PMID: 37956232
2. The expanding field of genetic developmental and epileptic encephalopathies: current understanding and future perspectives.. *The Lancet. Child & adolescent health*. PMID: 39419567
3. A mechanistic review on GNAO1-associated movement disorder.. *Neurobiology of disease*. PMID: 29758257
4. Molecular and clinical spectrum of epilepsy-dyskinesia syndromes: a cross-sectional study of 609 patients.. *Brain : a journal of neurology*. PMID: 40811633
5. Phenotypic Diversity in GNAO1 Patients: A Comprehensive Overview of Variants and Phenotypes.. *Human mutation*. PMID: 40225165

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.5 |
| 高置信度残基 (pLDDT>90) 占比 | 87.0% |
| 置信残基 (pLDDT 70-90) 占比 | 11.0% |
| 中等置信 (pLDDT 50-70) 占比 | 1.4% |
| 低置信 (pLDDT<50) 占比 | 0.6% |
| 有序区域 (pLDDT>70) 占比 | 98.0% |
| 可用 PDB 条目 | 6FUF, 6G79, 6K41, 6OIK, 6WWZ, 7D76, 7D77, 7EJ0, 7EJ8, 7EJA |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6FUF, 6G79, 6K41, 6OIK, 6WWZ, 7D76, 7D77, 7EJ0, 7EJ8, 7EJA）+ AlphaFold极高置信度预测（pLDDT=94.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001408, IPR001019, IPR011025, IPR027417; Pfam: PF00503 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNB1 | 0.996 | 0.968 | — |
| RGS16 | 0.993 | 0.841 | — |
| RGS4 | 0.989 | 0.638 | — |
| RGS7 | 0.981 | 0.295 | — |
| GNG2 | 0.980 | 0.897 | — |
| ADRA2A | 0.956 | 0.935 | — |
| DRD2 | 0.950 | 0.442 | — |
| GNB4 | 0.947 | 0.478 | — |
| RIC8A | 0.946 | 0.758 | — |
| GNB5 | 0.935 | 0.323 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DCTN2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Ywhaz | psi-mi:"MI:0028"(cosedimentation in solution) | imex:IM-11648|pubmed:19562802 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| SNCA | psi-mi:"MI:0096"(pull down) | pubmed:18614564|imex:IM-19211 |
| Haus4 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| 616370" | psi-mi:"MI:0096"(pull down) | pubmed:23606334|imex:IM-21247 |
| Cnksr2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| Syngap1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| GNAI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KIFAP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.5 + PDB: 6FUF, 6G79, 6K41, 6OIK, 6WWZ,  | pLDDT=94.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Membrane / 暂无HPA定位数据 | 一致 |
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
1. GNAO1 — Guanine nucleotide-binding protein G(o) subunit alpha，研究基础较多，新颖性有限。
2. 蛋白大小354 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 167 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P09471
- Protein Atlas: https://www.proteinatlas.org/ENSG00000087258-GNAO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNAO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P09471
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P09471-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
