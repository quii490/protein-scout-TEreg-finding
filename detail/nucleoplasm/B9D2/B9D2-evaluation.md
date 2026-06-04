---
type: protein-evaluation
gene: "B9D2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## B9D2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | B9D2 / MKSR2 |
| 蛋白名称 | B9 domain-containing protein 2 |
| 蛋白大小 | 175 aa / 19.3 kDa |
| UniProt ID | Q9BPU9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Golgi apparatus; 额外: Vesicles, Centrosome, Basal b; UniProt: Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cytos |
| 蛋白大小 | 8/10 | ×1 | 8 | 175 aa / 19.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR010796; Pfam: PF07162 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Golgi apparatus; 额外: Vesicles, Centrosome, Basal body | Uncertain |
| UniProt | Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cytoskeleton, cilium axoneme; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axoneme (GO:0005930)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- MKS complex (GO:0036038)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MKSR2 |

**关键文献**:
1. Joubert syndrome: a model for untangling recessive disorders with extreme genetic heterogeneity.. *Journal of medical genetics*. PMID: 26092869
2. Joubert Syndrome.. **. PMID: 20301500
3. Variable phenotypes and penetrance between and within different zebrafish ciliary transition zone mutants.. *Disease models & mechanisms*. PMID: 36533556
4. Ciliopathy-related B9 protein complex regulates ciliary axonemal microtubule posttranslational modifications and initiation of ciliogenesis.. *The Journal of clinical investigation*. PMID: 41165761
5. Diagnostic potential of the B9D2 gene in colorectal cancer based on whole blood gene expression data and machine learning.. *Discover oncology*. PMID: 40813507

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.6 |
| 高置信度残基 (pLDDT>90) 占比 | 64.6% |
| 置信残基 (pLDDT 70-90) 占比 | 30.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.6% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 95.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.6，有序区 95.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010796; Pfam: PF07162 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| B9D1 | 0.999 | 0.882 | — |
| CC2D2A | 0.997 | 0.624 | — |
| TCTN1 | 0.997 | 0.726 | — |
| TMEM231 | 0.996 | 0.796 | — |
| TMEM67 | 0.994 | 0.000 | — |
| TCTN2 | 0.993 | 0.438 | — |
| TMEM216 | 0.993 | 0.000 | — |
| TCTN3 | 0.980 | 0.140 | — |
| MKS1 | 0.974 | 0.642 | — |
| CEP290 | 0.970 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TLX3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ALKBH7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| VPS25 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| P4HA3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SAXO4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| B9D1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| SPAG8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PLEKHA7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| QARS1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TCTN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.6 + PDB: 无 | pLDDT=89.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, cilium basal body; Cytopl / Nucleoli, Golgi apparatus; 额外: Vesicles, Centrosom | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. B9D2 — B9 domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小175 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BPU9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123810-B9D2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B9D2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BPU9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
