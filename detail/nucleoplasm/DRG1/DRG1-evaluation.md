---
type: protein-evaluation
gene: "DRG1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DRG1 — REJECTED (研究热度过高 (PubMed strict=106，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DRG1 / NDRG1 |
| 蛋白名称 | Protein NDRG1 |
| 蛋白大小 | 394 aa / 42.8 kDa |
| UniProt ID | Q92597 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; 额外: Cytosol; UniProt: Cytoplasm, cytosol; Cytoplasm, cytoskeleton, microtubule org |
| 蛋白大小 | 10/10 | ×1 | 10 | 394 aa / 42.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=106 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.0; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Cytosol | Supported |
| UniProt | Cytoplasm, cytosol; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Nucleus; Cel... | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 106 |
| PubMed broad count | 149 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Ambient NO(2) induces premature pulmonary senescence in rats: The role of the ROS-DRG1/CDK5 axis.. *J Environ Sci (China)*. PMID: 42070819
2. [Localization and distribution pattern in trigeminal ganglia for the acupoints of governor vessel on the head and face based on neurotracing].. *Zhongguo Zhen Jiu*. PMID: 42116785
3. Molecular role of developmentally regulated GTP-binding protein 1 in coordinating osteoclast and osteoblast differentiation during bone remodeling.. *Mol Cells*. PMID: 41786215
4. Cell-type-resolved transcriptomic landscape of human focal cortical dysplasia.. *Proc Natl Acad Sci U S A*. PMID: 42012959
5. Cryo-EM structure of the AAA+ SPATA5 complex and its role in human cytoplasmic pre-60S maturation.. *Nat Commun*. PMID: 40268917

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.0 |
| 高置信度残基 (pLDDT>90) 占比 | 57.6% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 5.8% |
| 低置信 (pLDDT<50) 占比 | 25.1% |
| 有序区域 (pLDDT>70) 占比 | 69.0% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=78.0，有序区 69.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZC3H15 | 0.000 | 0.000 | — |
| RWDD1 | 0.000 | 0.000 | — |
| RPL23A | 0.000 | 0.000 | — |
| MRPS7 | 0.000 | 0.000 | — |
| RPL8 | 0.000 | 0.000 | — |
| RPLP0 | 0.000 | 0.000 | — |
| PSMC2 | 0.000 | 0.000 | — |
| POLE2 | 0.000 | 0.000 | — |
| TSN | 0.000 | 0.000 | — |
| CS | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9H446 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P04632 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9Y295 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q5I0F0 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P78362 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:- |
| uniprotkb:Q15345-3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8WU90 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8WVF1-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9BV86 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q6FHY5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.0 + PDB: 无 | pLDDT=78.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Cytoplasm, cytoskeleton, micro / Nucleoplasm, Nuclear bodies; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DRG1 — Protein NDRG1，研究基础较多，新颖性有限。
2. 蛋白大小394 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 106 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 106 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92597
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185721-DRG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DRG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92597
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
