---
type: protein-evaluation
gene: "FOXA2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOXA2 — REJECTED (研究热度过高 (PubMed strict=924，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXA2 / HNF3B, TCF3B |
| 蛋白名称 | Hepatocyte nuclear factor 3-beta |
| 蛋白大小 | 457 aa / 48.3 kDa |
| UniProt ID | Q9Y261 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cell Junctions; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 457 aa / 48.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=924 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.7; PDB: 5X07, 7YZE, 7YZF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013638, IPR001766, IPR018533, IPR050211, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cell Junctions | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell junction (GO:0030054)
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 924 |
| PubMed broad count | 1799 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HNF3B, TCF3B |

**关键文献**:
1. FOXA2 promotes metastatic competence in small cell lung cancer.. *Nature communications*. PMID: 40419484
2. Ginger nanoparticles mediated induction of Foxa2 prevents high-fat diet-induced insulin resistance.. *Theranostics*. PMID: 35154496
3. Epididymis-specific lipocalin promoters.. *Asian journal of andrology*. PMID: 17589789
4. Fam3a-mediated prohormone convertase switch in α-cells regulates pancreatic GLP-1 production in an Nr4a2-Foxa2-dependent manner.. *Metabolism: clinical and experimental*. PMID: 39362520
5. FOXA2 prevents hyperbilirubinaemia in acute liver failure by maintaining apical MRP2 expression.. *Gut*. PMID: 35444014

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.7 |
| 高置信度残基 (pLDDT>90) 占比 | 15.3% |
| 置信残基 (pLDDT 70-90) 占比 | 4.6% |
| 中等置信 (pLDDT 50-70) 占比 | 26.7% |
| 低置信 (pLDDT<50) 占比 | 53.4% |
| 有序区域 (pLDDT>70) 占比 | 19.9% |
| 可用 PDB 条目 | 5X07, 7YZE, 7YZF |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=56.7），有序残基占 19.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013638, IPR001766, IPR018533, IPR050211, IPR018122; Pfam: PF00250, PF08430, PF09354 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PDX1 | 0.968 | 0.095 | — |
| ONECUT1 | 0.963 | 0.292 | — |
| SHH | 0.956 | 0.000 | — |
| SOX17 | 0.942 | 0.063 | — |
| RPS6KB1 | 0.919 | 0.000 | — |
| OTX2 | 0.918 | 0.510 | — |
| RPS6KB2 | 0.914 | 0.000 | — |
| HNF1A | 0.899 | 0.000 | — |
| POU5F1 | 0.882 | 0.000 | — |
| HIF1A | 0.880 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Hif1a | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14960|pubmed:20609350 |
| Arnt | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14960|pubmed:20609350 |
| EP300 | psi-mi:"MI:0096"(pull down) | imex:IM-14960|pubmed:20609350 |
| EBI-2895376 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-14960|pubmed:20609350 |
| URS00000A07C1_10090 | psi-mi:"MI:0096"(pull down) | pubmed:29867223|imex:IM-24989 |
| H2az1 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-20542|pubmed:23260146 |
| ENSMUSP00000045918.4 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-20542|pubmed:23260146 |
| Kat5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-20542|pubmed:23260146 |
| Nap1l1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-20542|pubmed:23260146 |
| Smarca4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-20542|pubmed:23260146 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.7 + PDB: 5X07, 7YZE, 7YZF | pLDDT=56.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm, Cell Junctions | 一致 |
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
1. FOXA2 — Hepatocyte nuclear factor 3-beta，研究基础较多，新颖性有限。
2. 蛋白大小457 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 924 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 924 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y261
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125798-FOXA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y261
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
