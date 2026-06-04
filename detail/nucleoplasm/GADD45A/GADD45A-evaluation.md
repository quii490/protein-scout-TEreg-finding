---
type: protein-evaluation
gene: "GADD45A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GADD45A — REJECTED (研究热度过高 (PubMed strict=717，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GADD45A / DDIT1, GADD45 |
| 蛋白名称 | Growth arrest and DNA damage-inducible protein GADD45 alpha |
| 蛋白大小 | 165 aa / 18.3 kDa |
| UniProt ID | P24522 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 165 aa / 18.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=717 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=81.2; PDB: 2KG4 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR024824, IPR029064, IPR004038; Pfam: PF01248 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 717 |
| PubMed broad count | 1241 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DDIT1, GADD45 |

**关键文献**:
1. GADD45A: With or without you.. *Medicinal research reviews*. PMID: 38264852
2. Loss of the stress sensor GADD45A promotes stem cell activity and ferroptosis resistance in LGR4/HOXA9-dependent AML.. *Blood*. PMID: 38579286
3. Role of GADD45A in myocardial ischemia/reperfusion through mediation of the JNK/p38 MAPK and STAT3/VEGF pathways.. *International journal of molecular medicine*. PMID: 36331027
4. METTL1-mediated tRNA m(7)G methylation and translational dysfunction restricts breast cancer tumorigenesis by fueling cell cycle blockade.. *Journal of experimental & clinical cancer research : CR*. PMID: 38822363
5. Retraction.. *Journal of cellular physiology*. PMID: 34191308

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.2 |
| 高置信度残基 (pLDDT>90) 占比 | 47.3% |
| 置信残基 (pLDDT 70-90) 占比 | 30.9% |
| 中等置信 (pLDDT 50-70) 占比 | 13.3% |
| 低置信 (pLDDT<50) 占比 | 8.5% |
| 有序区域 (pLDDT>70) 占比 | 78.2% |
| 可用 PDB 条目 | 2KG4 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=81.2，有序区 78.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024824, IPR029064, IPR004038; Pfam: PF01248 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K4 | psi-mi:"MI:0111"(dihydrofolate reductase reconstru | pubmed:12052864 |
| MAP2K6 | psi-mi:"MI:0111"(dihydrofolate reductase reconstru | pubmed:12052864 |
| DCTN2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FTL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NUCB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |
| SH3GLB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |
| CDK11A | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| FAS | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PSMC3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| PTPRK | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.2 + PDB: 2KG4 | pLDDT=81.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GADD45A — Growth arrest and DNA damage-inducible protein GADD45 alpha，研究基础较多，新颖性有限。
2. 蛋白大小165 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 717 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 717 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P24522
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116717-GADD45A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GADD45A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P24522
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
