---
type: protein-evaluation
gene: "CMAS"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CMAS — REJECTED (研究热度过高 (PubMed strict=772，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CMAS |
| 蛋白名称 | N-acylneuraminate cytidylyltransferase |
| 蛋白大小 | 434 aa / 48.4 kDa |
| UniProt ID | Q8NFW8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Cytosol; 额外: Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 434 aa / 48.4 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=772 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=87.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.5/180** | |
| **归一化总分** | | | **46.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli | Uncertain |
| UniProt | Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 772 |
| PubMed broad count | 822 |
| 别名(未计入scoring) |  |

**关键文献**:
1. AQbD-assisted HPLC method for simultaneous determination of methylparaben and propylparaben in liquid oral dosage forms.. *Sci Rep*. PMID: 42215541
2. Assessing and strengthening community-based coastal governance.. *Conserv Biol*. PMID: 42178841
3. Clinical features, triggers, and risk factors of severe gastrointestinal involvement in anti-NXP2-positive juvenile dermatomyositis: a retrospective cohort study.. *Pediatr Rheumatol Online J*. PMID: 42174651
4. Economic evidence of alternative formulations and routes of administration for identical active pharmaceutical ingredient: a systematic review.. *Health Econ Rev*. PMID: 42159667
5. Chaperone-mediated autophagy protects against retinal photoreceptor degeneration by modulating proteostasis of glucose metabolism enzymes.. *Proc Natl Acad Sci U S A*. PMID: 42113991

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.8 |
| 高置信度残基 (pLDDT>90) 占比 | 71.7% |
| 置信残基 (pLDDT 70-90) 占比 | 17.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 8.3% |
| 有序区域 (pLDDT>70) 占比 | 89.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.8，有序区 89.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NANS | 0.000 | 0.000 | — |
| NANP | 0.000 | 0.000 | — |
| SLC35A1 | 0.000 | 0.000 | — |
| VPS29 | 0.000 | 0.000 | — |
| VPS35 | 0.000 | 0.000 | — |
| GNE | 0.000 | 0.000 | — |
| RNF10 | 0.000 | 0.000 | — |
| VPS26A | 0.000 | 0.000 | — |
| ST3GAL4 | 0.000 | 0.000 | — |
| NPL | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8NFW8 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P10809 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q16799-3 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q5M963 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q5S007 | psi-mi:"MI:0089"(protein array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.8 + PDB: 无 | pLDDT=87.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Cytosol; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CMAS -- N-acylneuraminate cytidylyltransferase，研究基础较多，新颖性有限。
2. 蛋白大小434 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 772 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 772 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NFW8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111726-CMAS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CMAS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NFW8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
