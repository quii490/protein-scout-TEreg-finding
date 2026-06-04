---
type: protein-evaluation
gene: "BMPR2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BMPR2 — REJECTED (研究热度过高 (PubMed strict=1015，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BMPR2 / PPH1 |
| 蛋白名称 | Bone morphogenetic protein receptor type-2 |
| 蛋白大小 | 1038 aa / 115.2 kDa |
| UniProt ID | Q13873 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane; UniProt: Cell membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 1038 aa / 115.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1015 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.4; PDB: 2HLQ, 3G2F, 6UNP, 7PPA, 7PPB, 7PPC, 7U5O |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000472, IPR011009, IPR000719, IPR017441, IPR045 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane | Supported |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- apical plasma membrane (GO:0016324)
- axon (GO:0030424)
- basal plasma membrane (GO:0009925)
- caveola (GO:0005901)
- cell surface (GO:0009986)
- clathrin-coated pit (GO:0005905)
- dendrite (GO:0030425)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1015 |
| PubMed broad count | 1532 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PPH1 |

**关键文献**:
1. BMPR2 Mutation and Metabolic Reprogramming in Pulmonary Arterial Hypertension.. *Circulation research*. PMID: 36603064
2. Dysregulated Smooth Muscle Cell BMPR2-ARRB2 Axis Causes Pulmonary Hypertension.. *Circulation research*. PMID: 36744494
3. Anti-remodeling therapies in pulmonary arterial hypertension.. *Trends in pharmacological sciences*. PMID: 40541519
4. Cathepsin L Promotes Pulmonary Hypertension via BMPR2/GSDME-Mediated Pyroptosis.. *Hypertension (Dallas, Tex. : 1979)*. PMID: 39403807
5. Regulation of the Methylation and Expression Levels of the BMPR2 Gene by SIN3a as a Novel Therapeutic Mechanism in Pulmonary Arterial Hypertension.. *Circulation*. PMID: 34078089

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.4 |
| 高置信度残基 (pLDDT>90) 占比 | 26.0% |
| 置信残基 (pLDDT 70-90) 占比 | 11.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.4% |
| 低置信 (pLDDT<50) 占比 | 57.0% |
| 有序区域 (pLDDT>70) 占比 | 37.6% |
| 可用 PDB 条目 | 2HLQ, 3G2F, 6UNP, 7PPA, 7PPB, 7PPC, 7U5O |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.4），有序残基占 37.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000472, IPR011009, IPR000719, IPR017441, IPR045860; Pfam: PF01064, PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BMP10 | 0.999 | 0.932 | — |
| BMP4 | 0.999 | 0.658 | — |
| BMP2 | 0.999 | 0.832 | — |
| BMPR1B | 0.999 | 0.510 | — |
| ACVR1 | 0.999 | 0.755 | — |
| BMPR1A | 0.999 | 0.510 | — |
| BMP7 | 0.999 | 0.553 | — |
| BMP6 | 0.999 | 0.354 | — |
| GDF2 | 0.999 | 0.553 | — |
| GDF9 | 0.998 | 0.354 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000363708.4 | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| Arrb1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| C4bpa | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| Hnrnpr | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| Nop56 | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| Ctbp1 | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| Arsa | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| Cryab | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| Oc90 | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| Sult1e1 | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.4 + PDB: 2HLQ, 3G2F, 6UNP, 7PPA, 7PPB,  | pLDDT=57.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BMPR2 — Bone morphogenetic protein receptor type-2，研究基础较多，新颖性有限。
2. 蛋白大小1038 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1015 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1015 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13873
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204217-BMPR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BMPR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13873
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
