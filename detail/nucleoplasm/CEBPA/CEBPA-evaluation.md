---
type: protein-evaluation
gene: "CEBPA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CEBPA — REJECTED (研究热度过高 (PubMed strict=1271，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEBPA / CEBP |
| 蛋白名称 | CCAAT/enhancer-binding protein alpha |
| 蛋白大小 | 358 aa / 37.6 kDa |
| UniProt ID | P49715 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 358 aa / 37.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1271 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.7; PDB: 6DC0, 8K8C |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR046347, IPR031106, IPR016468; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Nucleus; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- C/EBP complex (GO:1990647)
- CHOP-C/EBP complex (GO:0036488)
- chromatin (GO:0000785)
- nuclear matrix (GO:0016363)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- Rb-E2F complex (GO:0035189)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1271 |
| PubMed broad count | 2331 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CEBP |

**关键文献**:
1. Hepatocyte-specific CCAAT/enhancer binding protein α restricts liver fibrosis progression.. *The Journal of clinical investigation*. PMID: 38557493
2. R-2HG Exhibits Anti-tumor Activity by Targeting FTO/m(6)A/MYC/CEBPA Signaling.. *Cell*. PMID: 29249359
3. Oncofetal TRIM71 drives liver cancer carcinogenesis through remodeling CEBPA-mediated serine/glycine metabolism.. *Theranostics*. PMID: 39267787
4. Prognostic impact of CEBPA bZIP domain mutation in acute myeloid leukemia.. *Blood advances*. PMID: 34448807
5. Polyploidisation pleiotropically buffers ageing in hepatocytes.. *Journal of hepatology*. PMID: 38583492

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.7 |
| 高置信度残基 (pLDDT>90) 占比 | 18.4% |
| 置信残基 (pLDDT 70-90) 占比 | 13.4% |
| 中等置信 (pLDDT 50-70) 占比 | 27.9% |
| 低置信 (pLDDT<50) 占比 | 40.2% |
| 有序区域 (pLDDT>70) 占比 | 31.8% |
| 可用 PDB 条目 | 6DC0, 8K8C |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.7），有序残基占 31.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347, IPR031106, IPR016468; Pfam: PF07716 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RUNX1 | 0.994 | 0.328 | — |
| CDK2 | 0.992 | 0.644 | — |
| PPARG | 0.991 | 0.045 | — |
| CDK4 | 0.991 | 0.646 | — |
| SPI1 | 0.990 | 0.516 | — |
| CEBPB | 0.990 | 0.623 | — |
| FLT3 | 0.981 | 0.046 | — |
| FOXO1 | 0.975 | 0.094 | — |
| RUNX1T1 | 0.961 | 0.067 | — |
| CDKN1A | 0.956 | 0.299 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000427514.1 | psi-mi:"MI:0413"(electrophoretic mobility shift as | imex:IM-12004|pubmed:17097562 |
| EBI-1172084 | psi-mi:"MI:0413"(electrophoretic mobility shift as | imex:IM-12004|pubmed:17097562 |
| Trib2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12004|pubmed:17097562 |
| C1QBP | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| RASGRF1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SKP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| XRCC6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16490787|imex:IM-19555 |
| PARP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16490787|imex:IM-19555 |
| XRCC5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16490787|imex:IM-19555 |
| ENSMUSP00000096129.5 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-13770|pubmed:20211135 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.7 + PDB: 6DC0, 8K8C | pLDDT=61.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus / Nucleoplasm; 额外: Vesicles | 一致 |
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
1. CEBPA — CCAAT/enhancer-binding protein alpha，研究基础较多，新颖性有限。
2. 蛋白大小358 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1271 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1271 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49715
- Protein Atlas: https://www.proteinatlas.org/ENSG00000245848-CEBPA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEBPA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49715
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
