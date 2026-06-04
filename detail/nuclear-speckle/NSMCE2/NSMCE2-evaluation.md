---
type: protein-evaluation
gene: "NSMCE2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NSMCE2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NSMCE2 / C8orf36, MMS21 |
| 蛋白名称 | E3 SUMO-protein ligase NSE2 |
| 蛋白大小 | 247 aa / 27.9 kDa |
| UniProt ID | Q96MF7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Nucleus; Chromosome, telomere; Nucleus, PML body |
| 蛋白大小 | 10/10 | ×1 | 10 | 247 aa / 27.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=81.7; PDB: 2YU4 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR026846, IPR004181, IPR013083; Pfam: PF11789 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **158.0/180** | |
| **归一化总分** | | | **87.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Supported |
| UniProt | Nucleus; Chromosome, telomere; Nucleus, PML body | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)
- Smc5-Smc6 complex (GO:0030915)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 52 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C8orf36, MMS21 |

**关键文献**:
1. NSMCE2, a novel super-enhancer-regulated gene, is linked to poor prognosis and therapy resistance in breast cancer.. *BMC cancer*. PMID: 36224576
2. Hypomorphism in human NSMCE2 linked to primordial dwarfism and insulin resistance.. *The Journal of clinical investigation*. PMID: 25105364
3. Necdin promotes ubiquitin-dependent degradation of PIAS1 SUMO E3 ligase.. *PloS one*. PMID: 24911587
4. The landscape of 8q24 cytoband in gastric cancer (Review).. *Oncology letters*. PMID: 38464340
5. Identification of BRIP1, NSMCE2, ANAPC7, RAD18 and TTL from chromosome segregation gene set associated with hepatocellular carcinoma.. *Cancer genetics*. PMID: 36126360

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.7 |
| 高置信度残基 (pLDDT>90) 占比 | 53.8% |
| 置信残基 (pLDDT 70-90) 占比 | 25.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.1% |
| 低置信 (pLDDT<50) 占比 | 14.2% |
| 有序区域 (pLDDT>70) 占比 | 79.7% |
| 可用 PDB 条目 | 2YU4 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=81.7，有序区 79.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026846, IPR004181, IPR013083; Pfam: PF11789 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NSMCE3 | 0.999 | 0.996 | — |
| SMC6 | 0.999 | 0.997 | — |
| NSMCE1 | 0.999 | 0.997 | — |
| SMC5 | 0.999 | 0.992 | — |
| EID3 | 0.998 | 0.968 | — |
| NSMCE4A | 0.995 | 0.815 | — |
| UBE2I | 0.965 | 0.516 | — |
| SUMO4 | 0.962 | 0.287 | — |
| SLF2 | 0.883 | 0.610 | — |
| SMC3 | 0.879 | 0.616 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Smc6 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ZNF597 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NSMCE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EID3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TXLNA | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| Rbm8a | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Lck | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SYNCRIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SORT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ILK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 7 / 15 = 47%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 47%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.7 + PDB: 2YU4 | pLDDT=81.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, telomere; Nucleus, PML body / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NSMCE2 — E3 SUMO-protein ligase NSE2，非常新颖，仅有少数基础研究。
2. 蛋白大小247 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96MF7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156831-NSMCE2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NSMCE2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96MF7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
