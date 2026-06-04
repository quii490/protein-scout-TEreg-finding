---
type: protein-evaluation
gene: "GSK3B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GSK3B — REJECTED (研究热度过高 (PubMed strict=703，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GSK3B |
| 蛋白名称 | Glycogen synthase kinase-3 beta |
| 蛋白大小 | 420 aa / 46.7 kDa |
| UniProt ID | P49841 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus; Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 420 aa / 46.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=703 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=88.2; PDB: 1GNG, 1H8F, 1I09, 1J1B, 1J1C, 1O6K, 1O6L |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050591, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Cytoplasm; Nucleus; Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- beta-catenin destruction complex (GO:0030877)
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- glutamatergic synapse (GO:0098978)
- mitochondrion (GO:0005739)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 703 |
| PubMed broad count | 5958 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Aloe Emodin Alleviates Radiation-Induced Heart Disease via Blocking P4HB Lactylation and Mitigating Kynurenine Metabolic Disruption.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39494721
2. TRAF6 inhibits colorectal cancer metastasis through regulating selective autophagic CTNNB1/β-catenin degradation and is targeted for GSK3B/GSK3β-mediated phosphorylation and degradation.. *Autophagy*. PMID: 30806153
3. Proteogenomic characterization unveils biomarkers associated with chemoresistance in muscle-invasive bladder cancer.. *Cell reports. Medicine*. PMID: 40749681
4. Transcriptional repression of autophagy and lysosome biogenesis.. *Autophagy*. PMID: 39936623
5. EPHB1 Protein Promoted the Progression of Prostate Adenocarcinoma Through Phosphorylating GSK3B and Activating EPHB1-GSK3B-SMAD3 Pathway.. *Human mutation*. PMID: 40548257

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.2 |
| 高置信度残基 (pLDDT>90) 占比 | 77.1% |
| 置信残基 (pLDDT 70-90) 占比 | 9.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.4% |
| 低置信 (pLDDT<50) 占比 | 12.1% |
| 有序区域 (pLDDT>70) 占比 | 86.4% |
| 可用 PDB 条目 | 1GNG, 1H8F, 1I09, 1J1B, 1J1C, 1O6K, 1O6L, 1O9U, 1PYX, 1Q3D |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1GNG, 1H8F, 1I09, 1J1B, 1J1C, 1O6K, 1O6L, 1O9U, 1PYX, 1Q3D）+ AlphaFold极高置信度预测（pLDDT=88.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050591, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSNK1A1 | 0.999 | 0.077 | — |
| APC | 0.999 | 0.863 | — |
| AXIN1 | 0.999 | 0.996 | — |
| MAPT | 0.999 | 0.942 | — |
| FRAT1 | 0.999 | 0.842 | — |
| BTRC | 0.999 | 0.971 | — |
| DVL1 | 0.999 | 0.093 | — |
| AXIN2 | 0.999 | 0.921 | — |
| CTNNB1 | 0.999 | 0.991 | — |
| MYC | 0.996 | 0.822 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UPF3A | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| AKT1 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-14541|pubmed:16282323 |
| GYS1 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-14541|pubmed:16282323 |
| AKT2 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:12434148 |
| NIN | psi-mi:"MI:0018"(two hybrid) | pubmed:11004522|imex:IM-19078 |
| Epm2a | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12037|pubmed:16959610 |
| SMYD2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ENSP00000264235.9 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HSD17B4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SNRNP70 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.2 + PDB: 1GNG, 1H8F, 1I09, 1J1B, 1J1C,  | pLDDT=88.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GSK3B — Glycogen synthase kinase-3 beta，研究基础较多，新颖性有限。
2. 蛋白大小420 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 703 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 703 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49841
- Protein Atlas: https://www.proteinatlas.org/ENSG00000082701-GSK3B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GSK3B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49841
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
