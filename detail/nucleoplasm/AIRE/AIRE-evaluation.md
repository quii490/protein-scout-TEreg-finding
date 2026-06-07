---
type: protein-evaluation
gene: "AIRE"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AIRE — REJECTED (研究热度过高 (PubMed strict=906，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AIRE / APECED |
| 蛋白名称 | Autoimmune regulator |
| 蛋白大小 | 545 aa / 57.7 kDa |
| UniProt ID | O43918 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 545 aa / 57.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=906 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.2; PDB: 1XWH, 2KE1, 2KFT, 2LRI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008087, IPR042580, IPR004865, IPR010919, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- female germ cell nucleus (GO:0001674)
- male germ cell nucleus (GO:0001673)
- nuclear body (GO:0016604)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 906 |
| PubMed broad count | 2682 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: APECED |

**关键文献**:
1. Autoinmune polyendocrinopathy.. *Medicina clinica*. PMID: 33958142
2. Autoimmune polyendocrine syndrome type 1: Clinical manifestations, pathogenetic features, and management approach.. *Autoimmunity reviews*. PMID: 35690244
3. Autoimmune Polyendocrinopathy-Candidiasis-Ectodermal Dystrophy.. *Frontiers in pediatrics*. PMID: 34790633
4. Projection of an immunological self shadow within the thymus by the aire protein.. *Science (New York, N.Y.)*. PMID: 12376594
5. Where AIRE we now? Where AIRE we going?. *Current opinion in allergy and clinical immunology*. PMID: 39440452

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.2 |
| 高置信度残基 (pLDDT>90) 占比 | 22.2% |
| 置信残基 (pLDDT 70-90) 占比 | 14.3% |
| 中等置信 (pLDDT 50-70) 占比 | 13.8% |
| 低置信 (pLDDT<50) 占比 | 49.7% |
| 有序区域 (pLDDT>70) 占比 | 36.5% |
| 可用 PDB 条目 | 1XWH, 2KE1, 2KFT, 2LRI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.2），有序残基占 36.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008087, IPR042580, IPR004865, IPR010919, IPR000770; Pfam: PF03172, PF00628, PF01342 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| H3C12 | 0.989 | 0.945 | — |
| H3-4 | 0.987 | 0.934 | — |
| H3C13 | 0.983 | 0.911 | — |
| H3-2 | 0.983 | 0.911 | — |
| H3-3B | 0.983 | 0.911 | — |
| H3-5 | 0.983 | 0.911 | — |
| H3C1 | 0.955 | 0.952 | — |
| H3C7 | 0.916 | 0.911 | — |
| H3C3 | 0.915 | 0.911 | — |
| H3-3A | 0.915 | 0.911 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.2 + PDB: 1XWH, 2KE1, 2KFT, 2LRI | pLDDT=61.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. AIRE — Autoimmune regulator，研究基础较多，新颖性有限。
2. 蛋白大小545 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 906 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 906 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43918
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160224-AIRE/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AIRE
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43918
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43918-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43918 |
| SMART | SM00249;SM00258; |
| UniProt Domain [FT] | DOMAIN 1..105; /note="HSR"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00747"; DOMAIN 181..280; /note="SAND"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00185" |
| InterPro | IPR008087;IPR042580;IPR004865;IPR010919;IPR000770;IPR043563;IPR019786;IPR011011;IPR001965;IPR019787;IPR013083; |
| Pfam | PF03172;PF00628;PF01342; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000160224-AIRE/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DAXX | Intact, Biogrid | true |
| H3C1 | Intact, Biogrid | true |
| PRKDC | Intact, Biogrid | true |
| CREBBP | Biogrid | false |
| DDX5 | Biogrid | false |
| FBXO3 | Biogrid | false |
| H3C10 | Intact | false |
| H3C11 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
