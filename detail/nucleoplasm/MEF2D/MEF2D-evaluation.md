---
type: protein-evaluation
gene: "MEF2D"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MEF2D — REJECTED (研究热度过高 (PubMed strict=368，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MEF2D |
| 蛋白名称 | Myocyte-specific enhancer factor 2D |
| 蛋白大小 | 521 aa / 55.9 kDa |
| UniProt ID | Q14814 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 521 aa / 55.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=368 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.8; PDB: 7X1N, 8C84 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR022102, IPR033896, IPR002100, IPR036879; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 368 |
| PubMed broad count | 568 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Emerging molecular subtypes and therapies in acute lymphoblastic leukemia.. *Seminars in diagnostic pathology*. PMID: 37120350
2. Genomic analyses identify recurrent MEF2D fusions in acute lymphoblastic leukaemia.. *Nature communications*. PMID: 27824051
3. Genomic Profiling of Adult and Pediatric B-cell Acute Lymphoblastic Leukemia.. *EBioMedicine*. PMID: 27428428
4. Whole-transcriptome analysis in acute lymphoblastic leukemia: a report from the DFCI ALL Consortium Protocol 16-001.. *Blood advances*. PMID: 34933343
5. Molecular classification improves risk assessment in adult BCR-ABL1-negative B-ALL.. *Blood*. PMID: 33895809

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.8 |
| 高置信度残基 (pLDDT>90) 占比 | 16.5% |
| 置信残基 (pLDDT 70-90) 占比 | 2.5% |
| 中等置信 (pLDDT 50-70) 占比 | 13.6% |
| 低置信 (pLDDT<50) 占比 | 67.4% |
| 有序区域 (pLDDT>70) 占比 | 19.0% |
| 可用 PDB 条目 | 7X1N, 8C84 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=53.8），有序残基占 19.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022102, IPR033896, IPR002100, IPR036879; Pfam: PF12347, PF00319 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MEF2A | 0.991 | 0.823 | — |
| MEF2B | 0.979 | 0.661 | — |
| HDAC4 | 0.963 | 0.783 | — |
| NFATC2 | 0.952 | 0.292 | — |
| CABIN1 | 0.940 | 0.625 | — |
| HDAC5 | 0.936 | 0.596 | — |
| NFATC1 | 0.933 | 0.000 | — |
| NFATC3 | 0.926 | 0.000 | — |
| MYOG | 0.926 | 0.049 | — |
| EP300 | 0.923 | 0.525 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Hdac5 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Hdac9 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| ENSP00000517292.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| MAPK14 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| COPS5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| rnfC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| MEF2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PKM | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-22313|pubmed:24606918 |
| EBI-9351778 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-22313|pubmed:24606918 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.8 + PDB: 7X1N, 8C84 | pLDDT=53.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MEF2D — Myocyte-specific enhancer factor 2D，研究基础较多，新颖性有限。
2. 蛋白大小521 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 368 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=53.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 368 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14814
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116604-MEF2D/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEF2D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14814
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
