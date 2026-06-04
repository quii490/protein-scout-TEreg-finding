---
type: protein-evaluation
gene: "CHM"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CHM — REJECTED (研究热度过高 (PubMed strict=603，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHM / REP1, TCD |
| 蛋白名称 | Rab proteins geranylgeranyltransferase component A 1 |
| 蛋白大小 | 653 aa / 73.5 kDa |
| UniProt ID | P24386 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 653 aa / 73.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=603 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036188, IPR018203, IPR001738, IPR054420; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **85.5/180** | |
| **归一化总分** | | | **47.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- Rab-protein geranylgeranyltransferase complex (GO:0005968)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 603 |
| PubMed broad count | 4501 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: REP1, TCD |

**关键文献**:
1. Comprehensive Molecular Screening in Chinese Usher Syndrome Patients.. *Investigative ophthalmology & visual science*. PMID: 29625443
2. Impact of Next Generation Sequencing in Unraveling the Genetics of 1036 Spanish Families With Inherited Macular Dystrophies.. *Investigative ophthalmology & visual science*. PMID: 35119454
3. Choroideremia.. *Current opinion in ophthalmology*. PMID: 28520608
4. Choroideremia: The Endpoint Endgame.. *International journal of molecular sciences*. PMID: 37762657
5. Choroideremia: molecular mechanisms and therapies.. *Trends in molecular medicine*. PMID: 35341685

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.2 |
| 高置信度残基 (pLDDT>90) 占比 | 65.1% |
| 置信残基 (pLDDT 70-90) 占比 | 9.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 21.6% |
| 有序区域 (pLDDT>70) 占比 | 74.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=80.2，有序区 74.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036188, IPR018203, IPR001738, IPR054420; Pfam: PF00996, PF22603 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RABGGTA | 0.985 | 0.892 | — |
| RAB1A | 0.949 | 0.693 | — |
| RAB7A | 0.947 | 0.861 | — |
| RAB27A | 0.935 | 0.184 | — |
| RAB3A | 0.935 | 0.671 | — |
| RABGGTB | 0.923 | 0.403 | — |
| RAB1B | 0.911 | 0.779 | — |
| RAB5A | 0.878 | 0.666 | — |
| RAB5C | 0.861 | 0.689 | — |
| RAB8A | 0.847 | 0.362 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Zif | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ten-m | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| NetB | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Rab7a | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15186776 |
| MIOS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| PABIR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| POLA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SEH1L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| NUP98 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| TJP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.2 + PDB: 无 | pLDDT=80.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. CHM — Rab proteins geranylgeranyltransferase component A 1，研究基础较多，新颖性有限。
2. 蛋白大小653 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 603 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 603 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P24386
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188419-CHM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHM
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P24386
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
