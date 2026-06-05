---
type: protein-evaluation
gene: "REL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## REL — REJECTED (研究热度过高 (PubMed strict=3023，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | REL |
| 蛋白名称 | Proto-oncogene c-Rel |
| 蛋白大小 | 619 aa / 68.5 kDa |
| UniProt ID | Q04864 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 619 aa / 68.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=3023 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013783, IPR014756, IPR002909, IPR033926, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- NF-kappaB complex (GO:0071159)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3023 |
| PubMed broad count | 6447 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Distinctions between c-Rel and other NF-kappaB proteins in immunity and disease.. *BioEssays : news and reviews in molecular, cellular and developmental biology*. PMID: 12879447
2. c-Rel and its many roles in cancer: an old story with new twists.. *British journal of cancer*. PMID: 26757421
3. The Unsolved Puzzle of c-Rel in B Cell Lymphoma.. *Cancers*. PMID: 31277480
4. Stringent Response in Mycobacteria: From Biology to Therapeutic Potential.. *Pathogens (Basel, Switzerland)*. PMID: 34832573
5. Molecular characterization and functional analysis of a mollusk Rel homologous gene.. *Fish & shellfish immunology*. PMID: 37890738

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.3 |
| 高置信度残基 (pLDDT>90) 占比 | 40.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 49.8% |
| 有序区域 (pLDDT>70) 占比 | 48.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.3），有序残基占 48.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013783, IPR014756, IPR002909, IPR033926, IPR000451; Pfam: PF16179, PF00554 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NFKBIA | 0.999 | 0.908 | — |
| NFKBIE | 0.999 | 0.898 | — |
| NFKBIB | 0.999 | 0.887 | — |
| NFKB2 | 0.999 | 0.933 | — |
| RELA | 0.999 | 0.910 | — |
| NFKB1 | 0.999 | 0.902 | — |
| RELB | 0.998 | 0.847 | — |
| CD40 | 0.992 | 0.000 | — |
| CHUK | 0.967 | 0.098 | — |
| TBK1 | 0.957 | 0.334 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000295025.7 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| A4V2K3 | psi-mi:"MI:0397"(two hybrid array) | doi:10.1016/j.celrep.2019.03.0 |
| RELA | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:8246997 |
| NFKB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RELB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| dl | psi-mi:"MI:0018"(two hybrid) | pubmed:9367441 |
| Dif | psi-mi:"MI:0045"(experimental interaction detectio | pubmed:unassigned4 |
| Nfatc2 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:20064450|imex:IM-24461 |
| TNIP2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.3 + PDB: 无 | pLDDT=65.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. REL — Proto-oncogene c-Rel，研究基础较多，新颖性有限。
2. 蛋白大小619 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3023 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 3023 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q04864
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162924-REL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=REL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q04864
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q04864-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
