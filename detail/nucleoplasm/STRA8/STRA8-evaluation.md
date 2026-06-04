---
type: protein-evaluation
gene: "STRA8"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STRA8 — REJECTED (研究热度过高 (PubMed strict=391，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STRA8 |
| 蛋白名称 | Stimulated by retinoic acid gene 8 protein homolog |
| 蛋白大小 | 330 aa / 36.9 kDa |
| UniProt ID | Q7Z7C7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 330 aa / 36.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=391 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR057021, IPR036638, IPR033537; Pfam: PF23175 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 391 |
| PubMed broad count | 601 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mechanisms of meiosis initiation and meiotic prophase progression during spermatogenesis.. *Molecular aspects of medicine*. PMID: 38797021
2. Histone demethylase KDM2A recruits HCFC1 and E2F1 to orchestrate male germ cell meiotic entry and progression.. *The EMBO journal*. PMID: 39160277
3. Mettl3-/Mettl14-mediated mRNA N(6)-methyladenosine modulates murine spermatogenesis.. *Cell research*. PMID: 28914256
4. MEIOSIN Directs the Switch from Mitosis to Meiosis in Mammalian Germ Cells.. *Developmental cell*. PMID: 32032549
5. The retrotransposon-derived capsid genes PNMA1 and PNMA4 maintain reproductive capacity.. *Nature aging*. PMID: 40263616

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.2 |
| 高置信度残基 (pLDDT>90) 占比 | 2.4% |
| 置信残基 (pLDDT 70-90) 占比 | 41.2% |
| 中等置信 (pLDDT 50-70) 占比 | 24.2% |
| 低置信 (pLDDT<50) 占比 | 32.1% |
| 有序区域 (pLDDT>70) 占比 | 43.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=63.2），有序残基占 43.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR057021, IPR036638, IPR033537; Pfam: PF23175 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NANOS2 | 0.959 | 0.000 | — |
| CYP26B1 | 0.934 | 0.000 | — |
| DAZL | 0.851 | 0.000 | — |
| SYCP3 | 0.847 | 0.000 | — |
| TAF4B | 0.830 | 0.000 | — |
| CYP26C1 | 0.823 | 0.000 | — |
| ZBTB16 | 0.813 | 0.000 | — |
| CYP26A1 | 0.796 | 0.000 | — |
| REC8 | 0.792 | 0.000 | — |
| BHMG1 | 0.786 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| POU6F2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SERTAD2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CTDSP1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ANKRD11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZMYND12 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TFIP11 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MEOX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CTAG1A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NME2P1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.2 + PDB: 无 | pLDDT=63.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. STRA8 — Stimulated by retinoic acid gene 8 protein homolog，研究基础较多，新颖性有限。
2. 蛋白大小330 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 391 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 391 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z7C7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146857-STRA8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STRA8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z7C7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
