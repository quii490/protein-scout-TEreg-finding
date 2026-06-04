---
type: protein-evaluation
gene: "GATA4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GATA4 — REJECTED (研究热度过高 (PubMed strict=2324，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GATA4 |
| 蛋白名称 | Transcription factor GATA-4 |
| 蛋白大小 | 442 aa / 44.6 kDa |
| UniProt ID | P43694 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear bodies; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 442 aa / 44.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2324 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.2; PDB: 2M9W, 8VG0, 8VG1 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008013, IPR016375, IPR039355, IPR000679, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2324 |
| PubMed broad count | 3671 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Endothelial GATA4 controls liver fibrosis and regeneration by preventing a pathogenic switch in angiocrine signaling.. *Journal of hepatology*. PMID: 32916216
2. Transcription factor protein interactomes reveal genetic determinants in heart disease.. *Cell*. PMID: 35182466
3. Structural insights into the cooperative nucleosome recognition and chromatin opening by FOXA1 and GATA4.. *Molecular cell*. PMID: 39121853
4. GATA4: orchestrating cardiac development and beyond.. *Cardiovascular research*. PMID: 41239560
5. Patient-specific iPSC-derived cardiomyocytes reveal abnormal regulation of FGF16 in a familial atrial septal defect.. *Cardiovascular research*. PMID: 33956078

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.2 |
| 高置信度残基 (pLDDT>90) 占比 | 18.3% |
| 置信残基 (pLDDT 70-90) 占比 | 4.5% |
| 中等置信 (pLDDT 50-70) 占比 | 20.4% |
| 低置信 (pLDDT<50) 占比 | 56.8% |
| 有序区域 (pLDDT>70) 占比 | 22.8% |
| 可用 PDB 条目 | 2M9W, 8VG0, 8VG1 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.2），有序残基占 22.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008013, IPR016375, IPR039355, IPR000679, IPR013088; Pfam: PF00320, PF05349 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NKX2-5 | 0.999 | 0.814 | — |
| ZFPM2 | 0.999 | 0.644 | — |
| TBX5 | 0.998 | 0.311 | — |
| TBX20 | 0.991 | 0.103 | — |
| SRF | 0.991 | 0.538 | — |
| HAND2 | 0.990 | 0.308 | — |
| NFATC4 | 0.984 | 0.000 | — |
| SOX9 | 0.977 | 0.053 | — |
| SMARCD3 | 0.975 | 0.095 | — |
| EP300 | 0.973 | 0.537 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Nkx2-5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12845333 |
| TBX5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12845333 |
| Jarid2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15542826 |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ARHGEF19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| KSR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27086506|imex:IM-25748 |
| ERF003 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| TCP8 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| MYB21 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| AGL42 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.2 + PDB: 2M9W, 8VG0, 8VG1 | pLDDT=57.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nuclear bodies | 一致 |
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
1. GATA4 — Transcription factor GATA-4，研究基础较多，新颖性有限。
2. 蛋白大小442 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2324 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2324 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P43694
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136574-GATA4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GATA4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P43694
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
