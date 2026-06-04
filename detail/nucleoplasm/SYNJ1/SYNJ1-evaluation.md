---
type: protein-evaluation
gene: "SYNJ1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SYNJ1 — REJECTED (研究热度过高 (PubMed strict=123，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SYNJ1 / KIAA0910 |
| 蛋白名称 | Synaptojanin-1 |
| 蛋白大小 | 1573 aa / 173.1 kDa |
| UniProt ID | O43426 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Centrosome; UniProt: Cytoplasm, perinuclear region |
| 蛋白大小 | 5/10 | ×1 | 5 | 1573 aa / 173.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=123 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.1; PDB: 1W80, 2DNR, 2VJ0, 7A0V, 7A17 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036691, IPR046985, IPR000300, IPR012677, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Centrosome | Approved |
| UniProt | Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- clathrin coat of coated pit (GO:0030132)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- membrane coat (GO:0030117)
- perinuclear region of cytoplasm (GO:0048471)
- presynapse (GO:0098793)
- synaptic membrane (GO:0097060)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 123 |
| PubMed broad count | 180 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0910 |

**关键文献**:
1. Monogenic Parkinson's Disease: Genotype, Phenotype, Pathophysiology, and Genetic Testing.. *Genes*. PMID: 35328025
2. Monogenic Parkinson Disease Overview.. **. PMID: 20301402
3. 'Atypical' Parkinson's disease - genetic.. *International review of neurobiology*. PMID: 31779813
4. Synaptojanin1 Modifies Endolysosomal Parameters in Cultured Ventral Midbrain Neurons.. *eNeuro*. PMID: 37072173
5. SYNJ1 rescues motor functions in hereditary and sporadic Parkinson's disease mice by upregulating TSP-1 expression.. *Behavioural brain research*. PMID: 37419331

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.1 |
| 高置信度残基 (pLDDT>90) 占比 | 32.4% |
| 置信残基 (pLDDT 70-90) 占比 | 21.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.0% |
| 低置信 (pLDDT<50) 占比 | 36.0% |
| 有序区域 (pLDDT>70) 占比 | 54.0% |
| 可用 PDB 条目 | 1W80, 2DNR, 2VJ0, 7A0V, 7A17 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.1），有序残基占 54.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036691, IPR046985, IPR000300, IPR012677, IPR035979; Pfam: PF08952, PF22669, PF02383 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SH3GL2 | 0.998 | 0.731 | — |
| AMPH | 0.997 | 0.456 | — |
| BIN1 | 0.994 | 0.099 | — |
| SH3GL1 | 0.969 | 0.418 | — |
| ITSN1 | 0.961 | 0.475 | — |
| INPP4A | 0.953 | 0.000 | — |
| SNX9 | 0.951 | 0.755 | — |
| PIP5K1C | 0.951 | 0.068 | — |
| GRB2 | 0.950 | 0.490 | — |
| SH3GL3 | 0.949 | 0.313 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15417|pubmed:21706016 |
| Q81KB5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| gpmI | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Ywhaz | psi-mi:"MI:0028"(cosedimentation in solution) | imex:IM-11648|pubmed:19562802 |
| Atp6v1a | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:22707207|imex:IM-17710 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| Syngap1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| SNX9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AP2M1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLEKHA7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-25739|pubmed:28877994 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.1 + PDB: 1W80, 2DNR, 2VJ0, 7A0V, 7A17 | pLDDT=67.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region / Nucleoplasm, Cytosol; 额外: Centrosome | 一致 |
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
1. SYNJ1 — Synaptojanin-1，研究基础较多，新颖性有限。
2. 蛋白大小1573 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 123 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 123 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43426
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159082-SYNJ1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYNJ1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43426
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
