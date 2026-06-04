---
type: protein-evaluation
gene: "HES5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HES5 — REJECTED (研究热度过高 (PubMed strict=352，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HES5 / BHLHB38 |
| 蛋白名称 | Transcription factor HES-5 |
| 蛋白大小 | 166 aa / 18.2 kDa |
| UniProt ID | Q5TA89 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nuclear speckles, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 166 aa / 18.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=352 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050370, IPR036638, IPR003650; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear speckles, Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 352 |
| PubMed broad count | 652 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHB38 |

**关键文献**:
1. Fluoxetine shows neuroprotective effects against LPS-induced neuroinflammation via the Notch signaling pathway.. *International immunopharmacology*. PMID: 36461606
2. NOTCH target gene HES5 mediates oncogenic and tumor suppressive functions in hepatocarcinogenesis.. *Oncogene*. PMID: 32055024
3. Control of hair cell development by molecular pathways involving Atoh1, Hes1 and Hes5.. *Gene*. PMID: 25550047
4. PCSK9 Loss-of-Function Disrupts Cellular Microfilament Network via LIN28A/HES5/JMY Axis in Neural Tube Defects.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40788992
5. ZFP423 coordinates Notch and bone morphogenetic protein signaling, selectively up-regulating Hes5 gene expression.. *The Journal of biological chemistry*. PMID: 20547764

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.7 |
| 高置信度残基 (pLDDT>90) 占比 | 33.1% |
| 置信残基 (pLDDT 70-90) 占比 | 24.7% |
| 中等置信 (pLDDT 50-70) 占比 | 20.5% |
| 低置信 (pLDDT<50) 占比 | 21.7% |
| 有序区域 (pLDDT>70) 占比 | 57.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=72.7，有序区 57.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050370, IPR036638, IPR003650; Pfam: PF07527, PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOTCH1 | 0.934 | 0.000 | — |
| NOTCH3 | 0.930 | 0.000 | — |
| HES1 | 0.920 | 0.071 | — |
| NOTCH2 | 0.892 | 0.000 | — |
| DLL1 | 0.859 | 0.000 | — |
| RBPJ | 0.857 | 0.000 | — |
| JAG1 | 0.837 | 0.000 | — |
| STAT3 | 0.799 | 0.292 | — |
| NOTCH4 | 0.797 | 0.000 | — |
| MAML1 | 0.795 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| SIRT1 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:25490446|imex:IM-24165 |
| H1-4 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:25490446|imex:IM-24165 |
| H4C16 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:25490446|imex:IM-24165 |
| EBI-26482811 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| EBI-26487840 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| TNFSF14 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| EBI-36946204 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:34733326|imex:IM-29675 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.7 + PDB: 无 | pLDDT=72.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear speckles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HES5 — Transcription factor HES-5，研究基础较多，新颖性有限。
2. 蛋白大小166 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 352 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 352 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5TA89
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197921-HES5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HES5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5TA89
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
